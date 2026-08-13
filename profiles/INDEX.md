# Open Source Frontiers — Ecosystem & Tooling Profiles Index

> **Chain-Agnostic Governance, Deployment & Collection Profiles across Web3 & Web2**  
> *LF Decentralized Trust · Open Source Frontiers Lab*

---

## Directory Organization

Profiles are categorized into dedicated subdirectories within `profiles/`:
```
profiles/
├── INDEX.md
├── ecosystems/
│   ├── CARDANO.md
│   ├── OPTIMISM_SUPERCHAIN.md
│   ├── POLKADOT.md
│   ├── ETHEREUM_EVM.md
│   ├── COSMOS_INTERCHAIN.md
│   ├── SOLANA.md
│   ├── ZCASH_DEV_FUND.md
│   ├── FILECOIN.md
│   └── WEB2_FOUNDATIONS.md
└── tooling/
    ├── governance/
    │   └── SAFE_PROPOSAL.md
    ├── deployment/
    │   ├── OPEN_SOURCE_OBSERVER.md
    │   └── GITCOIN_ALLO.md
    ├── collection/
    │   ├── DRIPS_PROTOCOL.md
    │   ├── SUPERFLUID.md
    │   └── OCTANT.md
    └── enterprise/
        └── TIDELIFT_LFX.md
```

---

## 🏛️ Ecosystem Profiles (`profiles/ecosystems/`)

| Ecosystem Profile | Primary Consensus / Ledger | Key Governance & Collection Mechanism | Link to Profile |
|---|---|---|---|
| **Cardano (POSM)** | UTXO / Ouroboros PoS | CIP-1694 Lovelace Treasury, POSM Retainers, Mission Stake Pools | [`ecosystems/CARDANO.md`](./ecosystems/CARDANO.md) |
| **Optimism (Superchain)** | EVM L2 Rollup | Sequencer fee tithe, RetroFunding (RetroPGF), Open Source Observer analytics | [`ecosystems/OPTIMISM_SUPERCHAIN.md`](./ecosystems/OPTIMISM_SUPERCHAIN.md) |
| **Polkadot (Substrate)** | Substrate Nominated PoS | OpenGov tracks, Slashing routing to Treasury, PCF legal sleeve | [`ecosystems/POLKADOT.md`](./ecosystems/POLKADOT.md) |
| **Ethereum & EVM** | EVM L1 / L2 | EIP-1559 burn countermodel, Protocol Guild 1% pledge, ENS Registrar fees & EP 6.46 IPS | [`ecosystems/ETHEREUM_EVM.md`](./ecosystems/ETHEREUM_EVM.md) |
| **Cosmos & Interchain** | Tendermint PoS / IBC | Community Pool staking fees, ATOM Accelerator DAO (AADAO), Osmosis grants, DoraHacks QF | [`ecosystems/COSMOS_INTERCHAIN.md`](./ecosystems/COSMOS_INTERCHAIN.md) |
| **Solana** | Sealevel / PoH | Realms (SPL Governance), Squads smart account multisig, Solana Foundation & R.E.D. grants | [`ecosystems/SOLANA.md`](./ecosystems/SOLANA.md) |
| **Zcash** | UTXO / Equihash | ZIP 1014 (80/20 block subsidy), ZIP 1015/2001 Lockbox, ZIP 1016/271 coinholder vote transition | [`ecosystems/ZCASH_DEV_FUND.md`](./ecosystems/ZCASH_DEV_FUND.md) |
| **Filecoin** | Expected Consensus / PoRep | Gas burn countermodel, Filecoin Plus DataCap benefit-gating, Drips Filecoin integration | [`ecosystems/FILECOIN.md`](./ecosystems/FILECOIN.md) |
| **Web2 Foundations** | Traditional Open Source | Linux Foundation LFX, Apache governance separation, Tidelift & Red Hat enterprise SLAs | [`ecosystems/WEB2_FOUNDATIONS.md`](./ecosystems/WEB2_FOUNDATIONS.md) |

---

## 🛠️ Tooling & Protocol Profiles (`profiles/tooling/`)

| Tool Profile | Domain Category | Core Primitive / Capability | Link to Profile |
|---|---|---|---|
| **Safe Multisig** | Governance (`tooling/governance/`) | Secure multisig execution, SafeSnap governance integration | [`tooling/governance/SAFE_PROPOSAL.md`](./tooling/governance/SAFE_PROPOSAL.md) |
| **Open Source Observer** | Deployment (`tooling/deployment/`) | Open-source data infrastructure, dependency graph indexing, contribution analytics | [`tooling/deployment/OPEN_SOURCE_OBSERVER.md`](./tooling/deployment/OPEN_SOURCE_OBSERVER.md) |
| **Gitcoin Allo Protocol** | Deployment (`tooling/deployment/`) | Programmable capital allocation engine (Allo v2), quadratic funding, RFPs | [`tooling/deployment/GITCOIN_ALLO.md`](./tooling/deployment/GITCOIN_ALLO.md) |
| **Drips Protocol** | Collection (`tooling/collection/`) | On-chain dependency graph splitting, streaming distributions across chains | [`tooling/collection/DRIPS_PROTOCOL.md`](./tooling/collection/DRIPS_PROTOCOL.md) |
| **Superfluid** | Collection (`tooling/collection/`) | Real-time payment streaming, continuous maintainer retainers, streaming QF | [`tooling/collection/SUPERFLUID.md`](./tooling/collection/SUPERFLUID.md) |
| **Octant** | Collection (`tooling/collection/`) | ETH/GLM staking yield routing, 25% ops budget anchor | [`tooling/collection/OCTANT.md`](./tooling/collection/OCTANT.md) |
| **Tidelift & LFX** | Enterprise (`tooling/enterprise/`) | Enterprise LTS patch windows, supply-chain assurance, LFX project control center | [`tooling/enterprise/TIDELIFT_LFX.md`](./tooling/enterprise/TIDELIFT_LFX.md) |
