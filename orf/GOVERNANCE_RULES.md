# Open Replenishment Framework — Governance Rules & Operational Safeguards

> **LF Decentralized Trust · Open Source Frontiers Lab Specification**  
> *Stage 0 Research Candidate · Release Edition: `v0.8.0-rc.1`*

---

## 1. Executive Governance Principles

The **Open Replenishment Framework (ORF)** enforces strict economic, legal, and operational rules to prevent treasury misallocation, maintainer capture, pay-to-play corruption, or legal liability exposure. ORF operates under the authority of **Community Governance** and policy coordination from the **dOSPO**, but commercial operations are executed through an independent, neutral legal entity.

---

## 2. The 8 Hard Gates for Self-Sustainability

An ecosystem MAY NOT claim Level 3 "Self-Sustaining" maturity based on additive point scores alone. An ecosystem must satisfy **all eight hard gates**:

```text
┌────────────────────────────────────────────────────────────────────────┐
│                   THE 8 HARD GATES FOR SELF-SUSTAINABILITY             │
├──────────────────┬──────────────────┬──────────────────┬───────────────┤
│ Gate 1           │ Gate 2           │ Gate 3           │ Gate 4        │
│ Measurement      │ Cash Evidence    │ Net Coverage     │ Diversity     │
│ Verified cost    │ Audited cash     │ Net Inflows ≥    │ ≥ 2 Uncorrelated│
│ baseline         │ receipts only    │ Cost Floor       │ Risk Classes  │
├──────────────────┼──────────────────┼──────────────────┼───────────────┤
│ Gate 5           │ Gate 6           │ Gate 7           │ Gate 8        │
│ Concentration    │ Stress Runway    │ Liabilities      │ Independent   │
│ Single payer     │ 24+ Mo. Stressed │ All SLA liabilities│ Annual Audit│
│ ≤ 25% Inflow     │ Operating Reserve│ Covered          │ Published     │
└──────────────────┴──────────────────┴──────────────────┴───────────────┘
```

1. **Gate 1 — Measurement**: The ecosystem must possess an empirically verified annual maintenance cost floor ($C_{\text{base}}$).
2. **Gate 2 — Cash Evidence**: Inflow metrics must reflect audited cash or stablecoin receipts actually received — theoretical demand projections or un-realized token pledges do not qualify.
3. **Gate 3 — Net Coverage**: Recurring non-inflationary net inflows must equal or exceed 100% of baseline maintenance expenses ($\text{PCR} \ge 1.0$).
4. **Gate 4 — Multi-Class Diversity**: Inflows must originate from at least two materially uncorrelated Revenue Correlation Classes (e.g. enterprise contracts + protocol fees).
5. **Gate 5 — Concentration Limit**: No single commercial customer or payer may account for more than 25% of total recurring net inflows.
6. **Gate 6 — Stress Runway**: The ecosystem must maintain at least 24 months of operating liquidity under a compound stress scenario ($\text{SCR} \ge 1.0$).
7. **Gate 7 — Liability Coverage**: All contractual customer SLAs and maintainer retainers must be fully backed by allocated service capacity and wind-down reserves.
8. **Gate 8 — Independent Audit**: Annual financial and operational audits must be published publicly by an independent third party.

---

## 3. The 5 Formal Replenishment Ratios

ORF quantifies ecosystem health using five standardized financial ratios:

### 1. Incremental Earned Coverage Ratio (IECR)
$$\text{IECR} = \frac{R_{\text{earned\_net}}}{C_{\text{base}}}$$
*Measures new commercial value created directly by enterprise subscriptions, membership dues, and certifications.*

### 2. Structural Protocol Coverage Ratio (SPCR)
$$\text{SPCR} = \frac{R_{\text{protocol\_net}}}{C_{\text{base}}}$$
*Measures non-inflationary protocol fee splits ($\tau$) and sequencer revenue contributions.*

### 3. Portfolio Coverage Ratio (PCR)
$$\text{PCR} = \frac{R_{\text{earned\_net}} + R_{\text{protocol\_net}} + R_{\text{yield\_net}} + R_{\text{pledges\_net}}}{C_{\text{base}}}$$
*Measures total recurring non-inflationary net coverage across all active revenue families.*

### 4. Stress Coverage Ratio (SCR)
$$\text{SCR} = \frac{R_{\text{stressed\_inflows}}}{C_{\text{austerity\_floor}}}$$
*Evaluates treasury resilience under a compound stress scenario (50% token price crash + 30% transaction drop + 25% customer churn).*

