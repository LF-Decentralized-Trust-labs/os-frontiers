Now I have a thorough picture of Merit Systems. Here is the completed template:

---

# Open Source Frontiers Lab — Tool Submission Template

## Tool Name
Merit Systems

---

# Overview

## Summary
Merit Systems is building a new economy for open source. Merit adds rich attribution information to software version control systems like GitHub, allowing capital sources to route funds to codebases and incentivize builders directly. Tying this capital to impact creates a dynamic market where innovation thrives and builders flourish. The company's product suite spans two layers: the **Terminal**, a contributor payments interface for open source maintainers, and **AgentCash**, an agentic commerce layer enabling AI agents to autonomously discover and pay for APIs using open payment protocols.

## Purpose
Merit Systems addresses the crisis in open source funding. Although open source software underpins 95% of commercial software, funding its development has been a perennial challenge. The venture ecosystem demands exponential returns that don't match most open source projects, while Big Tech subsidizes "free" software as a strategy to commoditize their complements — distorting market signals and stripping pricing power from sustainable alternatives. Developers face a stark choice: burn out or find a benefactor.

## Mission Alignment
Merit Systems envisions a new commons where market forces, not subsidies, guide innovation; value creators capture a sustainable share through direct monetization; ideas and expertise flow freely across organizational boundaries; and long-term work captures its future value.

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

> *Note: Merit builds on and contributes to open payment standards (x402, MPP). The Terminal and AgentCash products are proprietary; the underlying payment protocol infrastructure is open.*

## License
Not publicly specified; proprietary commercial products built atop open standards (x402 / MPP)

---

# Ecosystem Context

## Target Ecosystems
- GitHub-native open source projects across all languages and domains
- The x402 and MPP (Machine Payments Protocol) agentic commerce ecosystems
- Base / Ethereum (stablecoin settlement layer)
- AI agent runtimes: Claude, Codex, Cursor, Gemini CLI

## Intended Users
- Open source project maintainers seeking to pay contributors
- Foundations and sponsors routing capital to repos
- Developers building AI agents that need to consume paid APIs
- API providers wanting to monetize services to autonomous agents

## Current Pain Points Addressed
Friction still exists in the open source ecosystem: it's hard for projects to understand the impact of their contributors, challenging to find payment models that work for the industry, and if you do want to monetize, the administrative burdens are numerous — taxes, payroll, and incorporation. On the agentic side, AI tools like Claude, Cursor, and Codex previously could not buy data and services on behalf of users — agents needed account creation, API keys, and subscriptions before they could pay for a service.

---

# Technical Information

