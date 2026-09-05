---
name: resume-pdf-packager
description: Build or tailor resumes, CVs, and cover letters in the established dark-header single-column format, then export them as print-ready PDFs with stable page breaks. Use when a user wants a new application pack, wants an existing resume adapted for a role, or wants markdown content converted into the standard polished PDF layout.
---

# Resume PDF Packager

## Overview

Use this skill when the user wants a resume, CV, or cover letter drafted or tailored and delivered in the established print-ready PDF style already used in this workspace: dark header, single-column layout, strong section dividers, and WeasyPrint-based export.

This skill is optimized for repeatable job application packs:
- tailored resume in markdown first
- matching cover letter in markdown first
- print HTML derived from the standard templates
- PDF export with controlled page breaks

## Workflow

1. Gather the source material.
   Read the job ad, the user's latest resume variants, and any prior tailored applications that are close in tone or scope.

2. Draft the editable source documents first.
   Create or update the resume and cover letter in markdown before touching the print HTML.
   Keep the markdown as the durable editing source.

3. Build print HTML from the standard templates.
   Use:
   - `assets/resume_print_template.html`
   - `assets/cover_letter_print_template.html`

   Copy the relevant template into the working folder, then replace the placeholders with the actual content.

4. Keep the visual system stable.
   Follow the formatting rules in `references/formatting-guide.md`.
   Do not improvise a new layout unless the user explicitly asks for a different style.

5. Export with WeasyPrint.
   Use `scripts/render_pdf.py` to render the HTML into PDF.
   If useful, also generate a first-page PNG preview for quick visual inspection.

6. Verify before delivery.
   At minimum, confirm:
   - PDF exists
   - page count is sensible
   - first page renders correctly
   - no obvious header overlap or broken section spacing
   - content was not altered during the HTML/PDF conversion

## Working Rules

- Keep the content editing in markdown; treat HTML as the presentation layer.
- Prefer single-column layouts for resumes and cover letters in this skill.
- Preserve exact wording when moving from markdown to print HTML unless the user asked for content changes.
- Use page-break control on headers, section titles, and grouped blocks so the PDF feels intentional.
- For resumes, keep the header visually strong and compress dense sections with typography before changing wording.
- For cover letters, prioritize readability over forcing a one-page result. A clean two-page letter is better than an over-compressed one.

## Template Use

### Resume template

Use `assets/resume_print_template.html` for the PDF layout. Replace:
- `{{TITLE}}`
- `{{NAME}}`
- `{{HEADLINE}}`
- `{{CONTACT_HTML}}`
- `{{BODY_HTML}}`

`{{BODY_HTML}}` should contain the fully prepared section markup.

### Cover letter template

Use `assets/cover_letter_print_template.html` for the PDF layout. Replace:
- `{{TITLE}}`
- `{{NAME}}`
- `{{HEADLINE}}`
- `{{CONTACT_HTML}}`
- `{{BODY_HTML}}`

The body should already be paragraph-ready HTML.

## Rendering

Render with:

```bash
python3 scripts/render_pdf.py input.html output.pdf --preview preview.png
```

If `weasyprint` is not available, stop and report that the PDF runtime is missing rather than silently switching to a different renderer. The format is tuned for WeasyPrint.

## Validation

For fast validation:
- use the renderer preview output when available
- use `pypdf` or `fitz` if installed to confirm page count or extract quick text
- inspect the first page visually when layout quality matters

## Resources

- Formatting and editorial rules: `references/formatting-guide.md`
- Resume print template: `assets/resume_print_template.html`
- Cover letter print template: `assets/cover_letter_print_template.html`
- PDF renderer: `scripts/render_pdf.py`
