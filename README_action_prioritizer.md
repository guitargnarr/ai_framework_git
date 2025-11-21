# Mirador Daily Action Prioritization System

**Purpose**: Score opportunities, prioritize daily actions, and track outcomes systematically.

## Overview

This system helps you:
- **Score opportunities** based on multiple factors (financial impact, time efficiency, strategic value, etc.)
- **Prioritize daily actions** based on objective scoring
- **Track execution** and outcomes
- **Learn from performance** data over time

## Installation

The script is self-contained and requires only Python 3 standard library.

```bash
# Make executable (optional)
chmod +x mirador_action_prioritizer.py

# Run directly
python3 mirador_action_prioritizer.py --help
```

## Quick Start

### 1. Add an Opportunity

```bash
python3 mirador_action_prioritizer.py add \
  --title "Automate daily reports" \
  --description "Build script to generate daily performance reports" \
  --financial-impact 7 \
  --time-efficiency 8 \
  --strategic-value 6 \
  --feasibility 9 \
  --urgency 5 \
  --learning-value 4 \
  --estimated-time 120 \
  --potential-income 500
```

**Scoring scale**: 1-10 for each factor
- **Financial Impact**: Potential revenue or cost savings
- **Time Efficiency**: Time saved vs time invested
- **Strategic Value**: Long-term positioning value
- **Feasibility**: How achievable is this?
- **Urgency**: How time-sensitive?
- **Learning Value**: Skill development opportunity

### 2. View Top Opportunities

```bash
# Show top 10 opportunities
python3 mirador_action_prioritizer.py top --limit 10

# Show only high-priority items (score > 6.0)
python3 mirador_action_prioritizer.py top --min-score 6.0
```

### 3. Select Daily Action

```bash
# Select opportunity ID 5 for today
python3 mirador_action_prioritizer.py select 5
```

### 4. Start Action

```bash
# Start working on opportunity ID 5
python3 mirador_action_prioritizer.py start 5 \
  --planned-duration 90
```

### 5. Complete Action

```bash
# Mark as complete with outcome data
python3 mirador_action_prioritizer.py complete 5 \
  --actual-time 85 \
  --actual-income 450 \
  --satisfaction 8 \
  --notes "Implemented successfully, minor tweaks needed"
```

### 6. Generate Reports

```bash
# Priority report (what should I do next?)
python3 mirador_action_prioritizer.py report

# Performance summary (how am I doing?)
python3 mirador_action_prioritizer.py performance
```

## Data Storage

All data is stored in:
- **Database**: `~/ai_framework_git/action_tracking.db` (SQLite)
- **Action Files**: `~/ai_framework_git/daily_actions/` (JSON logs)

## Scoring Algorithm

The system calculates a weighted priority score:

```
Priority Score =
  (0.30 × Financial Impact) +
  (0.20 × Time Efficiency) +
  (0.20 × Strategic Value) +
  (0.15 × Feasibility) +
  (0.10 × Urgency) +
  (0.05 × Learning Value)
```

Higher scores = higher priority.

## Example Workflow

```bash
# Morning: Review top opportunities
python3 mirador_action_prioritizer.py top --limit 5

# Select today's action (e.g., ID 3)
python3 mirador_action_prioritizer.py select 3

# Start working
python3 mirador_action_prioritizer.py start 3 --planned-duration 120

# ... work happens ...

# Complete and record outcome
python3 mirador_action_prioritizer.py complete 3 \
  --actual-time 110 \
  --actual-income 750 \
  --satisfaction 9 \
  --notes "Exceeded expectations, client very happy"

# End of week: Review performance
python3 mirador_action_prioritizer.py performance
```

## Advanced Usage

### Custom Scoring Weights

Modify `self.scoring_weights` in the `MiradorActionPrioritizer` class to adjust priorities:

```python
self.scoring_weights = {
    'financial_impact': 0.4,      # Increase financial weight
    'time_efficiency': 0.3,       # Increase time efficiency
    'strategic_value': 0.15,
    'feasibility': 0.1,
    'urgency': 0.05,
    'learning_value': 0.0         # Ignore learning value
}
```

### Batch Operations

```bash
# Add multiple opportunities from a script
for project in project_a project_b project_c; do
  python3 mirador_action_prioritizer.py add \
    --title "$project" \
    --financial-impact 7 \
    --time-efficiency 8 \
    # ... etc
done
```

### Integration with Daily Workflow

Create an alias in your `.bashrc` or `.zshrc`:

```bash
alias daily-action='python3 ~/ai_framework_git/mirador_action_prioritizer.py'
```

Then use:
```bash
daily-action top
daily-action select 5
daily-action start 5
```

## Testing

Run the test suite:

```bash
python3 test_action_prioritizer.py
```

Expected output:
```
Running mirador_action_prioritizer tests...

✓ Help command works
✓ Database initialization works
✓ Database tables created correctly
✓ Added opportunity with ID: 1, Score: 4.70
✓ Retrieved 1 top opportunities

✓ All tests passed!
```

## Command Reference

| Command | Description | Example |
|---------|-------------|---------|
| `add` | Add new opportunity | `python3 mirador_action_prioritizer.py add --title "Task" --financial-impact 7 ...` |
| `top` | Show top opportunities | `python3 mirador_action_prioritizer.py top --limit 10` |
| `select` | Select daily action | `python3 mirador_action_prioritizer.py select 5` |
| `start` | Start action | `python3 mirador_action_prioritizer.py start 5 --planned-duration 90` |
| `complete` | Complete action | `python3 mirador_action_prioritizer.py complete 5 --actual-time 85 --satisfaction 8` |
| `report` | Priority report | `python3 mirador_action_prioritizer.py report` |
| `performance` | Performance summary | `python3 mirador_action_prioritizer.py performance` |

## Database Schema

### action_opportunities

Stores all opportunities with scores and outcomes.

**Key fields**:
- Priority scores (financial_impact_score, time_efficiency_score, etc.)
- Estimates (estimated_time_minutes, potential_income)
- Actuals (actual_time_minutes, actual_income)
- Outcomes (satisfaction_rating, lessons_learned, would_repeat)

### daily_action_log

Tracks daily execution details.

**Key fields**:
- Timing (planned_start_time, actual_start_time, actual_duration)
- Progress (completion_percentage, obstacles_encountered)
- Outcomes (immediate_outcome, follow_up_required)
- Wellbeing (energy_level_before, energy_level_after, mood_before, mood_after)

## Troubleshooting

**Database locked error**:
```bash
# Stop any running instances
pkill -f mirador_action_prioritizer

# Or manually remove lock (last resort)
rm ~/ai_framework_git/action_tracking.db-journal
```

**Permissions issue**:
```bash
# Ensure base directory exists
mkdir -p ~/ai_framework_git/daily_actions

# Make script executable
chmod +x mirador_action_prioritizer.py
```

## License

MIT - Use freely for personal or commercial projects.

## Author

Created as part of the Mirador improvement planning system.

---

**Quick Tip**: Start with 3-5 opportunities, use the system for a week, then review performance data to refine your scoring approach.
