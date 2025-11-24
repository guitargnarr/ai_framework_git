# 40 Projects in 3 Months: What I Learned Leaving Humana

*A transparent account of career transition, building with AI, and figuring out what actually works*

---

I left Humana in August 2025 after 10 years. Stable job, known path, comfortable.

Then: Uncertainty.

What do you build when everything feels urgent? How do you know what's valuable when you have 40 ideas and no focus?

I built them all. Some worked. Most didn't. Here's the honest account.

---

## The Setup: Too Many Ideas, No Filter

**August-November 2025**: Built 40 projects.

Email security tools. Job search automation. Healthcare AI. Guitar learning apps. Consciousness experiments. Documentation systems. Deployment tools.

Everything that seemed interesting, I built.

**The question I couldn't answer**: Which ones actually matter?

**The temptation**: Deploy everything, maybe something sticks.

---

## The Mistakes (What I Got Wrong)

### 1. Archive-Recovery Incident

I archived projects too quickly.

"This looks incomplete" → Move to Archive folder.

Weeks later: "Wait, I need that code" → Spend hours recovering.

**Lesson**: Give everything a fair shake. 15-30 min investigation prevents recovery waste.

**The framework I built**: Fair Shake Process (investigate deeply → test if applicable → decide with data → archive only after proving no value)

### 2. The Documentation Explosion

I love frameworks.

Built comprehensive guides, workflows, assessment tools. Grew to 4,500 lines of documentation.

Then realized: I was documenting possibilities, not outcomes.

**Purged 82%** (down to 800 lines of actually useful stuff).

**Lesson**: Document what worked (outcomes), not what might work (speculation).

### 3. Building Tools Instead of Using What Exists

Built a Deployment Oracle (AI tool to assess which of 40 projects were valuable).

