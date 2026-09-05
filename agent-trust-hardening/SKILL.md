---
name: agent-trust-hardening
description: Audit and raise the trust line for autonomous AI agents. Use when hardening agent execution, defining approval gates, restricting subagent tool scopes, verifying artifact outputs, and pruning startup context tax.
version: 1.0.0
---

# Agent Trust Hardening

Use this skill when the objective is to **raise the trust line** so more of the agent's work can run without supervision.

## Core Principle

Agent value is constrained by the weakest of:
1. How much work it can do
2. How much you trust it
3. How much can happen without human supervision

## 1. Verify Artifact Output over Verbal Claims

Never declare success based on model text output alone.

- **Bad**: Agent says "The deployment script ran successfully."
- **Good**: Agent inspects exit codes, checks HTTP endpoint health, and verifies system log traces.

### Silent Failure Prevention
Treat zero-byte outputs, missing logs, empty API arrays, or missing files as **hard failures**, not successes.

## 2. Explicit Approval Boundaries & Gates

Define clear boundaries between unattended operations and interactive human approvals.

- **Unattended / Low-risk**: Read operations, local test runs, temporary file drafting, log analysis.
- **Approval Gated / High-risk**: Remote server reboots, production database migrations, destructive file deletes, public API calls.

For each gated workflow:
- Document what can run without review.
- Document what must pause for approval.
- Provide clear context and rollback steps at pause time.

## 3. Restricted Subagents & Tool Walls

Enforce security by restricting subagent tool sets ("tool walls") rather than relying on prompt-only instructions:

- **Triage Subagent**: Read & search tools only.
- **Research Subagent**: Web & file read tools only.
- **Drafting Subagent**: File write tools only (no execution).
- **Executor Subagent**: Restricted execution tools only.

## 4. Context Tax Pruning

Audit active skills periodically to reduce token startup overhead:
1. Which skills are loaded by default?
2. What is their token cost in system prompts?
3. Disable niche or unused skills by default, enabling them progressively on demand.

## Quick Hardening Checklist

- [ ] Output verified from real artifact / system state
- [ ] Logic moved into deterministic scripts where appropriate
- [ ] Prerequisite checks executed before running operations
- [ ] Empty output / silent failure treated as failure
- [ ] Explicit approval gates defined for high-risk actions
- [ ] Rollback / checkpoint path available
- [ ] Subagent tool scopes restricted to minimum necessary
