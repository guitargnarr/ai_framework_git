# Mirador Actionable Instruction System

**Purpose**: Generates one actionable instruction per day to help you make consistent progress on your projects.

## Quick Start

```bash
# Generate today's action
python3 mirador_actionable.py generate

# Or use the launcher
/tmp/mirador-action generate
```

## Commands

### Generate Today's Action
```bash
python3 mirador_actionable.py generate
```
Creates a new daily action instruction based on:
- Your current projects and priorities
- Recent activity patterns
- Specialist AI models (matthew-career-coach, barrier-breaker, etc.)

### Show Today's Action
```bash
python3 mirador_actionable.py show
```
Displays the current day's action without generating a new one.

### Mark Action as Complete
```bash
python3 mirador_actionable.py complete
```
Records completion of today's action and stores it in history.

### View Action History
```bash
python3 mirador_actionable.py history
```
Shows all past completed actions with dates.

## Example Workflow

```bash
# Morning: Generate today's action
$ python3 mirador_actionable.py generate
🎯 Generating daily action for 2025-11-21
==================================================
Today's Action: Update your resume for the UofL Senior Software Engineer position...

# During the day: Check what you're working on
$ python3 mirador_actionable.py show
📋 Today's Action (2025-11-21)
==================================================
Update your resume for the UofL Senior Software Engineer position...

# Evening: Mark as complete
$ python3 mirador_actionable.py complete
✅ Action completed for 2025-11-21

# Weekly: Review progress
$ python3 mirador_actionable.py history
📚 Action History
==================================================
2025-11-21: Update your resume for the UofL Senior Software Engineer position...
2025-11-20: Create cover letter for Indeed application...
```

## How It Works

### Data Sources
The system analyzes:
- **JOB_TRACKER_2025.csv**: Current job applications and status
- **GMAIL_search_results.csv**: Recent email activity
- **Project files**: Your active development work
- **Claude context**: Your documented priorities and goals

### AI Models Used
- **matthew-career-coach**: Career strategy and job search guidance
- **barrier-breaker**: Hiring tactics and application optimization
- **louisville-job-market**: Local market insights

### Action Generation Process
1. **Context Analysis**: Reviews your current situation
2. **Priority Detection**: Identifies most urgent/impactful task
3. **Action Synthesis**: Creates one specific, actionable instruction
4. **Verification**: Ensures action is achievable within a day

### Retry Logic
If action generation fails:
- Retries up to 3 times
- Falls back to simpler models
- Provides useful fallback actions

## Storage

Actions are stored in:
```
~/.mirador/actions/
├── current_action.json       # Today's active action
└── action_history.json        # All completed actions
```

## Launcher Script

A launcher script is installed at `/tmp/mirador-action` for quick access:

```bash
# Add to your shell profile for global access
alias ma='/tmp/mirador-action'

# Then use it anywhere
ma generate
ma show
ma complete
ma history
```

## Integration with Daily Workflow

### Morning Routine
```bash
# Start your day with a clear action
ma generate
```

### Throughout the Day
```bash
# Quick reminder of today's focus
ma show
```

### Evening Review
```bash
# Mark completion and prepare for tomorrow
ma complete
ma generate  # Optional: preview tomorrow's action
```

## Testing

Run the test suite:
```bash
python3 test_mirador_actionable.py
```

This verifies:
- ✅ Help command works
- ✅ Generate command works
- ✅ Show command works
- ✅ History command works

## Philosophy

**One action per day** keeps you focused without overwhelming you. Each action is:
- **Specific**: Clear what to do
- **Achievable**: Can be done in one day
- **Impactful**: Moves Priority 1 forward
- **Adaptive**: Based on current context, not static plans

## Troubleshooting

### "No action for today"
```bash
# Generate a new one
ma generate
```

### "Ollama model not found"
```bash
# Verify models are running
ollama list | grep -E "matthew-career-coach|barrier-breaker|louisville"
```

### Action seems stale/irrelevant
```bash
# Regenerate based on current context
ma generate
```

## Examples of Generated Actions

Real examples from the system:

```
📋 Apply to 3 software engineering positions on LinkedIn that match your React/TypeScript skills

📋 Update your GitHub profile README to showcase parallel development methodology

📋 Send follow-up email to UofL HR about interview timeline

📋 Complete the cover letter customization for Indeed application using barrier-breaker tactics

📋 Review and improve projectlavos-monorepo test coverage to 80%+
```

## Why This Works

Based on proven principles:
- **Daily consistency** > sporadic bursts
- **One focus** > scattered effort
- **Context-aware** > generic advice
- **Action-oriented** > planning paralysis

The system uses your own documented context (working philosophy, job tracker, project status) to generate actions that align with your actual priorities.

## Future Enhancements

Potential additions:
- Weekly goal setting
- Progress tracking dashboard
- Integration with calendar
- Slack/email notifications
- Team collaboration mode

---

**Created**: November 20, 2025
**Part of**: AI Framework Git Project
**Related**: mirador_actionable.py, Mirador Core System