Spent 2 days building, testing, fixing (small AI models can't do arithmetic - had to make it hybrid Python+AI).

Then discovered: I already had projects with validation data (pilot interest, personal use traction, technical proof).

**Lesson**: Audit before building. Understand what you have before creating tools to find it.

---

## The Breakthroughs (What Actually Worked)

### 1. Hybrid AI+Python

**The failure**: Small AI model scored all 40 projects identically (couldn't differentiate).

**The discovery**: llama3.2:1b can't do arithmetic. It pattern-matches ("B+ seems reasonable") but doesn't count points.

**The fix**: Python does math (deterministic scoring), AI does qualitative (recommendations).

**Tools I built with this**:
- Deployment Oracle: Instant repo assessment (0-100 score, platform recommendation)
- Elite Frontend: Generates 85% correct Next.js code (I fix the other 15%)

**Why this matters**: Use AI for what it's good at (code generation), Python for what it's good at (math, logic). Hybrid beats pure AI.

---

### 2. Rapid Deployment (30-Minute Full-Stack)

**Proven 4 times**:
- PhishGuard (email security): Backend API (Railway) + Frontend demo (Vercel)
- jaspermatters (ML portfolio showcase)
- FretForge (guitar learning)
- llm-engineer-demo (enterprise AI patterns)

**The pattern**:
1. Backend to Railway (15 min: fix PORT env var, create railway.json, deploy)
2. Frontend with Elite Frontend (5 min: AI generates component, I fix imports)
3. Next.js project (5 min: create-next-app, copy code)
4. Deploy to Vercel (5 min: vercel --prod, disable auth)

**Total**: 30 minutes, repeatedly.

**The catch**: AI generates B+ code (85% correct). Human adds the 15% (Icon imports, API fields, edge cases).

**Why this works**: AI scaffolds, human QA's. Fast + quality (not choose one).

---

### 3. Fair Shake Prevents Regrets

**After Archive-Recovery incident**, I built systematic vetting:
- Every project gets 15-30 min investigation (not quick scan)
- Check: What it does, who needs it, is it finished, does it work
- Decide: Only after thorough assessment

**Results**: Found capabilities I would've dismissed:
- Norton pilot data (almost archived as "just an experiment")
- Job search traction (81 applications, 14.3% response rate)
- PhishGuard technical depth (7-model ensemble, not just demo)

**Lesson**: Thoroughness up front > Recovery work later.

---

### 4. Transparency Builds Trust

**Most people hide**:
- AI limitations (don't mention models can't do math)
- Mistakes (Archive-Recovery incident)
- Process (how things actually get built)
- State (no revenue, still building)

**I show**:
- Limitations and fixes (hybrid approach)
- Mistakes and lessons (fair shake framework)
- Process (built with Claude Code, 85% AI + 15% human)
- State (3 months in, capability proven, customers TBD)

**Why**: Honesty differentiates. Everyone claims authority. Few share struggle.

**Result**: This article exists because of that transparency.

---

## The Outcomes (3 Months of Building)

**Tangible**:
- 18 live deployments (all public, all testable)
- 26 GitHub repositories (see the code)
- Tools that work (Deployment Oracle, Elite Frontend)
- 55 commits in last 2 days alone (Nov 22-24)

**Methodologies proven**:
- Fair Shake (prevents archive regrets)
- Hybrid AI+Python (reliable, each does what it's good at)
- Rapid deployment (30 min full-stack, 4/4 success)
- Building in public (this article is part of it)

**Honest state**:
- Capability: Proven (can build, can ship, can deploy fast)
- Validation: Some exists (pilot interest, traction data, technical proof)
- Revenue: $0 (no paying customers yet)
- Next: Build online trust, then outreach

---

## What This Taught Me (Lessons for Anyone in Similar Position)

**If you're leaving a job**:
- Build multiple things (won't know what works until you try)
- Give each fair assessment (prevent regret from hasty decisions)
- Document outcomes (not possibilities)

**If you're working with AI**:
- Hybrid > Pure AI (use each for strengths)
- 85% AI + 15% human = production quality
- Be transparent (show AI assistance, not hide it)

**If you're struggling with focus**:
- Vetting reveals validation (I found it in existing projects)
- Infrastructure helps, but can become its own delay
- Test: "Does this get me closer to a customer?" (if no, defer)

**If you're building in public**:
- Transparency differentiates (everyone hides struggle)
- Share mistakes (builds more trust than claims)
- Honest about state (3 months in, learning, no revenue yet)

---

## Where I Am Now (The Honest Answer)

**What I have**:
- Technical capability (18 deployments prove I can build)
- Some validation (pilot testing, personal use that works, measurable outcomes)
- Methodology (fair shake, hybrid AI, rapid deploy)

**What I don't have**:
- Paying customers
- Established online presence (working on it - this article is part of that)
- Certainty about what comes next

**What I'm doing**:
- Building online trust (LinkedIn optimization, publishing articles)
- Preparing outreach (when online presence exists)
- Continuing to build and learn

**The gap**: Capability → Trust → Customers

**The work**: Publishing this article (and 3 more), establishing presence, then executing outreach.

---

## The Invitation

**If you're going through similar**:
- Career transition (left job, building new path)
- Working with AI (trying to figure out what actually works)
- Building in public (struggling with what to share)

**Let's connect.** Not to sell you anything. Just to compare notes with someone who's been there.

**If you're exploring AI for your organization**:
- Healthcare (privacy-first architecture interests you)
- Automation (rapid deployment capability matters)
- Tools (deployment assessment, code generation)

**Let's talk.** No pitch. Honest conversation about needs and capabilities.

---

**Matthew Scott**
Louisville, KY
3 months post-Humana, building with AI, learning in public

*GitHub: guitargnarr (26 repos)*
*Live demos: 18 deployments*
*Built with: Claude Code (AI-assisted, transparently)*

---

**This is the real story.** 3 months of building, mistakes included, still figuring it out.

If that resonates, you know where to find me.
