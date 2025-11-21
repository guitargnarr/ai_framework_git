#!/usr/bin/env python3
"""
Mirador AI Orchestration Framework
Personal Life Opportunity Identification System
WITH ENHANCED ERROR HANDLING AND RETRY LOGIC
"""

import argparse
import json
import requests
import sys
import time
from datetime import datetime
from pathlib import Path
import subprocess

class MiradorOrchestrator:
    def __init__(self):
        self.ollama_url = "http://localhost:11434"
        self.output_dir = Path.home() / "ai_framework_git" / "outputs"
        self.context_dir = Path.home() / "ai_framework_git" / "context"
        self.timeout = 120
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.user_context = self.load_context()

    def load_context(self):
        """Load user context from JSON (graceful fallback)"""
        context_file = self.context_dir / "user_profile.json"
        try:
            if context_file.exists():
                with open(context_file, 'r') as f:
                    return json.load(f)
        except Exception as e:
            print(f"⚠️ Context load failed: {e}")
        return {}  # Empty dict if missing/broken

    def format_context_string(self):
        """Format context for injection into prompts"""
        if not self.user_context:
            return ""

        ctx = self.user_context
        parts = ["\n--- USER CONTEXT ---"]

        if 'location' in ctx:
            parts.append(f"Location: {ctx['location'].get('city')}, {ctx['location'].get('state')}")

        if 'professional' in ctx:
            parts.append(f"Role: {ctx['professional'].get('role')}")
            parts.append(f"Focus: {ctx['professional'].get('work_mode')}")

        if 'goals' in ctx and 'short_term' in ctx['goals']:
            parts.append(f"Goals: {', '.join(ctx['goals']['short_term'])}")

        parts.append("--- END CONTEXT ---\n")
        return '\n'.join(parts)

    def list_models(self):
        """List all available Ollama models"""
        try:
            response = requests.get(f"{self.ollama_url}/api/tags")
            if response.status_code == 200:
                models = response.json()
                print("Available Models:")
                for model in models.get('models', []):
                    print(f"  - {model['name']}")
                return True
        except Exception as e:
            print(f"Error connecting to Ollama: {e}")
            return False

    def query_model(self, model_name, prompt, context="", max_retries=3, inject_user_context=True):
        """Query a single model with retry logic and validation"""
        # Inject user context if enabled
        if inject_user_context:
            user_ctx = self.format_context_string()
            prompt = f"{user_ctx}\n{prompt}" if user_ctx else prompt

        full_prompt = f"{context}\n\n{prompt}" if context else prompt

        for attempt in range(max_retries):
            try:
                payload = {
                    "model": model_name,
                    "prompt": full_prompt,
                    "stream": False
                }

                print(f"Querying {model_name}... (attempt {attempt + 1}/{max_retries})")
                start_time = time.time()

                response = requests.post(
                    f"{self.ollama_url}/api/generate",
                    json=payload,
                    timeout=self.timeout
                )

                end_time = time.time()
                duration = end_time - start_time

                if response.status_code == 200:
                    result = response.json()
                    response_text = result.get('response', '')

                    # Validate meaningful response (>50 characters minimum)
                    if len(response_text.strip()) > 50:
                        print(f"✓ {model_name} completed ({duration:.0f}s, {len(response_text.split())} words)")
                        return response_text
                    else:
                        print(f"⚠ {model_name} returned short response ({len(response_text)} chars), retrying...")
                        if attempt < max_retries - 1:
                            time.sleep(2)  # Brief pause before retry
                            continue
                else:
                    print(f"⚠ HTTP {response.status_code}, retrying...")
                    if attempt < max_retries - 1:
                        time.sleep(2)
                        continue

            except requests.exceptions.Timeout:
                print(f"⚠ {model_name} timeout after {self.timeout}s (attempt {attempt + 1}), retrying...")
                if attempt < max_retries - 1:
                    time.sleep(3)  # Longer pause after timeout
                    continue
            except Exception as e:
                print(f"⚠ Error with {model_name}: {e}")
                if attempt == max_retries - 1:
                    return f"Error: Failed to get response from {model_name} after {max_retries} attempts: {str(e)}"
                time.sleep(2)
                continue

        return f"Error: {model_name} failed after {max_retries} attempts"

    def run_chain(self, task, models):
        """Execute a chain of models"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        chain_dir = self.output_dir / f"chain_{timestamp}"
        chain_dir.mkdir(parents=True, exist_ok=True)

        print(f"\n{'=' * 60}")
        print(f"Running chain with {len(models)} models")
        print(f"Task: {task}")
        print(f"Models: {', '.join(models)}")
        print(f"Output: {chain_dir}")
        print(f"{'=' * 60}\n")

        context = f"Task: {task}"
        all_outputs = []
        failed_models = []

        for i, model in enumerate(models, 1):
            print(f"\n[Step {i}/{len(models)}] Running {model}")
            print("-" * 50)

            # Create step-specific prompt
            if i == 1:
                prompt = f"Task: {task}\n\nPlease provide comprehensive analysis and recommendations."
            else:
                prompt = f"Building on the previous analysis, please enhance and expand with additional insights:\n\nPrevious analysis: {context[-1000:]}\n\nTask: {task}"

            # Query model with retry logic
            result = self.query_model(model, prompt)

            if result and not result.startswith("Error:"):
                # Save individual output
                step_file = chain_dir / f"step{i:02d}_{model.replace(':', '_')}.txt"
                with open(step_file, 'w') as f:
                    f.write(f"Model: {model}\n")
                    f.write(f"Timestamp: {datetime.now().isoformat()}\n")
                    f.write("-" * 60 + "\n\n")
                    f.write(result)

                all_outputs.append({
                    'step': i,
                    'model': model,
                    'output': result,
                    'word_count': len(result.split()),
                    'char_count': len(result),
                    'status': 'success'
                })

                context += f"\n\n=== {model.upper()} ANALYSIS ===\n{result}"

                print(f"✓ Step {i} complete: {len(result.split())} words")
            else:
                print(f"✗ Step {i} failed: {model}")
                failed_models.append(model)
                all_outputs.append({
                    'step': i,
                    'model': model,
                    'output': result if result else "No output received",
                    'word_count': 0,
                    'status': 'failed'
                })

        # Create comprehensive summary
        summary_content = self._create_summary(task, timestamp, models, all_outputs, failed_models)

        summary_file = chain_dir / "summary.md"
        with open(summary_file, 'w') as f:
            f.write(summary_content)

        # Create metadata
        metadata = {
            'task': task,
            'timestamp': timestamp,
            'models': models,
            'total_models': len(models),
            'successful_models': len([o for o in all_outputs if o['status'] == 'success']),
            'failed_models': failed_models,
            'total_words': sum(o.get('word_count', 0) for o in all_outputs),
            'chain_dir': str(chain_dir)
        }

        metadata_file = chain_dir / "metadata.json"
        with open(metadata_file, 'w') as f:
            json.dump(metadata, f, indent=2)

        # Print results
        print(f"\n{'=' * 60}")
        print(f"Chain execution complete!")
        print(f"{'=' * 60}")
        print(f"✓ Success: {metadata['successful_models']}/{metadata['total_models']} models")
        if failed_models:
            print(f"✗ Failed: {', '.join(failed_models)}")
        print(f"📊 Total output: {metadata['total_words']} words")
        print(f"📁 Results: {chain_dir}")
        print(f"📄 Summary: {summary_file}")
        print(f"{'=' * 60}\n")

        return chain_dir

    def _create_summary(self, task, timestamp, models, outputs, failed):
        """Create formatted summary markdown"""
        summary = f"# Mirador Chain Analysis Summary\n\n"
        summary += f"**Task:** {task}\n"
        summary += f"**Timestamp:** {timestamp}\n"
        summary += f"**Models Used:** {', '.join(models)}\n"
        summary += f"**Success Rate:** {len([o for o in outputs if o['status'] == 'success'])}/{len(models)}\n"
        if failed:
            summary += f"**Failed Models:** {', '.join(failed)}\n"
        summary += "\n---\n\n"

        for output in outputs:
            if output['status'] == 'success':
                summary += f"## Step {output['step']}: {output['model'].upper()}\n\n"
                summary += f"**Output:** {output['word_count']} words\n\n"
                summary += f"{output['output']}\n\n"
                summary += "---\n\n"
            else:
                summary += f"## Step {output['step']}: {output['model'].upper()} (FAILED)\n\n"
                summary += f"**Error:** {output['output']}\n\n"
                summary += "---\n\n"

        return summary

def main():
    parser = argparse.ArgumentParser(
        description="Mirador AI Orchestration Framework with Enhanced Error Handling",
        epilog="Examples:\n"
               "  mirador-ez models\n"
               "  mirador-ez ask financial_planning_expert_v5 'Budget analysis'\n"
               "  mirador-ez chain 'Career planning' model1 model2 model3\n",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # Models command
    models_parser = subparsers.add_parser('models', help='List available models')

    # Ask command
    ask_parser = subparsers.add_parser('ask', help='Query a single model')
    ask_parser.add_argument('model', help='Model name')
    ask_parser.add_argument('prompt', help='Prompt/question')

    # Chain command
    chain_parser = subparsers.add_parser('chain', help='Run model chain')
    chain_parser.add_argument('task', help='Task description')
    chain_parser.add_argument('models', nargs='+', help='Models to chain')

    args = parser.parse_args()

    orchestrator = MiradorOrchestrator()

    if args.command == 'models':
        orchestrator.list_models()
    elif args.command == 'ask':
        result = orchestrator.query_model(args.model, args.prompt)
        if result:
            print(f"\n{'-' * 60}")
            print(f"Response from {args.model}:")
            print(f"{'-' * 60}\n")
            print(result)
            print()
    elif args.command == 'chain':
        orchestrator.run_chain(args.task, args.models)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
