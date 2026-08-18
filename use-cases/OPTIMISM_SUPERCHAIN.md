# Open Source Frontiers Lab — Use Case Submission

# Optimism Superchain: Sequencer Revenue Tithe & RetroFunding Architecture
---

# Overview

## Summary
The **Optimism Superchain** (comprising OP Mainnet, Base, Zora, Mode, Ink, Fraxtal) represents the premier Web3 production precedent for **Protocol-Layer Revenue Routing ($\tau$)** and bi-cameral ecosystem governance. Member rollup chains in the Superchain contribute a standardized fee-take (**the greater of 15% of net transaction-fee profit or 2.5% of gross fees**) directly to a shared Optimism Collective Treasury. While Optimism pioneered automated sequencer revenue collection, its historical distribution relied on retroactive voter rounds (RetroPGF / RetroFunding) evaluated via **Open Source Observer (OSO)** impact data.

## Problem Statement
Layer-2 scaling solutions generate substantial economic activity, but early L2 rollups captured sequencing revenue entirely for private operators or token buybacks, leaving underlying open-source maintainers uncompensated. Furthermore:
- Open-source infrastructure maintainers lack predictable ongoing compensation when funding relies on episodic grant rounds.
- Subjective retroactive voter rounds create severe voter fatigue among badgeholders and encourage speculative grant-writing over long-term code stewardship.
- Fluctuations in native governance token prices create budget instability for maintainer payroll.
- Evaluating multi-chain impact across dozens of L2 rollups requires open, verifiable data infrastructure to prevent fraud.

## Why This Matters
The Superchain fee split demonstrates that protocol-level sequencing rules can generate tens of millions of dollars in non-inflationary treasury replenishment without relying on continuous token inflation. Analyzing Optimism's success in revenue collection — combined with its operational challenges in retroactive grant allocation — provides vital empirical lessons for how decentralized ecosystems must structure their replenishment and deployment frameworks.

---

# Ecosystem Context

## Ecosystem / Organization
- Optimism Collective
- OP Labs
- Optimism Foundation
- Citizens' House & Token House
- Superchain Member Chains (Base, Zora, Mode, Ink, Fraxtal)
- Kariba Labs (Open Source Observer)

## Stakeholders
- Layer-2 rollup operators & sequencers
- Open-source infrastructure maintainers & developer tooling builders
- Citizens' House badgeholders & Token House delegates
- Ecosystem dApp developers & users
- Impact data analysts & grant administrators

## Current Challenges
- Badgeholder voter fatigue during large retroactive grant rounds
- Over-reliance on volatile native OP token disbursements for maintainer payroll
- Distinguishing continuous maintenance commitments from short-term promotional projects
- Scaling sequencer revenue enforcement across newly onboarded Superchain chains

---

# Proposed Solution

