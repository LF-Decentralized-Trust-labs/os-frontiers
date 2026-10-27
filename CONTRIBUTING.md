# Contributing to Open Source Frontiers Lab

> **Guidelines for Contributing Specifications, Evaluators, and Ecosystem Profiles**  
> *LF Decentralized Trust · Open Source Frontiers Lab*

---

## 1. Welcome & Scope

Thank you for your interest in contributing to the **Open Source Frontiers Lab**! We welcome contributions across all components of the 3-Piece Framework Suite (dOSPO · OMF · ORF):

- 🏛️ **Governance Specifications** (`dospo/`)
- 🛠️ **Maintenance Frameworks** (`omf/`)
- 💰 **Replenishment Frameworks** (`orf/`)
- 📊 **Evaluator Tools & Adapters** (`evaluator/`)
- 🌍 **Ecosystem precedents** (`docs/precedents/`). Stage 0 use-case research and the submission template stay in `use-cases/`.
- 🛠️ **Tooling Integrations** (`tools/`)

---

## 2. Directory Architecture

Contributions must align with the current repository directory structure:

```text
LF-Decentralized-Trust-labs/os-frontiers/
├── dospo/                  # Decentralized OSPO governance framework
├── omf/                    # Open Maintenance Framework
├── orf/                    # Open Replenishment Framework
├── evaluator/              # Assessment tools, adapters, and the local preview
├── use-cases/              # Stage 0 use-case research and the submission template
├── tools/                  # Tooling and protocol integrations (not precedents)
├── outreach/               # Adoption one-pager and governance proposal template
├── docs/                   # Guides, evidence, precedents, chains, and surveys
├── whitepapers/            # Series index, errata, v1.1 manuscript, and the v1.0 PDFs
├── claims/                 # Claim-validation notes
├── research-log/           # Working audit trail (not the specification)
├── LICENSE                 # Apache-2.0 for code
└── LICENSE-DOCS            # CC-BY-4.0 for documentation
```

There is no `contracts/` directory and no `LICENSE-CODE` file. `CODEOWNERS` does not list `/contracts/`. GitHub Pages for this repository is published at <https://lf-decentralized-trust-labs.github.io/os-frontiers/>.

---

## 3. Developer Certificate of Origin (DCO)

All Linux Foundation repositories strictly enforce the **Developer Certificate of Origin (DCO)**. Every git commit MUST be signed off using `git commit -s`. Pull-request CI checks `Signed-off-by` on each non-merge commit in the pull request and fails if one is missing.

---

## 4. Licensing

- **Code**: Licensed under [Apache-2.0](LICENSE). There is no `LICENSE-CODE` file and no `contracts/` directory.
- **Documentation & Whitepapers**: Licensed under [Creative Commons Attribution 4.0 International (CC-BY-4.0)](LICENSE-DOCS).
