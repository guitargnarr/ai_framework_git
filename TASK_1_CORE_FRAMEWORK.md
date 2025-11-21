# Task 1: Core Framework Module

**Branch**: core-framework
**Worktree**: ~/ai_framework_worktrees/core-framework

## Objective
Create the foundational framework architecture with base classes, configuration system, and model management.

## Files to Create

### 1. `framework/__init__.py`
- Package initialization
- Version info
- Core imports

### 2. `framework/core/__init__.py`
- Core module exports

### 3. `framework/core/base_model.py`
```python
# Abstract base class for all universal models
- AbstractBaseModel class
- Methods: load(), save(), validate(), get_config()
- Properties: name, version, base_model, parameters
- Support for Ollama modelfile generation
```

### 4. `framework/core/config.py`
```python
# Configuration management
- ModelConfig dataclass
- Parameters: temperature, top_p, top_k, repeat_penalty
- System prompt management
- Base model selection (llama3.2, qwen2.5, gemma2)
- Validation methods
```

### 5. `framework/core/model_manager.py`
```python
# Model lifecycle management
- ModelManager class
- Methods: create_model(), load_model(), delete_model()
- Model registry tracking
- Version control
- Database integration for chain_memory.db
```

### 6. `framework/core/exceptions.py`
```python
# Custom exceptions
- ModelNotFoundError
- ConfigurationError
- ValidationError
- OllamaConnectionError
```

## Requirements
- Use dataclasses for configuration
- Type hints throughout
- Docstrings for all classes/methods
- Support for the 8 universal models found in outputs/
- Compatible with Ollama's modelfile format

## Acceptance Criteria
- [ ] All files created with proper structure
- [ ] Base classes are abstract and extensible
- [ ] Config system handles all model parameters
- [ ] Manager can track multiple models
- [ ] Exceptions cover common error cases
- [ ] Code is typed and documented