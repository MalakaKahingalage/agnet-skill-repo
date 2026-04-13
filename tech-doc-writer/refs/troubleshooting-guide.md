# Troubleshooting & Recovery Guide — Document Guide

**Purpose:** Step-by-step diagnosis and recovery procedures for when a platform is down, degraded, or needs full rebuild.
**Audience:** Operations engineers, on-call responders, anyone recovering the system at 2am.
**Tone:** Procedural. Start with "what you see" → work to "what you do". No theory. Every step must be actionable.

---

## Source References (load sections as needed — do not load both at once)

**Operational procedures and known issues:**
```
/mnt/c/Users/malaka.kahingalage/OneDrive - Rio Tinto/Second_Brain/RioTinto/20_Projects/2026/OT_AgenticOps/NetAssist_Platform_AsBuilt_auperzap207.md
```
Load: offset=1547, limit=80 (incident response + service management)
Load: offset=1684, limit=200 (backup & recovery + DR procedure)
Load: offset=1814, limit=200 (health checks + troubleshooting section 7.5)

---

## Required Sections (in order)

### 1. Document Purpose & Quick Reference

**Open with a 60-second triage block — the first thing a responder reads:**

```
PLATFORM:     {Name} on {hostname}
ACCOUNT:      {sa-account-name}   (ALL ops must run as this account)
BASE PATH:    /opt/apps/containers/
ON-CALL:      {Name} — {contact}
TICKET:       {ServiceNow / JIRA link}
RTO:          {e.g. 4 hours}
RPO:          {e.g. 24 hours}
```

### 2. Platform Health Check Runbook

**Run this first — before doing anything else.**

#### 2.1 Full Health Check (copy-paste ready)
```bash
# Switch to service account
sudo su - {sa-account-name}

# 1. Container status
podman ps -a --format "table {{.Names}}\t{{.Status}}\t{{.Health}}"

# 2. Resource check
df -h /opt && free -h && podman stats --no-stream

# 3. API health checks
curl -s http://localhost:{litellm-port}/health
curl -s http://localhost:{qdrant-port}/health
curl -s -o /dev/null -w "WebUI HTTP: %{http_code}\n" http://localhost:{webui-port}

# 4. Database check
podman exec {postgres-container} pg_isready -U {db-admin-user}

# 5. Network check
podman network ls | grep {network-name}
```

#### 2.2 Health Check Interpretation Table
| What you see | Meaning | Jump to |
|---|---|---|
| All containers "Up X days" | Platform healthy | No action |
| One container "Exited" | Single service failure | Section 4 |
| Multiple containers "Exited" | Cascade failure / startup order issue | Section 5 |
| No containers listed at all | Full platform down | Section 6 |
| Containers "Up" but API failing | Internal service error | Section 4 |
| /opt disk >90% | Storage critical | Section 3.5 |
| Server unreachable via SSH | Infrastructure/host issue | Section 7 |

### 3. Common Issues — Symptom → Fix

One sub-section per symptom. Each must follow this pattern:
- **Symptom:** What the user/engineer sees
- **Likely cause:** 1-3 sentences
- **Diagnosis commands:** exact bash
- **Fix commands:** exact bash
- **Verify fix:** how to confirm it worked

#### 3.1 Container Fails to Start
#### 3.2 "Permission denied" on Volume Mounts
#### 3.3 "No space left on device"
#### 3.4 Database Connection Refused
#### 3.5 MCP Service Shows Unhealthy
#### 3.6 WebUI Unreachable (HTTP 502/503/timeout)
#### 3.7 LiteLLM API Errors / Model Unavailable
#### 3.8 Qdrant Collections Empty or Missing
#### 3.9 SELinux Denial Blocking Service
#### 3.10 Network / Container DNS Failure

**Template for each issue:**
```markdown
#### 3.X {Issue Name}

**Symptom:** {What the user sees — e.g. "Open WebUI returns 502 Bad Gateway"}

**Likely cause:** {1-2 sentences}

**Diagnose:**
```bash
# commands to confirm root cause
```

**Fix:**
```bash
# commands to resolve
```

**Verify:**
```bash
# commands to confirm fixed
```
```

