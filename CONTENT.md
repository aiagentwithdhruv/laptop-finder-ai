# Content Pack — LaptopFinder AI

> Ready-to-post content for LinkedIn, YouTube, and Twitter/X.
> Built with the [ai-coding-rules](https://github.com/aiagentwithdhruv/ai-coding-rules) framework.

---

## LinkedIn Posts

### Post 1: The Build Story (Hero Post)

```
I built a full-stack AI product in one session.

No team. No Figma. No Jira tickets.
Just me + Claude Code + a 160-line CLAUDE.md file.

Here's what came out:

LaptopFinder AI — an AI-powered laptop recommendation engine.

What it does:
→ Ask "best laptop for programming under $1500" in plain English
→ AI searches 30+ laptops using RAG + pgvector
→ Streams structured recommendations with specs, pros, and trade-offs
→ Browse, filter, and compare laptops side-by-side

The stack:
• Frontend: Next.js 15 + TypeScript + Tailwind
• Backend: FastAPI + async SQLAlchemy + Pydantic
• Database: PostgreSQL + pgvector (vector similarity search)
• AI: OpenAI GPT-4o + text-embedding-3-small
• Deployment: Vercel + Render — $0/month

The secret sauce?

A CLAUDE.md file with 15 engineering rules that made the AI write production-grade code from the start:
— Clean 3-layer architecture (routes → services → repos)
— Typed schemas everywhere
— Async I/O
— Proper error handling
— Centralized config

Without these rules → you get prototype-quality spaghetti code.
With these rules → you get deployable, maintainable code.

I open-sourced the rules: github.com/aiagentwithdhruv/ai-coding-rules

Live demo: laptopfinder.aiwithdhruv.com
Full code: github.com/aiagentwithdhruv/laptop-finder-ai

The era of "AI can't write production code" is over.
You just need the right instructions.

#AIEngineering #ClaudeCode #BuildInPublic #RAG #FullStack
```

**Visuals:** Screenshot of homepage + screenshot of AI chat response side-by-side

---

### Post 2: The Architecture Breakdown (Educational)

```
How I architect every AI product — a 3-layer system that scales.

Most AI projects fail because they dump everything in one file.
Here's the architecture I use for every production AI app:

Layer 1: Routes (HTTP only)
→ Receives requests, validates input, returns responses
→ ZERO business logic here

Layer 2: Services (brain)
→ All business logic lives here
→ Orchestrates repos, calls AI, applies rules

Layer 3: Repositories (database)
→ All SQL/ORM queries here
→ Services never touch the database directly

For AI features, add a RAG layer:
→ Ingestion: chunk documents → embed → store in pgvector
→ Retrieval: embed query → similarity search → top K results
→ Generation: context + query → stream LLM response

This is exactly how LaptopFinder AI works:
• User asks a question
• Backend embeds the query (text-embedding-3-small)
• pgvector finds the 8 most relevant laptop chunks
• GPT-4o generates a structured recommendation
• Response streams back via Server-Sent Events

Result? Sub-second first token. Grounded answers. No hallucination.

I teach these patterns in my open-source engineering rules:
github.com/aiagentwithdhruv/ai-coding-rules

15 rules. Works with Claude Code + Cursor.
One file changes how AI writes your code.

#SystemDesign #AIArchitecture #RAG #SoftwareEngineering
```

**Visuals:** Architecture diagram from README (ASCII or hand-drawn via handdrawn-diagram skill)

---

### Post 3: The $0 Deployment (Practical)

```
I deployed a full AI product for $0/month.

Not a demo. Not localhost.
A production app with a custom domain, AI chat, and a real database.

Here's the exact setup:

Frontend → Vercel (free)
• Next.js auto-deploys on git push
• Custom subdomain via CNAME record
• 100GB bandwidth/month — more than enough

Backend → Render (free)
• FastAPI + PostgreSQL + pgvector
• Auto-deploys from GitHub
• Catch: spins down after 15 min inactivity

The fix for Render cold starts?

I created an n8n workflow that pings the API every 14 minutes.
2 nodes. 30 seconds to set up. Problem solved.

Schedule Trigger (every 14 min) → HTTP GET /laptops?limit=1

The only cost: ~$0.01-0.05 per AI chat query (OpenAI API).
At 100 queries/day, that's ~$3-5/month.

Total: $0 hosting + $3-5 API costs.

Most people think production AI apps need AWS ($50+/mo).
For side projects and portfolios? Free tier is enough.

Full deployment guide in the README:
github.com/aiagentwithdhruv/laptop-finder-ai

n8n keep-alive workflow included (just import and activate).

What are you paying for hosting that should be free?

#FreeHosting #n8n #Vercel #Render #DevOps #BuildInPublic
```

**Visuals:** Cost comparison table from README

---

### Post 4: The RAG Prompt (Technical Deep Dive)

```
The prompt that makes my AI actually useful (not generic).

Most AI chatbots give vague, hallucinated answers.
Mine gives structured, grounded recommendations every time.

The difference? 50 lines of system prompt engineering.

Here's what I enforce:

1. ONLY recommend from retrieved context
→ No hallucinated laptop models
→ If nothing matches, say so honestly

2. Structured markdown output (strict)
→ ### headings for each laptop
→ Bold labels for specs
→ Emoji for visual hierarchy (💰⚡🎮💼)
→ Horizontal rules between recommendations

3. Format template the LLM must follow:

### 💻 [Brand Model]
**💰 Price:** $X,XXX
[Why it fits in 1-2 sentences]
**Key Specs:** Processor, GPU, RAM, Storage, Display, Battery
**✅ Pros:** 2-3 strengths
**⚠️ Trade-off:** One honest limitation

4. Comparison format with tables:

| Feature | Laptop 1 | Laptop 2 |
|---------|----------|----------|
| Price   | $X,XXX   | $X,XXX   |

**🏆 Verdict:** 1-2 sentence recommendation

The result?
Before: wall of unformatted text
After: clean, scannable, actionable recommendations

Full prompt in the repo:
github.com/aiagentwithdhruv/laptop-finder-ai

The prompt is in backend/app/rag/prompts.py

Prompts are the new UI.

#PromptEngineering #RAG #AI #LLM #GPT4o
```

**Visuals:** Before/after screenshot of AI chat formatting

---

### Post 5: The n8n Secret (Unique Angle)

```
n8n use cases for AI apps that nobody talks about.

Everyone knows n8n for email automation and CRM workflows.
But it's secretly one of the best tools for AI app operations.

Here are 6 real use cases I use:

1. Keep-Alive for Free Hosting
→ Render/Railway free tier spins down after 15 min
→ n8n pings your API every 14 min
→ 2 nodes. Zero cold starts. Problem solved.

2. AI Response Quality Monitoring
→ Send test queries every hour
→ Check if RAG pipeline returns good results
→ Alert on Slack/email if quality drops

3. Automated Database Seeding
→ Pull data from Google Sheets daily
→ POST to your seed endpoint
→ Always-fresh product data without manual work

4. Cost Monitoring
→ Check OpenAI usage API daily
→ Calculate daily spend
→ Alert if over budget (before the bill surprises you)

5. User Query Analytics
→ Log every chat query to Google Sheets
→ Weekly summary email
→ Know what users actually want → build that

6. Review Aggregation
→ Scrape reviews from Amazon/BestBuy
→ Feed into your RAG system
→ Fresh data = better recommendations

I included the keep-alive workflow in my repo as a JSON file.
Import it into n8n → change the URL → activate. Done.

github.com/aiagentwithdhruv/laptop-finder-ai

Most AI builders ignore operations.
n8n makes it a 5-minute setup.

#n8n #AIops #Automation #WorkflowAutomation #BuildInPublic
```

**Visuals:** n8n workflow screenshot (import the JSON and take one)

---

### Post 6: AI Coding Rules (Cross-Promo)

```
I open-sourced the 15 rules that make AI write production code.

Yesterday I published ai-coding-rules on GitHub.
Today I built LaptopFinder AI using those exact rules.

The difference is night and day:

Without rules:
❌ Business logic in route handlers
❌ Raw SQL scattered everywhere
❌ No error handling
❌ Hardcoded config values
❌ Spaghetti imports

With rules:
✅ Clean 3-layer architecture (routes → services → repos)
✅ Typed Pydantic schemas
✅ Centralized config + error handling
✅ Async I/O everywhere
✅ Production-grade from line one

The rules cover:
• FastAPI backend patterns
• Next.js frontend patterns
• PostgreSQL + migrations
• RAG systems
• API contracts
• Security
• Error handling + observability
• DevOps + deployment

Works with both Claude Code (CLAUDE.md) and Cursor (.mdc files).

One-liner install:
curl -fsSL https://raw.githubusercontent.com/aiagentwithdhruv/ai-coding-rules/main/install.sh | bash

Or just copy the CLAUDE.md into your project root.

Repo: github.com/aiagentwithdhruv/ai-coding-rules
Proof it works: github.com/aiagentwithdhruv/laptop-finder-ai

Stop fighting AI-generated code quality.
Give it better instructions.

#AIEngineering #ClaudeCode #CursorAI #OpenSource #DevTools
```

**Visuals:** Side-by-side of code without rules vs. with rules

---

## Twitter/X Thread

### Thread: "I built a full AI product with 7 prompts"

```
Tweet 1 (Hook):
I built a full-stack AI product with 7 natural language prompts.

No manual coding. No boilerplate. No copy-paste from Stack Overflow.

Here's the exact prompts I used 🧵

Tweet 2:
Prompt 1 — Architecture:
"Build a laptop recommendation system with AI chat. FastAPI + PostgreSQL + pgvector. Next.js frontend. Clean architecture — routes → services → repos."

Claude Code generated the entire project structure, all models, schemas, and API routes.

Tweet 3:
Prompt 2 — Database + Seed Data:
"Create the schema with laptops, specs, reviews, embeddings. Seed 30 laptops across 6 categories."

Got: Alembic migrations, full JSON seed data with realistic specs and prices.

Tweet 4:
Prompt 3 — RAG Pipeline:
"Build RAG — chunk laptop data, embed with text-embedding-3-small, store in pgvector, retrieve top 8, stream GPT-4o via SSE."

5 files generated: prompts.py, embeddings.py, retriever.py, ingestion.py, generator.py

Tweet 5:
Prompt 4 — Frontend:
"Home page with hero + categories. Browse with filters. Laptop detail with specs. AI chat with streaming. Comparison page."

Full Next.js 15 app with TypeScript, Tailwind, dark theme, responsive.

Tweet 6:
Prompt 5 — Deploy:
"Deploy frontend to Vercel, backend to Render free tier. Custom domain."

Claude handled: render.yaml, Dockerfile, env vars, DNS CNAME setup.

Tweet 7:
Prompt 6 — Keep-Alive:
"Render spins down after 15 min. Create n8n workflow to ping every 14 min."

2-node workflow. Import JSON → activate → done.

Tweet 8:
Prompt 7 — Polish:
"Chat responses are unstructured. Fix the prompt + CSS."

Claude rewrote the system prompt with markdown templates and styled the chat UI.

Tweet 9:
The secret ingredient?

A CLAUDE.md file with 15 engineering rules.

It tells the AI HOW to write code:
— Clean architecture
— Typed schemas
— Async patterns
— Error handling
— Production conventions

Without it: prototype code.
With it: deployable code.

Tweet 10:
Everything is open source:

🔗 Live demo: laptopfinder.aiwithdhruv.com
🔗 Code: github.com/aiagentwithdhruv/laptop-finder-ai
🔗 Engineering rules: github.com/aiagentwithdhruv/ai-coding-rules

The era of "AI can't write production code" is over.
You just need better instructions.
```

---

## YouTube Video Script

### Title Options:
1. "I Built a Full AI Product with 7 Prompts (No Manual Coding)"
2. "How I Use Claude Code to Ship Production AI Apps"
3. "AI Coding Rules: The File That Makes AI Write Clean Code"
4. "From Zero to Deployed: AI Product in One Session"

### Outline:

```
HOOK (0:00 - 0:30)
"What if I told you this entire app — the frontend, backend,
database, AI chat, deployment — was built with 7 natural
language prompts? No manual coding. Let me show you."
[Show live demo of laptopfinder.aiwithdhruv.com]

THE PRODUCT (0:30 - 2:00)
- Walk through the live app
- Show homepage, browse, filters
- Show laptop detail page
- Demo the AI chat — ask a real question
- Show the streaming response with structured formatting
- Show the comparison feature

THE ARCHITECTURE (2:00 - 4:00)
- Show the project structure in VS Code
- Explain 3-layer architecture: routes → services → repos
- Show the RAG pipeline: embed → search → generate
- Explain pgvector for similarity search
- Show SSE streaming code

THE 7 PROMPTS (4:00 - 8:00)
- Go through each prompt:
  1. Architecture setup
  2. Database + seed data
  3. RAG pipeline
  4. Frontend
  5. Deployment
  6. n8n keep-alive
  7. Chat formatting
- Show before/after for each step
- Highlight what Claude Code generated

THE SECRET: CLAUDE.md (8:00 - 10:00)
- Show the CLAUDE.md file
- Explain 15 engineering rules
- Side-by-side: code without rules vs. with rules
- "This one file changes everything"
- Show ai-coding-rules GitHub repo

DEPLOYMENT (10:00 - 12:00)
- Show Vercel deployment (60 seconds)
- Show Render deployment
- Show the n8n keep-alive workflow
- Cost: $0/month + pennies for OpenAI
- vs AWS at $35-50/month

CTA (12:00 - 12:30)
"Links in the description. Star the repos.
Try the live demo. And if you want to build AI
products like this — subscribe."

LINKS:
- Live: laptopfinder.aiwithdhruv.com
- Code: github.com/aiagentwithdhruv/laptop-finder-ai
- Rules: github.com/aiagentwithdhruv/ai-coding-rules
- Portfolio: aiwithdhruv.com
```

---

## Carousel Post (LinkedIn/Instagram)

### Slide-by-Slide:

```
Slide 1 (Cover):
"I Built a Full AI Product
With 7 Prompts"
[Screenshot of the app]

Slide 2:
"The Stack"
Frontend: Next.js 15
Backend: FastAPI
Database: PostgreSQL + pgvector
AI: GPT-4o + RAG
Cost: $0/month

Slide 3:
"Prompt 1: Architecture"
→ 3-layer clean architecture
→ Routes → Services → Repos
→ Generated full project structure

Slide 4:
"Prompt 3: RAG Pipeline"
→ Embed laptop data with text-embedding-3-small
→ Store vectors in pgvector
→ Retrieve top 8 matches
→ Stream GPT-4o response

Slide 5:
"The Secret Sauce"
A CLAUDE.md file with 15 rules
that makes AI write production code
→ Not prototype code
→ Not tutorial code
→ Production-grade, deployable code

Slide 6:
"Deployed for $0"
Frontend → Vercel (free)
Backend → Render (free)
Keep-alive → n8n workflow
Only cost: ~$0.01/query (OpenAI)

Slide 7 (CTA):
"Everything is open source"
🔗 github.com/aiagentwithdhruv/laptop-finder-ai
🔗 github.com/aiagentwithdhruv/ai-coding-rules
[QR code or link]
```

---

## Thumbnail Prompt (for YouTube)

```
Cinematic photo of a South Asian man wearing black t-shirt and glasses,
sitting at a MacBook Pro in a dark room, screen glowing with code.
Split screen showing a sleek dark-themed web app on the right side.
Text overlay: "7 PROMPTS → FULL AI APP"
Purple and teal neon lighting, dark background, moody tech aesthetic.
Hyperrealistic, 4K, shallow depth of field.
```

---

## Hashtag Sets

**LinkedIn:**
```
#AIEngineering #ClaudeCode #BuildInPublic #RAG #FullStack #AIAutomation #SoftwareArchitecture #OpenSource
```

**Twitter/X:**
```
#AI #ClaudeCode #RAG #BuildInPublic #OpenSource #WebDev #n8n
```

**YouTube Tags:**
```
claude code, ai coding, rag tutorial, fastapi nextjs, pgvector, ai product, build with ai, claude code tutorial, ai engineering, laptop recommendation ai, deploy for free, n8n automation, vercel render deployment
```

---

## Cross-Link Strategy

Every piece of content should link to:
1. **Live demo:** laptopfinder.aiwithdhruv.com
2. **Source code:** github.com/aiagentwithdhruv/laptop-finder-ai
3. **Engineering rules:** github.com/aiagentwithdhruv/ai-coding-rules
4. **Portfolio:** aiwithdhruv.com
5. **AWS reference:** github.com/aiagentwithdhruv/conversa-ai (for production deployment)
