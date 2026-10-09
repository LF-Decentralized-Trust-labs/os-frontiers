# Top-100 audit, batch 1 (ranks 1–25 of 100; batches 2–4 on hold): where N1 money could come from (patterns note)

> **Stage 0.** No ORF Hard Gate is marked passed for any chain. The OSFL whitepapers and `whitepapers/ORF_ERRATA.md` (PR #105, commit 065e843) are the spec; errata control. Chains are **examples only** and supporting evidence for N1, not a headline finding. Every suggestion is labeled **PROPOSAL (example; not a finding)**, applies the whitepaper text as written, and is not a spec change.
> **Counts source:** `chains/top100-audit.md` **batch 1 (ranks 1–25) only**, mtime 2026-10-09 05:42 PT, after QA (`chains/top100-qa-log.md`, verdict SHIP WITH FIXES; blockers B-1 and B-2 checked applied in the audit file). **Batches 2–4 are on hold.** Snapshot: CoinGecko, 2026-10-09 05:19 PT.
> **N1** = predictable, sustained pay (§2.3 needs table; Tidelift 2024 [S01]: 81% prefer predictable monthly income, n=344, p. 11). Last refreshed: 2026-10-09 07:56 PT.

## QA-confirmed batch-1 counts (25 chains)

| Function | Present | Partial | Missing |
|---|---|---|---|
| dOSPO-like | 0 | 9 | 16 |
| OMF-like | 0 | 17 | 8 |
| ORF-like | 0 | 11 | 14 |

- All three at least Partial: 5 (Zcash, Monero, Cardano, Bitcoin Cash, Canton Network). All three Missing: 5 (TRON, Whitechain, Bittensor, X Layer, MemeCore).
- POSM leading stage: P1 2 · P2 5 · P3 4 · P5 14; **0 at P6**. Of the 14 at P5, 9 leak (BNB, XRP, SOL, TRX, HYPE, WBT, AVAX, CRO, OKB) per QA recount (`top100-qa-log.md`; reconfirmed by scripted recount of the audit table, 2026-10-09 07:55 PT).
- None meets Minimum Viable ORF or Minimum Viable OMF.

## Where N1 money could come from (finding, then PROPOSAL)

1. **In batch 1, today's money is mostly not replenishment.** The 11 ORF Partials are three kinds (audit summary): voluntary Family D money without net accounting (Bitcoin, Ethereum, Monero, Bitcoin Cash, Litecoin); collection not routed to maintenance (Hyperliquid, NEAR, Cronos); issuance streams, which are excluded (Zcash, Canton, Cardano). Issuance, grants, Retro Funding, Gitcoin rounds, Drips, Superfluid and treasury drawdown are not replenishment; payment rails move money but are not revenue.
2. **Closest structural source: Family A fee collection that already exists.** NEAR already pays 30% of gas to contract owners, not to OSS maintenance (collection not routed). Cardano belongs in the issuance group (item 1), not here: its treasury cut (τ) includes a fee share that does reach the treasury funding Intersect, but ≈0.2% of treasury inflow is fee-derived and ≈99.8% is reserve issuance (**derived** 9 Oct 2026 from Koios, epochs 588–660, not an official figure). *PROPOSAL (example; not a finding):* such fee shares could be measured, reported net and routed to maintenance under ORF WP §8 Family A (Protocol Fee Routing) and ORF WP §4 MV-ORF item 4, as written. This is not observed in batch 1.
3. **Closest deployment channel for predictable pay: Cardano's Intersect OSC programs** (including a Maintainer Retainer for 25 open-source projects (OSC POSM page: https://github.com/IntersectMBO/documentation/blob/63a1c0b5f9b8b0d2171961bf820338bee1349e5b/open-source-committee/about/paid-open-source-model-posm/README.md, commit 63a1c0b, last changed 8 Sep 2026, checked 9 Oct 2026); `top100-audit.md` row 12, QA-checked in `top100-qa-log.md`, 2026-10-09). The 2025 proposals page says "over 50 repositories"; repositories are a different unit from projects, so the count here stays at 25 projects. The whole OSC/POSM budget, not the Retainer alone, is funded by a ₳5,885,000 treasury withdrawal enacted 12 Aug 2025 (epoch 576). That is a retainer shape that matches N1, but it is funded by a treasury withdrawal (≈99.8% issuance, derived). The 2026–27 request (₳4,601,000) was not submitted on-chain as of epoch 660 (Koios, checked 2026-10-09).
4. **Family D pledges are real but voluntary and not net-accounted.** Protocol Guild raised $7,231,668 in 2025 (valued at time of donation; $2,634,505 at report-date value, annual report 29 Jan 2026) from 6,202 unique donors, and had 190 members as of 5 Aug 2026 (Q3 2026 audit) (Validated). No cost floor or net-contribution reporting is shown (MV-ORF not met). Unvalidated Protocol Guild totals and commitments stay out of this note (see `C-110`, errata).
5. **Enterprise earned (Family B) does not appear in batch 1.** Off-chain, the Tidelift–Sonar deal is a "definitive agreement" only; it is not counted here.

**Reading for the verdict:** batch 1 does not change it. Within a funded portfolio, N1 has a named mechanism, but no top-25 chain shows a non-issuance, net-accounted inflow paying maintainers predictably. The Release 1 verdict stands: 6 of 8 needs are covered within a funded portfolio, N3 (a way to receive money) stays a Gap, N7 stays Partial, and small projects outside a funded ecosystem's portfolio (the long tail) stay unreached.

## Not yet covered
Ranks 26–100 (batches 2–4, on hold). Re-fetch a new dated CoinGecko snapshot when they resume.
