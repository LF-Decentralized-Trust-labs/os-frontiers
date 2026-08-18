# Tool Profile: Merit Systems

> **LF Decentralized Trust · Open Source Frontiers Lab Profile**  
> *Metadata: `observed_at: 2026-08-13` · `evidence_status: Live Beta Tooling & Agentic Protocol`*

---

# Overview

## Summary
**Merit Systems** ([https://merit.systems](https://merit.systems)) is building a new economic layer for open-source software. Merit enriches version control systems like GitHub with direct attribution data, allowing capital sources to route funds to codebases and builders based on verifiable contributions. Founded by Sam Ragsdale, Ryan Sproule, and Mason Hall, Merit's product suite spans two primary layers: the **Terminal**, a contributor payments interface for open-source maintainers, and **AgentCash**, an agentic commerce layer enabling AI agents (Claude, Codex, Cursor) to autonomously discover and pay for APIs using open payment protocols (x402 / MPP).

## Purpose
Merit Systems addresses the root economic crisis in open-source funding. Although open-source software underpins 95% of commercial software, funding its development has historically relied on episodic grants, venture capital (which demands inappropriate equity returns), or big-tech corporate subsidies. Merit enables market forces to guide innovation by routing direct stablecoin capital to maintainers based on merged PRs, code reviews, and commit history.

## Mission Alignment
Merit Systems aligns with the Open Source Frontiers mission by creating frictionless payment primitives for human maintainer payouts and establishing open payment protocol gateways (x402/MPP) for autonomous agentic commerce.

---

# Tool Classification

## Category
- [ ] Governance Tooling
- [x] **Open Source Sustainability**
- [x] **Contributor Coordination**
- [x] **Treasury & Funding Infrastructure**
- [ ] Credentialing & Reputation
- [ ] Analytics & Observability
- [ ] Security & Incident Response
- [ ] Developer Tooling
- [x] **Interoperability Infrastructure**
- [ ] Community Operations
- [ ] Documentation & Knowledge Systems
- [ ] Lifecycle Management
- [x] **Public Goods Infrastructure**
- [ ] Compliance & Policy
- [ ] Other: ___________

## Open Source Status
- [ ] Fully Open Source
- [ ] Source Available
- [x] **Mixed / Hybrid**
- [ ] Proprietary Components

> *Note: Built on open payment protocol standards (x402, MPP). Terminal and AgentCash UIs are proprietary commercial products.*

## License
Proprietary UI built atop open standards (x402 Foundation / MPP Open Standards)

---

# Ecosystem Context

## Target Ecosystems
- GitHub-native open-source repositories across all programming languages
- The x402 and MPP (Machine Payments Protocol) agentic commerce networks
- Base / Ethereum (USDC stablecoin settlement layer)
- Autonomous AI agent runtimes (Claude, Cursor, Codex, Gemini CLI)

## Intended Users
- Open-source project maintainers paying contributors via commit attribution
- Ecosystem foundations and sponsors routing grant capital directly to repositories
- Developers building AI agents that require paywalled API access
- API providers monetizing services for autonomous agent consumption

## Current Pain Points Addressed
Eliminates administrative friction in maintainer payroll (managing global taxes, W-8/W-9 compliance, and incorporation overhead) and enables autonomous AI agents to pay micro-fees for web APIs without pre-configured corporate credit cards or manual whitelisting.

---

# Technical Information

## Repository / Source Code
[https://github.com/merit-systems](https://github.com/merit-systems)

## Documentation
[https://terminal.merit.systems](https://terminal.merit.systems) / [https://agentcash.dev/docs](https://agentcash.dev/docs)

## Core Technologies
- x402 (HTTP 402 Payment Required open protocol co-developed with Coinbase / x402 Foundation)
- MPP (Machine Payments Protocol co-developed with Tempo + Stripe)
- GitHub REST / GraphQL APIs (contribution attribution & repository analytics)
- Base blockchain (USDC stablecoin settlement layer)
- MCP (Model Context Protocol for AI agent tool integration)

## Architecture Overview
Merit Systems operates across two technical product layers:
1. **Terminal**: An interface for open-source maintainers that maps pull requests, code reviews, and commit contributions to developer wallets, executing instant USDC payouts on Base while managing end-to-end tax compliance.
2. **AgentCash**: A single-balance wallet providing AI agents with instant access to paywalled APIs. When an agent hits an HTTP 402 paywall, AgentCash spends micro-pennies via x402/MPP protocols, letting agents execute tools seamlessly. Merchants register servers on `x402scan.com` or `mppscan.com`.

## Dependencies
- GitHub (source of contribution data and developer identity)
- Base / Ethereum blockchain (USDC settlement layer)
- x402 and MPP open payment protocol standards
- Circle USDC smart contracts

---

# Operational Model

## Governance Model
Merit Systems is a private company based in Brooklyn, NY. Payment protocol standards (x402) are governed independently by the x402 Foundation (Coinbase, Cloudflare, and partners).

## Maintenance Model
Terminal and AgentCash products are maintained by the Merit Systems engineering team. Protocol contributions flow back into open x402/MPP standards.

## Funding Model
Raised $10,000,000 in seed funding led by a16z crypto, Blockchain Capital, and industry angels. Revenue model includes payment gateway fees and API routing margins.

## Contributor Model
Open-source contribution attribution via GitHub PRs drives payout allocations in Terminal. Open protocol contributions (x402, MPP) are community-governed.

---

# Open Source Impact

## Expected Benefits
- Direct, frictionless commit-attribution payouts to human open-source maintainers
- End-to-end tax management (W-8/W-9) for global open-source developer compensation
- Permissionless, open payment rails (x402/MPP) for autonomous agentic commerce
- Monetization layer for ecosystem developer APIs serving AI agents

## Ecosystem Value
Merit connects open-source contribution metrics directly to financial compensation, while establishing open payment standards that let AI agents become economic actors in the public-goods ecosystem.

## Risks & Limitations
- Terminal and AgentCash UIs operate as proprietary commercial offerings built atop open protocols.
- Payout mechanics depend on stablecoin rails (USDC on Base), exposing the protocol to regional crypto regulatory policies.
- Terminal requires incoming capital (grant budgets, enterprise sponsorships) — it routes capital efficiently but cannot create project funding out of thin air.

---

# Adoption & Maturity

## Current Lifecycle Stage
- [ ] Concept
- [ ] Prototype
- [ ] Alpha
- [x] **Beta**
- [ ] Production
- [ ] Mature

## Current Adoption
AgentCash launched in March 2026, processing over 770,000 paid agentic API tool calls across 2,000+ autonomous AI agents within days of launch. API partners include Minerva, Parallel, Nansen, and Zapper. The Terminal is active in a payments beta for GitHub repositories.

## Roadmap
Expanding AgentCash API marketplace catalog (280+ tier-1 APIs), launching consumer agent products (Poncho), and expanding x402/MPP protocol support across new blockchains.

---

# Metrics & Evaluation

## Success Metrics

| Metric | Description |
|---|---|
| Paid Tool Calls | Total autonomous AI agent API transactions processed via AgentCash (770k+ at launch) |
| Active API Partners | Number of API providers registered on x402scan / mppscan |
| Terminal Payout Volume | USD value disbursed to open-source contributors based on GitHub PR attribution |
| Repositories Integrated | Open-source GitHub repositories using Merit Terminal for maintainer payouts |

## Observability / Reporting
Live dataset registries on `x402scan.com` and `mppscan.com`, with real-time agent spend history dashboards at `agentcash.dev`.

---

# Alignment With Open Source Frontiers

## Relevant Focus Areas
- [x] **Open Source Sustainability**
- [ ] Decentralized Governance
- [x] **Contributor Incentives**
- [x] **Treasury Coordination**
- [ ] Security & Resilience
- [ ] Ecosystem Analytics
- [ ] Lifecycle Stewardship
- [x] **Public Goods Funding**
- [x] **Cross Ecosystem Collaboration**
- [x] **Infrastructure Neutrality**
- [ ] Other: ___________

## Why This Tool Fits the Lab
Merit Systems provides crucial payment primitives for human maintainer commit payouts and autonomous AI agentic micro-transactions.

## Program Relevance & Direct OSF Alignment

### 1. OMF Automated Contributor Payouts (Terminal Integration)
- **OSF Mapping**: **OMF Program 2 (Code Bounties)** & **Program 1 (Maintainer Retainers)**.
- **Mechanism Validated**: Validates direct GitHub commit-attribution payouts using automated stablecoin rails (USDC on Base), eliminating manual payroll overhead for un-incorporated open-source maintainer teams.
- **Operator Takeaway**: An OMF Operator integrates Merit Terminal rails to execute instant milestone payouts to secondary contributors based on merged pull requests.

### 2. ORF Autonomous Agentic Revenue Inflows (AgentCash / HTTP 402)
- **OSF Mapping**: **ORF Layer 2 (Application & Service Layer)** & **[`INSTRUMENT_CATALOG.md`](../orf/INSTRUMENT_CATALOG.md)**.
- **Mechanism Validated**: Proves that autonomous AI agents can query, negotiate, and pay micro-fees for API services using open payment standards (x402 / MPP).
- **Operator Takeaway**: An ORF Operator configures x402/MPP payment gateways on ecosystem developer APIs (e.g. RPC nodes, indexers, vulnerability scanners), capturing agentic micro-transaction fees to replenish the ecosystem treasury.

---

# Supporting Materials

## References
- Merit Systems Website: https://merit.systems
- Terminal App: https://terminal.merit.systems
- AgentCash Platform: https://agentcash.dev
- x402 Foundation: https://x402.org

## Demonstrations / Screenshots
- Terminal: https://terminal.merit.systems
- AgentCash: https://agentcash.dev
- x402 Registry: https://x402scan.com

## Related Projects
- Coinbase x402 Payment Protocol
- Tempo / Stripe Machine Payments Protocol (MPP)
- Open Source Observer

---

# Contributor Information

## Primary Contact
- Sam Ragsdale — Founder & CEO / Twitter: [@samrags\_](https://x.com/samrags_)
- Merit Systems Team — Brooklyn, NY

## Contributors
- Merit Systems core engineering team
- x402 Foundation ecosystem contributors

## Submission Date
2026-08-18
