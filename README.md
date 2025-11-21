# Mirador AI Orchestration Framework

**Daily action generation, fact validation, opportunity prioritization, and model health monitoring powered by specialized Ollama models.**

[![Status](https://img.shields.io/badge/status-production-green)]() [![Models](https://img.shields.io/badge/models-3%20specialist-blue)]() [![License](https://img.shields.io/badge/license-MIT-blue)]()

---

## What This Is

Mirador is an AI orchestration system that generates **daily high-value actions** using multi-model chains with built-in fact validation and opportunity scoring.

**Core capabilities**:
- **Daily Action Generation**: Automated, context-aware task generation
- **Fact Validation**: Verifies claims with confidence scoring and caching
- **Opportunity Prioritization**: Scores opportunities on 6 dimensions (financial, strategic, time, feasibility, urgency, learning)
- **Model Health Monitoring**: Tests and tracks Ollama model performance

---

## Quick Start

### 1. Generate Today's Action

```bash
python3 mirador_actionable.py generate
```

**Output**: Markdown file in `daily_actions/` with:
- One specific high-value action for today
- Why it matters (quantified value)
- Step-by-step execution instructions
- Resource requirements
- Success criteria
- Fact validation report

### 2. Check Model Health

```bash
./scripts/model_health_check.sh
```

**Shows**: Which models working, latency measurements, system status

### 3. Run Multi-Model Chain

```bash
python3 mirador.py chain "Your task description" \
  opportunity_identification_specialist \
  instruction_generation_specialist
```

---

## Installation

### Prerequisites

- Python 3.10+
- [Ollama](https://ollama.ai) installed and running
- Specialist models created (see below)

### Setup

```bash
# Clone repository
git clone https://github.com/guitargnarr/ai_framework_git.git
cd ai_framework_git

# Verify Ollama running
ollama list

# Verify specialist models installed
./scripts/model_health_check.sh

# Generate first daily action
python3 mirador_actionable.py generate

# View the action
cat daily_actions/daily_action_$(date +%Y-%m-%d).md
```

### Specialist Models Required

The system uses 3 core specialist models (all included):

1. **opportunity_identification_specialist** - Identifies actionable opportunities
2. **instruction_generation_specialist** - Converts opportunities to step-by-step instructions
3. **fact_validation_specialist** - Validates factual accuracy with confidence scoring

**Status**: ✅ All 3 models working (verified November 21, 2025)

---

## Features

### 🎯 Daily Action Generation

**File**: `mirador_actionable.py`

Generates one high-value action daily using a 5-model chain:
1. Opportunity identification
2. Louisville context (optional)
3. Financial impact analysis (optional)
4. Instruction generation
5. Fact validation

**Graceful degradation**: Works with 3/5 models if some unavailable.

**Usage**:
```bash
python3 mirador_actionable.py generate    # Generate today's action
python3 mirador_actionable.py show        # View today's action
python3 mirador_actionable.py complete 2025-11-21 --outcome "Completed" --time 45
python3 mirador_actionable.py history     # View past actions
```

---

### 📊 Opportunity Prioritization

**File**: `mirador_action_prioritizer.py`

Scores opportunities on 6 weighted dimensions:
- Financial impact (30%)
- Time efficiency (20%)
- Strategic value (20%)
- Feasibility (15%)
- Urgency (10%)
- Learning value (5%)

**Database**: SQLite tracking with outcome measurement and ROI analysis.

**Usage**:
```bash
python3 mirador_action_prioritizer.py add --title "Task" --financial-impact 8 --time-efficiency 7 ...
python3 mirador_action_prioritizer.py top --limit 10
python3 mirador_action_prioritizer.py select 5
python3 mirador_action_prioritizer.py complete 5 --actual-time 90 --satisfaction 8
```

**See**: `README_action_prioritizer.md` for complete guide

---

### ✅ Fact Validation System

**File**: `mirador_fact_validator.py`

Validates claims with:
- Confidence scoring (0.8-1.0 reliability scale)
- 24-hour fact caching (prevents re-checking)
- Louisville-specific source verification
- Financial data validation

**Validation rules for**:
- Business hours, phone numbers, addresses
- Financial rates and program deadlines
- Cost amounts and time-sensitive info

**Usage**:
```bash
python3 mirador_fact_validator.py init
python3 mirador_fact_validator.py validate "TARC bus fare is $1.75"
```

**See**: `README_fact_validator.md` for complete guide

---

### 🏥 Model Health Monitoring

**Files**: `scripts/model_health_check.sh`, `scripts/model_cleanup.sh`

**Health Check**:
- Tests all specialist models with latency measurement
- Reports working/broken status
- Saves logs to `health_check_log.txt`

**Cleanup**:
- Identifies unused Ollama models safely
- Generates cleanup commands (doesn't auto-delete)
- Recommends which models safe to remove

**Usage**:
```bash
./scripts/model_health_check.sh     # Run health check
cat health_check_log.txt            # View results
./scripts/model_cleanup.sh          # Analyze unused models
```

**See**: `README_model_management.md` for complete guide

---

## Architecture

### Model Chain Flow

```
User Prompt
    ↓
opportunity_identification_specialist
    ↓ (context accumulation)
instruction_generation_specialist
    ↓ (context accumulation)
fact_validation_specialist
    ↓
Daily Action (Markdown)
```

### Enhanced Error Handling

- **3-attempt retry logic** with exponential backoff
- **Response validation** (minimum 50 characters)
- **Timeout handling** (120s per attempt, automatic retry)
- **Graceful degradation** (continues with working models if some fail)

### Quality Features

- Timestamped output storage (`outputs/chain_TIMESTAMP/`)
- Individual model outputs saved
- Comprehensive summary generation
- Success/failure tracking
- Word count and latency metrics

---

## Daily Workflow

```bash
# Morning: Generate daily action
python3 mirador_actionable.py generate

# Read the action
cat daily_actions/daily_action_$(date +%Y-%m-%d).md

# Execute the action (in real life)
# ...

# Evening: Mark complete and record outcome
python3 mirador_actionable.py complete $(date +%Y-%m-%d) \
  --time 60 \
  --outcome "Applied to 3 jobs" \
  --value "High priority opportunities"

# Weekly: Check model health
./scripts/model_health_check.sh
```

---

## File Structure

```
ai_framework_git/
├── mirador.py                          # Core orchestrator with retry logic
├── mirador_actionable.py               # Daily action generation
├── mirador_action_prioritizer.py       # Opportunity scoring system
├── mirador_fact_validator.py           # Fact validation with caching
├── scripts/
│   ├── model_health_check.sh           # Health monitoring
│   └── model_cleanup.sh                # Safe model cleanup
├── daily_actions/                      # Generated actions (markdown + JSON)
├── outputs/                            # Chain execution results
├── README_*.md                         # Component documentation
└── test_*.py                           # Test suites
```

---

## Testing

```bash
# Test action prioritizer
python3 test_action_prioritizer.py

# Test fact validator
python3 test_fact_validator.py

# Test actionable system
python3 test_mirador_actionable.py

# Test model health
./scripts/model_health_check.sh
```

**Expected**: All tests pass, all specialist models working

---

## Performance

**Model latencies** (measured November 21, 2025):
- `opportunity_identification_specialist`: ~3-5s
- `instruction_generation_specialist`: ~1-9s
- `fact_validation_specialist`: ~1-11s

**Total chain execution**: 15-25 seconds for complete daily action

**System health**: 3/3 specialist models operational

---

## Development

### Built With
- Python 3.14
- Ollama (local LLM orchestration)
- SQLite (tracking databases)
- Requests (Ollama API calls)

### Created From
- Mirador improvement planning (June-November 2025)
- Parallel development v5 methodology
- Pattern learning integration (November 20-21, 2025)

### Key Features
- Enhanced retry logic (prevents timeout failures)
- Response validation (ensures meaningful output)
- Graceful degradation (works with partial model availability)
- Comprehensive tracking (SQLite databases for learning)

---

## License

MIT License - See LICENSE file for details

---

## Author

**Matthew Scott**
- GitHub: [@guitargnarr](https://github.com/guitargnarr)
- Email: matthewdscott7@gmail.com

---

## Related Projects

- [projectlavos-monorepo](https://github.com/guitargnarr/projectlavos-monorepo) - Multi-site AI platform
- [job-search-automation](https://github.com/guitargnarr/job-search-automation) - Job search automation with NLP
- [phishguard-ml](https://github.com/guitargnarr/phishguard-ml) - Phishing detection with 7-model ensemble

---

**Status**: Production-ready as of November 21, 2025
**Last Health Check**: 3/3 specialist models working
**Last Daily Action**: 2025-11-21 (mortgage refinancing opportunity)
