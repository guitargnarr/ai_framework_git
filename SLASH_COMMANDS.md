# Slash Commands Reference - Custom Claude Code Commands

**Updated**: Nov 24, 2025
**Location**: ~/.claude/commands/
**Total**: 23 custom commands

---

## 🎯 Most Useful (Proven This Session)

### Git Workflow

**/commit**
- **Purpose**: AI-generated commit messages (conventional format)
- **Usage**: Type `/commit` when changes are staged
- **Output**: Analyzes git diff, suggests commit message
- **Proven**: Used 40+ times this session

**/push-pr**
- **Purpose**: Push branch and create pull request
- **Usage**: `/push-pr [base-branch]`
- **Output**: Pushes to GitHub, creates PR with AI description

**/git**
- **Purpose**: Comprehensive git workflow with Ultrathink analysis
- **Usage**: `/git [commit|push|pr|review]`

---

## 🛠️ Development Commands

**/code [prompt]**
- **Purpose**: Generate Python code using code-executor Ollama model
- **Usage**: `/code "create function to parse JSON"`
- **Model**: code-executor (Ollama)

**/analyze [data]**
- **Purpose**: Data analysis using data-analyzer-qwen
- **Usage**: `/analyze "analyze this dataset"`
- **Output**: Returns JSON analysis

---

## 🤖 AI Model Commands

**/coach [question]**
- **Purpose**: Career coaching via matthew-career-coach model
- **Usage**: `/coach "how to answer behavioral questions"`
- **Note**: Has personal context (may need Tabula Rasa check)

**/louisville [query]**
- **Purpose**: Louisville KY market data from louisville-job-market
- **Usage**: `/louisville "tech companies hiring"`

**/tactic [situation]**
- **Purpose**: Hiring tactics from barrier-breaker model
- **Usage**: `/tactic "how to get past ATS"`

**/quick [question]**
- **Purpose**: Quick brief answers from quick-advisor-phi
- **Usage**: `/quick "what is FastAPI"`

**/test-models**
- **Purpose**: Run comprehensive Ollama model test suite
- **Usage**: `/test-models`
- **Output**: Tests all models, reports status

---

## 🎨 Creative/Generative Commands

**/art [type]**
- **Purpose**: Generate algorithmic art (flow fields, geometric, etc.)
- **Usage**: `/art flow-field --seed 42 --color vibrant`

**/canvas-design [type]**
- **Purpose**: Advanced algorithmic art (Voronoi, neural networks, terrain)
- **Usage**: `/canvas-design voronoi --nodes 100`

**/generative-artist [style]**
- **Purpose**: Generative art creation
- **Usage**: `/generative-artist abstract`

**/slack-gif [type] "text"**
- **Purpose**: Create animated GIFs optimized for Slack
- **Usage**: `/slack-gif emoji "success" --animation bounce`

**/theme [action]**
- **Purpose**: Apply consistent themes across output formats
- **Usage**: `/theme preview` or `/theme export css`

**/humanize [text]**
- **Purpose**: Convert AI-generated text to natural human language
- **Usage**: `/humanize "transform this robotic text"`

---

## 📦 Repository Management

**/audit-repo [name]**
- **Purpose**: Execute complete rigorous audit of repository
- **Usage**: `/audit-repo phishguard-ml`
- **Output**: Comprehensive audit report (code quality, tests, docs, deployment)

**/audit-status**
- **Purpose**: Show current audit progress, identify gaps
- **Usage**: `/audit-status`

**/audit-handoff**
- **Purpose**: Sync with other Claude instance, read handoff docs
- **Usage**: `/audit-handoff`

**/audit-sync [operation]**
- **Purpose**: Update coordination file with progress (atomic locking)
- **Usage**: `/audit-sync update phishguard-ml`

---

## 🌿 Git Worktree Commands

**/worktree <create|list|remove|cleanup>**
- **Purpose**: Manage git worktrees for parallel development
- **Usage**:
  - `/worktree create feature-branch main`
  - `/worktree list`
  - `/worktree remove feature-branch`
- **Proven**: Used during parallel development sessions

**/cleanup-worktrees**
- **Purpose**: Clean up merged worktrees and branches
- **Usage**: `/cleanup-worktrees`
- **Use when**: After parallel dev session, branches merged

---

## 📊 Usage Patterns (This Session)

**Actually used**:
- /commit (40+ times - every git commit)
- /push-pr (never used - manual git push preferred)
- /worktree (referenced in docs, not used this session)

**Never used**:
- /audit-* commands (repo audit system)
- /art, /canvas-design, /generative-artist (creative)
- /slack-gif, /theme (utility)
- /coach, /louisville, /tactic (Ollama models with personal context)

**Should use more**:
- /analyze (for data-driven decisions)
- /code (for quick script generation)

---

## 🎯 Recommendations

**Keep using**:
- /commit (proven, fast, accurate)
- /worktree (parallel dev workflow)

**Try using**:
- /analyze (data analysis for strategy decisions)
- /code (quick Python script generation)

**Review for Tabula Rasa**:
- /coach (has personal context - check if compliant)
- /louisville (local market data - verify no personal info)
- /tactic (hiring tactics - check context)

**Archive/Remove**:
- /audit-* (if not using repo audit workflow)
- Creative commands (if not creating art)

---

**23 commands available. Most unused. Focus on the proven ones (/commit, /worktree).**
