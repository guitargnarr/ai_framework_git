#!/usr/bin/env python3
"""
System Inventory Oracle - Fast JSON inventory queries + Deployment Readiness Analysis
Uses ollama Python library for clean output (no CLI ANSI codes)
Based on mirador.py pattern - Demonstrates Tabula Rasa + Specialist Model approach
"""

import ollama
import json
import sys
import os
import subprocess
from pathlib import Path
from datetime import datetime


def strip_markdown(text: str) -> str:
    """Remove markdown code block wrapper if present"""
    text = text.strip()
    if text.startswith('```'):
        lines = text.split('\n')
        lines = lines[1:]  # Remove ```json or ```
        if lines and lines[-1].strip() == '```':
            lines = lines[:-1]
        return '\n'.join(lines).strip()
    return text


def extract_json(text: str) -> str:
    """Extract first valid JSON object from text (handles prose before/after)"""
    text = strip_markdown(text)

    # Find first { and last }
    start = text.find('{')
    if start == -1:
        return text

    # Find matching closing brace
    depth = 0
    for i in range(start, len(text)):
        if text[i] == '{':
            depth += 1
        elif text[i] == '}':
            depth -= 1
            if depth == 0:
                return text[start:i+1]

    return text


def query_inventory(query_type: str) -> dict:
    """Query system inventory oracle, return clean JSON"""
    try:
        response = ollama.generate(
            model='system_inventory_oracle',
            prompt=query_type,
            options={'temperature': 0.0, 'num_predict': 500}
        )

        output = strip_markdown(response['response'])
        return json.loads(output)

    except json.JSONDecodeError as e:
        return {"error": "json_parse_error", "message": str(e)}
    except Exception as e:
        return {"error": "query_failed", "message": str(e)}


def find_repo(repo_name: str) -> Path:
    """
    Find repository in common locations

    Args:
        repo_name: Repository name (e.g., "reflexia", "phishguard")

    Returns:
        Path: Absolute path to repository

    Raises:
        FileNotFoundError: If repository not found
    """
    # Common search locations
    search_paths = [
        Path.home() / "Projects" / repo_name,
        Path.home() / "Projects" / "Security-Tools" / repo_name,
        Path.home() / "Projects" / "Web-Development" / repo_name,
        Path.home() / "Projects" / "Career-Business" / repo_name,
        Path.home() / repo_name,
        Path(repo_name)  # Try as-is (if full path)
    ]

    # Fuzzy search (case-insensitive, partial match)
    for base in [Path.home() / "Projects", Path.home() / "Projects" / "Security-Tools"]:
        if base.exists():
            for item in base.iterdir():
                if item.is_dir() and repo_name.lower() in item.name.lower():
                    return item

    # Exact matches
    for path in search_paths:
        if path.exists() and path.is_dir():
            return path

    raise FileNotFoundError(f"Repository '{repo_name}' not found in common locations")


