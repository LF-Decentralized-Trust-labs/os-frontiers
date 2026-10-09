# Top-100 audit QA rubric (does dOSPO + OMF + ORF solve the crisis?)

> **Owner:** QA (executor). **Applies to:** every row of Researchy's `chains/top100-audit.md`, plus PR batches 1–4 on `LF-Decentralized-Trust-labs/os-frontiers`. **Version:** v1.0, 9 Oct 2026 05:23 PT. It includes the 05:19 scope change to the three-function model and the 05:20 whitepaper-only rule.
> **Framing (from Christian):** the question is whether the 3-piece model as written closes the gap. **Chains are examples, not inputs that change the model.** Definitions come **only** from the repo whitepapers and `whitepapers/ORF_ERRATA.md`. Where the errata differs from `orf-v1.0.pdf`, the errata controls. `orf/`, `omf/` and `dospo/` specs are Stage 0, and where they differ from the paper, the paper controls (`whitepapers/README.md`).
> **Result per row:** **PASS**, or **FIX** (with rule ID and reason). FIX rows are logged in `top100-qa-log.md` and are never silently edited in Researchy's file.

---

## A. Global rules (any violation = FIX)

| ID | Check |
|---|---|
| A1 | **Stage 0.** The row says nothing that implies a Hard Gate is passed, "self-sustaining", "runs ORF", or Minimum Viable ORF or OMF is met, unless every item of that minimum is sourced. No row is marked as passing any of the 8 Hard Gates (`orf-v1.0.pdf` §12). |
| A2 | **Not replenishment:** issuance or monetary expansion, grants, Retro Funding, Gitcoin, Drips, Superfluid (and other routing rails or allocation engines), treasury drawdown, and returned unspent grants. Per `ORF_ERRATA.md` ("Retro Funding deploys resources. It does not replenish them. OMF is the right layer for that deployment") and MV-ORF item 2 ("Issuance and routing are excluded from replenishment totals", `orf-v1.0.pdf` p.18). |
| A3 | **Every figure** (USD, token amount, %, count) has a **source URL + check date + status** from {**Validated**, **Partial**, **Unverified**, **Unknown**}. Self-reported figures say so. "Unknown" is a valid entry, but a guessed number is not. |
| A4 | **Derived** numbers (token × price, ratios, splits) are labelled *derived*, with inputs and price date. |
| A5 | **No invented figures or quotes.** Every quoted string must be findable on the cited page. Expert positions are paraphrased with source, never presented as endorsements. |
| A6 | **Dating.** Every "as of" is explicit. A superseded figure (e.g. PG 196 → 190) is dated rather than called wrong. |

## B. The three functions: definitions (whitepapers only; quote, don't paraphrase into new scope)

