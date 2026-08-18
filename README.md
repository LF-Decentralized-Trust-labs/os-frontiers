# Open Source Frontiers (OSF) Lab

> **Linux Foundation Decentralized Trust · Stage 0 Research Candidate**  
> *Release Candidate Edition: `v0.8.0-rc.1` · Open Source Governance & Replenishment System*

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)
[![Release Candidate](https://img.shields.io/badge/Status-Stage_0_Research_Candidate-orange.svg)](VALIDATION.md)
[![DCO Signed](https://img.shields.io/badge/DCO-Signed_Commits-green.svg)](CONTRIBUTING.md)

---

## Executive Summary

The **Open Source Frontiers Lab (OSF)** is a research and architectural framework built within **LF Decentralized Trust** to solve the open-source maintenance crisis. Modern digital society relies on thousands of critical open-source software libraries, yet funding has historically suffered from one-way capital outflows — short-term grants, volunteer burnout, and corporate capture.

OSF synthesizes Web2 and Web3 precedents into a unified, three-piece closed-loop architecture:

```text
               ┌──────────────────────────────────────────┐
               │  dOSPO (Decentralized OSPO Governance)   │
               │   • Holds Zero Direct Treasury Custody   │
               │   • Sets Policy, Charters & Budget Caps  │
               └────────────────────┬─────────────────────┘
                                    │
               ┌────────────────────┴─────────────────────┐
               ▼                                          ▼
┌──────────────────────────────┐          ┌──────────────────────────────┐
│   OMF (Maintenance Engine)   │          │  ORF (Replenishment Engine)  │
│ • Maintainer Retainers       │          │ • Structural Network Revenue │
│ • Resilience & Security      │◄─────────┤ • Enterprise Assurance & SLAs│
│ • Contributor Pathways       │  Net $   │ • Consortium Dues & Certs    │
│ • Incubation Charters        │ Flows    │ • Governed Endowment Yield   │
└──────────────────────────────┘          └──────────────────────────────┘
```

1. **dOSPO (Decentralized Open Source Program Office)**: *Who Decides*. A non-custodial governance layer that sets policy guidelines, defines maintenance charters, and enforces operator replaceability.
2. **OMF (Open Maintenance Framework)**: *How Money Goes Out*. A structured maintenance deployment engine executing maintainer retainers, vulnerability audits, contributor pathways, and dependency incubation.
3. **ORF (Open Replenishment Framework)**: *How Money Comes Back*. A portfolio framework identifying, validating, collecting, and diversifying recurring sources of value to replenish ecosystem treasuries.

---

## Key Core Principles of ORF

- **Legitimacy & Counter-Value**: Optional commercial collection must provide independent counter-value (assurances, SLAs, registries, training). Protocol-native collection requires explicit governance legitimacy.
- **Strict Functional Separation**: Decouples *Revenue Sources* (new money generated) from *Routing Rails* (smart contracts moving existing money like Drips/Superfluid) and *Allocation Engines* (AI/voting algorithms).
- **Correlation-Aware Diversification**: Requires multiple uncorrelated revenue risk classes (enterprise contracts, protocol fees, capital yield) rather than token-price-correlated instruments.
- **Net Contribution Auditability**: Evaluated strictly on *Net Contribution* after deducting sales, legal, tax, support delivery, and administrative overhead.
- **8 Hard Gates for Self-Sustainability**: Enforces strict quantitative criteria (Measurement, Cash evidence, Net coverage $\ge 100\%$, Diversity $\ge 2$ classes, Concentration $\le 25\%$, Stress runway $\ge 24$ mo., Liabilities covered, Independent Audit).

---

## Master Document Directory & Navigation

### Core Architectural Specification
- **[`dospo/START_HERE.md`](./dospo/START_HERE.md)**: Decentralized OSPO Governance Specification & RACI Matrix.
- **[`omf/PROGRAM_PORTFOLIO.md`](./omf/PROGRAM_PORTFOLIO.md)**: Maintenance Program Specifications (Retainers, Bounties, Pathways, Resilience, Incubation).
- **[`orf/START_HERE.md`](./orf/START_HERE.md)**: Open Replenishment Framework Master Introduction & 5 Revenue Families.
- **[`orf/INSTRUMENT_CATALOG.md`](./orf/INSTRUMENT_CATALOG.md)**: Inventory of Revenue Families, Routing Rails, and Advanced Financial Products.
- **[`orf/GOVERNANCE_RULES.md`](./orf/GOVERNANCE_RULES.md)**: The 8 Hard Gates, 5 Replenishment Ratios, Correlation Classes, and Legal Entity Architecture.
- **[`VALIDATION.md`](./VALIDATION.md)**: 4-Stage Research Validation Lifecycle & Honest Stage 0 Labelling.

### Evidence, Research & Scenarios
- **[`docs/EVIDENCE_REGISTER.md`](./docs/EVIDENCE_REGISTER.md)**: Primary-Source Precedent Audit Matrix & Transferability Ratings.
- **[`docs/PRIOR_ART_AND_COMPETITIVE_ANALYSIS.md`](./docs/PRIOR_ART_AND_COMPETITIVE_ANALYSIS.md)**: 5-Vector Deep Dives into STF, Protocol Guild, Tidelift, Project Odin, Optimism, Polkadot, and ENS.
- **[`docs/TIER_1_FEASIBILITY_MODEL.md`](./docs/TIER_1_FEASIBILITY_MODEL.md)**: Financial Scenario Model & Compound Stress Test.

### Multi-Chain Ecosystem Profiles
- **[`use-cases/CARDANO_POSM.md`](./use-cases/CARDANO_POSM.md)**: Cardano Paid Open Source Model (POSM) Precursor.
- **[`use-cases/ETHEREUM_EVM.md`](./use-cases/ETHEREUM_EVM.md)**: Protocol Guild, Project Odin, and ENS Endowment Architecture.
- **[`use-cases/OPTIMISM_SUPERCHAIN.md`](./use-cases/OPTIMISM_SUPERCHAIN.md)**: Superchain 15% Net Fee Split & OSO Impact Tracing.
- **[`use-cases/POLKADOT_OPENGOV.md`](./use-cases/POLKADOT_OPENGOV.md)**: Technical Fellowship Ranks 0–9 & PCF Legal Foundation Execution.

### Tool & Infrastructure Specifications
- **[`tools/PROJECT_ODIN.md`](./tools/PROJECT_ODIN.md)**: EF Funding Coordination & Renaissance Philanthropy DPG Incubation Lab.
- **[`tools/OPEN_SOURCE_OBSERVER.md`](./tools/OPEN_SOURCE_OBSERVER.md)**: Multi-Ecosystem BigQuery Data Warehouse & Hasura GraphQL API.
- **[`tools/DRIPS_PROTOCOL.md`](./tools/DRIPS_PROTOCOL.md)**: EVM Smart Contracts for Dependency Graph Fund Splitting (ORF Routing Rail).
- **[`tools/SUPERFLUID.md`](./tools/SUPERFLUID.md)**: Constant Flow Agreements for Real-Time Streaming Stipends (ORF Routing Rail).
- **[`tools/GRIMOIRELAB_CHAOSS.md`](./tools/GRIMOIRELAB_CHAOSS.md)**: Perceval Data Retrieval & SortingHat Identity Resolution Engine.
- **[`tools/MERIT_SYSTEMS.md`](./tools/MERIT_SYSTEMS.md)**: GitHub Commit Attribution & AgentCash x402/MPP Agentic Commerce Gateway.
- **[`tools/ANDAMIO.md`](./tools/ANDAMIO.md)**: Cardano Plutus Course Validators & Tokenized Contributor Credentials.

---

## Canonical Systems Evaluator & CLI

The repository includes a reference implementation of the **Canonical Systems Evaluator** in Python and Node.js:

```bash
# Run unit test suite
python evaluator/tests/test_evaluator.py

# Run Canonical Systems Assessment on sample configuration
python evaluator/cli/assess_ecosystem.py evaluator/examples/sample_input_config.json

# Run experimental QUAID heuristic scanner
python evaluator/cli/quaid_adapter.py intersectmbo/cardano-node
```

---

## Legal & License

All code and specifications in this repository are licensed under the **Apache License 2.0**. See [`LICENSE`](LICENSE) for details.
All contributions must include a Developer Certificate of Origin (DCO) sign-off (`git commit -s`).
