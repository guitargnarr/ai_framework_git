# Database Inventory - Complete System

**Updated**: Nov 24, 2025
**Total databases found**: 20+ SQLite files
**Cloud/Remote databases**: 0 confirmed
**Strategy**: Privacy-first, local databases (no hosting costs)

---

## 🎯 Active Databases (In Use)

### 1. job-search-automation
- **File**: `job_search.db` (SQLite)
- **Type**: SQLite + aiosqlite (async)
- **Purpose**: Job applications, email history, resume versions
- **Size**: Active (81 jobs tracked)
- **Config**: Can use PostgreSQL (option in .env.example, not active)
- **Location**: ~/Projects/job-search-automation/

---

### 2. Mirador Systems (Multiple instances)
- **Files**:
  - `mirador_memory.db` (main)
  - `mirador_healthcare_cache.db` (Norton pilot)
  - `technical_translator_crm.db` (CRM data)
  - `healthcare_cache.db` (Docker instance)
- **Type**: SQLite (local, HIPAA-compliant by design)
- **Purpose**: AI agent conversation history, healthcare data cache
- **Locations**:
  - ~/Projects/Security-Tools/mirador-test/
  - ~/Projects/AI-ML/AI-Framework-Unified/
  - ~/Projects/career-pivot/

**Strategic**: Local SQLite = privacy-first = HIPAA-compliant = competitive advantage

---

### 3. tool-gmail-integration / gmail-automation-system
- **Files**:
  - `email_tracking.db`
  - `job_applications.db`
- **Type**: SQLite
- **Purpose**: Gmail automation, email classification, job tracking
- **Locations**:
  - ~/Projects/tool-gmail-integration/
  - ~/Projects/gmail-automation-system/
- **Note**: May be superseded by job-search-automation

---

### 4. OurJourney (Personal)
- **File**: `ourjourney.db`
- **Type**: SQLite
- **Purpose**: Couples wellness, relationship tracking, custody schedule
- **Location**: ~/Projects/Personal/personal-journey/

---

### 5. apartment-leasing-demo
- **File**: `apartment_leasing.db`
- **Type**: SQLite
- **Purpose**: Demo data for apartment leasing app
- **Location**: ~/Projects/Portfolio/apartment-leasing-demo/backend/

---

### 6. consciousness-experiments
- **File**: `consciousness_tracking.db`
- **Type**: SQLite
- **Purpose**: AI consciousness detection experiment data
- **Location**: ~/Projects/AI-ML/consciousness-experiments/

---

## 📦 Vector Databases (Embeddings/RAG)

### 7. reflexia-model-manager
- **File**: `chroma.sqlite3` (ChromaDB)
- **Type**: Vector database (sentence embeddings)
- **Purpose**: RAG (Retrieval-Augmented Generation)
- **Locations**:
  - ~/Projects/reflexia-model-manager-restored/vector_db_backup_final/
  - Archive versions also exist

---

## 🗄️ Archive/Historical (Not Active)

**In Archive-Recovered-2025-11-18**:
- financeforge: `finance.db`
- Gmail tools: `email_tracking.db`, `job_applications.db`
- OurJourney: `ourjourney.db`
- Mirador: `mirador_memory.db`
- reflexia: ChromaDB files

**Status**: Historical backups, not actively used

---

## 📊 Database Summary

**By Type**:
- SQLite: 15+ files (local, file-based)
- ChromaDB: 2+ instances (vector embeddings)
- PostgreSQL: 0 active (configs exist, not deployed)
- MongoDB/MySQL: 0

**By Status**:
- Active: 6-8 databases
- Archive: 10+ historical backups

**By Purpose**:
- Job search/career: 4-5 databases
- Mirador/AI: 3-4 databases
- Personal tools: 2-3 databases
- Demos/experiments: 2-3 databases

---

## 🔒 Privacy-First Architecture (Strategic Advantage)

**Why all local databases**:
- **HIPAA compliance**: No cloud data = no HIPAA risk (Mirador advantage)
- **Privacy**: User data never leaves their machine (jobtrack, OurJourney)
- **Cost**: $0 database hosting (vs $25-100/month for managed Postgres)
- **Simplicity**: No database migrations, backups, connection pooling

**This is a feature, not a limitation.**

---

## 🚀 Production Database Strategy

**Current** (all projects):
- SQLite for local/single-user
- No cloud databases deployed

**If scaling** (future):
- **Mirador**: Keep SQLite (privacy is selling point)
- **job-search**: Add PostgreSQL option for SaaS (multi-user)
- **PhishGuard**: Stateless (no database needed)

**Don't**: Rush to add databases before validating SaaS model
**Do**: SQLite is fine for MVP, add Postgres when you have paying users

---

## 📋 Database Backup Status

**Active databases** (should backup):
- job_search.db (81 jobs tracked - valuable data!)
- mirador_memory.db / healthcare_cache.db (Norton pilot data)
- ourjourney.db (personal data)

**Backup method**:
```bash
# These are already in git repos (committed as data files)
# If not committed: Add to .gitignore, backup separately
# Or: Commit small databases (<10MB) to git
```

**Risk**: Databases are local files - if disk fails, data lost (unless backed up to GitHub or cloud)

---

## 🎯 Key Insights

**Pattern**: Privacy-first, local-first architecture across all projects

**Advantage**:
- HIPAA compliance (Mirador)
- Privacy positioning (jobtrack, OurJourney)
- Zero hosting costs
- Simple deployment

**Trade-off**:
- Single-user (not multi-tenant SaaS ready)
- No cloud sync (jobtrack could add as premium feature)

**Strategic**: This is your positioning - "privacy-first AI" (competitive advantage, not technical debt)

---

**All projects use local databases. This is intentional, strategic, and valuable.**
