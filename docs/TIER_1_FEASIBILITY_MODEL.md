# Tier 1 Ecosystem Feasibility Scenario Model

> **Illustrative scenario, not a forecast and not evidence.** This file predates the arithmetic in the ORF whitepaper, section 15 (18 August 2026). An earlier draft of this file used certification net $193,150, commercial-pilot net $918,150 (IECR 30.6%), and a stressed total of $1,803,150 (SCR 1.002), and it treated a 47.4% protocol-fee share as payer concentration (RCR). Section 15 uses certification net $195,000, pilot net $920,000 (IECR 30.7%), and a stressed total of $1,835,000 (SCR 1.019), and it treats the 47.4% protocol-fee share as mechanism concentration (MCR), not RCR. The tables below are the whitepaper's tables. The two sets are not averaged. Neither set is a measured result. **No gate in this file is PASSED.** A gate passes only on audited receipts in an adopting ecosystem. Do not cite this file as validation.

> **LF Decentralized Trust · Open Source Frontiers Lab Analysis**  
> *Stage 0 Research Candidate · Edition: `v0.8.0-rc.1` · Illustrative only*

---

## 1. What this file is

This document records one author's illustrative scenario for a closed-loop sustainability architecture. It is the scenario in whitepaper section 15, copied here so the repository does not keep a second arithmetic. It is not a forecast, not evidence, and not a third case.

The cost floor is an illustrative mid-sized ecosystem at **$3,000,000 / year**. The commercial pilot does not claim self-sustainability. The full portfolio's coverage ratio is arithmetic on assumed inflows.

---

## 2. Illustrative Maintenance Cost Floor ($C_{\text{base}}$)

```text
┌────────────────────────────────────────────────────────────────────────┐
│        ILLUSTRATIVE ECOSYSTEM MAINTENANCE BUDGET ($3.0M)              │
├─────────────────────────────────────┬──────────────────┬───────────────┤
│ Component Expense Area              │ Annual Allocation│ Budget Share  │
├─────────────────────────────────────┼──────────────────┼───────────────┤
│ Core Consensus & Client Maintenance │ $1,600,000       │ 53.3%         │
│ Core SDK & Tooling Maintenance      │ $600,000         │ 20.0%         │
│ Security Audits & Vulnerability Triage│ $400,000       │ 13.3%         │
│ Program Ops, Legal & Admin Overhead │ $400,000         │ 13.3%         │
├─────────────────────────────────────┼──────────────────┼───────────────┤
│ TOTAL BASELINE MAINTENANCE FLOOR    │ $3,000,000       │ 100.0%        │
└─────────────────────────────────────┴──────────────────┴───────────────┘
```

These shares are scenario parameters. They are not a measured cost floor.

---

## 3. Whitepaper Tables (illustrative, not a forecast)

### 3.1 Defensible initial commercial pilot

Restricting the launch portfolio to the instruments in section 15:

| Instrument | Assumption | Gross | Overhead | Net Contribution |
|---|---|---|---|---|
| Open Infrastructure Assurance | 5 customers @ $75K/yr | $375,000 | 20% | $300,000 |
| Sustaining Consortium Memberships | 10 members @ $50K/yr | $500,000 | 15% | $425,000 |
| Certified Ecosystem Provider | 10 offerings @ $25K/yr | $250,000 | 22% | $195,000 |
| Defensible Commercial Net Total | — | $1,125,000 | — | $920,000 / yr |

Incremental Earned Coverage Ratio: **30.7%** ($920,000 / $3,000,000). The scenario's point is that this does not claim self-sustainability.

### 3.2 Full multi-family scenario

Section 15 adds governance-legitimized structural protocol fees ($1.5M gross, 2% overhead, $1.47M net) and governed capital yield ($750K gross, 5% overhead, $712.5K net). Together with the pilot lines, stated net replenishment is **$3,102,500** against the $3.0M floor. Portfolio Coverage Ratio: **103.4%**. The scenario also states that no commercial customer exceeds 15% of net inflows and that four correlation classes are represented. Those are assumptions inside the scenario, not observed results.

