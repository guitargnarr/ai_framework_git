# Proven Workflows & Methodologies - Infrastructure Inventory

**Updated**: Nov 24, 2025
**Source**: Nov 22-24 session (successful deployments, tools built, systems validated)
**Purpose**: Know what works, repeat winning patterns

---

## 🎯 Workflow 1: Rapid Full-Stack Deployment (PhishGuard Pattern)

**Proven with**: PhishGuard (API + UI), jaspermatters, FretForge

### Steps

1. **Backend Deployment to Railway** (15 min)
   - Fix PORT env var: `port = int(os.environ.get("PORT", 8000))`
   - Create railway.json (healthcheck, Docker)
   - Push to GitHub → Railway auto-deploys
   - Verify: `railway logs`, test /health endpoint

2. **Frontend Generation with Elite Frontend** (5 min)
   - `ollama run elite-frontend "Create [component description]"`
   - Output: B+ code (TypeScript + Next.js 14 + Shadcn)
   - Known fixes: Icon imports, API field names

3. **Next.js Project Setup** (5 min)
   - `npx create-next-app@latest [name] --typescript --tailwind --app`
   - `npx shadcn@latest init && add card button input badge`
   - Copy generated code, fix imports

4. **Deploy to Vercel** (5 min)
   - `vercel --prod --yes`
   - **Critical**: Disable Vercel Authentication in dashboard
   - Verify HTTP 200 (not 401)

5. **Connect to GitHub** (2 min)
   - `gh repo create [name] --public --source=. --push`
   - CI/CD auto-enabled

**Total time**: 30-35 minutes
**Success rate**: 3/3 (PhishGuard, jaspermatters, FretForge)
**Result**: Full-stack product (backend API + frontend demo) publicly accessible

---

## 🔍 Workflow 2: Fair Shake Repository Vetting (Systematic Assessment)

**Proven with**: 40 repos assessed, 3 enterprise products discovered

### Phase 1: Deep Investigation (15-30 min per repo)

**Don't**: Quick README scan → dismiss
**Do**: Systematic investigation

```bash
# 1. Read ALL documentation
cat README.md DEMO_README.md docs/*.md

# 2. Check what exists
ls -la  # File structure
find . -name "*.py" -o -name "*.ts" -o -name "*.tsx"  # Code files

# 3. Check completeness
git log --oneline -10  # Recent activity?
npm run build 2>&1 || python3 -m pytest 2>&1  # Does it work?

# 4. Assess deployment status
git remote -v  # On GitHub?
find . -name ".vercel" -o -name "railway.json" -o -name "netlify.toml"  # Deployed?

# 5. Determine value
# - What problem does it solve? (specific)
# - Who uses it? (real users or hypothetical)
# - Is it finished? (working code or scaffolding)
```

**Output**: Detailed assessment (not "looks incomplete, archive it")

### Phase 2: Value Classification

**Ask 3 questions**:
1. Does this have validation? (customer, traction, ROI data)
2. Does this demonstrate valuable expertise? (consulting leads)
3. Is this finished enough to show? (working, not half-baked)

**Decisions**:
- **If validation**: Tier 1 (scale this)
- **If demos expertise**: Tier 2 (portfolio piece)
- **If neither but pivot potential**: Tier 3 (investigate pivot)
- **If none**: Tier 4 (archive after fair shake)

**Key**: Archive is LAST resort (after investigation proves no value)

---

## ⚡ Workflow 3: Oracle + Human Collaboration (Hybrid Assessment)

**Proven with**: 40 repos scored, decisions made accurately

### Oracle Role (Automated Filter)

```bash
python3 ~/ai_framework_git/inventory_oracle.py readiness REPO_NAME
```

**What Oracle does** (instant):
- Scores infrastructure (0-100)
- Checks: Dockerfile, tests, README, LICENSE, git status
- Recommends platform (Railway/Vercel/Netlify)
- Estimates deploy time

**What Oracle CAN'T do**:
- Assess user value (you do this)
- Check if already deployed (you verify)
- Determine if finished vs scaffolding

### Human Role (Value Validation)

**After Oracle scores**, investigate:
1. What does it actually do? (run the code)
2. Who would use this? (specific users, not "developers")
3. Is it deployed already? (check Vercel, Railway, etc.)
4. Does it solve a real problem? (validation data)

### The Collaboration

**Oracle**: "These 10 have high scores (infrastructure-ready)"
**Human**: "Of those 10, these 3 solve real problems"
**Decision**: Focus on the 3 (not deploy all 10)

**Success**: Discovered Mirador, job-search, phishguard had validation

---

## 🛠️ Workflow 4: Hybrid AI+Python Pattern (Quantitative vs Qualitative)

**Proven with**: Oracle scoring, Elite Frontend code generation

### When to Use Python (Deterministic)

**Tasks**:
- Arithmetic/scoring (calculate deployment readiness score)
- Logic/rules (if Dockerfile: +20 points, if tests: +10 points)
- File operations (scan repos, check for files)
- API calls (vercel ls, railway status, git commands)

**Why**: Fast (<0.1s), 100% accurate, debuggable, no hallucinations

**Example**: Oracle scoring (tried AI, failed → switched to Python, works perfectly)

### When to Use AI (Qualitative)

**Tasks**:
- Code generation (Elite Frontend scaffolds components)
- Natural language understanding (interpret user requests)
- Pattern recognition (identify similar repos)
- Recommendations (suggest platforms based on tech stack)

**Why**: Flexible, handles variation, generates creative solutions

**Example**: Elite Frontend (generates 85% correct code, human adds 15%)

### The Hybrid Approach

**Don't**: Use AI for everything (small models can't do math)
**Don't**: Use only Python (miss AI's qualitative strengths)
**Do**: Python for what it's good at, AI for what it's good at

