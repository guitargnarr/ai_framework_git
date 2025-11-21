# Task 2: Training Pipeline

**Branch**: training-pipeline
**Worktree**: ~/ai_framework_worktrees/training-pipeline

## Objective
Build the training and fine-tuning infrastructure for creating specialized models.

## Files to Create

### 1. `framework/training/__init__.py`
- Training module exports

### 2. `framework/training/fine_tuner.py`
```python
# Fine-tuning implementation
- FineTuner class
- Methods: prepare_dataset(), fine_tune(), evaluate()
- Support for LoRA/QLoRA
- Integration with base models (llama3.2, qwen2.5, gemma2)
- Parameter optimization
```

### 3. `framework/training/prompt_engineer.py`
```python
# System prompt engineering
- PromptEngineer class
- Methods: create_system_prompt(), optimize_prompt(), test_prompt()
- Template management for different domains:
  - Music, Creative, Career, Financial, Corporate
  - Relationships, Health, Location-specific
- Prompt validation and scoring
```

### 4. `framework/training/model_builder.py`
```python
# Ollama modelfile builder
- ModelBuilder class
- Methods: create_modelfile(), add_adapter(), set_parameters()
- Template for modelfile generation:
  FROM base_model
  ADAPTER path
  PARAMETER settings
  SYSTEM prompt
- Validation of modelfile syntax
```

### 5. `framework/training/dataset_loader.py`
```python
# Training data management
- DatasetLoader class
- Methods: load_jsonl(), load_csv(), prepare_prompts()
- Support for different data formats
- Data validation and cleaning
- Train/val/test splitting
```

## Requirements
- Compatible with Ollama's training format
- Support for the specialized domains found in universal models
- Efficient data loading for large datasets
- Progress tracking during training

## Acceptance Criteria
- [ ] Fine-tuner can adapt base models
- [ ] Prompt engineer handles all 8 domains
- [ ] Model builder generates valid Ollama modelfiles
- [ ] Dataset loader supports multiple formats
- [ ] All modules integrate smoothly
- [ ] Proper error handling throughout