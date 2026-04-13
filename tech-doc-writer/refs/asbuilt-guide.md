# As-Built Document Guide

**Purpose:** Document exactly what is deployed in production — the definitive record of a running system.
**Audience:** Engineers, security teams, operations, future administrators.
**Tone:** Factual, precise, no design intent — only what IS deployed.

---

## Source Reference (load first 120 lines for structure context)

```
/mnt/c/Users/malaka.kahingalage/OneDrive - Rio Tinto/Second_Brain/RioTinto/20_Projects/2026/OT_AgenticOps/NetAssist_Platform_AsBuilt_auperzap207.md
```

---

## Required Sections (in order)

### 1. Executive Summary
- 1.1 Project Overview — what the platform does, key capabilities
- 1.2 System Scope — server, IP, OS, deployment model, service account
- 1.3 Deployed Components — table: component | version | status | uptime | ports

### 2. Architecture Overview
- 2.1 Physical / VM Infrastructure — hardware specs, OS, storage layout
- 2.2 Network Topology — IP addresses, VLANs, firewall zones, access paths
- 2.3 Component Interaction Diagram (ASCII or description)
- 2.4 Port & Service Map table: Port | Protocol | Service | Source | Destination | Purpose

### 3. Infrastructure Details
- 3.1 Server Specification — CPU, RAM, disk, NIC, BIOS/firmware
- 3.2 Operating System — version, kernel, SELinux mode, FIPS status
- 3.3 Storage Layout — mount points, filesystem types, sizes, usage
- 3.4 Network Configuration — interfaces, IPs, routes, DNS

### 4. Container / Application Platform
- 4.1 Container runtime (Podman/Docker) — version, rootless config, runtime user
- 4.2 Compose/orchestration config — file paths, startup method
- 4.3 Image registry — source (Artifactory/Docker Hub/air-gap), pull policy
- 4.4 Volume mounts table: Container | Host Path | Mount Point | Purpose

### 5. Application Components
One sub-section per service/component:
- Service name + container name
- Image + version/tag
- Exposed ports
- Environment variables (no secrets — reference credential doc instead)
- Data persistence (volumes/bind mounts)
- Health check method
- Upstream/downstream dependencies

### 6. Security & Compliance
- 6.1 Access Control — service accounts, sudo rules, SSH key policy
- 6.2 Network Security — firewall rules, ACLs, inbound/outbound rules table
- 6.3 Data Security — encryption at rest, encryption in transit (TLS)
- 6.4 Secret Management — where credentials are stored (vault/env files), NOT the values
- 6.5 SELinux / AppArmor / auditd posture
- 6.6 Compliance notes (OT standards, CIS, NIST)

### 7. Operations & Maintenance
- 7.1 Service Management commands (start/stop/restart/status)
- 7.2 Log locations and log rotation
- 7.3 Backup procedures and schedules
- 7.4 Health check commands
- 7.5 Common troubleshooting steps

### 8. Deployment History
Table: Date | Change | Performed By | Reference | Outcome

### 9. Appendices
- A: Full port listing
- B: Service account details
- C: Environment variable reference (no values — reference credential doc)
- D: Related documents and links

---

## OT-Specific Requirements

- Always state the OT security zone (e.g. APAC-W OT Production Zone)
- Note air-gap status and any internet connectivity restrictions
- Include SCADA/OT integration points if applicable
- Service account must be explicitly named — never "root" in production OT

---

## As-Built Checklist

- [ ] All running containers documented with current versions
- [ ] All listening ports documented
- [ ] No credential values in this document (reference credentials doc)
- [ ] Firewall rules match what is actually deployed
- [ ] Volume mounts verified against live system
- [ ] Service account and permissions documented
- [ ] Document control version table updated
- [ ] Classification label correct
