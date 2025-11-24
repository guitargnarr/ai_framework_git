# Railway Deployments - Complete Inventory

**Updated**: Nov 24, 2025
**Account**: Matthew David Scott
**Projects**: 2 (1 deployed, 1 ready)

---

## ✅ Live on Railway

### 1. phishguard-api (earnest-cat project) ⭐⭐⭐⭐⭐
- **URL**: https://phishguard-api-production-88df.up.railway.app
- **Status**: ✅ Live, healthy
- **Service**: PhishGuard ML API (email phishing detection)
- **Deployed**: Nov 22, 2025
- **Tech**: Python, FastAPI, scikit-learn, XGBoost
- **Mode**: Simple model (20ms response, 7-model ensemble available but not deployed)
- **Tests**: 32/38 passing
- **Path**: ~/Projects/Security-Tools/security-phishing-detector
- **GitHub**: guitargnarr/phishguard-ml
- **Cost**: $5/month credit (free tier)

**Endpoints**:
- /health - Health check (verified working)
- /classify - Phishing detection
- /stats - Usage statistics
- /docs - Swagger documentation

**Connected**: phishguard-ui.vercel.app (frontend calls this API)

---

## ⚡ Ready to Deploy (Railway Config Exists)

### 2. llm-engineer-demo (not yet deployed)
- **Path**: ~/Projects/AI-ML/llm-engineer-demo
- **Config**: railway.json created Nov 23
- **Status**: GitHub connected, ready for Railway
- **Tech**: FastAPI, multi-agent orchestration, RAG, JWT auth
- **Purpose**: Demonstrates enterprise LLM integration patterns
- **Blocker**: Needs Railway project creation (manual, interactive)
- **GitHub**: guitargnarr/llm-engineer-demo
- **Estimated**: 10 min to deploy (manual Railway dashboard setup)

**Why deploy**: Consulting lead generator (shows enterprise AI skills)

---

## 📊 Summary

**Live**: 1 (phishguard-api)
**Ready**: 1 (llm-engineer-demo)
**Cost**: $5/month credit (covers 1-2 services on free tier)

---

## Railway Strategy

**When to use Railway**:
- Backend APIs with Dockerfile
- Python/FastAPI services
- ML model serving
- Anything needing persistent compute

**Current usage**:
- PhishGuard API (working well, fast deploys)
- Ready: llm-engineer-demo

**Alternatives**:
- Vercel: Frontends only (serverless functions, not persistent APIs)
- Render: Similar to Railway (1 service there: projectlavos-backend)
- Could consolidate: Move projectlavos-backend to Railway

---

## Next Actions

**Immediate**:
- [ ] Deploy llm-engineer-demo (manual Railway project setup)
- [ ] Verify phishguard-api health (already done ✅)

**Consider**:
- [ ] Deploy full 7-model ensemble for PhishGuard (enterprise mode)
- [ ] Consolidate: Move projectlavos-backend from Render to Railway
- [ ] Use Railway for future backend APIs (consistent platform)

---

**Railway is strategic for backend APIs.** 1 live, working well, ready for more.
