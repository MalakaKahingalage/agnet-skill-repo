# Malaka's Career Reference — LinkedIn Writing

*This is the portable career reference for the linkedin-writer skill. It is a structured summary of Malaka's CV, organised for quick lookup when writing LinkedIn content. Use this to ground all claims, stories, and experience references.*

---

## Who Malaka Is — The One-Paragraph Version

Malaka Indrajith Kahingalage is a senior network and AI operations practitioner based in Perth, WA, Australia. He has 20+ years of experience across mining, healthcare, and enterprise environments — and is among the small number of practitioners in Australia who has designed, built, operationalised, and led a team through a full production-grade AgenticOps deployment, end to end, in a live enterprise. His work sits at the intersection of network operations, applied AI, and organisational change. He is not a vendor, not an analyst, and not a consultant — he builds things in production and leads the teams that run them.

**Contact:** malaka.indrajith@gmail.com | +61 466 619 225
**LinkedIn:** linkedin.com/in/malakaindrajith

---

## The Headline Numbers (Use These for Credibility)

| Fact | Detail |
|---|---|
| **200+ sites** | Global mining enterprise network footprint — LAN, WAN, Wi-Fi |
| **100+ SD-WAN locations** | Managed as part of the AgenticOps programme |
| **3,000+ hours/year** | Projected manual effort elimination as agent scope reaches full write-access |
| **100+ hours/month** | Saved immediately via automated alert suppression and correlation |
| **~10 days** | Manual engineering effort recovered within the first five weeks of agent launch |
| **60,000 clinical users** | Served across WA metro hospital network |
| **11 Tier 1 hospitals** | Concurrent network cutovers led during COVID-19 |
| **13 major cutovers** | Zero clinical incidents across all of them |
| **500+ fibre connections** | Migrated on time and within budget |
| **3,000+ network devices** | Monitored statewide via SolarWinds platform at WA Health |
| **1,000+ hours/6-month cycle** | Saved via automated device onboarding at mining enterprise |
| **50%** | Reduction in device onboarding time via Catalyst Centre + Ansible automation |
| **7** | Strategy and architecture documents authored, all executive-sponsored |
| **120+ tool integrations** | In-house MCP development to accommodate the integration landscape |
| **FY2025** | Recognised by senior management as a high performer |

---

## Current Role

**Network Platform AgenticOps & AIOps Tech Lead**
Global ASX-listed Mining Enterprise | Perth, WA
September 2024 – Present

Programme owner and Principal-level architect across AgenticOps, the Network Platform Intelligent Automation Centre of Excellence, and the enterprise automation and observability strategy.

**What this role actually involves:**
- Conceived, secured executive sponsorship for, and operationalised the organisation's first production LLM-based network operations agent
- Integrated with network controllers, monitoring platforms, and ITSM tooling via a RAG-augmented knowledge layer
- Built a staged trust-model progression: read-only diagnostics → supervised fault triage → controlled write access (port reset, interface error clearing)
- Designed and built the **Loosely Coupled Integration Layer** — Apache Kafka + OpenTelemetry Collector + Azure API Gateway, multi-region
- Closed-loop self-healing for known fault patterns in production, with governed action paths, auditability, and rollback control
- Programme in Phase 2 production; Phase 3 (full autonomous write-access) scoped and funded for FY2026
- Led the Network Platform Intelligent Automation Centre of Excellence

---

## Previous Role at Same Organisation

**Specialist, Network Optimisation**
Global ASX-listed Mining Enterprise | Perth, WA
January 2022 – September 2024

Built the foundations that made the AgenticOps programme possible:
- Led global managed services transition (LAN/Wi-Fi) ahead of schedule, zero degradation
- Automated device onboarding with Ansible + Catalyst Centre — 50% faster, 1,000+ hours saved per cycle
- Designed and commissioned global Splunk syslog environment (40+ nodes) — became the AgenticOps data layer
- Established the automation team that became the nucleus of the Centre of Excellence
- Introduced data-driven reporting and KPI frameworks for executive decision-making