### 4. Single Service Recovery

**When one container is down while others are healthy.**

#### 4.1 Dependency Map (startup order)
Always start dependencies FIRST, application LAST.

```
Layer 1 (data):    postgres → qdrant
Layer 2 (gateway): litellm → nginx-proxy-manager
Layer 3 (platform): MCP services (all)
Layer 4 (apps):    openwebui → netAssist-L1 agents
```

#### 4.2 Restart a Single Service
```bash
cd /opt/apps/containers/{service-dir}
podman-compose down
podman-compose up -d
podman logs -f {container-name}   # watch for errors
```

#### 4.3 Force Rebuild (image pull + recreate)
```bash
cd /opt/apps/containers/{service-dir}
podman-compose down
podman pull {image:tag}
podman-compose up -d --force-recreate
```

### 5. Cascade Failure Recovery (Multiple Services Down)

**When multiple containers are down — usually a startup order or dependency problem.**

#### 5.1 Full Platform Restart (ordered)
```bash
sudo su - {sa-account-name}

# Stop everything first
cd /opt/apps/containers
for dir in netAssist-L1-netEngineer_general netAssist-L1-netEngineer openwebui MCP npm litellm qdrant postgres; do
  cd /opt/apps/containers/$dir && podman-compose down
done

# Start in dependency order
cd /opt/apps/containers/postgres && podman-compose up -d && sleep 10
cd /opt/apps/containers/qdrant && podman-compose up -d && sleep 5
cd /opt/apps/containers/litellm && podman-compose up -d && sleep 5
cd /opt/apps/containers/npm && podman-compose up -d && sleep 5
cd /opt/apps/containers/MCP && podman-compose up -d && sleep 10
cd /opt/apps/containers/openwebui && podman-compose up -d && sleep 5
cd /opt/apps/containers/netAssist-L1-netEngineer && podman-compose up -d
cd /opt/apps/containers/netAssist-L1-netEngineer_general && podman-compose up -d

# Verify all up
podman ps -a
```

#### 5.2 Post-Restart Verification Checklist
- [ ] All containers show "Up" status
- [ ] No containers in "Restarting" loop
- [ ] LiteLLM `/health` returns OK
- [ ] Qdrant `/health` returns OK
- [ ] WebUI loads in browser
- [ ] Test agent query end-to-end

### 6. Full Disaster Recovery (Server Loss / Complete Rebuild)

**When the server is gone, corrupted, or needs full rebuild from scratch.**

**Estimated time:** {RTO — e.g. 4 hours}  
**Required:** Backup tarball + DB dump + Qdrant snapshots

#### 6.1 Pre-Rebuild Checklist
- [ ] New server provisioned: RHEL 9, {RAM}GB RAM, {size}GB /opt partition
- [ ] Server accessible via SSH from jump host
- [ ] Backup files accessible (from: {backup location})
- [ ] Artifactory/image registry credentials available
- [ ] Firewall rules applied to new server IP

#### 6.2 Step-by-Step Rebuild

**Step 1 — Prepare server**
```bash
# Install container runtime
sudo dnf install -y podman podman-compose

# Create service account
sudo useradd -m -s /bin/bash {sa-account-name}
sudo usermod -aG wheel {sa-account-name}   # if sudo needed
```

**Step 2 — Restore configuration files**
```bash
sudo su - {sa-account-name}
mkdir -p /opt/apps/containers

# Extract backup tarball
tar -xzf /path/to/configs-backup.tar.gz -C /opt/apps/containers/

# Restore storage and registry config
mkdir -p ~/.config/containers/
cp /path/from/backup/storage.conf ~/.config/containers/
cp /path/from/backup/registries.conf ~/.config/containers/
```

**Step 3 — Pull container images**
```bash
# Authenticate to registry
podman login {registry-url} -u {username}

# Pull all required images (from compose files)
for dir in /opt/apps/containers/*/; do
  cd "$dir" && podman-compose pull
done
```

