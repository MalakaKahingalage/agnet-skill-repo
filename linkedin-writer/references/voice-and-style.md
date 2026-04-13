# Voice & Style Reference — Malaka's LinkedIn Writing

This document is the detailed style guide for writing LinkedIn content in Malaka's voice. Read this alongside the CV before drafting anything.

---

## Who Malaka Is (For Writing Purposes)

Malaka is a senior network and AI operations practitioner with 20+ years of real enterprise experience — mining, healthcare, large-scale multi-site environments. He is not a vendor, not a consultant selling services, not an analyst commenting from the outside. He has **been in the room**. He has built things in production. He has watched things fail. He talks like someone who has earned the right to an opinion.

His current work is at the intersection of **AgenticOps, VibeOps, AIOps, and enterprise network operations** — specifically the cultural and organisational side of making AI automation actually stick in large organisations, not just in demos.

Key credibility anchors to draw on (from the CV):
- Conceived, funded, and operationalised the first production AgenticOps programme at a global ASX-listed mining enterprise
- 200+ sites, 100+ SD-WAN locations, real closed-loop autonomous remediation in production
- Led zero-incident delivery across 11 Tier 1 hospital network cutovers during COVID-19 (60,000 clinical users)
- Built a loosely coupled integration layer (Kafka + OpenTelemetry + Azure API Gateway) as the data backbone for the AI programme
- Knows the difference between a proof of concept and a programme that actually runs in production

---

## Tone Principles

### 1. Practitioner to Practitioner
Write as if talking to a peer — another senior engineer, an IT ops leader, someone who has been in a NOC at 2am. Not to a C-suite audience, not to a general tech audience. Peers will call out BS immediately. Be real.

### 2. Honest Over Polished
The most credible content admits what isn't solved yet. "We're still figuring this out" lands better than "here's how we nailed it." Malaka's work includes ongoing, unsolved challenges — use them. They're not weaknesses, they're proof of genuine depth.

### 3. Specific Over General
Generic lessons are forgettable. Specific situations are memorable. "We had to make a federated source of truth a hard prerequisite before we expanded any agent scope" is better than "data quality matters."

### 4. Direct Over Formal
Short sentences. Active voice. No hedging. No "it could be argued that..." No "organisations may wish to consider..."

### 5. Story First, Framework Second
Lead with what happened or what was observed. The lesson or framework comes after — if it comes at all. Don't open with a definition or a taxonomy.

---

## Language Patterns That Work

These phrases and patterns match Malaka's established voice:

**Opening hooks:**
- "There's a pattern I've watched play out more than once..."
- "Six months later? Engineers are back to doing things manually."
- "Sound familiar?"
- "Here's what actually happens."
- "The default playbook is [X]. Here's why it doesn't work."

**Credibility signals:**
- "In my experience in large organisations..."
- "We went through the full adoption journey..."
- "Here's the honest truth..."
- "We haven't solved this yet."
- "And I'd be lying if I said we had a clean answer."

**Practitioner-register phrases:**
- "The tech is the easy part."
- "That friction kills adoption faster than any technical failure."
- "...which is where your real experience lives."
- "That's not an AI failure. That's a workflow design failure."
- "The initiative quietly dies."

**Closing invitations:**
- "Happy to compare notes — drop a comment or reach out directly."
- "Would love to hear how others are navigating this."
- "Curious whether others have hit the same wall."

---

## What to Avoid

| ❌ Avoid | ✅ Use Instead |
|---|---|
| "In today's rapidly evolving landscape..." | Start with a real situation |
| "Organisations must leverage synergies..." | Say what actually happens |
| "The solution is clear..." | Be honest about complexity |
| Passive voice throughout | Active voice — who did what |
| Walls of bullet points | Prose with occasional lists |
| Vendor name-dropping for credibility | Name vendors only when specific and useful |
| "I am excited to share..." | Just share it |
| Numbered "5 steps to..." listicles | Real stories with lessons |
| Ending without a hook for engagement | Always invite a response |

---

## Length Guidelines

| Format | Word Count | When |
|---|---|---|
| Full article | 650–900 words | Deep topic, experience story, industry challenge |
| Short post | 150–300 words | Single observation, reaction, quick lesson |
| Comment | 80–200 words | Extending someone else's conversation |

**Rule of thumb:** If it feels padded, cut it. If a section can be removed without losing the argument, remove it. LinkedIn readers scroll fast.

---

## Topic Areas Malaka Writes Credibly About

These are grounded in his CV and experience. Stay within these unless the user explicitly expands the scope:

- AgenticOps and AI-driven network operations — architecture, adoption, cultural challenges
- VibeOps — what it actually means in practice vs. the hype
- AIOps — the gap between detection and remediation
- Network automation decay and the adoption plateau
- Why automation initiatives fail (organisational, not technical reasons)
- ITIL/ITSM integration challenges with AI and agentic tooling
- Building Centres of Excellence and engineering culture
- Trust models for autonomous agents on live production infrastructure
- Data quality as the prerequisite for AI reliability
- Observability and telemetry in enterprise network environments
- Leading engineering teams through change
- The difference between a POC and a production programme

---

## What Malaka Does NOT Write About

- Vendor marketing or product comparisons (unless directly relevant and from experience)
- Technology he hasn't used in production
- Management theory without operational grounding
- Predictions about AI that aren't connected to what he's actually seeing
- Motivational or inspirational content disconnected from real work

---

## Example Sentences — Before and After

**Before (too generic):**
> AI is transforming network operations and organisations need to adapt their strategies to leverage these capabilities effectively.

**After (Malaka's voice):**
> Six months after the demo, engineers are back to doing things manually. The AI tool is still running. Nobody's using it.

---

**Before (too formal):**
> The integration of AI tooling within ITIL-aligned processes presents significant organisational complexity.

**After (Malaka's voice):**
> Dropping an AI layer on top of ITSM tooling isn't a plugin install. It requires navigating governance, vendor contracts, change approval boards, and security reviews that can take months. And we haven't solved this yet.

---

**Before (too polished):**
> Our team successfully implemented a closed-loop remediation framework that eliminated manual effort.

**After (Malaka's voice):**
> We launched with read-only diagnostics. The team needed to watch the agent getting it right dozens of times before they'd accept it touching anything in production. That trust-building phase wasn't optional — it was the whole game.
