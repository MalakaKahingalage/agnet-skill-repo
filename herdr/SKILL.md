---
name: herdr
description: >-
  Master guide and procedure for using Herdr (terminal workspace manager) to orchestrate local
  and remote Linux servers, platforms, processes, background agents, and multi-pane deployments.
  Use when managing remote Linux servers, running multi-pane server workloads, monitoring platform
  logs, spawning sub-processes/agents inside Herdr, or attaching to remote Herdr instances.
---

# Herdr Server & Terminal Workspace Management Skill

Herdr is a terminal workspace manager designed for AI coding agents and systems engineers. It organizes terminals into **workspaces**, **tabs**, and **panes**, tracks process/agent lifecycles, and exposes a CLI API to inspect and control local and remote server environments.

This skill equips Antigravity (AGY) to act as a primary agent managing Linux servers, platform services, and multi-pane infrastructure using Herdr.

---

## 1. Context & Environment Verification

Before executing control commands, verify if AGY is executing inside a Herdr-managed pane or targeting an external Herdr session:

```bash
# Check if running inside Herdr
test "${HERDR_ENV:-}" = 1 && echo "Inside Herdr context" || echo "External context"
```

- **Inside Herdr (`HERDR_ENV=1`)**: Use `--current` or direct pane/tab IDs relative to the current workspace.
- **Remote / Headless Server (`herdr --remote <ssh-target>`)**: Attach to or query remote Herdr daemons running on target Linux servers.

---

## 2. Server Infrastructure Topology Design

Structure your Herdr workspace according to the server/application management model:

| Hierarchy Level | Herdr Primitive | Server / Infrastructure Mapping Example |
| :--- | :--- | :--- |
| **Session** | Named Session (`herdr --session ops`) | Entire infrastructure environment (e.g., `prod-us-east`, `staging-k8s`). |
| **Workspace** | `workspace create --name <name>` | Project / Platform domain (e.g., `web-frontend`, `auth-service`, `db-cluster`). |
| **Tab** | `tab create --name <name>` | Specific host / server role (e.g., `app-node-01`, `postgres-primary`, `redis-cache`). |
| **Pane** | `pane split` | Terminal tasks on that host (e.g., SSH session, live log tailing, metric monitoring, background worker). |

---

## 3. Core Workflow Runbooks

### Runbook A: Setting Up Multi-Server Management Layout

1. **List existing workspaces and tabs**:
   ```bash
   herdr workspace list
   herdr tab list --workspace "$HERDR_WORKSPACE_ID"
   ```

2. **Create a new server management tab**:
   ```bash
   herdr tab create --name "srv-app-01" --workspace "$HERDR_WORKSPACE_ID"
   ```

3. **Split panes using smart geometry rules**:
   Inspect layout first:
   ```bash
   herdr pane layout --pane "$HERDR_PANE_ID"
   ```
   - **Wide viewport**: Split right (`--direction right`).
   - **Tall/Narrow viewport**: Split down (`--direction down`).
   - **Always preserve context**: Pass `--cwd "$PWD"` and `--no-focus` to keep user focus uninterrupted.

   ```bash
   # Split right for log monitoring
   herdr pane split --current --direction right --cwd "$PWD" --no-focus
   ```

### Runbook B: Managing Remote Linux Servers via SSH / Herdr Remote

#### Method 1: Direct SSH in Dedicated Herdr Panes
1. Create a pane for the target server:
   ```bash
   NEW_PANE=$(herdr pane split --current --direction right --no-focus | jq -r '.result.pane.pane_id')
   ```
2. Initiate persistent SSH connection:
   ```bash
   herdr pane run "$NEW_PANE" "ssh -t user@remote-server-ip 'htop || top'"
   ```
3. Run background server administration command in a secondary pane:
   ```bash
   CMD_PANE=$(herdr pane split --current --direction down --no-focus | jq -r '.result.pane.pane_id')
   herdr pane run "$CMD_PANE" "ssh user@remote-server-ip 'sudo systemctl status nginx'"
   ```

#### Method 2: Attaching to Remote Herdr Server Daemons
When target servers have `herdr` installed:
```bash
# Query or attach to remote Herdr server instance via SSH tunnel
herdr --remote user@remote-server-ip session list
```

### Runbook C: Non-Blocking Command Execution & Log Monitoring

When executing long-running builds, deployments, or remote commands:

1. **Dispatch the command to a target pane**:
   ```bash
   herdr pane run <target-pane-id> "docker-compose up -d && docker-compose logs -f"
   ```

2. **Wait for output patterns (non-blocking verification)**:
   ```bash
   herdr pane wait-output <target-pane-id> --match "Server started on port" --timeout 60000
   ```

3. **Read execution output cleanly**:
   ```bash
   # Use recent-unwrapped for clean multiline logs without artificial line wraps
   herdr pane read <target-pane-id> --source recent-unwrapped --lines 100
   ```

### Runbook D: Coordinating Secondary AI Agents in Herdr

When delegating server diagnosis or code fixes to a secondary agent running inside a Herdr pane:

1. **Verify agent kinds available**:
   ```bash
   herdr agent list
   ```

2. **Start agent in an interactive shell pane**:
   ```bash
   herdr agent start app-fixer --kind codex --pane <target-pane-id>
   ```

3. **Submit prompt and wait for completion**:
   ```bash
   herdr agent prompt app-fixer "Check system log at /var/log/syslog for memory errors and report." --wait --timeout 120000
   ```

4. **Handle agent states**:
   - `idle` / `done`: Task complete, ready for output extraction (`herdr agent read app-fixer`).
   - `blocked`: Agent requires user confirmation or input. Inspect UI via `herdr agent read app-fixer` and notify user.

---

## 4. Safety Guidelines & Rules of Engagement

1. **Focus Protection**: Always use `--no-focus` when spawning panes for background operations or remote servers to avoid disturbing the user's active viewport.
2. **Context Preservation**: Always preserve current working directory (`--cwd "$PWD"`) unless specifically instructed to open a different directory.
3. **Explicit Targeting**: Always use explicit target IDs (e.g., `--pane <pane_id>` or `--current`) rather than assuming default UI selection.
4. **Server Stop Safeguard**: **NEVER** execute `herdr server stop` unless explicitly ordered by the user, as it terminates the multiplexer and all attached process panes.
5. **Clean Log Extraction**: Use `--source recent-unwrapped` when reading logs to ensure tracebacks and long terminal lines are not truncated or wrapped artificially.
6. **Graceful Error Handling**: Parse JSON responses from `herdr` commands to verify status (`.status == "ok"`). If a process stalls, inspect the pane before retrying.

---

## 5. Quick Reference CLI Commands

```bash
# Discovery & Status
herdr status                       # Server/client status
herdr workspace list               # View all workspaces
herdr tab list --workspace <id>    # View tabs in workspace
herdr pane list --workspace <id>   # View panes in workspace

# Pane Operations
herdr pane split --current --direction right --no-focus  # Split pane horizontally
herdr pane split --current --direction down --no-focus   # Split pane vertically
herdr pane run <pane_id> "<cmd>"                         # Send command + Enter
herdr pane read <pane_id> --source recent-unwrapped      # Read output text
herdr pane wait-output <pane_id> --match "<string>"      # Wait for output match

# Agent Operations
herdr agent start <name> --kind <kind> --pane <pane_id>  # Start agent
herdr agent prompt <name> "<prompt>" --wait               # Send prompt and wait
herdr agent read <name> --lines 50                        # Read agent terminal output
```
