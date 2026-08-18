# Tool Profile: Drips Protocol (`drips.network`)

> **LF Decentralized Trust · Open Source Frontiers Lab Profile**  
> *Metadata: `observed_at: 2026-08-13` · `evidence_status: Live Production Protocol`*

---

## 1. Intent & Philosophical Problem Statement
Drips Protocol ([https://drips.network](https://drips.network)) was created to solve the nested open-source dependency distribution crisis. When an open-source framework or dApp receives a grant or enterprise payment, that capital historically stops at the top-level repository maintainer. The hundreds of underlying library dependencies (e.g. `ethers.js`, `wagmi`, `tokio`) that make the top-level software possible receive zero financial benefit. Drips was designed as an EVM and Filecoin smart contract protocol that enables open-source projects to receive continuous streaming funds and automatically cascade incoming revenue down their dependency graph in real time.

## 2. Detailed Operational & Technical Mechanics
Drips operates through a deployed `DripsHub` smart contract architecture. Maintainers register an on-chain `SplitsReceiver` array on the contract, mapping upstream open-source dependency wallet addresses to designated percentage splits (e.g. project X splits 20% of incoming streams equally across 5 core dependencies). When token streams arrive at project X, the `DripsHub` contract executes recursive distribution logic using per-second streaming math, automatically updating the stream balances of all upstream recipients without requiring manual invoice approvals or transaction claims.

## 3. Empirical Achievements & Demonstrated Traction
Drips operates natively across Ethereum mainnet, OP Mainnet, and Filecoin, powering dependency-directed funding streams for dozens of major open-source projects and developer collectives. It serves as a primary Web3 distribution rail for continuous funding experiments, proving empirically that open-source software can automate cascading financial distributions directly on-chain.

## 4. Structural Limitations, Trade-offs & Failure Modes
Drips requires top-level maintainers to explicitly register and maintain their dependency split configurations on-chain. If a project fails to update its split array when dependencies change, funds continue flowing to legacy maintainers. Furthermore, while Drips excels at dependency-directed fund distribution, it does not generate incoming commercial revenue — it relies on external enterprise SLAs, grants, or protocol fee splits to feed funds into the distribution network.

## 5. Program Relevance & Direct dOSPO / OMF / ORF Evaluation
- **dOSPO Evaluation**: Demonstrates how dOSPO governance can mandate dependency split rules as a prerequisite for maintainer retainer eligibility.
- **OMF Evaluation**: Drips provides the primary distribution rail for **OMF Program 1 (Maintainer Retainers)**, enabling continuous per-second maintainer stipend streaming across EVM networks.
- **ORF Evaluation**: Serves as the primary distribution rail for **ORF Layer 2 (Dependency-Directed Revenue Share)** in [`orf/INSTRUMENT_CATALOG.md`](../orf/INSTRUMENT_CATALOG.md). An ORF Operator integrates Drips contracts to automatically split incoming enterprise SLA fees and dApp certification revenue down the ecosystem dependency tree.

---

## Primary References & Links
- **Website**: [https://drips.network](https://drips.network)
- **Documentation**: [https://docs.drips.network](https://docs.drips.network)
