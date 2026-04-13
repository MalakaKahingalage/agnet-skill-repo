---
name: webresearch
description: "Research any topic on the internet. Fetches web pages, documentation, articles, and technical content via an optional HTTP proxy (set RESEARCH_PROXY env var). WHEN: research a topic, look up anything online, fetch documentation, APIs, news, technical references."
allowed-tools:
  - bash
  - read_bash
  - write_bash
---

## Autonomous Behaviour — CRITICAL

**When this skill is invoked, immediately start researching. Do NOT:**
- ❌ Ask the user for permission to search
- ❌ Ask "would you like me to look that up?"
- ❌ Ask which URLs to visit
- ❌ Ask for clarification before starting (unless the topic is completely ambiguous)
- ❌ Announce what you're about to do and wait for approval

**DO:**
- ✅ Start fetching and searching immediately on the first tool call
- ✅ Run multiple searches in parallel — stagger 1–2s apart to avoid bot detection
- ✅ Return findings directly — let the user redirect if needed
- ✅ If the topic is ambiguous, pick the most likely interpretation

**The rule:** If you have enough information to form a search query, just do it.

---

## Proxy

Optional. Set `RESEARCH_PROXY` to route all requests through an HTTP proxy:
```bash
export RESEARCH_PROXY="http://your-proxy:port"
```
Unset or empty = direct internet access.

---

## Fetching a URL

Use the `fetch.sh` script — handles all headers, proxy, and smart extraction automatically:

```bash
SKILL_DIR=$(find ~/.agents/skills ~/.github/skills ~/.config/opencode/skills ~/.claude/skills -name "fetch.sh" 2>/dev/null | head -1 | xargs dirname 2>/dev/null)
bash "$SKILL_DIR/scripts/fetch.sh" "https://example.com"
```

Or set `SKILL_DIR` explicitly if you know the path, then:
```bash
bash "$SKILL_DIR/scripts/fetch.sh" "<URL>"
```

The script outputs clean article text. Bot/CAPTCHA blocks are detected and reported automatically.

---

## Searching

### Brave Search (primary — max 2 per burst)
```bash
QUERY="your search terms here"
bash "$SKILL_DIR/scripts/fetch.sh" "https://search.brave.com/search?q=$(python3 -c "import urllib.parse,sys; print(urllib.parse.quote(sys.argv[1]))" "$QUERY")&source=web"
```

### DuckDuckGo (fallback)
```bash
bash "$SKILL_DIR/scripts/fetch.sh" "https://duckduckgo.com/html/?q=$(python3 -c "import urllib.parse,sys; print(urllib.parse.quote(sys.argv[1]))" "$QUERY")&kl=au-en"
```

### Mojeek (secondary fallback — no CAPTCHA)
```bash
bash "$SKILL_DIR/scripts/fetch.sh" "https://www.mojeek.com/search?q=$(python3 -c "import urllib.parse,sys; print(urllib.parse.quote(sys.argv[1]))" "$QUERY")"
```

### Stagger parallel searches (avoids bot detection)
```bash
bash "$SKILL_DIR/scripts/fetch.sh" "https://search.brave.com/search?q=query1" &
sleep 1
bash "$SKILL_DIR/scripts/fetch.sh" "https://duckduckgo.com/html/?q=query2&kl=au-en" &
wait
```

---

## Search Engine Strategy

| Engine | Use | Notes |
|---|---|---|
| **Brave** | Primary | Max 2 per burst — 3rd triggers PoW CAPTCHA |
| **DuckDuckGo** | Good fallback | Full Chrome headers required |
| **Mojeek** | Secondary fallback | No CAPTCHA, reliable |
| **Direct URL** | Preferred for known URLs | Fastest — bypasses search entirely |
| **Bing** | ⚠️ Avoid via proxy | May return wrong-language results based on proxy geolocation |
| **Google** | ❌ Avoid | CAPTCHA always triggers via curl |

---

## Bot Detection

`extract.py` automatically detects and reports blocks:
- **Tier 1:** Cloudflare, Akamai, PerimeterX, DataDome, Imperva, Kasada, Sucuri
- **Tier 2:** Generic block terms on short pages
- **Tier 3:** Structural checks (empty body, near-empty page)

On a `BLOCKED` response → switch to the next fallback engine.

---

## Workflow

1. **Known URL?** → `fetch.sh` directly, skip search
2. **Unknown topic?** → Brave search first, extract result URLs, then `fetch.sh` the best ones
3. **Brave blocked?** → Switch to DuckDuckGo, then Mojeek
4. **Multiple angles?** → Stagger parallel fetches 1–2s apart
