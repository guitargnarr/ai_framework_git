# Mirador Phoenix - Handoff Instructions

**System**: Tabula Rasa AI orchestration with context injection
**Updated**: November 21, 2025
**For**: Future sessions or new users

---

## Quick Start (5 Minutes)

```bash
cd ~/ai_framework_git
source venv/bin/activate  # Or: python3 -m venv venv && source venv/bin/activate
python3 mirador_actionable.py generate
cat daily_actions/daily_action_$(date +%Y-%m-%d).md
```

**Result**: Daily high-value action generated from blank slate models + your context

---

## Setup: Edit Your Context

### 1. Open Context File
```bash
nano context/user_profile.json
```

### 2. Update Sections

**Location** (where you live/work):
```json
"location": {
  "city": "Louisville",
  "state": "KY",
  "county": "Jefferson"
}
```

**Financial** (goals, income model):
```json
"financial": {
  "income_model": "consulting_variable",
  "focus_areas": ["reduce_expenses", "increase_passive_income"],
  "debt_priorities": ["mortgage_optimization"]
}
```

**Professional** (skills, platforms, focus):
```json
"professional": {
  "role": "AI-native developer",
  "core_skills": ["Python", "React", "AI orchestration"],
  "platforms": ["guitar.projectlavos.com", "ai_framework_git"],
  "work_mode": "apply_fix_scale_deploy_sell_automate"
}
```

**Goals** (short/medium/long term):
```json
"goals": {
  "short_term": ["vet_24_github_repos", "deploy_platforms"],
  "medium_term": ["consulting_clients", "platform_adoption"],
  "long_term": ["sustainable_income", "methodology_teaching"]
}
```

### 3. Save and Verify
```bash
# Verify JSON is valid
python3 -c "import json; json.load(open('context/user_profile.json')); print('✅ Context valid')"
```

---

## Execution: Run Blank Slate Chains

### Single Model Query
```bash
# With context injection (default)
python3 mirador.py ask financial_calculator "Calculate savings: $500/mo at 7% for 10 years"

# Without context (pure blank slate)
python3 mirador.py ask financial_calculator "Calculate..." --no-context
# Note: --no-context flag not implemented yet, use Python directly for now
```

### Multi-Model Chain
```bash
# 3-model chain example
python3 mirador.py chain "Find cost reduction opportunities" \
  research_analyst \
  financial_calculator \
  action_builder
```

### Daily Action Generation (5-model chain)
```bash
python3 mirador_actionable.py generate
# Uses: opportunity_identification → louisville_expert → financial_planning → instruction → validation

# View output
cat daily_actions/daily_action_$(date +%Y-%m-%d).md

# Mark complete (records outcome for pattern learning)
python3 mirador_actionable.py complete 2025-11-21 --time 45 --outcome "Executed" --value "High"
```

---

## Expansion: Build New Chains

### Create New Blank Slate Model

**Step 1**: Write modelfile
```bash
cd modelfiles
cat > your_new_model.modelfile << 'EOF'
FROM llama3.2:latest

PARAMETER temperature 0.3
PARAMETER top_p 0.9
PARAMETER num_predict 1000

SYSTEM """You are a [SPECIALIST TYPE].

Your function: [WHAT IT DOES]

You do NOT:
- Give generic advice
- Assume user context (context will be provided)
- Make recommendations outside your specialty

You DO:
- [Specific capability 1]
- [Specific capability 2]
- [Specific capability 3]

Output: [FORMAT - tables, lists, structured data, etc.]"""
EOF
```

**Step 2**: Create model
```bash
ollama create your_new_model -f your_new_model.modelfile
```

**Step 3**: Test
```bash
python3 mirador.py ask your_new_model "Test question"
# Verify context injected automatically
```

### Design New Chain

**Example: Content Factory Chain**
```python
# In mirador.py or new script
chain = [
    "market_researcher",      # Find trending topics
    "content_strategist",     # Plan content series
    "copywriter",             # Write engaging copy
    "seo_optimizer",          # Optimize for search
    "publication_planner"     # Schedule and distribute
]

result = orchestrator.run_chain("Create content for guitar platform", chain)
```

**Example: Deal Hunter Chain**
```python
chain = [
    "opportunity_scanner",    # Find potential deals
    "due_diligence_analyst", # Analyze viability
    "financial_calculator",   # Calculate ROI
    "negotiation_strategist", # Plan approach
    "contract_reviewer"       # Verify terms
]

result = orchestrator.run_chain("Find acquisition opportunities in Louisville", chain)
```

---

## The Merry Go Round

**Week 1**: Run daily actions → Execute → Record outcomes
**Week 2**: Update context/user_profile.json with new goals/skills
**Week 3**: Models see fresh context → Generate better actions
**Week 4**: Pattern learning shows improvement

**The loop**: Context evolves → Models adapt → Results improve → Context evolves

---

## Model Categories

### Blank Slates (Timeless) ✅
- financial_calculator (pure math)
- opportunity_identification_specialist (finds opportunities)
- instruction_generation_specialist (creates steps)
- fact_validation_specialist (verifies claims)

### To Create (Next Session)
- research_analyst (market/competitor research)
- copywriter (sales/marketing copy)
- code_reviewer (software quality analysis)
- seo_optimizer (content optimization)
- negotiation_strategist (deal structuring)

### Legacy (Archive)
- matthew_context_provider_* (baked-in personal history)
- matthew_advisor_* (career-specific)
- humana_* (corporate-specific - deprecated)

---

## Troubleshooting

**Context not loading**:
```bash
python3 -c "import json; print(json.load(open('context/user_profile.json')))"
# Check for JSON syntax errors
```

**Model doesn't see context**:
```bash
# Verify context injection in mirador.py
grep -A 10 "def format_context_string" mirador.py
```

**Chain fails mid-execution**:
- Check which model failed (retry logic shows attempts)
- Verify model installed: `ollama list | grep model_name`
- System continues with remaining models (graceful degradation)

---

## Files Reference

**Core**:
- `mirador.py` - Orchestrator with context injection
- `context/user_profile.json` - Your data (update frequently)
- `modelfiles/*.modelfile` - Blank slate agent definitions

**Systems**:
- `mirador_actionable.py` - Daily action generator
- `mirador_action_prioritizer.py` - Opportunity scoring
- `mirador_fact_validator.py` - Claim verification
- `scripts/model_health_check.sh` - Model status monitoring

**Utilities**:
- `lib/mirador_core-2.1.2-py3-none-any.whl` - Python engine
- `test_*.py` - Verification scripts

---

**The system is alive. The merry go round spins. Context evolves. Models remain timeless.**

**Next session: Build Content Factory or Deal Hunter chain.**
