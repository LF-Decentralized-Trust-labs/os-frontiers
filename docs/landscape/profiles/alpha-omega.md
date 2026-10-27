# Alpha-Omega (Linux Foundation / OpenSSF)

> **Pass date:** 2026-10-27 PT
> **Stage 0 reference profile.** No Hard Gate is passed. Nothing here is an audit.
> **Category:** Security fund
> **OSF mapping:** OMF (security engagements, audits, security staff at critical projects) · dOSPO-like (a neutral program inside a foundation, funded by several companies) · **not ORF**
> **Related files in this repo:** [`docs/surveys/oss-survey-inventory.md`](../../surveys/oss-survey-inventory.md) (S17), [`openssf.md`](./openssf.md)

## What they do

A security funding program run inside the Linux Foundation alongside OpenSSF. It makes grants to organizations that run critical open source projects and package registries so they can hire security staff, run audits and fix vulnerabilities. It is funded by large technology companies. In March 2026 it and OpenSSF received a joint $12.5m commitment aimed at helping maintainers handle the rise in AI-generated security reports.

## Evidence

| Claim | Figure or fact | Source | Class | Confidence |
|---|---|---|---|---|
| 2025 grants | 31 grants to 18 organizations, $6,155,410 in total, average $198,562 | [S1] | Program annual report | High |
| Package registries | 29.8% of 2025 grants ($2,929,702) | [S1] | Program annual report | High |
| Since inception | $19,674,118 | [S1] | Program annual report | High |
| Backers named in the 2025 report | AWS, Citi, Google, Microsoft | [S1] | Program annual report | High |
| 2026 joint commitment | $12.5m from Anthropic, AWS, GitHub, Google, Google DeepMind, Microsoft and OpenAI, managed by Alpha-Omega and OpenSSF; announced 17 March 2026 | [S2] | Foundation announcement | Sourced |
| Split of the $12.5m | Not stated | [S2] | — | Unverified |
| 2026 grant examples | Ruby Central (security engineers in residence); FreeBSD (AI-assisted vulnerability discovery); amounts not given | [S3] | Newsletter | Low |

## OSF fit

| OSF layer | What maps | What does not |
|---|---|---|
| dOSPO | Neutral host inside a foundation; several funders pool money | Funders and staff decide; no community vote |
| OMF | Security retainers and engagements at critical projects and registries | Mostly organization-level grants, not individual maintainer pay |
| ORF | — | Depends on yearly corporate commitments |

## Gaps and cautions

- **Conflicting 2025 totals.** The annual report says $6,155,410 in 31 grants to 18 organizations. The OpenSSF March 2026 post says Alpha-Omega invested $5.8m in 14 projects in 2025. They may count different things (grants vs projects, or different cut-off dates). This profile uses the annual report.
- Do not add the $12.5m to the since-inception total; it is a new 2026 commitment that is only partly Alpha-Omega's.

## Sources

| ID | URL | Supports | Checked | Access |
|---|---|---|---|---|
| S1 | https://alpha-omega.dev/wp-content/uploads/sites/22/2026/07/Alpha-Omega-Annual-Report-2025_073126a.pdf | 2025 and cumulative figures (report p26) | 2026-10-09 PT | Repo inventory entry S17 (PDF not committed) |
| S2 | https://openssf.org/?p=9804 | $12.5m commitment; OpenSSF's 2025 summary of Alpha-Omega | 2026-10-27 PT | Fetched |
| S3 | https://buttondown.com/ossfunded/archive/2026-06-15/ | 2026 grant examples | 2026-10-27 PT | Fetched |
</content>
</invoke>