Two assumptions section 15 states explicitly, and which this file does not drop:

- The $750,000 gross capital-yield sleeve requires approximately **$15M–$25M** of productive principal already under management, at the 3–5% real yield assumed for Family E, before operating costs, reserves, tax, and volatility. An ecosystem without that principal cannot include the line.
- Gate 6 runway in the scenario is computed from a stated opening liquid operating reserve of **$5,130,000** in stable assets, against an austerity floor of **$1,800,000** per year ($150,000 per month). The resulting **34.2 months** assumes stressed inflows cease entirely rather than continuing at stressed levels.

### 3.3 Ratios in this scenario

1. **IECR** = ($300,000 + $425,000 + $195,000) / $3,000,000 = **30.7%**.
2. **SPCR** = $1,470,000 / $3,000,000 = **49.0%**.
3. **PCR** = $3,102,500 / $3,000,000 = **103.4%**. This is scenario arithmetic. It does not satisfy Gate 3, because Gate 3 requires audited cash.
4. **MCR** = $1,470,000 / $3,102,500 = **47.4%**. This is mechanism concentration on the protocol-fee line, not payer concentration. It is not RCR. In the whitepaper an MCR above 0.50 is a review trigger, not a hard gate. 47.4% is below that trigger. It is still a disclosure, not a pass.
5. **RCR** is not 47.4%. The scenario's separate assumption is that no commercial customer exceeds 15% of net inflows. That assumption is not a Gate 5 result.

---

## 4. Compound Stress Test (section 15 shocks only)

Four simultaneous shocks, as section 15 states them. Certification is held flat. That hold is an assumption, not an omission. No other shock set is added.

| Line | Base Net | Shock | Stressed Net |
|---|---|---|---|
| Protocol fees | $1,470,000 | −50% | $735,000 |
| Enterprise assurance | $300,000 | −40% | $180,000 |
| Membership dues | $425,000 | −30% | $297,500 |
| Capital yield | $712,500 | −40% | $427,500 |
| Certification | $195,000 | held flat | $195,000 |
| Stressed total | $3,102,500 | — | $1,835,000 |
| Austerity floor | — | — | $1,800,000 |
| Surplus / (deficit) | — | — | +$35,000 |

Stress Coverage Ratio: **1.019** ($1,835,000 / $1,800,000). Section 15 treats that margin as thin. It is not a pass. Combined with the stated $5,130,000 opening reserve, the scenario preserves 34.2 months only under the assumption noted above.

---

## 5. The 8 Hard Gates — none passed

No gate in this file is PASSED. A gate passes only on audited receipts in an adopting ecosystem.

1. **Gate 1 (Measurement)**: not passed. The $3.0M floor is an assumed parameter.
2. **Gate 2 (Cash Evidence)**: not passed. This file contains no audited cash or stablecoin receipts.
3. **Gate 3 (Net Coverage)**: not passed. PCR 103.4% is scenario arithmetic.
4. **Gate 4 (Diversity)**: not passed. Naming four classes in a scenario does not establish independence.
5. **Gate 5 (Concentration)**: not passed. RCR is not demonstrated. The 47.4% figure is MCR.
6. **Gate 6 (Stress Runway)**: not passed. SCR 1.019 and 34.2 months are scenario arithmetic, including an assumed opening reserve.
7. **Gate 7 (Liabilities Covered)**: not passed. No customer liabilities have been measured.
8. **Gate 8 (Independent Audit)**: not passed. This file is not an audit.

### Methodological note

These figures are scenario parameters, not forecasts. They show how the ratios can be computed. They do not show that another ecosystem will achieve the same prices, demand, costs, or mix. Every parameter has to be derived again locally.
