# Render Deployments - Complete Inventory

**Updated**: Nov 24, 2025
**Account**: guitargnarr
**Active Deployments**: 1 confirmed

---

## ✅ Confirmed Live on Render

### 1. projectlavos-backend ⭐⭐⭐⭐
- **URL**: https://projectlavos-backend.onrender.com
- **Status**: ✅ Live, healthy (health endpoint responding)
- **Purpose**: FastAPI backend for projectlavos.com AI demos
- **Tech**: Python, FastAPI, 6 demo endpoints
- **Connected**: Serves guitar, demos, services frontends on Vercel
- **Path**: ~/Projects/projectlavos-backend
- **GitHub**: guitargnarr/projectlavos-backend
- **Cost**: $0/month (free tier)

---

## ⚠️ Render Configs Present (Not Deployed)

### 2. security-phishing-detector (Has render.yaml)
- **Path**: ~/Projects/Security-Tools/security-phishing-detector
- **Config**: render.yaml present (Docker service, free tier)
- **Actual deployment**: Railway (not Render)
- **URL**: https://phishguard-api-production-88df.up.railway.app
- **Reason**: Deployed to Railway instead (Nov 22)

### 3. personal-journey (Has render.yaml)
- **Path**: ~/Projects/Personal/personal-journey
- **Config**: render.yaml present (static site)
- **Actual deployment**: Vercel (personal-journey-flow)
- **Status**: Config exists but likely not deployed to Render

### 4. portfolio-website (Has render.yaml)
- **Path**: ~/Projects/Web-Development/portfolio-website
- **Config**: render.yaml present
- **Actual deployment**: Netlify (jaspermatters.com)
- **Status**: Config exists but deployed elsewhere

---

## 📊 Summary

**Live on Render**: 1 (projectlavos-backend)
**Render configs**: 4 total (1 deployed, 3 configs-only)
**Cost**: $0/month (free tier)

**Render role**: Minimal (1 backend service)
**Primary platforms**: Vercel (15 deployments), Railway (2), Netlify (1)

---

## Deployment Platform Distribution

**Vercel**: 15 live deployments (frontends, static sites)
**Render**: 1 deployment (projectlavos-backend)
**Railway**: 2 deployments (PhishGuard API, possibly Mirador)
**Netlify**: 1 deployment (jaspermatters.com portfolio)

**Total**: 19+ live deployments across 4 platforms

---

## Recommendations

**Keep on Render**:
- projectlavos-backend (working, no reason to move)

**Archive render.yaml files** (deployed elsewhere):
- security-phishing-detector (on Railway now)
- personal-journey (on Vercel)
- portfolio-website (on Netlify)

**Platform strategy**:
- Vercel: Frontends (Next.js, React, static)
- Railway: Backend APIs with Docker (Python/FastAPI)
- Render: Legacy backend (keep projectlavos-backend for now)
- Netlify: Static sites (jaspermatters.com)

---

**Render is not a focus platform.** Minimal usage (1 service), consider migrating to Railway if needed.