### 5. Revenue Concentration Ratio (RCR)
$$\text{RCR} = \frac{\max(R_i)}{\sum R_i}$$
*Measures single-payer dependency risk. RCR must remain $\le 0.25$.*

---

## 4. Revenue Correlation Classes

To achieve true economic diversification, an ecosystem must combine instruments across distinct, uncorrelated risk classes:

1. **Class 1 — Native Network Activity**: Protocol transaction fees, sequencer profit splits ($\tau$).
2. **Class 2 — Native Token Price**: Staking yield, validator pool pledges.
3. **Class 3 — Enterprise Contract Revenue**: Infrastructure assurance subscriptions, LTS SLAs.
4. **Class 4 — Membership & Certification**: Consortium dues, provider certification programs, training.
5. **Class 5 — Capital-Market Return**: Endowment IPS yield, liquid US Treasury sleeves.
6. **Class 6 — Philanthropic / Voluntary**: Ecosystem dApp pledges, public grants.

---

## 5. Service Capacity Test for Extended Lifecycle Support (LTS)

An ecosystem MAY NOT offer or sell **Extended Lifecycle Support (LTS) / Maintenance SLAs** (Instrument B.2) until passing a formal **Service Capacity Test**:

```text
┌────────────────────────────────────────────────────────────────────────┐
│                        SERVICE CAPACITY TEST                           │
├────────────────────────────────────────────────────────────────────────┤
│ 1. Contracted Maintainer Capacity (Dedicated engineering hours committed)│
│ 2. Triage & Support Infrastructure (24/7 or defined intake & ticketing)  │
│ 3. Escalation & Backport Procedures (Documented patch release pipelines) │
│ 4. Liability & Insurance Coverage (Contractual liability caps & legal)  │
│ 5. Wind-down Operating Reserve (6 months reserved customer refund pool)  │
└────────────────────────────────────────────────────────────────────────┘
```

If an ecosystem fails the Service Capacity Test, it is restricted to selling **Open Infrastructure Assurance Subscriptions** (Instrument B.1), which provide risk intelligence without SLA guarantees.

---

## 6. Neutral Legal Entity Architecture & Operating Overhead

To prevent dOSPO or OMF managers from acting as commercial sales agents or assuming legal liability, ORF enforces a clear structural separation:

```text
COMMUNITY GOVERNANCE ──> Authorizes Policy & Budget Caps
        │
        ▼
   dOSPO LAYER       ──> Audits Performance & Coordinates Policy
        │
        ├───────────────────────────────┐
        ▼                               ▼
   OMF OPERATOR                    ORF OPERATOR
(Deploys Maintenance)          (Manages Commercial Strategy)
        │                               │
        └───────────────┬───────────────┘
                        ▼
            NEUTRAL LEGAL ENTITY (PCF Wrapper)
   • Signs Commercial Customer SLAs & Contracts
   • Invoices Customers & Collects Fiat / Stablecoins
   • Files W-8/W-9 Taxes & Complies with Local Laws
   • Maintains Liability Insurance & Legal Defense
   • Routes Net Proceeds to Governed Treasury
```

Operating expenses (sales, legal counsel, corporate filing fees, tax compliance, support delivery) are paid directly by the Neutral Legal Entity from gross customer receipts before net proceeds flow to the Governed Treasury.

---

## 7. Legal & Tax Compliance Rules

### Recoverable Mission Funding (RMF) vs Program-Related Investments (PRIs)
- Agreements that finance open-source projects with potential revenue returns are designated as **Recoverable Mission Funding (RMF)**.
- RMF MAY NOT be categorized automatically as a U.S. IRS Program-Related Investment (PRI) without explicit tax counsel opinion verifying that the investment primarily furthers tax-exempt purposes and that income production is not a significant purpose.

### Unrelated Business Income Tax (UBIT) Compliance
- Commercial service revenues (SLAs, custom engineering) received by tax-exempt foundation wrappers are subject to Unrelated Business Income Tax (UBIT) unless the activity is substantially related to the organization's exempt purpose.
- Merely using commercial proceeds to fund open-source maintainers DOES NOT exempt income from UBIT. Neutral legal entities must maintain proper tax reserves.

---

## 8. Audit & Reporting Requirements

The ORF Operator must publish a public **Quarterly Replenishment Audit** containing:
1. Gross receipts collected by revenue family.
2. Itemized cost-to-collect (sales overhead, legal fees, tax payments, platform fees).
3. Net contribution transferred to Governed Treasury.
4. Single-payer revenue concentration ratios ($\text{RCR}$).
5. Stressed operating runway metrics ($\text{SCR}$).
6. Status of customer SLA liabilities and wind-down reserves.
