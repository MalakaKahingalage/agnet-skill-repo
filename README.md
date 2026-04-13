# 🧠 Agent Skills Repository

A curated library of **pi coding-agent skills** used by Malaka's AI agent setup.  
Each skill is a self-contained directory with a `SKILL.md` instruction file and any supporting scripts or reference documents the agent needs.

---

## 📁 Skill Index

| Skill | Description |
|---|---|
| [`business-plan-pdf`](#business-plan-pdf) | Generate a professional, navy-branded business plan PDF from any Markdown file |
| [`linkedin-writer`](#linkedin-writer) | Write LinkedIn articles and posts in Malaka's authentic practitioner voice |
| [`manage-terminal`](#manage-terminal) | Control a tmux session (`NetOps_BAU`) — send commands and read pane output |
| [`minimalist-business-plan`](#minimalist-business-plan) | Build a full research-backed business plan using the Minimalist Entrepreneur framework |
| [`pdf`](#pdf) | Read, extract, search, and summarise content from PDF files |
| [`rt-branded-pdf`](#rt-branded-pdf) | Generate a Rio Tinto corporate-branded PDF from any Markdown file |
| [`tech-doc-writer`](#tech-doc-writer) | Write enterprise-grade technical documents — As-Built, HLD, Security Guides, and more |
| [`webresearch`](#webresearch) | Research any topic online — fetches web pages, docs, APIs, and news |

---

## 📖 Skill Details

### `business-plan-pdf`
Converts a Markdown business plan into a clean, professional A4 PDF.  
Features a navy-branded cover page, auto-generated table of contents, document control block, revision history, styled tables, code blocks, blockquote callouts, and status badges.  
**Trigger:** *"convert business plan to PDF", "export strategy document", "create investor-ready document"*

---

### `linkedin-writer`
Drafts LinkedIn articles, posts, and comments in Malaka's authentic voice — experience-based, practitioner-to-practitioner storytelling grounded in 20+ years of enterprise network and AI operations.  
Always aligns with real production experience and avoids theory and vendor marketing language.  
**Trigger:** *"write a LinkedIn post", "draft a LinkedIn article", "improve a LinkedIn comment"*

---

### `manage-terminal`
Uses the tmux terminal driver to send commands to the `NetOps_BAU` tmux session and read output from individual panes.  
**Trigger:** *"run a command in the terminal", "send to the NetOps session", "read the terminal output"*

---

### `minimalist-business-plan`
Builds a complete, research-backed business plan from any raw idea using the full **Minimalist Entrepreneur** framework.  
Reads all existing idea documents, applies 10 framework skills, runs 10 parallel web research tracks (including WA government sites, grants, market stats, competitors), and produces:
- `plan_v2.md` — 13-section full plan  
- Client discovery questions document  
- Compliance + ABN/ASIC checklist  
- Exported branded professional PDF  

**Trigger:** *"build a business plan", "plan a startup", "turn my idea into a plan", "plan a side hustle"*

---

### `pdf`
Reads, extracts, and analyses content from PDF files.  
Supports full extraction, page-range targeting, keyword search, and summary mode.  
Uses `pymupdf` for clean text extraction with noise removal.  
**Trigger:** *"read a PDF", "extract text from PDF", "summarise PDF", "search PDF for content"*

---

### `rt-branded-pdf`
Generates an authentic Rio Tinto corporate-branded A4 PDF from any Markdown file.  
Matches the RT document template: white cover with the RioTinto SVG logo, black H2 rules, running header (document title left / logo right), light grey footer, styled tables, code blocks, and a classification banner.  
**Trigger:** *"generate a Rio Tinto document", "create branded PDF", "export report as PDF", "leadership report"*

---

### `tech-doc-writer`
Produces structured, professional enterprise technical documents for network and OT platforms.  
Document types supported: **As-Built**, **HLD**, **Reference Doc**, **Security Guide**, **Troubleshooting Guide**.  
All documents include YAML frontmatter, document control, version history, and correct classification headers.  
**Trigger:** *"write an as-built", "create an HLD", "document a platform", "write a security guide", "write technical documentation"*

---

### `webresearch`
Researches any topic on the internet — fetches web pages, documentation, articles, APIs, and technical references.  
Supports an optional HTTP proxy via the `RESEARCH_PROXY` environment variable.  
**Trigger:** *"research a topic", "look up anything online", "fetch documentation", "find news or technical references"*

---

## 🗂️ Repository Structure

```
agnet-skill-repo/
├── README.md
├── business-plan-pdf/
│   ├── SKILL.md
│   └── generate_pdf.py
├── linkedin-writer/
│   ├── SKILL.md
│   └── references/
│       ├── career-reference.md
│       └── voice-and-style.md
├── manage-terminal/
│   └── SKILL.md
├── minimalist-business-plan/
│   └── SKILL.md
├── pdf/
│   ├── SKILL.md
│   └── scripts/
│       └── read.py
├── rt-branded-pdf/
│   ├── SKILL.md
│   ├── generate_pdf.py
│   └── logo.svg
├── tech-doc-writer/
│   ├── SKILL.md
│   └── refs/
│       ├── asbuilt-guide.md
│       ├── hld-guide.md
│       ├── reference-doc-guide.md
│       ├── security-guide.md
│       ├── troubleshooting-guide.md
│       └── writing-standards.md
└── webresearch/
    ├── SKILL.md
    └── scripts/
        ├── extract.py
        └── fetch.sh
```

---

## ℹ️ How Skills Work

Skills are loaded by the **pi coding agent** at runtime.  
When a user's request matches a skill's trigger phrases, the agent reads the `SKILL.md` file for that skill and follows its instructions — including running any supporting scripts in the skill's directory.

To add a new skill: create a new directory, add a `SKILL.md` with a `name` and `description` in the YAML frontmatter, and include any supporting files.

---

*Last updated: April 2026*
