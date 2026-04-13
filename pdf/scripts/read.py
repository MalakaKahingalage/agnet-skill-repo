#!/usr/bin/env python3
"""
PDF extraction CLI for AI agent skills.

Usage:
  python3 read.py <path> check
  python3 read.py <path> full [max_chars]
  python3 read.py <path> pages <start> <end>
  python3 read.py <path> keyword <term>
  python3 read.py <path> summary

Modes:
  check    Validate the file (pages, encrypted, readable)
  full     Extract all text — use for small PDFs (<10 pages)
  pages    Extract a page range (1-indexed, inclusive)
  keyword  Return only pages containing the keyword
  summary  Page 1 + every 5th page — first pass on unknown docs
"""
import sys, re

def clean(text):
    text = re.sub(r'\n{3,}', '\n\n', text)
    text = re.sub(r'[ \t]+', ' ', text)
    return text.strip()

def open_doc(path):
    try:
        import fitz
    except ImportError:
        print('ERROR: pymupdf not installed — run: pip install pymupdf')
        sys.exit(1)
    try:
        doc = fitz.open(path)
    except Exception as e:
        print(f'ERROR: {e}')
        sys.exit(1)
    if doc.is_encrypted:
        print('ERROR: PDF is password-protected — cannot extract text without password')
        sys.exit(1)
    return doc

def mode_check(path):
    try:
        import fitz
        doc = fitz.open(path)
        encrypted = doc.is_encrypted
        pages = len(doc)
        if encrypted:
            print(f'ERROR: PDF is password-protected ({pages} pages)')
            sys.exit(1)
        # Quick readability check — sample first page
        sample = doc[0].get_text().strip() if pages > 0 else ''
        if not sample:
            print(f'WARNING: {pages} pages — page 1 returned no text (may be scanned/image PDF)')
        else:
            print(f'OK: {pages} pages — text readable')
    except Exception as e:
        print(f'ERROR: {e}')
        sys.exit(1)

def mode_full(doc, path, max_chars=0):
    print(f'[PDF: {len(doc)} pages — {path}]')
    chunks = []
    for i in range(len(doc)):
        text = clean(doc[i].get_text())
        if text:
            chunks.append(f'--- Page {i+1} ---\n{text}')
    output = '\n\n'.join(chunks)
    if max_chars and len(output) > max_chars:
        print(output[:max_chars])
        print(f'\n[TRUNCATED — {len(output)} total chars, showing first {max_chars}]')
    else:
        print(output)

def mode_pages(doc, start, end):
    total = len(doc)
    start = max(1, start)
    end   = min(end, total)
    print(f'[PDF: {total} total pages — reading pages {start}–{end}]')
    for i in range(start - 1, end):
        text = clean(doc[i].get_text())
        if text:
            print(f'--- Page {i+1} ---')
            print(text)

def mode_keyword(doc, keyword):
    matches = []
    for i in range(len(doc)):
        text = doc[i].get_text()
        if keyword.lower() in text.lower():
            matches.append(f'--- Page {i+1} [MATCH] ---\n{clean(text)}')
    if matches:
        print(f'[Found "{keyword}" on {len(matches)} page(s)]')
        print('\n\n'.join(matches))
    else:
        print(f'[No pages found containing "{keyword}"]')

def mode_summary(doc, path):
    total = len(doc)
    sample_pages = sorted(set([0] + list(range(0, total, 5))))
    print(f'[PDF Summary — {path}]')
    print(f'[{total} pages total — sampling {len(sample_pages)} pages: {[p+1 for p in sample_pages]}]')
    for i in sample_pages:
        text = clean(doc[i].get_text())
        if text:
            preview = text[:500] + ('...' if len(text) > 500 else '')
            print(f'\n--- Page {i+1} ---\n{preview}')

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)

    path = sys.argv[1]
    mode = sys.argv[2].lower()

    if mode == 'check':
        mode_check(path)
        sys.exit(0)

    doc = open_doc(path)

    if mode == 'full':
        max_chars = int(sys.argv[3]) if len(sys.argv) > 3 else 0
        mode_full(doc, path, max_chars)

    elif mode == 'pages':
        if len(sys.argv) < 5:
            print('Usage: read.py <path> pages <start> <end>')
            sys.exit(1)
        mode_pages(doc, int(sys.argv[3]), int(sys.argv[4]))

    elif mode == 'keyword':
        if len(sys.argv) < 4:
            print('Usage: read.py <path> keyword <term>')
            sys.exit(1)
        mode_keyword(doc, sys.argv[3])

    elif mode == 'summary':
        mode_summary(doc, path)

    else:
        print(f'ERROR: Unknown mode "{mode}". Use: check, full, pages, keyword, summary')
        sys.exit(1)
