---
name: agent-trust-hardening
description: Audit and raise the trust line for autonomous AI agents. Use when hardening agent execution, defining approval gates, restricting subagent tool scopes, enforcing artifact verification, establishing atomic rollbacks, and pruning startup context tax.
version: 2.0.0
tags: [agent, hardening, trust, safety, approval-gates, rollbacks, tool-walls, auditing]
---

# Agent Trust Hardening

Use this skill to raise the **trust line** of an AI agent setup, enabling more work to execute autonomously, reliably, and safely without human supervision.

## Core Principle

An agent's enterprise value is constrained by the weakest link among:
1. **Capability**: How much work it can perform
2. **Trust**: How reliably it executes without errors
3. **Autonomy**: How much execution can occur without human intervention

**Goal**: Move the trust line up so routine tasks run unattended, high-risk tasks pause at explicit approval gates, and failures trigger automated rollbacks rather than silent corruption.

---

## 1. Verification over Verbal Claims (Artifact-First Rule)

Never declare success based on LLM text output alone.

- **Bad**: Agent outputs: *"The service was restarted successfully and the logs look clear."*
- **Good**: Agent inspects process exit status (`$? == 0`), queries systemd status (`active (running)`), checks the HTTP health endpoint (`curl -sf http://host/health`), and verifies exact log tracebacks.

### Rules of Verification:
1. **Artifact Inspection**: Verify generated files, build binaries, or DB entries on disk before completing a task.
2. **Non-Silent Failures**: Treat 0-byte files, empty JSON responses, missing logs, or empty arrays as **hard failures**, not successes.
3. **Deterministic Execution First**: For complex multi-step data transformations or system operations, execute **deterministic Python/Bash helper scripts** inside `scripts/` rather than relying on prompt-based manual LLM execution steps.

---

## 2. Explicit Approval Gates & Boundaries

Define explicit boundaries between unattended operations and interactive human approvals.

| Operating Mode | Risk Level | Actions Allowed | Human Approval Required? |
| :--- | :--- | :--- | :--- |
| **Unattended** | Low | Read operations, local test runs, log analysis, temporary file drafting, status checks | ❌ No |
| **Monitored** | Medium | Non-production code changes, stashing, local git commits, container restarts | ❌ No (Log notify) |
| **Gated** | High | Production deployments, database schema migrations, remote host reboots, public API calls, destructive deletes | ✅ YES |

### Standardized Human Approval Payload Schema
When an agent hits a Gated action, it MUST pause and emit a standardized approval payload:

```json
{
  "approval_request": {
    "action_type": "MUTATION_REMOTE_SERVER_REBOOT",
    "target": "10.10.40.22 (srv-app-01)",
    "impact_summary": "Rebooting application server node. Service will be unavailable for ~60s.",
    "prerequisites_verified": true,
    "rollback_plan": "IPMI / Out-of-band power cycle via mgmt-01 if host fails to ping after 180s.",
    "prompt_question": "Do you approve rebooting 10.10.40.22 now? (Y/N)"
  }
}
```

---

## 3. Atomic State Checkpoints & Rollback Protocol

Before executing any mutating or gated action:

1. **Create Checkpoint**: Take a git stash, file copy (`.bak`), database dump, or config snapshot before altering system state.
2. **Execute Mutating Action**.
3. **Verify Result**: Run artifact verification checks.
4. **Rollback on Failure**: If verification fails or is aborted:
   ```bash
   # Restore from checkpoint automatically
   git checkout -- . || cp -f config.yaml.bak config.yaml
   ```

---

## 4. Subagent Tool-Wall Permission Matrix

Prevent accidental side-effects by restricting child subagent toolsets ("tool walls") rather than relying on prompt instructions alone:

| Subagent Role | Enabled Toolsets / Tools | Prohibited Actions |
| :--- | :--- | :--- |
| **Triage Agent** | `[read_file, grep_search, find_by_name]` | No file writing, no command execution |
| **Research Agent** | `[read_url_content, search_web]` | No local filesystem mutation, no terminal access |
| **Drafting Agent** | `[write_to_file, replace_file_content]` | No command execution, no network calls |
| **Executor Agent** | `[run_command]` (Scoped to explicit CWD) | Restricted target paths, no global daemon stops |

---

## 5. Bounded Self-Healing Loop

When artifact verification fails during a task:
1. Capture exact traceback / stderr log lines.
2. Diagnose root cause systematically.
3. Apply targeted fix.
4. Re-verify artifact.
5. **Retry Bound**: Limit self-healing attempts to **maximum 2 retries**. If the 2nd retry fails, elevate to human operator with diagnostic log.

---

## 6. Prune Startup Context Tax

Every enabled skill costs system prompt context tokens before work begins.

### 30-Second Audit Checklist:
- [ ] List all currently enabled skills across directories.
- [ ] Identify skills unused in the last 30 days.
- [ ] Keep daily-active core skills enabled; disable niche skills by default and load them progressively on demand.

---

## 7. Reusable Trust Audit Prompt

Use this prompt to audit any agent setup:

> Audit my AI agent setup for trust-line weaknesses. Check for: (1) actions that claim success without verifying real artifacts or exit codes, (2) multi-step operations using prose instead of deterministic helper scripts, (3) missing prerequisite checks or unhandled empty outputs, (4) gated/high-risk actions lacking explicit approval payloads, (5) mutating actions without atomic rollback checkpoints, and (6) subagents given broader tool access than their specific role requires. Return actionable, prioritized recommendations.
