# Model Management Tools

**Created:** November 20, 2025
**Purpose:** Health monitoring and cleanup tools for Mirador Ollama models

---

## Overview

This directory contains two essential scripts for managing Ollama models used by the Mirador AI Orchestration Framework:

1. **model_health_check.sh** - Tests model availability and performance
2. **model_cleanup.sh** - Identifies unused models and suggests safe cleanup

---

## Scripts

### 1. Model Health Check (`scripts/model_health_check.sh`)

Tests all specialist models referenced in the Mirador system, measures latency, and reports health status.

#### Usage

```bash
# Run health check
./scripts/model_health_check.sh

# View last health check log
cat health_check_log.txt
```

#### What It Does

- ✅ Verifies Ollama service is running
- ✅ Tests each specialist model with a test prompt
- ✅ Measures response latency (with 30s timeout)
- ✅ Reports working/broken status for each model
- ✅ Saves detailed results to `health_check_log.txt`
- ✅ Color-coded output (green=working, red=failed, yellow=warning)

#### Models Tested

**Specialist Models:**
- `opportunity_identification_specialist`
- `instruction_generation_specialist`
- `fact_validation_specialist`

**Common Models:**
- `financial_planning_expert_v5`
- `enhanced_agent_fast_v3`
- `louisville_expert_v2`

#### Exit Codes

- `0` - All models healthy
- `1` - Partial failure (some models failed)
- `2` - All models failed

#### Example Output

```
========================================
Mirador Model Health Check
========================================
Timestamp: Wed Nov 20 10:30:45 PST 2025

Checking Ollama service...
✓ Ollama service running

Fetching installed models...
✓ Found 8 installed models

========================================
Testing Specialist Models
========================================

Testing opportunity_identification_specialist... ✓ WORKING (12s latency)
Testing instruction_generation_specialist... ✓ WORKING (8s latency)
Testing fact_validation_specialist... ✗ NOT INSTALLED

========================================
Health Check Summary
========================================

Specialist Models: 2/3 working
Common Models: 3/3 working
Overall: 5/6 models healthy

System Status: PARTIAL FAILURE ⚠

Log saved to: health_check_log.txt
```

---

### 2. Model Cleanup (`scripts/model_cleanup.sh`)

Analyzes which Ollama models are actually used in `mirador.py` and suggests safe cleanup commands for unused models.

#### Usage

```bash
# Run cleanup analysis
./scripts/model_cleanup.sh

# Create backup before cleanup
ollama list > ~/ollama_models_backup_$(date +%Y%m%d).txt

# Review suggestions, then manually remove unused models
ollama rm <model-name>
```

#### What It Does

- ✅ Lists all installed Ollama models
- ✅ Analyzes `mirador.py` for model references
- ✅ Identifies which models are actually used
- ✅ Generates safe cleanup commands (does NOT auto-delete)
- ✅ Provides warnings about potential issues
- ✅ Shows summary and recommendations

#### Safety Features

- **Never auto-deletes** - Only suggests commands
- **Warning messages** - Alerts about base models and dependencies
- **Backup recommendations** - Suggests creating backups first
- **Manual review required** - User must execute cleanup commands

#### Example Output

```
========================================
Mirador Model Cleanup Analysis
========================================
Timestamp: Wed Nov 20 10:35:12 PST 2025

Fetching installed Ollama models...
✓ Found 12 installed models

Analyzing mirador.py for model references...

========================================
Model Usage Analysis
========================================

Models Referenced in mirador.py:
  ✓ financial_planning_expert_v5
  ✓ enhanced_agent_fast_v3
  ✓ louisville_expert_v2

Models NOT Referenced in mirador.py:
  ⚠ llama3.2
  ⚠ codellama
  ⚠ mistral
  ⚠ old_test_model

========================================
Cleanup Suggestions
========================================

⚠ Found 4 potentially unused model(s)

Review the following models and consider removing them:

# Remove llama3.2:
ollama rm llama3.2

# Remove codellama:
ollama rm codellama

# Remove mistral:
ollama rm mistral

# Remove old_test_model:
ollama rm old_test_model

WARNING: Review carefully before removing models!
Some models may be:
  - Used in other scripts or projects
  - Base models for derived models
  - Required for future development

========================================
Summary
========================================

Total Models Installed: 12
Models Used in mirador.py: 3
Models Not Referenced: 4

========================================
Recommendations
========================================

1. Review the unused models list above
2. Check if they're used in other projects
3. Verify they're not base models for Modelfiles
4. Remove only models you're certain are unused
5. Re-run this script after cleanup to verify

To see detailed model information:
  ollama list

To create a backup before cleanup:
  ollama list > ~/ollama_models_backup_20251120.txt
```

