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

### Deployment Tools (Nov 22, 2025)

**Readiness Assessment** (Hybrid: Python scoring + rule-based logic):
```bash
# Assess any repo for deployment readiness
python3 inventory_oracle.py readiness REPO_NAME

# Returns: score (0-100), grade (A-F), platform, deploy time estimate
# Example: python3 inventory_oracle.py readiness reflexia
# Output: {"score": 85, "grade": "B+", "platform": "railway", "time": 15}

# Scoring is deterministic (Python math, not AI):
# - Infrastructure: Dockerfile(20), platform config(10), etc.
# - Quality: tests(10), CI/CD(10), git clean(5)
# - Documentation: README(10), LICENSE(5)
# - Deployability: git remote(5), build scripts(5)
```

**Code Generation** (B+ quality, needs human QA):
```bash
# Generate Next.js 14 + TypeScript + Shadcn components
ollama run elite-frontend "Create a responsive navbar"

# Quality: B+ (85% time savings, 2 min human fixes needed)
# Fixes needed: Import corrections (Icon → specific lucide icons)
# Use for: Component scaffolding, not production-final code
# Stack: Next.js 14 App Router, TypeScript strict, Tailwind, Shadcn/UI
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

## The Merry Go Round Protocol

**Definition**: Continuous cycle of context injection → blank slate chains → result refinement

**The Cycle**:
```
1. Edit context/user_profile.json (update goals, skills, priorities)
   ↓
2. Run blank slate chain (models see fresh context)
   ↓
3. Execute generated actions (real-world results)
   ↓
4. Refine context based on outcomes
   ↓
LOOP: Return to step 1 (context evolves, models stay timeless)
```

**Commands**:
```bash
# Update context
nano context/user_profile.json

# Run with context injection
python3 mirador.py ask financial_calculator "Your question"
# Context auto-injected from user_profile.json

# Run without context (pure blank slate)
python3 -c "
from mirador import MiradorOrchestrator
m = MiradorOrchestrator()
result = m.query_model('financial_calculator', 'Question', inject_user_context=False)
print(result)
"

# Generate daily action (uses context)
python3 mirador_actionable.py generate
```

**Why this works**: Models = timeless specialists. Context = current reality. Updates happen in JSON, not modelfiles.

---

## Critical Rules

**Tabula Rasa Law**: NEVER bake personal context into modelfiles. Update `context/user_profile.json`, not system prompts.

**Quality Before Deployment**:
- Test repos before deploying (check what they do, who needs them)
- Don't ship blindly because Oracle says "B+" - understand the value first
- Deployment Oracle scores deployability, not usefulness
- You decide what's valuable, Oracle decides what's deployable

**AI + Python Hybrid Pattern** (Nov 22, 2025):
- Use AI for: qualitative tasks (code generation, recommendations)
- Use Python for: quantitative tasks (scoring, math, logic)
- Don't use AI for static inventory (CLI tools + JSON is simpler)
- Small models can't do arithmetic reliably (hybrid scoring proven)

**Deployment Pattern**:
- Railway: Dockerfile + Python/FastAPI (PORT from env, health endpoint)
- Vercel: Next.js/React (package.json with build script)
- Netlify: Static sites (HTML/markdown)
- Template: `~/.claude/templates/deploy-railway.md`

---

## Legacy References

**Old repo**: https://github.com/guitargnarr/mirador (DEPRECATED, Grade F)
**This repo**: Clean phoenix, Tabula Rasa architecture, production-ready

**Philosophy**: @~/.claude/context/working-philosophy.md
