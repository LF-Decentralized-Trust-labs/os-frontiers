# Open Source Frontiers Lab — Tool Submission Template

## Tool Name
Drips Protocol (drips.network)

---

# Overview

## Summary
Drips Protocol ([https://drips.network](https://drips.network)) is an EVM and Filecoin smart contract protocol that enables open-source projects to receive continuous streaming funds and automatically cascade incoming revenue down their dependency graph in real time. Built by the Radicle / Monadic US software ecosystem, Drips provides continuous token streaming, recurring project subscriptions, and automated recursive dependency splitting.

## Purpose
Drips addresses the nested open-source dependency distribution crisis. When an open-source framework or dApp receives a grant or enterprise payment, that capital historically stops at the top-level repository maintainer. The hundreds of underlying library dependencies (e.g. `ethers.js`, `wagmi`, `tokio`) that make the top-level software possible receive zero financial benefit. Drips enables top-level projects to register on-chain dependency split rules, automatically routing pre-set percentages of incoming revenue to upstream maintainers.

## Mission Alignment
Drips aligns with the Open Source Frontiers mission by creating open, custody-free, transparent funding distribution rails that strengthen software supply-chain resilience without central corporate brokers.

---

# Tool Classification

## Category
- [ ] Governance Tooling
- [x] Open Source Sustainability
- [x] Contributor Coordination
- [x] Treasury & Funding Infrastructure
- [ ] Credentialing & Reputation
- [ ] Analytics & Observability
- [ ] Security & Incident Response
- [ ] Developer Tooling
- [x] Interoperability Infrastructure
- [ ] Community Operations
- [ ] Documentation & Knowledge Systems
- [ ] Lifecycle Management
- [x] Public Goods Infrastructure
- [ ] Compliance & Policy
- [ ] Other: ___________

## Open Source Status
- [x] Fully Open Source
- [ ] Source Available
- [ ] Mixed / Hybrid
- [ ] Proprietary Components

## License
GNU General Public License v3.0 (GPL-3.0)

---

# Ecosystem Context

## Target Ecosystems
- Ethereum Mainnet & EVM Layer-2s (OP Mainnet, Arbitrum, Base)
- Filecoin network
- Open-source developer communities across JavaScript, Rust, Python, and Solidity

## Intended Users
- Open-source package maintainers setting up dependency split streams
- Grants committees and DAO treasuries streaming public-goods funds
- Commercial dApps pledging continuous revenue streams to their software supply chain
- Individual supporters creating continuous per-second micro-donations

## Current Pain Points Addressed
Drips solves the inability to fund deep software supply chains. It eliminates manual invoice processing, replaces episodic one-shot grants with continuous per-second streams, and automates multi-recipient revenue sharing without requiring intermediate corporate brokers.

---

# Technical Information

## Repository / Source Code
[https://github.com/radicle-dev/drips-contracts](https://github.com/radicle-dev/drips-contracts)

## Documentation
[https://docs.drips.network](https://docs.drips.network)

## Core Technologies
- Solidity (smart contract engine)
- EIP-712 / ERC-20 (token streaming standards)
- Subgraph / Goldsky (data indexing layer)
- TypeScript / React (Drips web app front-end)

## Architecture Overview
Drips operates through a central `DripsHub` smart contract deployed across supported chains. Senders deposit ERC-20 tokens into `DripsHub` and configure a streaming rate (tokens per second) to target recipient wallet addresses. Recipients configure a `SplitsReceiver` array containing wallet addresses and percentage allocations for their upstream dependencies. When streams arrive at a recipient, the `DripsHub` contract executes recursive distribution logic, automatically allocating fractions of the incoming stream to upstream dependencies per second.

## Dependencies
- EVM-compatible execution layer
- ERC-20 token contracts (USDC, WETH, DAI, OP)
- Subgraph indexers for frontend state management

---

# Operational Model

## Governance Model
Drips protocol contracts are immutable or governed by open-source maintainers within the Radicle ecosystem. Protocol rules operate without centralized admin keys or corporate gatekeepers.

## Maintenance Model
Maintained by Monadic US and the open-source Radicle / Drips contributor collective via public GitHub repositories.

## Funding Model
Initial development funded via Radicle ecosystem grants, public-goods allocations, and protocol foundation backing. Operates as zero-fee public infrastructure for open-source maintainers.

## Contributor Model
Open-source contribution model via GitHub issues and pull requests. Protocol SDKs and frontend interfaces are open for community integration.

---

# Open Source Impact

## Expected Benefits
- Automated, recursive dependency graph funding for deep software supply chains
- Gas-efficient continuous per-second streaming for maintainer retainers
- Elimination of manual grant application cycles for upstream dependency authors
- Transparent, audit-able on-chain distribution history

## Ecosystem Value
Drips allows multi-million dollar grants or commercial SLA payments to cascade across hundreds of open-source projects automatically, multiplying the ecosystem impact of every dollar funded.

## Risks & Limitations
- Maintainers must manually configure and update their on-chain dependency split arrays.
- Senders must maintain sufficient ERC-20 balance in `DripsHub` to prevent stream exhaustion.
- Does not generate native commercial revenue — relies on external SLAs, grants, or protocol fee splits to feed the distribution network.

---

# Adoption & Maturity

## Current Lifecycle Stage
- [ ] Concept
- [ ] Prototype
- [ ] Alpha
- [ ] Beta
- [x] Production
- [ ] Mature

## Current Adoption
Deployed across Ethereum, OP Mainnet, and Filecoin. Used by leading Web3 infrastructure projects, Protocol Labs, and open-source maintainers to distribute continuous funding streams down their software supply chain.

## Roadmap
Expanding multi-chain deployment, integrating automated GitHub dependency tree scanning via Open Source Observer, and implementing cross-chain streaming bridges.

---

# Metrics & Evaluation

## Success Metrics

| Metric | Description |
|---|---|
| Active Streams | Total continuous per-second token streams managed by DripsHub |
| Streaming Volume | Cumulative USD value streamed across supported EVM networks |
| Dependency Splits Configured | Number of open-source projects with registered upstream split arrays |
| Upstream Beneficiaries | Unique maintainer wallets receiving cascaded dependency funds |

## Observability / Reporting
On-chain stream balances and split configurations are queryable via public GraphQL subgraphs and visual dashboards at `drips.network`.

---

# Alignment With Open Source Frontiers

## Relevant Focus Areas
- [x] Open Source Sustainability
- [ ] Decentralized Governance
- [x] Contributor Incentives
- [x] Treasury Coordination
- [ ] Security & Resilience
- [ ] Ecosystem Analytics
- [x] Lifecycle Stewardship
- [x] Public Goods Funding
- [x] Cross Ecosystem Collaboration
- [x] Infrastructure Neutrality
- [ ] Other: ___________

## Why This Tool Fits the Lab
Drips Protocol provides the primary distribution primitive for dependency-directed open-source funding. Its ability to automate recursive fund splitting down software dependency trees makes it an essential operational component for Web3 public-goods sustainability.

## Program Relevance & Direct OSF Alignment

### 1. ORF Dependency-Directed Revenue Share
- **OSF Mapping**: **ORF Layer 2 (Application & Service Layer)** & **[`INSTRUMENT_CATALOG.md`](../orf/INSTRUMENT_CATALOG.md)**.
- **Mechanism Validated**: Proves that open-source projects can automatically pass a portion of their incoming commercial SLA or grant revenue down their dependency graph using smart contracts.
- **Operator Takeaway**: An ORF Operator utilizes Drips Protocol contracts to execute automated dependency-graph revenue splits whenever enterprise SLA payments or dApp certification fees are received.

### 2. OMF Retainer Disbursement Infrastructure
- **OSF Mapping**: **OMF Program 1 (Maintainer Retainers)** & **Superfluid/Drips Streaming**.
- **Mechanism Validated**: Demonstrates real-time, custody-free streaming for maintainer stipends across multi-chain EVM environments.
- **Operator Takeaway**: OMF Retainers leverage Drips streaming rails to disburse monthly maintainer retainers continuously per second, eliminating monthly invoice processing.

---

# Supporting Materials

## References
- Drips Website: https://drips.network
- Drips Protocol Documentation: https://docs.drips.network
- Radicle Ecosystem Overview: https://radicle.xyz

## Demonstrations / Screenshots
- Live platform: https://drips.network
- Drips App Explorer: https://app.drips.network

## Related Projects
- Superfluid (streaming protocol primitive)
- Open Source Observer (dependency data integration)
- Protocol Guild (maintainer retainer model)

---

# Contributor Information

## Primary Contact
- Monadic US / Drips Development Team — GitHub: [@radicle-dev](https://github.com/radicle-dev)

## Contributors
- Monadic US core engineering team
- Radicle ecosystem contributors

## Submission Date
2026-08-18
