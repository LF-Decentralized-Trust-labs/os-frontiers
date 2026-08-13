# Open Source Frontiers Lab (LF Decentralized Trust)

> **Guidance Frameworks on Open-Source Sustainability in Web3**  
> *A 3-Piece Architecture: Governance (dOSPO), Deployment (OMF), and Collection (ORF)*

[![License: Apache 2.0 / CC-BY-4.0](https://img.shields.io/badge/License-Apache_2.0_%7C_CC--BY--4.0-blue.svg)](LICENSE)
[![LF Decentralized Trust](https://img.shields.io/badge/LF-Decentralized_Trust_Lab-green.svg)](https://lfdecentralizedtrust.org)
[![Edition: July 2026 Validated](https://img.shields.io/badge/Edition-July_2026_Validated-orange.svg)](opensourcecowboy.org)

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

### 1. [dOSPO — Decentralized Open Source Program Office](./dOSPO/START_HERE.md)
* **Question Answered**: *WHO* holds authority and sets policy?
* **Role**: Bounded, community-mandated coordination body holding the governance triangle (**legitimacy, neutrality, execution**). Sets spending priorities and collection rules while remaining fully replaceable by the community.

### 2. [OMF — Open Maintenance Framework](./OMF/START_HERE.md)
* **Question Answered**: *HOW* is capital deployed to sustain infrastructure?
* **Role**: Portfolio of operational programs translating mandates and treasury capital into long-term infrastructure health (Maintainer Retainers, Contributor Pathways, Tooling Stewardship, Lifecycle-Aligned Funding).

### 3. [ORF — Open Replenishment Framework](./ORF/START_HERE.md)
* **Question Answered**: *HOW* does value flow back to replenish the treasury?
* **Role**: Governed portfolio of 20+ collection instruments matched to where value is realized across 5 layers (**Protocol, Application, Enterprise & Services, Capital, Delegation**). Reframes initial reserve usage as a measured "Bootstrap Loan."

---

## Quick Navigation & Master Document Index

| Framework / Module | Description | Core Artifacts & Templates |
|---|---|---|
| 🏛️ **dOSPO** | Governance & Policy Framework | [dOSPO Specification](./dOSPO/START_HERE.md) • [dOSPO Charter](./dOSPO/CHARTER.md) • [Funding Principles](./dOSPO/FUNDING_PRINCIPLES.md) |
| 🛠️ **OMF** | Maintenance & Deployment Framework | [OMF Specification](./OMF/START_HERE.md) • [Program Charter Template](./OMF/PROGRAM_CHARTER_TEMPLATE.md) • [Stewardship](./OMF/STEWARDSHIP.md) |
| 💰 **ORF** | Replenishment & Inflow Framework | [ORF Specification](./ORF/START_HERE.md) • [Instrument Catalog](./ORF/INSTRUMENT_CATALOG.md) • [Governance Rules](./ORF/GOVERNANCE_RULES.md) |
| 📈 **Pro-Forma Proof** | Sourced Mathematical Proof ($\ge 1.0$) | [Tier 1 Sourced Pro-Forma Proof](./docs/TIER_1_PRO_FORMA_PROOF.md) |
| 🌍 **Use Cases** | Multi-Chain Ecosystem Profiles | [Cardano POSM](./use-cases/CARDANO_POSM.md) • [Optimism Superchain](./use-cases/OPTIMISM_SUPERCHAIN.md) • [Polkadot](./use-cases/POLKADOT_OPENGOV.md) • [Ethereum EVM](./use-cases/ETHEREUM_EVM.md) |
| 🛠️ **Tools & Protocols** | Governance & Replenishment Tools | [Open Source Observer](./tools/OPEN_SOURCE_OBSERVER.md) • [Drips Protocol](./tools/DRIPS_PROTOCOL.md) • [Superfluid](./tools/SUPERFLUID.md) |
| 📊 **Evaluator Suite** | QUAID, CHAOSS & Systems Assessor | [Evaluator Documentation](./evaluator/README.md) • [QUAID Audit Example](./evaluator/examples/CARDANO_QUAID_SCANNER_REPORT.md) |
| 📜 **Smart Contracts** | Deployable Solidity & Aiken Vaults | [Native Contracts Guide](./contracts/README.md) • [EVM Solidity Contract](./contracts/solidity/ORFSlaVault.sol) • [Cardano Aiken Validator](./contracts/aiken/validators/orf_sla_vault.ak) |
| 📊 **Pitch & Adoption Kit** | Executive Decks & Proposal Templates | [Pitch Deck](./pitch/EXECUTIVE_PITCH_DECK.md) • [One-Pager](./pitch/ONE_PAGER.md) • [Forum Proposal](./pitch/GOVERNANCE_PROPOSAL_TEMPLATE.md) • [Enterprise Sales Kit](./pitch/ENTERPRISE_SPONSOR_KIT.md) |
| 🌐 **Web Suite App** | Interactive 3-Piece Dashboard | Launch [`index.html`](./index.html) in your browser for the Interactive Catalog, 3-Piece Evaluator, Pro-Forma Calculator, and Exporter. |

---

## Citation & License

**Validated Research Edition · Final Revised & Expanded July 2026**  
*Author*: Christian Taylor (`opensourcecowboy.org`) · Open Source Frontiers Lab · LF Decentralized Trust  
*License*: Code under [Apache-2.0](LICENSE); Documentation under [CC-BY-4.0](LICENSE).
