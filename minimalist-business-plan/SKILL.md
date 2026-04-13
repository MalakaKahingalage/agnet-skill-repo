---
name: minimalist-business-plan
description: >
  Build a complete, research-backed business plan from any raw idea using the full
  Minimalist Entrepreneur framework. Reads all existing idea documents, applies all
  10 framework skills, runs 10 parallel web research tracks (including WA government
  sites, grants, market stats, competitors), produces a plan_v2.md with 13 sections,
  a client discovery questions document, a compliance + ABN/ASIC checklist, and exports
  a branded professional PDF. WHEN: build a business plan, create a startup plan,
  turn an idea into a business plan, create a minimalist entrepreneur plan, create a
  plan for a new business, plan a startup, plan a side hustle, build a business from
  scratch.
---

## What I Do

I reverse-engineer and apply the full Minimalist Entrepreneur methodology (by Sahil Lavingia) to any business idea. I:

1. **Read** all existing idea documents in the project folder
2. **Apply** `minimalist-review` to audit what exists
3. **Load** all 9 minimalist framework skills
4. **Run** 10 parallel web research tracks (market data, competitors, grants, community, tools, legal, insurance, content, pricing, government resources)
5. **Assemble** a 13-section business plan with real data
6. **Generate** supporting documents (discovery questions, compliance checklist)
7. **Export** a branded A4 PDF using `business-plan-pdf`

---

## Autonomous Behaviour — CRITICAL

**When this skill is invoked, start immediately. Do NOT:**
- ❌ Ask for permission to research
- ❌ Ask which sections to include
- ❌ Ask what skills to use
- ❌ Ask whether to produce the PDF
- ❌ Announce what you're about to do and wait for approval

**DO:**
- ✅ Read all documents in the idea folder immediately
- ✅ Run all research tracks in parallel (use async bash shells)
- ✅ Load all framework skills before writing
- ✅ Produce all three output files: `plan_v2.md`, `first-meeting-discovery-questions.md`, PDF
- ✅ Report the output location and page count when done

---

## Inputs Required

| Input | How to Get It |
|-------|--------------|
| **Business idea** | Read from tagged files, existing docs, or user's message |
| **Target city/market** | Extract from existing docs or ask once if completely absent |
| **Output folder** | Default: create `idea_v2/` subfolder alongside existing `idea/` folder |

---

## Phase 1 — Intake & Audit

### Step 1: Read All Existing Documents

Find and read all files in the idea folder:

```bash
find "[IDEA_FOLDER]" -type f | sort
```

Read each file. Extract:
- **Business concept** (what is being sold)
- **Target market** (who is the customer)
- **Geography** (what city/region — this drives research targeting)
- **Stage** (raw idea, early concept, or existing business)
- **What already exists** (ABN, brand, website, prior plans)

### Step 2: Apply Minimalist Review

Invoke the `minimalist-review` skill on the existing idea. Capture:
- What to **keep** from existing documents
- What to **cut** (over-engineered, premature, or irrelevant)
- What to **build** (gaps that need to be filled)

Output: a short internal audit note (not written to file — used to shape the plan).

---

## Phase 2 — Load All Framework Skills

Load these skills **before writing any plan content**. Each one contributes a full section:

| Skill | Contributes To |
|-------|---------------|
| `find-community` | Section 2: Community |
| `validate-idea` | Section 3: Validate |
| `mvp` | Section 4: Build |
| `processize` | Section 5: Processize |
| `first-customers` | Section 6: Sell |
| `pricing` | Section 7: Price |
| `marketing-plan` | Section 8: Market |
| `grow-sustainably` | Section 9: Grow |
| `company-values` | Section 10: Culture |
| `minimalist-review` | Section 11: Review |

---

## Phase 3 — Parallel Web Research (10 Tracks)

Run all 10 tracks simultaneously using `mode: async` bash shells. Use **Brave Search** as primary search engine. Use the `webresearch` skill proxy (`http://10.10.40.22:8443`).

### Track 1 — Community Research
**Goal:** Find where the target community gathers online and in person in the target city.

