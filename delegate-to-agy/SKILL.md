---
name: delegate-to-agy
description: Delegate complex web research, multi-server infrastructure management via Herdr, or deep codebase refactoring tasks to Antigravity CLI (AGY). Use when Pi.dev or Hermes agents need to offload heavy web research, multi-host log tailing, or multi-pane Herdr orchestration to AGY.
version: 1.1.0
tags: [agy, antigravity, delegation, webresearch, herdr, multi-server, orchestration, async, timeouts]
---

# Delegate to Antigravity (AGY)

This skill provides Pi.dev, Hermes, and secondary agents with the exact procedure to delegate complex tasks directly to **AGY (Antigravity CLI)**.

AGY is specialized for:
1. **Deep Web Research**: Multi-source web scraping, live documentation lookup, market research, and technical fact-checking.
2. **Multi-Server Infrastructure Management**: Orchestrating remote Linux hosts, tailing multi-pane logs, and deploying services using **Herdr**.
3. **Complex Code Refactoring & Architecture**: End-to-end multi-file feature implementation and codebase analysis.

---

## 1. Prerequisites Check

Before delegating, verify that `agy` is available in the environment:

```bash
which agy || export PATH="$HOME/.local/bin:$PATH"
```

If `agy` is not installed on the host, install it via the official installer:
```bash
curl -fsSL https://antigravity.google/cli/install.sh | bash
```

---

## 2. Choosing Execution Mode: Synchronous vs. Async / Herdr Subagent

AGY autonomous runs perform deep multi-step reasoning, network requests, and code generation, which can take anywhere from **1 to 10 minutes**.

### Execution Mode Selection Matrix

| Task Type | Recommended Mode | Reasoning |
| :--- | :--- | :--- |
| **Quick lookups / Short summaries** (< 60s) | **Synchronous Direct CLI** | Fast, linear output returned directly to calling tool. |
| **Deep Web Research & Document Synthesis** (2-10 mins) | **Async Herdr Pane / Background** | Prevents calling agent shell timeout. |
| **Multi-Server & Herdr Orchestration** (3-15 mins) | **Async Herdr Pane** | Isolated terminal pane, real-time log inspection. |
| **Multi-File Refactoring & Verification** (3-10 mins) | **Async Herdr Pane / Background** | Long build & test cycles won't abort caller. |

---

## 3. Delegation Patterns

### Pattern A: Direct Synchronous CLI (For Fast Tasks)
When using direct synchronous CLI execution, **you MUST set a long tool timeout (minimum 600s / 10 mins)** in your tool call if supported by your runtime.

```bash
agy --dangerously-skip-permissions --prompt "Quick lookup: Fetch latest API endpoints for <SERVICE> and print summary to stdout"
```

### Pattern B: Herdr Subagent Pane Execution (Recommended for Long Tasks)
To prevent shell command timeouts, spawn AGY in a dedicated Herdr pane as an autonomous subagent. Instruct AGY to write a completion sentinel file (e.g. `COMPLETED.md` or output report).

```bash
# 1. Create a background Herdr pane without interrupting user focus
PANE_ID=$(herdr pane split --current --direction right --no-focus | jq -r '.result.pane.pane_id')

# 2. Launch AGY autonomously in the new pane with explicit output instructions
herdr pane run "$PANE_ID" "agy --dangerously-skip-permissions --prompt 'Perform comprehensive web research on <TOPIC>. Save final report to research_report.md and create DONE.md when finished.'"

# 3. Wait/poll for completion sentinel file or monitor output via Herdr
until [ -f "DONE.md" ]; do sleep 5; done
cat research_report.md
```

### Pattern C: Background Execution with Logging (No Herdr)
If Herdr is not active on the host, launch AGY in the background with `nohup`:

```bash
nohup agy --dangerously-skip-permissions --prompt "Refactor component <NAME> in src/ and create DONE.md when finished" > agy_task.log 2>&1 &
```

---

## 4. Best Practices for Delegation

1. **Self-Contained Prompts**: Provide AGY with full context, exact file paths, target server IPs, and explicit output requirements.
2. **Sentinel Completion Files**: Always ask AGY to create a `DONE.md` or target report file upon completion so calling agents can reliably detect when execution finishes.
3. **No Focus Interruption**: When spawning AGY in Herdr panes, always pass `--no-focus` to keep user context active.
4. **Timeout Guards**: Never execute AGY synchronously with standard 30s/60s command timeouts; always set timeout to 600s+ or use Herdr pane execution.
