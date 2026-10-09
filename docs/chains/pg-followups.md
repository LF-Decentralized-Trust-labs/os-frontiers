> **Status (9 Oct 2026):** §1–3 below were applied in the follow-up PR on branch `osfl/release1-sec2-needs-batch1` (stacked on #105), to `claims/orf-claims-validated.md`, `docs/EVIDENCE_REGISTER.md` and `docs/PRIOR_ART_AND_COMPETITIVE_ANALYSIS.md`. In §2a and §2b the proposed cells were placed under the matching table headers. §4 was **not** inserted anywhere. The original draft text follows unchanged.

# Protocol Guild and Cardano follow-ups: drafted corrections (NOT APPLIED)

> Prepared 2026-10-09 (PT) for the batch-1 follow-up PR. **Drafts only. No upstream file below was edited.**
> **Canonical errata:** `whitepapers/ORF_ERRATA.md` in PR #105 (head commit `065e843`), "Protocol Guild — corrected scale (approved 9 October 2026)" and "Cardano POSM — 2025 treasury withdrawal confirmed on-chain (approved 9 October 2026)". Projects Manager is applying the Cardano errata move on #105, so it is **not drafted again here**. The workspace copy `sources/ORF_ERRATA.md` is byte-identical to the PR #105 version (diff checked 2026-10-09 05:27 PT).
> **Manuscript mirror:** `whitepapers/orf-whitepaper-v1.1-errata-applied.md` in PR #105 at `065e843` mirrors the same errata (L127, L165, L243; per QA log, `top100-qa-log.md` item (2), "Resolved"). §1e and §3c below match both files; nothing here edits either.
> **Figures used (High, per PR #105):** $7,231,668 in total 2025 donations, valued at time of donation, from 6,202 unique donors (Annual Report 2025, 29 Jan 2026); **190 funded members as of 5 Aug 2026, a net decrease of 6 from 196** (Q3 2026 Membership Audit, 26 Aug 2026). "Commitments above $80 million" stays **UNVERIFIED**.
> **Re-check 2026-10-09:** both figures matched the live official site (post text in the site's public JS bundle) and the archived captures. No discrepancy.

**Captures (cite these):**
- Annual Report 2025: `docs/chains/data/pg-20260129-annual-report-2025-2026-10-09.html` (and `.pdf`), captured 2026-10-09, for $7,231,668 / 6,202 only.
- Q3 2026 audit: `docs/chains/data/pg-20260826-q3-quarterly-audit-2026-10-09.html` (and `.pdf`), captured 2026-10-09, for **190 members** only. It records "membership is now 190, with a net decrease of 6 (-3.1%) members from 196", for funded members as of August 5, 2026.
- The 190 figure is cited **only** to the Q3 audit capture. Membership figures in the Annual Report are from a different date and are not used here.
(On the box these captures sit under `/workspace/osfl/chains/data/`. In the repo, PR #105 places them under `docs/chains/data/`.)

**Path note:** there is no `docs/` directory on the box. The upstream files `docs/EVIDENCE_REGISTER.md` and `docs/PRIOR_ART_AND_COMPETITIVE_ANALYSIS.md` exist on the box as `sources/EVIDENCE_REGISTER.md` (near-duplicate: `sources/evidence-register.md`) and `sources/PRIOR_ART_AND_COMPETITIVE_ANALYSIS.md`. Line numbers below refer to those box copies and must be re-located with `rg` in the repo before applying.

---

## 1. `claims/orf-claims-validated.md` (merged in #103)

### 1a. C-026 (box lines 243–247)
**Current (stale):**
```
- **Claim:** Protocol Guild: $7.2M from 6,202 donors (2025); 196 members as of Q2 2026; $80M+ committed.
- **Source:** `whitepapers/orf-v1.0.pdf · §2 Protocol Guild`
- **Validation status:** ERRATA
- **Evidence:** sources/ORF_ERRATA.md · Protocol Guild; https://www.protocolguild.org/blog/20260604-Q2-quarterly-audit
- **Notes:** 196 members (22 May 2026) recoverable. Dollar totals $7.2M / 6,202 donors / $80M+ NOT recoverable from rendered primary page — mark unverified.
```
**Proposed:**
```
- **Claim:** Protocol Guild: $7.2M from 6,202 donors (2025); 196 members as of Q2 2026; $80M+ committed.
- **Source:** `whitepapers/orf-v1.0.pdf · §2 Protocol Guild`
- **Validation status:** ERRATA
- **Evidence:** whitepapers/ORF_ERRATA.md · "Protocol Guild — corrected scale (approved 9 October 2026)"; https://www.protocolguild.org/blog/20260129-annual-report-2025 (capture docs/chains/data/pg-20260129-annual-report-2025-2026-10-09.html, 2026-10-09); https://www.protocolguild.org/blog/20260826-q3-quarterly-audit (capture docs/chains/data/pg-20260826-q3-quarterly-audit-2026-10-09.html, 2026-10-09)
- **Notes:** Corrected per errata (High): total 2025 donations $7,231,668, valued at time of donation, from 6,202 unique donors (Annual Report 2025, 29 Jan 2026). Membership: 190 funded members as of 5 Aug 2026, a net decrease of 6 from 196 (Q3 2026 audit, 26 Aug 2026). The 196 figure (22 May 2026) is superseded, not wrong for its date. "$80M+ committed" stays UNVERIFIED.
```
(The claim line stays in the paper's original wording ($7.2M, 196, $80M+) as the record of the original claim. Status is **ERRATA**, and all corrections are in Notes. This is the form USe Me's QA log accepts, per Batch 1 QA "For Projects Manager" item 2, 2026-10-09.)

### 1b. C-110 (box lines 915–919)
**Current (stale):**
```
- **Claim:** ERRATA Protocol Guild: Q2 2026 membership audit records 196 funded members as of 22 May 2026 (up from 187); dollar totals $7.2M/6,202 donors and $80M+ not recoverable from rendered primary page — do not publish as High until annual report quoted.
- **Source:** `whitepapers/ORF_ERRATA.md · Protocol Guild`
- **Validation status:** SUPPORTS
- **Evidence:** ORF_ERRATA.md Protocol Guild; protocolguild.org Q2 2026 audit
- **Notes:** Membership recoverable; dollars downgraded.
```
**Proposed:**
```
- **Claim:** ERRATA Protocol Guild (corrected scale, approved 9 Oct 2026): 2025 Annual Report (29 Jan 2026) reports total 2025 donations of $7,231,668, valued at time of donation, from 6,202 unique donors; Q3 2026 membership audit (26 Aug 2026) records 190 funded members as of 5 Aug 2026, a net decrease of 6 from 196. "Commitments above $80 million" stays unverified.
- **Source:** `whitepapers/ORF_ERRATA.md · Protocol Guild — corrected scale (approved 9 October 2026)`
- **Validation status:** SUPPORTS
- **Evidence:** docs/chains/data/pg-20260129-annual-report-2025-2026-10-09.html ($7,231,668 / 6,202); docs/chains/data/pg-20260826-q3-quarterly-audit-2026-10-09.html (190 members); both captured 2026-10-09
- **Notes:** Supersedes the earlier downgrade (196 members as of 22 May 2026; dollars not High). High for $7,231,668 / 6,202 / 190; UNVERIFIED for $80M+.
```

### 1c. Summary table row (box line 1184)
**Current (stale):** `| C-026, C-110 (Protocol Guild) | ERRATA / SUPPORTS | Q2 2026 audit **200**; 196 members hold; **$7.2M / $80M+ still not High** |`
**Proposed:** `| C-026, C-110 (Protocol Guild) | ERRATA / SUPPORTS | Per ORF_ERRATA (approved 9 Oct 2026): **$7,231,668 / 6,202 unique donors High**; **190 members (5 Aug 2026, Q3 2026 audit) High**; **$80M+ still Unverified** |`

### 1d. Index line (box line 32)
**Current (stale):** `2. Protocol Guild / Polkadot spend / POSM budget / Octant Epoch / Deep Funding dollars: **ERRATA unverified** (`C-026`–`C-030`, `C-111`).`
**Proposed:** `2. Polkadot spend / POSM $300K bounty / Octant Epoch / Deep Funding dollars: **ERRATA unverified** (`C-027`–`C-030`, `C-111`). Protocol Guild (`C-026`, `C-110`) corrected per ORF_ERRATA (approved 9 Oct 2026): $7,231,668 / 6,202 donors / 190 members High, $80M+ Unverified. POSM ₳5,885,000 is High (on-chain) per ORF_ERRATA; see `C-029`.`
(Box claim IDs: C-027 = Polkadot/PCF, C-028 = Octant, C-029 = Cardano POSM, C-030 = Drips/Superfluid/Deep Funding, C-111 = errata unverified list.)

### 1e. C-029 (box line 267), optional, for consistency with the PR #105 Cardano errata
**Current (stale):** `- **Claim:** Cardano POSM: 5.885M ADA 2025 budget; $300K bounty pool fully utilized — deployment precedent, not replenishment.`
**Proposed note to add:** `- **Notes:** ₳5,885,000 is High (on-chain): governance action 8ad3d454…833e#11, enacted epoch 576 (12 Aug 2025), per ORF_ERRATA (approved 9 Oct 2026). The ₳4,601,000 2026–27 OSC request was never submitted on-chain (Koios, epoch 660, checked 2026-10-09). "$300K bounty fully utilized" is UNVERIFIED: only a planned ₳600K (≈$300K) allocation is documented.`

---

## 2. Evidence register (`docs/EVIDENCE_REGISTER.md`; box `sources/EVIDENCE_REGISTER.md`, duplicate `sources/evidence-register.md`)

### 2a. Box `sources/EVIDENCE_REGISTER.md` line 37 (`evidence-register.md` line 44)
**Current (stale):**
```
| **Protocol Guild** | **OMF + ORF** | Eligibility, vesting, and voluntary pledges are the mechanism the framework discusses. Membership count and dollar totals are not quoted. The Q2 2026 audit URL returned an empty shell. | Voluntary pledge. Amounts unverified. | Not established from a rendered page this pass. | Not established from a rendered page this pass. | https://www.protocolguild.org/blog/20260604-Q2-quarterly-audit | **Unverified** for counts and dollars |
```
**Proposed:**
```
| **Protocol Guild** | **OMF + ORF** | Eligibility, vesting, and voluntary pledges are the mechanism the framework discusses. Total 2025 donations $7,231,668, valued at time of donation, from 6,202 unique donors; 190 funded members as of 5 Aug 2026 (net decrease of 6 from 196). | Voluntary pledge. | Annual Report 2025 (29 Jan 2026); capture docs/chains/data/pg-20260129-annual-report-2025-2026-10-09.html (2026-10-09). | Q3 2026 Membership Audit (26 Aug 2026); capture docs/chains/data/pg-20260826-q3-quarterly-audit-2026-10-09.html (2026-10-09). | https://www.protocolguild.org/blog/20260129-annual-report-2025 ; https://www.protocolguild.org/blog/20260826-q3-quarterly-audit | **High** (ORF_ERRATA, approved 9 Oct 2026); "$80M+ commitments" **Unverified** |
```
(Columns were inferred from their position. Check them against the table header before applying.)

### 2b. Box `sources/EVIDENCE_REGISTER.md` line 60 (`evidence-register.md` line 67)
**Current (stale):**
```
| **Protocol Guild** | Not established from a rendered page. | Unverified. Dollar totals and donor counts are not restated. Membership is not quoted: the Q2 2026 audit URL returned an empty shell, so a membership count is not asserted. | Unverified. | https://www.protocolguild.org/blog/20260604-Q2-quarterly-audit | **Unverified** | Mechanism may still be discussed elsewhere. This row does not publish a scale. |
```
**Proposed:**
```
| **Protocol Guild** | Rendered captures (both pages are JS-rendered): docs/chains/data/pg-20260129-annual-report-2025-2026-10-09.{html,pdf} and docs/chains/data/pg-20260826-q3-quarterly-audit-2026-10-09.{html,pdf}, captured 2026-10-09. | $7,231,668 total 2025 donations (valued at time of donation) from 6,202 unique donors; 190 funded members as of 5 Aug 2026. | High. | https://www.protocolguild.org/blog/20260129-annual-report-2025 ; https://www.protocolguild.org/blog/20260826-q3-quarterly-audit | **High** (ORF_ERRATA, approved 9 Oct 2026) | "Commitments above $80 million" stays Unverified. |
```

---

## 3. `docs/PRIOR_ART_AND_COMPETITIVE_ANALYSIS.md` (box `sources/PRIOR_ART_AND_COMPETITIVE_ANALYSIS.md`)

### 3a. §4.5 Protocol Guild, Empirical Metrics (box line 132)
**Current (stale), quoted for replacement:** `- **Empirical Metrics**: Raised **$7.2M from 6,202 unique donors** in 2025; stewards **187 members** across 10+ client teams in 2026.`
**Proposed:** `- **Empirical Metrics**: Raised **$7,231,668 (valued at time of donation) from 6,202 unique donors** in 2025 (Annual Report 2025, 29 Jan 2026); **190 funded members as of 5 Aug 2026**, a net decrease of 6 from 196 (Q3 2026 Membership Audit, 26 Aug 2026; capture docs/chains/data/pg-20260826-q3-quarterly-audit-2026-10-09.html, 2026-10-09).`

### 3b. §4.5 Detailed Mechanics (box line 131), flag only
**Current (stale), quoted:** "… for ~180 core Ethereum L1 developers …" and "($200K 2-year ops reserve)".
**Proposed:** change "~180 core Ethereum L1 developers" to "190 funded members (as of 5 Aug 2026, Q3 2026 audit)". Mark "$200K 2-year ops reserve" **UNVERIFIED** (not re-checked in this pass).

### 3c. §4.4 Cardano POSM, Empirical Metrics (box line 126)
**Current (stale), quoted:** `- **Empirical Metrics**: 2025 POSM budget request approved at **5.885M ADA**. First-year Bug Bounty pool of **$300K** was 100% utilized by July 23, 2026. Maintainer Retainers launched a 6-maintainer pre-pilot in April 2026.`
**Proposed (consistent with ORF_ERRATA in PR #105, commit 065e843):** `- **Empirical Metrics**: 2025 OSC/POSM treasury withdrawal of **₳5,885,000** enacted on-chain: governance action 8ad3d454f3496a35cb0d07b0fd32f687f66338b7d60e787fc0a22939e5d8833e#11, proposed epoch 570, ratified epoch 575, **enacted epoch 576 (12 Aug 2025)** (High, on-chain; https://cardanoscan.io/govAction/gov_action13tfag48nf94rtjcdq7c06vhkslmxxw9h6c88sl7q5g5nnewcsvlqkqx0ecg). This is a single 2025 tranche. The ₳4,601,000 2026–27 OSC request **was never submitted on-chain** (no TreasuryWithdrawals action on Koios as of epoch 660, checked 2026-10-09). The **$300K Bug Bounty pool was a planned allocation** (₳600K ≈ $300K at $0.50/ADA in the 2025 budget); utilization is **not shown** and stays UNVERIFIED. "6-maintainer pre-pilot in April 2026": **UNVERIFIED** (not re-checked in this pass).`
(Re-check 2026-10-09 via Koios: amount 5,885,000,000,000 lovelace; epoch 576 starts 12 Aug 2025 14:44 PT. The governancespace budget link for the planned ₳600K is carried from PR #105's errata and was not re-opened in this pass.)

### 3d. Chart, "Selected observed annual financial flows" (box lines 85–90)
**Current (stale), quoted:**
```
    │ Polkadot 2025 Treasury Spend       ■■■■■■■■■■■■■■ $70.6M   │
    │ ENS DAO 2025 Operating Revenue     ■■■ $18.22M             │
    │ Protocol Guild 2025 Funds Raised   ■ $7.2M                 │
    │ Octant Epoch 8 Distribution        ■ $1.7M                 │
    │ Cardano 2025 Bug Bounty Pool       ■ $0.3M                 │
    │ Deep Funding 2025 Challenge Pool   ■ $0.22M                │
```
**Proposed:**
```
    │ Polkadot 2025 Treasury Spend       ■■■■■■■■■■■■■■ $70.6M (UNVERIFIED) │
    │ ENS DAO 2025 Operating Revenue     ■■■ $18.22M             │
    │ Protocol Guild 2025 Donations      ■ $7.23M (at donation)  │
    │ Octant Epoch 8 Distribution        ■ $1.7M (UNVERIFIED)    │
    │ Cardano 2025 Bug Bounty Pool       ■ $0.3M (planned, not shown as paid) │
    │ Deep Funding 2025 Challenge Pool   ■ $0.22M (UNVERIFIED)   │
```
None of Polkadot $70.6M, Octant $1.7M, Deep Funding $0.22M or the Cardano $0.3M was sourced with a URL in this pass, so each keeps its label. They are listed as unverified in ORF_ERRATA "Claims to mark unverified". ENS $18.22M was not re-checked here (it is in ORF_ERRATA's ENS entry).

---

## 4. Later-errata candidates (NOT for insertion now)

Both appear in Protocol Guild's own Annual Report 2025. They were removed from the drafts above per PR #105's canonical text and are listed here for a later errata decision.

| Candidate | Exact source text | Source URL | Capture | Check date | Suggested status |
|---|---|---|---|---|---|
| $12.4M distributed to members in 2025 | "During that same time, a total of $12.4mm in funding was vested and distributed to Protocol Guild members, representing approximately $62k per member." Also: "Funding outflows … totalled $12.4mm in 2025, an increase from the $10m distributed in 2024." | https://www.protocolguild.org/blog/20260129-annual-report-2025 | docs/chains/data/pg-20260129-annual-report-2025-2026-10-09.html (text present; also in the live site bundle /assets/index-DCUyXotM.js) | 2026-10-09 | Candidate High (primary, self-reported) |
| 1% pledge ≈83% of total funding to date | "[pledgers via] the Protocol Guild Pledge — account for roughly 83% of PG's total funding to date." | same | same capture (text present) | 2026-10-09 | Candidate High (primary, self-reported); "to date" means as of the report (29 Jan 2026) |

"Commitments above $80 million": not in the report. It stays **Unverified**, and it is not a candidate.
