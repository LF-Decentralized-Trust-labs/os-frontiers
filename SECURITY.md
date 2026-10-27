# Security Policy

> **Edition**: July 2026 Research Candidate (v0.8.0-rc.1)  
> *LF Decentralized Trust · Open Source Frontiers Lab*

## Reporting a Vulnerability

Open Source Frontiers Lab takes software and framework security seriously. If you discover a security vulnerability in the repository code, CLI evaluators, or the local preview, please report it immediately:

- **GitHub private vulnerability reporting**: use the repository's private reporting flow once it is enabled. TODO (Christian): enable private vulnerability reporting for `LF-Decentralized-Trust-labs/os-frontiers` (Settings → Code security → Private vulnerability reporting). Until that is on, do not file a public issue.
- **Lab security mailbox**: TODO (Christian). This file does not publish a personal address or a consulting-firm address. Add a lab-controlled mailbox here only after one exists.

Please do **NOT** create a public GitHub issue for security vulnerabilities.

## Scope & Security Controls

This repository contains:
1. **Normative Guidance & Framework Documents**: Architectural standards for dOSPO, OMF, and ORF.
2. **CLI Tools & Evaluator Engines**: Python and Node.js command-line tools (`assess_ecosystem.py`, `quaid_adapter.py`).
3. **Published page and local preview**: GitHub Pages for this repository is published at https://lf-decentralized-trust-labs.github.io/os-frontiers/ (checked 27 October 2026). The same files can be opened locally from `evaluator/preview/` (`index.html`, `app.js`, `style.css`).

`ORFSlaVault.sol`, `orf_sla_vault.ak`, and the `contracts/` directory are not in this tree. [`VALIDATION.md`](VALIDATION.md) records that directory as removed on 20 August 2026.
