# Content Pack — LaptopFinder AI

> Built with [ai-coding-rules](https://github.com/aiagentwithdhruv/ai-coding-rules) + [Claude Code](https://claude.ai/claude-code)

---

## LinkedIn Post (Copy-Paste Ready)

```
I built a full-stack AI product in one session.

No team. No Figma. No Jira tickets.
Just me + Claude Code + a 160-line CLAUDE.md file.

Here's what came out:

LaptopFinder AI — an AI-powered laptop recommendation engine.

→ Ask "best laptop for programming under $1500" in plain English
→ RAG pipeline searches 30+ laptops using pgvector
→ Streams structured recommendations with specs, pros, and trade-offs
→ Browse, filter, and compare side-by-side

The stack:
• Next.js 15 + TypeScript + Tailwind
• FastAPI + async SQLAlchemy + Pydantic
• PostgreSQL + pgvector (vector similarity search)
• OpenAI GPT-4o + text-embedding-3-small
• Deployed on Vercel + Render — $0/month

The secret? A CLAUDE.md file with 15 engineering rules:

Without rules → prototype-quality spaghetti code
With rules → clean 3-layer architecture, typed schemas, async I/O, proper error handling

The rules tell AI HOW to write code:
— Routes handle HTTP only (zero business logic)
— Services handle all business logic
— Repositories handle all database access
— Pydantic validates everything
— Config is centralized, never hardcoded

I used an n8n workflow to keep Render's free tier alive (pings every 14 min).

2 nodes. 30 seconds to set up. No cold starts.

Total cost: $0 hosting + ~$0.01 per AI query.

I open-sourced everything — the app, the rules, and the deployment guide.

The era of "AI can't write production code" is over.
You just need better instructions.

Want to learn how to build production AI systems like this?
I teach RAG, agents, full-stack AI, and deployment at euron.one — join 2200+ engineers already learning.

#AIEngineering #ClaudeCode #BuildInPublic #RAG #FullStack #n8n #OpenSource
```

**Attach:** Homepage screenshot + AI chat screenshot (side-by-side or carousel)

---

## First Comment (Post Immediately After)

```
📝 Full deep-dive article (architecture, prompts, deployment) → [paste LinkedIn article URL here]

All links:

🔗 Live demo → laptopfinder.aiwithdhruv.com
💻 Source code → github.com/aiagentwithdhruv/laptop-finder-ai
📐 AI coding rules (15 rules for Claude + Cursor) → github.com/aiagentwithdhruv/ai-coding-rules
☁️ AWS deployment reference → github.com/aiagentwithdhruv/conversa-ai
🌐 Portfolio → aiwithdhruv.com

What's in the repo:
• Full README with architecture diagram
• RAG system prompt (the exact prompt powering the AI chat)
• Free deployment guide (Vercel + Render + n8n keep-alive)
• Deployment cost comparison (6 options from $0 to $50/mo)
• n8n workflow JSON — import and activate
• AWS ECS Fargate guide with service-by-service cost breakdown

The AI coding rules repo has:
• 15 production-grade .mdc rules for Cursor
• Same rules as CLAUDE.md for Claude Code
• 9 project doc templates (PRD, Architecture, API Spec, DB Schema, Deployment)
• One-liner install script

Star the repos if this is useful ⭐

🎓 Want to build AI systems like this from scratch?
I teach RAG, agents, full-stack AI, and production deployment at euron.one
→ 2200+ engineers enrolled. Next cohort open now.
```

---

## Twitter/X Thread

```
Tweet 1 (Hook):
I built a full-stack AI product with 7 natural language prompts.

No manual coding. No boilerplate.

Here's the exact prompts I used 🧵

Tweet 2:
Prompt 1 — Architecture:
"Build a laptop recommendation system with AI chat. FastAPI + PostgreSQL + pgvector. Next.js frontend. Clean architecture — routes → services → repos."

Claude Code generated the entire project structure.

Tweet 3:
Prompt 2 — Database:
"Create the schema with laptops, specs, reviews, embeddings. Seed 30 laptops across 6 categories."

Got: Alembic migrations + full JSON seed data with realistic specs.

Tweet 4:
Prompt 3 — RAG Pipeline:
"Chunk laptop data, embed with text-embedding-3-small, store in pgvector, retrieve top 8, stream GPT-4o via SSE."

5 files generated. Full RAG pipeline.

Tweet 5:
Prompt 4 — Frontend:
"Home with hero + categories. Browse with filters. Detail page. AI chat with streaming. Comparison page."

Full Next.js 15 app. TypeScript. Tailwind. Dark theme.

Tweet 6:
Prompt 5 — Deploy:
"Deploy to Vercel + Render free tier. Custom domain."

render.yaml, env vars, DNS — all handled.

Tweet 7:
Prompt 6 — Keep-Alive:
"Render spins down after 15 min. Create n8n workflow to ping every 14 min."

2 nodes. Done.

Tweet 8:
Prompt 7 — Polish:
"Chat responses are unstructured. Fix the prompt + CSS."

Rewrote system prompt + styled markdown. Clean output.

Tweet 9:
The secret: a CLAUDE.md file with 15 engineering rules.

It tells AI HOW to write code.

Without it: prototype code.
With it: deployable code.

Tweet 10:
Everything is open source:

🔗 Live: laptopfinder.aiwithdhruv.com
🔗 Code: github.com/aiagentwithdhruv/laptop-finder-ai
🔗 Rules: github.com/aiagentwithdhruv/ai-coding-rules

AI can write production code.
You just need better instructions.

Tweet 11 (Reply):
Want to learn how to build RAG, agents, and full-stack AI systems like this?

I teach it all at euron.one — 2200+ engineers already learning.

From architecture to deployment. Production-grade.
```

---

## YouTube Video Outline

**Title:** "I Built a Full AI Product with 7 Prompts (No Manual Coding)"

```
HOOK (0:00 - 0:30)
[Show live demo] "This entire app was built with 7 prompts."

THE PRODUCT (0:30 - 2:00)
Walk through: homepage → browse → filters → detail → AI chat → compare

THE ARCHITECTURE (2:00 - 4:00)
VS Code: 3-layer architecture + RAG pipeline + pgvector + SSE streaming

THE 7 PROMPTS (4:00 - 8:00)
Show each prompt → what Claude Code generated → before/after

THE SECRET: CLAUDE.md (8:00 - 10:00)
Show the file. 15 rules. Side-by-side: code without vs. with rules.

DEPLOYMENT (10:00 - 12:00)
Vercel (60 sec) → Render → n8n keep-alive → $0/month vs AWS $35-50

CTA (12:00 - 12:30)
"Links in description. Star the repos. Subscribe."
```

**Description links:**
```
🔗 Live demo: https://laptopfinder.aiwithdhruv.com
💻 Source code: https://github.com/aiagentwithdhruv/laptop-finder-ai
📐 AI coding rules: https://github.com/aiagentwithdhruv/ai-coding-rules
☁️ AWS reference: https://github.com/aiagentwithdhruv/conversa-ai
🌐 Portfolio: https://aiwithdhruv.com
```

**Tags:**
```
claude code, ai coding, rag tutorial, fastapi nextjs, pgvector, ai product, build with ai, claude code tutorial, ai engineering, laptop recommendation ai, deploy for free, n8n automation, vercel render deployment
```

---

## YouTube Thumbnail Prompt (thumbnail-generator skill)

**Visual Hook:** #3 Pipeline Flow (Blue Metallic palette)
**Text Overlay:** "7 PROMPTS → **FULL AI APP**"

```
Wide-angle cinematic still, futuristic workspace with brushed aluminum and chrome surfaces. Young Indian male developer with short hair, trimmed beard, and glasses, wearing a plain black t-shirt, sitting confidently at natural wooden desk with arms resting on keyboard. The MacBook Pro screen shows a dark-themed AI chat interface with laptop recommendations, streaming response with emoji headings and structured specs. Floating around him: frosted glass UI panels showing the LaptopFinder homepage (dark theme, cyan accents, "Find Your Perfect Laptop" hero text) and a browse page with laptop cards grid. Above: a holographic pipeline "PROMPT → CLAUDE CODE → DEPLOY" with green checkmarks on each step, connected by glowing cyan arrows. On the left side, clean vertical badge-style labels: Next.js, FastAPI, pgvector, GPT-4o, Vercel — stacked neatly with colored brand icons. Small floating code snippet card bottom-right showing Python RAG pipeline code on frosted glass with teal neon border. Dark moody room with warm ambient light, bookshelf with plants softly blurred in background. Natural skin tones, warm room lighting with teal and gunmetal silver-blue neon accents only from the floating panels. Clean composition with breathing room between elements. Photorealistic, 8K, sharp focus, shallow depth of field, DSLR quality, cinematic color grading, 16:9 YouTube thumbnail ratio.
```

**Alt Prompt (LinkedIn 4:5):**
```
Cinematic portrait, dark moody workspace. Young Indian male developer with short hair, trimmed beard, and glasses, wearing a plain black t-shirt, looking at MacBook Pro screen showing a dark-themed laptop recommendation chat with structured AI responses. Single frosted glass panel floating behind him showing the LaptopFinder browse page with laptop cards. Small vertical badge list on left edge: Next.js, FastAPI, pgvector. Dark navy background, teal and gunmetal silver-blue ambient lighting, rim light from behind, cinematic shallow depth of field, 8K, sharp focus, hyperrealistic, 4:5 ratio.
```

---

## Hand-Drawn Diagram Prompt (handdrawn-diagram skill — paste in Gemini)

```
Hand-drawn whiteboard infographic on white lined notebook paper, sitting on a natural wooden desk surface visible at the edges. Black marker lines, cyan (#00D4FF) marker highlights, yellow highlighter on key numbers. Real marker ink texture, natural paper grain. Photo of a real whiteboard after a brainstorming session. 16:9 aspect ratio.

=== TOP TITLE BAR ===
Hand-written bold title: "LaptopFinder AI — Full-Stack RAG Product"
Below it: "Built with 7 Prompts. Deployed for $0/month." with yellow highlight on "7 Prompts" and "$0/month"
Cyan marker underline stroke under the main title.
TOP-RIGHT: "AiwithDhruv" in bold cyan marker inside a hand-drawn rounded rectangle badge. Smaller text below: "youtube | github | linkedin"

=== LEFT COLUMN — "Tech Stack" ===
Header: "Tech Stack" inside a hand-drawn box
Checklist with small hand-drawn logos next to each:
☑ Next.js 15 — small React logo
☑ FastAPI — small Python snake logo
☑ PostgreSQL + pgvector — small elephant logo
☑ OpenAI GPT-4o — small OpenAI logo
☑ Tailwind CSS — small wind logo
☑ Vercel + Render — small V and R logos

=== CENTER — "How It Works" (largest section) ===
Header: "How It Works" with a circle around it

Flowchart with boxes connected by hand-drawn arrows:
[BOX 1]: "User Asks Question" — subtitle: "Best laptop for programming?"
↓ arrow
[BOX 2]: "Embed Query" — subtitle: "text-embedding-3-small" with small OpenAI logo
↓ arrow
[BOX 3]: "pgvector Search" — subtitle: "Top 8 similar laptops" with small elephant logo
↓ arrow
[BOX 4]: "Stream GPT-4o" — subtitle: "Structured markdown response" with green checkmark badge

=== FLASH CARDS scattered around like sticky notes, tilted at slight angles ===

Yellow sticky note (tilted, near top-right):
"AI-Powered Chat"
"Ask anything about laptops"
"Streaming responses via SSE"
Small chat bubble doodle

Light Blue sticky note (tilted, near center-right):
"Browse & Filter"
"30+ laptops, 6 categories"
"Brand, price, specs filters"
Small laptop doodle

Pink sticky note (tilted, near bottom-left):
"Side-by-Side Compare"
"Up to 4 laptops"
"Highlighted winners per spec"
Small comparison table doodle

Light Green sticky note (tilted, near center-left):
"n8n Keep-Alive"
"Pings API every 14 min"
"Zero cold starts on free tier"
Small clock/gear doodle

Light Purple sticky note (tilted, near top-center):
"CLAUDE.md"
"15 engineering rules"
"Production-grade AI code"
Small file/document doodle

Some flash cards have paper clip or tape marks holding them on.

=== RIGHT COLUMN — "The App" ===
Header: "The App"
Hand-drawn browser window mockup showing:
— Dark-themed homepage with "Find Your Perfect Laptop" title
— Category cards row (Ultrabook, Gaming, Workstation, Business)
— "Ask AI" cyan button
— URL bar showing "laptopfinder.aiwithdhruv.com"

=== BOTTOM LEFT — Architecture Diagram ===
Three-layer architecture boxes connected by arrows:
[Routes] → "HTTP only"
↓ arrow
[Services] → "Business logic"
↓ arrow
[Repos] → "Database access"
Side label: "Clean Architecture" with cyan underline
Small logos: FastAPI, SQLAlchemy, Pydantic next to each layer

=== BOTTOM CENTER — Stats Row ===
Three items in a row, each circled with yellow highlight:
"$0/month"    "7 Prompts"    "30+ Laptops"
Small star doodles around the stats

=== BOTTOM RIGHT — Author + Branding ===
"AiwithDhruv" with cyan lightning bolt
"@aiwithdhruv" and "github.com/aiagentwithdhruv"
"AD" monogram in a hand-drawn circle

=== AMBIENT DETAILS ===
- Coffee ring stain near bottom-left (subtle)
- Paper clips on 1-2 flash cards
- Tape marks on corners of some sticky notes
- Blue pen lying on the desk
- Small doodle arrows and stars in empty spaces
- Wooden desk texture at all edges
- Faint "AiwithDhruv" watermark diagonally across center in light grey

=== STYLE — CRITICAL ===
- Real black marker on white paper — authentic hand-drawn feel
- Slightly imperfect handwriting but always readable
- Cyan for headers, connections, branding
- Yellow highlighter for numbers and stats
- Pastel colored sticky notes at slight angles
- Small recognizable tech logos hand-drawn next to every tool
- Everything hand-drawn — NO computer fonts
- Clean enough to read on a phone screen
```

---

## LinkedIn Article (Long-Form — Publish on LinkedIn)

**Title:** How I Built a Full-Stack AI Product With 7 Prompts and Deployed It for $0

**Subtitle:** The architecture, the prompts, the rules, and the deployment — everything I used to build LaptopFinder AI with Claude Code.

**Cover Image:** Use the hand-drawn architecture diagram (architecture-handdrawn.png)

**After publishing:** Add the article link to the First Comment above.

```
I built a full-stack AI product in one session. No team. No designer. No project manager. Just me, Claude Code, and a 160-line instruction file.

The result: LaptopFinder AI — an AI-powered laptop recommendation engine that lets you ask questions in plain English like "best laptop for programming under $1500" and get structured, spec-by-spec recommendations powered by a RAG pipeline.

Live demo: laptopfinder.aiwithdhruv.com
Source code: github.com/aiagentwithdhruv/laptop-finder-ai

In this article, I'll walk through exactly how I built it — the architecture, the 7 prompts I used, the engineering rules that made the AI write production-grade code, and how I deployed everything for $0/month.


## What LaptopFinder AI Does

[Insert: homepage screenshot — home-page.jpg]

Four core features:

1. AI-Powered Chat — Ask anything about laptops in plain English. The AI searches a database of 30+ laptops using vector similarity, then streams a structured response with specs, pros, cons, and trade-offs.

2. Browse & Filter — Browse all laptops with filters for brand, category, price range, and specs. Six categories: Ultrabook, Gaming, Workstation, Business, Budget, and Creative.

3. Laptop Detail Pages — Every laptop has a dedicated page with full specs, reviews, ratings, and a "Similar Laptops" section powered by pgvector similarity search.

4. Side-by-Side Comparison — Select up to 4 laptops and compare them spec-by-spec. The best value in each category gets highlighted.

[Insert: AI chat screenshot — ai-chat.jpg]


## The Tech Stack

Here's what powers the app:

Frontend:
• Next.js 15 (App Router) + TypeScript
• Tailwind CSS (dark theme)
• React Markdown for AI response rendering
• Deployed on Vercel

Backend:
• FastAPI (async Python)
• SQLAlchemy + asyncpg (async database access)
• Pydantic v2 (validation + schemas)
• Alembic (database migrations)
• Deployed on Render (free tier)

Database:
• PostgreSQL 16 with pgvector extension
• Vector similarity search (cosine distance)
• Hosted on Render (free tier)

AI:
• OpenAI GPT-4o (answer generation via streaming)
• text-embedding-3-small (1536-dim embeddings)
• Server-Sent Events (SSE) for real-time streaming


## The Architecture — Why It's Not Spaghetti Code

[Insert: hand-drawn architecture diagram — architecture-handdrawn.png]

Most AI-generated code is a mess. Everything in one file. No separation. No error handling. Breaks the moment you try to deploy.

This project is different because of clean 3-layer architecture:

Layer 1: Routes (HTTP only)
Routes handle requests and responses. Zero business logic. They just validate input, call a service, and return the result.

Layer 2: Services (Business logic)
All the actual logic — RAG retrieval, embedding generation, recommendation scoring, comparison logic — lives here. Services don't know about HTTP. They don't know about database queries. They just process data.

Layer 3: Repositories (Database access)
All SQL, ORM queries, and pgvector searches live here. Repositories don't know about business rules. They just fetch and store data.

Why this matters:
• Each layer can be tested independently
• You can swap the database without touching business logic
• You can swap the API framework without rewriting services
• It's the same architecture used by teams at scale


## The RAG Pipeline — How AI Chat Works

This is the most interesting part. When a user asks "best laptop for video editing under $2000", here's what happens:

Step 1: Embed the query
The user's question gets converted into a 1536-dimensional vector using OpenAI's text-embedding-3-small model.

Step 2: Vector search
pgvector searches the database using cosine similarity and returns the top 8 most relevant laptops. Each laptop was pre-embedded during data ingestion — combining name, brand, category, specs, and use cases into a single text chunk.

Step 3: Build context
The top 8 laptop results get formatted into structured context with full specs, prices, ratings, and pros/cons.

Step 4: Stream GPT-4o
The context + user question + a carefully crafted system prompt get sent to GPT-4o. The response streams back via Server-Sent Events (SSE), so the user sees the answer typing out in real time.

The system prompt is critical. It tells GPT-4o to:
• Always respond with structured markdown (### headings, tables, emoji labels)
• Include a comparison table when multiple laptops match
• End with a verdict section picking the best option
• Never hallucinate specs — only use the provided context
• Handle "no match" cases gracefully

The exact system prompt is in the repo: backend/app/rag/prompts.py


## The 7 Prompts That Built Everything

Here are the exact natural language prompts I gave Claude Code:

Prompt 1 — Architecture:
"Build a laptop recommendation system with AI chat. FastAPI + PostgreSQL + pgvector. Next.js frontend. Clean architecture — routes → services → repos."

Result: Complete project structure with 3-layer backend, Next.js 15 frontend, and all config files.

Prompt 2 — Database:
"Create the schema with laptops, specs, reviews, embeddings. Seed 30 laptops across 6 categories."

Result: Alembic migrations, SQLAlchemy models, and a full JSON seed file with realistic specs for 30+ laptops.

Prompt 3 — RAG Pipeline:
"Chunk laptop data, embed with text-embedding-3-small, store in pgvector, retrieve top 8, stream GPT-4o via SSE."

Result: 5 files — embedding service, retrieval service, RAG service, streaming endpoint, and system prompt.

Prompt 4 — Frontend:
"Home with hero + categories. Browse with filters. Detail page. AI chat with streaming. Comparison page."

Result: Full Next.js 15 app with TypeScript, Tailwind, and dark theme. All 5 pages with loading states and error handling.

Prompt 5 — Deploy:
"Deploy to Vercel + Render free tier. Custom domain."

Result: render.yaml blueprint, environment variable configs, and DNS setup instructions.

Prompt 6 — Keep-Alive:
"Render spins down after 15 min. Create n8n workflow to ping every 14 min."

Result: Complete n8n workflow JSON — 2 nodes, import and activate.

Prompt 7 — Polish:
"Chat responses are unstructured. Fix the prompt + CSS."

Result: Rewrote the system prompt for structured markdown output. Added custom CSS for dark-themed markdown rendering.

7 prompts. Full product. Deployed and live.


## The Secret — CLAUDE.md (15 Engineering Rules)

Here's what most people miss about AI coding: the AI is only as good as your instructions.

Without rules, Claude Code writes prototype-quality code — everything in one file, no error handling, hardcoded values, no types.

With a CLAUDE.md file containing 15 engineering rules, it writes production-grade code with clean architecture, typed schemas, async I/O, centralized config, and proper error handling.

The 15 rules cover:
• Routes handle HTTP only (zero business logic)
• Services handle all business logic
• Repositories handle all database access
• Pydantic validates every input and output
• Config is centralized, never hardcoded
• Use async I/O everywhere
• RESTful naming with API versioning
• Consistent error response structure
• Structured logging on critical paths
• Never hardcode secrets or environment-specific URLs
• Migrations for all schema changes
• Separate RAG ingestion from answer generation
• Health endpoints for every service
• Type hints everywhere
• Parameterized queries, no N+1 patterns

I open-sourced these rules as a standalone repo:
github.com/aiagentwithdhruv/ai-coding-rules

It includes:
• 15 .mdc rules for Cursor
• Same rules as CLAUDE.md for Claude Code
• 9 project doc templates (PRD, Architecture, API Spec, DB Schema, Deployment)
• One-liner install script

The difference between "AI can't write real code" and "AI wrote my entire product" is literally a 160-line instruction file.


## Deploying for $0/Month

The entire app runs for free:

Frontend (Vercel — Free):
• Push to GitHub → auto-deploys
• Custom domain: laptopfinder.aiwithdhruv.com
• Edge network, SSL, preview deploys — all included
• Setup: 60 seconds

Backend + Database (Render — Free):
• render.yaml blueprint → one-click deploy
• PostgreSQL 16 with pgvector extension
• Python backend with auto-builds
• Free tier: 750 hours/month, 256MB RAM

The one catch: Render's free tier spins down after 15 minutes of inactivity. First request after spin-down takes 30-50 seconds.

The fix: n8n keep-alive workflow.


## The n8n Keep-Alive Trick (Zero Cold Starts)

n8n is a free, self-hostable workflow automation tool. I created a 2-node workflow:

Node 1: Schedule Trigger — fires every 14 minutes
Node 2: HTTP Request — pings the backend health endpoint

That's it. The API never spins down. Zero cold starts. Free.

The workflow JSON is in the repo — import it into n8n and activate.

Other n8n use cases I use with this stack:
• Daily database backup alerts
• Weekly analytics digest (most searched laptops, popular queries)
• Price monitoring (scrape and update laptop prices)
• Uptime monitoring with Telegram/Slack alerts
• Nightly embedding refresh for new products
• SEO ping on content updates


## What If You Need More Scale?

If free tier isn't enough, here are the options I compared:

$0/month — Vercel + Render free tier + n8n keep-alive (what I use)
$7/month — Render Starter (no cold starts, 1GB RAM)
$20/month — Railway Pro (auto-scaling, managed Postgres)
$25/month — DigitalOcean (VPS + managed DB)
$35-50/month — AWS ECS Fargate (production-grade, auto-scaling)

For the AWS option, I have a full deployment guide with ECS Fargate, ALB, RDS, and service-by-service cost breakdown in my Conversa AI repo:
github.com/aiagentwithdhruv/conversa-ai


## The Numbers

• Total hosting cost: $0/month
• AI cost per query: ~$0.01 (GPT-4o streaming)
• Laptops in database: 30+ across 6 categories
• Backend response time: <2s (with n8n keep-alive active)
• Time to build: One session with Claude Code
• Lines in CLAUDE.md: 160


## Everything Is Open Source

Live demo: laptopfinder.aiwithdhruv.com
Source code: github.com/aiagentwithdhruv/laptop-finder-ai
AI coding rules: github.com/aiagentwithdhruv/ai-coding-rules
AWS deployment reference: github.com/aiagentwithdhruv/conversa-ai
Portfolio: aiwithdhruv.com

The repo includes:
• Full README with architecture diagram and screenshots
• The exact RAG system prompt powering the AI chat
• Free deployment guide (Vercel + Render + n8n)
• Deployment cost comparison (6 options from $0 to $50/month)
• n8n workflow JSON — import and activate
• AWS ECS Fargate guide with cost breakdown

Star the repos if this was useful.


## Want to Build AI Systems Like This?

I teach RAG, agents, full-stack AI, and production deployment at euron.one.

2200+ engineers enrolled. From architecture to deployment. Production-grade.

The era of "AI can't write production code" is over. You just need better instructions.

— Dhruv | aiwithdhruv.com
```

**Formatting notes for LinkedIn article editor:**
- Add H2 headers for each `##` section
- Bold key terms and tool names
- Insert screenshots at the marked `[Insert: ...]` points
- Add hyperlinks for all URLs (LinkedIn articles support clickable links)
- The hand-drawn architecture diagram makes a great cover image

**After publishing, update the First Comment to include:**
```
📝 Full deep-dive article → [paste LinkedIn article URL here]
```

---

## Carousel (LinkedIn/Instagram) — 7 Slides

```
Slide 1: "I Built a Full AI Product With 7 Prompts" [app screenshot]
Slide 2: "The Stack" — Next.js 15, FastAPI, PostgreSQL + pgvector, GPT-4o, $0/month
Slide 3: "Clean Architecture" — Routes → Services → Repos (no spaghetti)
Slide 4: "RAG Pipeline" — Embed → pgvector search → Stream GPT-4o
Slide 5: "The Secret" — CLAUDE.md with 15 rules = production-grade AI code
Slide 6: "Deployed for $0" — Vercel + Render + n8n keep-alive
Slide 7: "Open Source" — github.com/aiagentwithdhruv/laptop-finder-ai
```
