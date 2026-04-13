#!/usr/bin/env python3
"""
Generate a professional business plan PDF from any markdown file.

Usage:
  python3 generate_pdf.py --input plan.md [--output plan.pdf] [--title "My Business Plan"]
                          [--subtitle "Subtitle"] [--prepared-by "Author"]
                          [--classification "CONFIDENTIAL"] [--scope "Scope line"]
                          [--date "28 March 2026"]
"""
import argparse
import os
import re
import sys
import datetime

# ── Brand colours ─────────────────────────────────────────────────────────────
NAVY        = "#1A3A5C"   # Primary navy blue — headings, accents
DARK        = "#1A1A1A"   # Body text
GREY        = "#6B7280"   # Secondary / footer text
LIGHT       = "#F3F4F6"   # Table alternating rows / code backgrounds
BORDER      = "#D1D5DB"   # Table / rule borders
ACCENT      = "#1A3A5C"   # Same navy for accent use


# ── HTML/CSS template ─────────────────────────────────────────────────────────
CSS = f"""
/* ── Page layout ── */
@page {{
    size: A4;
    margin: 28mm 20mm 28mm 20mm;

    @top-left {{
        content: element(doc-header);
        vertical-align: top;
        padding-top: 5mm;
    }}
    @top-center {{ content: none; }}
    @top-right  {{ content: none; }}

    @bottom-left   {{ content: none; }}
    @bottom-center {{
        content: element(doc-footer);
        vertical-align: top;
    }}
    @bottom-right {{
        content: counter(page) " / " counter(pages);
        font-family: Arial, sans-serif;
        font-size: 7pt;
        color: {GREY};
        vertical-align: top;
        padding-top: 4pt;
        text-align: right;
        width: 20mm;
    }}
}}

/* Cover page — no running headers/footers, no margins */
@page :first {{
    margin: 0;
    @top-left      {{ content: none; }}
    @top-center    {{ content: none; }}
    @top-right     {{ content: none; }}
    @bottom-left   {{ content: none; border-top: none; }}
    @bottom-center {{ content: none; border-top: none; }}
    @bottom-right  {{ content: none; border-top: none; }}
}}

/* ── Running header ── */
#doc-header {{
    position: running(doc-header);
    width: 170mm;
    border-bottom: 0.75pt solid {NAVY};
    padding-bottom: 3pt;
    overflow: hidden;
}}

.hdr-right {{
    float: right;
    line-height: 1;
    font-family: Arial, sans-serif;
    font-size: 7pt;
    font-weight: bold;
    color: {NAVY};
    letter-spacing: 0.5pt;
    text-transform: uppercase;
}}

.hdr-left {{
    font-family: Arial, sans-serif;
    font-size: 7pt;
    color: {DARK};
    line-height: 2.2;
    overflow: hidden;
}}

/* ── Running footer ── */
#doc-footer {{
    position: running(doc-footer);
    font-family: Arial, sans-serif;
    font-size: 7.5pt;
    color: {GREY};
    text-align: center;
    padding-top: 4pt;
    width: 100%;
}}

/* ── Base styles ── */
* {{ box-sizing: border-box; margin: 0; padding: 0; }}

body {{
    font-family: Arial, sans-serif;
    font-size: 10pt;
    color: {DARK};
    line-height: 1.5;
    background: white;
}}

/* ══════════════════════════════
   COVER PAGE
══════════════════════════════ */
.cover {{
    width: 210mm;
    height: 297mm;
    position: relative;
    background: white;
    page-break-after: always;
}}

/* Navy accent bar at top */
.cover-top-bar {{
    width: 100%;
    height: 12mm;
    background: {NAVY};
}}

/* Navy accent bar at bottom */
.cover-bottom-bar {{
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
    height: 8mm;
    background: {NAVY};
}}

.cover-body {{
    padding: 20mm 20mm 18mm 20mm;
}}

.cover-label {{
    font-family: Arial, sans-serif;
    font-size: 9pt;
    font-weight: bold;
    color: {NAVY};
    letter-spacing: 1.5pt;
    text-transform: uppercase;
    margin-bottom: 8mm;
}}

.cover-title {{
    font-family: Arial, sans-serif;
    font-size: 30pt;
    font-weight: bold;
    color: {DARK};
    line-height: 1.15;
    margin-bottom: 4mm;
}}

.cover-subtitle {{
    font-family: Arial, sans-serif;
    font-size: 14pt;
    font-weight: normal;
    color: {GREY};
    margin-bottom: 14mm;
}}

.cover-divider {{
    width: 20mm;
    height: 2pt;
    background: {NAVY};
    margin-bottom: 10mm;
}}

.cover-meta {{
    font-family: Arial, sans-serif;
    font-size: 10pt;
    color: {DARK};
    line-height: 1.8;
}}

.cover-footer {{
    position: absolute;
    bottom: 12mm;
    left: 20mm;
    right: 20mm;
}}

.cover-footer p {{
    font-family: Arial, sans-serif;
    font-size: 8pt;
    color: {GREY};
    line-height: 1.5;
    margin: 0;
}}

/* ══════════════════════════════
   MAIN CONTENT
══════════════════════════════ */
.section {{
    page-break-before: always;
}}

/* ── h2 — main section heading + navy rule below ── */
h2 {{
    font-family: Arial, sans-serif;
    font-size: 16pt;
    font-weight: bold;
    color: {NAVY};
    margin: 0 0 3pt 0;
    padding: 0 0 4pt 0;
    border-bottom: 1.5pt solid {NAVY};
    page-break-after: avoid;
}}

/* ── h3 ── */
h3 {{
    font-family: Arial, sans-serif;
    font-size: 13pt;
    font-weight: bold;
    color: {DARK};
    margin: 12pt 0 4pt 0;
    padding: 0;
    page-break-after: avoid;
}}

/* ── h4 ── */
h4 {{
    font-family: Arial, sans-serif;
    font-size: 10pt;
    font-weight: bold;
    color: {DARK};
    margin: 8pt 0 2pt 0;
    page-break-after: avoid;
}}

p {{
    margin: 0 0 7pt 0;
    font-size: 10pt;
    color: {DARK};
}}

strong {{ font-weight: bold; }}
em     {{ font-style: italic; }}

/* ── Tables ── */
table {{
    border-collapse: collapse;
    width: 100%;
    margin: 6pt 0 10pt 0;
    font-size: 9.5pt;
    page-break-inside: avoid;
}}

thead tr {{
    background: {NAVY};
}}

thead th {{
    padding: 5pt 7pt;
    text-align: left;
    font-weight: bold;
    font-size: 9.5pt;
    border: 0.75pt solid {BORDER};
    color: white;
    background: {NAVY};
}}

tbody tr:nth-child(even)  {{ background: {LIGHT}; }}
tbody tr:nth-child(odd)   {{ background: white; }}

tbody td {{
    padding: 4pt 7pt;
    border: 0.75pt solid {BORDER};
    vertical-align: top;
    color: {DARK};
    font-size: 9.5pt;
}}

tbody td:first-child {{ font-weight: bold; }}

/* ── Detail/compact table ── */
.detail-table table  {{ font-size: 7.5pt; margin: 4pt 0 8pt 0; page-break-inside: auto; }}
.detail-table thead th {{
    font-size: 7.5pt; padding: 3pt 5pt;
    background: {NAVY}; color: white;
    border: 0.5pt solid {BORDER};
}}
.detail-table tbody td {{
    font-size: 7.5pt; padding: 2.5pt 5pt; border: 0.5pt solid {BORDER};
}}
.detail-table tbody td:first-child {{ font-weight: bold; max-width: 100pt; }}
.detail-table tbody tr:nth-child(even) {{ background: {LIGHT}; }}

/* ── Inline code ── */
code {{
    font-family: 'Courier New', Courier, monospace;
    font-size: 8.5pt;
    background: {LIGHT};
    padding: 1pt 3pt;
    border: 0.5pt solid {BORDER};
    color: {DARK};
}}

/* ── Code block ── */
pre {{
    font-family: 'Courier New', Courier, monospace;
    font-size: 8pt;
    background: {LIGHT};
    border: 0.75pt solid {BORDER};
    padding: 7pt 9pt;
    white-space: pre-wrap;
    word-wrap: break-word;
    margin: 5pt 0 8pt 0;
    color: {DARK};
    page-break-inside: avoid;
}}

/* ── Blockquote — navy left-border callout ── */
blockquote {{
    border-left: 3pt solid {NAVY};
    padding: 4pt 10pt;
    margin: 5pt 0 8pt 0;
    font-size: 9.5pt;
    color: #333;
    font-style: italic;
    background: {LIGHT};
}}

blockquote p {{ margin: 0; }}

/* ── Lists ── */
ul, ol {{
    margin: 2pt 0 6pt 18pt;
    padding: 0;
}}

li {{
    margin: 2pt 0;
    font-size: 10pt;
}}

/* ── HR ── */
hr {{
    border: none;
    border-top: 0.5pt solid {BORDER};
    margin: 8pt 0;
}}

/* ── Status badges ── */
.badge-red    {{ color: #CC0000; font-weight: bold; }}
.badge-orange {{ color: #CC5500; font-weight: bold; }}
.badge-yellow {{ color: #886600; font-weight: bold; }}
.badge-green  {{ color: #007700; font-weight: bold; }}

/* ── Document Control table ── */
.meta-table {{
    border-collapse: collapse;
    width: 100%;
    margin: 8pt 0;
    font-size: 10pt;
}}

.meta-table td {{
    padding: 4pt 6pt 4pt 0;
    border-bottom: 0.5pt solid {BORDER};
    vertical-align: top;
}}

.meta-table td:first-child {{
    font-weight: bold;
    width: 42mm;
    color: {DARK};
}}

/* ── Change log table ── */
.changelog-table {{
    border-collapse: collapse;
    width: 100%;
    margin: 6pt 0;
    font-size: 9.5pt;
}}

.changelog-table th {{
    font-weight: bold;
    border: 0.75pt solid {BORDER};
    padding: 4pt 6pt;
    text-align: left;
    background: {NAVY};
    color: white;
}}

.changelog-table td {{
    padding: 3pt 6pt;
    border: 0.75pt solid {BORDER};
}}

/* ── TOC ── */
.toc-body {{
    margin: 8pt 0;
}}

.toc-item {{
    display: flex;
    padding: 4pt 0;
    border-bottom: 0.5pt solid {BORDER};
    font-size: 10pt;
}}

.toc-item-section {{
    width: 30mm;
    font-weight: bold;
    color: {NAVY};
    flex-shrink: 0;
}}

.toc-item-title {{
    flex: 1;
    color: {DARK};
}}
"""

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<style>{css}</style>
</head>
<body>

