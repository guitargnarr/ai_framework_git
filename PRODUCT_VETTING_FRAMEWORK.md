# Product Vetting Framework - Give Every Repo Its Fair Shake

**Created**: Nov 23, 2025
**Purpose**: Systematic validation process before ANY archive decision
**Lesson**: Archive-Recovered-2025-11-18 incident - don't lose repos hastily

---

## ⚠️ The Archive Recovery Lesson

**What happened**: Repos were archived prematurely, had to be recovered (painful, time-consuming)

**The mistake**: Quick judgments ("this looks incomplete") without thorough investigation

**The principle**: **Every repo deserves investigation before archive decision.**

**This framework ensures**: 40 repos get fair assessment, data-driven decisions, no regrets.

---

## The Fair Shake Process (Per Repo)

### Phase 1: Deep Investigation (15-30 minutes)

**Not**: Surface-level README scan
**Actually**: Understand what it really does

**Steps**:
1. **Read all READMEs** (README.md, DEMO_README.md, etc.)
2. **Check commit history**: Recent? Active? Or abandoned?
3. **Run the code** (if possible): Does it actually work?
4. **Check dependencies**: Can it run? Missing pieces?
5. **Look for deployed versions**: Already live somewhere?

**Questions to answer**:
- What problem does this solve? (be specific)
- Who would use this? (real users, not hypothetical)
- Is it finished or half-baked? (functionality check)
- Why was this built? (was there a real need?)

**Output**: Detailed assessment, not quick judgment

---

### Phase 2: Market Validation (24 hours)

**Goal**: Get DATA, not revenue (yet)

**Option A: Pricing Test** (if product-ready)
```bash
# Add simple Stripe checkout
# Don't build full subscription system (overkill)
# Just: "Pay $5 to try" button
# Track: How many click? How many pay?
```

**Option B: Interest Test** (if not quite ready)
```bash
# Create landing page
# Add email signup ("Get notified when ready")
# Share on relevant community (Reddit, HN, Twitter)
# Track: Signups, comments, interest level
```

**Option C: Demo Test** (if unclear value)
```bash
# Deploy publicly
# Share with 5-10 target users
# Ask: "Would you use this? Why/why not?"
# Track: Actual user feedback (not assumptions)
```

**Time limit**: 24 hours to get initial data
**Don't**: Build for months before validating
**Do**: Test quickly, learn fast

---

### Phase 3: Data-Driven Decision

**Based on Phase 2 results**:

**IF**: Interest shown (signups, purchases, positive feedback)
**THEN**: ✅ Pursue (Tier 1: Commercial potential)
**ACTION**: Build more, iterate, scale

**IF**: No market interest BUT demonstrates valuable capability
**THEN**: ✅ Keep (Tier 3: Portfolio piece)
**ACTION**: Deploy for consulting leads, don't monetize directly

**IF**: No interest AND no consulting value
**THEN**: ⚠️ Investigate pivot potential
**ACTION**: Could it solve a different problem? Different audience?

**IF**: No interest, no demo value, AND pivot unlikely
**THEN**: ❌ Archive (ONLY after fair shake)
**ACTION**: Move to Archive/ with documentation of why

**The key**: Archive is LAST resort, after data shows it's not valuable.

---

## Application to 40 Repos

### Batch 1: Already Investigated (Fair Shake Complete)

**PhishGuard**: ✅ Deployed, working, real problem solved
**Decision**: Pursue (add pricing, test market)

**OurJourney**: ✅ Investigated thoroughly, personal tool, valuable for personal use
**Decision**: Keep (Tier 3: Personal, not commercial)

**reflexia**: ✅ Investigated, niche use case, complex dependencies
**Decision**: TBD (needs market test - would anyone actually use an Ollama orchestration layer?)

**prompt-showcase**: ✅ Already live, demonstrates expertise
**Decision**: Keep (consulting lead generator)

### Batch 2: Quick Dismissals (Need Fair Shake)

**knowledge-base**: ⚠️ Dismissed as "placeholder"
**Fair shake needed**: Actually investigate - what files exist? Is there hidden value?

**consciousness-experiments**: ⚠️ Dismissed as "experiment"
**Fair shake needed**: What experiments? Any working demos? Lessons learned?

**sentiment-analysis-api**: ⚠️ Dismissed as "not deployment-ready"
**Fair shake needed**: What does it do? Who needs sentiment analysis? Working code?

---

## The Vetting Template (Copy for Each Repo)

```markdown
## [Repo Name] Vetting Report

**Investigation Date**: YYYY-MM-DD
**Investigator**: [You/Claude]

### Phase 1: Understanding (15-30 min)

**What it does**: [Detailed description after reading all docs, running code]
**Target users**: [Specific personas, not "developers" or "people"]
**Problem solved**: [Concrete pain point, not vague "makes X easier"]
**Completeness**: [% finished, what's working, what's missing]
**Already deployed**: [URLs if live, where, when]

### Phase 2: Market Test (24 hours)

**Test method**: [Pricing/Interest/Demo - which chosen and why]
**Execution**: [What was built/shared/tested]
**Data collected**:
- Visitors: ___
- Signups/purchases: ___
- Feedback: [actual quotes]
- Interest level: High/Medium/Low/None

### Phase 3: Decision

**Commercial viability**: [Score 0-10, reasoning]
**Consulting value**: [Score 0-10, reasoning]
**Decision**: Pursue / Portfolio / Pivot / Archive
**Reasoning**: [Data-driven, not assumptions]

**If Archive**: Why? What data showed no value?
**If Pursue**: Next steps? What to build/improve?
```

---

## Commitment: Fair Shake for All 40

**Remaining to vet**: ~30 repos (10 already investigated)

**Process**:
1. Deep investigation (each repo)
2. Market validation (where applicable)
3. Data-driven decision (not quick judgment)
4. Document reasoning (so we remember why)

**Timeline**: Not rushed, systematic

**This prevents**: Hasty archive decisions we'll regret (like the recovery incident)

---

## The Revenue Challenge (Reframed)

**Not**: "Rush to monetize in 24 hours"

**Actually**: "Test market response in 24 hours, then decide"

**For PhishGuard**:
- Phase 1: ✅ Done (we know what it is, it works)
- Phase 2: Add Stripe, test $5 price point, measure response
- Phase 3: If interest → build more, if not → keep as portfolio

**For AI DevOps Toolkit**:
- Phase 1: ✅ Done (Oracle + Frontend tools work)
- Phase 2: Create Gumroad page, share in communities, measure interest
- Phase 3: If downloads → package properly, if not → keep for consulting demos

**The test**: Can we get ONE person interested (not buying yet, just interested)?

**If we can't get interest**: That's valuable data (market doesn't want this, or positioning is wrong).

---

**This framework ensures**: No repo gets archived without investigation and attempted validation.

**Archive only after**: Fair shake + market test + data shows no path forward.
