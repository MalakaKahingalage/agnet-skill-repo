# Reference Document Guide

**Purpose:** Quick-access technical reference sheets — port tables, credential placeholders, config parameters, service URLs, IP lists.
**Audience:** Engineers working hands-on with the platform. Day-to-day operational reference.
**Tone:** Concise, tabular, scannable. No prose sections longer than 3 lines. Every fact has a table.

---

## Source Reference (load first 80 lines for structure context)

```
/mnt/c/Users/malaka.kahingalage/OneDrive - Rio Tinto/Second_Brain/RioTinto/20_Projects/2026/OT_AgenticOps/CREDENTIALS_REFERENCE_auperzap207.md
```

---

## Types of Reference Documents

Choose the appropriate sub-type based on content:

| Sub-type | When to use | Key sections |
|---|---|---|
| **Platform Reference** | Server/platform config summary | Infra, services, ports, URLs |
| **Credential Reference** | Credential inventory + rotation | Accounts, storage, rotation schedule |
| **Port Reference** | Firewall or network reference | All ports, protocols, sources, destinations |
| **Config Reference** | Environment variables, parameters | All configurable settings per component |

---

## Platform Reference — Required Sections

### 1. Platform Identity
```
Platform:       {Name}
Server:         {hostname.domain}
IP Address:     {x.x.x.x/mask}
Environment:    {Prod OT / Dev / Lab}
OS:             {RHEL 9.x / Ubuntu 22.x}
Service Account:{sa-account-name}
Last Updated:   {YYYY-MM-DD}
```

### 2. Service Inventory
Table: Service | Container Name | Image:Tag | Ports | Status | Data Volume | Notes

### 3. URL Reference
Table: Service | Internal URL | External URL (if any) | Auth Required | Notes

### 4. Port Reference
Table: Port | Protocol | Service | Direction | Source | Destination | Firewall Rule Ref

### 5. Environment Variables Reference (no values)
Table: Variable | Service | Purpose | Default | Override Required?

### 6. Key File Paths
Table: Description | Host Path | Notes

### 7. Management Commands Quick Reference
```bash
# Service status
podman ps -a

# Start all services
cd /opt/apps/containers && podman-compose up -d

# Stop all services
podman-compose down

# View logs for a service
podman logs -f {container-name}

# Restart single service
podman restart {container-name}
```

---

## Credential Reference — Required Sections

> ⚠️ **NEVER put actual credential values in this document.**
> Use `<PLACEHOLDER_NAME>` for all values. Actual credentials live in the encrypted vault.

### 1. Credential Inventory
Table: Credential ID | Service | Type | Username | Value | Storage Location | Owner | Rotation Period

**Value column must always contain** `[see vault]` or `<PLACEHOLDER_N>` — never actual values.

### 2. Database Credentials
Table: Database | Username | Role | Storage | Notes

### 3. API Keys & Tokens
Table: Service | Key Name | Scope | Storage | Rotation Period

### 4. Service Account Reference
Table: Account | Host | Purpose | Auth Method | SSH Key Location | sudo Access

### 5. Integration Credentials (external systems)
Table: System | Auth Type | Username/ClientID | Storage | Owner

### 6. Credential Rotation Schedule
Table: Credential | Service | Period | Last Rotated | Next Due | Owner | Rotation Method

### 7. Credential Retrieval Procedure
```bash
# Decrypt from vault (auperzap207)
gpg --decrypt ~/.credentials/{platform}-creds.gpg > /tmp/creds-$$.md

# View, then delete
less /tmp/creds-$$.md
shred -u /tmp/creds-$$.md
```

---

## Port Reference — Required Sections

### 1. All Listening Ports
Table: Port | Protocol | Service | Bind Address | Listening On | Firewall Status | Notes

### 2. Firewall Rules Summary
Table: Rule # | Direction | Source | Destination | Port(s) | Action | Review Date

### 3. Inter-Service Communication
Table: Source Service | Destination Service | Port | Protocol | Auth | Notes

---

## Config Reference — Required Sections

### 1. Environment Variables per Component
One table per component:

**{Component Name}**
| Variable | Current Value | Description | Sensitive? |
|---|---|---|---|
| `VAR_NAME` | `value` or `<PLACEHOLDER>` | What it controls | Yes/No |

### 2. Compose File Locations
Table: Service | Compose File Path | Config File Path | .env File Path

### 3. Configuration Change Procedure
1. Back up current config file
2. Make change in compose file or .env
3. Restart affected container: `podman restart {name}`
4. Verify health: `podman ps` and service health check
5. Update this reference document with the change

---

## Reference Document Checklist

- [ ] No actual credential values included — all are `<PLACEHOLDER>` or `[see vault]`
- [ ] All ports verified against live running system
- [ ] Service inventory matches current container list
- [ ] URLs tested and reachable
- [ ] Key file paths verified on server
- [ ] Rotation schedule has named owners and next-due dates
- [ ] Document classification set to 🔴 HIGHLY CONFIDENTIAL if it contains credential inventory
- [ ] Document version updated on every edit