**Success**: Hybrid Oracle (Python scores, AI could add qualitative insights if needed)

---

## 📚 Workflow 5: Documentation Governance (Modular Not Monolithic)

**Proven with**: Doc purge (4,500 → 800 lines), then 16 focused documents

### The Anti-Pattern (What Failed)

**Before**: One massive CLAUDE.md (4,500 lines)
- Mixed permanent with temporal
- Hard to update (change one thing, rewrite everything)
- Context bloat (loading everything always)

**Result**: Unmaintainable, outdated, ignored

### The Working Pattern (What Succeeded)

**Structure**:
- **Permanent** (strategy, philosophy, guides): Update rarely
- **Temporal** (portfolio map, session handoff): Update frequently
- **Navigation** (Master Index): Points to all, doesn't duplicate

**Loading**:
- **Auto-load**: CLAUDE.md (rules, always needed)
- **@ import**: strategy.md, philosophy.md (when relevant)
- **Read manually**: SESSION_HANDOFF (start of work)

**Updates**:
- Change one doc without touching others
- Append to CLAUDE.md (latest governance at end, overrides previous)
- No massive rewrites

**Success**: 16 documents (modular, focused, current)

---

## 🚀 Workflow 6: Strategic Pivot (Data-Driven Refocus)

**Proven with**: Nov 24 vetting discovery (3 businesses vs 40 repos mindset)

### When Data Contradicts Strategy

**Situation**: Thought we needed to "discover products from 40 repos"
**Data**: Vetting revealed 3 validated businesses already exist
**Action**: Pivot strategy immediately

### The Pivot Process

1. **Acknowledge reality**: You have validation already (Norton, job-search traction, phishguard accuracy)
2. **Update all docs**: Portfolio, strategy, session handoff (all aligned in <1 hour)
3. **Refocus effort**: 80/15/5 (Mirador/job-search/phishguard)
4. **Stop building**: Tools are sufficient, scale businesses instead

**Success**: Strategy now aligned with reality (scale validation, not discover more)

---

## 🎓 Workflow 7: Session Continuity (Terminal Stays Open)

**Proven with**: Nov 22-24 continuous work (sleep break, terminal open)

### The Pattern

**Don't**: Close terminal at "end of day"
**Do**: Keep terminal open, work across multiple days

**Context management**:
- SESSION_HANDOFF.md preserves state
- CLAUDE.md loads automatically (rules persist)
- @ import context as needed (strategy, philosophy)

**Benefits**:
- No re-setup cost (environment ready)
- History persists (scroll up to see what was done)
- Continuity (pick up where you left off)

**Governance**: Never suggest closing based on time/fatigue (user controls boundaries)

---

## 💡 Workflow 8: Direct Communication (No False Choices)

**Proven with**: 6-7 decision points where I knew the answer but presented options

### The Anti-Pattern

**Bad**: "Here are 3 options (A, B, C)..." [secretly knowing C is right]
**Result**: Decision paralysis, wasted time

### The Working Pattern

**Good**: "C is the right move because [reasons]. Execute this, or want alternatives?"
**Result**: Fast execution, user can override if needed

**Governance**: State what you know, recommend explicitly, then offer choice

**Success**: Saves 30+ minutes per session (no option paralysis)

---

## 📊 Success Metrics (What Actually Worked)

### Deployment Velocity

**Pattern**: Investigate → Generate → Deploy → Verify
**Time**: 15-35 minutes per full-stack product
**Success rate**: 4/4 (PhishGuard, jaspermatters, FretForge, llm-demo prep)

### Discovery Efficiency

**Pattern**: Fair shake vetting (investigate deeply, not quickly)
**Time**: 15-30 min per repo
**Success**: Found 3 enterprise products (would've missed with quick scans)

### Tool Development

**Pattern**: Test-driven (prove concept before scaling)
**Time**: Oracle (2 hours build + test), Elite Frontend (1 hour)
**Success**: Both work, both useful, both proven

---

## 🔄 Workflows Per Project Category

### For Enterprise Products (Mirador, job-search, phishguard)

**Workflow**: Scale validated → Sales collateral → Customer outreach
**NOT**: Build more features before getting customers
**Example**: Mirador - Norton proves ROI → pitch 3 more hospitals (don't build new features)

### For Portfolio Demos (jaspermatters, FretForge, llm-demo)

**Workflow**: Deploy → Document tech → Link from portfolio → Maintain
**NOT**: Monetize everything (some are lead generators, not products)
**Example**: jaspermatters - shows ML expertise → consulting leads (not SaaS product)

### For Personal Tools (OurJourney, vision-board)

**Workflow**: Keep for personal use → Don't commercialize
**NOT**: Try to monetize everything
**Example**: OurJourney - valuable for you, not market product

### For Archive Candidates (consciousness-experiments, knowledge-base)

**Workflow**: Fair shake investigation → Document learnings → Archive with reasoning
**NOT**: Quick dismissal (risks Archive-Recovery incident)
**Example**: consciousness-experiments - investigated, no commercial value, documented why, then archive

---

## 🎯 Application Guide

**When deploying new project**: Use Workflow 1 (Rapid Full-Stack)
**When assessing repos**: Use Workflow 2 (Fair Shake Vetting) + Workflow 3 (Oracle + Human)
**When building tools**: Use Workflow 4 (Hybrid AI+Python)
**When documenting**: Use Workflow 5 (Modular Not Monolithic)
**When strategy feels off**: Use Workflow 6 (Strategic Pivot)
**When working**: Use Workflow 7 (Session Continuity)
**When deciding**: Use Workflow 8 (Direct Communication)

---

**These 8 workflows are proven.** Repeat them. Don't reinvent.
