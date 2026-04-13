# Writing Standards — Technical Documents

Used by the tech-doc-writer skill for ALL document types.

---

## YAML Frontmatter (always first)

```yaml
---
title: "{Platform} - {Document Type}"
platform: "{Platform Name}"
environment: "{Prod OT / Prod IT / Dev / Lab}"
server: "{hostname.domain}"          # omit if not applicable
document_type: "{As-Built / HLD / Security Guide / Reference}"
version: "1.0"
status: "{Draft / Review / Approved / Operational}"
date: "{YYYY-MM-DD}"
author: "{Author Name}"
classification: "Internal - Rio Tinto Confidential"
---
```

---

## File Naming Convention

| Type | Pattern |
|---|---|
| As-Built | `{Platform}_AsBuilt_{hostname}.md` |
| HLD | `{Platform}_HLD.md` |
| Security Guide | `{Platform}_Security_Guide.md` |
| Reference Doc | `{Platform}_Reference_{hostname}.md` |
| Troubleshooting Guide | `{Platform}_Troubleshooting_Guide.md` |
| Recovery Runbook | `{Platform}_Recovery_Runbook.md` |

Use underscores, no spaces. PascalCase for platform names.

---

## Classification Levels

| Label | Use for |
|---|---|
| `Public` | External-facing, no sensitive content |
| `Internal - Rio Tinto Confidential` | Standard internal docs |
| `Restricted - OT Operations Only` | OT-specific, limited distribution |
| `🔴 HIGHLY CONFIDENTIAL` | Credentials, secrets, PII |

---

## Document Control Block (required in every document)

```markdown
## Document Control

| Version | Date | Author | Description |
|---|---|---|---|
| 1.0 | YYYY-MM-DD | Author Name | Initial document |

### Distribution
- **Primary Audience:** [list roles]
- **Classification:** Internal - Rio Tinto Confidential
- **Review Cycle:** Quarterly or upon major changes
```

---

## RAG Status Indicators

| Emoji | Meaning |
|---|---|
| 🟢 Green | Healthy / On-track / Compliant |
| 🟡 Amber | Warning / Needs attention |
| 🔴 Red | Critical / Non-compliant / Failed |
| ✅ | Complete / Operational |
| ❌ | Failed / Not implemented |
| ⚠️ | Caution / Action required |

---

## Heading Levels

- `#` — Document title (one per doc)
- `##` — Major section (numbered: `## 1. Executive Summary`)
- `###` — Sub-section (`### 1.1 Overview`)
- `####` — Detail level (`#### Component Name`)

---

## Table Style

All tables must have a header row and use `|---|` separators.
For status tables, include a RAG column as the last column.

---

## Code Blocks

Use fenced code blocks with language tag:
```bash
# Shell commands
```
```yaml
# Config files
```
```
# Generic / unknown
```

---

## Section Separator

Use `---` (horizontal rule) between major sections.

---

## Checklist Format

Audit and action checklists use:
```
- [ ] Item not done
- [x] Item complete
```