```
Search: "[city] entrepreneur Facebook groups side hustle community 2024 2025
Search: "[city] startup networking events coworking spaces entrepreneurs
```

**Also fetch directly:**
- `https://spacecubed.com/events` (Perth)
- `https://startupwa.org` (Perth)
- `https://meetup.com/entrepreneurs-in-[city]`

**Extract:** Named Facebook groups, meetup groups, coworking venues, events calendar.

---

### Track 2 — Competitor Analysis
**Goal:** Identify who is already doing this, what they charge, what gap they leave.

```
Search: "[service type] [city] Australia pricing 2025 consultant
Search: done for you [service] Australia consultant cost
Search: [specific niche] service provider [city] Australia
```

**Extract:** Competitor names, URLs, price signals (hourly or package), what they don't offer.

---

### Track 3 — WA Market Statistics (or city-equivalent)
**Goal:** Pull hard numbers on business activity, new registrations, growth rates.

**Fetch directly (Perth/WA):**
```bash
curl ... "https://smallbusiness.wa.gov.au/about/small-business-landscape"
curl ... "https://abs.gov.au/statistics/economy/business-indicators/counts-australian-businesses-including-entries-and-exits/latest-release"
curl ... "https://asbfeo.gov.au/small-business-data-portal/number-small-businesses-australia"
```

**Search:**
```
Search: [state] small business registrations [year] statistics growth
Search: [city] startup ecosystem ranking Australia 2024 2025
```

**Extract:** Total businesses, new registrations, growth %, city startup ranking.

---

### Track 4 — Government Grants & Support Programs
**Goal:** Find all active and upcoming grants the client can use.

**Fetch directly (WA):**
```bash
curl ... "https://smallbusiness.wa.gov.au/grants"
curl ... "https://smallbusiness.wa.gov.au/growth"
curl ... "https://perth.wa.gov.au/businesses/starting-a-business"
curl ... "https://business.gov.au/grants-and-programs/innovation-booster-grant-wa"
curl ... "https://startupnews.com.au/news/grants-available-in-wa-for-startups"
```

**Search:**
```
Search: WA small business growth grants 2025 2026 eligibility amount
Search: City of Perth business improvement grants small business
Search: Innovation Booster Grant WA eligibility how to apply
Search: [state] startup grant small business [current year]
```

**Extract:** Grant name, amount, eligibility criteria, current status (open/closed), application URL.

---

### Track 5 — Target Customer Pain Points
**Goal:** Find published research on what the target customer struggles with.

```
Search: [target customer type] pain points starting business Australia 2024
Search: Australian small business owner challenges survey 2024 2025
Search: [specific niche] founder problems Reddit forum Australia
```

**Fetch:**
```bash
curl ... "https://asbfeo.gov.au/small-business-data-portal/asbfeo-small-business-pulse"
curl ... "https://smallbusinessaustralia.org/are-these-the-same-top-5-issues-facing-your-small-business-in-2024"
```

**Extract:** Top 5 pain points as named by the target customer (use their exact words).

---

### Track 6 — AI Tool Stack Research
**Goal:** Identify the best AI tools to deliver the service internally.

```
Search: AI business plan generator comparison 2025 best VentureKit PrometAI
Search: Canva AI brand kit logo generator tutorial 2025
Search: AI tools business consultants use 2025 ChatGPT Claude workflow
```

**Extract:** Best tool for each step (plan generation, brand design, market research, document creation), pricing, pros/cons.

---

### Track 7 — Legal & Business Registration Requirements
**Goal:** Build a complete compliance checklist for the business owner AND their clients.

**Fetch directly:**
```bash
curl ... "https://abr.gov.au/business-super-funds-charities/applying-abn/abn-entitlement/sole-trader"
curl ... "https://asic.gov.au/for-business/registering-a-company"
curl ... "https://ato.gov.au/businesses-and-organisations/starting-registering-or-closing-a-business/starting-your-own-business/business-structures-key-tax-obligations"
curl ... "https://business.gov.au/registrations/register-for-taxes/register-for-gst"
```

**Search:**
```
Search: sole trader vs Pty Ltd Australia consultant 2025 pros cons
Search: ABN registration sole trader Australia free how long
Search: GST registration threshold Australia 2025
Search: business name registration ASIC cost Australia
```

