# The Open Replenishment Framework (ORF)

> **Closing the Loop: Value-Aligned Collection for Self-Sustaining Open Source Ecosystems**  
> *Author: Christian Taylor · Open Source Frontiers Lab · LF Decentralized Trust*  
> *Companion to the dOSPO Whitepaper and the Open Maintenance Framework (OMF)*  
> *Validated Research Edition · Final Revised & Expanded July 2026 · `opensourcecowboy.org`*

---

## Abstract

Web3 ecosystems have made meaningful progress on the **deployment half** of open source sustainability: how treasuries authorize spending through on-chain governance (**dOSPO**), who coordinates it, and how programs run through the Open Maintenance Framework (**OMF**). Cardano’s Paid Open Source Model (POSM) provides a concrete, approved pilot of this operating architecture, although implementation remains incomplete across the full program portfolio.

What remains less developed is the **collection half**: how value created by sustained open source infrastructure can flow back into the capital base that funded it. Many token-funded ecosystems still depend heavily on monetary expansion, finite reserves, or one-time token allocations. Those mechanisms can bootstrap a system, but they do not by themselves create a durable feedback loop.

This paper introduces the **Open Replenishment Framework (ORF)**: a portfolio of collection instruments organized into four primary layers — **protocol, application, enterprise and services, and capital** — with an ecosystem-specific **delegation extension**. The portfolio is governed by four principles: **value alignment, fork resistance, benefit bundling, and mandate governance**.

---

## 1. The Problem: A Half-Built Cycle

The sustainability cycle every treasury-funded ecosystem aspires to is simple to state:

```
[ Treasury Deploys Capital ] ──> [ Open Source Sustained ] ──> [ Risk Reduced & Adoption Grows ]
           ▲                                                                 │
           │                                                                 ▼
[ Capital Base Replenished ] <── [ Economic Value Collected ] <── [ Enterprise & User Activity ]
```

In compressed form: **treasury and revenue fund open source and product support, which drives market activity, which is collected and replenished.**

The deployment half of this cycle is increasingly well-architected. The dOSPO whitepaper resolves the coordination question — who holds bounded, replaceable, community-mandated authority to direct sustainability work. The Open Maintenance Framework resolves the operational question — how mandates become programs such as maintainer retainers, contributor pathways, tooling stewardship, and lifecycle-aligned funding.

The second half is more often asserted than architected. Reliance on finite token allocations or native-asset reserves creates a ticking clock. Transaction fees are a genuine feedback mechanism because they rise with network use; monetary expansion is a finite bootstrap subsidy because it draws down the reserve over time.

---

## 2. Definitions and Scope

- **Replenishment**: Any flow of value into the sustainability treasury that is causally connected to the value the treasury's deployments created. External donations and one-time endowments are welcome but out of scope; they are gifts, not loops.
- **Collection Instrument**: A specific, governable mechanism by which such a flow occurs — a fee split, a service subscription, a royalty, a yield strategy. Instruments are the unit of design, authorization, and renewal in this framework, exactly as programs are the unit of design in the OMF.
- **Fork-Resistant Anchor**: An asset, right, or relationship whose economic value is not reproduced merely by copying the source code: canonical ledger state and liquidity, the native token and treasury, governance legitimacy, certifications and brand, network effects, and institutional relationships.
- **Earned Revenue vs. Captured Value**: Captured value is routed automatically by protocol rules (a fee split). Earned revenue is exchanged voluntarily for something the payer wants (an SLA, a certification, a service).

---

## 3. Four Core Governing Principles

### 3.1 Value Alignment
Collect at the exact point where value is realized. Treasury deployments create value at four distinct points — the protocol, the applications built on it, the enterprises that adopt it, and the capital base itself — and each point requires its own instrument.

### 3.2 Fork Resistance
Attach capture to fork-resistant anchors, not to permission to use the code. A compulsory charge embedded only in software can be removed by a fork, while value associated with canonical state, liquidity, governance, brand, or trusted registries does not travel automatically with the source tree.

### 3.3 Benefit Bundling
Sell, do not merely tax. Wherever an instrument is optional, the payment must purchase something the payer independently values: defined engineering support, long-term-support (LTS) commitments, certification and registry placement, dependency intelligence, or priority access to funded development.  
> ⚠️ **Universal Safety Rule**: Essential vulnerability intake, coordinated disclosure, triage of actively exploited issues, and incident communications affecting end users remain universal public-safety functions rather than paid benefits.

### 3.4 Mandate Governance
Collection requires the same authorization discipline as spending. Every collection instrument carries four governance requirements: a traceable mandate from community governance, a defined budget interface, time-bounded renewal, and public accountability for what was collected and where it went.

---

## 4. The Case Against Collection & Burn Counter-Models

A framework proposing collection must answer ecosystems that deliberately destroy value rather than assign it.
- **Ethereum's EIP-1559**: Burns the base fee instead of routing it to a treasury, removing a recipient from allocation decisions and lowering administrative overhead.
- **Uniswap UNIfication**: Activated protocol fees, burned 100M UNI from the treasury, and routed protocol/Unichain revenue through a buyback-and-burn architecture.

