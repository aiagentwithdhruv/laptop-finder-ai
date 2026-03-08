# LaptopFinder AI

> AI-powered laptop recommendation engine with RAG-based chat, smart filters, and side-by-side comparison. Built entirely with AI coding (Claude Code) — from architecture to production deployment.

**Live:** [laptopfinder.aiwithdhruv.com](https://laptopfinder.aiwithdhruv.com)

![Home Page](screenshots/home-page.jpg)

---

## What It Does

- **AI Chat** — Ask natural language questions like "Best laptop for programming under $1500" and get structured, context-aware recommendations powered by RAG + GPT-4o
- **Browse & Filter** — Filter 30+ laptops by brand, category, price range, and specs
- **Laptop Details** — Full spec sheets, reviews, highlights, and "Ask AI About This Laptop" button
- **Side-by-Side Compare** — Compare up to 4 laptops with highlighted winners per spec
- **Streaming Responses** — Real-time SSE streaming for chat (no waiting for full response)

## Screenshots

| Browse Laptops | Laptop Detail | AI Chat |
|:-:|:-:|:-:|
| ![Browse](screenshots/browse-laptops.jpg) | ![Detail](screenshots/laptop-detail.jpg) | ![Chat](screenshots/ai-chat.jpg) |

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| **Frontend** | Next.js 15, React 19, TypeScript, Tailwind CSS 4 |
| **Backend** | FastAPI (Python), async SQLAlchemy, Pydantic |
| **Database** | PostgreSQL 16 + pgvector (vector similarity search) |
| **AI/LLM** | OpenAI GPT-4o (chat), text-embedding-3-small (embeddings) |
| **RAG Pipeline** | Custom — ingestion → chunking → embedding → retrieval → generation |
| **Streaming** | Server-Sent Events (SSE) via sse-starlette |
| **Deployment** | Vercel (frontend) + Render (backend + DB) — **100% free tier** |
| **Keep-Alive** | n8n workflow (pings API every 14 min to prevent cold starts) |

---

## Architecture

```
┌─────────────────────┐     ┌──────────────────────────────┐
│   Next.js Frontend  │────▶│   FastAPI Backend (/api/v1)  │
│   (Vercel)          │     │   (Render)                   │
└─────────────────────┘     └──────────┬───────────────────┘
                                       │
                            ┌──────────┴───────────────────┐
                            │                              │
                    ┌───────▼──────┐            ┌──────────▼─────────┐
                    │  PostgreSQL  │            │   RAG Pipeline     │
                    │  + pgvector  │            │                    │
                    │              │            │  1. Embed query    │
                    │  • laptops   │◀───────────│  2. Vector search  │
                    │  • reviews   │            │  3. Build context  │
                    │  • embeddings│            │  4. Stream GPT-4o  │
                    │  • chat      │            │                    │
                    └──────────────┘            └────────────────────┘
```

**Clean Architecture (3 layers):**
```
Routes/Controllers  →  HTTP concerns only
Services            →  Business logic
Repositories        →  Database access (SQLAlchemy ORM)
```

---

## Built With AI Coding

This entire project was built using **[Claude Code](https://claude.ai/claude-code)** (Anthropic's AI coding agent) — from initial architecture to production deployment.

### How It Was Built

**No manual coding.** Every file was generated through natural language prompts to Claude Code. Here's the actual workflow:

1. **Architecture first** — Described the product vision, Claude generated the full project structure, database schema, API spec, and clean architecture patterns
2. **Backend** — Prompted for FastAPI with async SQLAlchemy, RAG pipeline, streaming chat, and pgvector integration
3. **Frontend** — Prompted for Next.js 15 with App Router, dark theme, responsive design, and SSE streaming
4. **Deployment** — Prompted to deploy to Vercel + Render free tier, fix DNS, and create n8n keep-alive
5. **Debugging** — Claude diagnosed and fixed production issues (SQL syntax conflicts with pgvector, SSE buffering, CORS, silent streaming errors)

### The Raw Prompts That Built This

These are the actual prompts (paraphrased) used to build the project end-to-end:

```
Prompt 1 (Architecture):
"Build a laptop recommendation system with AI chat.
Backend: FastAPI + PostgreSQL + pgvector.
Frontend: Next.js. Use clean architecture —
routes → services → repos. RAG pipeline for chat."

Prompt 2 (Database + Seed Data):
"Create the database schema with laptops, specs, reviews,
chat sessions, and embeddings. Seed with 30 realistic
laptops across ultrabook, gaming, workstation, business,
budget, and 2-in-1 categories."

Prompt 3 (RAG Pipeline):
"Build the RAG pipeline — ingest laptop data into chunks,
embed with text-embedding-3-small, store in pgvector,
retrieve top 8 by cosine similarity, and stream GPT-4o
responses via SSE."

Prompt 4 (Frontend):
"Build the frontend — home page with hero + categories,
browse page with filters (brand, category, price),
laptop detail page with specs + reviews, AI chat with
streaming, and side-by-side comparison page."

Prompt 5 (Deploy):
"Deploy frontend to Vercel, backend to Render free tier.
Set up custom domain laptopfinder.aiwithdhruv.com.
Fix any production issues."

Prompt 6 (Keep-Alive):
"Render free tier spins down after 15 min. Create an n8n
workflow that pings the API every 14 minutes to keep it alive."

Prompt 7 (Chat Formatting):
"AI chat responses look unstructured. Update the system prompt
for better markdown formatting with headings, emoji, spec
tables, and comparison tables. Style the frontend markdown
rendering for the dark theme."
```

### AI Coding Tools Used

| Tool | What It Did |
|------|-------------|
| **Claude Code** (Opus) | Architecture, all backend + frontend code, RAG pipeline, debugging, deployment |
| **CLAUDE.md** | Project-level instructions that guided Claude's code style, architecture patterns, and engineering standards |
| **.cursor/rules/** | 14 engineering rule files (FastAPI, Next.js, PostgreSQL, RAG, security, etc.) for AI-aware context |

> **Key insight:** The `CLAUDE.md` file (160 lines of engineering rules) made Claude Code produce production-grade code from the start — clean architecture, proper error handling, typed schemas, async patterns. Without it, you get prototype-quality code. With it, you get deployable code.

---

## The RAG System Prompt

This is the actual system prompt powering the AI chat recommendations (`backend/app/rag/prompts.py`):

```python
SYSTEM_PROMPT = """You are LaptopFinder AI — an expert laptop recommendation
assistant. Help users find the perfect laptop based on their needs, budget,
and preferences.

## Rules
- ONLY recommend laptops from the provided context below. Never invent
  or hallucinate laptop models.
- Explain WHY each laptop fits the user's needs with specific specs.
- When multiple options match, compare them and highlight trade-offs.
- Mention the price for every recommendation.
- If no laptops match, say so honestly and suggest adjusting requirements.

## Response Formatting (STRICT)
- Use ### headings for each laptop recommendation.
- Use bullet points with bold labels for specs.
- Use --- horizontal rules to separate multiple recommendations.
- Keep paragraphs short (2-3 sentences max).
- Use emoji sparingly: 💰 price, ⚡ performance, 🎮 gaming, 💼 work,
  🎨 creative, 📱 portability, 🔋 battery.

## Single Laptop Format
### 💻 [Brand Model]
**💰 Price:** $X,XXX

[1-2 sentences about why this laptop is a great fit.]

**Key Specs:**
- **Processor:** [CPU]
- **Graphics:** [GPU]
- **RAM / Storage / Display / Battery**

**✅ Pros:** [2-3 key strengths]
**⚠️ Trade-off:** [one honest limitation]

## Comparison Format
### 📊 Quick Comparison
| Feature | Laptop 1 | Laptop 2 |
|---------|----------|----------|
| Price   | $X,XXX   | $X,XXX   |

**🏆 Verdict:** [1-2 sentence recommendation]
"""
```

---

## Deploy Your Own (100% Free)

Everything runs on free tiers. Here's how:

### Prerequisites

- [Vercel](https://vercel.com) account (free)
- [Render](https://render.com) account (free)
- [OpenAI API key](https://platform.openai.com) (~$0.01-0.05 per chat query)
- [n8n](https://n8n.io) account (free, for keep-alive — optional)

### Step 1: Backend on Render

1. Fork this repo
2. Go to [Render Dashboard](https://dashboard.render.com) → **New** → **Blueprint**
3. Connect your forked repo — Render reads `render.yaml` automatically
4. Set environment variables:
   ```
   OPENAI_API_KEY=sk-your-key
   ```
5. Deploy — Render auto-creates the PostgreSQL database + web service
6. Once live, seed the database:
   ```bash
   curl -X POST https://your-app.onrender.com/api/v1/seed
   ```

### Step 2: Frontend on Vercel

1. Go to [Vercel](https://vercel.com) → **Import** → select your forked repo
2. Set root directory to `frontend`
3. Set environment variable:
   ```
   NEXT_PUBLIC_API_URL=https://your-app.onrender.com/api/v1
   ```
4. Deploy — takes ~60 seconds

### Step 3: Custom Domain (Optional)

1. In Vercel → Project Settings → Domains → Add `yoursubdomain.yourdomain.com`
2. Add a **CNAME** record in your DNS:
   ```
   Name:  yoursubdomain
   Value: cname.vercel-dns.com
   ```
3. Wait 1-2 minutes for propagation

### Step 4: Keep Render Alive with n8n

Render free tier spins down after 15 minutes of inactivity. The included n8n workflow prevents this:

1. Go to your n8n instance
2. Import `n8n-keepalive-workflow.json`
3. Update the URL in the "Ping Render API" node to your Render URL
4. Activate the workflow

**What it does:** Pings your API every 14 minutes with a lightweight `GET /laptops?limit=1` request, keeping the server warm.

```json
{
  "Schedule Trigger": "Every 14 minutes",
  "HTTP Request": "GET https://your-app.onrender.com/api/v1/laptops?limit=1",
  "Timeout": "60 seconds (handles cold start wake-up)"
}
```

> **Why n8n?** Most people use cron jobs or UptimeRobot for this. n8n gives you more control — you can add Slack/email alerts on failure, chain health checks, or integrate with your existing automation stack.

---

## n8n Use Cases (Beyond Keep-Alive)

n8n is a powerful workflow automation tool that pairs well with AI apps. Here are real use cases nobody talks about:

### 1. Keep-Alive for Free Tier Hosting _(included in this repo)_
**Problem:** Render/Railway free tier spins down after 15 min inactivity.
**Solution:** Schedule Trigger → HTTP Request every 14 min.
**Why n8n:** Can add error handling, alerts, and multi-service pings in one workflow.

### 2. Automated Database Seeding
**Workflow:** Schedule (daily) → HTTP POST `/api/v1/seed` → Slack notification
**Use case:** Auto-refresh laptop data from a Google Sheet or CSV, then re-seed the database.

### 3. AI Response Quality Monitoring
**Workflow:** Schedule (hourly) → POST `/chat` with test query → Check response quality → Alert if degraded
**Use case:** Catch when your RAG pipeline breaks (embedding service down, LLM errors) before users notice.

### 4. Review Aggregation Pipeline
**Workflow:** Webhook trigger → Scrape reviews from Amazon/BestBuy → POST to your API → Re-embed
**Use case:** Keep laptop reviews fresh by pulling from real sources and feeding into your RAG system.

### 5. Cost Monitoring
**Workflow:** Schedule (daily) → Check OpenAI usage API → Calculate daily spend → Alert if over budget
**Use case:** Prevent surprise API bills when your AI chat goes viral.

### 6. User Query Analytics
**Workflow:** Webhook from chat endpoint → Log to Google Sheets → Weekly summary email
**Use case:** Understand what users are actually asking for — informs which laptops to add next.

---

## API Endpoints

```
GET  /api/v1/laptops              # List with filters (brand, category, price, sort)
GET  /api/v1/laptops/search?q=    # Full-text search
GET  /api/v1/laptops/{id}         # Laptop detail with specs + reviews
GET  /api/v1/laptops/brands       # All brands
GET  /api/v1/laptops/categories   # All categories
POST /api/v1/chat                 # AI chat (SSE streaming response)
POST /api/v1/compare              # Side-by-side comparison
GET  /api/v1/health               # Health check
POST /api/v1/seed                 # Seed database (admin)
```

---

## Project Structure

```
├── backend/
│   ├── app/
│   │   ├── api/routes/          # HTTP controllers (thin)
│   │   ├── services/            # Business logic
│   │   ├── repositories/        # Database access (SQLAlchemy)
│   │   ├── models/              # ORM models
│   │   ├── schemas/             # Pydantic request/response
│   │   ├── rag/                 # RAG pipeline
│   │   │   ├── prompts.py       # System prompt + templates
│   │   │   ├── embeddings.py    # OpenAI text-embedding-3-small
│   │   │   ├── retriever.py     # pgvector similarity search
│   │   │   ├── ingestion.py     # Chunk + embed documents
│   │   │   └── generator.py     # LLM streaming (GPT-4o)
│   │   ├── core/                # Database + exceptions
│   │   └── config.py            # Centralized settings
│   ├── alembic/                 # Database migrations
│   ├── seed_data/laptops.json   # 30 laptops with full specs
│   └── requirements.txt
│
├── frontend/
│   ├── app/                     # Next.js App Router
│   │   ├── page.tsx             # Home (hero + categories)
│   │   ├── chat/page.tsx        # AI Chat (SSE streaming)
│   │   ├── laptops/page.tsx     # Browse + filters
│   │   ├── laptops/[id]/        # Laptop detail
│   │   └── compare/page.tsx     # Side-by-side comparison
│   ├── lib/api.ts               # Centralized API client
│   └── types/                   # TypeScript interfaces
│
├── screenshots/                 # App screenshots
├── render.yaml                  # Render deployment config
├── docker-compose.yml           # Local dev (PostgreSQL + pgvector)
├── n8n-keepalive-workflow.json  # n8n keep-alive workflow
├── CLAUDE.md                    # AI coding instructions
└── .env.example                 # Environment template
```

---

## Run Locally

```bash
# 1. Clone
git clone https://github.com/aiagentwithdhruv/laptop-finder-ai.git
cd laptop-finder-ai

# 2. Start PostgreSQL with pgvector
docker compose up -d db

# 3. Backend
cd backend
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
cp ../.env.example .env  # Add your OPENAI_API_KEY
alembic upgrade head
uvicorn app.main:app --reload

# 4. Frontend (new terminal)
cd frontend
npm install
npm run dev

# 5. Seed database
curl -X POST http://localhost:8000/api/v1/seed

# Open http://localhost:3000
```

---

## Environment Variables

```env
# Backend (Render)
DATABASE_URL=postgresql+asyncpg://user:pass@host:5432/dbname
OPENAI_API_KEY=sk-your-openai-key

# Frontend (Vercel)
NEXT_PUBLIC_API_URL=https://your-backend.onrender.com/api/v1
```

---

## Built By

**[Dhruv Tomar](https://aiwithdhruv.com)** — AI Solutions Architect

- Portfolio: [aiwithdhruv.com](https://aiwithdhruv.com)
- GitHub: [@aiagentwithdhruv](https://github.com/aiagentwithdhruv)
- LinkedIn: [/in/aiwithdhruv](https://linkedin.com/in/aiwithdhruv)
- YouTube: [@aiwithdhruv](https://youtube.com/@aiwithdhruv)

---

## License

MIT
