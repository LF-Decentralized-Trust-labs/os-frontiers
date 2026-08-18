# Ecosystem Profile: Optimism Superchain & Sequencer Revenue Allocation

> **EVM L2 Superchain Sequencer Revenue Tithe & RetroFunding Architecture**  
> *LF Decentralized Trust · Open Source Frontiers Lab Profile*

```yaml
ecosystem: "Optimism Superchain"
architecture_type: "EVM L2 Optimistic Rollup / Superchain"
primary_governance: "Optimism Collective (Token House & Citizens' House)"
replenishment_layer: "Protocol Layer (Superchain Sequencer Fee Contribution), Application Layer (Open Source Observer / Drips)"
native_assets: "OP, ETH"
observed_at: "2026-08-13"
evidence_status: "Live Production Precedent"
```

---

## 1. Executive Summary & Ecosystem Overview

The **Optimism Superchain** (comprising OP Mainnet, Base, Zora, Mode, Ink, Fraxtal) provides the primary Web3 production precedent for **Protocol-Layer Revenue Routing ($\tau$)**. Member chains in the Superchain contribute a standardized fee-take (**the greater of 15% of net transaction-fee profit or 2.5% of gross fees**) directly to a shared Optimism Collective Treasury.

While Optimism pioneered protocol fee-take collection, its historical distribution relied heavily on retroactive voting rounds (RetroPGF / RetroFunding). The Open Source Frontiers framework decouples Optimism's revenue collection rail from its grant allocation workflow — establishing that sequencer revenue must fund baseline maintainer retainers before remaining capital is distributed to speculative grants.

---

## 2. Core Precedents & Empirical Mechanics

### 2.1 Superchain Sequencer Contribution (Protocol Fee Split $\tau$)
- **Mechanics**: Sequencers running OP Stack chains capture transaction fees and priority tips. Protocol contracts enforce an automatic fee split: 15% of net profit (or 2.5% gross fees) flows automatically to the shared Collective Treasury.
- **Empirical Impact**: Generated tens of millions in non-inflationary revenue for public goods, demonstrating that L2 sequencing scales non-inflationary treasury replenishment.

### 2.2 Open Source Observer (OSO) Impact Metrics
- **Mechanics**: Optimism integrates **Open Source Observer (OSO)** to track developer retention, dependency graphs, commit frequencies, and gas utilization across Superchain repositories.
- **Empirical Impact**: Provides auditable, empirical data for RetroFunding rounds, eliminating unverified self-reported claims.

---

## 3. Program Relevance & Direct OSF Alignment

### 1. ORF Protocol Fee Split ($\tau$)
- **OSF Mapping**: **ORF Layer 1 (Protocol Fee Routing — $\tau$ Split)** & **[`INSTRUMENT_CATALOG.md`](../orf/INSTRUMENT_CATALOG.md)**.
- **Mechanism Validated**: Proves that protocol-level transaction fee splits generate massive recurring treasury replenishment without relying on token minting or inflationary expansion.
- **Operator Takeaway**: An ORF Operator adopts Optimism's 15% net profit split as the primary protocol-layer inflow rail ($\tau = 0.15$) to fund baseline ecosystem maintenance.

### 2. dOSPO Separation of Collection vs Allocation
- **OSF Mapping**: **dOSPO Specification ([`dospo/START_HERE.md`](../dospo/START_HERE.md))** & **Safeguard 3 (No Granular Budget Approval)**.
- **Mechanism Validated**: Demonstrates that while automated revenue collection works seamlessly, using subjective retroactive voter rounds for routine maintenance creates voter fatigue and unpredictable maintainer stipends.
- **Operator Takeaway**: dOSPO routes protocol fee revenue directly into predictable OMF maintainer retainers rather than subjecting routine maintenance to periodic popularity contests.
