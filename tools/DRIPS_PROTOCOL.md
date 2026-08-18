# Tool Profile: Drips Protocol (`drips.network`)

> **On-Chain Dependency Graph Splitting & Continuous Distribution Protocol**  
> *LF Decentralized Trust · Open Source Frontiers Lab Profile*

```yaml
tool_name: "Drips Protocol"
category: "ORF Application Layer / Distribution Rail"
chains_supported: "Ethereum, Filecoin, OP Mainnet"
primary_function: "Automated dependency graph fund splitting & continuous streaming"
website: "https://drips.network"
observed_at: "2026-08-13"
evidence_status: "Live Production Precedent"
```

---

## 1. Executive Summary & Capabilities

**Drips Protocol** ([https://drips.network](https://drips.network)) is an EVM and Filecoin smart contract protocol that enables open-source projects to receive continuous fund streams and automatically cascade incoming funds down their dependency graph.

Drips solves the "nested dependency funding problem": when an ecosystem grant or enterprise payment arrives at a top-level project, Drips automatically splits and routes pre-set percentages to upstream library maintainers (e.g. `ethers.js`, `wagmi`, `tokio`) without manual intervention.

---

## 2. Technical Architecture & Mechanics

- **Drips Hub Contract**: Manages streaming balances and multi-recipient splits using token-per-second streaming math.
- **Dependency Splitting**: Projects register an on-chain `SplitsReceiver` array mapping upstream dependency addresses and split percentages. When funds arrive, the contract executes recursive distribution.
- **Custody-Free Settlement**: Recipients claim accrued funds directly from the smart contract without intermediary approval.

---

## 3. Program Relevance & Direct OSF Alignment

### 1. ORF Dependency-Directed Revenue Share
- **OSF Mapping**: **ORF Layer 2 (Application & Service Layer)** & **[`INSTRUMENT_CATALOG.md`](../orf/INSTRUMENT_CATALOG.md)**.
- **Mechanism Validated**: Proves that open-source projects can automatically pass a portion of their incoming commercial SLA or grant revenue down their dependency graph using smart contracts.
- **Operator Takeaway**: An ORF Operator utilizes Drips Protocol contracts to execute automated dependency-graph revenue splits whenever enterprise SLA payments or dApp certification fees are received.

### 2. OMF Retainer Disbursement Infrastructure
- **OSF Mapping**: **OMF Program 1 (Maintainer Retainers)** & **Superfluid/Drips Streaming**.
- **Mechanism Validated**: Demonstrates real-time, custody-free streaming for maintainer stipends across multi-chain EVM environments.
- **Operator Takeaway**: OMF Retainers leverage Drips or Superfluid streaming rails to disburse monthly maintainer retainers continuously per second, eliminating monthly invoice processing.