**Extract:** Step-by-step registration requirements, costs, timelines, thresholds.

---

### Track 8 — Insurance Requirements
**Goal:** Get real pricing for professional indemnity and public liability insurance.

```
Search: professional indemnity insurance sole trader consultant Australia cost 2025
Search: public liability insurance sole trader office based Australia annual cost
```

**Fetch:**
```bash
curl ... "https://bizcover.com.au/how-much-does-professional-indemnity-cost"
curl ... "https://finder.com.au/business-insurance/professional-indemnity-insurance-in-australia"
```

**Extract:** Real $ figures for PI and PL insurance at sole trader scale, provider names.

---

### Track 9 — Content Marketing Benchmarks
**Goal:** Find what content platforms, formats, and posting frequency work for AU consultants.

```
Search: content marketing strategy small business consultant Australia LinkedIn Instagram 2025
Search: social media posting frequency small business Australia 2025 best practice
Search: LinkedIn content strategy Australia B2B consultant 2025
```

**Extract:** Best platforms for the target market, optimal posting frequency, content formats that work, AU-specific benchmarks.

---

### Track 10 — Competitor Pricing Deep Dive
**Goal:** Validate the pricing model against market data.

```
Search: business consultant hourly rate Australia 2025
Search: branding agency cost Australia logo brand kit small business
Search: Shopify website build cost Australia 2025
Search: startup package consulting price Australia done for you
```

**Fetch:**
```bash
curl ... "https://bark.com/services/business-consulting/price-guide"
curl ... "https://sleek.com/how-to-start-a-consulting-business-in-australia"
```

**Extract:** Hourly rates, package rates, what the market accepts at different price points.

---

## Phase 4 — Plan Assembly

Write to: `[OUTPUT_FOLDER]/plan_v2.md`

### Full 13-Section Structure

---

#### Section 1 — The One-Sentence Version
> **[Action verb] [target customer] [from state A] to [state B] in [timeframe] — [mechanism] to deliver [outcome they value] at [price].**

One sentence. No jargon. Passes the "BBQ test" — someone at a barbecue instantly understands it.

---

#### Section 2 — Community (from `find-community` skill + Track 1 research)

Include:
- **Primary community profile** — demographics, psychographics, behaviour, specific Perth/city examples
- **Why this community exists at scale** — use real ABS / SBDC numbers from Track 3
- **Top 5 pain points** — use exact language from Track 5 research
- **Where they gather** — table of online + in-person venues with specifics (group names, addresses, event frequency)
- **Community entry strategy** — week-by-week actions (Week 1: listen, Week 2: conversations)
- **Anti-patterns to avoid** — specific traps (don't sell on day 1, don't target everyone)

---

#### Section 3 — Validate (from `validate-idea` skill + Track 2 + Track 10 research)

Include:
- **The 4 minimalist validation questions** — answered specifically for this business
- **Competitor validation table** — names, what they offer, price signals, gap they leave
- **Market demand signals** — real data points (registrations, growth %, survey findings)
- **The validation test** — specific pilot price offer with word-for-word script
- **Validation checklist** — 5 checkboxes to complete before moving to Phase 2

---

#### Section 3b — Market Validation Report *(The Concept Validator deliverable)*

This section produces the actual client-facing Market Validation Report that is handed to each client as part of the Concept Validator package.

Include:
- **Goals and Hypotheses** — the initial assumptions the founder has made about the product and the market. Document them explicitly so they can be tested.
- **The Problem Space** — evidence that the problem being solved is a genuine, recurring pain point for consumers. Use: customer quotes, survey data, forum threads, competitor reviews, search volume.
- **Target Market Identification** — detailed customer personas with:
  - Demographics (age, location, income, occupation)
  - Psychographics (values, fears, aspirations, buying behaviour)
  - Job-to-be-done (what are they really hiring this product/service to do?)
  - Segment size estimate (use ABS, IBISWorld, Google Trends, eBay sold data as proxies)
