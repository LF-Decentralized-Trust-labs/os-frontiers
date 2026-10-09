# Top-100 audit QA log

> **QA owner:** executor. **Rubric:** `chains/top100-qa-rubric.md` (v1.0, 9 Oct 2026 05:23 PT). **Ranking reference:** `chains/top100-qa-ranking-crosscheck.md` (CoinGecko, data 05:15 PT).
> **Rules:** Researchy's `top100-audit.md` is never edited by QA. Each row gets **PASS** or **FIX (rule ID: reason)**. **FIX-SPEC** = a PROPOSAL that implies changing the dOSPO/OMF/ORF spec; escalate to Christian. Stage 0; no Hard Gate passed.

---

## Pass 1: 9 Oct 2026, 05:24 PT

**Status: waiting on batch 1.** `chains/top100-audit.md` doesn't exist yet, so **0 rows QA'd** (0 PASS / 0 FIX).

**Pre-QA findings from Researchy's working classifier** (`chains/work/classify.py`, read-only, 05:22 PT). These are advisory, since there are no audit rows yet:

| # | Item | Rule | Note |
|---|---|---|---|
| Q-1 | Exchange-origin tokens included (WBT #11, CRO, OKB, BGB, GT, KCS, GRX) | E1 / F2 | Consistent internally, but it **reverses the top-10 WBT exclusion**, so Cardano becomes chain #12. Team decision needed before batch 1 ships (batch 1 = chains 1–25 contains WBT, CRO and OKB). |
| Q-2 | WLD counted as World Chain's L2 token | F2 | WLD isn't World Chain gas (ETH is). Include only if a sourced governance role exists (**Unverified**). Otherwise exclude, as the cross-check does. |
| Q-3 | Lighter, XCN and Beam included (marked UNVERIFIED by Researchy) | F2 | App-rollup or subnet tokens. Fine if the batch keeps the UNVERIFIED flag and gives the rule. |
| Q-4 | Chain set for #79–#100 differs (11 swaps) | F1 | A knock-on effect of Q-1. It resolves once Q-1 is decided. |

---

## Batch 1 pre-ship (9 Oct 2026, 05:24 PT)

> **Status update 9 Oct 2026, 05:40 PT:** each finding below (1-a to 1-l, (2), and Q-1 to Q-4 above) is marked resolved or open in **"Batch 1 QA (ranks 1-25), 2026-10-09" → §0**. The original text is kept unchanged.

Checked against **upstream `main` @ `9a82a9c`** (8 Oct 2026 07:42 PT) and **PR #105 head `5e7b4c7`** (9 Oct 2026 05:18 PT), fetched 05:23 PT.

### (1) Protocol Guild follow-ups (`chains/pg-followups.md`)

**Status: checked at 05:24 PT** against `pg-followups.md` (mtime 05:23 PT, Researchy draft, NOT APPLIED). **Verdict: PASS on figures, dating and $80M+; FIX on 5 items before the PM applies it.**

| # | Check | Result |
|---|---|---|
| 1-a | Core figures **$7,231,668 / 6,202 unique donors / 190 members as of 5 Aug 2026**, High, in C-026, C-110, the L1184 row, EVIDENCE_REGISTER L37/L60 and PRIOR_ART L132 | **PASS.** Exact everywhere; valuation basis stated ($2,634,505 at report value); 196 (22 May 2026) and 187 treated as superseded. |
| 1-b | "Commitments >$80M" stays Unverified | **PASS.** UNVERIFIED in every proposed cell. |
| 1-c | Dating clear | **PASS.** 2025 calendar year; report dated 29 Jan 2026; audit dated 26 Aug 2026; membership as of 5 Aug 2026; checked 2026-10-09. |
| 1-d | Line numbers vs **upstream `main` @ 9a82a9c** | **PASS.** C-026 claim L243, C-110 L915, table L1184, index L32, EVIDENCE_REGISTER L37/L60, PRIOR_ART L131–132/L87 all match upstream. The draft's "no `docs/` on the box" path note is moot: upstream paths are `docs/EVIDENCE_REGISTER.md` and `docs/PRIOR_ART_AND_COMPETITIVE_ANALYSIS.md`, and PR #105 doesn't touch them. |
| 1-e | **Errata identity** | **FIX (G1).** There are **two different PG errata texts**. Box `/workspace/osfl/sources/ORF_ERRATA.md` (05:18 PT) has "Protocol Guild — 2025 figures restored", which adds "$12.4 million vested and distributed" and keeps the old paragraph as SUPERSEDED. **PR #105** `whitepapers/ORF_ERRATA.md` has "Protocol Guild — corrected scale (approved 9 October 2026)", which has **no $12.4M**, replaces the old paragraph, and adds "196 … superseded, not wrong for its date". `pg-followups.md` cites the **box** heading. Pick one text for the PR; downstream cells must cite that heading verbatim. The core figures agree in both. |
| 1-f | Extra figures beyond the errata | **FIX (G1).** EVIDENCE_REGISTER 2a and C-110 add **$12.4M distributed** and **"1% pledges ≈83%"**. Both are Validated in `researchy-chain-check.md`, but the ≈83% isn't in either errata text and the $12.4M isn't in PR #105's. Either add them to the chosen errata entry, or drop them / label them "Validated (annual report), not errata". |
| 1-g | Capture paths | **FIX.** 2b cites `chains/data/pg-*`. In the repo (PR #105) the captures are at **`docs/chains/data/`**. SHA-256 of the box and PR copies match. |
| 1-h | Index line L32 (1d) | **FIX (minor).** The proposed text drops "POSM budget" but keeps the range "C-027–C-030". POSM is in that range, and its removal depends on §4 (₳5.885M) being applied. Keep "POSM budget ('$300K bounty')" in the unverified list, since "$300K" stays unverified even after §4. |
| 1-i | C-026 status label | **FIX (minor).** "ERRATA (superseded entry, High)" sits on a claim line that still contains 196 and $80M+. Use "ERRATA: High for $7,231,668 / 6,202 / 190 (5 Aug 2026); 196 superseded; $80M+ UNVERIFIED", or rewrite the claim line. |
| 1-j | EVIDENCE_REGISTER column mapping | **Advisory.** I checked the draft against the upstream header (Network · Mapped OSF Function · Concrete Mechanism · Revenue/Inflow Type · Deployment Stage · Transferability · Source URL · Confidence): **2a fits that 8-column header.** The L60 table has a different header, so the PM should confirm 2b on apply. |
| 1-k | PRIOR_ART leftovers | **Advisory.** The draft flags "~180" and "$200K" (good). It doesn't flag chart L84–90: "Polkadot $70.6M", "Octant $1.7M" and "Deep Funding $0.22M" are errata-unverified, and "Cardano 2025 Bug Bounty Pool $0.3M" is a planned allocation. Label them or open a follow-up. |
| 1-l | Approval provenance | **Not verifiable by QA.** The drafts say "approved by Projects Manager (delegated by Christian), 2026-10-09". Keep it only if the PM confirms. |

**Approved errata (target text):** PR #105 `whitepapers/ORF_ERRATA.md`, "Protocol Guild — corrected scale (approved 9 October 2026)".
- **$7,231,668** (valued at time of donation; $2,634,505 at report value) from **6,202 unique donors**, per the 2025 Annual Report of 29 Jan 2026.
- **190 funded members as of 5 Aug 2026** (−6 from 196), per the Q3 audit of 26 Aug 2026.
- Confidence **High**. "Commitments above $80 million" stays **Unverified**. The 196 figure is "superseded, not wrong for its date".

**Captures verified (05:24 PT):**
- `chains/data/pg-20260129-annual-report-2025-2026-10-09.html` contains "Total Donations: $7,231,668 valued at time of donation ($2,634,505 current value)" and "6,202 unique donors".
- `chains/data/pg-20260826-q3-quarterly-audit-2026-10-09.html` and its PDF contain "as of August 5, 2026" and "membership is now 190, with a net decrease of 6 (-3.1%) members from 196".
- **SHA-256 of all four captures matches the copies in PR #105** (`docs/chains/data/`).

**Current text the follow-ups must correct (upstream `main`; PR #105 doesn't touch these files):**

| File / location | Current text | Must become (to match errata exactly) |
|---|---|---|
| `claims/orf-claims-validated.md` **C-026** (L241–247) | "Protocol Guild: $7.2M from 6,202 donors (2025); 196 members as of Q2 2026; $80M+ committed." Notes: dollar totals "NOT recoverable … mark unverified" | $7,231,668 (time of donation) from 6,202 unique donors (2025 Annual Report, 29 Jan 2026), **High**. 190 members as of 5 Aug 2026 (Q3 audit, 26 Aug 2026), **High**, with 196 (22 May 2026) superseded. "$80M+ committed" **Unverified**. Evidence: the two URLs + `docs/chains/data/` captures. |
| `claims/…` **C-110** (L913–918) | "ERRATA Protocol Guild: Q2 2026 … 196 funded members as of 22 May 2026 (up from 187); dollar totals … not recoverable" | Restate the **new** errata entry (corrected scale, approved 9 Oct 2026); source `ORF_ERRATA.md · Protocol Guild — corrected scale`. |
| `claims/…` summary L32 and the re-validation table row L1184 | L32 lists PG under "ERRATA unverified (C-026–C-030…)"; L1184 says "196 members hold; $7.2M / $80M+ still not High" | Take PG out of the unverified list (C-027–C-030 and C-111 remain). L1184 becomes "$7,231,668 / 6,202 High; 190 (5 Aug 2026) High; $80M+ Unverified". ("Q2 2026 audit **200**" in that row is an HTTP status, not a count. Leave it, or reword for clarity.) |
| `docs/EVIDENCE_REGISTER.md` L37 and L60 | "**Unverified** for counts and dollars"; "Q2 2026 audit URL returned an empty shell" | Counts and dollars **High** (JS-rendered pages; rendered captures archived 9 Oct 2026); URL changes to the annual report + Q3 audit; $80M+ Unverified. |
| `docs/PRIOR_ART_AND_COMPETITIVE_ANALYSIS.md` §4.5 L132 | "Raised **$7.2M from 6,202 unique donors** in 2025; stewards **187 members** … in 2026" | "$7,231,668 (valued at time of donation) from 6,202 unique donors in 2025; 190 funded members as of 5 Aug 2026". 187 is stale (it's the Q1 2026 count). |
| `docs/PRIOR_ART…` chart L87 | "Protocol Guild 2025 Funds Raised ■ $7.2M" | OK as a rounding of $7,231,668 if labelled "(time of donation)". |

**Pass criteria used for `pg-followups.md`:**
- exact figures **$7,231,668 / 6,202 / 190 / 5 Aug 2026**
- **High**, citing both URLs and the `docs/chains/data/` captures
- "$80M+" stays **Unverified**
- every figure has an explicit date (2025 calendar year, report 29 Jan 2026, audit 26 Aug 2026, as of 5 Aug 2026)
- 196 and 187 marked **superseded** (dated), not "wrong"
- no claim that PG is replenishment beyond Family D (voluntary pledges)

**Out of scope for the PG fix, but flagged in the same file (`PRIOR_ART…`):**
- "~180 core Ethereum L1 developers" and "$200K 2-year ops reserve" are unsourced in this pass.
- The chart shows the errata-unverified "Polkadot $70.6M", "Octant $1.7M" and "Deep Funding $0.22M", plus "Cardano 2025 Bug Bounty Pool $0.3M". That last one was a planned allocation, not utilization (`researchy-chain-check.md`). All should carry Unverified or "allocation" labels.

### (2) Cardano ₳5.885M: move out of "Claims to mark unverified" in `ORF_ERRATA.md`

**Result: FIX (G1/G2). The move hasn't been made in PR #105, and the PR is internally inconsistent.**

| Check | Finding |
|---|---|
| Is ₳5.885M moved out of "Claims to mark unverified"? | **No.** PR #105 `ORF_ERRATA.md` L47 still reads: *POSM "5.885M ADA" and "$300K bounty fully utilized." The Intersect explainer does not contain them.* Upstream main L45 has the same text. |
| Does anything else in PR #105 contradict the errata? | **Yes.** PR #105 `docs/precedents/CARDANO_POSM.md` adds "₳5,885,000. **High (on-chain)**: governance action `8ad3d454f3496a35cb0d07b0fd32f687f66338b7d60e787fc0a22939e5d8833e#11`, enacted epoch 576 (12 August 2025)". The controlling errata still lists it as unverified, so a derived doc claims more than the errata allows (G2). The v1.1 manuscript (L165, and the table row "ADA/$ bounty figures Unverified") is also unchanged. |
| Action ID, epoch and date correct where cited? | **Yes** in `CARDANO_POSM.md`: full hash `…e5d8833e#11`, epoch 576, 12 Aug 2025 all match Koios/Cardanoscan per `researchy-chain-check.md`. Recommend also adding the Cardanoscan URL (`https://cardanoscan.io/govAction/gov_action13tfag48nf94rtjcdq7c06vhkslmxxw9h6c88sl7q5g5nnewcsvlqkqx0ecg`) and the CIP-129 ID. |
| Does it imply ₳4.601M was enacted? | **No (PASS).** `CARDANO_POSM.md` says the 2026–27 request text exists but "no matching treasury-withdrawal action had been submitted on-chain as of epoch 660 (9 October 2026). There is no confirmed POSM funding beyond the 2025 tranche." |
| "$300K bounty fully utilized" | Must **stay** in "Claims to mark unverified". It was a planned ₳600K (≈$300K at $0.50) allocation, not utilization. |

**Required errata change (draft for the PM's batch-1 PR; QA doesn't edit the repo):**
1. In "Claims to mark unverified", change the POSM bullet to: *POSM "$300K bounty fully utilized." The only $300K found is the planned Bug Bounty allocation in the 2025 budget (₳600K at the proposal's $0.50/ADA), not utilization.*
2. Add a new entry, e.g. "## Cardano POSM — 2025 treasury withdrawal (verified on-chain 9 October 2026)": *The 2025 OSC/POSM treasury withdrawal of ₳5,885,000 is governance action `8ad3d454f3496a35cb0d07b0fd32f687f66338b7d60e787fc0a22939e5d8833e#11` (CIP-129 `gov_action13tfag48nf94rtjcdq7c06vhkslmxxw9h6c88sl7q5g5nnewcsvlqkqx0ecg`), submitted epoch 570, ratified epoch 575, enacted epoch 576 (12 August 2025). Confidence: High (on-chain; Koios and Cardanoscan agree). The OSC's 2026–27 request (₳4,601,000) had not been submitted on-chain as of epoch 660 (9 October 2026) and is not enacted. A treasury withdrawal is deployment (OMF), not replenishment.* Cite the Cardanoscan URL and `docs/chains/researchy-chain-check.md`.
3. Mirror this in `orf-whitepaper-v1.1-errata-applied.md` (L165 and the precedent-table row) so the manuscript matches the errata.

**`pg-followups.md` §4 (Researchy's draft of this same move), checked 05:24 PT: PASS, with one addition.**
- It cites action `8ad3d454…e5d8833e#11` with the full hash and CIP-129 ID, Cardanoscan and Koios.
- Epochs 570/575/576 and 12 Aug 2025 (14:44 PT) are correct.
- The ₳4.601M request is explicitly "has not been submitted on-chain … Do not describe it as approved, ratified or enacted", and "$300K bounty" stays unverified with the allocation explanation.
- It labels the withdrawal as OMF deployment, not replenishment.
- **Addition needed:** mirror the change in `whitepapers/orf-whitepaper-v1.1-errata-applied.md` (L165 and the precedent-table row "ADA/$ bounty figures Unverified"). The draft only targets `sources/ORF_ERRATA.md`; in the repo the target is `whitepapers/ORF_ERRATA.md`.

**Ship gate for batch 1:**
- (2) must be applied in the same PR as the `CARDANO_POSM.md` "High (on-chain)" wording (errata moved per `pg-followups.md` §4 + manuscript mirror), or that wording must be held back.
- (1) can ship once FIX 1-e to 1-i are resolved. 1-e (which errata text) is the blocker.

---

## Batch 1 QA (ranks 1-25), 2026-10-09

**Checked:** 9 Oct 2026, 05:25–05:40 PT. **Inputs:** `top100-audit.md` (mtime 05:32 PT), `top100-method.md` (05:32), `pg-followups.md` (05:28), rubric v1.0, `top100-qa-ranking-crosscheck.md` + `tools/qa_rank.py`, `top10-chains-orf-alignment.md` (LOCKED), `posm-cycle-chain-map.md`, `release1-section-3.3-chains.md`, `chains/data/`. **Definitions:** checked against repo PDFs (`whitepapers/dospo-whitepaper-v1.0.pdf` p.13, `open-maintenance-framework-omf-v1.0.pdf` p.5/p.15, `orf-v1.0.pdf` pp.2, 8, 18, §8 pp.23–25). **Errata:** `sources/ORF_ERRATA.md` is byte-identical to PR #105 head `065e843` (`whitepapers/ORF_ERRATA.md`, SHA-256 `bb0b53cf…b904`, fetched 05:33 PT). Researchy's files were not edited.

### Verdict: **SHIP WITH FIXES.** Blockers B-1 and B-2 must be applied before batch 1 ships.

Both blockers are text fixes. Neither changes a Present/Partial/Missing count or a POSM placement. All three summary tables, the POSM counts, the all-missing five and the all-partial five recount exactly from the table. The only count mismatch is the UNVERIFIED tally (12, not 11). No PROPOSAL needs FIX-SPEC.

### 0. Status of earlier findings

| ID | Finding | Status 05:40 PT | Evidence |
|---|---|---|---|
| Q-1 | WBT/CRO/OKB reverse the top-10 WBT exclusion | **Resolved** (team decision) | Projects Manager rule D (gas token of own live chain + public explorer) is applied in `top100-method.md` §4. WBT #11, CRO #23, OKB #24 are included, and GT/KCS/BGB/GRX are deferred to batches 2–4 under the same test (rubric F2 met for batch 1). |
| Q-2 | WLD | **Resolved** | WLD is excluded (World Chain gas is ETH). It is CG #53, outside batch 1. |
| Q-3 | Lighter, XCN, Beam | **Open** (batches 2–4) | Not in batch 1. |
| Q-4 | #79–#100 chain-set swaps | **Open** (batches 2–4) | Needs a rule-D re-run at batch time. |
| 1-a | PG core figures | **Resolved (PASS)** | Re-checked in `pg-followups.md`: $7,231,668 / 6,202 / 190 (5 Aug 2026), High. |
| 1-b | $80M+ Unverified | **Resolved (PASS)** | Unverified everywhere, and "not a candidate" in §4. |
| 1-c | Dating | **Resolved (PASS)** | |
| 1-d | Line numbers / docs path | **Resolved** (nit N-12 remains) | The "no `docs/` on the box" path note is still in `pg-followups.md` l.14. It is harmless, because the draft says to re-locate lines with `rg`. |
| 1-e | Two errata texts | **Resolved** | There is now one text: "Protocol Guild — corrected scale (approved 9 October 2026)" at PR #105 head `065e843`. The box copy is identical (SHA-256 above). |
| 1-f | $12.4M and ≈83% beyond the errata | **Resolved** | Both were removed from the drafts and appear only in `pg-followups.md` §4 "Later-errata candidates (NOT for insertion now)", with source URL, capture and date. Both strings were found in `data/pg-20260129-annual-report-2025-2026-10-09.html`: "totalled $12.4mm in 2025" / "a total of $12.4mm in funding was vested and distributed to Protocol Guild members" and "account for roughly 83% of PG’s total funding to date". |
| 1-g | Capture paths | **Resolved** | The drafts cite `docs/chains/data/…`. |
| 1-h | Index line L32 | **Resolved** | 1d now keeps "POSM $300K bounty" in the unverified list. |
| 1-i | C-026 status label | **Resolved, pending PM confirmation** | The proposed status is plain **ERRATA**, and Notes carry "High for $7,231,668 / 6,202 / 190; 196 superseded; $80M+ UNVERIFIED". The claim line still repeats the paper's original wording ($7.2M; 196 as of Q2 2026; $80M+). That is acceptable as the record of what the paper claimed, but the PM decides whether to rewrite it (see "For Projects Manager"). |
| 1-j | EVIDENCE_REGISTER 2b column mapping | **Open (advisory)** | The draft still says "Columns were inferred from their position. Check them against the table header before applying." The PM must check on apply. |
| 1-k | PRIOR_ART chart leftovers | **Resolved** | §3d labels Polkadot, Octant and Deep Funding as UNVERIFIED, and Cardano $0.3M as "planned, not shown as paid". |
| 1-l | Approval provenance | **Resolved** | "approved 9 October 2026" appears in both errata headings at PR #105 head `065e843`. The PR body says Christian Taylor approved the PR and will merge it. |
| (2) | Cardano ₳5.885M errata move | **Resolved** | PR #105 `ORF_ERRATA.md` adds "Cardano POSM — 2025 treasury withdrawal confirmed on-chain (approved 9 October 2026)". "Claims to mark unverified" now keeps only "$300K bounty fully utilized" (planned ₳600K allocation). The manuscript `orf-whitepaper-v1.1-errata-applied.md` at `065e843` mirrors it (L127, L165, L243). The ship gate for (2) is met. |

### 1. Recount from the table (`top100-audit.md` rows 1–25, parsed 05:30 PT)

| Item | Claimed | Recounted | Result |
|---|---|---|---|
| dOSPO-like P/Pa/M | 0 / 9 / 16 | 0 / 9 / 16 | ✓ |
| OMF-like | 0 / 17 / 8 | 0 / 17 / 8 | ✓ |
| ORF-like | 0 / 11 / 14 | 0 / 11 / 14 | ✓ |
| Combinations (7 rows) | 6 / 5 / 5 / 3 / 3 / 2 / 1 | same chains, same counts | ✓ |
| All Missing | TRON, Whitechain, Bittensor, X Layer, MemeCore | same | ✓ |
| All Partial | Zcash, Monero, Cardano, Bitcoin Cash, Canton | same | ✓ |
| POSM | P1 2 · P2 5 · P3 4 · P5 14 | same. P5 → leak = 9 (BNB, XRP, SOL, TRX, HYPE, WBT, AVAX, CRO, OKB); 0 at P6 | ✓ |
| UNVERIFIED tags | **11** (Zcash 3) | **12** (Zcash 4: fund balance; retainer-like programs; Family D to ZF; "retainer UNVERIFIED" in Missing pieces) | **✗ → F-1** |
| PROPOSAL prefix | all 25 | all 25 start "PROPOSAL (example; not a finding):" | ✓ |
| Market cap and CG rank | 25 rows | all 25 match `coingecko-snapshot-2026-10-09.json` exactly (value and `market_cap_rank`) | ✓ |
| Exclusions (CG 1–49) | 24 = 9 stablecoins + 4 RWA/commodity + 11 no own chain (Researchy, per parent) | Stablecoins 9: USDT, USDC, USDS, USDe (counted once), DAI, USD1, USDG, PYUSD, RLUSD. RWA/commodity 4: FIGR_HELOC, XAUT, USYC, USDY. No own chain 11: LINK, LEO, RAIN, UNI, BTW, QNT, SHIB, ENA, PUMP, AAVE, ONDO. 25 included + 24 excluded = 49 = CG #1–#49, no gaps; each CG id matches the snapshot rank | ✓ (9/4/11 = 24). The table itself never states the split → N-6 |
| Ranking vs cross-check (F1) | | Ranks 1–10 are identical. After removing WBT/CRO/OKB, 11–25 match the cross-check order. AVAX is CG #26 vs #27 (05:19 vs 05:17 snapshot, stated) | ✓ |
| Cardano rank | #12 (rule D) / #11 (WBT excluded) | #12 under rule D at both 05:19 and 03:53 PT (`coingecko-markets-2026-10-09.json`: WBT #15 sits above ADA #17) | ✓ |

### 2. Top-10 lock check (rubric E)

- **Scores:** the batch shows no 5-Question scores, so it can't contradict BTC 5 · ETH 9 · BNB 1 · XRP 2 · SOL 4 · TRX 2 · ZEC 11 raw / Phase 1 cap · HYPE 5 · DOGE 1 · XMR 4. **PASS.**
- **POSM:** BTC P3, ETH P3 (capital-side P6 analog), ZEC/DOGE/XMR P2, BNB/XRP/SOL/TRX/HYPE P5 → leak, Cardano P1–P5 with P6 ≈99.8% issuance (DERIVED). **All match.**
- **ORF ceiling (E5):** no top-10 chain is Present, ETH and ZEC are at most Partial, and HYPE is Partial (consistent with the locked A ◐). **PASS.**
- **Two contradictions with the locked file:** B-1 (MV-ORF item 2 implied met) and B-2 (Zcash Family D).

### 3. Function-cell checks (rubric B/C)

**ORF Partial given only for issuance or unrouted collection:**

| Row | Basis | Does the rubric allow Partial? | Rubric text |
|---|---|---|---|
| Zcash (7) | issuance only (8% + 12% block subsidy) | **Allows Partial (ceiling); Missing not required.** | C2: "Example: Zcash's 8% + 12% block-subsidy stream is at most **ORF-like Partial (issuance, excluded)**". C2 also: "= FIX → downgrade to Missing or Partial". |
| Canton (16) | issuance only (5% of CC mint emissions, CIP-0082) | **Allows Partial**, by direct analogy to the C2 Zcash example (dev fund from protocol issuance aimed at core R&D). | as above |
| Cardano (12) | fee share ≈0.2% mixed with ≈99.8% issuance (DERIVED) | **Allows Partial.** | B: "Partial = collection exists but isn't routed to maintenance, isn't net-accounted, **or is mixed with issuance**." |
| Hyperliquid (8) | unrouted collection (Assistance Fund → buyback/burn) | **Allows Partial.** Burns and buybacks are listed only under "never counts as **Present**". | B: "Partial = **collection exists but isn't routed to maintenance**". Matches the locked top-10 "A ◐ (fee capture exists, routed to buyback/burn)". |
| NEAR (14) | unrouted collection (CONTRACT_PCT 0.3 of gas to contract owners; Nomicon verified) | **Allows Partial** (same B text). | |
| Cronos (23) | unrouted collection (Cronos Labs product revenue → staking, growth, buyback/burn under #1291; #1323 would make it 100% buy-and-burn) | **Allows Partial** (same B text). The #1291 "approved" status is sourced only from the #1323 proposer's text → N-9. | |

Consistency note (advisory, not a FIX): Zcash and Canton issuance streams aimed at OSS are rated Partial, while MemeCore (10% block rewards to the Viral Grants Reserve) and Bittensor are Missing. The split rests on the method's "issuance not aimed at OSS" = Missing (`top100-method.md` §6). The rubric does not contain that criterion. It is defensible and consistently applied, but **rubric v1.1 should state it** (QA action).

**Other cell checks:**
- No dOSPO/OMF/ORF cell is Present, so C7 is moot.
- Grants and Retro never support an ORF Partial (Avalanche Retro9000 is ORF Missing, with "Retro deploys but does not replenish" quoted).
- One-off grants are capped at OMF Partial (Dogecoin CoreFund is Partial). **PASS.**

### 4. PROPOSAL cells (rubric D)

All 25 carry the exact prefix and use conditional language. The cited whitepaper sections exist:
- ORF WP §8 "The Five Revenue Families" (pp.23–25): Protocol Fee Routing, Sequencer Profit Contribution, Product A/B, Family C consortium membership, Family D Protocol Guild-style pledges and "validator stake-pool contributions", Family E capital income.
- ORF WP §4 Minimum Viable ORF (p.18).
- OMF WP §8 Program Architecture: Maintainer Retainer, Code Bounties, Resilience Programs.
- OMF WP Appendix B "Retainer Program Operational Requirements".

The spec IDs also exist: `orf/INSTRUMENT_CATALOG.md` A.1, A.2, A.4, B.1, B.2, C.1, D.1, D.2, E.1; `omf/PROGRAM_PORTFOLIO.md` §2.1, §2.2, §2.4. **No PROPOSAL implies a spec change, so there is no FIX-SPEC.** MemeCore's issuance-funded retainer idea explicitly keeps issuance excluded, which is consistent with ORF p.24 ("It may legitimately finance maintenance as a transitional source. It CANNOT count…"). Page-number nit: N-7.

### 5. Numeric spot-checks (primary pages and on-chain APIs, fetched 05:28–05:38 PT)

| # | Claim (row) | Source checked | Result |
|---|---|---|---|
| 1 | All 25 market caps and CG ranks | `chains/coingecko-snapshot-2026-10-09*.json` | ✓ exact |
| 2 | OpenSats $2,328,000 / $5,639,789 / 674 donations / $3,158,680 (BTC) | opensats.org/blog/2025-year-in-review | ✓ |
| 3 | OpenSats $29,914,999 to 352 grantees (BTC) | opensats.org/funds: "allocated $ 29,914,999 USD … to 352 grantees" | ✓ |
| 4 | Brink ≈$7,800,000 (BTC) | brink.dev 2025 annual report: "approximately $7,800,000" | ✓ |
| 5 | EF A = 15%, glide to 5% over ~5 yrs (ETH) | blog.ethereum.org 2025/06/04: "A = 15% … B = 2.5 years"; "reduce annual opex roughly linearly over the next five years, ending at a long-term 5% baseline" | ✓ (note N-2) |
| 6 | EF ≈70,000 ETH staked (ETH) | blog.ethereum.org 2026/02/24: "Approximately 70,000 ETH" | ✓ |
| 7 | Ripple >$550M since 2017; 26 Feb 2026 (XRP) | ripple.com insights (curl 429; WebFetch OK) | ✓ |
| 8 | SGP-0002 67.001%, 28 Aug 2026 (SOL) | blockdaemon.com: "passed on August 28 with 67.001% of participating stake" | ✓ |
| 9 | TBL "Up to $5,000,000" (TRX) | trondao.org/tron-builders-league | ✓ (page title says "Tron Builders **Club**", N-10) |
| 10 | ZIP 1016 8% / 12% / 420,000 ZEC (ZEC) | raw zip-1016.md: "a minimum of 420,000 ZEC (2% of the total eventual supply) MUST be voted" | ✓ |
| 11 | HL deployers keep up to 50%; AF HYPE burned (HYPE) | hyperliquid gitbook fees | ✓ |
| 12 | CoreFund 5,000,000 / 500,000 DOGE / ≥25 PRs (DOGE) | foundation.dogecoin.com 2022-12-31 | ✓ |
| 13 | Whitechain Builders "up to $300K" per team (WBT) | whitechain.io/builders | ✓ |
| 14 | Whitechain explorer "61.4M transactions" (exclusion note) | explorer.whitechain.io returns HTTP 200, but the figure is JS-rendered | **Not reproducible by QA** → N-11 |
| 15 | Cardano ₳5,885,000, epochs 570/575/576; 104 TW actions, latest proposed 654, tip 660; ₳4,601,000 absent; ₳12M dOSPO/OMF expired (637) and ₳4.094M (648) (ADA) | Koios proposal_list + tip | ✓ all |
| 16 | Cardano Maintainer Retainer "25 projects" (ADA) | OSC POSM GitBook: "Supports key maintainers for 25 open-source projects" | ✓ |
| 17 | SCF Build Awards "up to $150K in XLM", 10/20/30/40% tranches (XLM) | v7.0 blog: 10/20/30/40 ✓, but "Follow-on Build Awards … up to $300K in total funding over the project’s full lifecycle". Handbook: "up to a total maximum of $150,000 in XLM across all awards" | **Conflict** → F-6 |
| 18 | NEAR TREASURY_PCT 0.1 / CONTRACT_PCT 0.3 (NEAR) | nomicon.io Economics | ✓ |
| 19 | HSP-026 $196,000 + 60,000 NEAR; "ratified 25 Jul 2026" (NEAR) | houseofstake.org: amounts ✓; post dated July 25, 2026; Security Council review closed July 14, 2026 | ✓ (wording nit N-3) |
| 20 | BCHN ≈2,048 BCH moved 27 May 2026; 3-of-5; "no additional power…" (BCH) | bitcoincashnode.org announcement (dated 10 Jun 2026) | ✓ |
| 21 | CIP-0082 5% of mint emissions, Final, approved 2025-10-01 (CC) | raw cip-0082.md | ✓ |
| 22 | Litecoin match $250,000/yr × 5 yrs, $50,000 to projects/bounties; bounty goal $100,000 (LTC) | litecoin.com/donate; bounty page | ✓ figures. The bounty is **not yet live** → F-7 |
| 23 | Retro9000 "up to $40M" (AVAX) | avalanche.com blog | ✓ |
| 24 | Sui $25k research award; "long-term support - not grants" (SUI) | sui.io/programs-funding | ✓ |
| 25 | Hedera 25,302,501,344 HBAR (50.61%) "Ecosystem and Open Source Development" (HBAR) | hederacouncil.org/treasury | ✓ |
| 26 | Cronos #1323 Sep 19 2026, "Unanswered", 100% buy-and-burn (CRO) | github discussion | ✓ |
| 27 | OKB "only gas and native token"; 21 million (OKB) | okx.com announcement | ✓ |
| 28 | MemeCore 10% block rewards to Viral Grants Reserve; Meme 2.0 (TBA) (M) | docs.memecore.com | ✓ |
| 29 | Bittensor "All TAO enters circulation through protocol emissions" (TAO) | blockworks token-transparency filing | ✓ |
| 30 | TON grants "currently paused" (TON) | github ton-society/grants-and-bounties | ✓ |

**Derived labels:** the only derived figure in the batch, Cardano ≈0.2% / ≈99.8%, is labeled DERIVED with method and epochs. Market caps are CoinGecko's own values. **PASS.**
**Tidelift:** the batch uses only "Tidelift-style" (no acquisition claim), and the errata wording "under a definitive agreement announced by Sonar" is untouched. **PASS.**
**ENS KPK / EP 6.46:** not cited in batch 1, so there is nothing stacked. **PASS.**
**Stage 0:** the header says "No ORF Hard Gate is marked passed". No row says "self-sustaining", "runs ORF" or "meets MV-ORF/MV-OMF". **PASS.** (B-1 is an *implied* MV-ORF item, not a gate.)

### 6. `pg-followups.md` (mtime 05:28 PT)

| Check | Result |
|---|---|
| 190 cited **only** to the Q3 audit capture `pg-20260826-q3-quarterly-audit-2026-10-09.html` | ✓ l.10–11: "The 190 figure is cited **only** to the Q3 audit capture." The capture has "membership is now 190, with a net decrease of 6 (-3.1%) members from 196" and "as of August 5, 2026". |
| 186 kept out | ✓ Not present. (The annual report capture has "started 2025 with 186 members, but ended with 184", which is correctly not used.) |
| 187 only in "Current (stale)" blocks | ✓ l.42 (1b Current) and l.100 (3a Current) only. |
| $12.4M and ≈83% only in §4, with sources | ✓ l.141–142 only, with URL, capture and check date. Verified in the annual report capture (quotes in §0 1-f). Nit N-8: the ≈83% quote is not verbatim. |
| Cardano ₳5,885,000 High (on-chain) | ✓ 1d, 1e, 3c, with action hash, epochs and Cardanoscan. |
| ₳4.601M never submitted | ✓ "was never submitted on-chain (Koios, epoch 660…)". Koios confirmed by QA at 05:35 PT. |
| $300K planned, UNVERIFIED | ✓ "planned allocation (₳600K ≈ $300K at $0.50/ADA) … utilization is not shown and stays UNVERIFIED". |
| Canonical errata = PR #105 `065e843` | ✓ Confirmed via GitHub (PR #105 head `065e8435c78e…`, open, mergeable). |

**Result: PASS.** The open items are 1-j (advisory) and nits N-8 and N-12.

### 7. Blocked explorers (rule D liveness)

`top100-method.md` §4 says only that 403'd explorers "were accepted when the chain is plainly live". **No alternative evidence is logged for Avalanche or Bitcoin Cash.** Canton's alternative (lighthouse.cantonloop.com HTTP 200) is logged and is adequate. QA collected the evidence below, and Researchy should copy it into the method (F-8):

| Chain | Blocked | QA alternative (9 Oct 2026) | Adequate? |
|---|---|---|---|
| Avalanche | snowtrace, avascan (QA saw HTTP 202 challenge pages) | Public C-Chain RPC `api.avax.network/ext/bc/C/rpc` `eth_getBlockByNumber latest` → block **97,122,948** at **05:36:17 PT** | Yes |
| Bitcoin Cash | bchexplorer (403 for Researchy; HTTP 200 "Bitcoin Cash Explorer" for QA); blockchair.com HTML 401 | `api.blockchair.com/bitcoin-cash/stats` → best block **972,125** at **05:30:44 PT**, 15,203 tx/24h | Yes |
| Canton | ccview 403 (QA confirms) | lighthouse.cantonloop.com HTTP 200 (QA confirms) | Yes (already logged) |
| X Layer (extra) | — | `rpc.xlayer.tech` → block 72,780,451 at 05:38:07 PT | Supports inclusion |

### 8. Findings

| # | Sev | Row | Quote | Exact fix |
|---|---|---|---|---|
| **B-1** | **blocker** | 1 Bitcoin, 2 Ethereum, 10 Monero, 12 Cardano, 15 Bitcoin Cash, 17 Litecoin (Missing pieces) | "MV-ORF items 1, 3, 4, 5" (ETH: "MV-ORF items 1, 3 (earned instrument), 4, 5") | Listing 1, 3, 4, 5 implies **MV-ORF item 2 (classified inflow inventory, issuance and routing excluded; ORF p.18) is met**. No source is given. The locked top-10 file says "none publishes … a classified inflow inventory that excludes issuance" (§2 Overall), and Cardano's fee/issuance split is "derived, not official". Change all six to **"MV-ORF items 1–5"**. Rubric A1/E5. |
| **B-2** | **blocker** | 7 Zcash (ORF-like) | "Family D donations to ZF are UNVERIFIED." | The locked top-10 file §3.7 has "D ✅ (ZF and Shielded Labs donations)". Replace with "Family D: ZF and Shielded Labs donations (✅ per `top10-chains-orf-alignment.md` §3.7; not re-opened this pass)." The cell stays Partial. This removes one UNVERIFIED tag (see F-1). Rubric E5. |
| F-1 | fix | UNVERIFIED summary | "11 UNVERIFIED tags in the batch-1 table: … Zcash (3) …" | The table has **12** (Zcash 4). Either correct it to "12 … Zcash (4)", or apply B-2 first, after which 11 / Zcash 3 is correct. Rubric A3. |
| F-2 | fix | Header "Definitions used" | "**OMF** (OMF START_HERE §1–2): … 5-Requirement Compliance Bar …"; "**ORF** (ORF START_HERE §1): 'a governance and economic design framework…'" | Rubric §B allows whitepaper definitions only ("spec … may be cited as spec, but not as the definition"). Replace them with the whitepaper quotes already in `top100-method.md` §2 (OMF WP p.5 "portable operational architecture…"; ORF WP p.2 "the ORF defines the replenishment layer (how resources come back)"; MV-OMF p.15; MV-ORF p.18). START_HERE can stay, labeled "spec". Rubric C1/B0. |
| F-3 | fix | 3 BNB Chain (ORF-like) | "Missing: fee flows exist but go to validators and burns, not to OSS maintenance (Family A collection exists, unrouted)." | The text describes rubric B's **Partial** condition ("collection exists but isn't routed") but the cell rates Missing. The locked top-10 has BNB A ❌. Reword: "Missing: fees go to validators and BEP-95 burns (validator income and burns never count, rubric B); no collection layer feeding a treasury." Keep Missing, so the counts are unchanged. |
| F-4 | fix | 4 XRP, 18 Avalanche, 19 Sui, 20 TON, 21 Hedera (Missing pieces) | e.g. XRP "MV-OMF items 1, 3, 4, 5"; OMF cell "MV-OMF: no item shown" | Item 2 is neither shown nor listed as missing. Change each to **"MV-OMF items 1–5"**, or cite the program-governance authority that meets item 2. |
| F-5 | fix | 9 Dogecoin, 10 Monero, 15 BCH, 16 Canton, 17 Litecoin, 20 TON (OMF-like) | e.g. DOGE "Partial: release-gated payout is bounty-like (Program 2), rules-based and transparent." | Rating rule: "Each OMF cell lists the MV-OMF items shown." Add "MV-OMF: item 3 ✓ (…); items … not shown" to each, matching the Missing-pieces column. Dogecoin's Missing pieces ("1, 2, 5") implies item 4 (quarterly reporting) is met, but none is cited, so it should read "1, 2, 4, 5". |
| F-6 | fix | 13 Stellar (Funding processes) | "Build Awards up to $150K in XLM" | The cited SCF v7.0 page says "Follow-on Build Awards … up to $300K in total funding over the project’s full lifecycle". The handbook says "up to a total maximum of $150,000 in XLM across all awards". Write: "lifetime cap $150,000 in XLM (SCF handbook) vs up to $300K incl. follow-on (SCF v7.0 blog, Jan 2026); sources conflict (Partial)." |
| F-7 | fix | 17 Litecoin (OMF-like, Funding) | "security bounty pool (Program 2)" | The bounty page says "Fundraising goal: $100,000 … reward criteria will be published before bounty submissions are accepted. Until then, this page is for funding…". Say "bounty pool fundraising; not yet accepting submissions (9 Oct 2026)". OMF stays Partial on Foundation-staffed developers. |
| F-8 | fix | Method §4 explorer check | "Explorers that returned 403 … were accepted when the chain is plainly live" | Log the alternative liveness evidence per chain (table in §7 above: AVAX C-Chain RPC block and time; BCH Blockchair API block and time; Canton lighthouse 200). "Plainly live" alone is not evidence (rubric A3). |
| F-9 | fix | 4 XRP (dOSPO-like) | "(i) community mandate, partial: XAO DAO community voting on allocation." | The cited Ripple page (26 Feb 2026) describes XAO DAO in the future tense: "As soon as the proposal window opens, the DAO will empower its members…". Either cite a dated source showing XAO DAO votes are live, or mark it "(planned; UNVERIFIED live)". If it isn't live, XRP dOSPO becomes Missing (dOSPO 0/8/17), and the combinations and has-function view must be re-run. |
| N-1 | nit | 2 Ethereum (ORF-like) | "No Family A (fees burned)." | Write "No Family A at L1 (fees burned); L2/app-layer A ◐ per top-10 file" to match the locked "A ◐ (L2/app layer only)". |
| N-2 | nit | Re-verification paragraph | "EF treasury policy (15%, 5%, 2.5 yrs)" | Write "A = 15% opex, B = 2.5-year runway, 5% baseline after ~5-year glide", so 2.5 is not read as the glide length. |
| N-3 | nit | 14 NEAR (Direction) | "HSP-026 ratified 25 Jul 2026" | Write "ratification announced 25 Jul 2026 (Security Council review closed 14 Jul 2026)". |
| N-4 | nit | Cardano rank note | "`release1-section-3.3-chains.md` says "Cardano (#11)". … flag for Projects Manager." | This is stale. §3.3 now reads "#11 when WBT is excluded; #12 under the top-100 gas-token scope rule". Update the note. The remaining unconditional "#11" is `posm-cycle-chain-map.md` l.113 (PM item). |
| N-5 | nit | 2 Ethereum (Direction) | "PG 'Sponsor a Core Dev' (18 Dec 2025 … UNVERIFIED this pass)" | The program's existence is confirmed in `data/pg-20260129-annual-report-2025-2026-10-09.html` ("A new funding program was announced in 2025: “Sponsor a Core Dev”"). Only the 18 Dec date stays UNVERIFIED. |
| N-6 | nit | Exclusions summary | "**24 exclusions** … (24 = stablecoins/RWA/app/exchange/protocol tokens)" | State the split: "24 = 9 stablecoins (USDe counted once) + 4 tokenized RWAs/commodities + 11 tokens with no own chain" (QA-verified). |
| N-7 | nit | All PROPOSAL cells | "OMF WP Program Architecture (p.24) and Appendix B Retainer Program (p.52)" | The OMF PDF TOC says 24/52, but the page footers put §8 Program Architecture on p.23 and "Retainer Program Operational Requirements" on p.51. Cite "OMF WP §8 Program Architecture; Appendix B" with the footer page, or note "TOC p.24/52". |
| N-8 | nit | `pg-followups.md` §4 | "[pledgers via] the Protocol Guild Pledge — account for roughly 83%…" | Quote verbatim (A5): "Projects that have pledged to donate 1% of their token supply - i.e. the Protocol Guild Pledge - account for roughly 83% of PG’s total funding to date." |
| N-9 | nit | 23 Cronos (Funding) | "Proposal #1291 (approved, per #1323)" | Fine as written. Add "(approval status as stated by the #1323 proposer; #1291 vote record not opened)". |
| N-10 | nit | 6 TRON | "TRON Builders League" | The live page title reads "TBL - Tron Builders Club". Use the page's name, or note both. |
| N-11 | nit | Edge case WBT | "61.4M transactions shown" | JS-rendered, so QA could not reproduce it with curl. Add "(read in browser, 9 Oct 2026)" or drop the figure. |
| N-12 | nit | `pg-followups.md` l.14 | "there is no `docs/` directory on the box" | Moot (see 1-d). Optionally add "upstream line numbers verified by QA 05:24 PT". |
| A-1 | advisory | 12 Cardano (Direction) | "Stalled: no TreasuryWithdrawals action for ₳4,601,000 …" | Correct. Koios also shows a **pending ₳11,787,063 "OpenZeppelin Stack administered by Intersect"** withdrawal (proposed epoch 654; not ratified or expired as of epoch 660). It isn't POSM, but it is OSS deployment on Cardano and worth a mention. |
| A-2 | advisory | Rubric v1.1 (QA) | — | Write down the method's split: issuance aimed at OSS = ORF Partial (Zcash, Canton); issuance not aimed at OSS = Missing (MemeCore, Bittensor, NEAR's treasury share). |

### For Projects Manager

1. **Cardano rank.** Under rule D Cardano is **#12** (05:19 and 03:53 snapshots). `release1-section-3.3-chains.md` already gives both (#11 if WBT is excluded, #12 under rule D). Still unconditional "#11": `posm-cycle-chain-map.md` l.113 ("Cardano (ref., #11)"). Rubric E1 ("Cardano is the #11 reference (only if WBT stays excluded)") is now conditional-false. Decide whether §3.3 keeps "top ten + Cardano #11 reference" under the old rule or restates as #12; QA will update rubric E1 to match.
2. **C-026 label.** `pg-followups.md` 1a keeps status **ERRATA** (claims-file vocabulary) and moves the High/Unverified split into Notes. The claim line still repeats the paper's "$7.2M … 196 members as of Q2 2026; $80M+ committed". QA accepts this as the record of the original claim. Confirm, or rewrite the claim line to "$7,231,668 (time of donation) from 6,202 unique donors (2025); 190 members as of 5 Aug 2026; $80M+ UNVERIFIED".
3. **1-j:** check EVIDENCE_REGISTER L60 column mapping on apply.
4. **Exclusions:** 9/4/11 = 24 verified directly from the table (the earlier "11 labeled 10" check is retired).
