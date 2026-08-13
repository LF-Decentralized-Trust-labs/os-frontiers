# Ecosystem Profile: Polkadot OpenGov & Substrate Treasury

> **Substrate Nominated Proof-of-Stake & OpenGov Architecture**  
> *LF Decentralized Trust · Open Source Frontiers Lab Profile*

```yaml
ecosystem: "Polkadot"
architecture_type: "Substrate Nominated Proof-of-Stake (NPoS) / Parachains"
primary_governance: "Polkadot OpenGov (Track-based Referenda & Technical Fellowship)"
deployment_framework: "Polkadot Treasury Spender Tracks & Polkadot Community Foundation (PCF)"
replenishment_layer: "Protocol Layer (Slashing & Penalty Routing, Fee Tithe)"
native_assets: "DOT"
```

---

## 1. Overview & Architecture

Polkadot's **OpenGov** model provides a stake-weighted, multi-track referenda system operating directly on-chain via Substrate. The Polkadot Treasury is funded by unspent block rewards, transaction fees, and validator slashing penalties.

---

## 2. Framework Mapping

### dOSPO (Governance Authority)
- **OpenGov Spender Tracks**: Proposals are segmented into tracks (Small Spender, Big Spender, Treasurer) with distinct origin thresholds, decision periods, and confirmation periods.
- **Polkadot Technical Fellowship**: A self-governing body of core developers that can whitelist technical proposals to accelerate emergency maintenance upgrades.
- **Polkadot Community Foundation (PCF)**: Off-chain foundation entity created to execute legal contracts, fiat payments, and commercial maintenance SLAs that cannot be processed directly on-chain.

### OMF (Maintenance Deployment)
- **Maintainer Retainers**: Parachain maintainers and core Substrate developers submit multi-month retainer proposals to the Treasury.

### ORF (Collection & Replenishment)
- **Protocol Layer (Slashing & Penalty Routing)**: Polkadot directs a designated share of validator slashing penalties directly to the Treasury pool, creating an automated protocol-native inflow.