- **Competitive Analysis** — evaluate direct and indirect competitors:
  - Direct: businesses offering the same product/service
  - Indirect: alternatives the customer might choose instead (including "do nothing")
  - Table: Competitor | Price | Strength | Weakness | Differentiation Opportunity
- **Market Demand and Pricing** — assessment of:
  - Market size (TAM/SAM estimate — keep it simple)
  - Evidence of willingness to pay (eBay sold data, competitor pricing, existing transactions)
  - Recommended price positioning

---

#### Section 4 — Build (from `mvp` skill)

Include:
- **The three delivery stages** — Manual → Processized → Productized (with trigger milestones)
- **MVP definition table** — what it does, who it's for, how it's delivered, tools needed
- **MVP launch checklist** — every item needed before Client 1 (ABN, Calendly, Stripe, tools)
- **What NOT to build** — explicit list of things to avoid before first paying client

---

#### Section 4b — Comprehensive Business Plan *(The Concept Validator deliverable)*

This section is the actual business plan template that the consultant delivers to each client. It becomes the client's strategic roadmap.

Include all of the following subsections — each populated with client-specific data gathered in the discovery call:

**Executive Summary & Company Description**
- Business name and one-sentence description
- Mission statement (why this business exists beyond making money)
- Core values (3 maximum — real, not generic)
- Founding story (why this founder, why now)
- Current stage and immediate goals

**The Opportunity and Solution**
- Problem statement — the specific pain being solved, backed by evidence
- Solution description — exactly what is being sold (product, service, experience)
- Why now — market timing factors (technology, regulation, culture shift, etc.)
- Unique selling proposition — one clear differentiator

**Revenue Model**
- Primary revenue stream — what the customer pays for, how often
- Pricing model — fixed price, subscription, usage-based, tiered
- Unit economics — cost per unit sold, gross margin
- Revenue projections — Month 1, Month 3, Month 6, Year 1 (simple table)
- Break-even analysis — how many sales to cover all costs

**Target Market and Customer Personas**
- Primary persona (name, demographics, psychographics, buying triggers)
- Secondary persona if applicable
- Market size estimate (TAM → SAM → SOM — keep simple and defensible)
- Customer acquisition channels — where they are and how to reach them

**Marketing and Sales Channels**
- Primary acquisition channel (organic content, referrals, cold outreach, partnerships)
- Secondary channel
- Sales process — from lead to payment (step by step)
- Customer retention strategy
- Metrics to track (CAC, conversion rate, referral rate)

**Team and Needs**
- Founding team (names, roles, relevant experience)
- Key skills present vs. gaps
- Immediate hiring or contractor needs
- Advisory or mentor relationships
- Tools and systems needed to operate

**Milestones and Roadmap**
- 30-day goals
- 90-day goals
- 12-month goals
- Key risks and mitigation strategies

---

#### Section 5 — Processize (from `processize` skill)

Include:
- **Day-by-day delivery table** — every step, tool, and time estimate for every day of the service delivery cycle
- **Total delivery time** calculation
- **Effective hourly rate** calculation
- **What to automate first** — ordered list for Stage 2 (after 10 clients)
- **Quality control checklist** — what to verify before every handover

---

#### Section 6 — Sell (from `first-customers` skill + Track 1 research)

Include:
- **Three concentric circles** — Friends/Family → Community → Strangers (with client count targets per circle)
- **Personal outreach script** — word-for-word message for warm contacts
- **Community outreach script** — for Facebook groups, events, LinkedIn
- **Cold DM/email template** — personalised approach for cold contacts
- **Rules for cold outreach** — what to do and what never to do
- **Weekly sales targets table** — by week for first 3 months
- **Referral engine** — word-for-word ask at handover call, referral incentive structure

---

#### Section 7 — Price (from `pricing` skill + Track 10 research)

Include:
- **Pricing philosophy** — value-based, not hourly
- **Comparison anchor table** — what the client would pay for each piece separately vs. your package price
- **Pricing structure table** — pilot price, standard price, phase 2 price
- **Payment terms** — deposit %, trigger for second payment, tool used (Stripe)
- **Price increase triggers** — milestone-based price ladder
- **Financial independence maths** — clients/month × price = monthly/annual revenue table

