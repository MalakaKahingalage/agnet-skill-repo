# LLD Document Guide

**Purpose:** Provide the detailed technical blueprint for building or deploying a system — the engineering specification engineers follow to construct what the HLD designed.
**Audience:** Network engineers, system/server administrators, deployment teams, project engineers.
**Tone:** Highly technical, prescriptive, exact. Specifies HOW to build with specific values, parameters, and config snippets. No strategic narrative — only engineering detail.

> **Relationship to other docs:**
> - HLD answers: **WHY** and **WHAT** (design intent, architecture)
> - LLD answers: **HOW** (exact parameters, configs, IPs, ports, protocols)
> - As-Built answers: **WHAT IS** (what is actually running in production)

---

## Source Reference (load first 150 lines for structure context if a source doc exists)

```
/mnt/c/Users/malaka.kahingalage/OneDrive - Rio Tinto/Second_Brain/RioTinto/20_Projects/2026/OT_AgenticOps/
```
Look for any existing HLD, design notes, or network diagrams in the project folder as source input.

---

## Required Sections (in order)

### 1. Executive Summary
- 1.1 Document Purpose — what this LLD covers, which HLD it implements
- 1.2 Scope & Boundaries — systems, devices, services, and locations covered; explicit out-of-scope
- 1.3 Related Documents — table: Document | Type | Version | Location

### 2. Design Overview
- 2.1 Solution Summary — brief description of what is being built (2–4 sentences max)
- 2.2 Architecture Diagram — ASCII diagram or component map showing all elements and their relationships
- 2.3 Component List — table: Component | Role | Technology | Hostname/IP | Environment | Version

### 3. Network Design (detailed)

#### 3.1 IP Addressing Table
Table: Device/Interface | Subnet | IP Address | Gateway | VLAN | Zone | Purpose

#### 3.2 VLAN Design
Table: VLAN ID | Name | Subnet | Purpose | Devices | Security Zone | Tagged Ports

#### 3.3 Interface Specifications
Table: Device | Interface | Description | IP/Mask | Speed/Duplex | Encapsulation | Connected To

#### 3.4 Routing Design
- Routing protocol (static / OSPF / BGP / EIGRP)
- Table: Route Prefix | Next-Hop | Interface | Protocol | Metric | Purpose
- Redistribution rules and route filtering if applicable

#### 3.5 DNS & DHCP Design
- DNS zones, forwarders, records required
- Table: Hostname | FQDN | IP | Record Type | Zone | Purpose
- DHCP scope, reservations, lease time

### 4. Device & Component Specifications

One sub-section per major device/component:

#### 4.x {Device/Component Name}
- **Role:** (e.g. Core Switch, Application Server, Firewall)
- **Hostname:** exact hostname
- **Hardware Model / VM Spec:** CPU, RAM, disk, NIC count
- **OS / Firmware:** version, build, patch level
- **Location:** rack/slot, data centre, OT zone
- **Management IP:** IP, access method (SSH/HTTPS), port
- **Key Configuration Parameters:** list specific values (e.g. MTU, NTP server, syslog target, SNMP community)

### 5. Protocol & Service Configuration Design

#### 5.1 Routing Protocol Parameters
Table: Protocol | Parameter | Value | Applied To | Notes
(e.g. OSPF Area, Hello/Dead timers, BGP ASN, timers, authentication)

#### 5.2 Switching Design
- STP mode (RSTP/MSTP), root bridge assignment
- Table: VLAN | Root Bridge | Secondary Bridge | Priority | Port Fast Ports

#### 5.3 QoS Design
- QoS policy intent, DSCP markings
- Table: Traffic Class | DSCP | Queue | Drop Policy | Interfaces Applied

#### 5.4 NTP Design
- NTP hierarchy, stratum levels
- Table: Device | NTP Server | Stratum | Auth Key | Timezone

#### 5.5 Syslog & SNMP Design
- Table: Device | Syslog Target | Port | Facility | Severity | SNMP Version | Community/USM

### 6. Security Design (detailed)

#### 6.1 Firewall Rule Table
Table: Rule ID | Direction | Source Zone | Dest Zone | Source IP | Dest IP | Port/Protocol | Action | Logging | Justification

#### 6.2 ACL Specifications
Table: ACL Name | Applied To | Direction | Sequence | Action | Source | Destination | Protocol/Port | Remarks

#### 6.3 Authentication & Access Control
- AAA design (TACACS+/RADIUS server, fallback)
- Table: Device | Auth Method | Primary Server | Secondary Server | Fallback | Privilege Levels
- SSH key requirements, banner text, session timeout values

