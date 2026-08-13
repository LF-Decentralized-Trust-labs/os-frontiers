# Open Source Frontiers Lab — Tool Submission Template

## Tool Name
Open Source Observer (OSO)

---

# Overview

## Summary
Open Source Observer is an open analytics platform that measures the impact of open source projects through onchain and offchain data. Built by Kariba Labs and co-founded by Carl Cervone and Raymond Cheng, OSO aggregates data from GitHub repositories, npm packages, onchain deployments, and other sources into a unified analytics layer.

## Purpose
OSO's mission is to help internet economies measure the impact of open source software contributions to the growth and adoption of their platform. Current approaches to tracking and bootstrapping economic activity aren't very effective — projects are rewarded for marketing and grant writing ability over impact, and foundations and ecosystem funds don't have the data they need to make smarter funding allocations.

## Mission Alignment
Kariba Labs is committed to being the most open and reliable source of impact metrics by embracing open source software, open data, and open infrastructure — building collaboratively rather than hoarding data in centralized infrastructure, to power the next generation of data-driven applications.

---

# Tool Classification

## Category
- [ ] Governance Tooling
- [ ] Open Source Sustainability
- [ ] Contributor Coordination
- [ ] Treasury & Funding Infrastructure
- [ ] Credentialing & Reputation
- [x] **Analytics & Observability**
- [ ] Security & Incident Response
- [ ] Developer Tooling
- [ ] Interoperability Infrastructure
- [ ] Community Operations
- [ ] Documentation & Knowledge Systems
- [ ] Lifecycle Management
- [x] **Public Goods Infrastructure**
- [ ] Compliance & Policy
- [ ] Other: ___________

## Open Source Status
- [x] **Fully Open Source**
- [ ] Source Available
- [ ] Mixed / Hybrid
- [ ] Proprietary Components

## License
Apache 2.0

---

# Ecosystem Context

## Target Ecosystems
OSO supports evaluation for Optimism's Retro Funding program, Filecoin's first RetroPGF round, and has received grants from Protocol Labs and Arbitrum.
- Optimism / Superchain (Base, Frax, Metal, Mode, PGN, Zora)
- Filecoin
- Arbitrum
- Ethereum and broader EVM ecosystems

## Intended Users
OSO serves retroactive funding programs evaluating applicants using verifiable impact metrics, badgeholders and voters making data-informed allocation decisions, project maintainers understanding their project's reach and onchain footprint, researchers and analysts querying comprehensive public datasets, and grant programs tracking portfolio performance over time.
- Grant program administrators and foundations
- DAO voters and badgeholders
- Open source project maintainers
- Impact data scientists and researchers

## Current Pain Points Addressed
OSO addresses the problem that projects are rewarded for marketing and grant writing ability over real impact, and that foundations and ecosystem funds lack the data needed to make smarter funding allocations. OSO puts all the metrics funders need in one place — including impact tracing, activity graphing, and financing estimation.

---

# Technical Information

