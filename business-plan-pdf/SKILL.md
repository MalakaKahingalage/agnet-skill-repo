---
name: business-plan-pdf
description: "Generate a professional, clean business plan PDF from any markdown file. Produces an A4 PDF with a navy-branded cover page, table of contents, document control, revision history, styled tables with navy headers, code blocks, blockquote callouts, and status badges. No company-specific branding. WHEN: convert business plan to PDF, export strategy document, create investor-ready document, generate plan PDF, produce professional business document, export markdown as PDF."
---

## What I do

I convert any markdown document into a polished, professional A4 business plan PDF using a clean navy colour scheme. Output is suitable for investors, stakeholders, or management review.

**Output features:**
- Cover page with title, subtitle, author, date, and classification banner
- Navy accent bars (top and bottom) on cover — no company logo
- Table of contents (auto-numbered from `##` headings)
- Document Control and Revision History pages
- Running page headers (doc title left, "Business Plan" right) and page number footers
- Styled tables with navy header rows and alternating row shading
- Status badges (🔴 🟠 🟡 ✅ ❌) rendered as coloured HTML spans
- Code blocks with monospace styling
- Blockquote callout boxes with navy left border

## When to use me

- Creating business plans, strategy documents, or pitch decks in document form
- Exporting markdown planning docs as a shareable professional PDF
- Producing investor-ready or management-ready deliverables
- Generating any confidential business document from markdown

## Prerequisites

- Python 3 with `weasyprint` installed (`pip install weasyprint`)
- The source markdown file must exist

## How to run

### Step 1 — Identify inputs

Collect from the user:
1. **Source markdown file** — full absolute path
2. **Output PDF path** — where to save (default: same folder as source, same name with `.pdf`)
3. **Document title** — shown on cover (default: inferred from first `#` heading)
4. **Subtitle** — optional second line on cover (default: blank)
5. **Prepared By** — author or team name (default: blank)
6. **Classification** — cover label (default: `CONFIDENTIAL`)
7. **Scope** — brief scope/description for cover metadata (default: blank)

Use `ask_user` for any missing critical inputs (source path at minimum).

### Step 2 — Run the generator

```bash
python3 ~/.agents/skills/business-plan-pdf/generate_pdf.py \
  --input  "/absolute/path/to/plan.md" \
  --output "/absolute/path/to/output.pdf" \
  --title  "Business Plan Title" \
  --subtitle "Optional Subtitle" \
  --prepared-by "Author / Team" \
  --classification "CONFIDENTIAL" \
  --scope "Brief scope description"
```

All arguments except `--input` are optional.

### Step 3 — Verify output

```bash
python3 -c "
from pypdf import PdfReader
r = PdfReader('/path/to/output.pdf')
print(f'Pages: {len(r.pages)}')
"
ls -lh /path/to/output.pdf
```

### Step 4 — Report to user

Tell the user:
- Output file path
- File size
- Page count
- The exact command used (so they can regenerate)

## Argument reference

| Argument | Required | Default | Description |
|---|---|---|---|
| `--input` | ✅ Yes | — | Absolute path to source `.md` file |
| `--output` | No | Source path with `.pdf` extension | Output PDF path |
| `--title` | No | First `#` heading from markdown | Cover page main title |
| `--subtitle` | No | _(blank)_ | Cover page subtitle |
| `--prepared-by` | No | _(blank)_ | Author / team name |
| `--classification` | No | `CONFIDENTIAL` | Cover banner and footer label |
| `--scope` | No | _(blank)_ | Scope / description line on cover |
| `--date` | No | Today's date | Override document date |

## Markdown features supported

| Markdown | Rendered as |
|---|---|
| `# Heading 1` | Skipped (used for cover title only) |
| `## Heading 2` | Navy section header + page break before |
| `### Heading 3` | Bold dark subheading |
| `#### Heading 4` | Small bold label |
| `\| table \| rows \|` | Styled table with navy header row |
| `` `code` `` | Inline code (grey background) |
| ```` ```block``` ```` | Code fence (grey background, monospace) |
| `> blockquote` | Navy left-border callout box |
| `**bold**` | Bold |
| `*italic*` | Italic |
| `- list item` | Unordered list |
| `1. item` | Ordered list |
| `---` | Horizontal rule |
| `🔴 🟠 🟡` | Coloured dot badges |
| `✅ ❌` | ✓ / ✗ symbols |

## Design

| Element | Value |
|---|---|
| Primary colour | Navy `#1A3A5C` |
| Body text | Dark `#1A1A1A` |
| Secondary text | Grey `#6B7280` |
| Table alt rows | Light grey `#F3F4F6` |
| Logo | None (no company branding) |
| Page size | A4 |

## Installing dependencies

```bash
pip install weasyprint pypdf
```

## Example invocations

### Convert a business plan markdown file
```
User: "Convert my_business_plan.md to a PDF"

Agent steps:
1. Run generate_pdf.py --input /path/my_business_plan.md
2. Verify page count and file size
3. Report: "PDF saved to /path/my_business_plan.pdf — 12 pages, 280 KB"
```

### With full metadata
```
User: "Create a PDF of strategy.md, prepared by Jane Smith, subtitle 'FY2026 Growth Strategy'"

Agent steps:
1. Run with --prepared-by "Jane Smith" --subtitle "FY2026 Growth Strategy"
2. Verify and report
```

---

**Version:** 1.0
**Created:** 2026-03-28
**Depends on:** `weasyprint`, Python 3.10+
**Script:** `generate_pdf.py` (same directory as this SKILL.md)
