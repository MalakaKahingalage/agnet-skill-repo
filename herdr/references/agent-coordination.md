# Herdr Multi-Agent Orchestration & Coordination

Herdr allows AGY to spawn, prompt, monitor, and coordinate sub-agents inside dedicated terminal panes.

---

## 1. Lifecycle States of Herdr Agents

Agents managed by Herdr exhibit five primary lifecycle states:

- **`idle`**: Agent has finished work, tab has been seen in UI, and agent is ready for input.
- **`done`**: Agent completed work in background (unseen in UI focus). CLI can safely read results.
- **`working`**: Agent is currently processing a prompt or executing actions.
- **`blocked`**: Agent requires human approval, confirmation, or interactive decision.
- **`unknown`**: Agent present but status unclassified.

---

## 2. Agent Management Workflow

### Spawning an Agent
```bash
# 1. Prepare target pane
TARGET_PANE=$(herdr pane split --current --direction right --no-focus | jq -r '.result.pane.pane_id')

# 2. Start agent
herdr agent start db-auditor --kind codex --pane "$TARGET_PANE"
```

### Prompting with Non-Blocking Wait
```bash
# Prompt and wait for completion
herdr agent prompt db-auditor "Inspect postgresql.conf for optimal buffer settings." --wait --timeout 60000
```

### Handling Blocked / Approval States
If `herdr agent prompt` or `herdr agent wait` returns `agent_blocked`:
1. Read the current terminal lines to inspect what approval or question is requested:
   ```bash
   herdr agent read db-auditor --source recent-unwrapped --lines 30
   ```
2. Notify the user or ask for clarification before sending keypresses or approvals.
3. To send keypresses (such as Esc or Ctrl+C):
   ```bash
   herdr agent send-keys db-auditor esc
   ```
