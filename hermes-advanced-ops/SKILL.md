---
name: hermes-advanced-ops
description: Operations guide for Hermes agent execution, token auditing, cron job attribution, plugin hook limitations, and messaging access policies. Use when troubleshooting Hermes agent runs, auditing token spend, or managing Hermes gateway integrations.
version: 1.0.0
---

# Hermes Advanced Ops

This skill provides advanced operational guidelines for monitoring, auditing, and configuring Hermes AI Agent platforms.

---

## 1. Plugin Development & Hook Mechanics

Hermes plugins register hooks and custom slash commands inside `__init__.py`:

```python
def register(ctx) -> None:
    ctx.register_hook("pre_llm_call", _on_pre_llm_call)
    ctx.register_hook("post_tool_call", _on_post_tool_call)
    ctx.register_command("my-cmd", handler=_handle_slash, description="Custom command")
```

### Hook Limitations
- `pre_llm_call`: Can inject context messages, but cannot override the active LLM model via return values.
- `pre_api_request`: Return values are ignored (telemetry/logging only).
- `pre_tool_call`: Can block or intercept tool execution before it runs.

---

## 2. Token Spend & Usage Auditing

When auditing Hermes agent token spend:

- **Insights Formula**: `Total Tokens = Input Tokens + Output Tokens + Cache Read Tokens + Cache Write Tokens`.
- **Gotcha**: Cache reads often dominate recurring cron jobs. Summing only `input_tokens + output_tokens` will undercount actual model usage.

### Audit Command Sequence
```bash
# 1. Check overall 24-hour spend summary
hermes insights --days 1

# 2. Filter spend by background cron jobs
hermes insights --days 1 --source cron
```

---

## 3. Gateway Messaging & Access Policies

When managing Telegram or messaging gateway integrations:
- Setting `TELEGRAM_ALLOWED_USERS` causes Hermes to treat unauthorized DMs as restricted and silently ignore them by default.
- To enable pairing codes for new users when an allowlist exists, explicitly set:
  ```yaml
  telegram:
    unauthorized_dm_behavior: pair
  ```
- Restart the gateway service and approve user pairing codes via `hermes pairing approve telegram <CODE>`.
