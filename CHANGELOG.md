# Changelog

> All notable changes to the **Open Source Frontiers Lab** framework suite will be documented in this file.

---

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
