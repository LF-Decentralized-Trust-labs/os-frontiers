# Native Reference Smart Contracts (EVM Solidity & Cardano Aiken)

> **Deployable Reference Contracts for dOSPO Governance, OMF Retainers, and ORF Value Replenishment**  
> *LF Decentralized Trust · Open Source Frontiers Lab*

---

## Overview

The `contracts/` directory provides production-ready reference smart contracts implementing the 3-piece Open Source Frontiers architecture across **EVM (Solidity)** and **Cardano (Aiken / Plutus UPLC)**:

```
contracts/
├── README.md
├── solidity/
│   └── ORFSlaVault.sol               # EVM Solidity SLA Escrow & Automated Tithe Vault
└── aiken/
    └── validators/
        └── orf_sla_vault.ak          # Cardano Plutus Aiken Maintenance Escrow Validator
```

---

## 1. EVM Solidity Contract (`ORFSlaVault.sol`)

- **Primary Features**:
  - `purchaseSLA()`: Handles enterprise maintenance SLA purchases, automatically routing 80% of funds to the treasury and 20% to maintainer retainer streams.
  - `depositReciprocalFee()`: Receives reciprocal commercial revenue share under SLA contract terms.
  - `claimMaintainerStipend()`: Streams monthly retainers to core maintainers continuously per-second.
  - `transferDOSPOAdmin()`: Enforces **Operator Replaceability**, allowing governance to transfer dOSPO administrative authority.
- **Compilation**: `npx hardhat compile` or `forge build` (Solidity `^0.8.20`).

---

## 2. Cardano Aiken Contract (`orf_sla_vault.ak`)

- **Primary Features**:
  - Compiles directly to **Plutus UPLC** bytecode for on-chain execution on Cardano.
  - Validates maintainer stipend claims, treasury fee routing, and operator replacement actions under CIP-1694 DRep & SPO governance signatures.
- **Compilation**: `aiken build` or `aiken check`.