---

#### Section 8 — Market (from `marketing-plan` skill + Track 9 research)

Include:
- **Prerequisites before marketing** — checklist (clients, testimonials, defined niche)
- **Platform strategy** — primary and secondary platform with rationale
- **Three levels of content** — Educate, Inspire, Entertain (10 ideas each = 30 content ideas)
- **Email list strategy** — lead magnet idea, collection method, cadence
- **Sustainable weekly content calendar** — by day, platform, format, time required
- **When to spend money** — explicit trigger for paid ads (not before Month 6)
- **Paid ads guardrails** — maximum CPA rule

---

#### Section 9 — Grow (from `grow-sustainably` skill + Track 7 + Track 8 research)

Include:
- **The Golden Rule** — spend less than you make, every month
- **Full monthly cost table** — every tool with real $ from Track 8 research (PI insurance, tools, subscriptions)
- **Default Alive Test** — how to run it monthly
- **Business structure guidance** — sole trader now, Pty Ltd trigger ($75k revenue), with real costs and process
- **GST registration** — $75k threshold, when to register early
- **Hiring sequence** — 4 stages with revenue triggers
- **No-fundraising rationale** — why bootstrapping is the right choice for this type of business

---

#### Section 10 — Culture (from `company-values` skill)

Include:
- **Why culture matters as a solo founder** — it sets the default for when you hire
- **5 company values** — each with:
  - Name and one-line definition
  - What it looks like in practice (2 concrete examples)
  - The anti-pattern (what it's NOT)
- **Working style principles** — async by default, meeting rules, client boundaries, pricing psychology

---

#### Section 11 — Review (from `minimalist-review` skill)

Include:
- **The 5-question minimalist decision framework** — applied to this business
- **Decision log** — table of common temptations with minimalist verdict and "do instead" column
- **Monthly business health check** — 5 yes/no questions to run every month

---

#### Section 12 — Locked Away

Include:
- Table of future ideas with specific unlock milestones
- Rule: nothing gets unlocked before the milestone is hit
- Common items: Phase 2 service, referral network, website, hiring, white-label tool, venture studio

---

#### Section 13 — What to Do Tomorrow Morning

Include:
- Numbered, ordered action list — 7–10 items max
- No skipping allowed
- First action: identify 10 real people to message
- Last pre-client action: set up Stripe
- Final note: the single metric for the first 30 days

---

## Phase 5 — Supporting Documents

### Document A: First-Meeting Discovery Questions

Write to: `[OUTPUT_FOLDER]/first-meeting-discovery-questions.md`

A complete 60-minute discovery call guide with:
- Time budget per section (7 sections totalling 60 minutes)
- 25 questions across sections: Warm-up, The Idea, The Customer, Competition, Their Situation, What They Need, Wrap-up
- Coaching note under each question — what to listen for and why
- Word-for-word closing script
- 🔴 Red flags (6 walk-away signals)
- 🟢 Green lights (6 buy signals)
- 📋 Post-call capture template — fill in within 30 minutes

---

### Document B: Compliance & Setup Checklist

Include as an appendix in `plan_v2.md`.

#### For the Business Owner (Founding the Consultancy)

**Immediate (Before First Client):**
- [ ] Register ABN as sole trader — free, 15 min, at `abr.gov.au` — ABN confirmed instantly in most cases
- [ ] Register business name (if trading under a name other than your own) — $39/yr via ASIC Connect at `connectonline.asic.gov.au`
- [ ] Purchase domain name — ~$15/yr at Namecheap or Google Domains
- [ ] Open a dedicated business bank account — keeps personal and business finances separate (required for tax)
- [ ] Set up Stripe for payments — `stripe.com.au` — no monthly fee, 2.9% + 30¢ per transaction
- [ ] Set up Calendly for bookings — free tier at `calendly.com`
- [ ] Set up Google Workspace — $14/month for professional email (`yourname@yourbrand.com.au`)
- [ ] Get Professional Indemnity Insurance — ~$102/month, compare at `bizcover.com.au` or `finder.com.au`
- [ ] Get Public Liability Insurance — ~$32/month for office-based sole trader

**Within 90 Days:**
- [ ] Register for GST if turnover will exceed $75,000/year (or register early if clients are businesses who can claim GST back) — free via ATO at `ato.gov.au/business`
- [ ] Set up accounting software — Xero ($35/month) or Wave (free) — record all income and expenses from Day 1
- [ ] Create a filing system for client records (Google Drive or Notion)
- [ ] Draft a standard Consulting Agreement / SOW template (use v1 docs as base)
- [ ] Create a Privacy Policy for your business (required if collecting personal data) — use Termly or GetTerms

**When Revenue Exceeds ~$75,000/year:**
- [ ] Consult an accountant about upgrading to Pty Ltd — ASIC registration ~$538 + accountant fees
- [ ] Register Pty Ltd with ASIC at `asic.gov.au/for-business/registering-a-company`
- [ ] Apply for a new ABN for the company (separate from your sole trader ABN)
- [ ] Transfer business name and domain to the new company

---

#### For Each Client (Founder Registration Checklist)

**Business Structure — Choose One:**
- [ ] **Sole Trader** — simplest, free, income reported in personal tax return. Suitable for solo founders under $75k/year. Register ABN at `abr.gov.au` (free, instant)
- [ ] **Partnership** — for 2+ founders, shared ABN. Register at `abr.gov.au`. Draft a Partnership Agreement.
- [ ] **Pty Ltd (Company)** — limited liability, more professional. ~$538 ASIC registration + annual ASIC review fee (~$290). Register at `connectonline.asic.gov.au`
- [ ] **Trust** — for asset protection or family income splitting. Requires a solicitor. Not recommended for early-stage founders.

**Registration Steps (In Order):**
1. [ ] Choose business name — check availability at `connectonline.asic.gov.au` (business name search)
2. [ ] Register ABN — free at `abr.gov.au` — takes 15 minutes, confirmed within 28 days (usually instant)
3. [ ] Register business name with ASIC — $39/yr or $92/3 yrs at `connectonline.asic.gov.au`
4. [ ] Register for GST if turnover will exceed $75,000/year — via ATO at `ato.gov.au/business`
5. [ ] Register for PAYG Withholding if you plan to hire staff — via ATO
6. [ ] Open a business bank account (most major banks require ABN)
7. [ ] Set up bookkeeping software — Xero ($35/mo), MYOB ($27/mo), Wave (free)

**Intellectual Property:**
- [ ] Register trade mark if brand name needs protection — IP Australia at `ipaustralia.gov.au` — ~$250 per class
- [ ] Understand copyright — original creative work (logo, copy, photography) is automatically protected in Australia

**Insurance (Recommended for All Client Businesses):**
- [ ] Public Liability Insurance — essential if client has customer-facing premises or products
- [ ] Product Liability — if selling physical goods
- [ ] Professional Indemnity — if providing advice or professional services
- Compare at: `bizcover.com.au`, `quotesonline.com.au`, `aami.com.au`

---

#### WA Grants Reference (Verify Status Before Advising Any Client)

| Grant | Amount | Who | Status to Check |
|-------|--------|-----|----------------|
| **SBDC Small Business Growth Grants** | Up to $10,000 matched | WA small businesses — metro + regional (different criteria) | `smallbusiness.wa.gov.au/growth` |
| **City of Perth Business Improvement Grants** | Varies | Businesses within City of Perth boundary | `perth.wa.gov.au/businesses` |
| **Innovation Booster Grant WA** | Up to $50,000 | WA businesses commercialising new ideas | `business.gov.au/grants-and-programs/innovation-booster-grant-wa` |
| **City of Joondalup Grants** | $5,000–$25,000 | Eligible Joondalup businesses or relocating businesses | `joondalup.wa.gov.au` |
| **New Industries Fund (Regional)** | Varies | Regional WA businesses, innovation-focused | `dpird.wa.gov.au/businesses/grants-and-support` |
| **R&D Tax Incentive** | 43.5% cash rebate | All AU businesses with R&D spend >$20k | `business.gov.au/grants-and-programs/research-and-development-tax-incentive` |

**How to use this in a client plan:**
- Mention grants as a potential cost offset for the consulting fee
- Note that SBDC Growth Grants accept consulting services as eligible expenses
- Always verify current open/closed status before advising — grant cycles change quarterly

---

## Phase 6 — PDF Export

Use the `business-plan-pdf` skill:

```bash
pip install weasyprint pypdf -q

python3 ~/.agents/skills/business-plan-pdf/generate_pdf.py \
  --input  "[OUTPUT_FOLDER]/plan_v2.md" \
  --output "[OUTPUT_FOLDER]/[BusinessName]_Business_Plan_v2.pdf" \
  --title  "[Business Name]" \
  --subtitle "Business Plan v2 — [City] | Minimalist Entrepreneur Framework" \
  --prepared-by "[Founder Name or Business Name]" \
  --classification "CONFIDENTIAL" \
  --scope "Complete business plan covering all 10 Minimalist Entrepreneur framework pillars"
```

Verify:
```bash
python3 -c "
from pypdf import PdfReader
r = PdfReader('[OUTPUT_FOLDER]/[BusinessName]_Business_Plan_v2.pdf')
print(f'Pages: {len(r.pages)}')
"
ls -lh "[OUTPUT_FOLDER]/[BusinessName]_Business_Plan_v2.pdf"
```

---

## Output Files

| File | Description |
|------|-------------|
| `[OUTPUT_FOLDER]/plan_v2.md` | Full 13-section business plan (~800 lines) |
| `[OUTPUT_FOLDER]/first-meeting-discovery-questions.md` | 60-min discovery call guide with 25 questions |
| `[OUTPUT_FOLDER]/[BusinessName]_Business_Plan_v2.pdf` | Branded A4 PDF (~30–40 pages) |

---

## Final Report to User

When complete, tell the user:

```
✅ Business plan complete.

📄 Files created in [OUTPUT_FOLDER]:
  - plan_v2.md — [X] lines
  - first-meeting-discovery-questions.md — [X] lines
  - [BusinessName]_Business_Plan_v2.pdf — [X] pages, [X] KB

📋 Plan covers all 10 framework pillars:
  Community · Validate · Build · Processize · Sell · Price · Market · Grow · Culture · Review

🔬 Research completed:
  [X] web searches across [X] tracks — community, competitors, market stats,
  grants, pain points, tools, legal, insurance, content, pricing

📑 Includes:
  - Market Validation Report (client deliverable template)
  - Comprehensive Business Plan template (client deliverable)
  - ABN/ASIC/GST compliance checklist (for you and your clients)
  - WA grants reference table with status-check URLs
  - First-meeting discovery questions with red flags and post-call template
```

---

## Notes & Lessons Learned

- ✅ **Always read existing docs first** — clients often have more material than they realise; build on it rather than starting from scratch
- ✅ **Run all research in parallel** — 10 async bash shells finish in the same time as 1 sequential search
- ✅ **Use Brave Search** (`search.brave.com`) — not Google (blocked via proxy), not DuckDuckGo (CAPTCHA issues after 3 searches)
- ✅ **Fetch government sites directly** — `smallbusiness.wa.gov.au`, `abr.gov.au`, `asic.gov.au`, `ato.gov.au`, `business.gov.au` all return clean content with Chrome UA
- ✅ **Capture exact customer language** in the discovery call — it becomes the plan's brand voice and the marketing copy
- ✅ **The Processize section is the most valuable** — it transforms an abstract service into a reproducible, sellable product
- ✅ **The compliance checklist earns trust** — clients value knowing exactly what to register and in what order
- ⚠️ **Grant status changes** — always include a "verify current status" note; grants open and close quarterly
- ⚠️ **Don't over-engineer the plan** — the minimalist review at the start prevents building a 60-page document nobody reads

---

**Version:** 1.0
**Created:** 2026-03-29
**Inspired by:** The Minimalist Entrepreneur by Sahil Lavingia
**Skills invoked:** find-community, validate-idea, mvp, processize, first-customers, pricing, marketing-plan, grow-sustainably, company-values, minimalist-review, business-plan-pdf, webresearch
