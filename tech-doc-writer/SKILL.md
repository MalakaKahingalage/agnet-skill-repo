---
name: tech-doc-writer
description: "Write detailed enterprise technical documents — As-Built, HLD, LLD, Reference Docs, and Security Guides — for network and OT platforms. Produces structured, professional documents with YAML frontmatter, document control, version history, and correct classification. WHEN: write an as-built, create an HLD, create an LLD, write a low-level design, document a platform, write a security guide, create a reference document, write technical documentation, document a network design, as-built for a server."
---

# Technical Document Writer

I produce enterprise-grade technical documents for network engineering and OT platforms.
I follow Rio Tinto documentation standards based on real production documents.

**Token-controlled:** I load only the reference file matching the requested document type — not all references at once.

---

## Step 1 — Identify Document Type

| User asks for… | Load reference file | Source doc for context |
|---|---|---|
| **As-Built** / as-built / AsBuilt / as built | `refs/asbuilt-guide.md` | See guide for source doc path |
| **HLD** / High-Level Design / network design | `refs/hld-guide.md` | See guide for source doc path |
| **LLD** / Low-Level Design / detailed design / engineering spec / build spec | `refs/lld-guide.md` | See guide for source doc path |
| **Security Guide** / security doc / credentials guide | `refs/security-guide.md` | See guide for source doc path |
| **Reference Doc** / port reference / config reference / credential reference | `refs/reference-doc-guide.md` | See guide for source doc path |
| **Troubleshooting Guide** / recovery guide / runbook / system down / disaster recovery / incident runbook | `refs/troubleshooting-guide.md` | See guide for source doc path |

**Read ONLY the matching reference file above. Do not load all refs at once.**

Also read `refs/writing-standards.md` — it is always required (it is small).

---

## Step 2 — Gather Inputs

Before writing, collect from the user or infer from context:
- **Platform / system name** (e.g. NetAssist, OT SCADA, Cisco WAN)
- **Environment** (Prod / Dev / Lab / OT / IT)
- **Server / hostname** (if AsBuilt or Reference)
- **Author name** (default: Malaka Kahingalage)
- **Classification** (default: Internal - Rio Tinto Confidential)
- **Any existing document or notes** to use as source material

If a source document exists, read only the sections needed — use `read` with `offset`/`limit`.

---

## Step 3 — Write the Document

Follow the structure in the loaded reference file exactly.
Apply all formatting rules from `refs/writing-standards.md`.

Always include:
1. YAML frontmatter block
2. Document Control (version history + distribution table)
3. Table of Contents with anchor links
4. All required sections from the reference file

---

## Step 4 — Save the Output

**Default save location:**
```
/mnt/c/Users/malaka.kahingalage/OneDrive - Rio Tinto/Second_Brain/RioTinto/20_Projects/2026/OT_AgenticOps/
```

**Naming convention** (from `refs/writing-standards.md`):
- AsBuilt: `{Platform}_AsBuilt_{hostname}.md`
- HLD: `{Platform}_HLD.md`
- Security Guide: `{Platform}_Security_Guide.md`
- Reference Doc: `{Platform}_Reference_{hostname}.md`

After saving, confirm: filename, path, approximate line count.

---

## Reference files (do not pre-load — read on demand)

| File | Contents | Approx size |
|---|---|---|
| `refs/writing-standards.md` | Formatting, YAML, classification, naming | ~80 lines |
| `refs/asbuilt-guide.md` | As-Built sections, checklist, OT specifics | ~120 lines |
| `refs/hld-guide.md` | HLD sections, design decisions, stakeholders | ~120 lines |
| `refs/security-guide.md` | Security posture, threat model, controls, audits | ~110 lines |
| `refs/reference-doc-guide.md` | Port tables, config reference, credential reference | ~100 lines |
| `refs/lld-guide.md` | LLD sections, IP design, protocol config, build sequence, test plan | ~180 lines |
| `refs/troubleshooting-guide.md` | Diagnosis runbook, common issues, DR procedure, log reference | ~230 lines |
