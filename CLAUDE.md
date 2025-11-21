# AI Framework Project Context

**Last Updated**: November 20, 2025
**Session Type**: Parallel Development Execution

## Project Overview
Universal AI Model System - Creates specialized Ollama models for different domains

## Current State (Nov 20)
- ✅ Git repository initialized
- ✅ 4 parallel worktrees created (no conflicts)
- ✅ Task specifications written
- ✅ Ready for parallel execution

## Worktree Structure
```
~/ai_framework_worktrees/
├── core-framework/       # Base classes, config, model manager
├── training-pipeline/    # Fine-tuning, prompt engineering, model builder
├── runtime-deployment/   # Ollama interface, inference, API server
└── docs-and-tests/      # README, tests, examples
```

## Execution Options
1. **Parallel (4 terminals)**: Open 4 Claude instances, paste task specs
2. **Sequential (this session)**: Build each worktree one by one
3. **Skeleton Crew**: Just essentials (30 min MVP)

## Task Files
- TASK_1_CORE_FRAMEWORK.md
- TASK_2_TRAINING_PIPELINE.md
- TASK_3_RUNTIME_DEPLOYMENT.md
- TASK_4_DOCS_AND_TESTS.md

## Universal Models to Support
1. universal_music_mentor
2. universal_creative_catalyst
3. universal_career_strategist
4. universal_financial_advisor
5. universal_corporate_navigator
6. universal_relationship_harmony
7. universal_health_wellness
8. universal_louisville_expert

## Key Decisions
- Use dataclasses for configuration
- Type hints throughout
- Ollama modelfile format compatibility
- SQLite for chain_memory.db
- FastAPI for model server

## Commands
```bash
# Check status
git worktree list

# After completion, merge all
git merge core-framework
git merge training-pipeline
git merge runtime-deployment
git merge docs-and-tests

# Clean up
git worktree prune
```

## Philosophy
This is the meta-system - it creates the creators. Each universal model can spawn unlimited specialized variants.