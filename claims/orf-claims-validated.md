# ORF Claims — Validated (Release-1)

> **Validator:** USe Me (RESEARCH ENGINE)  
> **Date:** 2026-09-24 PT  
> **Inputs:** `claims/orf-claims-draft.md` (141), `sources/ORF_ERRATA.md` (controls over PDF), `sources/EVIDENCE_REGISTER.md`, `sources/VALIDATION.md`, `sources/orf-docs/*`, `sources/precedents/*`, `sources/tools/*`  
> **Banner:** **Stage 0**. No Hard Gate marked passed. Errata controls over `orf-v1.0.pdf`.

## Status legend

| Status | Meaning |
|---|---|
| **SUPPORTS** | Claim accurately restates Stage 0 specs, or a primary sourced page states it |
| **PARTIAL** | Directionally right; magnitude, stacking, confidence, or fetch incomplete |
| **CONFLICTS** | Paper/draft wording conflicts with errata or primary source; use corrected form |
| **ERRATA** | Controlling correction already in `ORF_ERRATA.md` — treat errata text as claim |
| **UNVERIFIABLE** | No rendered primary page in this pass supports the figure (reserved; prefer ERRATA when listed there) |

## Summary counts

| Status | Count |
|---|---|
| SUPPORTS | 99 |
| PARTIAL | 35 |
| CONFLICTS | 2 |
| ERRATA | 5 |
| UNVERIFIABLE | 0 |
| **Total** | 141 |

## Hard flags for synthesis (do not soft-pedal)

1. No ecosystem clears Gates 1–8 / PCR≥1.0 under ORF rules (`C-011`, `C-101`).
2. Protocol Guild / Polkadot spend / POSM budget / Octant Epoch / Deep Funding dollars: **ERRATA unverified** (`C-026`–`C-030`, `C-111`).
3. Tidelift: **definitive agreement**, not acquired (`C-025`, `C-112`).
4. ENS: **two closes** — do not stack KPK and EP 6.46 (`C-023`, `C-107`).
5. Optimism: standard-chain vs OP Mainnet 100%; buyback is timed pilot; cite vote (`C-020`–`C-021`, `C-105`–`C-106`).
6. Retro Funding / Gitcoin ≠ replenishment (`C-048`, `C-113`).
7. `ORFSlaVault.sol` removed 2026-08-20 — not an implementation (`C-129`, VALIDATION).

---

## C-001

- **Claim:** This paper is the third and final installment in a series meant to be read alongside the dOSPO paper and the OMF paper.
- **Source:** `whitepapers/orf-v1.0.pdf · Author's Note`
- **Validation status:** SUPPORTS
- **Evidence:** sources/orf-whitepaper.txt · Author's Note; sources/dospo-whitepaper.txt; sources/omf-whitepaper.txt
- **Notes:** Series framing matches Author's Note; companion papers present in sources/.

## C-002

- **Claim:** dOSPO defines governance coordination (who decides); OMF defines maintenance deployment (how resources go out); ORF defines replenishment (how resources come back).
- **Source:** `whitepapers/orf-v1.0.pdf · Author's Note`
- **Validation status:** SUPPORTS
- **Evidence:** sources/orf-whitepaper.txt · Author's Note; Framework Summary
- **Notes:** Accurate restatement of series role split.

## C-003

- **Claim:** Together dOSPO, OMF, and ORF describe a complete closed loop, but each framework can also be used independently.
- **Source:** `whitepapers/orf-v1.0.pdf · Author's Note`
- **Validation status:** SUPPORTS
- **Evidence:** sources/orf-whitepaper.txt · Author's Note; §4 stand-alone language
- **Notes:** Normative series claim; independence also stated in §4.

## C-004

- **Claim:** Instruments catalogued in ORF describe existing models and options observable in production today, not 'must use' mandates.
- **Source:** `whitepapers/orf-v1.0.pdf · Author's Note`
- **Validation status:** PARTIAL
- **Evidence:** sources/EVIDENCE_REGISTER.md; sources/orf-docs/INSTRUMENT_CATALOG.md
- **Notes:** Catalog mixes live precedents (Optimism/ENS) with D0 hypotheses and removed contracts. "Observable in production" holds for many instruments, not all catalog entries.

## C-005

- **Claim:** Open source software does not suffer from a lack of economic value; it suffers from a failure to connect value created by open infrastructure with resources required to maintain it.
- **Source:** `whitepapers/orf-v1.0.pdf · Executive Summary`
- **Validation status:** PARTIAL
- **Evidence:** sources/orf-whitepaper.txt · §1; Hoffmann HBS WP 24-038; Synopsys OSSRA 2024
- **Notes:** Diagnosis is judgment; supporting value magnitudes are external research (see C-013/C-014).

## C-006

- **Claim:** In nearly every Web3 ecosystem today, capital arrives through one-way mechanisms (token issuance, treasury reserves, grants, donations, corporate sponsorship) that deplete without replenishing.
- **Source:** `whitepapers/orf-v1.0.pdf · Executive Summary`
- **Validation status:** PARTIAL
- **Evidence:** sources/EVIDENCE_REGISTER.md §1–2; sources/VALIDATION.md
- **Notes:** Pattern judgment ("nearly every"); register supports one-way/partial-loop precedents, not a census.

## C-007

- **Claim:** ORF is not a single revenue mechanism; it treats sustainability as a portfolio design problem across five revenue families.
- **Source:** `whitepapers/orf-v1.0.pdf · Executive Summary`
- **Validation status:** SUPPORTS
- **Evidence:** sources/orf-whitepaper.txt · Exec Summary; §8; orf-docs/INSTRUMENT_CATALOG.md
- **Notes:** Accurate framework self-definition (Stage 0).

## C-008

- **Claim:** ORF strictly separates revenue generation from routing rails and allocation engines that merely move money.
- **Source:** `whitepapers/orf-v1.0.pdf · Executive Summary`
- **Validation status:** SUPPORTS
- **Evidence:** sources/orf-whitepaper.txt · Exec Summary; §5; ERRATA Gitcoin insert
- **Notes:** Core analytical rule; consistently applied in errata to Gitcoin/Retro.

## C-009

- **Claim:** ORF enforces six formal replenishment ratios, eight hard gates for self-sustainability, correlation-aware diversification, a Service Capacity Test before contractual liability may be sold, and paired P0–P5 / D0–D5 scales.
- **Source:** `whitepapers/orf-v1.0.pdf · Executive Summary`
- **Validation status:** SUPPORTS
- **Evidence:** sources/orf-whitepaper.txt · Exec Summary; §10–14; orf-docs/GOVERNANCE_RULES.md
- **Notes:** Components exist in paper + governance rules. No gate marked passed (C-101).

## C-010

- **Claim:** ORF does not propose monetizing open source code; the code remains open. Value is captured around non-copyable economic assets (maintainer capacity, verified compatibility, canonical network activity, trusted certification, enterprise response commitments, institutional coordination).
- **Source:** `whitepapers/orf-v1.0.pdf · Executive Summary`
- **Validation status:** SUPPORTS
- **Evidence:** sources/orf-whitepaper.txt · Exec Summary; §4–5; orf-docs/FORK_RESISTANCE_ANALYSIS.md
- **Notes:** Normative non-monetization of code + anchor list matches paper.

## C-011

- **Claim:** No reviewed ecosystem combines Optimism/ENS/Tidelift/Protocol Guild/Polkadot-style mechanisms into a complete, measured, closed-loop architecture.
- **Source:** `whitepapers/orf-v1.0.pdf · Executive Summary`
- **Validation status:** SUPPORTS
- **Evidence:** sources/EVIDENCE_REGISTER.md §1 Key Finding #1
- **Notes:** Matches register judgment: no reviewed ecosystem implements complete closed loop under these names. Keep labeled judgment.

## C-012

- **Claim:** ORF is presented as a Stage 0 research candidate — a testable architecture rather than a solved problem.
- **Source:** `whitepapers/orf-v1.0.pdf · Executive Summary`
- **Validation status:** SUPPORTS
- **Evidence:** sources/VALIDATION.md §2; sources/ORF_WHITEPAPER.md; orf-docs/START_HERE.md
- **Notes:** Stage 0 Research Candidate is explicit in VALIDATION and whitepaper pointer.

## C-013

- **Claim:** Open source components appeared in 96% of commercial codebases analyzed in Synopsys' 2024 Open Source Security and Risk Analysis.
- **Source:** `whitepapers/orf-v1.0.pdf · §1 Research Finding`
- **Validation status:** PARTIAL
- **Evidence:** https://www.synopsys.com (OSSRA 2024 / SBOM blog 17 Mar 2024); sources/ORF_ERRATA.md
- **Notes:** ERRATA: SBOM blog contains 96% sentence AND conflicting 2,400 codebases/81% line; press release states high-risk 74%, does not restate 96%. Cite carefully.

## C-014

- **Claim:** Hoffmann, Nagle & Zhou estimate supply-side replacement value of widely used OSS at approximately $4.15 billion and demand-side value at approximately $8.8 trillion.
- **Source:** `whitepapers/orf-v1.0.pdf · §1 Research Finding`
- **Validation status:** SUPPORTS
- **Evidence:** https://www.hbs.edu/faculty/Pages/item.aspx?num=65230 ; sources/ORF_ERRATA.md
- **Notes:** HBS Working Paper 24-038 figures as stated; spelling Hoffmann per errata.

