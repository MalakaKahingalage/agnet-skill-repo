---
name: pdf
description: "Read, extract, and analyse content from PDF files. Supports full extraction, page-range targeting, keyword search, and summary mode. Uses pymupdf for clean text extraction with noise removal. WHEN: read a PDF, extract text from PDF, summarise PDF, search PDF for content, get specific pages from PDF, analyse a PDF document."
allowed-tools:
  - bash
  - read_bash
  - write_bash
---

## Autonomous Behaviour — CRITICAL

**When this skill is invoked, immediately start reading. Do NOT:**
- ❌ Ask the user for permission to open the file
- ❌ Ask "would you like me to extract the text?"
- ❌ Ask which pages to read before attempting
- ❌ Announce what you're about to do and wait for approval

**DO:**
- ✅ Open and extract the PDF immediately on the first tool call
- ✅ Choose the appropriate mode based on the request
- ✅ For large PDFs, use `summary` or `keyword` first to avoid token bloat
- ✅ Return findings directly — let the user redirect if needed

**The rule:** If you have a file path, just read it.

---

## Setup

Locate the script directory first:

```bash
SKILL_DIR=$(find ~/.agents/skills ~/.github/skills ~/.config/opencode/skills ~/.claude/skills ~/.gemini/skills -name "read.py" 2>/dev/null | head -1 | xargs dirname 2>/dev/null)
```

Or set it explicitly if you know the path:
```bash
SKILL_DIR="$HOME/.agents/skills/pdf/scripts"
```

---

## Modes

| Mode | When to use | Token cost |
|---|---|---|
| **check** | Always run first on an unknown file | Minimal |
| **summary** | First pass on large/unknown docs | Low |
| **pages** | You know which pages you need | Low |
| **keyword** | Find where specific content appears | Low |
| **full** | Small PDFs (<10 pages) or complete extraction needed | Higher |

---

## Usage

### 1. Check the file first
```bash
python3 "$SKILL_DIR/read.py" "/path/to/file.pdf" check
```

### 2. Summary — first pass on unknown docs
```bash
python3 "$SKILL_DIR/read.py" "/path/to/file.pdf" summary
```

### 3. Page range — read specific pages (1-indexed, inclusive)
```bash
python3 "$SKILL_DIR/read.py" "/path/to/file.pdf" pages 1 3
```

### 4. Keyword — find pages containing a term
```bash
python3 "$SKILL_DIR/read.py" "/path/to/file.pdf" keyword "your search term"
```

### 5. Full extraction — complete text of the whole document
```bash
python3 "$SKILL_DIR/read.py" "/path/to/file.pdf" full
# With character limit to avoid token overflow:
python3 "$SKILL_DIR/read.py" "/path/to/file.pdf" full 8000
```

---

## Error Handling

| Issue | Symptom | Response |
|---|---|---|
| File not found | `ERROR: ...` from fitz | Ask user to confirm the path |
| Password protected | `ERROR: PDF is password-protected` | Report and ask for password |
| Scanned/image PDF | `WARNING: ... no text` | Report — OCR not supported; ask user to provide text version |
| pymupdf missing | `ERROR: pymupdf not installed` | Run `pip install pymupdf` |

---

## Token Budget

- **< 10 pages:** `full` is fine
- **10–50 pages:** `summary` first, then `pages` for sections of interest
- **50+ pages:** Always use `keyword` or `pages` — never `full`
- **Resumes / short docs:** `full` is fine regardless of page count