## Repository / Source Code
[https://github.com/merit-systems](https://github.com/merit-systems)

## Documentation
- Terminal: [https://terminal.merit.systems](https://terminal.merit.systems)
- AgentCash: [https://agentcash.dev/docs](https://agentcash.dev/docs)

## Core Technologies
- Stablecoins for instant global payouts, with end-to-end tax management
- x402 (HTTP 402-based open payment protocol, co-developed with Coinbase / x402 Foundation)
- MPP — Machine Payments Protocol (co-developed with Tempo + Stripe)
- GitHub API (contribution attribution and repo analytics)
- Base blockchain (primary stablecoin settlement layer — USDC)

## Architecture Overview
Merit Systems operates two distinct product layers:

**Terminal** — A new interface for anyone building software in the open to surface and pay high-impact contributors. Projects have a simple way to pay open source developers directly based on their contributions to a repo, using stablecoins for instant global payouts, with Merit managing all taxes end-to-end.

**AgentCash** — A single balance providing access to every API on the internet. When an agent gets blocked by a paywall, it can reach for thousands of APIs, spend pennies, and proceed. AgentCash bundles payment and merchant discovery — merchants register their servers on x402scan.com or mppscan.com and are instantly exposed to all AgentCash agents.

## Dependencies
- GitHub (source of contribution data and identity)
- Base / Ethereum (onchain stablecoin settlement)
- x402 and MPP protocol standards
- USDC (Circle) for payment denomination
- MCP (Model Context Protocol) for agent tool integration

---

# Operational Model

## Governance Model
Merit Systems was founded by Sam Ragsdale, Ryan Sproule, and Mason Hall, built in Brooklyn, NY. Privately held; governance is internal to the company. Payment protocol work (x402) is governed externally by the x402 Foundation (Coinbase, Cloudflare, and partners).

## Maintenance Model
Core products (Terminal, AgentCash) are maintained by the Merit Systems team. Protocol-level contributions flow back into the open x402 and MPP standards. Merit is actively hiring developers.

## Funding Model
Merit Systems raised $10M from a16z crypto, Blockchain Capital, and industry-leading angels to build a new economy for open source. Revenue model is expected to include payment processing fees and API gateway margins through AgentCash.

## Contributor Model
Open source attribution via GitHub PRs drives payment allocation in the Terminal. Maintainers can choose to focus on longtime contributors with months or years of PR history, or use Merit to pay a longer tail of developers who have recently merged PRs. External developer contributions to the open protocol layer (x402, MPP) are community-governed.

---

# Open Source Impact

## Expected Benefits
Projects now have a simple way to pay open source developers directly based on their contributions to a repo — flexible for all kinds of open-source projects, from enduring infrastructure to teams that haven't yet incorporated. On the agentic side, open payment protocols eliminate gatekeeping from agent-to-API commerce: an agent that can only buy from pre-approved merchants is an employee with a corporate card restricted to three vendors; an agent with open protocols is an entrepreneur with a bank account.

## Ecosystem Value
Open Agentic Commerce — powered by open standards like x402 and MPP — means no BD process, no whitelist, just simple permissionless standards. Agents can discover an API, read its schema, and use it correctly without any prior training, composing capabilities at unprecedented scale. For open source specifically, Merit enables market-rate compensation to flow directly to contributors without corporate intermediaries.

## Risks & Limitations
- Proprietary product layer atop open protocols creates dependency on a single commercial entity for key UX and distribution
- Stablecoin/crypto payment rails may face regulatory headwinds in key jurisdictions
- Contributor payment model requires project-level revenue or sponsorship to function — projects with no funding still cannot pay contributors
- Early-stage: adoption, tooling maturity, and long-term sustainability are unproven at scale
- Tax and compliance management is handled by Merit — creates a single point of failure for payout infrastructure

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
Agents have made 770,000+ paid tool calls on AgentCash. API partners include Minerva, Parallel, Nansen, and Zapper. AgentCash launched in March 2026 and had 2,000+ agents accessing its ecosystem within days of launch. The Terminal is available to all GitHub users with a limited payments beta cohort.

## Roadmap
- Expand AgentCash API catalog (280+ tier-1 APIs including LinkedIn, Instagram, Reddit, image/video generation, travel)
- Poncho — a consumer product described as making the one-person team unstoppable, currently in development
- Continued expansion of x402 / MPP protocol support across new blockchains and settlement layers
- Growth of merchant discovery infrastructure (x402scan, MPPscan)

---

# Metrics & Evaluation

## Success Metrics

| Metric | Description |
|---|---|
| Paid tool calls | Total agent-initiated API transactions through AgentCash (770k+ as of launch) |
| APIs available | Number of API routes accessible through the AgentCash marketplace |
| Contributors paid | Open source developers who have received payments via the Terminal |
| Repos integrated | GitHub repositories with Merit Terminal installed |
| Merchant registrations | API providers registered on x402scan / mppscan for agent discovery |

## Observability / Reporting
- [x402scan.com](https://x402scan.com) — live registry and explorer for x402-enabled services
- [mppscan.com](https://mppscan.com) — live registry and explorer for MPP-enabled services
- AgentCash dashboard with balance, spend history, and API usage per agent

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
Merit Systems is one of the most direct attempts to solve the root economic problem of open source: the disconnect between value created and value captured by builders. Where most tools in this space measure health or coordinate governance, Merit goes a layer deeper — routing actual capital to contributors based on verifiable attribution. Its dual focus on the Terminal (human contributor payments) and AgentCash (AI agent payments) positions it at the intersection of two critical transitions: the shift from volunteer-driven to market-compensated open source, and the emergence of agentic commerce as a new monetization layer for the open internet. Both are central to the long-term resilience of open source ecosystems.

---

# Supporting Materials

## References
- [Announcing Merit Systems — $10M Seed Round](https://merit.systems/blog/fundraise)
- [Open Source Capitalism — Company Manifesto](https://merit.systems/blog/manifesto)
- [Launching the Terminal](https://merit.systems/blog/launch)
- [The Age of Open Agentic Commerce](https://merit.systems/blog/open-agentic-commerce)

## Demonstrations / Screenshots
- Terminal: [https://terminal.merit.systems](https://terminal.merit.systems)
- AgentCash: [https://agentcash.dev](https://agentcash.dev)
- x402 ecosystem explorer: [https://x402scan.com](https://x402scan.com)
- MPP ecosystem explorer: [https://mppscan.com](https://mppscan.com)

## Related Projects
- [x402 Foundation](https://x402.org) — open payment protocol (Coinbase, Cloudflare)
- [MPP / Machine Payments Protocol](https://mpp.dev) — open payment protocol (Tempo, Stripe)
- [Poncho](https://tryponcho.com) — Merit's consumer agent product

---

# Contributor Information

## Primary Contact
- Sam Ragsdale — Founder & CEO / [@samrags\_](https://x.com/samrags_)
- Ryan Sproule — Co-founder
- Mason Hall — Co-founder
- Twitter/X: [@merit\_systems](https://x.com/merit_systems)

## Contributors
- Merit Systems core team (Brooklyn, NY)
- x402 Foundation ecosystem contributors
- AgentCash API partner network

## Submission Date
2026-05-21
