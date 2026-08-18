# Tool Profile: Andamio Protocol

> **LF Decentralized Trust · Open Source Frontiers Lab Profile**  
> *Metadata: `observed_at: 2026-08-13` · `evidence_status: Live Production Protocol`*

---

# Overview

## Summary
**Andamio Protocol** ([https://andamio.io](https://andamio.io)) is an open-source decentralized protocol built on the Cardano blockchain designed to bridge developer onboarding, verifiable skill accreditation, and automated smart-contract treasury escrow. Built for open-source organizations, DAOs, and dOSPOs, Andamio enables projects to create structured onboarding ladders where contributors complete maintenance modules and task milestones to earn verifiable on-chain credentials that unlock project tasks and treasury payouts.

## Purpose
Andamio addresses the maintainer onboarding bottleneck. Open-source projects frequently suffer from contributor churn: new developers join communication channels but lack structured learning pathways, while maintainers spend excessive hours evaluating unverified developer claims. Andamio replaces informal onboarding with verifiable on-chain skill credentials, tokenized task ladders, and automated smart contract escrow.

## Mission Alignment
Andamio aligns with the Open Source Frontiers mission by providing open, verifiable on-chain credentialing and treasury escrow rails that convert novel developers into trusted, long-term maintainers.

---

# Tool Classification

## Category
- [ ] Governance Tooling
- [x] **Open Source Sustainability**
- [x] **Contributor Coordination**
- [x] **Treasury & Funding Infrastructure**
- [x] **Credentialing & Reputation**
- [ ] Analytics & Observability
- [ ] Security & Incident Response
- [ ] Developer Tooling
- [ ] Interoperability Infrastructure
- [ ] Community Operations
- [ ] Documentation & Knowledge Systems
- [x] **Lifecycle Management**
- [x] **Public Goods Infrastructure**
- [ ] Compliance & Policy
- [ ] Other: ___________

## Open Source Status
- [x] **Fully Open Source**
- [ ] Source Available
- [ ] Mixed / Hybrid
- [ ] Proprietary Components

## License
Apache 2.0 / GNU General Public License v3.0

---

# Ecosystem Context

## Target Ecosystems
- Cardano blockchain & UTXO smart contract ecosystem
- Substrate / Polkadot networks (via cross-chain adapters)
- Open-source developer communities, DAOs, and dOSPO initiatives

## Intended Users
- Open-source project maintainers defining contributor learning pathways
- Contributor mentees seeking verifiable skills and milestone bounties
- dOSPO program managers tracking contributor onboarding velocity
- DAO treasury managers automating task escrow payouts

## Current Pain Points Addressed
Eliminates informal maintainer onboarding bottlenecks, replaces unverified resume claims with tokenized on-chain credentials, automates milestone escrow payouts, and provides transparent contributor conversion analytics.

---

# Technical Information

## Repository / Source Code
[https://github.com/andamio-platform](https://github.com/andamio-platform)

## Documentation
[https://docs.andamio.io](https://docs.andamio.io)

## Core Technologies
- Plutus / Aiken (Cardano UTXO smart contracts)
- Mesh JS / Lucid (Cardano transaction SDKs)
- Next.js / TypeScript (dApp portal & course interface)
- Blockfrost / TxPipe (blockchain indexing infrastructure)

## Architecture Overview
Andamio operates through a network of smart contract validators on Cardano:
- **Course & Module Validator**: Manages course content hashes, module prerequisites, and student enrollment records.
- **Credential Validator**: Issues tokenized credentials (native tokens/NFTs) to students who complete module assignments verified by maintainers.
- **Project Escrow Validator**: Holds milestone funding in smart contract escrow, automatically releasing stipends to credentialed developers upon deliverable verification.

## Dependencies
- Cardano node & UTXO ledger
- Blockfrost / Kupo / Ogmios indexing services
- Wallet web bridge (CIP-30 compatible wallets)

---

# Operational Model

## Governance Model
Andamio operates as an open protocol. Smart contract updates and platform features are governed by the Andamio core team and community contributors.

## Maintenance Model
Maintained by the Andamio team alongside open-source contributors in the Cardano community.

## Funding Model
Development funded via Cardano Catalyst grants, ecosystem foundation support, and protocol service integration fees.

## Contributor Model
Open-source contribution via public GitHub repositories. Course creators and maintainers participate via Andamio's own credentialing contracts.

---

# Open Source Impact

## Expected Benefits
- Verifiable, portable on-chain skill credentials for developer contributions
- Automated, custody-free milestone escrow disbursements upon task completion
- Structured progression ladders filtering for long-term stewardship orientation
- Transparent onboarding analytics for dOSPO program managers

## Ecosystem Value
Andamio institutionalizes developer onboarding, converting volunteer friction into a transparent, credentialed contributor pipeline for critical infrastructure.

## Risks & Limitations
- Smart contracts deployed natively on Cardano UTXO architecture (Plutus/Aiken), requiring adapters for EVM interoperability.
- Maintaining high-quality course modules requires active maintainer effort to prevent outdated content.

---

# Adoption & Maturity

## Current Lifecycle Stage
- [ ] Concept
- [ ] Prototype
- [ ] Alpha
- [ ] Beta
- [x] **Production**
- [ ] Mature

## Current Adoption
Deployed in production on Cardano. Used by Gimbalabs, Andamio learning spaces, and community projects to issue thousands of on-chain credentials and process milestone escrow payouts.

## Roadmap
Expanding EVM and Substrate cross-chain credential adapters, integrating automated GitHub PR verification, and publishing open course templates.

---

# Metrics & Evaluation

## Success Metrics

| Metric | Description |
|---|---|
| Credentials Issued | Total tokenized skill credentials minted to student contributors |
| Active Learning Spaces | Number of open-source projects running Andamio onboarding courses |
| Escrow Volume | Total ADA value disbursed through smart contract task escrows |
| Mentee Conversion Rate | Percentage of course enrollees advancing to active project maintainers |

## Observability / Reporting
On-chain credentials and escrow payouts are queryable on Cardano block explorers (Cardanoscan) and visual dashboards at `andamio.io`.

---

# Alignment With Open Source Frontiers

## Relevant Focus Areas
- [x] **Open Source Sustainability**
- [ ] Decentralized Governance
- [x] **Contributor Incentives**
- [x] **Treasury Coordination**
- [ ] Security & Resilience
- [ ] Ecosystem Analytics
- [x] **Lifecycle Stewardship**
- [x] **Public Goods Funding**
- [x] **Cross Ecosystem Collaboration**
- [x] **Infrastructure Neutrality**
- [ ] Other: ___________

## Why This Tool Fits the Lab
Andamio provides the essential technical primitives for **OMF Contributor Pathways**, converting developer onboarding into a transparent, credentialed maintainer pipeline.

## Program Relevance & Direct OSF Alignment

### 1. OMF Contributor Pathways & Progression Ladders
- **OSF Mapping**: **OMF Program 3 (Contributor Pathways)** & **[`omf/PROGRAM_PORTFOLIO.md`](../omf/PROGRAM_PORTFOLIO.md)**.
- **Mechanism Validated**: Validates that structured contributor ladders (Entry -> Regular -> Trusted -> Core) paired with verifiable on-chain credentials convert novel developers into long-term maintainers.
- **Operator Takeaway**: OMF Contributor Pathway managers use Andamio smart contracts to manage task assignments, credential issuing, and stipend escrow for mentee developers.

### 2. dOSPO Contributor Verification
- **OSF Mapping**: **dOSPO Specification ([`dospo/START_HERE.md`](../dospo/START_HERE.md))** & **Transparency Requirements**.
- **Mechanism Validated**: Proves that contributor skill claims and completed deliverables can be verified on-chain without relying on self-reported developer resumes.
- **Operator Takeaway**: A dOSPO utilizes Andamio credentials to verify that maintainer retainer candidates possess documented codebase contributions before approving retainer contracts.

---

# Supporting Materials

## References
- Andamio Website: https://andamio.io
- Andamio Documentation: https://docs.andamio.io
- Gimbalabs Education Platform: https://gimbalabs.com

## Demonstrations / Screenshots
- Live platform: https://andamio.io
- Andamio App Portal: https://app.andamio.io

## Related Projects
- Cardano Catalyst (grant funding)
- Open Source Frontiers Lab (OMF Contributor Pathways)

---

# Contributor Information

## Primary Contact
- Andamio Core Team — Website: [https://andamio.io](https://andamio.io) / GitHub: [@andamio-platform](https://github.com/andamio-platform)

## Contributors
- Andamio core development team & Gimbalabs contributors

## Submission Date
2026-08-18
