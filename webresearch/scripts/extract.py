#!/usr/bin/env python3
"""
Smart HTML extraction pipeline for web research.
Reads HTML from stdin, outputs clean text to stdout.
Usage: curl ... "<URL>" | python3 extract.py [max_chars]
"""
import sys, html as hl, re

raw = sys.stdin.read()
max_chars = int(sys.argv[1]) if len(sys.argv) > 1 else 0  # 0 = no limit

# ── TIER 1: Known vendor block markers ─────────────────────────────────────
BLOCKS_T1 = [
    (r'cf-error-code|challenge-form|__cf_chl_f_tk', 'Cloudflare'),
    (r'Reference #\d+\.\d+\.\d+',                  'Akamai'),
    (r'_pxAppId|pxchallenge|__px',                  'PerimeterX'),
    (r'captcha-delivery\.com',                       'DataDome'),
    (r'_Incapsula_Resource|incapsula\.com',          'Imperva'),
    (r'kasada\.io|kpsdk\.js',                        'Kasada'),
    (r'sucuri\.net/cloudproxy',                      'Sucuri'),
]
for pat, vendor in BLOCKS_T1:
    if re.search(pat, raw, re.I):
        print(f'BLOCKED [{vendor}] — switch search engine or use different URL')
        sys.exit(1)

# ── TIER 2: Generic block terms on short pages ─────────────────────────────
if len(raw) < 10000:
    for term in ['Access Denied', 'Just a moment', 'Checking your browser',
                 'You have been blocked', 'DDoS protection', 'automated request',
                 'PoW Captcha', 'bots use DuckDuckGo']:
        if term in raw:
            print(f'BLOCKED [generic: "{term}"] ({len(raw)} bytes) — switch fallback engine')
            sys.exit(1)

# ── TIER 3: Structural integrity ────────────────────────────────────────────
body_m = re.search(r'<body[^>]*>(.*?)</body>', raw, re.DOTALL|re.I)
if not body_m:
    print(f'WARNING: no body tag ({len(raw)} bytes) — likely bot-screen response')
    sys.exit(1)
if len(re.sub(r'<[^>]+>', '', body_m.group(1)).strip()) < 50:
    print('WARNING: near-empty page — likely block page')
    sys.exit(1)

# ── NOISE REMOVAL ───────────────────────────────────────────────────────────
noise_tags = r'nav|footer|header|aside|form|iframe|noscript|script|style'
content = re.sub(rf'<({noise_tags})[^>]*>.*?</\1>', '', raw, flags=re.DOTALL|re.I)
content = re.sub(
    r'<[^>]+(class|id)=["\'][^"\']*'
    r'(nav|footer|header|sidebar|advert|ads?|social|share|comment|'
    r'promo|cookie|banner|popup|modal|overlay|newsletter)[^"\']*["\'][^>]*>',
    '', content, flags=re.I)

# ── LINK CITATION EXTRACTION ────────────────────────────────────────────────
links = re.findall(r'<a[^>]+href=["\'](https?://[^"\'#][^"\']*)["\'][^>]*>(.*?)</a>', content, re.I|re.DOTALL)
seen, citations = {}, []
for url, title in links:
    url = url.strip()
    if url not in seen and len(url) < 200:
        seen[url] = len(seen) + 1
        t = re.sub(r'<[^>]+>', '', title).strip()[:80]
        citations.append(f'[{seen[url]}] {url}' + (f' — "{t}"' if t else ''))

# ── TEXT EXTRACTION ─────────────────────────────────────────────────────────
content = re.sub(r'<[^>]+>', ' ', content)
content = hl.unescape(content)
content = re.sub(r'\s+', ' ', content).strip()

output = content[:max_chars] if max_chars else content
print(output)
if max_chars and len(content) > max_chars:
    print(f'\n[TRUNCATED — {len(content)} total chars, showing first {max_chars}]')

if citations:
    print('\n--- Page Links ---')
    print('\n'.join(citations[:15]))
