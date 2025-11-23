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


def calculate_score_deterministic(signals: dict) -> dict:
    """
    Calculate deployment readiness score using deterministic Python logic
    (Small models can't do arithmetic - we do it for them)

    Args:
        signals: Deployment signals from collect_deployment_signals()

    Returns:
        dict: Score, grade, and breakdown
    """
    breakdown = {
        'infrastructure': 0,
        'quality': 0,
        'documentation': 0,
        'deployability': 0
    }

    # Infrastructure (40 points max)
    if 'Dockerfile' in signals:
        breakdown['infrastructure'] += 20
    if any(k in signals for k in ['railway.json', 'render.yaml', 'vercel.json', 'netlify.toml']):
        breakdown['infrastructure'] += 10
    if any(k in signals for k in ['docker-compose.yml', '.dockerignore']):
        breakdown['infrastructure'] += 5
    # Assume basic env handling if has requirements/package.json
    if 'requirements.txt' in signals or 'package.json' in signals:
        breakdown['infrastructure'] += 5

    # Quality (30 points max)
    if signals.get('has_tests'):
        breakdown['quality'] += 10
    if signals.get('has_ci'):
        breakdown['quality'] += 10
    if signals.get('git_clean'):
        breakdown['quality'] += 5
    # Check for linting configs
    lint_files = ['.eslintrc', '.eslintrc.json', '.flake8', 'pylintrc', '.prettierrc', 'pytest.ini']
    if any(f in signals.get('root_files', []) for f in lint_files):
        breakdown['quality'] += 5

    # Documentation (20 points max)
    if signals.get('has_readme'):
        breakdown['documentation'] += 10
    if signals.get('has_license'):
        breakdown['documentation'] += 5
    if 'requirements.txt' in signals or signals.get('scripts'):
        breakdown['documentation'] += 5

    # Deployability (10 points max)
    if signals.get('has_remote'):
        breakdown['deployability'] += 5
    if signals.get('scripts') or 'requirements.txt' in signals:
        breakdown['deployability'] += 5

    # Calculate total
    score = sum(breakdown.values())

    # Determine grade
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B+"
    elif score >= 70:
        grade = "B"
    elif score >= 60:
        grade = "C"
    else:
        grade = "F"

    # Check for critical blockers
    has_critical_blockers = False
    missing_critical = []

    if 'Dockerfile' not in signals and not any(k in signals for k in ['railway.json', 'render.yaml', 'vercel.json', 'netlify.toml']):
        has_critical_blockers = True
        missing_critical.append("No Dockerfile OR platform config (cannot deploy)")

    if 'requirements.txt' not in signals and 'package.json' not in signals:
        has_critical_blockers = True
        missing_critical.append("No dependencies file")

    if not signals.get('has_remote'):
        has_critical_blockers = True
        missing_critical.append("No git remote (cannot auto-deploy)")

    # Override grade if critical blockers
    if has_critical_blockers:
        grade = "F"
        score = min(score, 50)  # Cap at 50 if critical blockers

    return {
        'score': score,
        'grade': grade,
        'breakdown': breakdown,
        'has_critical_blockers': has_critical_blockers,
        'missing_critical': missing_critical
    }


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

        # Calculate score deterministically (Python does the math)
        scoring = calculate_score_deterministic(signals)

        # Determine recommended platform (rule-based)
        if 'Dockerfile' in signals and 'requirements.txt' in signals:
            platform = 'railway'
        elif signals.get('scripts') and 'package.json' in signals:
            if 'next' in str(signals.get('scripts', {})).lower() or 'react' in str(signals.get('scripts', {})).lower():
                platform = 'vercel'
            else:
                platform = 'railway'
        elif signals.get('has_readme') and not any(k in signals for k in ['Dockerfile', 'package.json', 'requirements.txt']):
            platform = 'netlify'
        else:
            platform = 'railway'

        # Determine deployment readiness
        deployment_ready = scoring['score'] >= 70 and not scoring['has_critical_blockers']

        # Estimate deploy time
        if scoring['score'] >= 90:
            est_time = 10
        elif scoring['score'] >= 80:
            est_time = 15
        elif scoring['score'] >= 70:
            est_time = 30
        else:
            est_time = 60

        # Build missing_recommended list
        missing_recommended = []
        if not signals.get('has_tests'):
            missing_recommended.append('tests')
        if not signals.get('has_ci'):
            missing_recommended.append('ci_cd')
        if not signals.get('has_license'):
            missing_recommended.append('LICENSE')
        if not signals.get('git_clean'):
            missing_recommended.append('commit_changes')

        # Generate next action
        if scoring['has_critical_blockers']:
            next_action = f"Fix critical: {', '.join(scoring['missing_critical'])}"
        elif deployment_ready:
            next_action = f"Deploy to {platform}" + (f" (add {missing_recommended[0]} first)" if missing_recommended else "")
        else:
            next_action = f"Add {', '.join(missing_recommended[:2])}, then deploy"

        # Build scorecard
        scorecard = {
            **scoring,  # score, grade, breakdown, has_critical_blockers, missing_critical
            'missing_recommended': missing_recommended,
            'deployment_ready': deployment_ready,
            'recommended_platform': platform,
            'estimated_deploy_time_minutes': est_time,
            'next_action': next_action,
            'repo_analyzed': repo_name,
            'repo_path': str(repo_path),
            'analyzed_at': datetime.now().isoformat(),
            'scoring_method': 'hybrid_deterministic_v1'
        }

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