---

## WA Health — Healthcare Network (2016–2022)

**Senior Network Administrator / Acting Team Leader → Network Solution Architect**
Health Support Services, WA Department of Health | Perth, WA

Key facts for writing:
- Supported 60,000+ end-users across metro hospital network
- Monitored 3,000+ network devices statewide via self-designed SolarWinds HA platform
- Led COVID-era concurrent delivery across 11 Tier 1 hospitals — zero clinical incidents, 13 cutovers
- Automated Day-0 and Day-N provisioning with Ansible and DNAC
- Represented network engineering on ICT Change Approval Board and Infrastructure Design Authority
- Co-developed future-state digital hospital network blueprint and SD-Access architecture for WA Health (as Solution Architect, 2021–2022)
- Perth Children's Hospital — greenfield network design and SD-Access POC; drove feature testing that shaped procurement decision

---

## Earlier Experience

**Systems Consultant — ISA Technologies | Perth, WA (2011–2016)**
- Enterprise infrastructure for financial services, utilities, professional services clients
- High-availability networks, firewalls, load balancers, secure VPN, multi-view DNS
- Achieved CCNP, RHCE, and VMware VCA during this period

**Engineering Executive & Network Administrator — Dialog Axiata PLC | Sri Lanka (2009–2011)**
- IP/MPLS backbone, mobile, and fixed-line infrastructure for one of Sri Lanka's largest telcos
- Carrier-scale experience: high-availability operations, multi-domain change management

---

## Education

| Qualification | Institution | Year |
|---|---|---|
| BSc (Honours) Information Technology | Middlesex University | 2007–2009 |
| Graduate Diploma, Telecommunication Systems | Engineering Council UK | 2006–2007 |
| Advanced Technical Diploma | City & Guilds Institute London | 2000–2006 |

---

## Certifications

- Cisco Certified Networking Professional (CCNP) — 2015
- Red Hat Certified Engineer (RHCE) — 2016
- VMware Certified Associate — Data Centre Virtualisation — 2014

---

## The Five Enterprise AgenticOps Challenges (Core Story Material)

These are the five real challenges Malaka navigated in his production programme. They are the most important source material for LinkedIn content — use them as the backbone of any experience-based story.

### 1. Data Quality
**What happened:** Legacy CMDB data was stale and inaccurate. Agents were making decisions on bad data and ops teams lost confidence fast.
**What was done:** Made a federated source of truth a hard, non-negotiable prerequisite. No agent scope expansion until data confidence was established.
**The lesson:** You cannot build trusted autonomous operations on dirty data. Fix the data problem first — everything else waits.

### 2. Tool Fragmentation
**What happened:** Multiple monitoring instances and controller clusters with tightly coupled integrations — touching one thing broke three others. "Random pops of capability" rather than a coherent platform.
**What was done:** Moved to a loosely coupled event-driven architecture (Kafka + OpenTelemetry). Automation logic, tool integrations, and observability services could now evolve independently.
**The lesson:** Tight coupling is the silent killer of automation programmes. The integration architecture matters as much as the AI layer.

### 3. Cultural Resistance
**What happened:** "What if the agent makes it worse?" — a recurring and completely reasonable concern from ops teams.
**What was done:** Read-only proving phase. Teams watched the agent getting it right consistently before any write access was granted. Authored a formal cultural change playbook.
**The lesson:** Trust is earned incrementally. Engineers won't accept autonomous remediation until they've watched the AI get it right dozens of times. The read-only phase isn't a warm-up — it's the whole game.

### 4. Security & Compliance
**What happened:** Write-access agents on live production networks needed Zero Trust controls, full audit trails, and change-window compliance — not optional.
**What was done:** All agent actions funnelled through proper ITIL approval pipelines. Only approved action types exposed as governed REST API endpoints. Full audit logging at every step.
**The lesson:** Security and compliance for agentic systems is a different conversation from traditional automation. Govern at the architecture level, not as an afterthought.

