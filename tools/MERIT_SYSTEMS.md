# Tool Profile: Merit Systems

> **LF Decentralized Trust · Open Source Frontiers Lab Profile**  
> *Metadata: `observed_at: 2026-08-13` · `evidence_status: Live Beta Tooling & Agentic Protocol`*

---

## 1. Intent & Philosophical Problem Statement
Merit Systems was created to solve the fundamental economic disconnect in open-source software: the gap between value created by software builders and value captured by those builders. Although open-source software underpins 95% of commercial software, funding has historically relied on episodic grants, venture capital (which demands inappropriate equity returns), or big-tech corporate subsidies. Merit Systems was founded to build an open economic layer for open-source software — enabling market forces to route direct capital to codebases and builders based on verifiable commit attribution and autonomous agentic payment protocols.

## 2. Detailed Operational & Technical Mechanics
Merit Systems operates across two distinct product layers:
- **Terminal**: A maintainer payout interface that parses GitHub version control data, mapping pull requests, code reviews, and commit contributions to developer wallet addresses. The Terminal executes instant global payouts using USDC on Base, with Merit managing end-to-end tax compliance and W-8/W-9 reporting.
- **AgentCash (Agentic Commerce Layer)**: An open payment gateway built on the **x402** (HTTP 402 Payment Required) and **MPP** (Machine Payments Protocol) open standards. AgentCash enables autonomous AI agents (Claude, Codex, Cursor) to discover APIs via `x402scan.com` / `mppscan.com`, negotiate pricing, and pay micro-fees per tool call using single-balance stablecoin rails.

## 3. Empirical Achievements & Demonstrated Traction
Merit Systems raised $10,000,000 in seed funding led by a16z crypto and Blockchain Capital. Its AgentCash platform launched in March 2026, processing over 770,000 paid agentic API tool calls across 2,000+ autonomous AI agents within days of launch. API partners include Minerva, Parallel, Nansen, and Zapper, demonstrating massive early adoption for machine-to-machine commerce.

## 4. Structural Limitations, Trade-offs & Failure Modes
Merit's Terminal and AgentCash product user interfaces operate as proprietary commercial offerings built atop open payment standards (x402, MPP). Furthermore, payout mechanics depend on stablecoin settlement (USDC on Base), which exposes the platform to regional crypto regulatory policies. Finally, Terminal payouts require an incoming source of capital (grant budgets, enterprise sponsorships); Merit routes capital efficiently but cannot create project funding out of thin air if a repository lacks external sponsors.

## 5. Program Relevance & Direct dOSPO / OMF / ORF Evaluation
- **dOSPO Evaluation**: Demonstrates how dOSPO policy guidelines can mandate automated tax compliance and W-8/W-9 management when contracting maintainers globally.
- **OMF Evaluation**: Serves as an execution rail for **OMF Program 2 (Code Bounties)** in [`omf/PROGRAM_PORTFOLIO.md`](../omf/PROGRAM_PORTFOLIO.md). OMF Operators use Merit Terminal to execute instant commit-attribution payouts to secondary maintainers.
- **ORF Evaluation**: Direct reference model for **ORF Layer 2 (Autonomous Agentic Revenue Inflows)** in [`orf/INSTRUMENT_CATALOG.md`](../orf/INSTRUMENT_CATALOG.md). An ORF Operator configures x402/MPP payment gateways on ecosystem developer APIs, capturing micro-transaction fees from autonomous AI agents to replenish the ecosystem treasury.

---

## Primary References & Links
- **Website**: [https://merit.systems](https://merit.systems)
- **Terminal**: [https://terminal.merit.systems](https://terminal.merit.systems)
- **AgentCash**: [https://agentcash.dev](https://agentcash.dev)
