# Open Source Frontiers (OSF) Lab

> **Linux Foundation Decentralized Trust · Stage 0 Research Candidate**  
> *Release Candidate Edition: `v0.8.0-rc.1` · Open Source Governance & Replenishment System*  
> A **Web3** framework for who decides, how money goes out, and how money comes back. The same framework also applies to Web2 foundations, companies, and public funders.

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)
[![Docs: CC-BY-4.0](https://img.shields.io/badge/Docs-CC--BY_4.0-lightgrey.svg)](LICENSE-DOCS)
[![Release Candidate](https://img.shields.io/badge/Status-Stage_0_Research_Candidate-orange.svg)](STATUS.md)
[![DCO Signed](https://img.shields.io/badge/DCO-Signed_Commits-green.svg)](CONTRIBUTING.md)

---

## Start here

- **I run a treasury:** [`QUICKSTART_FOR_TREASURIES.md`](./QUICKSTART_FOR_TREASURIES.md)
- **I'm a maintainer:** [`docs/MAINTAINER_AUTONOMY_GUIDE.md`](./docs/MAINTAINER_AUTONOMY_GUIDE.md)
- **I'm a researcher:** [`START_HERE.md`](./START_HERE.md)

New to the terms? See [`GLOSSARY.md`](./GLOSSARY.md). Which whitepaper text controls is explained in [`whitepapers/README.md`](./whitepapers/README.md).

No [hard gate](./GLOSSARY.md#hard-gates) is marked passed. The evaluator sample's `PASSED` output is a hypothetical, not a gate. No component is past Stage 0. Current stage per component: [`STATUS.md`](./STATUS.md).

## The loop, as a page

The triangle, the closed loop, and the fifteen-indicator scorer are one page.

- Live site: <https://lf-decentralized-trust-labs.github.io/os-frontiers/>
- Scorer, on that site: <https://lf-decentralized-trust-labs.github.io/os-frontiers/#evaluator>
- Source: [`docs/index.html`](./docs/index.html)

The scorer is the same 15-indicator preview as `evaluator/preview`. A level it prints is not one of the eight hard gates.

The same page has an Ask button. It answers from the framework on the page. It does not send the question anywhere.

## Executive Summary

The **Open Source Frontiers Lab (OSF)** is a research and architectural framework built within **LF Decentralized Trust** to solve the open-source maintenance crisis. Modern digital society relies on thousands of critical open-source software libraries, yet funding has historically suffered from one-way capital outflows — short-term grants, volunteer burnout, and corporate capture. Ecosystems can spend on maintenance for years and still have no path for the value of that infrastructure to come back.

OSF synthesizes Web3 and Web2 precedents into a unified, three-piece closed-loop architecture:

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

Each framework can still be used alone. Next file for each door:

- dOSPO: [`dospo/NON_POWERS.md`](./dospo/NON_POWERS.md), then [`dospo/CHARTER.md`](./dospo/CHARTER.md)
- OMF: [`omf/PROGRAM_CHARTER_TEMPLATE.md`](./omf/PROGRAM_CHARTER_TEMPLATE.md)
- ORF: [`orf/5_QUESTION_ASSESSMENT.md`](./orf/5_QUESTION_ASSESSMENT.md)

---

## Master Document Directory & Navigation

### Master Architectural Whitepapers Series ([`whitepapers/`](./whitepapers))

- **[`whitepapers/README.md`](./whitepapers/README.md)**: Master Whitepaper Series Index, series position, and which text controls.
- **dOSPO Whitepaper**: Canonical PDF [`whitepapers/dospo-whitepaper-v1.0.pdf`](./whitepapers/dospo-whitepaper-v1.0.pdf) (March 3, 2026). Pointer: [`whitepapers/DOSPO_WHITEPAPER.md`](./whitepapers/DOSPO_WHITEPAPER.md).
- **OMF Whitepaper**: Canonical PDF [`whitepapers/open-maintenance-framework-omf-v1.0.pdf`](./whitepapers/open-maintenance-framework-omf-v1.0.pdf) (March 7, 2026). Pointer: [`whitepapers/OMF_WHITEPAPER.md`](./whitepapers/OMF_WHITEPAPER.md). Citation layer: [`whitepapers/OMF_ERRATA.md`](./whitepapers/OMF_ERRATA.md).
- **ORF Whitepaper**: Canonical text is the v1.1 manuscript [`whitepapers/orf-whitepaper-v1.1-errata-applied.md`](./whitepapers/orf-whitepaper-v1.1-errata-applied.md); the v1.1 PDF is built from it in CI. Previous edition: [`whitepapers/orf-v1.0.pdf`](./whitepapers/orf-v1.0.pdf). Stage 0. No gate is marked passed.

### Core Architectural Specifications

- **[`dospo/START_HERE.md`](./dospo/START_HERE.md)**: Decentralized OSPO Governance Specification & RACI Matrix.
- **[`omf/PROGRAM_PORTFOLIO.md`](./omf/PROGRAM_PORTFOLIO.md)**: Maintenance Program Specifications (Retainers, Bounties, Pathways, Resilience, Incubation).
- **[`orf/START_HERE.md`](./orf/START_HERE.md)**: Open Replenishment Framework Master Introduction & 5 Revenue Families.
- **[`orf/INSTRUMENT_CATALOG.md`](./orf/INSTRUMENT_CATALOG.md)**: Inventory of Revenue Families, Routing Rails, and Advanced Financial Products, rated on the [P-scale](./GLOSSARY.md) (external precedent, P0–P5) and the [D-scale](./GLOSSARY.md) (local deployment, D0–D5).
- **[`orf/GOVERNANCE_RULES.md`](./orf/GOVERNANCE_RULES.md)**: The 8 Hard Gates, Replenishment Ratios, Correlation Classes, and Legal Entity Architecture.
- **[`VALIDATION.md`](./VALIDATION.md)**: 4-Stage Research Validation Lifecycle & Honest Stage 0 Labelling. Progress per component: [`STATUS.md`](./STATUS.md).

### Evidence, Research & Scenarios

- **[`docs/EVIDENCE_REGISTER.md`](./docs/EVIDENCE_REGISTER.md)**: Primary-Source Precedent Audit Matrix & Transferability Ratings.
- **[`docs/PRIOR_ART_AND_COMPETITIVE_ANALYSIS.md`](./docs/PRIOR_ART_AND_COMPETITIVE_ANALYSIS.md)**: 5-Vector Deep Dives into STF, Protocol Guild, Tidelift, Project Odin, Optimism, Polkadot, and ENS.
- **[`docs/landscape/README.md`](./docs/landscape/README.md)**: Landscape reference section — 30 evidence profiles of public funders, corporate and security funds, routing rails, foundations, philanthropy and research groups working on open source sustainability, each mapped to dOSPO, OMF and ORF.
- **[`docs/TIER_1_FEASIBILITY_MODEL.md`](./docs/TIER_1_FEASIBILITY_MODEL.md)**: Financial Scenario Model & Compound Stress Test.
- **[`docs/SOURCES.md`](./docs/SOURCES.md)**: Source list for third-party material (URL, access date, SHA-256, archive link). Third-party copies are not stored in this repository.

### Ecosystem precedents

- **[`docs/precedents/CARDANO_POSM.md`](./docs/precedents/CARDANO_POSM.md)**: Cardano Paid Open Source Model (POSM) funding model. The Intersect POSM accelerator never launched. It was only described as intent in the scope of work.
- **[`docs/precedents/ETHEREUM_EVM.md`](./docs/precedents/ETHEREUM_EVM.md)**: Protocol Guild, Project Odin, and ENS Endowment Architecture.
- **[`docs/precedents/OPTIMISM_SUPERCHAIN.md`](./docs/precedents/OPTIMISM_SUPERCHAIN.md)**: Superchain 15% Net Fee Split & OSO Impact Tracing.
- **[`docs/precedents/POLKADOT_OPENGOV.md`](./docs/precedents/POLKADOT_OPENGOV.md)**: Technical Fellowship Ranks 0–9 & PCF Legal Foundation Execution.
- **[`docs/precedents/PROJECT_ODIN.md`](./docs/precedents/PROJECT_ODIN.md)**: Ethereum Foundation Funding Coordination and Renaissance Philanthropy incubation program. A precedent, not a rail.

### Tool & Infrastructure Specifications

- **[`tools/OPEN_SOURCE_OBSERVER.md`](./tools/OPEN_SOURCE_OBSERVER.md)**: Multi-Ecosystem BigQuery Data Warehouse & Hasura GraphQL API.
- **[`tools/DRIPS_PROTOCOL.md`](./tools/DRIPS_PROTOCOL.md)**: EVM Smart Contracts for Dependency Graph Fund Splitting (ORF Routing Rail).
- **[`tools/SUPERFLUID.md`](./tools/SUPERFLUID.md)**: Constant Flow Agreements for Real-Time Streaming Stipends (ORF Routing Rail).
- **[`tools/GRIMOIRELAB_CHAOSS.md`](./tools/GRIMOIRELAB_CHAOSS.md)**: Perceval Data Retrieval & SortingHat Identity Resolution Engine.
- **[`tools/MERIT_SYSTEMS.md`](./tools/MERIT_SYSTEMS.md)**: GitHub Commit Attribution & AgentCash x402/MPP Agentic Commerce Gateway.
- **[`tools/ANDAMIO.md`](./tools/ANDAMIO.md)**: Cardano Plutus Course Validators & Tokenized Contributor Credentials.

### Community & Governance

- **[`GOVERNANCE.md`](./GOVERNANCE.md)**: How maintainers join, leave and are replaced; decisions and conflicts of interest.
- **[`MAINTAINERS.md`](./MAINTAINERS.md)** · **[`AUTHORS.md`](./AUTHORS.md)** · **[`CONTRIBUTING.md`](./CONTRIBUTING.md)** · **[`CODE_OF_CONDUCT.md`](./CODE_OF_CONDUCT.md)** · **[`SECURITY.md`](./SECURITY.md)**
- **[`docs/CALL_FOR_PILOTS.md`](./docs/CALL_FOR_PILOTS.md)**: Call for pilot ecosystems.

---

## Canonical Systems Evaluator & CLI

The repository includes a reference implementation of the **Canonical Systems Evaluator** in Python and Node.js:

```bash
# Run the test suite (indicators, hard gates, schema, QUAID fixture)
python3 -m unittest discover -s evaluator/tests

# Run Canonical Systems Assessment on sample configuration
python3 evaluator/cli/assess_ecosystem.py evaluator/examples/sample_input_config.json

# Run experimental QUAID heuristic scanner (calls the GitHub API; add --fixture <file> to stay offline)
python3 evaluator/cli/quaid_adapter.py intersectmbo/cardano-node
```

The `PASSED` line from that sample is a hypothetical. It does not pass a gate.

Local scorer preview, opened from its own folder: [`evaluator/preview/index.html`](./evaluator/preview/index.html), with [`evaluator/preview/app.js`](./evaluator/preview/app.js) and [`evaluator/preview/style.css`](./evaluator/preview/style.css). The published version is on the [live site](https://lf-decentralized-trust-labs.github.io/os-frontiers/#evaluator).

---

## Legal & License

Code in this repository is licensed under the **Apache License 2.0** ([`LICENSE`](LICENSE)). Documentation is licensed under **CC-BY-4.0** ([`LICENSE-DOCS`](LICENSE-DOCS)).
All contributions must include a Developer Certificate of Origin (DCO) sign-off (`git commit -s`).
