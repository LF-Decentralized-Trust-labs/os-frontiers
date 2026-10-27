# thanks.dev

> **Pass date:** 2026-10-27 PT
> **Stage 0 reference profile.** No Hard Gate is passed. Nothing here is an audit.
> **Category:** Routing rail (dependency-based allocation)
> **OSF mapping:** ORF/OMF **routing rail** · allocation engine for Family D money · **not replenishment**
> **Related files in this repo:** [`use-cases/dossier-pledge-thanksdev.md`](../../../use-cases/dossier-pledge-thanksdev.md) (full mechanism dossier, 2026-09-24)

## What they do

A platform that scans a donor's code repositories, builds the dependency tree (up to three levels deep, per the description Canonical reproduced) and splits the donor's budget across the maintainers of those dependencies. Donors can adjust weights by language or organization. Only maintainers who register can receive money. It takes a 5% commission. It is the main payout channel for Sentry and is used by Canonical.

## Evidence

| Claim | Figure or fact | Source | Class | Confidence |
|---|---|---|---|---|
| Commission | 5% | [S1] | Donor blog | Medium |
| Canonical commitment | $120,000 over 12 months, at $10,000 a month | [S1] | Donor blog | Medium |
| Canonical recipients | 358 | [S1] | Donor blog | Medium |
| Sentry 2025 distribution | $375,000 via thanks.dev | [S2] | Donor blog | Medium |
| How it allocates | Dependency analysis of the donor's code; the speaker notes that deciding the split algorithmically is hard | [S3] | Conference talk abstract | Sourced |
| Platform-wide totals | Not published on any page found | — | — | Unverified |

## OSF fit

| OSF layer | What maps | What does not |
|---|---|---|
| dOSPO | — | No governance beyond the donor's settings |
| OMF | Low-effort way to reach many small dependencies | No work terms; recipients must sign up |
| ORF | Allocation for Family D money | Not a source of money |

## Gaps and cautions

- Dependencies whose maintainers have not registered receive nothing in that cycle.
- No aggregate figures are published. The two largest known donors (Sentry, Canonical) are the main public evidence.
- Vlad-Stefan Harbuz presented on thanks.dev at FOSDEM 2025 and is also linked to the Open Source Pledge and the Open Source Endowment.

## Sources

| ID | URL | Supports | Checked | Access |
|---|---|---|---|---|
| S1 | https://canonical.com/blog/canonical-thanks-dev-giving-back-to-open-source-developers | Commission, Canonical figures, algorithm description | 2026-10-09 PT | Repo capture (`docs/surveys/data/canonical-thanksdev-2025.txt`) |
| S2 | https://blog.sentry.io/another-year-another-750-000-to-open-source-maintainers | Sentry distribution | 2026-10-27 PT | Fetched |
| S3 | https://fosdem.org/2025/schedule/event/fosdem-2025-4149-funding-open-source-projects-through-dependency-analysis | Allocation description | 2026-10-27 PT | Fetched |
</content>
</invoke>
