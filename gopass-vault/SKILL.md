---
name: gopass-vault
description: Manage secrets in Malaka's gopass vault — store, retrieve, add new keys, and sync to GitHub. Source of truth for all API keys, tokens, and credentials.
version: 1.0.0
tags: [secrets, gopass, gpg, credentials, api-keys]
---

# gopass Vault — Secret Management Skill

Encrypted secret management using `gopass`, backed by GPG and git-synced to a private GitHub repository.

## Key Facts

- **Binary:** `~/.local/bin/gopass`
- **Store path:** `~/.local/share/gopass/stores/root`
- **GitHub repo:** `github.com/MalakaKahingalage/alfred-vault` (private)
- **GPG Key:** `70F5847BA1E89C3E` (Malaka Kahingalage)

## Secret Naming Conventions

```
api/        Third-party API keys (OpenRouter, OpenAI, Anthropic)
github/     GitHub PATs and SSH keys
telegram/   Telegram bot credentials and pairing configs
email/      Email credentials and SMTP settings
infra/      Infrastructure secrets (SSH keys, Home Assistant tokens, OAuth tokens)
home/       Household passwords (WiFi, router, Home Assistant)
```

## Workflows

### Inserting a Secret (Without Shell History Leaks)
```bash
printf '%s' "$TOKEN" | gopass insert -f -m infra/my-token
gopass sync
```

### Retrieving a Secret Password
```bash
gopass show --password api/openrouter
```

### Verification Without Leaking to Logs
```bash
python3 - <<'PY'
import subprocess
s = subprocess.check_output(['gopass', 'show', '--password', 'infra/homeassistant-api-token'], text=True).strip()
print('Length:', len(s))
print('Prefix:', s[:10])
PY
```
