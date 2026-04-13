# HLD Document Guide

**Purpose:** Explain the design intent, architecture decisions, and business justification — before or alongside deployment.
**Audience:** Executive leadership, enterprise architects, security leads, service owners.
**Tone:** Strategic + technical. Explain WHY, not just WHAT. Use business language for exec sections, technical for architecture sections.

---

## Source Reference (load first 150 lines for structure context)

```
/mnt/c/Users/malaka.kahingalage/OneDrive - Rio Tinto/Second_Brain/RioTinto/20_Projects/2026/OT_AgenticOps/NetAssist_Platform_HLD.md
```

---

## Required Sections (in order)

### 1. Executive Summary
- 1.1 Business Purpose & Strategic Alignment — business drivers, strategic fit (SPS, Digital Transformation, OT/IT convergence)
- 1.2 Solution Overview — what it does, key capabilities, deployment scope
- 1.3 Business Value & Benefits — quantified (%) where possible + qualitative
- 1.4 Current Status & Success Metrics — RAG status table: criterion | target | actual | RAG

### 2. System Overview & Business Context
- 2.1 Problem Statement — what problem this solves, current pain points
- 2.2 Scope & Boundaries — what is in scope, what is explicitly out of scope
- 2.3 Stakeholders — table: Role | Name | Responsibility | Review Status
- 2.4 Assumptions & Constraints

### 3. Architecture & Design
- 3.1 Architecture Principles — guiding principles (e.g. air-gap compliant, zero-trust, rootless containers)
- 3.2 High-Level Architecture Diagram — ASCII or description of component relationships
- 3.3 Component Overview — table: Component | Role | Technology | Tier
- 3.4 Design Decisions Record — table: Decision | Options Considered | Rationale | Date

**Design Decision Record format:**
| # | Decision | Option A | Option B | Chosen | Rationale |
|---|---|---|---|---|---|

### 4. Integration Architecture
- 4.1 External System Integrations — table: System | Integration Type | Protocol | Data Flow | Auth Method
- 4.2 API & Interface Design — REST endpoints, message formats
- 4.3 Data Flow Diagrams — show how data moves between components

### 5. Security Architecture
- 5.1 Security Zones & Boundaries — OT/IT zone separation, trust levels
- 5.2 Authentication & Authorization — identity model, MFA, service accounts
- 5.3 Network Security Controls — firewall rules (conceptual), ACLs, TLS enforcement
- 5.4 Data Classification & Protection — what data is handled, how it is protected
- 5.5 Compliance Requirements — OT standards, CIS, NIST, internal Rio Tinto policy
- 5.6 Security Risk Summary — table: Risk | Likelihood | Impact | Mitigation

### 6. Data Architecture
- 6.1 Data Stores — table: Store | Type | Purpose | Retention | Backup
- 6.2 Data Classification — what is sensitive, PII, or operational-critical
- 6.3 Backup & Recovery — RPO/RTO targets and strategy

### 7. Infrastructure & Deployment
- 7.1 Infrastructure Requirements — server specs, OS, network requirements
- 7.2 Deployment Model — container, VM, bare metal; rootless/rootful; orchestration
- 7.3 Environment Strategy — Prod / Dev / Lab and promotion pathway
- 7.4 Deployment Runbook Reference — link to runbook document

### 8. Operational Architecture
- 8.1 Monitoring & Observability — tools, metrics, alerting thresholds
- 8.2 Incident Management — escalation path, on-call, runbook links
- 8.3 Change Management — change process, approval gates, rollback procedure
- 8.4 Capacity Planning — current utilisation, growth projections

### 9. Performance & Scalability
- 9.1 Performance Targets — response time, throughput, concurrent users
- 9.2 Scalability Design — horizontal/vertical scale options
- 9.3 Bottleneck Analysis — known constraints

### 10. Risk Assessment & Mitigation
Table: Risk ID | Risk Description | Category | Likelihood | Impact | RAG | Mitigation | Owner

### 11. Dependencies & Assumptions
- 11.1 Hard Dependencies (must exist before go-live)
- 11.2 Soft Dependencies (degraded operation if unavailable)
- 11.3 Key Assumptions

### 12. Appendices
- A: Glossary of terms
- B: Reference standards and policies
- C: Related documents

---

## HLD Checklist

- [ ] Business justification includes quantified metrics
- [ ] All stakeholders listed with review status
- [ ] Design decisions recorded with rationale
- [ ] Security architecture section addresses OT zone requirements
- [ ] Risk register completed with mitigations
- [ ] RPO/RTO defined for all data stores
- [ ] Document sent for review to all approvers in table
- [ ] Status updated from Draft → Review when submitted
