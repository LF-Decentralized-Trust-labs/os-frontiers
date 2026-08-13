# Unaudited Reference Smart Contracts & Implementation Patterns

> **Unaudited Reference Contracts for dOSPO Governance, OMF Retainers, and ORF Value Replenishment**  
> *LF Decentralized Trust · Open Source Frontiers Lab*

---

## Overview

The `contracts/` directory provides **unaudited reference smart contracts** demonstrating implementation patterns for the 3-piece Open Source Frontiers architecture across **EVM (Solidity)** and **Cardano (Aiken / Plutus UPLC)**:

```
contracts/
├── README.md
├── solidity/
│   └── ORFSlaVault.sol               # EVM Solidity SLA Escrow & Automated Tithe Vault
└── aiken/
    └── validators/
        └── orf_sla_vault.ak          # Cardano Plutus Aiken Maintenance Escrow Validator
```

> ⚠️ **Notice**: These smart contracts are reference implementations intended for architectural demonstration and prototyping within LFDT labs. They have not undergone an independent security audit and should be audited prior to production mainnet deployment.

---

## 1. EVM Solidity Reference Contract (`ORFSlaVault.sol`)

- **Primary Features**:
  - `purchaseSLA()`: Demonstrates enterprise maintenance SLA purchases, routing 80% of funds to the treasury and 20% to maintainer retainer streams.
  - `depositReciprocalFee()`: Receives reciprocal commercial revenue share under SLA contract terms.
  - `claimMaintainerStipend()`: Streams monthly retainers to core maintainers.
  - `transferDOSPOAdmin()`: Demonstrates **Operator Replaceability**, allowing governance to transfer dOSPO administrative authority.
- **Compilation**: `npx hardhat compile` or `forge build` (Solidity `^0.8.20`).

---

## 2. Cardano Aiken Reference Contract (`orf_sla_vault.ak`)

- **Primary Features**:
  - Compiles directly to **Plutus UPLC** bytecode for on-chain execution on Cardano.
  - Validates maintainer stipend claims, treasury fee routing, and operator replacement actions under CIP-1694 DRep & SPO governance signatures.
- **Compilation**: `aiken build` or `aiken check`.
