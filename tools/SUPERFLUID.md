# Open Source Frontiers Lab — Tool Submission Template

## Tool Name
Superfluid (superfluid.org)

---

# Overview

## Summary
Superfluid ([https://superfluid.org](https://superfluid.org)) is an EVM smart contract framework that enables continuous per-second money streaming for subscriptions, payroll, and maintainer stipends without incurring gas costs per block or per payment transaction. Built by Superfluid Finance, the protocol allows capital to flow continuously between accounts based on a target flow rate (e.g. 100 USDC per day).

## Purpose
Superfluid addresses payment friction, gas overhead, and administrative delays in recurring Web3 disbursements. Traditional Web2 and Web3 payroll models disburse capital in discrete monthly or bi-weekly blocks, creating manual invoice processing overhead and payment friction. Superfluid enables automated, zero-gas streaming subscriptions, retainers, and distributions where money flows continuously like electricity.

## Mission Alignment
Superfluid aligns with the Open Source Frontiers mission by providing automated, real-time streaming primitives that enable custody-free maintainer retainers and continuous enterprise subscription streams.

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
MIT License / GNU Lesser General Public License v3.0 (LGPL-3.0)

---

# Ecosystem Context

## Target Ecosystems
- Ethereum L1 & L2 EVM Networks (Arbitrum, Optimism, Polygon, Base, Avalanche, BNB Chain)
- Open-source DAO treasuries and maintainer collectives
- Web3 subscription and streaming quadratic funding projects (Geo Web, Superfluid Subscriptions)

## Intended Users
- Ecosystem foundations and dOSPO operators streaming maintainer retainers
- Open-source maintainers receiving continuous per-second stipends
- Commercial dApps establishing continuous subscription fee streams
- DAO treasury managers automating recurring contributor payroll

## Current Pain Points Addressed
Eliminates gas costs per payment block, replaces discrete bi-weekly payroll with continuous per-second streams, provides instant real-time stream cancellation rights, and automates 1-to-N token distributions in a single transaction.

---

# Technical Information

## Repository / Source Code
[https://github.com/superfluid-finance/protocol-monorepo](https://github.com/superfluid-finance/protocol-monorepo)

## Documentation
[https://docs.superfluid.finance](https://docs.superfluid.finance)

## Core Technologies
- Solidity (smart contract core framework)
- Super Tokens (`ERC20x` token wrapper standard)
- Constant Flow Agreement (CFA smart contract logic)
- Instant Distribution Agreement (IDA smart contract logic)
- SDK Core / Hardhat / Foundry (developer tooling)

## Architecture Overview
Superfluid operates by wrapping standard ERC-20 tokens into Super Tokens (`ERC20x`). Stream logic is managed by two primary agreement contracts:
- Constant Flow Agreement (CFA): Manages per-second streaming balances between accounts using a single state update. Money flows continuously per second based on a target flow rate (e.g. 100 USDC per day) without requiring block-by-block transactions. Streams run indefinitely until cancelled by either party or until the sender's balance is exhausted.
- Instant Distribution Agreement (IDA): Enables 1-to-N token distributions in a single transaction, distributing funds to thousands of token holders proportionally based on index units.
Solvency is maintained by a network of off-chain liquidators who automatically close streams if a sender's deposit buffer is breached.

## Dependencies
- EVM execution layer
- Underlying ERC-20 token contracts for wrapping into Super Tokens (`ERC20x`)
- Off-chain sentinel nodes for stream solvency monitoring and liquidation

---

# Operational Model

## Governance Model
Superfluid protocol contracts are governed by the Superfluid DAO and protocol maintainers, with governance transitioning toward decentralized token and multi-sig oversight.

## Maintenance Model
Core framework is maintained by Superfluid Finance alongside open-source contributors via public GitHub monorepos.

## Funding Model
Superfluid Finance raised venture capital backing (Multicoin Capital, Semantic Ventures, Circle Ventures) and public-goods grants to build open streaming primitives for Web3.

## Contributor Model
Open-source contribution via public GitHub monorepo issues, pull requests, and wave grants for developer integrations.

---

# Open Source Impact

## Expected Benefits
- Zero gas costs per payment transaction after stream initialization
- Continuous per-second streaming for maintainer retainers and subscriptions
- Real-time stream cancellation rights if maintainers breach charter commitments
- Instant 1-to-N distributions using Instant Distribution Agreements (IDA)

## Ecosystem Value
Superfluid establishes the financial plumbing for real-time streaming economies, allowing maintainers to earn continuous income every second while working on critical open-source infrastructure.

## Risks & Limitations
- Requires wrapping standard ERC-20 tokens into Super Tokens (`ERC20x`).
- Senders must lock a small security deposit buffer to cover liquidation costs if balances run out.
- RPC latency during severe network congestion can cause small liquidation delays.

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
Deployed in production across 10+ EVM networks. Used by DAO treasuries, streaming quadratic funding platforms (Geo Web), and maintainer groups to process tens of millions of dollars in real-time streams.

## Roadmap
Expanding cross-chain streaming bridges, native un-wrapped ERC-20 streaming, and integration with agentic payment protocols.

---

# Metrics & Evaluation

## Success Metrics

| Metric | Description |
|---|---|
| Active Flow Rate | Total USD value streamed per second across supported EVM networks |
| Total Volume Streamed | Cumulative token volume processed via CFA and IDA agreements |
| Active Super Tokens | Number of ERC-20 tokens wrapped into Super Tokens (`ERC20x`) |
| Integrated Apps | Number of Web3 dApps and protocols utilizing Superfluid streaming rails |

## Observability / Reporting
Public stream explorer (`console.superfluid.finance`), subgraph indexers, and real-time dashboard tracking stream solvency and active flow rates.

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
Superfluid provides the essential streaming primitive required to execute continuous maintainer retainers and enterprise streaming subscriptions without operational overhead.

## Program Relevance & Direct OSF Alignment

### 1. OMF Maintainer Retainer Disbursement
- **OSF Mapping**: **OMF Program 1 (Maintainer Retainers)** & **[`omf/PROGRAM_PORTFOLIO.md`](../omf/PROGRAM_PORTFOLIO.md)**.
- **Mechanism Validated**: Proves that maintainer stipends can be streamed continuously per second with real-time cancellation rights if a maintainer violates charter commitments.
- **Operator Takeaway**: OMF Retainer charters configure Superfluid CFA streams to disburse maintainer stipends continuously, eliminating monthly invoice processing and reducing operational admin overhead to zero.

### 2. ORF Streaming DApp Badges & Enterprise Subscriptions
- **OSF Mapping**: **ORF Layer 2 (Application & Enterprise Layer)** & **[`orf/INSTRUMENT_CATALOG.md`](../orf/INSTRUMENT_CATALOG.md)**.
- **Mechanism Validated**: Demonstrates continuous streaming subscriptions for commercial dApp certification badges and enterprise support retainers.
- **Operator Takeaway**: An ORF Operator configures Superfluid streams for "Sustains the Commons" dApp badges, allowing commercial projects to stream 0.1% of revenue continuously into the ecosystem treasury.

---

# Supporting Materials

## References
- Superfluid Website: https://superfluid.org
- Superfluid Documentation: https://docs.superfluid.finance
- Superfluid Protocol Monorepo: https://github.com/superfluid-finance/protocol-monorepo

## Demonstrations / Screenshots
- Console Explorer: https://console.superfluid.finance
- Dashboard: https://app.superfluid.finance

## Related Projects
- Drips Protocol (dependency splitting)
- Geo Web (streaming quadratic funding)
- Protocol Guild (retainer allocation)

---

# Contributor Information

## Primary Contact
- Superfluid Finance Core Team — GitHub: [@superfluid-finance](https://github.com/superfluid-finance)

## Contributors
- Superfluid Finance core protocol team
- Open-source ecosystem developers and wave grant recipients

## Submission Date
2026-08-18
