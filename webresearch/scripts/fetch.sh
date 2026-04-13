#!/usr/bin/env bash
# fetch.sh — Human Chrome curl wrapper for web research
# Usage: bash fetch.sh "<URL>" [max_chars]
# Env:   RESEARCH_PROXY — optional HTTP proxy (e.g. http://proxy:8080)
#        RESEARCH_UA    — optional User-Agent override

URL="$1"
MAX_CHARS="${2:-0}"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

UA="${RESEARCH_UA:-Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36}"

PROXY_ARG=""
[ -n "$RESEARCH_PROXY" ] && PROXY_ARG="--proxy $RESEARCH_PROXY"

curl -s $PROXY_ARG \
     --compressed --http2 \
     --max-time 30 --location \
     -c /tmp/research_cookies -b /tmp/research_cookies \
     -H "User-Agent: $UA" \
     -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8" \
     -H "Accept-Language: en-AU,en;q=0.9" \
     -H "Accept-Encoding: gzip, deflate, br" \
     -H "Sec-CH-UA: \"Chromium\";v=\"124\", \"Google Chrome\";v=\"124\", \"Not-A.Brand\";v=\"99\"" \
     -H "Sec-CH-UA-Mobile: ?0" \
     -H "Sec-CH-UA-Platform: \"Windows\"" \
     -H "Sec-Fetch-Dest: document" \
     -H "Sec-Fetch-Mode: navigate" \
     -H "Sec-Fetch-Site: none" \
     -H "Sec-Fetch-User: ?1" \
     -H "Upgrade-Insecure-Requests: 1" \
     -H "Cache-Control: max-age=0" \
     "$URL" | python3 "$SCRIPT_DIR/extract.py" "$MAX_CHARS"
