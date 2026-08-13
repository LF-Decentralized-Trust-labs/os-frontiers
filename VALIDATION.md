# Open Source Frontiers Framework Validation Lifecycle (`VALIDATION.md`)

> **Formal Validation Framework, Maturity Lifecycle & Peer Review Process**  
> *LF Decentralized Trust · Open Source Frontiers Lab*

---

## 1. Validation Lifecycle Stages

To ensure transparent, defensible progress from research concepts to operational deployment, all frameworks, collection instruments, and evaluation tools in this repository move through four distinct maturity stages:

```
[ Stage 0: Research Candidate ] ──> [ Stage 1: Peer Reviewed ] ──> [ Stage 2: Piloted ] ──> [ Stage 3: Validated ]
```

| Stage | Classification | Definition & Acceptance Criteria | Current Status |
|---|---|---|---|
| **Stage 0** | **Research Candidate** | Theoretical specification or pro-forma model authored and published in repo. | **Current Baseline (v0.8-RC)** |
| **Stage 1** | **Peer Reviewed** | Evaluated and critiqued by at least 2 independent external reviewers or OSPO leaders. | Target Stage |
| **Stage 2** | **Piloted** | Deployed in an active Web3 ecosystem (e.g. Cardano POSM, Optimism Superchain, Polkadot OpenGov) for 6+ months. | Active Pilot (Cardano POSM) |
| **Stage 3** | **Validated** | Empirical production data confirms net replenishment ratio $\ge 1.0$ and maintainer retainers sustained across market cycles. | Production Goal |

---

## 2. Auditable Framework Pilot Register

| Artifact / Module | Lifecycle Stage | Ecosystem Pilot | Pilot Start | Duration | Reference Link & Evidence | Pilot Outcome & Summary |
|---|---|---|---|---|---|---|
| **dOSPO Framework** | Stage 2 (Piloted) | Cardano (Intersect MBO) | Jan 2024 | 18+ Months | [Intersect Open Source Committee Charter](https://intersectmbo.org) | Established community-mandated governance committee & technical steering committee for open-source roadmap. |
| **OMF Framework** | Stage 2 (Piloted) | Cardano POSM Pilot | Jun 2024 | 12+ Months | [`use-cases/CARDANO_POSM.md`](./use-cases/CARDANO_POSM.md) | Funded 12 core Haskell client maintainers under 12-month retainers. Reduced maintainer turnover. |
| **ORF Framework** | Stage 0 (Research Candidate) | LF Decentralized Trust Lab | Jul 2026 | Candidate | [`docs/TIER_1_FEASIBILITY_MODEL.md`](./docs/TIER_1_FEASIBILITY_MODEL.md) | Formulated 20+ collection instruments; Tier 1 Feasibility Scenario Model demonstrates 1.14x coverage potential. |
| **QUAID Assessor Adapter** | Stage 1 (Peer Reviewed) | QUAID Scanner Community | May 2026 | Active | [quaid/quaid-scanner](https://github.com/quaid/quaid-scanner) | Integrated 5-pillar security & governance audit engine; tested on `intersectmbo/cardano-node`. |

---

## 3. How to Submit External Validation & Review

We invite independent OSPO managers, economists, smart contract auditors, and DAO governance researchers to submit validation feedback, pilot evidence, or peer reviews via GitHub Pull Requests or Discussions.
