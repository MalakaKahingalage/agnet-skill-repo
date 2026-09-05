# Herdr Multi-Server Management Cheatsheet & Patterns

This reference provides specific CLI patterns and workflows for managing multiple Linux servers, microservices, and platforms using Herdr.

---

## 1. Remote Server Access Patterns

### A. Persistent SSH Session in Herdr Pane
To keep a server session alive across agent turns:
```bash
# Create dedicated pane for remote host
PANE_ID=$(herdr pane split --current --direction right --no-focus | jq -r '.result.pane.pane_id')

# Connect via SSH with KeepAlive options
herdr pane run "$PANE_ID" "ssh -o ServerAliveInterval=60 user@remote-host.domain.com"
```

### B. Executing Non-Interactive Remote Administration Tasks
```bash
# Execute remote command and wait for expected output
PANE_ID=$(herdr pane split --current --direction down --no-focus | jq -r '.result.pane.pane_id')
herdr pane run "$PANE_ID" "ssh user@remote-host 'sudo systemctl restart nginx && sudo systemctl status nginx'"
herdr pane wait-output "$PANE_ID" --match "active (running)" --timeout 30000
herdr pane read "$PANE_ID" --source recent-unwrapped
```

---

## 2. Multi-Server Log Tailing & Monitoring

### Tailing Multiple Server Logs Simultaneously
When debugging issues across multiple nodes (e.g. load balancer + 2 app servers):

1. Create a workspace tab for the incident/monitoring session:
   ```bash
   TAB_ID=$(herdr tab create --name "incident-logs" --workspace "$HERDR_WORKSPACE_ID" | jq -r '.result.tab.tab_id')
   ```

2. Split into 3 panes for 3 servers:
   ```bash
   # Pane 1 (LB)
   PANE_LB=$(herdr pane list --workspace "$HERDR_WORKSPACE_ID" | jq -r '.result.panes[0].pane_id')
   herdr pane run "$PANE_LB" "ssh lb-01 'tail -f /var/log/nginx/access.log'"

   # Pane 2 (App 1)
   PANE_APP1=$(herdr pane split --pane "$PANE_LB" --direction right --no-focus | jq -r '.result.pane.pane_id')
   herdr pane run "$PANE_APP1" "ssh app-01 'journalctl -u my-app -f'"

   # Pane 3 (App 2)
   PANE_APP2=$(herdr pane split --pane "$PANE_APP1" --direction down --no-focus | jq -r '.result.pane.pane_id')
   herdr pane run "$PANE_APP2" "ssh app-02 'journalctl -u my-app -f'"
   ```

3. Read output from any specific server pane whenever needed:
   ```bash
   herdr pane read "$PANE_APP1" --source recent-unwrapped --lines 50
   ```

---

## 3. Deployment & Process Rollout Verification Pattern

When deploying software across remote nodes:

```bash
# 1. Run deployment command on remote host
herdr pane run "$PANE_ID" "ssh deployer@app-01 'cd /opt/app && git pull && systemctl restart app'"

# 2. Wait for deployment completion signal
herdr pane wait-output "$PANE_ID" --match "SUCCESS" --timeout 120000

# 3. Health check response
herdr pane run "$PANE_ID" "curl -sf http://app-01:8080/health || echo 'HEALTH_CHECK_FAILED'"
herdr pane wait-output "$PANE_ID" --regex "(200 OK|HEALTH_CHECK_FAILED)" --timeout 10000
```
