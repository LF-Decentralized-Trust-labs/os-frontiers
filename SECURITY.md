# Security Policy

> **Edition**: July 2026 Research Candidate (v0.8.0-rc.1)  
> *LF Decentralized Trust · Open Source Frontiers Lab*

## Reporting a Vulnerability

Open Source Frontiers Lab takes software and framework security seriously. If you discover a security vulnerability in the repository code, CLI evaluators, web dashboard, or reference smart contracts, please report it immediately:

- **Security Email**: **oscowboyc@gmail.com** 

Please do **NOT** create a public GitHub issue for security vulnerabilities.

## Scope & Security Controls

This repository contains:
1. **Normative Guidance & Framework Documents**: Architectural standards for dOSPO, OMF, and ORF.
2. **CLI Tools & Evaluator Engines**: Python and Node.js command-line tools (`assess_ecosystem.py`, `quaid_adapter.py`).
3. **Web Dashboard**: Client-side JavaScript web application (`index.html`, `app.js`).
4. **Reference Smart Contracts**: EVM Solidity (`ORFSlaVault.sol`) and Cardano Aiken (`orf_sla_vault.ak`) research candidate sketches.

> ⚠️ **Smart Contract Notice**: Smart contract artifacts in `contracts/` are unaudited reference sketches intended for research and feasibility modeling. They must undergo formal security auditing before deployment in production environments.