## C-015

- **Claim:** Web3 treasuries denominated in native tokens correlate maintenance funding capacity with market cycles that determine ecosystem stress.
- **Source:** `whitepapers/orf-v1.0.pdf · §1 Web3-Specific Dimension`
- **Validation status:** PARTIAL
- **Evidence:** sources/orf-whitepaper.txt · §1 Web3 dimension
- **Notes:** Mechanism plausible; "capacity collapses when resilience most needed" is illustrative, not a measured panel study in-repo.

## C-016

- **Claim:** Monetary expansion disguises depletion: newly issued tokens feel like revenue but represent dilution, not captured external value.
- **Source:** `whitepapers/orf-v1.0.pdf · §1 Web3-Specific Dimension`
- **Validation status:** SUPPORTS
- **Evidence:** sources/orf-whitepaper.txt · §5/§8 CRITICAL POLICY NOTICE; orf-docs/INSTRUMENT_CATALOG.md A.4
- **Notes:** Normative taxonomy: issuance ≠ non-inflationary replenishment.

## C-017

- **Claim:** Structural revenue alone does not solve sustainability because of correlation risk, buyer concentration, and governance-legitimacy requirements.
- **Source:** `whitepapers/orf-v1.0.pdf · §1 Web3-Specific Dimension`
- **Validation status:** PARTIAL
- **Evidence:** sources/EVIDENCE_REGISTER.md Optimism rows; sources/orf-whitepaper.txt §1 payer concentration
- **Notes:** Supported by Optimism concentration narrative; "alone does not solve" is judgment grounded in partial precedents.

## C-018

- **Claim:** Generating ~$3M/year of spendable income at 3–5% real yield requires $60M–$100M+ of productive principal (Endowment Mirage / Endowment Fantasy).
- **Source:** `whitepapers/orf-v1.0.pdf · §1 Documented Costs; Glossary`
- **Validation status:** SUPPORTS
- **Evidence:** sources/orf-whitepaper.txt · §1 Endowment Mirage (arithmetic)
- **Notes:** Illustrative yield math; not an empirical measurement of a specific fund.

## C-019

- **Claim:** Even a perfectly operated deployment architecture depletes without a replenishment architecture behind it.
- **Source:** `whitepapers/orf-v1.0.pdf · §1 series diagnosis`
- **Validation status:** SUPPORTS
- **Evidence:** sources/orf-whitepaper.txt · §1 series diagnosis
- **Notes:** Normative series corollary; consistent with Stage 0 framing.

## C-020

- **Claim:** Optimism Superchain: Standard OP Chains contribute the greater of 2.5% of Chain Revenue or 15% of Net Onchain Profit to the Optimism Collective.
- **Source:** `whitepapers/orf-v1.0.pdf · §2 Optimism`
- **Validation status:** PARTIAL
- **Evidence:** https://docs.optimism.io/governance/capital-allocation ; sources/ORF_ERRATA.md; sources/EVIDENCE_REGISTER.md
- **Notes:** ERRATA: formula is standard-chain rule; OP Mainnet contributes 100% (carve-out). Medium confidence Foundation docs, not audit.

## C-021

- **Claim:** Optimism governance extended the model in 2026 by approving routing of 50% of revenue to OP buybacks.
- **Source:** `whitepapers/orf-v1.0.pdf · §2 Optimism`
- **Validation status:** CONFLICTS
- **Evidence:** sources/ORF_ERRATA.md · §2 Optimism buyback; https://optimism.io/blog/op-token-buybacks ; CoinDesk 2026-01-28
- **Notes:** Paper shorthand "50% of revenue to OP buybacks" underspecifies. ERRATA: 12-month pilot from Feb; Foundation said "incoming"; CoinDesk reported "net" + 84.4%. Cite vote, not only proposal.

## C-022

- **Claim:** Base's 2026 move toward a Base-managed unified software stack demonstrates exit/dependency risk inside a structural mechanism.
- **Source:** `whitepapers/orf-v1.0.pdf · §2 Optimism`
- **Validation status:** PARTIAL
- **Evidence:** sources/orf-whitepaper.txt · §1 Documented Costs; sources/EVIDENCE_REGISTER.md Exit Risk note
- **Notes:** Cited as concentration/exit illustration; primary Base-stack transition page not separately fetched in register this pass.

## C-023

- **Claim:** ENS: Canonical .eth registration revenue ($18.22M in 2025) flows into DAO control; May 2026 EP6.46 IPS reports ~$93.4M AUM and >$8M net DeFi returns since inception.
- **Source:** `whitepapers/orf-v1.0.pdf · §2 ENS`
- **Validation status:** PARTIAL
- **Evidence:** https://discuss.ens.domains/t/kpk-2025-review-for-the-ens-endowment/21829 ; https://docs.ens.domains/dao/proposals/6.46/ ; sources/ORF_ERRATA.md
- **Notes:** Do NOT stack KPK Dec AUM with EP 6.46 ~$93.4M AUM. Two closes. Revenue $18.22M is KPK print (Medium).

## C-024

- **Claim:** ENS endowment yield covered approximately 20.3% of 2025 operating expenses; functions as resilience layer, not foundation.
- **Source:** `whitepapers/orf-v1.0.pdf · §2 ENS`
- **Validation status:** SUPPORTS
- **Evidence:** sources/ORF_ERRATA.md · §2 ENS; KPK 2025 review
- **Notes:** Endowment covering ~20.3% of opex is on KPK print; "resilience not foundation" is consistent judgment.

## C-025

- **Claim:** Tidelift (acquired by Sonar) shows enterprises will pay recurring subscriptions for open infrastructure assurance; named customers include Cisco, Fannie Mae, and U.S. Air Force.
- **Source:** `whitepapers/orf-v1.0.pdf · §2 Tidelift`
- **Validation status:** CONFLICTS
- **Evidence:** https://www.sonarsource.com/company/press-releases/sonar-to-acquire-tidelift/ ; sources/ORF_ERRATA.md Tidelift
- **Notes:** ERRATA: say "definitive agreement to acquire," not "acquired," unless closing announced. Named customers SUPPORTS.

## C-026

- **Claim:** Protocol Guild: $7.2M from 6,202 donors (2025); 196 members as of Q2 2026; $80M+ committed.
- **Source:** `whitepapers/orf-v1.0.pdf · §2 Protocol Guild`
- **Validation status:** ERRATA
- **Evidence:** sources/ORF_ERRATA.md · Protocol Guild; https://www.protocolguild.org/blog/20260604-Q2-quarterly-audit
- **Notes:** 196 members (22 May 2026) recoverable. Dollar totals $7.2M / 6,202 donors / $80M+ NOT recoverable from rendered primary page — mark unverified.

## C-027

- **Claim:** Polkadot/PCF: ~$70.6M 2025 treasury spend; $1.5M Anemoy allocation; Cayman executor pattern.
- **Source:** `whitepapers/orf-v1.0.pdf · §2 Polkadot`
- **Validation status:** ERRATA
- **Evidence:** sources/ORF_ERRATA.md · Claims to mark unverified; https://wiki.polkadot.com/general/pcf/
- **Notes:** Wiki SUPPORTS Cayman PCF legal design only. ~$70.6M spend / $1.5M Anemoy / referenda IDs UNVERIFIABLE this pass.

## C-028

- **Claim:** Octant: 100,000 ETH staked; ~460 ETH (~$1.7M) Epoch 8.
- **Source:** `whitepapers/orf-v1.0.pdf · §2 Octant`
- **Validation status:** ERRATA
- **Evidence:** sources/ORF_ERRATA.md; https://golem.foundation/2023/08/08/announcing-octant.html
- **Notes:** 100k ETH stake announcement SUPPORTS (with validator caveat). Epoch 8 ~460 ETH UNVERIFIABLE.

## C-029

- **Claim:** Cardano POSM: 5.885M ADA 2025 budget; $300K bounty pool fully utilized — deployment precedent, not replenishment.
- **Source:** `whitepapers/orf-v1.0.pdf · §2 Cardano POSM`
- **Validation status:** ERRATA
- **Evidence:** sources/ORF_ERRATA.md; https://www.intersectmbo.org/news/the-paid-open-source-model ; sources/precedents/CARDANO_POSM.md
- **Notes:** Program shape (retainers, Code for Us, incubation) SUPPORTS as OMF precursor. 5.885M ADA / $300K bounty NOT on explainer — UNVERIFIABLE.

## C-030

- **Claim:** Drips, Superfluid, and Deep Funding ($220K / 34 seed repos / 5,000+ dependencies) generate zero replenishment; they move/divide money already collected.
- **Source:** `whitepapers/orf-v1.0.pdf · §2 Routing Mirage`
- **Validation status:** PARTIAL
- **Evidence:** sources/orf-docs/INSTRUMENT_CATALOG.md S.1–S.3; sources/ORF_ERRATA.md Deep Funding; sources/tools/DRIPS_PROTOCOL.md; SUPERFLUID.md
- **Notes:** Classification as rails/engines SUPPORTS. Deep Funding $220K/34/5000+ UNVERIFIABLE per errata. "Zero replenishment" is taxonomy, not a cash audit of those systems.

