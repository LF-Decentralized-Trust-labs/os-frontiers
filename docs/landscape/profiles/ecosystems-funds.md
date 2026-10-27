# Ecosyste.ms Funds

> **Pass date:** 2026-10-27 PT
> **Stage 0 reference profile.** No Hard Gate is passed. Nothing here is an audit.
> **Category:** Routing rail (usage-weighted allocation by ecosystem)
> **OSF mapping:** ORF/OMF **routing rail** · allocation engine · **not replenishment**
> **Related files in this repo:** [`open-source-collective.md`](./open-source-collective.md), [`docs/surveys/oss-survey-inventory.md`](../../surveys/oss-survey-inventory.md) (S22, ecosyste.ms funding data)

## What they do

A joint service of ecosyste.ms (open source usage data) and Open Source Collective (payments). Projects are grouped into "funds", one per ecosystem: a core technology plus what depends on it, such as Rust, Python, Django or Postgres. A sponsor picks the ecosystems it relies on and gives once or on a schedule. Each month the money is split by observed usage and sent to the destinations maintainers list in their funding files. Unlike thanks.dev, it does not look at the sponsor's own dependencies.

## Evidence

| Claim | Figure or fact | Source | Class | Confidence |
|---|---|---|---|---|
| Funds available | 291 ecosystems, each with its own fund (at general availability) | [S1] | Operator announcement | Medium |
| First funder | Sentry, $67,500, opening the Rust, Python, Django and JavaScript funds | [S1] | Operator announcement | Medium |
| Early distribution | Over 80% of initial money paid out in 375 payments to 136 projects | [S1] | Operator announcement | Medium |
| Fee | 10% management fee on donations | [S1] | Operator announcement | Sourced |
| Payout rule | Funds with $1,000 or more allocate 100% of donations to maintainers monthly | [S1] | Operator announcement | Sourced |
| Data behind allocation | Usage across 240m tracked repositories and downloads for 10.7m packages | [S2] | Operator page | Sourced |
| Sentry 2025 giving through it | $75,000 (with Open Source Collective) | [S3] | Donor blog | Medium |
| Current totals | Not stated on the pages opened | — | — | Unverified |

## OSF fit

| OSF layer | What maps | What does not |
|---|---|---|
| dOSPO | Published, repeatable allocation per ecosystem | The algorithm's weights are not published on the overview page |
| OMF | Monthly payments reach many small dependencies | No work terms attached |
| ORF | Allocation for Family D money | Not a source of money |

## Gaps and cautions

- The general-availability post's URL is dated April 2025, but its text refers to a launch "before the holidays", which matches an earlier December 2024 post. Treat the 291 figure as of early 2025.
- Allocation is by usage, which favours widely downloaded packages over important but less visible ones.

## Sources

| ID | URL | Supports | Checked | Access |
|---|---|---|---|---|
| S1 | https://blog.ecosyste.ms/2025/04/04/ecosystem-funds-ga.html | Fund count, first funder, early payouts, fee | 2026-10-27 PT | Fetched |
| S2 | https://funds.ecosyste.ms/overview | Mechanism and data scale | 2026-10-27 PT | Fetched |
| S3 | https://blog.sentry.io/another-year-another-750-000-to-open-source-maintainers | Sentry's 2025 giving | 2026-10-27 PT | Fetched |
</content>
</invoke>
