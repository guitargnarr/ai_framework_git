# Mirador AI Orchestration - Phoenix Edition

**Updated**: November 21, 2025
**Focus**: Value creation via apply/fix/scale/deploy/sell/automate

---

## Quick Start

### Daily Action Generation
```bash
python3 mirador_actionable.py generate
cat daily_actions/daily_action_$(date +%Y-%m-%d).md
```

### Model Health Check
```bash
./scripts/model_health_check.sh
```

### Chain Execution
```bash
python3 mirador.py chain "Your prompt" opportunity_identification_specialist instruction_generation_specialist
```

---

## Installation

### Dependencies
```bash
# Install mirador-core utilities
pip install lib/mirador_core-2.1.2-py3-none-any.whl

# Verify
python3 -c "from mirador_core.error_handling import ChainExecutor; print('✅ mirador-core ready')"

# Install other dependencies
pip install rich pandas pyyaml requests
```

### Specialist Models (3 core)
```bash
ollama list | grep specialist
# Expected:
# - opportunity_identification_specialist
# - instruction_generation_specialist
# - fact_validation_specialist
```

---

## Architecture

**Core Engine**: mirador-core 2.1.2 (Python utilities)
- ChainExecutor: Retry logic, error handling
- CircuitBreaker: Failure protection
- ConstraintValidator: Output validation
- ContextManager: State management

**Orchestration**: mirador.py (enhanced shell wrapper)
- 3-attempt retry with backoff
- Response validation (>50 chars)
- Graceful degradation (works with partial model availability)

**Systems**:
1. Daily actions (`mirador_actionable.py`)
2. Opportunity scoring (`mirador_action_prioritizer.py`)
3. Fact validation (`mirador_fact_validator.py`)
4. Health monitoring (`scripts/model_health_check.sh`)

---

## Agent Library (80 modelfiles)

### Value Creation (Phoenix-Capable) ✅
- opportunity_analyst.modelfile
- sales_content_creator.modelfile
- digital_asset_curator.modelfile
- financial_planning_expert_v*.modelfile
- content_strategist_pro.modelfile
- creative_entrepreneur.modelfile
- side_income_opportunity_scout.modelfile

### Technical ✅
- code_reviewer.modelfile
- ux_designer.modelfile
- solution_architect.modelfile
- master_coder.modelfile

### Music/Creative ✅
- guitar_expert.modelfile
- master_guitar_instructor.modelfile
- touring_readiness_coach.modelfile
- audio_production_strategist.modelfile
- performance_anxiety_coach.modelfile

### Personal Context (Archive)
- matthew_context_provider_*.modelfile (personal history)
- matthew_advisor_*.modelfile (career specific)
- matthew_parenting_*.modelfile (family context)
- father_daughter_*.modelfile (parenting)

**Total**: 80 modelfiles (cleaned from 189 in legacy repo)

---

## Commands

### Core
```bash
# Generate daily action
python3 mirador_actionable.py generate

# Check model health
./scripts/model_health_check.sh

# Run chain
python3 mirador.py chain "prompt" model1 model2

# Score opportunity
python3 mirador_action_prioritizer.py add --title "Task" --financial-impact 8 --time-efficiency 7
```

### Testing
```bash
# Test core utilities
python3 -c "from mirador_core.error_handling import ChainExecutor; print('OK')"

# Test action generation
python3 test_mirador_actionable.py

# Test fact validation
python3 test_fact_validation.py

# Test prioritization
python3 test_action_prioritizer.py
```

---

## Pattern Learning Integration

After using daily actions:
```bash
# Record outcomes
python3 mirador_actionable.py complete 2025-11-21 --outcome "Result" --time 45 --value "High"

# Patterns stored in: ~/ai_framework_git/mirador_actions.db
```

---

## Development

### Creating New Agents
```bash
cd modelfiles
cat > new_agent.modelfile << 'EOF'
FROM llama3.2:latest
PARAMETER temperature 0.7
SYSTEM """Your system prompt here"""
EOF

ollama create new_agent -f new_agent.modelfile
```

### Health Monitoring
```bash
# Weekly check
./scripts/model_health_check.sh

# Results in: health_check_log.txt
```

---

## Critical Notes

- **No corporate context** (Humana references removed)
- **Focus**: Value creation (apply/fix/scale/deploy/sell/automate)
- **mirador-core 2.1.2**: Pre-built utilities (error handling, validation)
- **Ollama required**: All models run locally
- **Graceful degradation**: Works with 3/5 models if some unavailable

---

## Legacy References

**Old repo**: https://github.com/guitargnarr/mirador (DEPRECATED, Grade F)
**This repo**: Clean phoenix, value-focused, production-ready

**Philosophy**: @~/.claude/context/working-philosophy.md