## Repository / Source Code
[https://github.com/opensource-observer/oso](https://github.com/opensource-observer/oso)

## Documentation
[https://docs.oso.xyz](https://docs.oso.xyz) / [https://docs.opensource.observer](https://docs.opensource.observer)

## Core Technologies
OSO uses a sqlmesh pipeline to clean and normalize data into a universal event table and metrics, maintains separate Trino clusters operating over Iceberg tables, and uses Hasura to automatically generate a GraphQL API served via an Apollo Router.
- Python / sqlmesh / dbt (data pipeline)
- Google BigQuery (data warehouse)
- Dagster (orchestration)
- GraphQL / Hasura / Apollo Router (API layer)

## Architecture Overview
OSO stores all raw source data in a BigQuery data warehouse, defines sequences of transformations in its data pipeline, and builds on Google BigQuery's public datasets (including GitHub and Optimism blockchain data). The pipeline uses Dagster embedded-elt with dlt for data movement. OSO also publishes live datasets on Google BigQuery through the OSO Data Exchange, available free of charge, covering the full pipeline output, Superchain source data, Gitcoin data, and OpenRank reputation scores.

## Dependencies
- Google BigQuery (data warehouse and public data exchange)
- GitHub API (repository and contributor data)
- Onchain RPC / indexers (Superchain, Ethereum, etc.)
- Dagster (pipeline orchestration)
- Trino / Apache Iceberg

---

# Operational Model

## Governance Model
OSO operates without formal governance or a native token. Decisions are made by the Kariba Labs core team, with community input through GitHub and Discord.

## Maintenance Model
Open Source Observer is an open source public good maintained by Kariba Labs. Community contributors participate through the Kariba Data Collective.

## Funding Model
Kariba Labs is supported by generous grants from Protocol Labs, Optimism, and the Arbitrum Foundation. The project has also received a Builders Grant from Optimism and recognition at an Optimism hackathon.

## Contributor Model
OSO welcomes contributions to its repositories and runs the Kariba Data Collective for analysts and data scientists interested in becoming regular contributors. Contributors can query large amounts of OSO data via public datasets on BigQuery.

---

# Open Source Impact

## Expected Benefits
OSO enables retroactive funding programs to evaluate applicants using verifiable impact metrics rather than self-reported narratives, allows badgeholders and voters to make data-informed allocation decisions using standardized metrics, and helps grant programs track portfolio performance over time to assess the effectiveness of past funding decisions.

## Ecosystem Value
OSO's multi-chain data coverage allows grant programs across different ecosystems to use a common analytical framework, enabling comparisons and knowledge sharing across previously siloed communities.

## Risks & Limitations
- Dependency on Google BigQuery infrastructure introduces centralization risk
- The OSO API currently only allows read-only GraphQL queries against a subset of OSO data (mart models only); full dataset access requires direct BigQuery integration.
- Datasets may include material subject to third-party rights.
- Rate limits or subscription pricing may apply to API usage at scale

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
Optimism's Retro Funding program uses OSO to evaluate hundreds of applicant projects. For RetroPGF Round 4, OSO developed onchain impact metrics that measured each project's contribution to the Superchain ecosystem, including contract activity, user growth, and gas fees generated, with badgeholders using these metrics to allocate millions of dollars in OP tokens. OSO has also supported Filecoin and Arbitrum funding rounds.

## Roadmap
OSO is working toward advanced metrics to measure how specific interventions impact the public goods ecosystem, including comparing performance of projects or users who received token incentives against those who did not, using advanced statistical methods to estimate causal effects while controlling for market conditions and competing incentives.

---

# Metrics & Evaluation

## Success Metrics

| Metric | Description |
|---|---|
| Projects indexed | Number of open source projects with mapped artifacts in the OSO registry |
| Grant programs served | Number of ecosystem funding rounds using OSO data for allocation decisions |
| Active contributors tracked | GitHub developer activity aggregated across indexed projects |
| Onchain deployments mapped | Smart contracts and onchain activity linked to OSO project profiles |
| API / BigQuery queries | Volume of external data access indicating ecosystem adoption |

## Observability / Reporting
OSO orchestrates all data infrastructure using a public Dagster instance, where users can monitor all jobs and data freshness in the Dagster dashboard. Live, up-to-date datasets are published on Google BigQuery through the OSO Data Exchange, available free of charge, allowing anyone to query them directly using SQL.

---

# Alignment With Open Source Frontiers

## Relevant Focus Areas
- [x] **Open Source Sustainability**
- [ ] Decentralized Governance
- [ ] Contributor Incentives
- [ ] Treasury Coordination
- [ ] Security & Resilience
- [x] **Ecosystem Analytics**
- [ ] Lifecycle Stewardship
- [x] **Public Goods Funding**
- [x] **Cross Ecosystem Collaboration**
- [ ] Infrastructure Neutrality
- [ ] Other: ___________

## Why This Tool Fits the Lab
OSO directly addresses one of the most persistent failures in open source funding: the inability to measure real impact. By providing a neutral, open, multi-ecosystem analytics layer, OSO enables foundations, DAOs, and grant programs to fund based on verifiable contribution data rather than narrative. Its commitment to open data, open infrastructure, and open source code — combined with active deployments across Optimism, Filecoin, and Arbitrum — makes it a foundational piece of public goods infrastructure aligned with Open Source Frontiers' mission.

---

# Supporting Materials

## References
- [OSO Mission](https://docs.oso.xyz/docs/references/mission/)
- [Open Source, Open Data, Open Infra](https://docs.opensource.observer/blog/open-source-open-data-open-infra/)
- [OSO Architecture Evolution](https://docs.oso.xyz/blog/oso-architecture-evolution/)
- [Gitcoin App Profile](https://gitcoin.co/apps/opensource-observer)

## Demonstrations / Screenshots
- Live platform: [www.opensource.observer](https://www.opensource.observer)
- Public GraphQL explorer: [https://www.opensource.observer/graphql](https://www.opensource.observer/graphql)

## Related Projects
- Gitcoin / Gitcoin Passport (contributor credentialing)
- Optimism RetroPGF (primary use case)
- OSS Directory: [https://github.com/opensource-observer/oss-directory](https://github.com/opensource-observer/oss-directory)

---

# Contributor Information

## Primary Contact
- Carl Cervone — Co-founder, Kariba Labs / GitHub: [@ccerv1](https://github.com/ccerv1)
- Raymond Cheng — Co-founder, Kariba Labs / GitHub: [@ryscheng](https://github.com/ryscheng)

## Contributors
- Kariba Labs core team
- Kariba Data Collective (community analysts and data scientists)
- Open source contributors via [github.com/opensource-observer](https://github.com/opensource-observer)

## Submission Date
2026-05-21
