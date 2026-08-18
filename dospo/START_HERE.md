# dOSPO Architecture & Governance Specification

> **LF Decentralized Trust · Open Source Frontiers Lab Framework**  
> *Stage 0 Research Candidate · Release Edition: `v0.8.0-rc.1`*

---

## 1. Executive Summary & Core Definition

The **Decentralized Open Source Program Office (dOSPO)** defines *who decides* in an open-source ecosystem. A dOSPO is a non-custodial governance-coordination and portfolio-oversight layer that establishes ecosystem maintenance charters, sets budget caps, audits maintainer performance, and enforces operator replaceability.

### CRITICAL STRUCTURAL SAFEGUARD: ZERO TREASURY CUSTODY
The dOSPO **NEVER holds direct discretionary custody of treasury funds**. Treasury assets remain locked in non-custodial smart contracts or governed vault accounts authorized directly by Community Governance.

```text
               ┌──────────────────────────────────────────┐
               │    COMMUNITY GOVERNANCE (Token / DAO)    │
               │   • Authorizes Charters & Policy Rules   │
               │   • Approves Treasury Budget Caps        │
               │   • Appoints & Replaces Operators        │
               └────────────────────┬─────────────────────┘
                                    │ (Policy Mandates)
                                    ▼
               ┌──────────────────────────────────────────┐
               │        dOSPO COORDINATION LAYER          │
               │   • Holds Zero Direct Treasury Custody   │
               │   • Audits Maintainer Performance        │
               │   • Recommends Budget Allocations        │
               └────────────────────┬─────────────────────┘
                                    │
               ┌────────────────────┴─────────────────────┐
               ▼                                          ▼
┌──────────────────────────────┐          ┌──────────────────────────────┐
│        OMF OPERATOR          │          │        ORF OPERATOR          │
│ (Executes Maintainer Retainers│          │ (Manages Commercial Products │
│  & Security Resilience)      │          │  & Revenue Collection)       │
└──────────────┬───────────────┘          └──────────────┬───────────────┘
               │                                         │
               └────────────────────┬────────────────────┘
                                    ▼
               ┌──────────────────────────────────────────┐
               │   NEUTRAL LEGAL ENTITY (PCF Wrapper)     │
               │   • Signs Commercial Customer Contracts  │
               │   • Invoices Customers & Pays Fiat       │
               │   • Holds Liability & Enforces IP        │
               └──────────────────────────────────────────┘
```

---

## 2. Institutional Web3 Precedents for dOSPO Architecture

Primary evidence across major Web3 ecosystems demonstrates three distinct reference implementations for separating governance authorization from legal execution:

1. **Polkadot Community Foundation (PCF — Cayman Islands Foundation Company)**:
   - *Best dOSPO Organizational Precedent*. PCF is explicitly structured as an "unopinionated" off-chain executor of OpenGov referenda instructions. PCF signs commercial contracts, makes fiat payments, holds assets, and engages service providers, while DOT holders retain 100% governance authority (with power to withhold funding, replace directors, or dissolve the entity).
2. **Cardano Intersect Open Source Committee (OSC) & Open Source Office (OSO)**:
   - *Division of Operational Labor*. OSC provides governance oversight and policy direction, while OSO executes operational program management, bug bounty administration, and maintainer contracting.
3. **ENS DAO & ENS Foundation / KPK Endowment Manager**:
   - *Bounded Operational Discretion*. ENS DAO enacts social policy and Investment Policy Statements (EP6.46 IPS). Professional managers (KPK) execute asset allocation within strict governed boundaries, while the ENS Foundation (Cayman Foundation Company) provides the legal-world interface.

---

## 3. RACI Responsibility Assignment Matrix

To ensure absolute operational clarity, dOSPO functions are mapped across Community Governance, dOSPO Policy Team, OMF Operator, ORF Operator, and Neutral Legal Entity (PCF Wrapper):

| Function / Task | Community Governance | dOSPO Policy Team | OMF Operator | ORF Operator | Neutral Legal Entity |
|---|---|---|---|---|---|
| **Approve Maintenance Charters** | **Accountable (A)** | Responsible (R) | Consulted (C) | Consulted (C) | Informed (I) |
| **Approve Annual Budget Caps** | **Accountable (A)** | Responsible (R) | Consulted (C) | Consulted (C) | Informed (I) |
| **Maintainer Retainer Selection** | Informed (I) | **Accountable (A)** | Responsible (R) | Consulted (C) | Informed (I) |
| **Commercial SLA Sales & Contracting** | Informed (I) | Consulted (C) | Consulted (C) | **Accountable (A)** | Responsible (R) |
| **Fiat Payroll & Tax Filing** | Informed (I) | Informed (I) | Consulted (C) | Consulted (C) | **Accountable / Responsible (A/R)** |
| **Replace Non-Performing Operator** | **Accountable (A)** | Responsible (R) | Informed (I) | Informed (I) | Informed (I) |
| **Quarterly Performance Audit** | Informed (I) | **Accountable / Responsible (A/R)** | Consulted (C) | Consulted (C) | Informed (I) |

---

## 4. Operational Safeguards & Operator Replaceability

1. **Safeguard 1 — No Treasury Custody**: dOSPO members and operators NEVER hold direct multi-sig or private-key custody over treasury principal.
2. **Safeguard 2 — Operator Replaceability**: Community Governance retains absolute authority to vote out non-performing OMF/ORF operators or dissolve the legal foundation entity under pre-defined referendum thresholds.
3. **Safeguard 3 — Non-Granular Budget Allocation**: Governance approves high-level program charters and budget caps, leaving day-to-day maintainer triage and milestone verification to OMF operators under transparent rubrics.
