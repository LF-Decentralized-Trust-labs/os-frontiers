# Tool Profile: Open Source Observer (OSO)

> **LF Decentralized Trust · Open Source Frontiers Lab Profile**  
> *Metadata: `observed_at: 2026-08-13` · `evidence_status: Live Production Infrastructure`*

---

## 1. Intent & Philosophical Problem Statement
Open Source Observer (OSO) was created by Kariba Labs (co-founded by Carl Cervone and Raymond Cheng) to solve the core data deficit in public-goods funding. Historically, ecosystem foundations, DAOs, and grant committees allocated capital based on self-reported narratives, grant-writing charisma, or social media follower counts rather than verifiable technical impact. OSO was designed to provide a completely open, multi-ecosystem analytics infrastructure that measures real open-source impact across on-chain deployments and off-chain code repositories.

## 2. Detailed Operational & Technical Mechanics
OSO operates an open data architecture built on top of Google BigQuery, Trino, and Apache Iceberg. Its data pipeline uses `sqlmesh` and Dagster to aggregate raw event data from GitHub repositories, npm/PyPI registries, contract deployment logs across EVM chains (Optimism, Base, Arbitrum, Filecoin), and governance platforms. OSO cleans and normalizes these disparate data streams into universal event tables and mart models, exposing them via a public GraphQL API (Hasura / Apollo Router) and direct SQL queries via the OSO Data Exchange on BigQuery.

## 3. Empirical Achievements & Demonstrated Traction
OSO serves as the primary analytics engine for major Web3 funding programs, including Optimism's RetroFunding (Rounds 3 and 4), Filecoin's RetroPGF, and Arbitrum Foundation rounds. OSO has mapped and indexed over 1,000+ open-source projects, tracking developer retention, commit frequencies, active maintainers, dependency graphs, and multi-chain gas generation across the Superchain.

## 4. Structural Limitations, Trade-offs & Failure Modes
OSO's reliance on Google BigQuery for data warehousing introduces underlying infrastructure centralization risks. Furthermore, its GraphQL API currently exposes read-only access to mart models, requiring direct BigQuery integration for full raw dataset querying. Additionally, mapping off-chain GitHub identities to on-chain smart contract deployments requires ongoing manual registry verification to prevent misattribution or gaming by sybil applicants.

## 5. Program Relevance & Direct dOSPO / OMF / ORF Evaluation
- **dOSPO Evaluation**: Serves as the primary data feed for dOSPO transparency reporting — allowing governance bodies to verify maintainer activity, dependency depth, and organizational independence before approving maintainer retainer budgets.
- **OMF Evaluation**: Directly powers **OMF Program 6 (Resilience Programs)** in [`omf/PROGRAM_PORTFOLIO.md`](../omf/PROGRAM_PORTFOLIO.md). OMF Operators use OSO metrics (prevalence, bus factor, commit churn) to identify critical single-maintainer dependencies and trigger automated succession interventions.
- **ORF Evaluation**: Feeds the **Canonical Systems Evaluator** ([`evaluator/README.md`](../evaluator/README.md)), providing objective, multi-chain impact data to verify ecosystem health scores and calculate level-3 hard gate compliance.

---

## Primary References & Links
- **Website**: [https://www.opensource.observer/](https://www.opensource.observer/)
- **Documentation**: [https://docs.oso.xyz](https://docs.oso.xyz)
- **Source Code**: [https://github.com/opensource-observer/oso](https://github.com/opensource-observer/oso)