**Step 4 — Start database layer and restore data**
```bash
cd /opt/apps/containers/postgres && podman-compose up -d
sleep 15   # wait for postgres to initialise

# Restore PostgreSQL from backup
cat /path/to/full_backup_{date}.sql | podman exec -i {postgres-container} psql -U {db-admin-user} -d postgres
```

**Step 5 — Restore Qdrant vector data**
```bash
cd /opt/apps/containers/qdrant && podman-compose up -d
sleep 10

SNAPSHOT_DIR="/path/to/qdrant/snapshots"
QDRANT_HOST="localhost:{qdrant-port}"

for snapshot_file in "$SNAPSHOT_DIR"/*.snapshot; do
    collection_name=$(basename "$snapshot_file" | sed -E 's/-[0-9].*//')
    curl -s -X POST -F "snapshot=@$snapshot_file" \
        "http://$QDRANT_HOST/collections/$collection_name/snapshots/upload?priority=snapshot"
    echo "Restored: $collection_name"
done
```

**Step 6 — Start remaining services (dependency order)**
```bash
cd /opt/apps/containers/litellm && podman-compose up -d && sleep 5
cd /opt/apps/containers/npm && podman-compose up -d && sleep 5
cd /opt/apps/containers/MCP && podman-compose up -d && sleep 10
cd /opt/apps/containers/openwebui && podman-compose up -d && sleep 5
cd /opt/apps/containers/netAssist-L1-netEngineer && podman-compose up -d
cd /opt/apps/containers/netAssist-L1-netEngineer_general && podman-compose up -d
```

**Step 7 — Post-recovery verification**
```bash
podman ps -a
curl -s http://localhost:{litellm-port}/health
curl -s http://localhost:{qdrant-port}/health
curl -s -o /dev/null -w "WebUI: %{http_code}\n" http://localhost:{webui-port}
podman exec {postgres-container} psql -U {db-admin-user} -d postgres -c "\l"
```

#### 6.3 Post-Recovery Checklist
- [ ] All containers running and healthy
- [ ] All databases present and accessible
- [ ] Qdrant collections restored (check collection count and vector count)
- [ ] End-to-end agent query test passed
- [ ] DNS / load balancer updated to new server IP
- [ ] Firewall rules applied and verified
- [ ] Monitoring/alerting re-pointed to new server
- [ ] Backup schedule re-established on new server
- [ ] Incident ticket updated with recovery timestamp

### 7. Infrastructure / Host-Level Issues

**When the server itself is unreachable or unhealthy.**

- 7.1 Cannot SSH to server — check VM/hypervisor console, check network path, check firewall
- 7.2 Server hung / unresponsive — reboot via hypervisor, check boot logs via console
- 7.3 Disk full at OS level — emergency cleanup, log rotation, extend volume
- 7.4 Rootless Podman socket missing — check `systemctl --user status podman.socket` as service account
- 7.5 SELinux blocking all operations — check `ausearch -m avc -ts recent`, apply policies or set permissive temporarily

### 8. Log Reference (where to look for what)

| Symptom | Log location | Command |
|---|---|---|
| Container crash | Container stdout/stderr | `podman logs {name}` |
| Permission error | SELinux audit log | `sudo ausearch -m avc -ts recent` |
| SSH failure | Auth log | `sudo grep sshd /var/log/secure | tail -50` |
| Podman runtime error | Systemd journal | `journalctl _UID={uid} --since "1h ago"` |
| PostgreSQL error | Postgres container log | `podman logs postgres-db | tail -100` |
| Network issue | Podman network inspect | `podman network inspect {network-name}` |
| Disk full | df / du | `df -h /opt && du -sh /opt/apps/containers/*/` |

### 9. Escalation & Contacts

Table: Role | Name | Contact | Hours | Escalate when…

---

## Troubleshooting Guide Checklist

- [ ] All commands tested on actual platform before publishing
- [ ] Placeholders replaced with real values (ports, container names, paths)
- [ ] Startup dependency order verified and correct
- [ ] DR procedure tested (at least in dev/lab)
- [ ] RTO / RPO values agreed with service owner
- [ ] Escalation contacts current
- [ ] Document stored where it is accessible even when platform is DOWN (not just on the platform itself)
- [ ] Printed or offline copy available for OT environments
