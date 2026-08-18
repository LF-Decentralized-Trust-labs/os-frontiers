# Open Replenishment Framework (ORF)

> **LF Decentralized Trust · Open Source Frontiers Lab Framework**  
> *Stage 0 Research Candidate · Release Edition: `v0.8.0-rc.1`*

---

## 1. Executive Summary & Definition

The **Open Replenishment Framework (ORF)** is a governance and economic design framework for identifying, validating, collecting, diversifying, and routing recurring sources of value back into the maintenance of shared open-source infrastructure.

Traditional open-source funding models rely exclusively on one-way capital outflows — grant disbursements, venture capital subsidies, or episodic donations that inevitably result in maintainer burnout and funding cliffs. ORF provides an architectural blueprint for open ecosystems to build **closed-loop sustainability systems**, capturing value generated across the ecosystem to replenish maintainer reserves without compromising open-source licensing freedom.

```text
               ┌──────────────────────────────────────────┐
               │          ECONOMIC VALUE GENERATION       │
               │  ┌──────────────────┬─────────────────┐  │
               │  │ Protocol Revenue │ Enterprise Sales│  │
               │  ├──────────────────┼─────────────────┤  │
               │  │ Ecosystem Dues   │ Capital Yield   │  │
               │  └──────────────────┴─────────────────┘  │
               └────────────────────┬─────────────────────┘
                                    │ (Gross Inflows)
                                    ▼
               ┌──────────────────────────────────────────┐
               │           ORF COLLECTION LAYER           │
               │   • Tax, Legal & Operating Overhead      │
               │   • Wind-down & Reserves Deducted       │
               └────────────────────┬─────────────────────┘
                                    │ (Net Replenishment)
                                    ▼
               ┌──────────────────────────────────────────┐
               │            GOVERNED TREASURY             │
               │   • dOSPO Budget Caps & Policy Controls  │
               │   • Capital IPS / Reserve Management     │
               └────────────────────┬─────────────────────┘
                                    │ (Approved Allocations)
                                    ▼
               ┌──────────────────────────────────────────┐
               │         ROUTING & ALLOCATION RAILS       │
               │   • Drips / Superfluid Dependency Splits │
               │   • AI & Tenure-Weighted Allocation Engines│
               └────────────────────┬─────────────────────┘
                                    │ (Streaming Disbursements)
                                    ▼
               ┌──────────────────────────────────────────┐
               │         OMF MAINTENANCE DEPLOYMENT        │
               │   • Maintainer Retainers & SLAs          │
               │   • Resilience & Security Audit Program  │
               └────────────────────┬─────────────────────┘
                                    │ (Sustained Codebase)
                                    ▼
               ┌──────────────────────────────────────────┐
               │      CRITICAL OPEN INFRASTRUCTURE        │
               └──────────────────────────────────────────┘
```

---

## 2. Core Economic Principles

1. **Legitimacy & Counter-Value**: Optional collection mechanisms must provide independent, tangible counter-value to buyers (assurances, SLAs, registries, training). Protocol-native collection mechanisms require explicit governance legitimacy from token holders and network stakeholders.
2. **Strict Functional Separation**: ORF strictly decouples *Revenue Sources* (new money generated) from *Routing Rails* (smart contracts moving existing money like Drips or Superfluid) and *Allocation Engines* (algorithms deciding distribution percentages).
3. **Correlation-Aware Diversification**: Sustainable replenishment requires multiple uncorrelated revenue risk classes (e.g. enterprise contracts combined with protocol fees), rather than multiple token-price-correlated instruments.
4. **Net Contribution Auditability**: Every collection mechanism is evaluated strictly on *Net Contribution* after deducting sales, legal, tax, support delivery, and administrative overhead.
5. **Fork-Resilient Economic Anchors**: Monetization centers on non-copyable economic assets — maintainer capacity, brand trust, verified registry state, canonical network activity, and enterprise SLAs — rather than paywalling open-source code.

---

## 3. Two-Dimensional Instrument Matrix

Instruments are categorized across two distinct dimensions: **Value-Origin Layer** (where value originates) and **Instrument Type** (functional economic role).

### Dimension 1: Value-Origin Layer
- **Protocol Layer**: On-chain network activity, sequence fees, and canonical protocol services.
- **Application Layer**: User-facing dApps, ecosystem tooling, and dependency distribution.
- **Enterprise Layer**: Commercial adopters, corporate users, and institutional buyers.
- **Capital Layer**: Accumulated treasury reserves, yield strategies, and financial assets.
- **Delegation Layer**: Validator networks, stake pools, and community pledges.

### Dimension 2: Instrument Type
- **Revenue Source**: Generates or redirects new recurring money into sustainability.
- **Contribution Source**: Voluntary or incentive-based capital transfers.
- **Routing Rail**: Technical infrastructure that moves already-collected money down the supply chain.
- **Allocation Mechanism**: Algorithm or voting system that determines recipient split percentages.
- **Capital Management**: Generates financial return from accumulated principal reserves.
- **Financial / Risk Product**: Contingent claims, underwriting, or repayment rights.

---

## 4. The Five Practical Revenue Families

ORF organizes all valid replenishment instruments under five core revenue families:

```
┌────────────────────────────────────────────────────────────────────────┐
│                        FIVE REVENUE FAMILIES                           │
├──────────────────┬──────────────────┬──────────────────┬───────────────┤
│ Family A         │ Family B         │ Family C         │ Family D      │
│ Structural Net   │ Enterprise Earned│ Ecosystem Dues   │ Voluntary &   │
│ Revenue          │ Revenue          │ & Certification  │ Pledges       │
├──────────────────┼──────────────────┼──────────────────┼───────────────┤
│ • Protocol Fees  │ • Open Infra     │ • Consortium Dues│ • Project     │
│ • Sequencer Tithe│   Assurance      │ • Ecosystem Provider│ Pledges    │
│ • Canonical Fees │ • Maintainer LTS │   Certification  │ • Stake Pool  │
│                  │   SLAs           │ • Training Bundles│   Pledges     │
├──────────────────┴──────────────────┴──────────────────┴───────────────┤
│ Family E: Capital Income (Governed Endowment IPS Yield & Liquid Reserves)│
└────────────────────────────────────────────────────────────────────────┘
```

1. **Family A — Structural Network Revenue**: Protocol-level fee splits ($\tau$), sequencer profit contributions, and canonical protocol service fees. (Highest structural durability; requires explicit governance legitimacy).
2. **Family B — Enterprise Earned Revenue**: Commercial products including Open Infrastructure Assurance Subscriptions (risk intelligence/escalation) and Maintainer-backed Extended Lifecycle Support (LTS) SLAs. (Most transferable; requires operational service capacity).
3. **Family C — Ecosystem Membership & Certification**: Linux Foundation-style consortium membership tiers (*Supporter, Sustainer, Strategic Sustainer*) and Certified Ecosystem Provider/Sustainer programs backed by objective technical testing.
4. **Family D — Voluntary / Incentivized Contributions**: Protocol Guild-style 1% project token/yield pledges, ecosystem sponsorship pools, and validator stake pool pledges.
5. **Family E — Capital Income**: Governed endowment Investment Policy Statements (IPS) generating yield from low-risk liquid reserves (US Treasuries, stablecoins, ETH staking).

---

## 5. Deployment Evidence & Maturity Scale (D0 to D5)

To prevent conflating external market precedents with deployment readiness, ORF assigns a strict **Deployment Evidence Rating** to every instrument:

| Status | Stage Name | Definition & Qualification Criteria |
|---|---|---|
| **D0** | **Hypothesis** | Theoretical concept; no buyer interviews or technical specs completed. |
| **D1** | **Buyer Validated** | Documented buyer interviews and Letters of Intent (LOIs) confirming willingness-to-pay. |
| **D2** | **Paid Pilot** | Production pilot executing signed contracts with initial paying customers. |
| **D3** | **Renewable** | Paid customer renewals executed over a full multi-quarter contract cycle. |
| **D4** | **Scaled** | Diversified customer base delivering positive net contributions after all operational costs. |
| **D5** | **Resilient** | Multi-year operational history surviving a complete crypto/macro market downturn. |

---

## 6. MVP Architecture & Deployment Roadmap (0–24 Months)

An ecosystem deploying ORF should not attempt all instruments simultaneously. A realistic deployment executes in phased waves:

```
[ Phase 1: Months 0–3 ] ──> [ Phase 2: Months 3–6 ] ──> [ Phase 3: Months 6–12 ] ──> [ Phase 4: Months 12–24 ]
  • Maintenance Baseline     • Pre-Sell Assurance       • Maintainer LTS SLAs      • Conformance Programs
  • Audit Current Inflows      & Member Tiers           • Drips / Superfluid       • Endowment IPS
  • Form Legal Entity        • Onboard 3–5 Pilots         Routing Infrastructure     • Advanced Risk Products
```

- **Phase 1 (Months 0–3): Baseline & Setup**: Audit true annual maintenance costs, establish native-token exposure baselines, form neutral legal entity (PCF wrapper), and complete 15–25 enterprise buyer interviews.
- **Phase 2 (Months 3–6): Commercial Pre-Sell**: Launch Open Infrastructure Assurance Subscriptions and Ecosystem Sustaining Member tiers. Onboard 3 to 5 pilot customers before building 24/7 SLA infrastructure.
- **Phase 3 (Months 6–12): SLA Operations & Routing**: Contract maintainers under formal Service Capacity Tests to offer Extended Lifecycle Support (LTS) SLAs. Integrate Drips and Superfluid smart contracts as transparent routing rails.
- **Phase 4 (Months 12–24): Conformance & Endowment**: Launch Certified Ecosystem Provider technical testing and establish a governed Endowment IPS to manage accumulated capital reserves. Advanced financial instruments (mutuals, bonds) remain in long-term research.

---

## 7. Master Document Directory

- **[`INSTRUMENT_CATALOG.md`](./INSTRUMENT_CATALOG.md)**: Exhaustive specification of all 5 Revenue Families, Routing Rails, Allocation Engines, and Advanced Financial Products.
- **[`GOVERNANCE_RULES.md`](./GOVERNANCE_RULES.md)**: The 8 Hard Gates for Self-Sustainability, 5 Replenishment Ratios, Revenue Correlation Classes, Service Capacity Tests, and Legal Entity Architecture.
- **[`../docs/TIER_1_FEASIBILITY_MODEL.md`](../docs/TIER_1_FEASIBILITY_MODEL.md)**: Financial scenario modeling comparing commercial pilots against cost floors under compound stress tests.
- **[`../docs/EVIDENCE_REGISTER.md`](../docs/EVIDENCE_REGISTER.md)**: Primary-source audit matrix mapping external precedents, verified statuses, and transferability ratings.