## C-031

- **Claim:** Among precedents reviewed, no ecosystem operates a deliberately diversified portfolio across uncorrelated revenue classes with measured coverage targets.
- **Source:** `whitepapers/orf-v1.0.pdf · §3 Gaps`
- **Validation status:** PARTIAL
- **Evidence:** sources/EVIDENCE_REGISTER.md comparative matrix
- **Notes:** Judgment consistent with register (partial loops). Not a universal proof.

## C-032

- **Claim:** Public discussion almost universally cites gross figures; cost-to-collect is rarely disclosed.
- **Source:** `whitepapers/orf-v1.0.pdf · §3 Gaps`
- **Validation status:** PARTIAL
- **Evidence:** sources/EVIDENCE_REGISTER.md §1–3 (Foundation narratives vs audits)
- **Notes:** Observational judgment; Gate 2 language reinforces the gap.

## C-033

- **Claim:** Streaming rails / dependency splits / AI allocation are routinely presented as sustainability mechanisms but distribute rather than replenish.
- **Source:** `whitepapers/orf-v1.0.pdf · §3 Gaps`
- **Validation status:** SUPPORTS
- **Evidence:** sources/ORF_ERRATA.md grants-era insert; catalog S.1–S.3
- **Notes:** Consistent ORF taxonomy application.

## C-034

- **Claim:** Token issuance directed at maintenance is dilution and cannot appear in honest self-sustainability calculations.
- **Source:** `whitepapers/orf-v1.0.pdf · §3 Gaps`
- **Validation status:** SUPPORTS
- **Evidence:** orf-docs/INSTRUMENT_CATALOG.md A.4; GOVERNANCE_RULES
- **Notes:** Normative rule.

## C-035

- **Claim:** This review did not identify a published framework defining hard, non-compensable conditions that must all hold simultaneously for 'sustainable'.
- **Source:** `whitepapers/orf-v1.0.pdf · §3 Gaps`
- **Validation status:** PARTIAL
- **Evidence:** sources/VALIDATION.md; prior-art analysis
- **Notes:** Competitive claim — ORF positions eight gates as contribution. Treat as Stage 0 assertion pending broader prior-art audit.

## C-036

- **Claim:** Among frameworks reviewed, none separates external precedent from local deployment evidence on distinct scales.
- **Source:** `whitepapers/orf-v1.0.pdf · §3 Gaps`
- **Validation status:** PARTIAL
- **Evidence:** sources/orf-whitepaper.txt §14; sources/PRIOR_ART_AND_COMPETITIVE_ANALYSIS.md
- **Notes:** P/D scale separation is ORF contribution claim; "none among frameworks reviewed" needs prior-art dossier citation when published.

## C-037

- **Claim:** Any Web3 ecosystem can implement ORF without dependency on or license from any specific prior program.
- **Source:** `whitepapers/orf-v1.0.pdf · §3 Synthesis`
- **Validation status:** SUPPORTS
- **Evidence:** sources/orf-whitepaper.txt · §3/§4 stand-alone; Author's Note
- **Notes:** Normative portability claim.

## C-038