#### 6.4 Certificate & TLS Design
- CA hierarchy, certificate subject, SANs, validity period
- Table: Service | Certificate CN | Issuing CA | Expiry | Protocol | Cipher Suite | Notes

#### 6.5 Secret & Credential Management
- Where credentials are stored (CyberArk, HashiCorp Vault, env files)
- No credential values in this document — reference the Security Guide / credential doc

### 7. Application & Service Configuration Design

#### 7.1 Service Parameters
One sub-section per service/application component:
- Service name, executable/container image + version
- Config file path and key parameters (show values)
- Bind address, port, protocol
- Startup method (systemd unit name, compose service name)
- Dependencies (other services that must be running first)

#### 7.2 Integration Specifications
Table: Integration | Source System | Target System | Protocol | Port | Auth Method | Data Format | Frequency | Error Handling

#### 7.3 API Design (if applicable)
Table: Endpoint | Method | Auth | Request Format | Response Format | Rate Limit | Used By

#### 7.4 Storage & Volume Design
Table: Service | Host Path | Mount Point | Type | Size | Backup | Retention

### 8. Implementation Plan

#### 8.1 Pre-requisites
- [ ] List each dependency that must exist before build starts (DNS, firewall changes, service accounts, etc.)

#### 8.2 Build Sequence
Numbered ordered list — each step referencing which engineer/team performs it:
1. Step description — Owner
2. Step description — Owner
...

#### 8.3 Configuration Templates / Snippets
Provide key config blocks engineers will need during build:
```
# example: OSPF config snippet, systemd unit file, compose snippet, ACL template
```
Use fenced code blocks with appropriate language tags (bash, yaml, cisco-ios, etc.)

#### 8.4 Change Window Requirements
- Estimated build time
- Change risk rating (Low / Medium / High / Critical)
- Maintenance window required? Yes/No + justification
- Rollback time estimate

### 9. Test & Verification Plan

#### 9.1 Acceptance Criteria
Table: Test ID | Test Description | Method | Expected Result | Pass/Fail

#### 9.2 Connectivity Tests
Table: Test ID | Source | Destination | Protocol/Port | Tool | Expected | Result

#### 9.3 Functional Tests
Table: Test ID | Component | Test Action | Expected Behaviour | Result

#### 9.4 Security Validation Tests
Table: Test ID | Control | Test Method | Pass Criteria | Result

### 10. Rollback Plan
- Rollback trigger criteria (when to invoke)
- Ordered rollback steps (numbered list)
- Estimated rollback time
- Post-rollback validation steps

### 11. Dependencies & Assumptions
- 11.1 Hard Dependencies — must be true before build begins
- 11.2 Soft Dependencies — desired but not blocking
- 11.3 Key Assumptions — list what is assumed about the environment

### 12. Open Items & Known Gaps
Table: Item ID | Description | Owner | Priority | Target Date | Status

### 13. Appendices
- A: Glossary
- B: Reference standards and policies
- C: Full config backup / running config (if applicable)
- D: Related documents (HLD, As-Built, Security Guide links)

---

## OT-Specific Requirements

- Always state the OT security zone (e.g. APAC-W OT Production Zone, Purdue Level)
- Document the Purdue Model level for each component: L0 (Field), L1 (Control), L2 (Supervisory), L3 (OT DMZ), L4 (IT/OT boundary)
- Air-gap and unidirectional gateway (data diode) requirements must be explicit
- SCADA/OT protocol details (Modbus, DNP3, IEC 61850, OPC-UA) must be fully specified
- No default credentials — CyberArk or approved vault reference mandatory
- Change to OT live environment requires OT Change Manager sign-off

---

## LLD Checklist

- [ ] All IP addresses, VLANs, and interfaces fully specified
- [ ] Routing design documented with exact parameters
- [ ] All firewall rules documented with justification
- [ ] ACLs documented with sequence numbers
- [ ] Authentication design references AAA server, no default creds
- [ ] All service config parameters documented with values
- [ ] Integration specs include protocol, port, auth, and error handling
- [ ] Build sequence is ordered and owner-assigned
- [ ] Config templates/snippets provided for all key components
- [ ] Test plan has measurable pass/fail criteria
- [ ] Rollback plan is documented with time estimate
- [ ] All open items tracked with owner and due date
- [ ] No credential values in this document
- [ ] OT Purdue level documented for each component (if OT scope)
- [ ] Document control version table updated
- [ ] Classification label correct
