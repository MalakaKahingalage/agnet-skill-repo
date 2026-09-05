# Formatting Guide

This skill uses the same visual language as the recent polished exports in this workspace.

## Default look

- A4 pages
- dark navy header on the first page
- strong name line
- lighter blue headline line
- compact contact row
- single-column body
- uppercase section titles with thin divider line
- dense but readable body typography
- subtle blue accent on bullets and proof blocks

## Resume formatting rules

- Resume body should stay single-column.
- Keep section titles short and consistent.
- Use grouped blocks for roles, with:
  - role title
  - employer and location
  - date pill on the right
  - optional short intro line
  - bullets underneath
- Use proof blocks near the top when the role benefits from visible metrics.
- Use typography and spacing to control density before cutting valuable evidence.
- Avoid tables unless there is a compelling reason. Single-column bullet structure is safer for PDF stability.

## Cover letter formatting rules

- Keep the same header system as the resume.
- Use a simple section label such as `Cover Letter`.
- Body should remain paragraph-based, not bullet-heavy.
- Do not over-stylize the letter.
- Prefer a clean two-page result over making the text too small.

## Page-break rules

- Prevent headers from splitting from the first line of content below them.
- Prevent role headers from splitting from their intro line.
- Keep proof blocks together.
- Keep narrow grouped elements together where possible.
- Do not aggressively force every section onto one page; that usually harms density and flow.

## Content handling rules

- Markdown is the source of truth.
- HTML is the output layout layer.
- When converting to HTML, preserve wording exactly unless the user asked for content edits.
- Do not silently shorten or paraphrase text just to improve layout.

## PDF workflow rules

- Render with WeasyPrint.
- If available, generate a preview PNG of page 1 for visual checking.
- Confirm the final PDF path in the response.

## Practical defaults

- Resume PDFs can be multiple pages when the evidence warrants it.
- Cover letters can be one or two pages.
- Do not chase artificial one-page outcomes if it weakens readability or credibility.
