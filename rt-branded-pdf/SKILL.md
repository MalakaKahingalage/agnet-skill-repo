---
name: rt-branded-pdf
description: "Generate a Rio Tinto corporate-branded PDF document from any markdown file. Produces an authentic A4 PDF matching the RT template — clean white cover with RioTinto SVG logo, black h2 rules, running header (doc title left, logo right), light grey footer, styled tables, code blocks, and classification banner. WHEN: convert markdown to PDF, generate leadership report, create branded document, export report as PDF, Rio Tinto document template, share with management."
---

## What I do

I convert any markdown document into a polished, Rio Tinto branded A4 PDF using the corporate colour scheme (RT Red `#BE0000`). Output is suitable for sharing with leadership, management, or external stakeholders.

**Output features:**
- Cover page with RT logo box, document metadata table, CONFIDENTIAL banner
- Table of contents (auto-built from headings)
- Running page headers and footers with page numbers
- Styled tables with dark header rows and alternating row shading
- Urgency/status badges (🔴 🟠 🟡 ✅ ❌) rendered as styled HTML spans
- Stat highlight cards for executive summary numbers
- Code blocks with monospace styling
- Blockquote callout boxes
- Section page breaks

## When to use me

- Creating reports for leadership / management
- Exporting markdown specs or documentation as a shareable PDF
- Producing Rio Tinto branded deliverables from any markdown source
- Generating stage reports, compliance summaries, or design documents

## Prerequisites

- Python 3 with `weasyprint` installed (`pip install weasyprint`)
- The source markdown file must exist
- Internet connectivity is **not** required (fonts fall back to Arial)

## How to run

### Step 1 — Identify inputs

Collect from the user:
1. **Source markdown file** — full absolute path
2. **Output PDF path** — where to save (default: same folder as source, same name with `.pdf`)
3. **Document title** — shown on cover page (default: inferred from first `#` heading)
4. **Document subtitle** — optional second line on cover (default: blank)
5. **Prepared By** — team or person name (default: `Network Platform Team`)
6. **Classification** — cover banner text (default: `CONFIDENTIAL — INTERNAL USE ONLY`)
7. **Scope line** — brief scope description for cover metadata (default: blank)

Use `ask_user` for any missing critical inputs (source path and title at minimum).

### Step 2 — Run the generator

The generator script lives at:
```
/home/malakak/dev_area/.github/skills/rt-branded-pdf/generate_pdf.py
```

Call it from the project directory:

```bash
python3 /home/malakak/dev_area/.github/skills/rt-branded-pdf/generate_pdf.py \
  --input  "/absolute/path/to/source.md" \
  --output "/absolute/path/to/output.pdf" \
  --title  "Document Title" \
  --subtitle "Optional Subtitle" \
  --prepared-by "Team Name" \
  --classification "CONFIDENTIAL — INTERNAL USE ONLY" \
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

Confirm the PDF is valid (`%PDF-` header) and the page count looks right.

### Step 4 — Report to user

Tell the user:
- Output file path
- File size
- Page count
- How to regenerate (the exact command)

## Argument reference

| Argument | Required | Default | Description |
|---|---|---|---|
| `--input` | ✅ Yes | — | Absolute path to source `.md` file |
| `--output` | No | Source path with `.pdf` extension | Output PDF path |
| `--title` | No | First `#` heading from markdown | Cover page main title |
| `--subtitle` | No | _(blank)_ | Cover page subtitle (second line) |
| `--prepared-by` | No | `Network Platform Team` | Cover metadata field |
| `--classification` | No | `CONFIDENTIAL — INTERNAL USE ONLY` | Cover banner text and footer |
| `--scope` | No | _(blank)_ | Cover metadata scope/summary line |
| `--date` | No | Today's date | Override document date |

## Markdown features supported

| Markdown | Rendered as |
|---|---|
| `# Heading 1` | Skipped (used for cover title) |
| `## Heading 2` | Red section header bar, page break before |
| `### Heading 3` | Red left-border subheading |
| `#### Heading 4` | Small uppercase grey label |
| `\| table \| rows \|` | Styled table with dark header |
| `` `code` `` | Inline code (red monospace) |
| ```` ```block``` ```` | Code fence (grey background) |
| `> blockquote` | Left red border callout box |
| `**bold**` | Bold |
| `*italic*` | Italic |
| `- list item` | Unordered list |
| `1. item` | Ordered list |
| `---` | Horizontal rule |
| `🔴 🟠 🟡` | Coloured dot badges |
| `✅ ❌` | ✓ / ✗ symbols |

## Generator script location

```
/home/malakak/dev_area/.github/skills/rt-branded-pdf/generate_pdf.py
```

The script is self-contained. Copy it to any project or call it from its global location.

## Installing dependencies

```bash
pip install weasyprint pypdf
```

`weasyprint` handles HTML→PDF rendering. `pypdf` is optional (used only for page count verification).

## Customisation

To change branding colours, edit the constants at the top of `generate_pdf.py`:

```python
RT_RED   = "#BE0000"   # Primary Rio Tinto red
RT_DARK  = "#1A1A1A"   # Body text
RT_GREY  = "#4A4A4A"   # Secondary text
RT_LIGHT = "#F7F7F7"   # Table alternating rows / backgrounds
```

To add a real logo image instead of the `RT` text box, replace the `.cover-logo-box` block in the CSS and HTML cover template with an `<img>` tag pointing to a PNG/SVG logo file.

## Example invocations

### Convert a report for leadership sharing
```
User: "Convert stage1_reports.md to a PDF I can share with leadership"

Agent steps:
1. ask_user for output path if not specified
2. Run generate_pdf.py with --input and appropriate --title
3. Verify page count and file size
4. Report back: "PDF saved to /path/Stage1_Reports_RioTinto.pdf — 19 pages, 353 KB"
```

### Convert any project spec
```
User: "I need a branded PDF of specs.md"

Agent steps:
1. Infer title from first heading in specs.md
2. Run generator with defaults
3. Verify and report
```

---

**Version:** 1.0
**Created:** 2026-03-16
**Author:** Network Platform Team
**Depends on:** `weasyprint`, Python 3.10+
**Script:** `generate_pdf.py` (same directory as this SKILL.md)
