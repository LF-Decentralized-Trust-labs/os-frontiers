# Changelog

> All notable changes to the **Open Source Frontiers Lab** framework suite will be documented in this file.

---

## Unreleased

### Added
- **OSFL release 1, §2 and §2.7 (`docs/surveys/`)** (2026-10-09): survey evidence rebuilt around the Tidelift project needs N1–N8, survey inventory, closing-the-gaps section, and Researchy page and reference checks, with dated web captures in `docs/surveys/data/`. Verdict: as written, the whitepapers meet six of eight needs for projects inside a funded ecosystem's portfolio; N3 (a way to receive money) is a Gap, as no whitepaper describes a way for projects to receive money; N7 (recognition and relief from user burden) is Partial; small projects outside funded portfolios stay out of reach. Publisher PDFs are not committed; `docs/surveys/README.md` lists their URLs. Not yet folded into `docs/release1-research.md`. Stage 0; no Hard Gate passed.
- **Top-100 chains audit, batch 1 (ranks 1–25)** (2026-10-09): `docs/chains/top100-audit.md`, `top100-method.md`, `top100-qa-rubric.md`, `top100-qa-log.md`, CoinGecko top-100 snapshots (fetched 05:19 PT, data as of 05:17:50 PT) and dated captures in `docs/chains/data/`. 11 UNVERIFIED tags; batches 2–4 on hold.
- **`whitepapers/OMF_ERRATA.md`** (2026-10-09): citation layer for the OMF v1.0 PDF. Corrects the Tidelift figures on PDF p8, p32 and p45: 60% of maintainers quit or considered quitting in 2024 (59% is the 2021 figure); 60% describe themselves as unpaid hobbyists; 47% report no maintainer income.
- **OSFL release 1, §3.3 (`docs/chains/`)** (9 October 2026): top-10 chains vs ORF and the POSM cycle, Researchy verification pass, and dated source captures in `docs/chains/data/`. Stage 0; no Hard Gate passed.

### Changed
- **Protocol Guild and Cardano POSM follow-ups** (2026-10-09, `docs/chains/pg-followups.md` §1–3): `claims/orf-claims-validated.md` (C-026, C-029, C-110, index and summary rows), `docs/EVIDENCE_REGISTER.md` and `docs/PRIOR_ART_AND_COMPETITIVE_ANALYSIS.md` now carry the approved Protocol Guild figures (190 members as of 5 August 2026, replacing 187) and the on-chain ₳5,885,000 POSM withdrawal; the $300K bug bounty pool is described as a planned allocation, with utilization Unverified.
- **Cardano rank** (2026-10-09): §3.3 and `docs/chains/posm-cycle-chain-map.md` now give #11 with WBT excluded and #12 under the top-100 gas-token rule (CoinGecko top-100 snapshot, 9 October 2026); the top-10 table keeps the separate 03:51 PT snapshot.
- **Protocol Guild errata** (9 October 2026): `whitepapers/ORF_ERRATA.md` now carries the approved 2025 figures ($7,231,668 valued at time of donation, 6,202 unique donors) and 190 members as of 5 August 2026 (−6 from 196), Confidence High; applied to the v1.1 manuscript and `docs/release1-research.md`.
- **Cardano POSM errata** (9 October 2026): `whitepapers/ORF_ERRATA.md` moves ₳5,885,000 out of "Claims to mark unverified" into a corrected entry rated High (on-chain; governance action enacted epoch 576, 12 August 2025) and states that the ₳4,601,000 2026–27 request was never submitted or enacted on-chain; applied to the v1.1 manuscript.
- **`docs/precedents/CARDANO_POSM.md`**: dated treasury evidence; the ≈99.8% reserve-issuance share is labeled *derived*.

### Removed
- **Contracts directory** (20 August 2026): `contracts/solidity/ORFSlaVault.sol`, `contracts/aiken/validators/orf_sla_vault.ak`, and `contracts/README.md` were deleted (commit message "Delete contracts directory"). They are not in the tree and are not a present Stage 0 artifact. The [0.8.0-rc.1] Changed note about `ORFSlaVault.sol` records work that was later removed.

## [0.8.0-rc.1] - 2026-08-13

### Added
- **Canonical 15-Indicator Assessor Engine (`evaluator/cli/assess_ecosystem.py`)**: Full 75-point 0/3/5 indicator rubric with Level 3 Net Replenishment Ratio hard-gate ($\ge 1.0$) and boolean compatibility.
- **Canonical RACI Responsibility Matrix**: Explicit matrix in `dospo/START_HERE.md` separating Community Governance, dOSPO Policy, OMF Operation, ORF Inflow, and Independent Audit.
- **Validation Framework (`VALIDATION.md`)**: 4-stage lifecycle (Stage 0 Research Candidate -> Stage 1 Peer Reviewed -> Stage 2 Piloted Precursor -> Stage 3 Validated Production).
- **Pro-Forma Feasibility Model (`docs/TIER_1_FEASIBILITY_MODEL.md`)**: Line-by-line scenario analysis, austerity budget stress derivation, and SLA attrition sensitivity models.
- **Prior-Art Analysis (`docs/PRIOR_ART_AND_COMPETITIVE_ANALYSIS.md`)**: Survey of STF, Open Collective, Tidelift, GitHub Sponsors, Protocol Guild, NLnet, and RetroPGF.
- **Fork Resistance Analysis (`orf/FORK_RESISTANCE_ANALYSIS.md`)**: Conceptual defense of registry legitimacy and non-copyable state.
- **Legal & Regulatory Overview (`orf/LEGAL_AND_REGULATORY_FRAMEWORK.md`)**: Legal entity wrappers, UBIT considerations, yield sleeves, and SLA liability bounds.

### Changed
- **Contract Security (`contracts/solidity/ORFSlaVault.sol`)**: Implemented pull-payment treasury fee routing, expiration validation, two-step admin transfer (`transferDOSPOAdmin`), and direct receive deposit handling.
- **Experimental QUAID Adapter (`evaluator/cli/quaid_adapter.py`)**: Re-framed scanner as an experimental Stage 0 heuristic index, inspecting root and `.github/` security policies, and writing dynamic outputs to `evaluator/output/`.
- **License Realignment**: Completed canonical `LICENSE-CODE` (Apache-2.0) and `LICENSE-DOCS` (CC-BY-4.0) files and updated `CONTRIBUTING.md` links.
