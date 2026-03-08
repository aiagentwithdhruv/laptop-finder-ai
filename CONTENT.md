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