- **Claim:** CORE THESIS: An open source ecosystem becomes financially resilient when a sufficient portion of the economic value enabled by its infrastructure can be converted into diversified, recurring, auditable net inflows capable of financing the ongoing cost of maintaining that infrastructure.
- **Source:** `whitepapers/orf-v1.0.pdf · §4 Core Thesis`
- **Validation status:** SUPPORTS
- **Evidence:** sources/orf-whitepaper.txt · matching section; orf-docs/*
- **Notes:** Core thesis definition — Stage 0 normative.

## C-039

- **Claim:** Every candidate replenishment mechanism must answer five questions: Origin, Legitimacy, Cost, Risk, Coverage — or it is not a replenishment instrument.
- **Source:** `whitepapers/orf-v1.0.pdf · §4 Five Economic Questions`
- **Validation status:** SUPPORTS
- **Evidence:** sources/orf-whitepaper.txt · matching section; orf-docs/*
- **Notes:** Matches orf-docs/5_QUESTION_ASSESSMENT.md.

## C-040

- **Claim:** Minimum Viable ORF requires all five: (1) verified cost floor, (2) classified inflow inventory, (3) at least one earned instrument with real receipts, (4) net-contribution reporting, (5) ratio and gate review cadence.
- **Source:** `whitepapers/orf-v1.0.pdf · §4 Minimum Viable ORF`
- **Validation status:** SUPPORTS
- **Evidence:** sources/orf-whitepaper.txt · matching section; orf-docs/*
- **Notes:** MV ORF five conditions restated accurately.

## C-041

- **Claim:** An ecosystem meeting the five MV-ORF conditions is running ORF even with PCR far below 1.0.
- **Source:** `whitepapers/orf-v1.0.pdf · §4 Minimum Viable ORF`
- **Validation status:** SUPPORTS
- **Evidence:** sources/orf-whitepaper.txt · matching section; orf-docs/*
- **Notes:** Explicit paper language: running ORF ≠ PCR≥1.0.

## C-042

- **Claim:** Optional commercial collection must provide independent tangible counter-value; structural protocol collection requires explicit governance legitimacy — never quietly taxed.
- **Source:** `whitepapers/orf-v1.0.pdf · §5 Legitimacy & Counter-Value`
- **Validation status:** SUPPORTS
- **Evidence:** sources/orf-whitepaper.txt · matching section; orf-docs/*
- **Notes:** Principle 1 restatement.

## C-043

- **Claim:** Every mechanism is evaluated on net contribution after all cost-to-collect, never gross revenue.
- **Source:** `whitepapers/orf-v1.0.pdf · §5 Net Contribution`
- **Validation status:** SUPPORTS
- **Evidence:** sources/orf-whitepaper.txt · matching section; orf-docs/*
- **Notes:** Principle 2; aligns with 12-field reporting.

## C-044

- **Claim:** Revenue sources are strictly decoupled from routing rails and allocation engines.
- **Source:** `whitepapers/orf-v1.0.pdf · §5 Strict Functional Separation`
- **Validation status:** SUPPORTS
- **Evidence:** sources/orf-whitepaper.txt · matching section; orf-docs/*
- **Notes:** Principle 3.

## C-045

- **Claim:** Diversification is measured across economic correlation classes, not counted across instruments.
- **Source:** `whitepapers/orf-v1.0.pdf · §5 Correlation-Aware Diversification`
- **Validation status:** SUPPORTS
- **Evidence:** sources/orf-whitepaper.txt · matching section; orf-docs/*
- **Notes:** Principle 4; Gate 4.

## C-046

- **Claim:** ORF monetizes fork-resilient economic anchors (maintainer knowledge, enterprise relationships, certification trust, trademarks, canonical state/liquidity, operational response, governance legitimacy) rather than manufacturing scarcity around code.
- **Source:** `whitepapers/orf-v1.0.pdf · §5 Fork-Resilient Anchors`
- **Validation status:** SUPPORTS
- **Evidence:** sources/orf-whitepaper.txt · matching section; orf-docs/*
- **Notes:** Principle 5; Fork Resistance Analysis.

## C-047

- **Claim:** Closed-loop six stages: Value Generation → ORF Collection → Governed Treasury → Routing & Allocation → OMF Deployment → Sustained Infrastructure.
- **Source:** `whitepapers/orf-v1.0.pdf · §6 Six Stages`
- **Validation status:** SUPPORTS
- **Evidence:** sources/orf-whitepaper.txt · matching section; orf-docs/*
- **Notes:** Six-stage loop architecture.

## C-048

- **Claim:** Distribution must not be mistaken for replenishment; routing/allocation occupy Stage 4 and counting them as revenue is analogous to counting a conveyor belt as a factory.
- **Source:** `whitepapers/orf-v1.0.pdf · §6 Architectural Rule`
- **Validation status:** SUPPORTS
- **Evidence:** sources/orf-whitepaper.txt · matching section; orf-docs/*
- **Notes:** Architectural rule; errata applies to Retro/Gitcoin.

## C-049

- **Claim:** ORF is a portfolio architecture, not a revenue mechanism; it can perform with or without the other series frameworks.
- **Source:** `whitepapers/orf-v1.0.pdf · §6`
- **Validation status:** SUPPORTS
- **Evidence:** sources/orf-whitepaper.txt · matching section; orf-docs/*
- **Notes:** Stand-alone portfolio architecture.

## C-050

- **Claim:** Two-dimensional taxonomy: Value-Origin Layer (Protocol, Application, Enterprise, Capital, Delegation) × Instrument Type (Revenue Source, Contribution Source, Capital Management, Issuance Source, Routing Rail, Allocation Mechanism, Financial/Risk Product).
- **Source:** `whitepapers/orf-v1.0.pdf · §7`
- **Validation status:** SUPPORTS
- **Evidence:** orf-docs/INSTRUMENT_CATALOG.md §1
- **Notes:** Two-dimensional taxonomy matches catalog.

## C-051

- **Claim:** Issuance Source does not count as replenishment (dilution). Routing Rail and Allocation Mechanism do not count as replenishment.
- **Source:** `whitepapers/orf-v1.0.pdf · §7 Instrument Type table`
- **Validation status:** SUPPORTS
- **Evidence:** orf-docs/INSTRUMENT_CATALOG.md §1; A.4; S.1–S.3
- **Notes:** Issuance/rails/engines excluded from replenishment totals.

## C-052

- **Claim:** External Precedent Rating P0–P5 and Deployment Evidence Rating D0–D5 are deliberately separate scales.
- **Source:** `whitepapers/orf-v1.0.pdf · §7`
- **Validation status:** SUPPORTS
- **Evidence:** orf-docs/INSTRUMENT_CATALOG.md §1; whitepaper §14
- **Notes:** P vs D separation.

## C-053

- **Claim:** CNCF-style conformance certification is P4 externally and D0 for any ecosystem that has never run a conformance program.
- **Source:** `whitepapers/orf-v1.0.pdf · §7`
- **Validation status:** PARTIAL
- **Evidence:** orf-docs/INSTRUMENT_CATALOG.md C.2; whitepaper §7–8
- **Notes:** Illustrative rating example. CNCF "90+ offerings" not re-fetched as primary count this pass — treat P4 label as catalog assertion.

## C-054

- **Claim:** Five Revenue Families: A Structural Network Revenue; B Enterprise Earned Revenue; C Membership & Certification; D Voluntary/Incentivized Contributions; E Capital Income.
- **Source:** `whitepapers/orf-v1.0.pdf · §8`
- **Validation status:** SUPPORTS
- **Evidence:** whitepaper §8; INSTRUMENT_CATALOG Families A–E
- **Notes:** Family list accurate.

## C-055

- **Claim:** Cardano directs 20% of the epoch reward pot to the treasury; that pot combines fees with monetary expansion — only fee-derived portion qualifies as non-inflationary structural revenue under ORF.
- **Source:** `whitepapers/orf-v1.0.pdf · §8 Family A / CRITICAL POLICY NOTICE`
- **Validation status:** PARTIAL
- **Evidence:** INSTRUMENT_CATALOG A.4; Cardano monetary policy pages (not re-fetched for exact 20% wording this pass)
- **Notes:** Policy notice intent SUPPORTS. Exact "20% of epoch reward pot" wording should be tied to a dated Cardano primary page before Hard use.

## C-056

- **Claim:** Monetary expansion allocated toward maintenance CANNOT count toward non-inflationary self-sustainability metrics under any ORF calculation.
- **Source:** `whitepapers/orf-v1.0.pdf · §8 CRITICAL POLICY NOTICE`
- **Validation status:** SUPPORTS
- **Evidence:** INSTRUMENT_CATALOG A.4 CRITICAL POLICY NOTICE
- **Notes:** Normative.

## C-057

- **Claim:** Product A Open Infrastructure Assurance: indicative $25K–$100K+ annual; risk intelligence without 24/7 patching; Tidelift P4 externally, typically D1 locally.
- **Source:** `whitepapers/orf-v1.0.pdf · §8 Family B Product A`
- **Validation status:** PARTIAL
- **Evidence:** INSTRUMENT_CATALOG B.1
- **Notes:** Indicative price band is catalog guidance, not market survey evidence.

## C-058

- **Claim:** Product B LTS/SLA: indicative $75K–$250K+; prohibited until Service Capacity Test passed; for generic DAOs without support orgs rated D0.
- **Source:** `whitepapers/orf-v1.0.pdf · §8 Family B Product B`
- **Validation status:** SUPPORTS
- **Evidence:** INSTRUMENT_CATALOG B.2; whitepaper §8/§10
- **Notes:** SCT gate + D0 for generic DAOs matches specs. Reference contract removed 2026-08-20.

## C-059

- **Claim:** Do not sell maintenance guarantees the ecosystem lacks capacity to fulfill.
- **Source:** `whitepapers/orf-v1.0.pdf · §8 Family B warning`
- **Validation status:** SUPPORTS
- **Evidence:** whitepaper §8 Family B warning; SCT
- **Notes:** Normative safety rule.

## C-060

- **Claim:** Product B is only sellable because OMF Maintainer Retainer programs exist to contract capacity behind it.
- **Source:** `whitepapers/orf-v1.0.pdf · §8 Family B`
- **Validation status:** SUPPORTS
- **Evidence:** whitepaper §8; OMF retainer linkage; VALIDATION OMF retainers Stage 0
- **Notes:** Architectural dependency claim; OMF retainers themselves Stage 0 / POSM precursor.

## C-061

- **Claim:** Sustaining Consortium Membership: tiered dues $10K–$250K+; Linux Foundation membership P4 Scaled; technical governance remains 100% independent of membership status.
- **Source:** `whitepapers/orf-v1.0.pdf · §8 Family C`
- **Validation status:** PARTIAL
- **Evidence:** INSTRUMENT_CATALOG C.1; https://www.linuxfoundation.org
- **Notes:** LF membership as P4 pattern SUPPORTS qualitatively; tier dollar bands are indicative catalog figures.

## C-062

- **Claim:** Certified Ecosystem Provider: $10K–$50K; CNCF Certified Kubernetes 90+ offerings P4; payment buys testing not a passing result.
- **Source:** `whitepapers/orf-v1.0.pdf · §8 Family C`
- **Validation status:** PARTIAL
- **Evidence:** INSTRUMENT_CATALOG C.2; https://www.cncf.io
- **Notes:** Conformance model SUPPORTS; "90+ offerings" count not independently re-counted this pass.

## C-063

- **Claim:** Professional Certification & Training: $300–$750 exams; LF CKA/CKAD P3 Sustained.
- **Source:** `whitepapers/orf-v1.0.pdf · §8 Family C`
- **Validation status:** PARTIAL
- **Evidence:** INSTRUMENT_CATALOG C.3; LF training pages
- **Notes:** CKA/CKAD as live credential market PARTIAL pending dated price/page fetch for $300–$750 band.

## C-064

- **Claim:** Payment MUST NOT purchase a certification passing result.
- **Source:** `whitepapers/orf-v1.0.pdf · §8 Family C KEY PRINCIPLE`
- **Validation status:** SUPPORTS
- **Evidence:** INSTRUMENT_CATALOG C.2 KEY PRINCIPLE
- **Notes:** Normative integrity rule.

## C-065

- **Claim:** Family D is valuable diversification but a weak foundation for guaranteed operating liabilities.
- **Source:** `whitepapers/orf-v1.0.pdf · §8 Family D`
- **Validation status:** SUPPORTS
- **Evidence:** whitepaper §8 Family D
- **Notes:** Normative portfolio guidance.

## C-066

- **Claim:** Capital income is a late-stage resilience layer, NOT a Day-1 bootstrap solution.
- **Source:** `whitepapers/orf-v1.0.pdf · §8 Family E CRITICAL REALITY CHECK`
- **Validation status:** SUPPORTS
- **Evidence:** whitepaper §8 Family E; §1 Endowment Mirage; ENS ~20% coverage
- **Notes:** Consistent with ENS evidence pattern.

## C-067

- **Claim:** Separated roles: Community Governance, dOSPO, ORF Operator, OMF Operator, Neutral Legal Entity, Governed Treasury — each with explicit Cannot list.
- **Source:** `whitepapers/orf-v1.0.pdf · §9 Separated Roles`
- **Validation status:** SUPPORTS
- **Evidence:** whitepaper §9; orf-docs/GOVERNANCE_RULES.md
- **Notes:** Separated roles architecture.

## C-068

- **Claim:** Operator capture and customer capture are explicitly foreclosed: revenue production does not buy technical governance; payment does not buy maintainer control.
- **Source:** `whitepapers/orf-v1.0.pdf · §9`
- **Validation status:** SUPPORTS
- **Evidence:** whitepaper §9; GOVERNANCE_RULES §6
- **Notes:** Neutral Legal Entity separation.

## C-069

- **Claim:** Polkadot Community Foundation Cayman pattern is the strongest available template for ORF Neutral Legal Entity.
- **Source:** `whitepapers/orf-v1.0.pdf · §9 LEGAL EXECUTION PRECEDENT`
- **Validation status:** PARTIAL
- **Evidence:** https://wiki.polkadot.com/general/pcf/ ; EVIDENCE_REGISTER Polkadot row
- **Notes:** PCF legal design SUPPORTS as strongest fetched neutral-executor description. "Strongest template" is judgment.

## C-070

- **Claim:** For U.S. tax-exempt entities, commercial service revenue is generally subject to UBIT unless substantially related; applying proceeds to exempt purpose does not by itself make revenue substantially related.
- **Source:** `whitepapers/orf-v1.0.pdf · §9 UBIT`
- **Validation status:** PARTIAL
- **Evidence:** whitepaper §9; orf-docs/LEGAL_AND_REGULATORY_FRAMEWORK.md
- **Notes:** General UBIT statement — not transaction-specific counsel. Stage 0 legal note.

## C-071

- **Claim:** RMF arrangements should not be characterized as PRIs without transaction-specific tax analysis under IRC §4944(c).
- **Source:** `whitepapers/orf-v1.0.pdf · §9 RMF`
- **Validation status:** SUPPORTS
- **Evidence:** GOVERNANCE_RULES §7; LEGAL_AND_REGULATORY_FRAMEWORK.md
- **Notes:** Matches "no automatic PRI" rule.

## C-072

- **Claim:** Operating expenses are paid by Neutral Legal Entity from gross receipts before net proceeds flow to treasury.
- **Source:** `whitepapers/orf-v1.0.pdf · §9`
- **Validation status:** SUPPORTS
- **Evidence:** whitepaper §6/§9; GOVERNANCE_RULES
- **Notes:** Net-after-opex transfer rule.

## C-073

- **Claim:** Service Capacity Test requires all five: (1) Contracted Maintainer Capacity, (2) Triage & Support Infrastructure, (3) Escalation & Backport Procedures, (4) Liability & Insurance Coverage, (5) Wind-Down Operating Reserve (six months of obligations).
- **Source:** `whitepapers/orf-v1.0.pdf · §10`
- **Validation status:** SUPPORTS
- **Evidence:** whitepaper §10; GOVERNANCE_RULES §5; ENTERPRISE_SLA_AGREEMENT.md
- **Notes:** Five SCT conditions restated from specs.

## C-074

- **Claim:** Failing the Service Capacity Test restricts ecosystem to Open Infrastructure Assurance without contractual remediation guarantees.
- **Source:** `whitepapers/orf-v1.0.pdf · §10`
- **Validation status:** SUPPORTS
- **Evidence:** GOVERNANCE_RULES §5; INSTRUMENT_CATALOG B.1 vs B.2
- **Notes:** Restriction to B.1 on SCT fail.

## C-075

- **Claim:** IECR = R_earned_net / C_base — Incremental Earned Coverage Ratio.
- **Source:** `whitepapers/orf-v1.0.pdf · §11`
- **Validation status:** SUPPORTS
- **Evidence:** sources/orf-whitepaper.txt · §11; orf-docs/GOVERNANCE_RULES.md · §3 — IECR definition
- **Notes:** Formula accurately restated.

## C-076

- **Claim:** SPCR = R_protocol_net / C_base — Structural Protocol Coverage Ratio.
- **Source:** `whitepapers/orf-v1.0.pdf · §11`
- **Validation status:** SUPPORTS
- **Evidence:** sources/orf-whitepaper.txt · §11; orf-docs/GOVERNANCE_RULES.md · §3 — SPCR definition
- **Notes:** Formula accurately restated.

## C-077

- **Claim:** PCR = (earned + protocol + yield + pledges)_net / C_base; PCR ≥ 1.0 is Gate 3 threshold.
- **Source:** `whitepapers/orf-v1.0.pdf · §11`
- **Validation status:** SUPPORTS
- **Evidence:** sources/orf-whitepaper.txt · §11; orf-docs/GOVERNANCE_RULES.md · §3 — PCR definition + Gate 3
- **Notes:** Formula accurately restated.

## C-078

- **Claim:** SCR = R_stressed_inflows / C_austerity_floor — Stress Coverage Ratio; Gate 6 threshold.
- **Source:** `whitepapers/orf-v1.0.pdf · §11`
- **Validation status:** SUPPORTS
- **Evidence:** sources/orf-whitepaper.txt · §11; orf-docs/GOVERNANCE_RULES.md · §3 — SCR definition + Gate 6
- **Notes:** Formula accurately restated.

## C-079

- **Claim:** RCR = max(R_i) / Σ R_i; must remain ≤ 0.25 — Gate 5 threshold. Measures counterparty concentration, not revenue-family share.
- **Source:** `whitepapers/orf-v1.0.pdf · §11`
- **Validation status:** SUPPORTS
- **Evidence:** sources/orf-whitepaper.txt · §11; orf-docs/GOVERNANCE_RULES.md · §3 — RCR definition + Gate 5; interpretive note
- **Notes:** Formula accurately restated.

## C-080

- **Claim:** MCR = largest single mechanism's net contribution / total recurring net inflows; MCR > 0.50 triggers portfolio review; not a hard gate.
- **Source:** `whitepapers/orf-v1.0.pdf · §11`
- **Validation status:** SUPPORTS
- **Evidence:** sources/orf-whitepaper.txt · §11; orf-docs/GOVERNANCE_RULES.md · §3 — MCR definition + review trigger
- **Notes:** Formula accurately restated.

## C-081

- **Claim:** In the Tier 1 scenario (Section 15), protocol fees represent 47.4% of total net inflows — review-triggering MCR that payer-based RCR would not surface.
- **Source:** `whitepapers/orf-v1.0.pdf · §11`
- **Validation status:** PARTIAL
- **Evidence:** whitepaper §15 Tier 1 scenario; VALIDATION.md Feasibility Pro-Forma
- **Notes:** 47.4% is model output from illustrative Tier 1 scenario, not measured production portfolio.

## C-082

- **Claim:** Evidence Register defines composite Exit Risk Score = RCR × Contract Durability × Exit Rights × Economic Correlation × Enforceability.
- **Source:** `whitepapers/orf-v1.0.pdf · §11`
- **Validation status:** SUPPORTS
- **Evidence:** sources/EVIDENCE_REGISTER.md §4 Exit Risk Score formula
- **Notes:** Formula present in register; derived illustration from Optimism Base transition.

## C-083

- **Claim:** Gate 1 Measurement: empirically verified annual maintenance cost floor exists.
- **Source:** `whitepapers/orf-v1.0.pdf · §12`
- **Validation status:** SUPPORTS
- **Evidence:** sources/orf-whitepaper.txt · §12 Gate 1; orf-docs/GOVERNANCE_RULES.md
- **Notes:** Gate 1 text accurately restated. No ecosystem marked passed.

## C-084

- **Claim:** Gate 2 Cash Evidence: inflow metrics reflect audited cash/stablecoin receipts actually received; forecasts/pledges/hypotheticals do not qualify.
- **Source:** `whitepapers/orf-v1.0.pdf · §12`
- **Validation status:** SUPPORTS
- **Evidence:** sources/orf-whitepaper.txt · §12 Gate 2; orf-docs/GOVERNANCE_RULES.md
- **Notes:** Gate 2 text accurately restated. No ecosystem marked passed.

## C-085

- **Claim:** Gate 3 Net Coverage: PCR ≥ 1.0.
- **Source:** `whitepapers/orf-v1.0.pdf · §12`
- **Validation status:** SUPPORTS
- **Evidence:** sources/orf-whitepaper.txt · §12 Gate 3; orf-docs/GOVERNANCE_RULES.md
- **Notes:** Gate 3 text accurately restated. No ecosystem marked passed.

## C-086

- **Claim:** Gate 4 Multi-Class Diversity: inflows from ≥2 materially uncorrelated Revenue Correlation Classes via three-step independence procedure.
- **Source:** `whitepapers/orf-v1.0.pdf · §12`
- **Validation status:** SUPPORTS
- **Evidence:** sources/orf-whitepaper.txt · §12 Gate 4; orf-docs/GOVERNANCE_RULES.md
- **Notes:** Gate 4 text accurately restated. No ecosystem marked passed.

## C-087

- **Claim:** Gate 5 Concentration Limit: RCR ≤ 0.25.
- **Source:** `whitepapers/orf-v1.0.pdf · §12`
- **Validation status:** SUPPORTS
- **Evidence:** sources/orf-whitepaper.txt · §12 Gate 5; orf-docs/GOVERNANCE_RULES.md
- **Notes:** Gate 5 text accurately restated. No ecosystem marked passed.

## C-088

- **Claim:** Gate 6 Stress Runway: SCR ≥ 1.0 with ≥24 months liquid operating reserve under compound stress.
- **Source:** `whitepapers/orf-v1.0.pdf · §12`
- **Validation status:** SUPPORTS
- **Evidence:** sources/orf-whitepaper.txt · §12 Gate 6; orf-docs/GOVERNANCE_RULES.md
- **Notes:** Gate 6 text accurately restated. No ecosystem marked passed.

## C-089

- **Claim:** Gate 7 Liability Coverage: all SLAs, retainers, refund obligations fully backed by capacity and wind-down reserves.
- **Source:** `whitepapers/orf-v1.0.pdf · §12`
- **Validation status:** SUPPORTS
- **Evidence:** sources/orf-whitepaper.txt · §12 Gate 7; orf-docs/GOVERNANCE_RULES.md
- **Notes:** Gate 7 text accurately restated. No ecosystem marked passed.

## C-090

- **Claim:** Gate 8 Independent Audit: annual financial and operational audits published by independent third party.
- **Source:** `whitepapers/orf-v1.0.pdf · §12`
- **Validation status:** SUPPORTS
- **Evidence:** sources/orf-whitepaper.txt · §12 Gate 8; orf-docs/GOVERNANCE_RULES.md
- **Notes:** Gate 8 text accurately restated. No ecosystem marked passed.

## C-091

- **Claim:** No hard gate compensates for failure of another; additive maturity scoring is rejected.
- **Source:** `whitepapers/orf-v1.0.pdf · §12`
- **Validation status:** SUPPORTS
- **Evidence:** whitepaper §12; GOVERNANCE_RULES §2 Level 3 rule
- **Notes:** Non-compensable gates / no additive scoring.

## C-092

- **Claim:** Six Revenue Correlation Classes: (1) Native Network Activity, (2) Native Token Price, (3) Enterprise Contract Revenue, (4) Membership & Certification, (5) Capital-Market Return, (6) Philanthropic/Voluntary.
- **Source:** `whitepapers/orf-v1.0.pdf · §13`
- **Validation status:** SUPPORTS
- **Evidence:** whitepaper §13
- **Notes:** Six correlation classes listed in paper.

## C-093

- **Claim:** Independence Step 1: where ≥8 quarters of receipts exist, classes correlating above 0.6 treated as single class for Gate 4.
- **Source:** `whitepapers/orf-v1.0.pdf · §13`
- **Validation status:** SUPPORTS
- **Evidence:** whitepaper §13 Independence Step 1
- **Notes:** Normative test rule (0.6 threshold).

## C-094

- **Claim:** Independence Step 2: common risk-driver analysis when insufficient history.
- **Source:** `whitepapers/orf-v1.0.pdf · §13`
- **Validation status:** SUPPORTS
- **Evidence:** whitepaper §13 Step 2
- **Notes:** Normative.

## C-095

- **Claim:** Independence Step 3: compound stress co-movement test required in all cases.
- **Source:** `whitepapers/orf-v1.0.pdf · §13`
- **Validation status:** SUPPORTS
- **Evidence:** whitepaper §13 Step 3; GOVERNANCE_RULES SCR stress
- **Notes:** Normative; required in all cases.

## C-096

- **Claim:** P-scale (P0 Conceptual … P5 Cycle-Tested) answers 'does this work somewhere?'; D-scale (D0 Hypothesis … D5 Resilient) answers 'does this work here?'.
- **Source:** `whitepapers/orf-v1.0.pdf · §14`
- **Validation status:** SUPPORTS
- **Evidence:** whitepaper §14
- **Notes:** P vs D question split.

## C-097

- **Claim:** External precedent is not a local D rating; P4 elsewhere can still be D0 locally until receipts exist.
- **Source:** `whitepapers/orf-v1.0.pdf · §14 / Catalog architecture`
- **Validation status:** SUPPORTS
- **Evidence:** INSTRUMENT_CATALOG §1; whitepaper §14
- **Notes:** External P ≠ local D.

## C-098

- **Claim:** Tier 1 feasibility model uses an illustrative ~$3.0M baseline maintenance cost floor and compound stress (protocol fees −50%, enterprise −40%, membership −30%, capital yield −40%, certification flat).
- **Source:** `whitepapers/orf-v1.0.pdf · §15 / GOVERNANCE_RULES SCR`
- **Validation status:** SUPPORTS
- **Evidence:** VALIDATION.md Evidence Audit Log; whitepaper §15; GOVERNANCE_RULES SCR
- **Notes:** Explicitly illustrative / requires ecosystem-specific tuning. Stage 0.

## C-099

- **Claim:** ORF Operator must publish Quarterly Replenishment Audit with gross receipts, cost-to-collect, net contribution, RCR, MCR, SCR, SLA liabilities/wind-down status (and 12-field reporting standard).
- **Source:** `whitepapers/orf-v1.0.pdf · §17 / GOVERNANCE_RULES §8`
- **Validation status:** SUPPORTS
- **Evidence:** whitepaper §17; GOVERNANCE_RULES §8
- **Notes:** Quarterly audit requirement.

## C-100

- **Claim:** Named failure modes include Treasury Relabeling and Endowment Fantasy.
- **Source:** `whitepapers/orf-v1.0.pdf · Glossary / §18`
- **Validation status:** SUPPORTS
- **Evidence:** whitepaper Glossary / §18
- **Notes:** Named failure modes present in paper.

## C-101

- **Claim:** No ORF gate is marked passed; specifications under orf/ remain Stage 0.
- **Source:** `whitepapers/orf-v1.0.pdf · §19 / whitepapers README / ORF_WHITEPAPER.md`
- **Validation status:** SUPPORTS
- **Evidence:** VALIDATION.md; ORF_WHITEPAPER.md; orf-docs/START_HERE.md
- **Notes:** No ORF gate marked passed; orf/ specs Stage 0.

## C-102

- **Claim:** Where ORF_ERRATA.md differs from orf-v1.0.pdf, the errata controls until sentences are pasted into a new PDF.
- **Source:** `whitepapers/ORF_ERRATA.md · preamble`
- **Validation status:** SUPPORTS
- **Evidence:** sources/ORF_ERRATA.md preamble; sources/ORF_WHITEPAPER.md
- **Notes:** Errata controls over PDF — authoritative process claim.

## C-103

- **Claim:** ERRATA Evidence summary: Cumulative Superchain revenue 17,756 ETH all-time (Base share 6,210 ETH; OP Mainnet 11,170 ETH); 26.4M OP Retro Funding across 437 grantees — Foundation Year 3 budget update 24 June 2025; residual not itemized; not independent audit.
- **Source:** `whitepapers/ORF_ERRATA.md · Evidence summary`
- **Validation status:** SUPPORTS
- **Evidence:** ORF_ERRATA.md Evidence summary; https://gov.optimism.io/t/collective-year-3-budget-update-and-year-4-budget-outlook/10057
- **Notes:** Errata figures match Year 3 post; residual not itemized; Medium under Gate 2.

## C-104

- **Claim:** ERRATA: 8 January 2026 buyback proposal reports 5,868 ETH collected over preceding twelve months — different window, not revision of all-time figure.
- **Source:** `whitepapers/ORF_ERRATA.md · Evidence summary`
- **Validation status:** SUPPORTS
- **Evidence:** ORF_ERRATA.md; https://optimism.io/blog/op-token-buybacks
- **Notes:** Different window from all-time figure — correctly flagged.

## C-105

- **Claim:** ERRATA Optimism: formula is standard-chain rule; OP Mainnet contributes 100% of revenue; August 2024 'no exceptions' sentence is superseded.
- **Source:** `whitepapers/ORF_ERRATA.md · §2 Optimism`
- **Validation status:** SUPPORTS
- **Evidence:** ORF_ERRATA.md; https://docs.optimism.io/governance/capital-allocation
- **Notes:** Standard-chain vs OP Mainnet 100% carve-out.

## C-106

- **Claim:** ERRATA Optimism buyback: governance approved late Jan 2026 a twelve-month pilot beginning February allocating 50% of Superchain sequencer revenue; CoinDesk reports 84.4% in favor and 'net' wording — cite the vote, not only the proposal.
- **Source:** `whitepapers/ORF_ERRATA.md · §2 Optimism`
- **Validation status:** SUPPORTS
- **Evidence:** ORF_ERRATA.md; CoinDesk 2026-01-28; vote.optimism.io proposal
- **Notes:** Pilot wording + cite vote. incoming vs net discrepancy noted.

## C-107

- **Claim:** ERRATA ENS: KPK 2025 review (21 Jan 2026): $18.22M ops revenue, $17.54M ops expenses, endowment covering 20.3%, Dec 2025 AUM $113.86M; EP 6.46 later snapshot ~$93.4M AUM, >$8M net DeFi returns, $16.4M expense base — same institution, two closes.
- **Source:** `whitepapers/ORF_ERRATA.md · §2 ENS`
- **Validation status:** SUPPORTS
- **Evidence:** ORF_ERRATA.md §2 ENS; KPK thread; EP 6.46
- **Notes:** Two closes documented; do not stack.

## C-108

- **Claim:** ERRATA: Correct spelling Hoffmann (not Hoffman) for HBS Working Paper 24-038.
- **Source:** `whitepapers/ORF_ERRATA.md · §2 ENS / bibliography`
- **Validation status:** SUPPORTS
- **Evidence:** ORF_ERRATA.md; HBS item 65230
- **Notes:** Spelling correction.

## C-109

- **Claim:** ERRATA: Do not change ORF draft's Synopsys 96% vs Hoffmann $4.15B/$8.8T split; OMF paper merges those and writes '$4.15 trillion' — leave OMF for separate erratum.
- **Source:** `whitepapers/ORF_ERRATA.md`
- **Validation status:** SUPPORTS
- **Evidence:** ORF_ERRATA.md
- **Notes:** Keep Synopsys/Hoffmann split; do not copy OMF $4.15 trillion merge error.

## C-110

- **Claim:** ERRATA Protocol Guild: Q2 2026 membership audit records 196 funded members as of 22 May 2026 (up from 187); dollar totals $7.2M/6,202 donors and $80M+ not recoverable from rendered primary page — do not publish as High until annual report quoted.
- **Source:** `whitepapers/ORF_ERRATA.md · Protocol Guild`
- **Validation status:** SUPPORTS
- **Evidence:** ORF_ERRATA.md Protocol Guild; protocolguild.org Q2 2026 audit
- **Notes:** Membership recoverable; dollars downgraded.

## C-111

- **Claim:** ERRATA Claims to mark unverified: Polkadot ~$70.6M / Anemoy $1.5M / referenda #1122,#1416,#1591; POSM 5.885M ADA / $300K bounty; Octant Epoch 8 ~460 ETH; Deep Funding $220K/34 repos/5,000+ deps.
- **Source:** `whitepapers/ORF_ERRATA.md · Claims to mark unverified`
- **Validation status:** SUPPORTS
- **Evidence:** ORF_ERRATA.md · Claims to mark unverified
- **Notes:** Meta-claim correctly lists unverified magnitudes.

## C-112

- **Claim:** ERRATA Tidelift: change 'acquired by Sonar' to 'under a definitive agreement announced by Sonar to acquire Tidelift' unless closing announcement added.
- **Source:** `whitepapers/ORF_ERRATA.md · Tidelift`
- **Validation status:** SUPPORTS
- **Evidence:** ORF_ERRATA.md Tidelift; Sonar PR
- **Notes:** Wording correction authoritative.

## C-113

- **Claim:** ERRATA grants-era insert: Gitcoin Grants is Family D money plus an allocation engine — not replenishment; Retro Funding deploys resources, does not replenish them; ORF starts where the round ends.
- **Source:** `whitepapers/ORF_ERRATA.md · §2 grants-era insert`
- **Validation status:** SUPPORTS
- **Evidence:** ORF_ERRATA.md grants-era insert; https://gitcoin.co/program
- **Notes:** Gitcoin = Family D + allocation engine, not replenishment.

## C-114

- **Claim:** ERRATA: Gitcoin program page displays (without audit trail on page) 3,715 projects, 3.8M unique donations, >$50M — site's counters; do not upgrade.
- **Source:** `whitepapers/ORF_ERRATA.md · grants-era insert`
- **Validation status:** PARTIAL
- **Evidence:** ORF_ERRATA.md; https://gitcoin.co/program
- **Notes:** Counters are site-displayed without audit trail on page — errata already says do not upgrade.

## C-115

- **Claim:** An ecosystem MAY NOT claim Level 3 'Self-Sustaining' maturity based on additive point scores alone; must satisfy all eight hard gates.
- **Source:** `orf/GOVERNANCE_RULES.md · §2`
- **Validation status:** SUPPORTS
- **Evidence:** orf-docs/GOVERNANCE_RULES.md §2
- **Notes:** Level 3 / eight gates rule.

## C-116

- **Claim:** Compound stress scenario for SCR: protocol fees −50%, enterprise assurance −40%, membership dues −30%, capital yield −40%, certification held flat.
- **Source:** `orf/GOVERNANCE_RULES.md · §3 SCR`
- **Validation status:** SUPPORTS
- **Evidence:** orf-docs/GOVERNANCE_RULES.md §3 SCR
- **Notes:** Compound stress scenario parameters as specified.

## C-117

- **Claim:** A revenue family is not, by itself, a payer for RCR purposes.
- **Source:** `orf/GOVERNANCE_RULES.md · §3 RCR`
- **Validation status:** SUPPORTS
- **Evidence:** GOVERNANCE_RULES.md §3 RCR; whitepaper §11 interpretive note
- **Notes:** Family ≠ payer.

## C-118

- **Claim:** Where a structural mechanism has an identifiable dominant counterparty, that counterparty is a payer and RCR applies in full.
- **Source:** `orf/GOVERNANCE_RULES.md · §3 MCR/RCR`
- **Validation status:** SUPPORTS
- **Evidence:** GOVERNANCE_RULES.md §3; whitepaper RCR note
- **Notes:** Dominant counterparty = payer.

## C-119

- **Claim:** If ecosystem fails Service Capacity Test, restricted to Instrument B.1 Open Infrastructure Assurance Subscriptions (no SLA guarantees).
- **Source:** `orf/GOVERNANCE_RULES.md · §5`
- **Validation status:** SUPPORTS
- **Evidence:** GOVERNANCE_RULES.md §5
- **Notes:** SCT fail → B.1 only.

## C-120

- **Claim:** Neutral Legal Entity (PCF wrapper) signs SLAs, invoices, files W-8/W-9 taxes, maintains insurance, routes net proceeds to Governed Treasury.
- **Source:** `orf/GOVERNANCE_RULES.md · §6`
- **Validation status:** SUPPORTS
- **Evidence:** GOVERNANCE_RULES.md §6; PCF wiki as design analog
- **Notes:** NLE duties as specified; PCF is template analog not ORF deployment.

## C-121

- **Claim:** RMF MAY NOT be categorized automatically as U.S. IRS PRI without explicit tax counsel opinion.
- **Source:** `orf/GOVERNANCE_RULES.md · §7`
- **Validation status:** SUPPORTS
- **Evidence:** GOVERNANCE_RULES.md §7
- **Notes:** No automatic PRI.

## C-122

- **Claim:** Quarterly Replenishment Audit must include: gross by family, cost-to-collect, net to treasury, RCR, MCR, SCR, SLA liability/wind-down status.
- **Source:** `orf/GOVERNANCE_RULES.md · §8`
- **Validation status:** SUPPORTS
- **Evidence:** GOVERNANCE_RULES.md §8; EVIDENCE_REGISTER §4 twelve fields
- **Notes:** Quarterly audit contents.

## C-123

- **Claim:** Every catalog entry classified by Value-Origin Layer and Instrument Type, plus External Precedent P0–P5 and Local Deployment D0–D5.
- **Source:** `orf/INSTRUMENT_CATALOG.md · §1`
- **Validation status:** SUPPORTS
- **Evidence:** INSTRUMENT_CATALOG.md §1
- **Notes:** Catalog architecture.

## C-124

- **Claim:** A.1 Protocol Fee Routing (τ Split): P4 Scaled (Cardano/Polkadot L1); Local D0 until authorized fee split and cash arrived; Transferability Medium.
- **Source:** `orf/INSTRUMENT_CATALOG.md · A.1`
- **Validation status:** PARTIAL
- **Evidence:** INSTRUMENT_CATALOG.md A.1; EVIDENCE_REGISTER Cardano/Polkadot
- **Notes:** P4 Scaled is catalog rating. Local D0 until authorized. Fee-split production existence PARTIAL; magnitudes often unverified.

## C-125

- **Claim:** A.2 Sequencer Profit Contribution: Optimism Superchain greater of 15% net profit or 2.5% gross fees — P4 Scaled (L2); Local D0 until split authorized and cash arrived; Transferability High for L2.
- **Source:** `orf/INSTRUMENT_CATALOG.md · A.2`
- **Validation status:** PARTIAL
- **Evidence:** INSTRUMENT_CATALOG.md A.2; docs.optimism.io; EVIDENCE_REGISTER
- **Notes:** Matches standard-chain formula. Remember OP Mainnet 100% carve-out (ERRATA). Medium evidence.

## C-126

- **Claim:** A.3 Canonical Protocol Service Fees: ENS Registrar .eth — P4 Scaled; Local D0 without own canonical namespace; Transferability Low/Contextual.
- **Source:** `orf/INSTRUMENT_CATALOG.md · A.3`
- **Validation status:** PARTIAL
- **Evidence:** INSTRUMENT_CATALOG.md A.3; ENS KPK/EP6.46
- **Notes:** ENS registrar as P4 pattern SUPPORTS; local D0 without own canonical service correct.

## C-127

- **Claim:** A.4 Monetary Expansion Allocation: issuance is not non-inflationary revenue; transitional only; cannot count toward self-sustainability metrics.
- **Source:** `orf/INSTRUMENT_CATALOG.md · A.4 CRITICAL POLICY NOTICE`
- **Validation status:** SUPPORTS
- **Evidence:** INSTRUMENT_CATALOG.md A.4 CRITICAL POLICY NOTICE
- **Notes:** Issuance exclusion.

## C-128

- **Claim:** B.1 Open Infrastructure Assurance Subscription: Tidelift P4 externally; Local D1 Buyer Validated usual before receipts; $25k–$100k+; Transferability High.
- **Source:** `orf/INSTRUMENT_CATALOG.md · B.1`
- **Validation status:** PARTIAL
- **Evidence:** INSTRUMENT_CATALOG.md B.1; Sonar/Tidelift PR
- **Notes:** Tidelift P4 external is catalog judgment; customers sourced; acquisition wording per C-025/C-112.

## C-129

- **Claim:** B.2 Extended Lifecycle Support & SLA: Red Hat ELC / Canonical Ubuntu Advantage live precedent; Local D0 for generic DAOs; $75k–$250k+; Must pass Service Capacity Test; ORFSlaVault.sol removed 20 Aug 2026 — not an implementation.
- **Source:** `orf/INSTRUMENT_CATALOG.md · B.2`
- **Validation status:** PARTIAL
- **Evidence:** INSTRUMENT_CATALOG.md B.2; VALIDATION.md contracts removed 2026-08-20
- **Notes:** Red Hat/Canonical as live LTS precedent qualitatively PARTIAL (not dossier-fetched here). ORFSlaVault.sol NOT an implementation.

## C-130

- **Claim:** C.1 Ecosystem Sustaining Consortium Membership: Linux Foundation membership tiers P4 Scaled; Local D0 until membership receipts; $10k–$250k+; Transferability High.
- **Source:** `orf/INSTRUMENT_CATALOG.md · C.1`
- **Validation status:** PARTIAL
- **Evidence:** INSTRUMENT_CATALOG.md C.1; linuxfoundation.org
- **Notes:** LF membership P4 pattern qualitative.

## C-131

- **Claim:** C.2 Certified Ecosystem Provider / Sustainer: CNCF Certified Kubernetes 90+ offerings P4; payment buys testing not passing result; Local D0 until own conformance suite; $10k–$50k.
- **Source:** `orf/INSTRUMENT_CATALOG.md · C.2`
- **Validation status:** PARTIAL
- **Evidence:** INSTRUMENT_CATALOG.md C.2
- **Notes:** Same as C-062 — conformance model SUPPORTS; 90+ count PARTIAL.

## C-132

- **Claim:** C.3 Professional Developer Certification & Training: LF CKA/CKAD P3 Sustained; Local D0 until receipts; $300–$750; Transferability Medium.
- **Source:** `orf/INSTRUMENT_CATALOG.md · C.3`
- **Validation status:** PARTIAL
- **Evidence:** INSTRUMENT_CATALOG.md C.3
- **Notes:** Same as C-063.

## C-133

- **Claim:** D.1 Protocol Guild-Style Project Token/Yield Pledges: voluntary 1% pledges vesting revocable; dollar totals not restated in catalog; Local D0 until receipts; Transferability High.
- **Source:** `orf/INSTRUMENT_CATALOG.md · D.1`
- **Validation status:** ERRATA
- **Evidence:** INSTRUMENT_CATALOG.md D.1; ORF_ERRATA Protocol Guild
- **Notes:** Mechanism (1% pledges, vesting, revocable) SUPPORTS; dollar scale UNVERIFIABLE per errata.

## C-134

- **Claim:** D.2 Validator Stake Pool Maintenance Pledges: Cardano Mission-Driven Pools / POSM community pools P2 Operating; Local D2 Paid Pilot; Transferability Medium.
- **Source:** `orf/INSTRUMENT_CATALOG.md · D.2`
- **Validation status:** PARTIAL
- **Evidence:** INSTRUMENT_CATALOG.md D.2; precedents/CARDANO_POSM.md; Intersect POSM explainer
- **Notes:** Delegation-layer analog described; P2/D2 ratings are catalog judgments.

## C-135

- **Claim:** E.1 Governed Endowment IPS & Liquid Reserve Yield: ENS EP 6.46 and Octant staking announcement as external precedent; magnitudes not restated on rating line; Local D0 until own IPS receipts; requires $60M–$100M+ principal for ~$3M/yr yield.
- **Source:** `orf/INSTRUMENT_CATALOG.md · E.1`
- **Validation status:** PARTIAL
- **Evidence:** INSTRUMENT_CATALOG.md E.1; ENS EP6.46; Octant announcement
- **Notes:** ENS IPS SUPPORTS as endowment precedent; Octant is announcement not operating audit.

## C-136

- **Claim:** Rail S.1 Drips Protocol: Routing Rail — moves existing money; Live Precedent DripsHub; does not count as independent revenue.
- **Source:** `orf/INSTRUMENT_CATALOG.md · S.1`
- **Validation status:** SUPPORTS
- **Evidence:** INSTRUMENT_CATALOG.md S.1; sources/tools/DRIPS_PROTOCOL.md
- **Notes:** Routing rail — does not count as independent revenue. Correct taxonomy.

## C-137

- **Claim:** Rail S.2 Superfluid CFA: Routing Rail — continuous streaming; Live Precedent; does not count as independent revenue.
- **Source:** `orf/INSTRUMENT_CATALOG.md · S.2`
- **Validation status:** SUPPORTS
- **Evidence:** INSTRUMENT_CATALOG.md S.2; sources/tools/SUPERFLUID.md
- **Notes:** Routing rail taxonomy correct.

## C-138

- **Claim:** Engine S.3 AI-Assisted Impact & Dependency Allocation: Research-Stage (Deep Funding, Gitcoin AI); Allocation Mechanism — determines splits, not revenue.
- **Source:** `orf/INSTRUMENT_CATALOG.md · S.3`
- **Validation status:** SUPPORTS
- **Evidence:** INSTRUMENT_CATALOG.md S.3; ORF_ERRATA Deep Funding/Gitcoin AI
- **Notes:** Allocation engine / research-stage — not independent revenue.

## C-139

- **Claim:** Risk P.1 Open Source Security Mutuals: D0 Hypothesis — underwriting security pools with risk-adjusted premiums.
- **Source:** `orf/INSTRUMENT_CATALOG.md · P.1`
- **Validation status:** SUPPORTS
- **Evidence:** INSTRUMENT_CATALOG.md P.1
- **Notes:** Explicitly D0 Hypothesis — no overclaim.

## C-140

- **Claim:** Risk P.2 Recoverable Mission Funding (RMF/PRI): D1 Buyer Validated — repayable mission investments under strict IRS PRI guidelines.
- **Source:** `orf/INSTRUMENT_CATALOG.md · P.2`
- **Validation status:** PARTIAL
- **Evidence:** INSTRUMENT_CATALOG.md P.2; GOVERNANCE_RULES §7
- **Notes:** D1 Buyer Validated is catalog rating; still requires tax counsel (C-121). Not production ORF proof.

## C-141

- **Claim:** Risk P.3 Infrastructure Revenue Bonds: D0 Hypothesis — debt backed by verified recurring SLA or protocol fee cash flows.
- **Source:** `orf/INSTRUMENT_CATALOG.md · P.3`
- **Validation status:** SUPPORTS
- **Evidence:** INSTRUMENT_CATALOG.md P.3
- **Notes:** Explicitly D0 Hypothesis.

---

## Researchy live-web delta (2026-09-24 PT)

**Inputs:** `use-cases/researchy-validation.md` (23 rows: Validated 17 · Partial 4 · Broken 0 · Needs update 2); `use-cases/web2-web3-prototypes-expansion.md` (N1–N12).

### Status flips on C-001…C-141

**None.** Live HTTP confirms primary URLs; ERRATA magnitude discipline unchanged.

| Claim cluster | Prior status | Researchy effect |
|---|---|---|
| C-020–C-022, C-103–C-106 (Optimism) | PARTIAL / CONFLICTS / ERRATA SUPPORTS | URLs **200**; Year 3 / buyback / OP Mainnet carve-out guidance **unchanged** |
| C-023–C-024, C-107 (ENS) | PARTIAL / SUPPORTS | KPK + EP 6.46 **200**; **do not stack** closes — unchanged |
| C-025, C-112 (Tidelift) | CONFLICTS / ERRATA SUPPORTS | Sonar “to acquire” PR **200**; still **definitive agreement**, not acquired |
| C-026, C-110 (Protocol Guild) | ERRATA / SUPPORTS | Q2 2026 audit **200**; 196 members hold; **$7.2M / $80M+ still not High** |
| C-027–C-029 (Polkadot / POSM / Octant) | ERRATA | Wikis/explainers/announcement **200**; spend/budget/epoch magnitudes **still Unverified** |
| C-030, C-113–C-114 (rails / Gitcoin) | PARTIAL / SUPPORTS | Live; taxonomy (≠ replenishment) unchanged |
| C-101 (no gate passed) | SUPPORTS | Reinforced — Stage 0 |

### Catalog hygiene (not claim flips)

1. Merit Systems — add https://merit.systems to Sources (Needs update).  
2. Nouns DAO — add https://nouns.wtf; magnitudes remain Unverified (Needs update).

### New prototypes → future claim extraction (not in 141)

Do **not** invent whitepaper claim IDs for these yet. Map for synthesis §3 only:

| Expansion | ORF / OMF map | Claim-risk note |
|---|---|---|
| N1 Open Source Pledge | Family D corporate norm ($2k/dev/yr site rule) | Site counters ≠ audited cash |
| N2 thanks.dev | Routing rail (S.1-adjacent Web2) | Not independent revenue |
| N3 Geomys | OMF retainers / Family B-adjacent employment | Vendor firm ≠ Neutral Legal Entity |
| N4 HeroDevs NES | Family B EOL assurance | Distinct from Tidelift; vendor marketing magnitudes UNKNOWN |
| N5 Open Source Endowment | Family E Web2 endowment | Publisher corpus/spend-rate — not Gate 2 |
| N6 NLnet / NGI Zero | OMF public grants | One-way program capital |
| N7 Prototype Fund | OMF early stipends | Public sprint ≠ replenishment |
| N8 CURIOSS / UC OSPO | dOSPO campus lab | Grant/institutional, not earned portfolio |
| N9 Rust Foundation | Family C + Maintainers Fund | Membership / fund — no eight-gate claim |
| N10 Alpha-Omega | OMF security maintainer support | OpenSSF-associated; not five-family ORF |
| N11 Polar.sh | OMF/D maintainer monetization rail | Early; Gate 2 discipline required |
| N12 DPGA | Public-goods certification adjacency | Not ORF closed loop |

**Re-score owner:** USe Me · **Narrative fold:** Give me Purposise · **Pages:** Projects Manager after Christian go.
