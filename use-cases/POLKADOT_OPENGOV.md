# Open Source Frontiers Lab — Use Case Submission Template

## Use Case Title
Polkadot OpenGov: Technical Fellowship Ranks 0–9 & PCF Legal Execution Architecture

---

# Overview

## Summary
The **Polkadot ecosystem** provides two vital Web3 reference implementations for open-source sustainability:
1. **Polkadot Technical Fellowship**: A transparent, rank-based maintainer progression ladder (Ranks 0 through 9) with automated, tenure-weighted stipends that eliminate political grant voting for core developers.
2. **Polkadot Community Foundation (PCF)**: A neutral Cayman foundation company authorized by OpenGov referenda to execute off-chain legal contracts, pay fiat salaries, and hold commercial software licenses.

Polkadot's Treasury is funded directly through protocol-level rules: transaction fees, unspent token issuance, and **validator slashing penalties** flow directly into the OpenGov Treasury pool.

## Problem Statement
Decentralized blockchain governance frameworks frequently encounter severe operational bottlenecks:
- On-chain referenda and DAOs cannot legally sign commercial contracts, hire software vendors, hold intellectual property, or execute fiat payroll.
- Subjective token holder voting for developer salaries leads to political populism, toxic governance debates, and loss of senior technical talent.
- Core protocol maintainers require predictable multi-year career progression ladders rather than episodic grant applications.
- Treasury replenishment mechanisms that rely solely on inflation dilute token holders during bear markets.

## Why This Matters
Polkadot's dual implementation of the Technical Fellowship (rank-based technical meritocracy) and the Polkadot Community Foundation (legal execution wrapper) solves the core operational challenges facing decentralized governance. Demonstrating how an on-chain DAO can execute off-chain legal contracts while protecting maintainers from political grant voting provides a vital blueprint for all Web3 ecosystems.

---

# Ecosystem Context

## Ecosystem / Organization
- Polkadot Network & Parachain Ecosystem
- Polkadot OpenGov Referenda Framework
- Polkadot Technical Fellowship
- Polkadot Community Foundation (PCF)
- Parity Technologies & Web3 Foundation

## Stakeholders
- Core Substrate & Polkadot protocol developers (Fellowship Ranks 0–9)
- OpenGov Treasury delegates & DOT holders
- Parachain development teams & ecosystem builders
- PCF Foundation directors & legal compliance officers
- Independent security auditors & infrastructure providers

## Current Challenges
- Managing Treasury expenditure velocity during market downturns
- Protecting Technical Fellowship rank evaluations from external political interference
- Coordinating legal compliance across multi-jurisdictional maintainer teams via PCF
- Balancing fast-track emergency technical upgrades with decentralized referendum confirmation

---

# Proposed Solution

## Description
Polkadot addresses open-source stewardship through a three-part structural architecture:
1. Polkadot Technical Fellowship: An on-chain, self-governing body of core protocol developers structured across 10 distinct ranks (Rank 0 Candidate to Rank 9 Grand Master). Fellowship members receive automated monthly stipends scaled to their rank, evaluated exclusively by peer code reviews.
2. Polkadot Community Foundation (PCF): A neutral Cayman Foundation Company mandated by OpenGov referenda to act as the DAO's legal execution arm — signing commercial contracts, maintaining legal compliance, and paying fiat maintainer salaries.
3. Protocol-Native Treasury Inflows: Polkadot enforces protocol rules where unspent token issuance, transaction fees, and a designated percentage of validator slashing penalties flow directly into the OpenGov Treasury.

## Operational Model
The operational model functions across six interacting stages:
1. Validators execute Substrate consensus; transaction fees and slashing penalties accumulate.
2. Protocol contracts route fees, unspent issuance, and slashes to the OpenGov Treasury.
3. Developers apply to the Technical Fellowship; peers evaluate contributions and assign Rank 0–9 status.
4. Fellowship members receive automated, rank-scaled monthly stipends from Treasury tracks.
5. Complex commercial proposals are authorized by OpenGov referenda and assigned to PCF.
6. PCF executes legally binding contracts, managing vendor SLAs, fiat payouts, and compliance.

## Governance Considerations
Governance is segmented into specialized tracks:
- OpenGov Spender Tracks manage treasury budget caps, origin thresholds, and conviction voting.
- Technical Fellowship governs developer rank progression and whitelists emergency technical upgrades.
- PCF acts strictly under DAO mandate, holding zero independent discretionary policy authority.

## Funding / Sustainability Model
Funding combines protocol issuance, fee splits, and validator slashing penalties. By capturing a portion of validator slash events, the protocol penalizes bad actors while replenishing ecosystem reserves.

---

# Technical Details

## Technologies Involved
- Substrate blockchain framework & Rust runtime
- Polkadot OpenGov referenda pallets (Spender Tracks, Whitelist)
- Polkadot Technical Fellowship pallet (Rank 0–9 registry & stipend logic)
- PCF legal foundation agreements & bank escrow rails
- On-chain conviction voting & tallying logic

## Dependencies
- Substrate Nominated Proof-of-Stake (NPoS) consensus
- OpenGov referenda origin thresholds and decision periods
- Cayman Islands Foundation Company legal framework
- Peer review evaluation by senior Fellowship members (Ranks 4+)

## Integration Requirements
- On-chain Fellowship identity registration & rank tracking
- PCF corporate resolution documentation for OpenGov proposals
- Treasury payout address mapping for multi-sig and fiat rails