| Function column | Whitepaper definition (cite this, nothing else) | What counts as **Present** | Never counts as Present |
|---|---|---|---|
| **dOSPO-like** (Governance Primitive: *who decides*) | "A dOSPO is a community-mandated coordination layer that separates policy authority from operational execution in order to steward open source infrastructure within decentralized Web3 ecosystems. It derives legitimacy from decentralized governance and operates through a neutral, replaceable execution function constrained by explicit mandate." It is time-bounded, with a mandate renewed on a 2–4 year charter cycle. — `dospo-whitepaper-v1.0.pdf` p.13. Series label: "Governance Primitive · Who decides" (`orf-v1.0.pdf` p.8; p.2 author's note). | A sourced body with **(i) community mandate, (ii) policy/execution separation, (iii) replaceable operator, (iv) time-bounded or renewable charter**. Partial = some of (i)–(iv), named. | A foundation or company deciding alone with no community mandate. A token vote on monetary parameters only (e.g. an issuance change) with no OSS stewardship mandate. |
| **OMF-like** (Operational Framework: *how resources go out*) | "OMF is a portable operational architecture for sustaining decentralized open source infrastructure … In ecosystems that adopt coordination bodies such as a … dOSPO, OMF functions as the execution layer." — `open-maintenance-framework-omf-v1.0.pdf` p.5. Programs: "Maintainer Retainers, Code Bounties, Contributor Pathways, Operational Support, Incubation, and Resilience programs" (`orf-v1.0.pdf` p.8). **Minimum Viable OMF** = all five of: dependency audit · program governance authority · ≥1 sustainment program · transparent reporting (≥ quarterly) · portfolio review (OMF p.15). | A sourced, recurring maintenance-deployment program (retainer, bounty, contributor pathway, tooling stewardship). Present = recurring and authorized. Partial = one-off or episodic grants only, or programs without reporting. Say which MV-OMF items are met. | A VC fund, accelerator or SAFE equity (that's investment, not maintenance deployment). Buybacks or burns. |
| **ORF-like** (Economic Framework: *how resources come back*) | "The ORF defines the replenishment layer (how resources come back)" (`orf-v1.0.pdf` p.2). Replenishment portfolio: "five revenue families, net-contribution accounting, diversification rules, hard sustainability gates, and deployment evidence standards" (p.8). **Minimum Viable ORF** = verified cost floor · classified inflow inventory (issuance and routing excluded) · ≥1 earned instrument collecting real receipts on net contribution · net-contribution reporting · ratio and gate review cadence (p.18). | **Present** only if a **non-issuance, recurring inflow** (Family A structural fee share, B enterprise earned, C membership/certification, or E capital income, with D voluntary pledges allowed as a family) **flows back to an OSS-maintenance treasury**, with the mechanism named and sourced. Partial = collection exists but isn't routed to maintenance, isn't net-accounted, or is mixed with issuance. | **Grants alone or issuance alone are never ORF-like Present** (see C2). Fee burns or buybacks, validator income, Retro/Gitcoin/Drips/Superfluid rounds, foundation drawdown, unspent-grant returns, VC investment. |

**Label check (B0):** the scope note said "dOSPO = Governance, OMF = Operations, ORF = Collection". The whitepapers' own labels are **dOSPO = Governance (who decides)**, **OMF = Operational/Deployment (how resources go out)**, and **ORF = Economic/Replenishment (how resources come back)** (`whitepapers/README.md`; `orf-v1.0.pdf` pp.2, 8). "Collection" is one *layer inside* ORF (the collection layer before the governed treasury), not ORF's definition. **Rows must use the whitepaper wording.** A row that treats "has a fee-collection mechanism" as ORF-like Present fails C2.

Spec-level notes (Stage 0, the paper controls): `dospo/START_HERE.md` adds "zero treasury custody" and `omf/START_HERE.md` a "5-Requirement Compliance Bar". These may be cited as **spec**, but not as the definition.

## C. Row checks for the three-function columns

| ID | Check |
|---|---|
| C1 | **Definitions match** §B exactly. A row that redefines a function (e.g. "ORF-like = has a treasury", "dOSPO-like = has a foundation") = FIX. |
| C2 | **ORF-like = Present requires** a named, sourced, non-issuance recurring inflow returning to OSS maintenance. A row whose only evidence is grants, issuance, a dev-fund stream from block subsidy, a burn, or a Retro/Gitcoin/Drips/Superfluid round = **FIX → downgrade to Missing or Partial**. Example: Zcash's 8% + 12% block-subsidy stream is at most **ORF-like Partial (issuance, excluded)**, and its dOSPO-like/OMF-like cells can be Present/Partial on their own evidence. |
| C3 | **Every Present or Partial names its mechanism and cites it** (URL + date + status). Bare "Present" = FIX. |
| C4 | **Missing pieces** must be expressed in whitepaper terms (e.g. "no MV-OMF dependency audit", "no MV-ORF verified cost floor", "no Family B/C instrument"), not as new categories. |
| C5 | **POSM stage** is one of P1–P6 exactly as defined in `posm-cycle-chain-map.md` §2: P1 Funding In · P2 Steward Governance & Programs · P3 Outputs · P4 Commercialization Channels · P5 Commercial Adoption · P6 Return to Treasury. Placement = the furthest stage reached through a connected, evidenced path. "P5 → leak" is used when value exits via burn, validators or buyback. **P6 never counts as reached if the return is issuance-dominated** (cf. Cardano ≈99.8% reserve issuance, derived). |
| C6 | **Direction** is backed by a dated 2025–2026 signal (proposal, vote, announcement) or marked "no signal / stationary". |
| C7 | **Source, date and confidence** are present on the row (High/Medium/Low, or the A3 statuses). Medium or Low rows can't support a Present cell on their own. |
| C8 | **ORF-fit score, if shown:** 5-Question Q1–Q5, each 0–5, total /25 (`orf/5_QUESTION_ASSESSMENT.md`). Phase bands: 0–9 Phase 1, 10–18 Phase 2, 19–25 Phase 3. **Phase 1 cap:** an ecosystem whose dev fund is issuance-funded is reported as **raw score + "Phase 1 (policy cap)"**, as with Zcash in `top10-chains-orf-alignment.md` (raw 11 → Phase 1). Revenue families A–E are tagged ✅/◐/❌/?; burns, validator rewards and buybacks don't count as present. Closed-source L1s get an "out of frame" caveat (as Hyperliquid does). |

## D. PROPOSAL column (most likely place for drift)

| ID | Check |
|---|---|
| D1 | **Labelled.** The cell starts with "PROPOSAL:" (or the column header makes that unmistakable) and uses conditional language ("could", "would plug into"). A proposal stated as fact or as an existing program = FIX. |
| D2 | **Plugs into the spec as written.** It describes a **program or incentive structure** that fits an existing OMF program type or funding instrument, or an existing ORF revenue family or instrument, and **cites the whitepaper section**. Examples: "OMF Maintainer Retainer program (OMF, Program Architecture / Appendix B)"; "ORF Family B enterprise SLA (ORF §8)"; "Family A governance-authorized fee share (ORF §8; Counter-Value / governance-authorization safeguard p.8)". |
| D3 | **Spec-change flag.** Any PROPOSAL that **implies changing the model** = **FIX-SPEC** (escalate, don't fix inline). That includes: a new revenue family, counting issuance, grants or Retro as replenishment, relaxing a Hard Gate or MV-ORF/MV-OMF item, a new framework layer, giving the dOSPO decision authority beyond its mandate, or "the model needs X" claims. |
| D4 | **No numbers invented** in proposals. Any sizing is *derived* from cited inputs or omitted. |
| D5 | **No benefit claimed as fact.** "Would help" is a hypothesis tied to a named missing piece (C4). Nothing implies a gate is passed. |

## E. Consistency with the validated top-10 (no drift)

| ID | Check against the reconciled files (`top10-chains-orf-alignment.md`, `paid-oss-cycle-chain-map.md`, `posm-cycle-chain-map.md`, all reconciled 9 Oct 2026) |
|---|---|
| E1 | **Same ten, same order:** BTC, ETH, BNB, XRP, SOL, TRX, ZEC, HYPE, DOGE, XMR. Cardano is the reference: #11 by market cap with WBT excluded, #12 under the gas-token rule (WBT, CRO, OKB in), per the CoinGecko top-100 snapshot fetched 05:19 PT 9 Oct 2026 (top-10 table uses the separate 03:51 PT snapshot); see `top100-method.md`. |
| E2 | **Scores and phase unchanged:** BTC 5 · ETH 9 · BNB 1 · XRP 2 · SOL 4 · TRX 2 · ZEC 11 raw / Phase 1 cap · HYPE 5 (partly out of frame) · DOGE 1 · XMR 4. All Phase 1. |
| E3 | **POSM placement unchanged:** BTC P3 · ETH P3 (capital-side P6 analog, not adoption) · BNB P5→leak · XRP P5→leak · SOL P5→leak · TRX P5→leak · ZEC P2 · HYPE P5→leak · DOGE P2 · XMR P2 · Cardano P1–P5, P6 ≈99.8% issuance (derived). |
| E4 | **Reconciled figures used** (not the pre-reconciliation ones): OpenSats $29,914,999 / 352 (live counter, 9 Oct 2026; not $32.1M/377) · PG $7,231,668 / 6,202 donors / 190 members as of 5 Aug 2026 (High), ">$80M commitments" Unverified · Zcash lockbox ~68.5k ZEC ≈ $83M plus a 78,750 ZEC multisig (≈146.7k total, Unverified) · Hyperliquid 14,580,774.69 USDC on 3 Oct 2026 (Validated on-chain), DefiLlama Q3 fees $224.2M, ~93% Unverified · TRON $701.4M (self-reported) **and** ≈$77.8M (DefiLlama), Partial · BNB MVB $150K/5% SAFE + $350K uncapped SAFE, Partial · Solana Foundation treasury not published · Cardano ₳5.885M action `8ad3d454…e5d8833e#11`, enacted epoch 576 (12 Aug 2025); ₳4.601M **not submitted on-chain**. |
| E5 | **Three-function cells for the top 10 must be derivable from the reconciled evidence.** Expected ceiling: no top-10 chain is **ORF-like Present** (all collection paths end in burn, validators, buyback or issuance). ETH ORF-like is at most Partial (Family D pledges via PG + Class 2 staking yield); ZEC ORF-like at most Partial (issuance). Any stronger cell = FIX unless new primary evidence is cited. |

## F. Ranking and exclusions

| ID | Check |
|---|---|
| F1 | The row's rank matches `top100-qa-ranking-crosscheck.md`, or the batch cites its own dated snapshot. ±1–2 adjacent swaps from intraday drift are OK, and the snapshot time must be stated. |
| F2 | **Exclusions log** covers **stablecoins, wrapped/staked tokens, RWAs/tokenized funds or stocks, tokens with no native chain, secondary gas tokens, and exchange tokens without their own chain**. The WBT call is applied consistently to CRO/OKB/GT/KCS/BGB/GRX, or the reversal is stated for all of them. |
| F3 | The snapshot must reach chain #100. That needs ~CoinGecko rank 400, so ≥2 pages of 250. |

## G. PR / pre-ship checks (per batch)

| ID | Check |
|---|---|
| G1 | Repo errata changes go through `whitepapers/ORF_ERRATA.md` (the controlling layer), not silent edits to derived docs. Downstream docs (`claims/`, `docs/EVIDENCE_REGISTER.md`, `docs/PRIOR_ART_AND_COMPETITIVE_ANALYSIS.md`, the v1.1 manuscript) must match the errata exactly. |
| G2 | A precedent doc must not claim more than ORF_ERRATA allows. If ORF_ERRATA still lists a claim as unverified, the doc can't present it as High until the errata entry is moved. |
| G3 | No PR says Stage 1 or a passed gate. No figure loses its status label on the way into the repo. |

- 2026-10-09 05:41 PT: E1 Cardano rank changed to the dated two-rule line (Projects Manager call).