---

## Workflow

### Regular Health Monitoring

```bash
# 1. Check model health weekly
./scripts/model_health_check.sh

# 2. Review log for issues
cat health_check_log.txt

# 3. Fix any broken models
ollama pull <model-name>
# or recreate custom models from Modelfiles
```

### Cleanup Workflow

```bash
# 1. Create backup
ollama list > ~/ollama_models_backup_$(date +%Y%m%d).txt

# 2. Run cleanup analysis
./scripts/model_cleanup.sh

# 3. Review suggestions carefully

# 4. Remove only confirmed unused models
ollama rm <model-name>

# 5. Verify cleanup
./scripts/model_cleanup.sh
```

---

## Integration with Mirador

These scripts are designed to work with the Mirador AI Orchestration Framework (`mirador.py`).

### Model References in mirador.py

The cleanup script identifies models by scanning `mirador.py` for:
- Direct model name strings
- Variable assignments with model names
- Function parameters referencing models

### Expected Model Structure

Based on `implementation_commands.sh`, the following specialist models are expected:
- Opportunity identification specialist
- Instruction generation specialist
- Fact validation specialist

Common supporting models:
- Financial planning expert (v5)
- Enhanced agent (fast v3)
- Louisville expert (v2)

---

## Troubleshooting

### Health Check Issues

**Problem:** "Ollama service not running"
**Solution:**
```bash
brew services start ollama
# Wait 10 seconds, then retry
./scripts/model_health_check.sh
```

**Problem:** Model timeout (>30s)
**Possible causes:**
- Model too large for available RAM
- System under heavy load
- Ollama service issues

**Solution:**
```bash
# Restart Ollama
brew services restart ollama

# Check system resources
top

# Try again
./scripts/model_health_check.sh
```

**Problem:** Model not installed
**Solution:**
```bash
# For base models
ollama pull <model-name>

# For custom models, recreate from Modelfile
ollama create <model-name> -f <modelfile>
```

### Cleanup Issues

**Problem:** Script shows models as unused but they're needed
**Explanation:** The script only scans `mirador.py`. Models used in:
- Other scripts
- Modelfiles (as base models)
- External projects

...will show as unused.

**Solution:** Manually review before deleting. Base models (llama3.2, mistral, codellama) are often required for creating custom models.

---

## Reference: implementation_commands.sh

These scripts are based on patterns from:
```
~/Desktop/Manus/mirador-improvement-plan-maybe/implementation_commands.sh
```

Key patterns borrowed:
- Model testing with latency measurement
- Specialist model identification
- Health status reporting
- Safe cleanup suggestions (no auto-delete)

---

## Maintenance

### Adding New Models

When adding new models to `mirador.py`:

1. Update `model_health_check.sh` arrays:
```bash
SPECIALIST_MODELS=(
    "your_new_specialist_model"
    # ... existing models
)
```

2. Run health check to verify:
```bash
./scripts/model_health_check.sh
```

3. Run cleanup analysis:
```bash
./scripts/model_cleanup.sh
```

### Modifying Health Check Behavior

Edit `model_health_check.sh`:
- Adjust timeout (default: 30s)
- Change test prompt
- Modify latency thresholds
- Add custom model groups

### Extending Cleanup Analysis

Edit `model_cleanup.sh`:
- Add additional file scanning (beyond mirador.py)
- Include other projects
- Check Modelfile references
- Add size calculation logic

---

## Best Practices

1. **Run health checks regularly** (weekly recommended)
2. **Create backups before cleanup** (always)
3. **Review cleanup suggestions carefully** (never auto-delete)
4. **Keep base models** (llama3.2, mistral, codellama for Modelfiles)
5. **Document custom models** (save Modelfiles)
6. **Monitor disk space** (Ollama models can be large)
7. **Test after cleanup** (run health check to verify)

---

## Quick Reference

```bash
# Health check
./scripts/model_health_check.sh

# View log
cat health_check_log.txt

# Cleanup analysis
./scripts/model_cleanup.sh

# Create backup
ollama list > ~/ollama_backup_$(date +%Y%m%d).txt

# List all models with sizes
ollama list

# Remove specific model
ollama rm <model-name>

# Restart Ollama
brew services restart ollama
```

---

## Future Enhancements

Potential improvements:
- Automated backup before cleanup
- Model size calculation and reporting
- Historical health tracking (trends over time)
- Email/notification on health check failures
- Integration with monitoring tools
- Modelfile dependency scanning
- Multi-project model usage analysis

---

**Version:** 1.0
**Last Updated:** November 20, 2025
**Compatibility:** macOS with Homebrew Ollama installation
