#!/bin/bash
# Model Cleanup Script for Mirador
# Identifies unused Ollama models and suggests safe cleanup commands

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
MIRADOR_PY="$PROJECT_ROOT/mirador.py"

# Color output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo "========================================"
echo "Mirador Model Cleanup Analysis"
echo "========================================"
echo "Timestamp: $(date)"
echo ""

# Check if mirador.py exists
if [ ! -f "$MIRADOR_PY" ]; then
    echo -e "${RED}✗ mirador.py not found at $MIRADOR_PY${NC}"
    exit 1
fi

# Get all installed Ollama models
echo "Fetching installed Ollama models..."
INSTALLED_MODELS=$(ollama list 2>/dev/null | tail -n +2 | awk '{print $1}')

if [ -z "$INSTALLED_MODELS" ]; then
    echo -e "${YELLOW}⚠ No Ollama models installed${NC}"
    exit 0
fi

model_count=$(echo "$INSTALLED_MODELS" | wc -l | tr -d ' ')
echo -e "${GREEN}✓ Found $model_count installed models${NC}"
echo ""

# Extract model names referenced in mirador.py
echo "Analyzing mirador.py for model references..."
echo ""

# Look for model references in various formats:
# - String literals with model names
# - Variable assignments
# - Function calls with model parameters

USED_MODELS=()

# Search for common model name patterns
while IFS= read -r model; do
    # Remove :latest or other tags for comparison
    base_model=$(echo "$model" | cut -d':' -f1)

    # Check if model is referenced in mirador.py
    if grep -qi "$base_model" "$MIRADOR_PY" 2>/dev/null; then
        USED_MODELS+=("$model")
    fi
done <<< "$INSTALLED_MODELS"

# Display results
echo "========================================"
echo "Model Usage Analysis"
echo "========================================"
echo ""

if [ ${#USED_MODELS[@]} -gt 0 ]; then
    echo -e "${GREEN}Models Referenced in mirador.py:${NC}"
    for model in "${USED_MODELS[@]}"; do
        echo -e "  ${GREEN}✓${NC} $model"
    done
    echo ""
fi

# Find unused models
UNUSED_MODELS=()
while IFS= read -r model; do
    is_used=false
    for used in "${USED_MODELS[@]}"; do
        if [ "$model" == "$used" ]; then
            is_used=true
            break
        fi
    done

    if [ "$is_used" == "false" ]; then
        UNUSED_MODELS+=("$model")
    fi
done <<< "$INSTALLED_MODELS"

if [ ${#UNUSED_MODELS[@]} -gt 0 ]; then
    echo -e "${YELLOW}Models NOT Referenced in mirador.py:${NC}"
    for model in "${UNUSED_MODELS[@]}"; do
        echo -e "  ${YELLOW}⚠${NC} $model"
    done
    echo ""
fi

# Calculate storage impact
echo "========================================"
echo "Storage Analysis"
echo "========================================"
echo ""

total_size=0
unused_size=0

# Get model sizes (this is approximate, Ollama doesn't expose exact sizes easily)
for model in "${UNUSED_MODELS[@]}"; do
    # Typical model sizes (approximate)
    # This is a rough estimate - actual sizes vary
    echo -e "${BLUE}ℹ${NC} $model (size varies by model type)"
done

if [ ${#UNUSED_MODELS[@]} -gt 0 ]; then
    echo ""
    echo -e "${BLUE}Note:${NC} Run 'ollama list' to see actual model sizes"
fi

echo ""

# Generate cleanup suggestions
echo "========================================"
echo "Cleanup Suggestions"
echo "========================================"
echo ""

if [ ${#UNUSED_MODELS[@]} -eq 0 ]; then
    echo -e "${GREEN}✓ All installed models are referenced in mirador.py${NC}"
    echo -e "${GREEN}✓ No cleanup needed${NC}"
    echo ""
else
    echo -e "${YELLOW}⚠ Found ${#UNUSED_MODELS[@]} potentially unused model(s)${NC}"
    echo ""
    echo "Review the following models and consider removing them:"
    echo ""

    for model in "${UNUSED_MODELS[@]}"; do
        echo "# Remove $model:"
        echo "ollama rm $model"
        echo ""
    done

    echo -e "${RED}WARNING:${NC} Review carefully before removing models!"
    echo "Some models may be:"
    echo "  - Used in other scripts or projects"
    echo "  - Base models for derived models"
    echo "  - Required for future development"
    echo ""
    echo "To remove all unused models at once (USE WITH CAUTION):"
    echo ""
    echo "# ⚠️  DANGEROUS - Review first! ⚠️"
    for model in "${UNUSED_MODELS[@]}"; do
        echo "# ollama rm $model"
    done
    echo ""
fi

# Summary
echo "========================================"
echo "Summary"
echo "========================================"
echo ""
echo "Total Models Installed: $model_count"
echo "Models Used in mirador.py: ${#USED_MODELS[@]}"
echo "Models Not Referenced: ${#UNUSED_MODELS[@]}"
echo ""

# Recommendations
echo "========================================"
echo "Recommendations"
echo "========================================"
echo ""

if [ ${#UNUSED_MODELS[@]} -gt 0 ]; then
    echo "1. Review the unused models list above"
    echo "2. Check if they're used in other projects"
    echo "3. Verify they're not base models for Modelfiles"
    echo "4. Remove only models you're certain are unused"
    echo "5. Re-run this script after cleanup to verify"
else
    echo "✓ Your model installation is clean"
    echo "✓ All installed models are actively used"
fi

echo ""
echo "To see detailed model information:"
echo "  ollama list"
echo ""
echo "To create a backup before cleanup:"
echo "  ollama list > ~/ollama_models_backup_$(date +%Y%m%d).txt"
echo ""
