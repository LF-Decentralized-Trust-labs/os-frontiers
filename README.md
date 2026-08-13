# Open Source Frontiers Lab (LF Decentralized Trust)

> **Guidance Frameworks on Open-Source Sustainability in Web3**  
> *A 3-Piece Architecture: Governance (dOSPO), Deployment (OMF), and Collection (ORF)*

[![License: Apache 2.0 / CC-BY-4.0](https://img.shields.io/badge/License-Apache_2.0_%7C_CC--BY--4.0-blue.svg)](./LICENSE-CODE)
[![LF Decentralized Trust](https://img.shields.io/badge/LF-Decentralized_Trust_Lab-green.svg)](https://lfdecentralizedtrust.org)
[![Edition: July 2026 Research Candidate](https://img.shields.io/badge/Edition-July_2026_Research_Candidate-orange.svg)](./VALIDATION.md)

---

## Executive Overview

Open-source software powers critical global infrastructure, yet digital commons remain systematically under-funded and under-maintained. The **Open Source Frontiers Lab** (hosted at **LF Decentralized Trust**) provides a complete, 3-piece framework suite to transform open-source funding from episodic charity into a self-sustaining economic loop.

```
       +-------------------------------------------------------+
       |                        dOSPO                          |
       |       (Decentralized Open Source Program Office)       |
       |   WHO: Mandate, Governance, Policy & Neutrality       |
       +---------------------------+---------------------------+
                                   |
         +-------------------------+-------------------------+
         |                                                   |
         v                                                   v
+---------------------------------+         +---------------------------------+
|               OMF               |         |               ORF               |
|   (Open Maintenance Framework)  |         |  (Open Replenishment Framework) |
| HOW DEPLOY: Program Retainers,  |========>| HOW COLLECT: Value Alignment,   |
| Maintenance, Contributor Paths  | Treasury| Collection Instruments, Yield,  |
|                                 | Buffer  | Enterprise SLAs & Endowments    |
+---------------------------------+         +---------------------------------+
```

---

## The 3-Piece Framework Recipe

The suite enforces a strict division of labor with **zero functional overlap**:

### 1. [dOSPO — Decentralized Open Source Program Office](./dospo/START_HERE.md)
* **Question Answered**: *WHO* holds authority and sets policy?
* **Role**: Bounded, community-mandated coordination body holding the governance triangle (**legitimacy, neutrality, execution**). Sets spending priorities and collection rules while remaining fully replaceable by the community.

### 2. [OMF — Open Maintenance Framework](./omf/START_HERE.md)
* **Question Answered**: *HOW* is capital deployed to sustain infrastructure?
* **Role**: Portfolio of operational programs translating mandates and treasury capital into long-term infrastructure health (Maintainer Retainers, Contributor Pathways, Tooling Stewardship, Lifecycle-Aligned Funding).

### 3. [ORF — Open Replenishment Framework](./orf/START_HERE.md)
* **Question Answered**: *HOW* does value flow back to replenish the treasury?
* **Role**: Governed portfolio of 20+ collection instruments matched to where value is realized across 5 layers (**Protocol, Application, Enterprise & Services, Capital, Delegation**). Reframes initial reserve usage as a measured "Bootstrap Loan."

---

## Quick Navigation & Master Document Index

| Framework / Module | Description | Core Artifacts & Templates |
|---|---|---|
| 🏛️ **dOSPO** | Governance & Policy Framework | [dOSPO Specification](./dospo/START_HERE.md) • [dOSPO Charter](./dospo/CHARTER.md) • [Funding Principles](./dospo/FUNDING_PRINCIPLES.md) |
| 🛠️ **OMF** | Maintenance & Deployment Framework | [OMF Specification](./omf/START_HERE.md) • [Program Charter Template](./omf/PROGRAM_CHARTER_TEMPLATE.md) • [Stewardship](./omf/STEWARDSHIP.md) |
| 💰 **ORF** | Replenishment & Inflow Framework | [ORF Specification](./orf/START_HERE.md) • [Instrument Catalog](./orf/INSTRUMENT_CATALOG.md) • [Governance Rules](./orf/GOVERNANCE_RULES.md) |
| 📈 **Pro-Forma Model** | Tier 1 Feasibility Scenario Model | [Tier 1 Feasibility Scenario Model](./docs/TIER_1_FEASIBILITY_MODEL.md) |
| 🏆 **Validation Lifecycle** | 4-Stage Validation Framework | [Validation Framework & Register](./VALIDATION.md) |
| 🌍 **Use Cases** | Multi-Chain Ecosystem Profiles | [Cardano POSM](./use-cases/CARDANO_POSM.md) • [Optimism Superchain](./use-cases/OPTIMISM_SUPERCHAIN.md) • [Polkadot](./use-cases/POLKADOT_OPENGOV.md) • [Ethereum EVM](./use-cases/ETHEREUM_EVM.md) |
| 🛠️ **Tools & Protocols** | Governance & Replenishment Tools | [Open Source Observer](./tools/OPEN_SOURCE_OBSERVER.md) • [Drips Protocol](./tools/DRIPS_PROTOCOL.md) • [Superfluid](./tools/SUPERFLUID.md) |
| 📊 **Evaluator Suite** | QUAID, CHAOSS & Systems Assessor | [Evaluator Documentation](./evaluator/README.md) • [QUAID Audit Example](./evaluator/examples/CARDANO_QUAID_SCANNER_REPORT.md) |
| 📜 **Smart Contracts** | Reference Solidity & Aiken Vaults | [Native Contracts Guide](./contracts/README.md) • [EVM Solidity Contract](./contracts/solidity/ORFSlaVault.sol) • [Cardano Aiken Validator](./contracts/aiken/validators/orf_sla_vault.ak) |
| 📊 **Pitch & Adoption Kit** | Executive Decks & Proposal Templates | [Pitch Deck](./pitch/EXECUTIVE_PITCH_DECK.md) • [One-Pager](./pitch/ONE_PAGER.md) • [Forum Proposal](./pitch/GOVERNANCE_PROPOSAL_TEMPLATE.md) • [Enterprise Sales Kit](./pitch/ENTERPRISE_SPONSOR_KIT.md) |
| 🌐 **Web Suite App** | Interactive 3-Piece Dashboard | Launch [`index.html`](./index.html) in your browser for the Interactive Catalog, 3-Piece Evaluator, Pro-Forma Calculator, and Exporter. |

---

## Citation & License

**Research Edition — Candidate for External Validation**  
*Author*: Christian Taylor (`opensourcecowboy.org`) · Open Source Frontiers Lab · LF Decentralized Trust  
*License*: Code & CLI Tools under [Apache-2.0](./LICENSE-CODE); Documentation & Frameworks under [CC-BY-4.0](./LICENSE-DOCS).
