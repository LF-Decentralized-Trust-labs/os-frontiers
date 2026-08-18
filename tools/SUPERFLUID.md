# Tool Profile: Superfluid (`superfluid.org`)

> **LF Decentralized Trust · Open Source Frontiers Lab Profile**  
> *Metadata: `observed_at: 2026-08-13` · `evidence_status: Live Production Infrastructure Primitive`*

---

## 1. Intent & Philosophical Problem Statement
Superfluid ([https://superfluid.org](https://superfluid.org)) was developed to replace traditional discrete block-by-block transaction processing with continuous, real-time capital streams. In traditional Web2 and Web3 payroll models, maintainers and contractors receive episodic monthly or bi-weekly payouts, creating administrative overhead, invoice processing delays, and payment friction. Superfluid was conceived as a smart contract protocol that allows money to flow continuously per second, enabling automated, zero-gas streaming subscriptions, retainers, and distributions.

## 2. Detailed Operational & Technical Mechanics
Superfluid operates by wrapping standard ERC-20 tokens into **Super Tokens** (`ERC20x`). The protocol manages capital streams via two primary smart contract primitives:
- **Constant Flow Agreement (CFA)**: Manages per-second streaming balances between accounts using a single state update. Capital flows continuously per second based on a target flow rate (e.g. 100 USDC per day) without requiring block-by-block transactions. Streams run indefinitely until cancelled by either party or until the sender's balance is exhausted.
- **Instant Distribution Agreement (IDA)**: Enables 1-to-N token distributions in a single transaction, distributing funds to thousands of token holders proportionally based on index units. Solvency is maintained by a network of off-chain liquidators who automatically close streams if a sender's deposit buffer is breached.

## 3. Empirical Achievements & Demonstrated Traction
Superfluid operates in production across major EVM networks (Arbitrum, Optimism, Polygon, Base, Ethereum mainnet), processing tens of millions of dollars in continuous real-time streams for DAO payroll, maintainer stipends, streaming quadratic funding (via Geo Web), and subscription services. It stands as a battle-tested infrastructure primitive for continuous money movement in Web3.

## 4. Structural Limitations, Trade-offs & Failure Modes
Superfluid requires users to wrap underlying ERC-20 tokens into Super Tokens (`USDCx`), creating a temporary friction step during onboarding. Furthermore, senders must lock a small security deposit buffer to cover liquidation costs if their balance runs out. If liquidators experience RPC latency during extreme network congestion, liquidation delays can cause small stream buffer losses.

## 5. Program Relevance & Direct dOSPO / OMF / ORF Evaluation
- **dOSPO Evaluation**: Provides dOSPO operators with real-time stream cancellation mechanisms — allowing governance to halt maintainer stipends instantly if a maintainer breaches charter commitments.
- **OMF Evaluation**: Serves as the primary execution engine for **OMF Program 1 (Maintainer Retainers)** in [`omf/PROGRAM_PORTFOLIO.md`](../omf/PROGRAM_PORTFOLIO.md). OMF Retainer charters deploy Superfluid CFA streams to disburse monthly stipends continuously per second, eliminating monthly invoice processing overhead.
- **ORF Evaluation**: Powers **ORF Layer 2 (Application Layer Streaming Subscriptions)** by enabling commercial dApps to stream 0.1% dApp certification fees ("Sustains the Commons" badges) continuously into ecosystem treasuries.

---

## Primary References & Links
- **Website**: [https://superfluid.org](https://superfluid.org)
- **Documentation**: [https://docs.superfluid.finance](https://docs.superfluid.finance)