**Tradeoff**: Burning is simple, comparatively neutral, and resistant to operator capture; collection creates a potential maintenance loop but also introduces governance, audit, legitimacy, and regulatory burdens. Burning is incomplete when essential maintenance remains unfunded.

---

## 5. The Five Collection Layers

```
+-----------------------------------------------------------------------------------+
|                            THE FIVE COLLECTION LAYERS                             |
|                                                                                   |
|  1. PROTOCOL LAYER   : Fee Splits, Priority Tithes, Slashing Routing              |
|  2. APPLICATION LAYER: Sustains-Commons Certifications, Dependency Splitting      |
|  3. ENTERPRISE LAYER : Maintenance SLAs, LTS Patching, Consortium Memberships     |
|  4. CAPITAL LAYER    : Governed IPS Endowments, Yield Sleeve, Risk Mutuals      |
|  5. DELEGATION LAYER : Public-Goods Stake Pools, Cross-Chain Registry Discovery   |
+-----------------------------------------------------------------------------------+
```

1. **Protocol Layer (Automatic Capture)**: Encoded in ledger or sequencing rules. Cardano fee split, Optimism sequencer tithe, Polkadot slash routing.
2. **Application Layer (Incentivized Opt-In)**: Reaches application value through benefit-bundled bundles ("Sustains the Commons" badges, Drips/tea dependency graphs, Superfluid streams).
3. **Enterprise & Services Layer (Earned Revenue)**: Denominated in fiat/stables. Red Hat/Tidelift-style SLAs, patch windows, LF-style certification, recoverable/reciprocal grant clauses.
4. **Capital Layer (Productive Treasury)**: Investment Policy Statement (IPS) governed endowments (ENS IPS, Octant staking yield), perpetual auctions (Nouns), risk pools (Nexus Mutual).
5. **Delegation Layer (Ecosystem Extension)**: Stake pool margin pledges to public goods (Cardano mission pools, cross-chain delegation registries).

---

## 6. Governance Rules of Collection

1. **Program Chartering**: Every instrument receives a traceable mandate, bounded scope, time-limited charter, and evidence-based renewal.
2. **Separation of Policy and Execution**: dOSPO sets policy; OMF operates machinery; operators are replaceable.
3. **Legal & Regulatory Posture as Design Input**: Every charter must specify responsible legal entity, jurisdiction, accounting treatment, and suspension triggers.
4. **Independent Audit Review**: Gross inflow, cost to collect, net contribution, concentration, and attribution integrity examined by an independent audit function reporting directly to governance.

---

## 7. Phased Adoption: The "Bootstrap Loan" Reframing

Initial reserve dependence is reframed as a **bootstrap loan** to be measured and systematically reduced across three phases:

| Phase | Duration | Funding Mix | Exit Criteria |
|---|---|---|---|
| **Phase 1: Reserve-Funded** | 0–18 months | Reserves carry budget; optional pilots launched | First earned-revenue contracts signed; IPS & audit ready |
| **Phase 2: Fee-Supplemented** | 18–36 months | Earned + captured revenue covers 40–60% of OMF | Net earned + captured revenue covers governed threshold |
| **Phase 3: Self-Sustaining** | 36+ months | Endowment yield + earned revenue covers baseline | Net replenishment ratio ≥ 1.0 across full market cycle |

---

## 8. Nine Core Validation & Health Metrics

1. **Net Replenishment Ratio**: `(Collected Value - Collection & Admin Costs) / Deployed Value`
2. **Earned-Revenue Coverage**: Share of baseline maintenance cost covered by non-inflationary income.
3. **Treasury Runway**: Years of baseline cost fundable without reserve draw, stress-tested in bear markets.
4. **Price Correlation**: Sensitivity of the replenishment budget to native token price volatility.
5. **Revenue Concentration**: Dependence on largest single payer, token, manager, or service strategy.
6. **Cost to Collect**: Legal, sales, servicing, metering, custody, and audit expense as share of gross inflow.
7. **Attribution Integrity Score**: Share of attributed distributions backed by verified graphs/reproducible evidence.
8. **Benefit Realization Rate**: Evidence that payers independently value bundled SLA/certification benefits.
9. **Fork / Exit Pressure Index**: Governance challenges, migration attempts, and routing-around behavior.

---

## 9. Five Questions to Assess Replenishment Posture

1. **Ratio**: What is your replenishment ratio today, and what subsidizes the gap?
2. **Anchors**: Does each collection instrument attach to a fork-resistant source of value?
3. **Bundles**: Is every optional payment attached to a benefit the payer independently wants?
4. **Mandate**: Is each instrument chartered, time-bounded, and publicly reported like a spending program?
5. **Runway**: Can baseline maintenance survive a full bear market without an emergency reserve draw?
