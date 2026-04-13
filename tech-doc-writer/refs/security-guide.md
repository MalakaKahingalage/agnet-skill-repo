# Security Guide Document Guide

**Purpose:** Document security posture, controls, threat model, and operational security procedures for a platform.
**Audience:** Security leads, compliance teams, operations engineers, auditors.
**Tone:** Precise and unambiguous. Use explicit "MUST / SHOULD / MUST NOT" language for requirements.

---

## Source Reference (load for context only — do not reproduce actual credentials)

```
/mnt/c/Users/malaka.kahingalage/OneDrive - Rio Tinto/Second_Brain/RioTinto/20_Projects/2026/OT_AgenticOps/CREDENTIALS_SECURITY_GUIDE.md
```

---

## Required Sections (in order)

### 1. Document Purpose & Scope
- What system / platform this guide covers
- What is in scope and out of scope
- Who must follow this guide (mandatory vs. advisory)
- Classification of this document itself (usually 🔴 HIGHLY CONFIDENTIAL if it describes credential handling)

### 2. Security Posture Summary
Table: Control Area | Current State | Target State | Gap | Priority
- Access Control
- Network Security
- Data Protection
- Secret Management
- Audit & Monitoring
- Incident Response

### 3. Credential & Secret Management

#### 3.1 Credential Inventory
Table: Credential Name | Service | Type | Storage Location | Owner | Rotation Period

**IMPORTANT:** Never include actual credential values. Use `<PLACEHOLDER>` or `[see vault]` for values.

#### 3.2 Secret Storage Options (ranked by preference)
1. Enterprise Vault (CyberArk / HashiCorp) — preferred
2. GPG-encrypted file on controlled server
3. Encrypted USB in physical secure storage

#### 3.3 Encryption Standard
- Minimum: AES-256 symmetric encryption
- Key management: passphrase minimum 16 chars, stored separately from the file
- GPG command pattern:
```bash
gpg --symmetric --cipher-algo AES256 <filename>
```

#### 3.4 Access to Secrets
- Who can access (named individuals / roles)
- Decryption workflow (step-by-step)
- Auto-deletion of decrypted temporary files (15-minute timeout pattern)
- Audit logging requirement for all access

### 4. Access Control

#### 4.1 Service Accounts
Table: Account | Purpose | Host | Sudo Rights | SSH Access | Review Date

#### 4.2 Permissions Model
- Principle of least privilege
- No shared accounts
- No root login over SSH
- File permission standards (600 for secrets, 640 for configs, 644 for docs)

#### 4.3 MFA Requirements
- Which systems require MFA
- MFA method (TOTP / hardware token / AD-integrated)

### 5. Network Security Controls

#### 5.1 Firewall Rules
Table: Rule # | Source | Destination | Port | Protocol | Action | Purpose | Review Date

#### 5.2 Inbound Access Restrictions
- Allowed source IP ranges
- Denied sources (explicit deny-all default)
- VPN/jump server requirements

#### 5.3 Encryption in Transit
- TLS version minimum (TLS 1.2 minimum, TLS 1.3 preferred)
- Certificate management (self-signed vs. PKI)
- Internal API call encryption requirements

### 6. Audit & Monitoring

#### 6.1 Audit Log Sources
Table: System | Log Location | Retention | Alert Condition

#### 6.2 Key Events to Monitor
- Failed authentication attempts (>3 = alert)
- Credential file access (any access = log)
- Privilege escalation (any sudo = log)
- Container start/stop outside maintenance windows
- Network connections from unexpected sources

#### 6.3 Audit Commands
```bash
# Check recent login activity
sudo ausearch -m USER_LOGIN -ts recent

# Check credential file access
sudo ausearch -k credentials_access

# Check failed logins
sudo grep -i "failed" /var/log/secure | tail -50
```

### 7. Credential Rotation Schedule
Table: Credential | Service | Rotation Period | Last Rotated | Next Due | Owner | Method

### 8. Incident Response

#### 8.1 Credential Compromise Response (step-by-step)

**Immediate (within 1 hour):**
1. Notify security team — email/channel + incident ticket
2. Disable/revoke compromised credentials
3. Review audit logs for unauthorized access
4. Isolate affected service if needed

**Follow-up (within 24 hours):**
4. Rotate ALL credentials (not just compromised one)
5. File incident report in ServiceNow (Category: Security Incident)
6. Post-incident review within 5 business days

#### 8.2 Escalation Contacts
Table: Role | Name | Contact | Availability

### 9. Secure Development & Operations Checklist

**Before any deployment:**
- [ ] No credentials in source code or git repositories
- [ ] Credential files added to `.gitignore`
- [ ] Secrets use environment variables or vault references only
- [ ] Git history checked for accidental credential commits (`git log -p | grep -i password`)

**Quarterly audit:**
- [ ] All credentials still valid and rotated per schedule
- [ ] Access list reviewed — remove departed staff
- [ ] Audit logs reviewed for anomalies
- [ ] File permissions verified (no world-readable secret files)
- [ ] Encryption keys still valid
- [ ] Backup copy of encrypted credentials verified accessible

### 10. Backup & Recovery of Security Materials
- Primary: Enterprise Vault
- Secondary: Encrypted USB (physical secure storage)
- Sync after every credential rotation
- Recovery procedure tested annually

---

## Security Guide Checklist

- [ ] No actual credential values in this document
- [ ] All credential placeholders use `<PLACEHOLDER>` format
- [ ] Rotation schedule has named owners and dates
- [ ] Incident response procedure tested
- [ ] Emergency contacts current
- [ ] Document classification matches sensitivity
- [ ] `.gitignore` confirmed for all credential file patterns