def collect_deployment_signals(repo_path: Path) -> dict:
    """
    Collect high-signal deployment indicators (no source code)
    Target: <2KB context for small model

    Args:
        repo_path: Path to repository

    Returns:
        dict: Deployment signals
    """
    signals = {}

    # Root files (names only, not content)
    signals['root_files'] = [f.name for f in repo_path.iterdir() if f.is_file()]

    # Deployment configs (full content - these are small)
    for config in ['Dockerfile', 'railway.json', 'render.yaml', 'vercel.json', 'netlify.toml', 'docker-compose.yml']:
        config_path = repo_path / config
        if config_path.exists():
            try:
                signals[config] = config_path.read_text()[:1000]  # Max 1KB per file
            except:
                signals[config] = "exists_but_unreadable"

    # Dependencies
    if (repo_path / 'requirements.txt').exists():
        signals['requirements.txt'] = (repo_path / 'requirements.txt').read_text()[:500]

    if (repo_path / 'package.json').exists():
        try:
            pkg = json.loads((repo_path / 'package.json').read_text())
            signals['scripts'] = pkg.get('scripts', {})
            signals['dependencies_count'] = len(pkg.get('dependencies', {}))
        except:
            signals['package.json'] = "exists_but_invalid"

    # Quality indicators (existence checks only)
    signals['has_tests'] = (repo_path / 'tests').exists() or (repo_path / '__tests__').exists() or (repo_path / 'test').exists()
    signals['has_ci'] = (repo_path / '.github' / 'workflows').exists()
    signals['has_readme'] = (repo_path / 'README.md').exists()
    signals['has_license'] = (repo_path / 'LICENSE').exists() or (repo_path / 'LICENSE.md').exists()
    signals['has_dockerignore'] = (repo_path / '.dockerignore').exists()

    # Git state
    try:
        git_status = subprocess.check_output(
            ['git', 'status', '--porcelain'],
            cwd=repo_path,
            stderr=subprocess.DEVNULL
        ).decode()
        signals['git_clean'] = len(git_status.strip()) == 0
        signals['uncommitted_files'] = len(git_status.strip().split('\n')) if git_status.strip() else 0

        git_remote = subprocess.check_output(
            ['git', 'remote', '-v'],
            cwd=repo_path,
            stderr=subprocess.DEVNULL
        ).decode()
        signals['has_remote'] = 'github.com' in git_remote or 'gitlab' in git_remote
    except:
        signals['git_clean'] = False
        signals['has_remote'] = False

    return signals


def assess_readiness(repo_name: str) -> dict:
    """
    Assess deployment readiness of repository

    Args:
        repo_name: Repository name or path

    Returns:
        dict: Readiness scorecard with grade and recommendations
    """
    try:
        # Find repository
        repo_path = find_repo(repo_name)

        # Collect signals
        signals = collect_deployment_signals(repo_path)

        # Build analysis prompt
        prompt = f"""Analyze deployment readiness for repository.

DEPLOYMENT SIGNALS:
{json.dumps(signals, indent=2)}

Return readiness scorecard in strict JSON format."""

        # Query readiness analyzer
        response = ollama.generate(
            model='deployment_readiness_analyzer',
            prompt=prompt,
            options={'temperature': 0.0, 'num_predict': 800}
        )

        # Parse response (extract JSON, ignore prose)
        output = extract_json(response['response'])
        scorecard = json.loads(output)

        # Add metadata
        scorecard['repo_analyzed'] = repo_name
        scorecard['repo_path'] = str(repo_path)
        scorecard['analyzed_at'] = datetime.now().isoformat()

        return scorecard

    except FileNotFoundError as e:
        return {
            "error": "repo_not_found",
            "message": str(e),
            "searched_for": repo_name
        }
    except json.JSONDecodeError as e:
        return {
            "error": "invalid_json_from_model",
            "message": str(e),
            "raw_output": output[:300] if 'output' in locals() else "no output"
        }
    except Exception as e:
        return {
            "error": "analysis_failed",
            "message": str(e)
        }


def main():
    if len(sys.argv) < 2:
        print(json.dumps({
            "error": "missing_command",
            "usage": "inventory_oracle.py [COMMAND] [ARGS]",
            "commands": {
                "deployments": "List all deployed platforms",
                "find NAME": "Locate specific project",
                "count TYPE": "Count resources",
                "platforms": "List deployment platforms used",
                "readiness REPO": "Assess deployment readiness of repository"
            },
            "examples": [
                "inventory_oracle.py deployments",
                "inventory_oracle.py find phishguard",
                "inventory_oracle.py readiness reflexia",
                "inventory_oracle.py readiness ~/Projects/my-repo"
            ]
        }, indent=2))
        sys.exit(1)

    command = sys.argv[1]

    # Route to appropriate handler
    if command == "readiness" and len(sys.argv) >= 3:
        repo_name = sys.argv[2]
        result = assess_readiness(repo_name)
    else:
        # Default: pass full query to inventory oracle
        query = ' '.join(sys.argv[1:])
        result = query_inventory(query)

    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