<!-- ── Running header ── -->
<div id="doc-header">
  <span class="hdr-right">Business Plan</span>
  <span class="hdr-left">{doc_title_short}</span>
</div>

<!-- ── Running footer ── -->
<div id="doc-footer">
  {doc_title_short} &nbsp;|&nbsp; {classification}
</div>

<!-- ══════════════════════════════════════════
     COVER PAGE
══════════════════════════════════════════ -->
<div class="cover">

  <div class="cover-top-bar"></div>

  <div class="cover-body">

    <div class="cover-label">Business Plan</div>

    <div class="cover-title">{title_html}</div>

    {subtitle_html}

    <div class="cover-divider"></div>

    <div class="cover-meta">
      <strong>Prepared by:</strong> {prepared_by}<br/>
      <strong>Date:</strong> {date}<br/>
      {scope_line}
      <strong>Classification:</strong> {classification}
    </div>

  </div>

  <div class="cover-footer">
    <p>{classification}</p>
    <p>This document contains confidential and proprietary information. Unauthorised distribution is prohibited.</p>
  </div>

  <div class="cover-bottom-bar"></div>

</div>

<!-- ══════════════════════════════════════════
     DOCUMENT CONTROL PAGE
══════════════════════════════════════════ -->
<div class="section">
<h2>Document Control</h2>