### 5. Adoption Plateau
**What happened:** Early enthusiasm followed by gradual return to manual habits — a predictable decay pattern without active countermeasures.
**What was done:** Built the Centre of Excellence as the cultural anchor and idea incubation point. Data-driven reporting kept automation value visible. KPI ownership distributed across the whole team — not just the automation team.
**The lesson:** The technology isn't what sustains adoption. The organisational structure around it is.

---

## The ITIL / AgenticOps Integration Challenge (Ongoing — Not Solved)

This is an active, unresolved challenge — use it honestly in content as a real practitioner insight:

- Integrating a domain-specific, network-focused AI layer inside ITIL-aligned tooling is genuinely hard in large enterprises
- Change management workflows, approval gates, CMDB dependencies, SLA tracking, compliance requirements — all baked into ITSM platforms over years of customisation
- The ITSM platform team suggested using their own native agents instead — but those are scoped for service request fulfilment, catalogue automation, and general incident logging, not deep network fault reasoning or closed-loop remediation
- Generic ITSM-native agents (e.g. NowAssist-style tooling) don't carry the domain-specific context needed for network operations work
- The real challenge: embedding a custom, network-specific AI layer *inside* the ITIL workflow without replacing it — keeping change approval, audit trails, and SLA tracking intact while adding domain intelligence on top
- This is an integration architecture problem that most ITSM vendors haven't fully solved yet either
- This is why most organisations stop at the demo

---

## Technology Stack (Reference)

**AI & AgenticOps:** LLM integration, generative AI workflow design, closed-loop remediation, trust-model progression, agent security governance, MCP development, RAG architecture, Azure API Gateway (AI Gateway patterns)

**Integration & Data:** Apache Kafka, OpenTelemetry (OTEL), REST APIs, NetBox, CMDB integration, federated data pipelines, MELT telemetry, event-driven architecture

**Network Platforms:** Cisco Catalyst Centre (DNAC), Cisco ISE, Cisco SD-Access, ThousandEyes, SolarWinds (NPM, NCM, IPAM, UDT, SAM), Splunk

**Automation & DevOps:** Python, Ansible, Azure DevOps, CI/CD pipelines, IaC, NetDevOps practices

**Protocols & Design:** YANG/NETCONF, BGP, OSPF, MPLS, SD-WAN, 802.1x NAC, Zero Trust, VPN, DNS, HA design patterns

**Cloud & Infrastructure:** Azure PaaS, SQL HA clustering, Kubernetes (AKS/EKS), VMware, Red Hat Linux, OT/IT convergence

---

## Core Topics Malaka Writes From Experience

Use these as the guardrails for what content can credibly claim:

- AgenticOps architecture and production adoption — the full journey, not just the demo
- VibeOps in practice — what it means operationally vs. the hype
- AIOps — the gap between detection and remediation
- Network automation decay and the adoption plateau
- Why automation programmes fail (organisational, not technical causes)
- ITIL/ITSM integration with AI and agentic tooling — the real friction
- Building and leading Centres of Excellence
- Trust models for autonomous agents on live production infrastructure
- Data quality as the prerequisite for AI reliability
- Observability and telemetry in enterprise network environments
- Leading engineering teams through change and cultural resistance
- The difference between a POC and a programme that actually runs in production
- Large-scale concurrent project delivery (mining, healthcare)
- Carrier-scale network operations (telco background)

---

## Endorsements (Use Sparingly But When Relevant)

- **Direct manager:** *"Top performer who is self-motivated, well respected by peers for both technical knowledge and ways of working, and recognised as someone who consistently demonstrates organisational values."*
- **Senior technology partner:** *"Delivering world-class technical and stakeholder management — a leader by example who keeps complex multi-vendor delivery aligned and working in harmony."*
- **Senior management appointment:** Selected as the only practitioner to lead Enterprise Network operations in the manager's absence.
