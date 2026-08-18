# Tool Profile: Superfluid (`superfluid.org`)

> **Real-Time Money Streaming & Streaming Distribution Primitive**  
> *LF Decentralized Trust · Open Source Frontiers Lab Profile*

```yaml
tool_name: "Superfluid"
category: "OMF Retainer Rail / ORF Application Layer"
chains_supported: "Ethereum L2s (Arbitrum, Optimism, Polygon, Base)"
primary_function: "Real-time continuous per-second token streaming"
website: "https://superfluid.org"
observed_at: "2026-08-13"
evidence_status: "Live Production Infrastructure Primitive"
```

---

## 1. Executive Summary & Capabilities

**Superfluid** ([https://superfluid.org](https://superfluid.org)) is an EVM smart contract framework that enables continuous per-second money streaming for subscriptions, payroll, and maintainer stipends without incurring gas costs per block or per payment.

Superfluid wraps standard ERC-20 tokens into **Super Tokens** (`ERC20x`), allowing capital to flow continuously between accounts based on a target flow rate (e.g. 100 USDC per day).

---

## 2. Technical Architecture & Mechanics

- **Constant Flow Agreement (CFA)**: Manages per-second streaming balances using a single state update. Money streams indefinitely until cancelled or until sender balance reaches zero.
- **Instant Distribution Agreement (IDA)**: Enables 1-to-N token distributions in a single transaction, proportional to recipient shares.
- **Solvency & Liquidations**: Network liquidators monitor streams, automatically closing streams if a sender's deposit is exhausted.

---

## 3. Program Relevance & Direct OSF Alignment

### 1. OMF Maintainer Retainer Disbursement
- **OSF Mapping**: **OMF Program 1 (Maintainer Retainers)** & **[`omf/PROGRAM_PORTFOLIO.md`](../omf/PROGRAM_PORTFOLIO.md)**.
- **Mechanism Validated**: Proves that maintainer stipends can be streamed continuously per second with real-time cancellation rights if a maintainer violates charter commitments.
- **Operator Takeaway**: OMF Retainer charters configure Superfluid CFA streams to disburse maintainer stipends continuously, eliminating monthly invoice processing and reducing operational admin overhead to zero.

### 2. ORF Streaming DApp Badges & Enterprise Subscriptions
- **OSF Mapping**: **ORF Layer 2 (Application & Enterprise Layer)**.
- **Mechanism Validated**: Demonstrates continuous streaming subscriptions for commercial dApp certification badges and enterprise support retainers.
- **Operator Takeaway**: An ORF Operator configures Superfluid streams for "Sustains the Commons" dApp badges, allowing commercial projects to stream 0.1% of revenue continuously into the ecosystem treasury.
