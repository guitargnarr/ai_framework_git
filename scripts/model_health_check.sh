#!/bin/bash
# Model Health Check Script for Mirador Specialist Models
# Tests all specialist models and reports health status

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
LOG_FILE="$PROJECT_ROOT/health_check_log.txt"

# Specialist models from mirador.py (based on implementation_commands.sh)
SPECIALIST_MODELS=(
    "opportunity_identification_specialist"
    "instruction_generation_specialist"
    "fact_validation_specialist"
)

# Additional models that may be referenced
COMMON_MODELS=(
    "financial_planning_expert_v5"
    "enhanced_agent_fast_v3"
    "louisville_expert_v2"
)

# Color output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo "========================================"
echo "Mirador Model Health Check"
echo "========================================"
echo "Timestamp: $(date)"
echo ""

# Initialize log
echo "=== Mirador Model Health Check ===" > "$LOG_FILE"
echo "Timestamp: $(date)" >> "$LOG_FILE"
echo "" >> "$LOG_FILE"

# Check Ollama service
echo "Checking Ollama service..."
if ! pgrep -x "ollama" > /dev/null; then
    echo -e "${RED}✗ Ollama service not running${NC}"
    echo "✗ Ollama service not running" >> "$LOG_FILE"
    echo ""
    echo "Start Ollama with: brew services start ollama"
    exit 1
fi
echo -e "${GREEN}✓ Ollama service running${NC}"
echo "✓ Ollama service running" >> "$LOG_FILE"
echo ""

# Get list of installed models
echo "Fetching installed models..."
INSTALLED_MODELS=$(ollama list 2>/dev/null | tail -n +2 | awk '{print $1}')

if [ -z "$INSTALLED_MODELS" ]; then
    echo -e "${RED}✗ No models installed${NC}"
    echo "✗ No models installed" >> "$LOG_FILE"
    exit 1
fi

echo -e "${GREEN}✓ Found $(echo "$INSTALLED_MODELS" | wc -l | tr -d ' ') installed models${NC}"
echo ""

# Function to test a model
test_model() {
    local model_name=$1
    local test_prompt="Hello, this is a health check test. Please respond briefly."

    echo -n "Testing $model_name... "

    # Check if model exists
    if ! echo "$INSTALLED_MODELS" | grep -q "^$model_name"; then
        echo -e "${RED}NOT INSTALLED${NC}"
        echo "✗ $model_name - NOT INSTALLED" >> "$LOG_FILE"
        return 1
    fi

    # Measure latency
    start_time=$(date +%s)

    # Test the model with timeout
    response=$(timeout 30s ollama run "$model_name" "$test_prompt" 2>&1)
    exit_code=$?

    end_time=$(date +%s)
    duration=$((end_time - start_time))

    if [ $exit_code -eq 0 ] && [ -n "$response" ]; then
        echo -e "${GREEN}✓ WORKING${NC} (${duration}s latency)"
        echo "✓ $model_name - WORKING (${duration}s latency)" >> "$LOG_FILE"
        return 0
    elif [ $exit_code -eq 124 ]; then
        echo -e "${RED}✗ TIMEOUT${NC} (>30s)"
        echo "✗ $model_name - TIMEOUT (>30s)" >> "$LOG_FILE"
        return 1
    else
        echo -e "${RED}✗ FAILED${NC}"
        echo "✗ $model_name - FAILED (exit code: $exit_code)" >> "$LOG_FILE"
        return 1
    fi
}

# Test specialist models
echo "========================================"
echo "Testing Specialist Models"
echo "========================================"
echo ""
echo "--- Specialist Models ---" >> "$LOG_FILE"

specialist_working=0
specialist_total=${#SPECIALIST_MODELS[@]}

for model in "${SPECIALIST_MODELS[@]}"; do
    if test_model "$model"; then
        ((specialist_working++))
    fi
done

echo ""

# Test common models
echo "========================================"
echo "Testing Common Models"
echo "========================================"
echo ""
echo "--- Common Models ---" >> "$LOG_FILE"

common_working=0
common_total=${#COMMON_MODELS[@]}

for model in "${COMMON_MODELS[@]}"; do
    if test_model "$model"; then
        ((common_working++))
    fi
done

echo ""

# Summary
echo "========================================"
echo "Health Check Summary"
echo "========================================"
echo ""
echo "--- Summary ---" >> "$LOG_FILE"

total_working=$((specialist_working + common_working))
total_tested=$((specialist_total + common_total))

echo "Specialist Models: $specialist_working/$specialist_total working"
echo "Common Models: $common_working/$common_total working"
echo "Overall: $total_working/$total_tested models healthy"
echo ""
echo "Specialist Models: $specialist_working/$specialist_total working" >> "$LOG_FILE"
echo "Common Models: $common_working/$common_total working" >> "$LOG_FILE"
echo "Overall: $total_working/$total_tested models healthy" >> "$LOG_FILE"
echo "" >> "$LOG_FILE"

# Health status
if [ $total_working -eq $total_tested ]; then
    echo -e "${GREEN}System Status: ALL MODELS HEALTHY ✓${NC}"
    echo "System Status: ALL MODELS HEALTHY ✓" >> "$LOG_FILE"
    exit_status=0
elif [ $total_working -gt 0 ]; then
    echo -e "${YELLOW}System Status: PARTIAL FAILURE ⚠${NC}"
    echo "System Status: PARTIAL FAILURE ⚠" >> "$LOG_FILE"
    exit_status=1
else
    echo -e "${RED}System Status: ALL MODELS FAILED ✗${NC}"
    echo "System Status: ALL MODELS FAILED ✗" >> "$LOG_FILE"
    exit_status=2
fi

echo ""
echo "Log saved to: $LOG_FILE"
echo ""

exit $exit_status