---

# Open Source Impact

## Expected Benefits
- Transparent, rank-based maintainer career progression (Ranks 0 to 9)
- Elimination of political grant voting for core developer salaries
- Legally compliant off-chain contract execution via PCF
- Protocol-native treasury replenishment from validator slashing penalties
- High retention of senior protocol architects and security researchers

## Risks
- Fellowship cartelization risk if peer evaluations lack external transparency
- Offshore legal foundation jurisdiction risk under PCF
- Treasury depletion risks during extended crypto market drawdowns

## Metrics for Success

| Metric | Description |
|---|---|
| Fellowship Members (Ranks 0-9) | Active developers categorized by rank in Technical Fellowship ladder |
| Monthly Fellowship Stipends | Total DOT disbursed automatically based on rank progression |
| PCF Contracts Executed | Off-chain commercial maintainer SLAs and vendor contracts executed by PCF |
| Slashing Penalties Captured | Annual DOT value from validator slashes routed to Treasury replenishment |
| Emergency Upgrades Whitelisted | Critical technical fixes accelerated via Fellowship whitelist track |

---

# Lifecycle Assessment

## Current Stage
- [ ] Concept
- [ ] Research
- [ ] Prototype
- [ ] Pilot
- [x] Production (Live production OpenGov referenda, Technical Fellowship, & PCF legal wrapper)
- [ ] Scaling

## Estimated Timeline
Polkadot mainnet launched in 2020. OpenGov and Technical Fellowship deployed in 2023. PCF operationalized in 2024.

## Resource Requirements
- Substrate OpenGov runtime pallets
- Polkadot Treasury reserves
- PCF legal counsel & foundation directors
- Fellowship peer review committee (Ranks 4+)

---

# Alignment With Open Source Frontiers

## Relevant Focus Areas
- [x] Open Source Sustainability
- [x] Decentralized Governance
- [x] Funding Mechanisms
- [x] Contributor Incentives
- [x] Ecosystem Coordination
- [x] Infrastructure Stewardship
- [x] Security & Resilience
- [x] Public Goods Funding
- [x] Interoperability
- [ ] Compliance & Policy
- [ ] Other: ___________

## Why This Fits the Lab
Polkadot provides battle-tested Web3 reference models for maintainer rank progression (Technical Fellowship), legal foundation execution (PCF), and protocol slashing penalty routing.

## Program Relevance & Direct OSF Alignment

### 1. OMF Contributor Pathways (Technical Fellowship Rank Ladder)
- **OSF Mapping**: **OMF Program 3 (Contributor Pathways — Maintainer Ladder)** & **[`PROGRAM_PORTFOLIO.md`](../omf/PROGRAM_PORTFOLIO.md)**.
- **Mechanism Validated**: Validates that explicit rank-based progression (Ranks 0 to 9) combined with peer evaluation creates a transparent maintainer pipeline that retains senior talent.
- **Operator Takeaway**: OMF adopts Polkadot's Fellowship rank progression model to structure its contributor onboarding ladder from Entry Contributor to Core Maintainer.

### 2. dOSPO Legal Execution Layer (PCF Model)
- **OSF Mapping**: **dOSPO Legal Execution Layer** & **Safeguard 2 (Operator Replaceability)**.
- **Mechanism Validated**: Proves that decentralized governance requires an independent, neutral foundation wrapper (PCF) to execute commercial SLAs, contracts, and fiat payments.
- **Operator Takeaway**: dOSPO specifications adopt the PCF architecture — placing legal contracting authority in a neutral foundation wrapper while reserving charter authorization, budget votes, and operator replacement for Community Governance.

### 3. ORF Protocol Layer Slashing Penalty Routing
- **OSF Mapping**: **ORF Layer 1 (Protocol Fee & Slashing Routing)** & **[`INSTRUMENT_CATALOG.md`](../orf/INSTRUMENT_CATALOG.md)**.
- **Mechanism Validated**: Demonstrates that protocol-level penalty burns can be safely redirected to fund ecosystem maintenance treasuries.
- **Operator Takeaway**: ORF incorporates validator slashing penalty routing into its protocol fee split specifications.

---

# Supporting Materials

## References
- Polkadot Technical Fellowship Wiki: https://wiki.polkadot.network/learn/learn-polkadot-technical-fellowship/
- Polkadot OpenGov Treasury Wiki: https://wiki.polkadot.network/learn/learn-polkadot-opengov-treasury/
- Polkadot Community Foundation (PCF) Overview: https://wiki.polkadot.com/general/pcf/
- Substrate Framework Monorepo: https://github.com/paritytech/polkadot-sdk

## Related Repositories
- Polkadot Technical Fellowship Manifest: https://github.com/polkadot-fellows/manifesto
- Polkadot OpenGov Pallets: https://github.com/paritytech/polkadot-sdk/tree/master/substrate/frame/referenda
- PCF Legal Framework Docs: https://github.com/polkadot-community-foundation

## Additional Notes
Provides primary reference models for rank progression ladders and legal foundation execution wrappers.

---

# Contributor Information

## Primary Contact
- Polkadot Technical Fellowship Stewards
- Polkadot Community Foundation Directors
- Web3 Foundation Governance Team

## Contributors
- Christian Taylor
- Polkadot Fellow Members

## Submission Date
2026-08-18
