#!/usr/bin/env python3
"""
Render a print HTML file to PDF using WeasyPrint.

Optional:
- generate a first-page PNG preview when PyMuPDF (`fitz`) is installed
- print PDF page count when pypdf is installed
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path


def render_pdf(html_path: Path, pdf_path: Path) -> None:
    weasyprint = shutil.which("weasyprint")
    if not weasyprint:
        raise RuntimeError("weasyprint is not installed or not on PATH")

    pdf_path.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run([weasyprint, str(html_path), str(pdf_path)], check=True)


def render_preview(pdf_path: Path, preview_path: Path) -> None:
    try:
        import fitz  # type: ignore
    except Exception as exc:  # pragma: no cover
        raise RuntimeError("PyMuPDF (fitz) is not installed") from exc

    doc = fitz.open(pdf_path)
    page = doc[0]
    pix = page.get_pixmap(matrix=fitz.Matrix(1.6, 1.6), alpha=False)
    preview_path.parent.mkdir(parents=True, exist_ok=True)
    pix.save(preview_path)


def get_page_count(pdf_path: Path) -> int | None:
    try:
        from pypdf import PdfReader  # type: ignore
    except Exception:
        return None
    return len(PdfReader(str(pdf_path)).pages)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("html", help="Input HTML file")
    parser.add_argument("pdf", help="Output PDF file")
    parser.add_argument("--preview", help="Optional output PNG for first-page preview")
    args = parser.parse_args()

    html_path = Path(args.html).resolve()
    pdf_path = Path(args.pdf).resolve()

    if not html_path.exists():
        print(f"[ERROR] Missing input HTML: {html_path}", file=sys.stderr)
        return 1

    try:
        render_pdf(html_path, pdf_path)
    except Exception as exc:
        print(f"[ERROR] PDF render failed: {exc}", file=sys.stderr)
        return 1

    print(f"[OK] PDF written: {pdf_path}")

    page_count = get_page_count(pdf_path)
    if page_count is not None:
        print(f"[OK] Page count: {page_count}")

    if args.preview:
        preview_path = Path(args.preview).resolve()
        try:
            render_preview(pdf_path, preview_path)
            print(f"[OK] Preview written: {preview_path}")
        except Exception as exc:
            print(f"[WARN] Preview not generated: {exc}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
