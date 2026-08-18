# Open Replenishment Framework (ORF) Whitepaper

> **A Portfolio Architecture for Closed-Loop Open Source Ecosystem Replenishment**  
> *Author: LF Decentralized Trust · Open Source Frontiers Lab*  
> *Stage 0 Research Candidate · Release Edition: `v0.8.0-rc.1` · Version 1.0*

---

## Abstract

Traditional open-source funding operates exclusively as a one-way financial drain. Ecosystems disburse grants and treasury capital outward, but possess zero mechanisms to capture economic value created by sustained infrastructure, leading to perpetual treasury depletion.

This whitepaper introduces the **Open Replenishment Framework (ORF)** — a portfolio design framework for identifying, validating, collecting, diversifying, and routing recurring sources of value back into ecosystem maintenance treasuries. ORF organizes replenishment across **5 Revenue Families**, enforces **8 Hard Gates for Self-Sustainability**, quantifies health using **5 Replenishment Ratios**, and establishes a **Deployment Evidence Rating Scale (D0 to D5)**.

---

## 1. Closed-Loop Replenishment Architecture

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
               │   • Net Overhead & Tax Deducted          │
               │   • Wind-down Reserves Retained          │
               └────────────────────┬─────────────────────┘
                                    │ (Net Replenishment)
                                    ▼
               ┌──────────────────────────────────────────┐
               │            GOVERNED TREASURY             │
               └────────────────────┬─────────────────────┘
                                    │ (Approved Allocations)
                                    ▼
               ┌──────────────────────────────────────────┐
               │         ROUTING & ALLOCATION RAILS       │
               │   • Drips / Superfluid Dependency Splits │
               │   • AI Allocation Engines                │
               └──────────────────────────────────────────┘
```

---

## 2. Core Economic Principles

1. **Legitimacy & Counter-Value**: Optional commercial collection must provide independent counter-value (assurances, SLAs, registries, training). Protocol-native collection requires explicit governance legitimacy.
2. **Strict Functional Separation**: Decouples *Revenue Sources* (new money generated) from *Routing Rails* (smart contracts moving existing money like Drips/Superfluid) and *Allocation Engines* (AI/voting algorithms).
3. **Correlation-Aware Diversification**: Requires multiple uncorrelated revenue risk classes (enterprise contracts, protocol fees, capital yield) rather than token-price-correlated instruments.
4. **Net Contribution Auditability**: Evaluated strictly on *Net Contribution* after deducting sales, legal, tax, support delivery, and administrative overhead.
5. **Fork-Resilient Economic Anchors**: Monetization centers on non-copyable economic assets — maintainer capacity, brand trust, verified registry state, canonical network activity, and enterprise SLAs — rather than paywalling open-source code.

---

## 3. The Five Practical Revenue Families

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

---

## 4. The 8 Hard Gates for Self-Sustainability

An ecosystem MAY NOT claim Level 3 "Self-Sustaining" maturity based on additive point scores alone. An ecosystem must satisfy **all eight hard gates**:

1. **Gate 1 (Measurement)**: Verified annual baseline cost floor ($C_{\text{base}}$).
2. **Gate 2 (Cash Evidence)**: Audited cash or stablecoin receipts actually received.
3. **Gate 3 (Net Coverage)**: Recurring non-inflationary net inflows equal or exceed 100% of baseline maintenance ($\text{PCR} \ge 100\%$).
4. **Gate 4 (Multi-Class Diversity)**: Inflows originate from at least two uncorrelated Revenue Correlation Classes.
5. **Gate 5 (Concentration Limit)**: Single-payer revenue concentration ratio $\text{RCR} \le 25\%$.
6. **Gate 6 (Stress Runway)**: Preserves $\ge 24$ months liquid operating reserve under compound stress ($\text{SCR} \ge 1.0$).
7. **Gate 7 (Liability Coverage)**: All customer SLAs backed by contracted maintainers and refund reserves.
8. **Gate 8 (Independent Audit)**: Annual financial and operational audits published publicly.

---

## 5. Deployment Evidence & Maturity Scale (D0 to D5)

- **D0 (Hypothesis)**: Theoretical concept only.
- **D1 (Buyer Validated)**: Documented buyer interviews and LOIs confirming willingness-to-pay.
- **D2 (Paid Pilot)**: Executing signed pilot contracts with real cash/stablecoin receipts.
- **D3 (Renewable)**: Customer contract renewals executed over a full multi-quarter cycle.
- **D4 (Scaled)**: Diversified customer base generating positive net contribution after overhead.
- **D5 (Resilient)**: Multi-year operational history surviving a complete market downturn.