<table class="meta-table">
  <tr><td>Document Name</td><td>{title_html}</td></tr>
  <tr><td>Document Status</td><td>Draft</td></tr>
  <tr><td>Version</td><td>0.1</td></tr>
  <tr><td>Prepared By</td><td>{prepared_by}</td></tr>
  <tr><td>Date</td><td>{date}</td></tr>{extra_meta_rows}
</table>
</div>

<!-- ══════════════════════════════════════════
     CHANGE LOG PAGE
══════════════════════════════════════════ -->
<div class="section">
<h2>Revision History</h2>
<table class="changelog-table">
  <thead><tr><th>Version</th><th>Date</th><th>Author</th><th>Description</th></tr></thead>
  <tbody>
    <tr><td>0.1</td><td>{date}</td><td>{prepared_by}</td><td>Initial draft</td></tr>
  </tbody>
</table>
</div>

{body}

</body>
</html>
"""


def md_table_to_html(block: str) -> str:
    """Convert a markdown table block to an HTML table."""
    lines = [l.strip() for l in block.strip().splitlines() if l.strip()]
    rows = [l for l in lines if not re.match(r'^[\|\s\-:]+$', l)]
    if not rows:
        return ""

    html = "<table>\n"
    for i, row in enumerate(rows):
        cells = [c.strip() for c in row.strip('|').split('|')]
        tag = "th" if i == 0 else "td"
        if i == 0:
            html += "<thead><tr>"
        elif i == 1:
            html += "</thead>\n<tbody>\n<tr>"
        else:
            html += "<tr>"
        for cell in cells:
            cell = inline_md(cell)
            html += f"<{tag}>{cell}</{tag}>"
        html += "</tr>\n"
    html += "</tbody>\n</table>\n"
    return html


def inline_md(text: str) -> str:
    """Convert inline markdown to HTML."""
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'\*(.+?)\*',     r'<em>\1</em>',         text)
    text = re.sub(r'`([^`]+)`',     r'<code>\1</code>',     text)
    text = re.sub(r'\[([^\]]+)\]\(([^\)]+)\)', r'<a href="\2">\1</a>', text)
    text = text.replace('🔴', '<span class="badge-red">●</span>')
    text = text.replace('🟠', '<span class="badge-orange">●</span>')
    text = text.replace('🟡', '<span class="badge-yellow">●</span>')
    text = text.replace('✅', '✓')
    text = text.replace('❌', '✗')
    return text


def md_to_html_body(md: str) -> str:
    """Convert markdown content to styled HTML body."""
    lines = md.splitlines()
    html_parts = []
    i = 0
    in_code  = False
    code_buf = []
    in_list  = False
    list_type = None
    table_buf = []
    in_table  = False

    def flush_list():
        nonlocal in_list, list_type
        if in_list:
            tag = "ul" if list_type == "ul" else "ol"
            html_parts.append(f"</{tag}>\n")
            in_list = False
            list_type = None

    def flush_table():
        nonlocal in_table, table_buf
        if in_table and table_buf:
            html_parts.append(md_table_to_html("\n".join(table_buf)))
            table_buf = []
            in_table = False

    while i < len(lines):
        line = lines[i]

        # Code fence
        if line.strip().startswith("```"):
            if in_code:
                code_content = "\n".join(code_buf)
                html_parts.append(f"<pre>{code_content}</pre>\n")
                code_buf = []
                in_code = False
            else:
                flush_list()
                flush_table()
                in_code = True
            i += 1
            continue

        if in_code:
            code_buf.append(line)
            i += 1
            continue

        # Table
        if '|' in line and line.strip().startswith('|'):
            flush_list()
            in_table = True
            table_buf.append(line)
            i += 1
            continue
        elif in_table:
            flush_table()

        # Skip h1 (used as cover title only)
        if line.startswith("# ") and not line.startswith("## "):
            i += 1
            continue

        # h2 → new page section
        if line.startswith("## "):
            flush_list()
            title = line[3:].strip()
            html_parts.append(f'<div class="section">\n<h2>{inline_md(title)}</h2>\n')
            i += 1
            continue

        if line.startswith("### "):
            flush_list()
            title = line[4:].strip()
            html_parts.append(f"<h3>{inline_md(title)}</h3>\n")
            i += 1
            continue

        if line.startswith("#### "):
            flush_list()
            title = line[5:].strip()
            html_parts.append(f"<h4>{inline_md(title)}</h4>\n")
            i += 1
            continue

        if re.match(r'^---+$', line.strip()):
            flush_list()
            html_parts.append("<hr/>\n")
            i += 1
            continue

        if line.startswith("> "):
            flush_list()
            content = inline_md(line[2:])
            html_parts.append(f"<blockquote><p>{content}</p></blockquote>\n")
            i += 1
            continue

        if re.match(r'^[\-\*\+] ', line):
            if not in_list or list_type != "ul":
                if in_list:
                    flush_list()
                html_parts.append("<ul>\n")
                in_list = True
                list_type = "ul"
            html_parts.append(f"<li>{inline_md(line[2:])}</li>\n")
            i += 1
            continue

        if re.match(r'^\d+\. ', line):
            if not in_list or list_type != "ol":
                if in_list:
                    flush_list()
                html_parts.append("<ol>\n")
                in_list = True
                list_type = "ol"
            item_text = re.sub(r'^\d+\.\s', '', line)
            html_parts.append(f"<li>{inline_md(item_text)}</li>\n")
            i += 1
            continue

        flush_list()

        if not line.strip():
            i += 1
            continue

        html_parts.append(f"<p>{inline_md(line)}</p>\n")
        i += 1

    flush_list()
    flush_table()
    return "".join(html_parts)


def build_toc_from_md(md_content: str) -> str:
    """Auto-generate a table of contents from ## headings."""
    entries = []
    section_num = 0
    for line in md_content.splitlines():
        if line.startswith("## "):
            title = line[3:].strip()
            section_num += 1
            entries.append((str(section_num), title))

    if not entries:
        return ""

    rows = ""
    for label, title in entries:
        rows += f"""
    <div class="toc-item">
      <span class="toc-item-section">{label}.</span>
      <span class="toc-item-title"><strong>{inline_md(title)}</strong></span>
    </div>"""

    return f"""
<div class="section">
  <h2>Table of Contents</h2>
  <div class="toc-body">{rows}
  </div>
</div>
"""


