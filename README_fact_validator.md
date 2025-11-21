# Mirador Fact Validation System

**Intelligent fact-checking system with caching, retry logic, and specialized Ollama models**

## Overview

The Mirador Fact Validator automatically extracts factual claims from instruction files and validates them using specialized Ollama models with caching and retry logic.

## Features

- 🔍 **Automatic Fact Extraction**: Uses `fact-finder-llama` model to identify verifiable claims
- ✅ **Intelligent Validation**: Uses `fact-validator-qwen` model to verify accuracy
- 💾 **Smart Caching**: Prevents redundant validations with SQLite cache
- 🔄 **Retry Logic**: Automatic retry with exponential backoff for reliability
- 📊 **Detailed Reports**: Generates markdown reports with confidence scores

## Installation

### Prerequisites

1. **Ollama** must be installed and running
2. **Required Models**:
   ```bash
   ollama pull fact-finder-llama
   ollama pull fact-validator-qwen
   ```

### Quick Start

```bash
# Make script executable
chmod +x mirador_fact_validator.py

# Validate an instruction file
python3 mirador_fact_validator.py path/to/instruction.txt

# Save report to specific file
python3 mirador_fact_validator.py instruction.txt --output validation_report.md
```

## Usage Examples

### Basic Validation

```bash
python3 mirador_fact_validator.py my_instructions.txt
```

Output:
```
🔍 Extracting facts from instruction...
📊 Found 5 facts to validate

Validating fact 1/5: The Earth orbits the Sun...
✅ VERIFIED (confidence: 95%)

Validating fact 2/5: Water boils at 100°C at sea level...
✅ VERIFIED (confidence: 90%)

...

📝 Validation report saved to: validation_report_20251120_143022.md
```

### With Custom Output

```bash
python3 mirador_fact_validator.py instructions.txt --output my_report.md
```

### Sample Instruction File

Create a file `test_instruction.txt`:

```
# Guitar Technique Instruction

Fact 1: The guitar has six strings in standard tuning.
Fact 2: Standard tuning is E-A-D-G-B-E from lowest to highest.
Fact 3: Alternate tunings can change the sound character of the instrument.

Instructions:
- Practice chord transitions slowly
- Focus on clean string articulation
```

Then validate:
```bash
python3 mirador_fact_validator.py test_instruction.txt
```

## Report Format

The validation report includes:

```markdown
# Fact Validation Report

## Summary
- **Total Facts Analyzed:** 5
- **Verified:** 4 ✅
- **Warnings:** 1 ⚠️
- **Unverified:** 0 ❌
- **From Cache:** 2 💾

## Detailed Results

### ✅ Verified Facts

1. **The guitar has six strings in standard tuning**
   - Status: VERIFIED
   - Confidence: 95%
   - Reasoning: This is a well-established fact...

### ⚠️ Facts Needing Review

2. **Alternate tunings can change tonal character**
   - Status: WARNING
   - Confidence: 70%
   - Reasoning: While generally true, needs more specificity...
```

## Architecture

### Components

1. **FactExtractor**: Identifies factual claims using `fact-finder-llama`
2. **FactValidator**: Verifies facts using `fact-validator-qwen`
3. **CacheManager**: SQLite-based caching (stores at `~/.mirador/fact_cache.db`)
4. **RetryLogic**: Exponential backoff for transient failures

### Caching Strategy

- Facts are hashed and cached in SQLite
- Cache key includes fact text and model version
- Cached results prevent redundant API calls
- Cache location: `~/.mirador/fact_cache.db`

### Retry Logic

- Max 3 attempts per fact
- Exponential backoff: 2s, 4s, 8s
- Graceful degradation on persistent failures

## Model Requirements

### fact-finder-llama
**Purpose**: Extract factual claims from text
**Base**: llama3.2:latest
**Role**: Identifies verifiable statements

### fact-validator-qwen
**Purpose**: Validate factual accuracy
**Base**: qwen2.5:7b
**Role**: Assesses truth and confidence

### Creating Models

If models aren't available, create them:

```bash
# Create fact-finder
cat > fact_finder_modelfile << EOF
FROM llama3.2:latest
PARAMETER temperature 0.3
SYSTEM You are a fact extraction specialist...
EOF
ollama create fact-finder-llama -f fact_finder_modelfile

# Create fact-validator
cat > fact_validator_modelfile << EOF
FROM qwen2.5:7b
PARAMETER temperature 0.2
SYSTEM You are a fact validation expert...
EOF
ollama create fact-validator-qwen -f fact_validator_modelfile
```

## Testing

Run the test suite:

```bash
python3 test_fact_validation.py
```

Expected output:
```
Running fact validator tests...

✓ Help command works
✓ Basic validation test completed

✓ All tests completed successfully
```

## Troubleshooting

### "Model not found"
```bash
# Install required models
ollama pull fact-finder-llama
ollama pull fact-validator-qwen
```

### "Ollama not responding"
```bash
# Check Ollama is running
ollama list

# Restart Ollama if needed
ollama serve
```

### Cache Issues
```bash
# Clear cache if needed
rm ~/.mirador/fact_cache.db
```

### Performance Issues
- **Large files**: The validator processes facts sequentially
- **First run**: Model loading takes time; subsequent runs use cache
- **Network**: Ensure stable connection for initial model downloads

## Integration with AI Framework

This fact validator integrates with the universal AI model system:

```python
from mirador_fact_validator import MiradorFactValidator

validator = MiradorFactValidator()
results = validator.validate_file("instructions.txt")

for result in results:
    print(f"{result.fact}: {result.status} ({result.confidence}%)")
```

## Performance Characteristics

- **First validation**: ~5-10s per fact (model loading + inference)
- **Cached facts**: ~0.1s per fact
- **Typical document** (10 facts): ~1-2 minutes first run, ~5s cached

## Cache Statistics

View cache stats:
```bash
sqlite3 ~/.mirador/fact_cache.db "SELECT COUNT(*) FROM validations;"
sqlite3 ~/.mirador/fact_cache.db "SELECT fact, status FROM validations LIMIT 5;"
```

## Future Enhancements

- [ ] Parallel fact validation for speed
- [ ] Web search integration for current events
- [ ] Confidence threshold configuration
- [ ] JSON output format option
- [ ] Batch processing mode

## Related Documentation

- Main AI Framework: `README.md`
- Core Framework: `TASK_1_CORE_FRAMEWORK.md`
- Training Pipeline: `TASK_2_TRAINING_PIPELINE.md`

## License

Part of the Universal AI Model System

## Support

For issues or questions, see the main project README.

---

**Last Updated**: November 20, 2025
**Version**: 1.0
**Status**: Production Ready
