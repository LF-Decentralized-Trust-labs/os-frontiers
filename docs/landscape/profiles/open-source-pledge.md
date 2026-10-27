# Open Source Pledge

> **Pass date:** 2026-10-27 PT
> **Stage 0 reference profile.** No Hard Gate is passed. Nothing here is an audit.
> **Category:** Corporate commitment (norm and transparency standard)
> **OSF mapping:** ORF **Family D** (voluntary corporate contribution) · OMF (cash to maintainers chosen by each company) · dOSPO: reporting norm only
> **Related files in this repo:** [`use-cases/dossier-pledge-thanksdev.md`](../../../use-cases/dossier-pledge-thanksdev.md) (full mechanism dossier, 2026-09-24)

## What they do

A voluntary association of companies, launched by Sentry on 8 October 2024. Members commit to pay at least $2,000 per full-time developer per year, in cash, directly to open source maintainers or foundations of their choice, and to publish an annual report. The Pledge never handles the money; it sets the norm and lists members who report. Common payout rails are thanks.dev, Open Collective, GitHub Sponsors and Ecosyste.ms Funds.

## Evidence

| Claim | Figure or fact | Source | Class | Confidence |
|---|---|---|---|---|
| Paid since launch | $7,421,535 | [S1] | Site counter of member self-reports | Medium |
| Paid in the past year | $3,756,826 | [S1] | Site counter of member self-reports | Medium |
| Minimum | $2,000 per full-time developer per year | [S1], [S2] | Program rule | Sourced |
| Earlier total | $4.5m paid since launch, reported in January 2026 | [S3] | Member blog | Medium |
| At launch | 20 companies pledging nearly $1.3m | [S4] | Press | Medium |
| Example members | Sentry, HeroDevs, Zerodha, Bolt, Railway, Prefect, VoidZero, Pydantic, Convex, Speakeasy, ScreenshotOne | [S1], [S5] | Member list | Sourced |
| Validation | Member reports are self-reported; the Pledge does not audit them | [S1] | Program statement | Sourced |
| Key people | Chad Whitacre (Sentry); Vlad-Stefan Harbuz | [S4], [S6] | Press, interview | Medium |

## OSF fit

| OSF layer | What maps | What does not |
|---|---|---|
| dOSPO | Public annual reports are a transparency norm | No shared governance over where money goes |
| OMF | Cash reaches maintainers and foundations | Each company picks its own recipients; no coordination across members |
| ORF | Family D: recurring because members renew yearly | Voluntary; a member can leave at any time |

## Gaps and cautions

- The two totals are different snapshots ($4.5m in January 2026, $7.42m on 9 October 2026). Use the later one, and say it is self-reported.
- The figure counts what members say they paid, including to foundations. It is not a measure of money reaching individual maintainers.
- Allocation is the hard part. Members rely on rails such as thanks.dev to decide who gets paid; see [`thanks-dev.md`](./thanks-dev.md).

## Sources

| ID | URL | Supports | Checked | Access |
|---|---|---|---|---|
| S1 | https://opensourcepledge.com/members/ | Totals, member list, self-report status | 2026-10-09 PT | Repo capture (`docs/surveys/data/opensourcepledge-members-2026-10-09.txt`) |
| S2 | https://opensourcepledge.com/about/ | Rules; no custody of funds | 2026-10-09 PT | Repo capture (`docs/surveys/data/opensourcepledge-about-2026-10-09.html`) |
| S3 | https://blog.sentry.io/another-year-another-750-000-to-open-source-maintainers | $4.5m total, January 2026 | 2026-10-27 PT | Fetched |
| S4 | https://technical.ly/software-development/open-source-pledge-developer-pay/ | Launch figures, leadership | 2026-10-27 PT | Search result |
| S5 | https://screenshotone.com/blog/screenshotone-joins-the-open-source-pledge/ | Small-company member example | 2026-10-27 PT | Search result |
| S6 | https://opensourcesecurity.io/2026/2026-04-open-source-pledge-vlad/ | Allocation challenges, in an interview | 2026-10-27 PT | Search result |
</content>
</invoke>
