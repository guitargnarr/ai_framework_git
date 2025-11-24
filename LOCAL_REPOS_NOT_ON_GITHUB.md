# Local Repos Not on GitHub - Backup Gap Analysis

**Updated**: Nov 24, 2025
**Total local repos**: 40
**On GitHub**: 26
**Missing from GitHub**: 28 (14 need backup, 14 can archive)

---

## 🚨 CRITICAL: Deployed But Not on GitHub (Backup Risk!)

### 1. security-phishing-detector ⚠️ URGENT
- **Status**: Deployed to Railway (live production API)
- **URL**: https://phishguard-api-production-88df.up.railway.app
- **Problem**: NOT on GitHub (only phishguard-ml and phishguard-ui are)
- **Risk**: If local disk fails, lose production code
- **Action**: `gh repo create` IMMEDIATELY

**Note**: This repo IS on GitHub as "phishguard-ml" but local folder name doesn't match.

---

## ⚡ High Value (Should Push to GitHub)

**Production/Enterprise Quality**:
2. **fretforge-v1** - Deployed to Vercel, no GitHub backup
3. **portfolio-website** - jaspermatters.com source, needs backup

**Tools/Infrastructure**:
4. **mcp-vercel** - Vercel MCP integration (useful tool)

**Demos Worth Keeping**:
5. **jcps-boots** - School transfer tool (demonstrates UX)
6. **web-ziggy-dashboard** - AI metacognition demo
7. **ideapond** - Idea incubator (pivot potential)

---

## ⚠️ Medium Value (Consider Publishing)

**Career Tools**:
8. **career-automation** - Job search scripts (superseded but has learnings)
9. **tool-gmail-integration** - Gmail automation

**AI/ML Experiments**:
10. **ai-orchestrator** - AI workflow management (80% complete)
11. **AI-Framework-Unified** - Framework placeholder

**Music Projects**:
12. **music-fretforge** - Original fretforge version
13. **music-fretvision-app** - Music visualization
14. **music-fretvision-github** - GitHub version?
15. **music-guitar-tools** - Guitar utilities

**Personal**:
16. **personal-journey** - Portfolio version
17. **personal-journey-flow** - Couples wellness app
18. **personal-vision-board** - Goal tracking

---

## ❌ Low Value (Archive Locally, Don't Push)

**Duplicates**:
19. **security-phishing-detector.backup** - Backup copy (keep main only)
20. **reflexia-model-manager-restored** - Restored version (original on GitHub)

**Experiments/Incomplete**:
21. **consciousness-experiments** - Academic research (no product value)
22. **ollama-experiments** - Test scripts (reference only)
23. **knowledge-base** - Placeholder (20% complete)

**Worktrees** (temporary branches):
24. **email-notifications** - Git worktree (temporary)
25. **phishguard-features** - Git worktree (temporary)

**Career/Job (Superseded)**:
26. **career-job-tools** - Superseded by job-search-automation

**Other**:
27. **portfolio-goldmine-revealed** - Unknown purpose
28. **mirador-test** - Test environment

---

## 📊 Backup Priority

**URGENT** (push today):
1. security-phishing-detector (or verify it's phishguard-ml)
2. fretforge-v1 (deployed, no backup)
3. portfolio-website (jaspermatters.com source)

**HIGH** (push this week):
4-7. mcp-vercel, jcps-boots, web-ziggy, ideapond

**MEDIUM** (optional):
8-18. Tools, demos, personal projects

**SKIP** (archive locally):
19-28. Duplicates, experiments, worktrees

---

## Actions

### Immediate Backup (3 repos)

```bash
# 1. Verify security-phishing-detector
cd ~/Projects/Security-Tools/security-phishing-detector
git remote -v  # Check if already connected to phishguard-ml

# 2. Backup fretforge-v1
cd ~/Projects/fretforge-v1
gh repo create fretforge-v1 --public --source=. --push

# 3. Backup portfolio-website
cd ~/Projects/Web-Development/portfolio-website
gh repo create portfolio-website --public --source=. --push
```

### Worktree Cleanup (2 temporary branches)

```bash
# These are git worktrees (temporary), not standalone repos
cd ~/Projects/projectlavos-backend  # Or wherever main repo is
git worktree list
git worktree remove email-notifications
git worktree remove phishguard-features
```

---

## GitHub Gap Analysis

**On GitHub**: 26 repos (good coverage)
**Should add**: 3 urgent (deployed without backup)
**Optional**: 10 medium-value demos/tools
**Don't push**: 14 low-value (duplicates, experiments, archives)

---

**Priority**: Backup the 3 deployed-but-not-on-GitHub repos (data loss risk).
