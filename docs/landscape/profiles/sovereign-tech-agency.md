# Sovereign Tech Agency (Germany)

> **Pass date:** 2026-10-27 PT
> **Stage 0 reference profile.** No Hard Gate is passed. Nothing here is an audit.
> **Category:** Public funder
> **OSF mapping:** OMF (commissioned maintenance, fellowships, resilience services) · dOSPO-like selection (public agency sets criteria) · **not ORF** (federal budget appropriation, not a recurring source the agency earns)
> **Related files in this repo:** [`docs/surveys/oss-survey-inventory.md`](../../surveys/oss-survey-inventory.md) (S14–S16, S23)

## What they do

A German public agency, a subsidiary of SPRIND, Germany's federal agency for breakthrough innovation. It pays for maintenance and security work on open source components that public administrations and businesses rely on. It runs five programs: the Sovereign Tech Fund (commissioned work on chosen technologies), Resilience (vulnerability management services with industry partners), the Fellowship (pays maintainers and, from 2026, community managers and technical writers), Standards (supports maintainers in IETF, W3C and ISO work) and the Challenge (competitions). Work is commissioned under German public procurement law, not given as grants.

## Evidence

| Claim | Figure or fact | Source | Class | Confidence |
|---|---|---|---|---|
| Technologies supported | 118 since October 2022 | [S1] | Site counter | Medium |
| Invested in commissioned work | €41.1m | [S1] | Site counter | Medium |
| Critical technologies identified | 195 | [S1] | Site counter | Medium |
| Annual budget | 2022: €13m; 2023: about €22m; 2024: up to €16m expected | [S2] | Secondary (Wikipedia) | Low |
| Leadership | Adriana Groh and Luisa von Beust (co-CEOs), Fiona Krakenbürger (CTO) | [S2] | Secondary | Low |
| 2026 Fellowship cohort | 14 fellows: 8 maintainers, 4 community managers, 2 technical writers; 2 employed, 12 freelance; 20 applications for employee posts and 150 for freelance | [S3] | Program announcement | Sourced |
| Standards pilot | Runs June 2026 to June 2027 | [S4] | Program page | Sourced |
| Challenge budget | Up to €300,000 per four-month round | [S4] | Program page | Sourced |
| Example investment | KDE: €1,285,200 for 2026–2027 | [S2], [S5] | Secondary | Medium |
| Maintainer survey (2024) | 536 respondents; 33% unpaid; about 30% paid but not enough to live on; 31% work alone | [S6] | Open survey summary | Medium |

## OSF fit

| OSF layer | What maps | What does not |
|---|---|---|
| dOSPO | Published selection criteria; an agency that decides what to fund and contracts operators | Not community-governed; set by a government budget and ministry |
| OMF | Fellowship as a maintainer retainer; Resilience as security services; commissioned maintenance | Engagements are fixed-term contracts, not open-ended retainers |
| ORF | — | No earned or held income. It is the clearest example of public outflow funding |

## Gaps and cautions

- The €41.1m counter (repo capture, 9 Oct 2026) replaces the older "€24.6m across 60+ projects" figure from the EU case study. Do not quote both as current.
- The budget figures come from Wikipedia, not from a budget document. Treat as Low until checked against the Bundestag budget.
- The agency is the model for the proposed EU Sovereign Tech Fund; see [`eu-sovereign-tech-fund.md`](./eu-sovereign-tech-fund.md).

## Sources

| ID | URL | Supports | Checked | Access |
|---|---|---|---|---|
| S1 | https://www.sovereign.tech/tech | 118 technologies, €41.1m, 195 identified | 2026-10-09 PT | Repo capture (`docs/surveys/data/sta-tech-2026-10-09.txt`) |
| S2 | https://en.wikipedia.org/wiki/Sovereign_Tech_Agency | Budget by year, leadership, investment list | 2026-10-27 PT | Fetched |
| S3 | https://www.sovereign.tech/news/meet-the-2026-sovereign-tech-fellows | 2026 Fellowship cohort | 2026-10-27 PT | Fetched |
| S4 | https://www.sovereign.tech/programs | Program list, Standards dates, Challenge budget | 2026-10-27 PT | Fetched |
| S5 | https://muckrack.com/media-outlet/lxer | KDE investment amount and term | 2026-10-27 PT | Search result |
| S6 | https://www.sovereign.tech/news/what-open-source-maintainers-shared-with-us | 2024 maintainer survey | 2026-10-09 PT | Repo capture (`docs/surveys/data/sta-maintainers-shared-2026-10-09.txt`) |
</content>
</invoke>