def main():
    parser = argparse.ArgumentParser(
        description="Generate a professional business plan PDF from a markdown file."
    )
    parser.add_argument("--input",          required=True,  help="Source markdown file path")
    parser.add_argument("--output",         default=None,   help="Output PDF path (default: input with .pdf)")
    parser.add_argument("--title",          default=None,   help="Cover page main title")
    parser.add_argument("--subtitle",       default="",     help="Cover page subtitle")
    parser.add_argument("--prepared-by",    default="",     help="Author / team name")
    parser.add_argument("--classification", default="CONFIDENTIAL",
                        help="Classification label shown on cover and footer")
    parser.add_argument("--scope",          default="",     help="Scope / description line for cover")
    parser.add_argument("--date",           default=None,   help="Override document date")
    args = parser.parse_args()

    src = os.path.abspath(args.input)
    if not os.path.exists(src):
        print(f"ERROR: Input file not found: {src}", file=sys.stderr)
        sys.exit(1)

    out = args.output or os.path.splitext(src)[0] + ".pdf"
    out = os.path.abspath(out)

    with open(src, "r") as f:
        md_content = f.read()

    # Infer title from first # heading
    title = args.title
    if not title:
        for line in md_content.splitlines():
            if line.startswith("# ") and not line.startswith("## "):
                title = line[2:].strip()
                break
        if not title:
            title = os.path.splitext(os.path.basename(src))[0].replace("_", " ").replace("-", " ").title()

    today          = args.date or datetime.date.today().strftime("%-d %B %Y")
    prepared_by    = args.prepared_by
    classification = args.classification
    subtitle       = args.subtitle
    scope          = args.scope

    title_html       = title.replace("\n", "<br/>")
    doc_title_short  = title if len(title) <= 90 else title[:87] + "…"

    subtitle_html = f'<div class="cover-subtitle">{subtitle}</div>' if subtitle else ""
    scope_line    = f"<strong>Scope:</strong> {scope}<br/>\n      " if scope else ""

    extra_meta_rows = ""
    if scope:
        extra_meta_rows += f"\n  <tr><td>Scope</td><td>{scope}</td></tr>"
    if subtitle:
        extra_meta_rows += f"\n  <tr><td>Description</td><td>{subtitle}</td></tr>"

    toc_html  = build_toc_from_md(md_content)
    body_html = toc_html + md_to_html_body(md_content)

    full_html = HTML_TEMPLATE.format(
        css=CSS,
        body=body_html,
        date=today,
        prepared_by=prepared_by,
        title_html=title_html,
        subtitle_html=subtitle_html,
        doc_title_short=doc_title_short,
        classification=classification,
        extra_meta_rows=extra_meta_rows,
        scope_line=scope_line,
    )

    debug_html = os.path.join("/tmp", os.path.splitext(os.path.basename(src))[0] + "_bp_debug.html")
    with open(debug_html, "w") as f:
        f.write(full_html)

    from weasyprint import HTML
    import warnings
    warnings.filterwarnings("ignore")

    print(f"Generating PDF: {out}")
    HTML(string=full_html).write_pdf(out)
    print(f"Done — PDF written to: {out}")


if __name__ == "__main__":
    main()