## Description
Optimism addresses ecosystem sustainability through a two-part operational model:
1. **Protocol Fee Split ($\tau$)**: All OP Stack chains joining the Superchain execute a standardized contribution contract: sequencers automatically transfer 15% of net profit (or 2.5% of gross fees) to the shared Optimism Collective Treasury.
2. **Bi-Cameral Governance & Data Tracing**: Governance is split between token holders (Token House) and identity-verified badgeholders (Citizens' House). Citizens' House evaluates public-goods allocations using empirical metrics provided by **Open Source Observer (OSO)**.

## Operational Model
The Superchain operational model runs across six interacting stages:
1. Sequencers execute Layer-2 transactions and capture fees.
2. Smart contracts automatically enforce the 15% net profit split ($\tau$) to the Collective Treasury.
3. Treasury reserves accumulate in ETH and OP tokens.
4. OSO data pipelines aggregate GitHub commits, dependency trees, and gas generation across indexed projects.
5. Citizens' House badgeholders evaluate project impact using OSO metrics.
6. Treasury disburses allocated funding to project maintainers.

## Governance Considerations
Governance operates under a strict bi-cameral framework:
- Token House governs protocol upgrades, parameter changes, and treasury budget caps.
- Citizens' House governs public-goods funding allocations based on "impact = profit".
- Operational execution is supported by the Optimism Foundation and specialized grant councils.

## Funding / Sustainability Model
Funding is driven primarily by protocol-layer commercial sequencing revenue rather than continuous token minting. As transaction volume across Superchain L2s grows, non-inflationary treasury replenishment scales automatically.

---

# Technical Details

## Technologies Involved
- OP Stack rollup infrastructure & sequencer contracts
- Superchain Fee Split smart contracts
- Open Source Observer (OSO) BigQuery data warehouse & GraphQL API
- Drips Protocol dependency streaming contracts
- Attestation Station (identity & badgeholder attestations)

## Dependencies
- Ethereum L1 security & data availability layer
- OP Stack sequencer software & fee routing modules
- Kariba Labs OSO data pipeline infrastructure
- Citizens' House badgeholder voting applications

## Integration Requirements
- OP Stack chain deployment of Superchain fee split contracts
- OSO mapping of GitHub repositories and smart contract deployments
- Wallet registry for automated maintainer payouts

---

# Open Source Impact

## Expected Benefits
- Scalable, non-inflationary protocol fee revenue generated from L2 transaction activity
- Empirical, data-driven public-goods allocation powered by OSO metrics
- Alignment between commercial rollup growth and open-source infrastructure funding
- Reduced reliance on state budget grants or private venture capital

## Risks & Mitigation
- **Voter Fatigue Risk**: Mitigated by shifting routine maintenance from retroactive voting to predictable OMF maintainer retainers.
- **Token Volatility Risk**: Mitigated by converting a portion of sequencer fee inflows into stablecoin reserves.
- **Enforcement Risk**: Mitigated by standardized OP Stack chain governance agreements.

## Metrics for Success

| Metric | Description |
|---|---|
| Superchain Fee Revenue | Annual fee contributions from member L2 chains to Collective Treasury ($M+/yr) |
| Active Superchain Chains | Number of OP Stack chains executing protocol fee splits (OP Mainnet, Base, Mode, etc.) |
| Projects Indexed by OSO | Open-source repositories tracked with verifiable Superchain impact metrics |
| Maintainer Retention Rate | Multi-year retention rate of core infrastructure maintainers receiving funding |
| Non-Inflationary Ratio | Proportion of funding covered by sequencer fees vs OP token treasury reserves |

---

# Lifecycle Assessment

## Current Stage
- [ ] Concept
- [ ] Research
- [ ] Prototype
- [ ] Operational Pilot
- [x] Production (Live production Superchain revenue split & governance infrastructure)
- [ ] Scaling

## Estimated Timeline
OP Mainnet launched in 2021. RetroPGF Round 1 executed in 2021. Superchain fee split agreements were operationalized in 2023 with Base and subsequent chains.

## Resource Requirements
- OP Stack sequencer infrastructure
- Superchain fee split smart contracts
- Kariba Labs OSO analytics engine
- Citizens' House governance coordination

---

# Alignment With Open Source Frontiers

## Program Relevance & Direct OSF Alignment

### 1. ORF Protocol Fee Split ($\tau$)
- **OSF Mapping**: **ORF Layer 1 (Protocol Fee Routing — $\tau$ Split)** & **[`INSTRUMENT_CATALOG.md`](../orf/INSTRUMENT_CATALOG.md)**.
- **Mechanism Validated**: Proves that protocol-level transaction fee splits generate massive recurring treasury replenishment without relying on token minting or inflationary expansion.
- **Operator Takeaway**: An ORF Operator adopts Optimism's 15% net profit split as the primary protocol-layer inflow rail ($\tau = 0.15$) to fund baseline ecosystem maintenance.

### 2. dOSPO Separation of Collection vs Allocation
- **OSF Mapping**: **dOSPO Specification ([`dospo/START_HERE.md`](../dospo/START_HERE.md))** & **Safeguard 3 (No Granular Budget Approval)**.
- **Mechanism Validated**: Demonstrates that while automated revenue collection works seamlessly, using subjective retroactive voter rounds for routine maintenance creates voter fatigue and unpredictable maintainer stipends.
- **Operator Takeaway**: dOSPO routes protocol fee revenue directly into predictable OMF maintainer retainers rather than subjecting routine maintenance to periodic popularity contests.

---

# Supporting Materials

## References
- Optimism Superchain Revenue Docs: https://docs.optimism.io/governance/capital-allocation
- Optimism Collective Charter: https://github.com/ethereum-optimism/OIPs
- Open Source Observer Platform: https://www.opensource.observer/
- Drips Protocol Infrastructure: https://drips.network/

## Related Repositories
- OP Stack Monorepo: https://github.com/ethereum-optimism/optimism
- Open Source Observer Pipeline: https://github.com/opensource-observer/oso
- Superchain Governance Contracts: https://github.com/ethereum-optimism/governance

---

# Contributor Information

## Primary Contact
- Optimism Foundation & Governance Council
- Kariba Labs / Open Source Observer Team

## Contributors
- Christian Taylor
- Optimism Collective Contributors

## Submission Date
2026-08-18
