# Security Policy

> **Edition**: July 2026 Research Candidate (v0.8.0-rc.1)  
> *LF Decentralized Trust · Open Source Frontiers Lab*

## Reporting a Vulnerability

Open Source Frontiers Lab takes software and framework security seriously. If you discover a security vulnerability in the repository code, CLI evaluators, or the local preview, please report it immediately:

- **Security Email**: **security@opensourcefrontiers.org** (or **chris@opensourcecowboy.org**)

Please do **NOT** create a public GitHub issue for security vulnerabilities.

## Scope & Security Controls

This repository contains:
1. **Normative Guidance & Framework Documents**: Architectural standards for dOSPO, OMF, and ORF.
2. **CLI Tools & Evaluator Engines**: Python and Node.js command-line tools (`assess_ecosystem.py`, `quaid_adapter.py`).
3. **Local preview**: Client-side files in `evaluator/preview/` (`index.html`, `app.js`, `style.css`). This is a local preview, not a published site. GitHub Pages for this repository is not published.

`ORFSlaVault.sol`, `orf_sla_vault.ak`, and the `contracts/` directory are not in this tree. [`VALIDATION.md`](VALIDATION.md) records that directory as removed on 20 August 2026.
