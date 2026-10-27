# CHAOSS (Community Health Analytics in Open Source Software)

> **Pass date:** 2026-10-27 PT
> **Stage 0 reference profile.** No Hard Gate is passed. Nothing here is an audit.
> **Category:** Research and measurement
> **OSF mapping:** Measurement layer for dOSPO, OMF and ORF reporting · the evaluator's 15 indicators should map to CHAOSS metrics · not a funder
> **Related files in this repo:** [`tools/GRIMOIRELAB_CHAOSS.md`](../../../tools/GRIMOIRELAB_CHAOSS.md), [`docs/surveys/oss-survey-inventory.md`](../../surveys/oss-survey-inventory.md) (S23)

## What they do

A Linux Foundation project, started in 2017, that defines metrics and builds software for measuring the health and sustainability of open source communities. Metrics are grouped into focus areas (common, diversity and inclusion, risk, value, evolution) and "metrics models" that combine them. Its software includes GrimoireLab (analytics across many data sources). It began in research by Matt Germonprez and Sean Goggins (Universities of Nebraska and Missouri) and has been funded by the Linux Foundation, the Alfred P. Sloan Foundation and Mozilla. It co-wrote a toolkit with the Sovereign Tech Agency on measuring the impact of public funding.

## Evidence

| Claim | Figure or fact | Source | Class | Confidence |
|---|---|---|---|---|
| Host and start | Linux Foundation project, established 2017 | [S1], [S2] | Academic paper; secondary | Medium |
| Founders' research base | Universities of Nebraska and Missouri (Germonprez, Goggins) | [S3] | Community map | Medium |
| Funders | Linux Foundation, Alfred P. Sloan Foundation, Mozilla | [S3], [S4] | Community map; university news | Medium |
| Earlier grant | Over $1.6m in private funding to the two universities (2020) | [S4] | University news | Medium |
| Main software | GrimoireLab is pinned on the CHAOSS GitHub organization | [S5] | Code host | Sourced |
| Software change | A third-party directory says Augur left CHAOSS in March 2026, replaced by CollectOSS; the CHAOSS GitHub page still lists Augur | [S6], [S5] | Secondary vs code host | Low (conflicting) |
| Public funding toolkit | With the Sovereign Tech Agency, NGI Commons and the Linux Foundation | Repo inventory S23 | Method paper | Medium |

## OSF fit

| OSF layer | What maps | What does not |
|---|---|---|
| dOSPO | Health metrics for oversight and transparency reports | Does not set policy |
| OMF | Metrics to choose and review maintenance programs | — |
| ORF | — | Not a money source; measurement only |

## Gaps and cautions

- Confirm the Augur and CollectOSS change on CHAOSS's own site before citing it.
- Mapping the lab's 15 evaluator indicators to CHAOSS metrics would let others read the lab's scores in a standard vocabulary.

## Sources

| ID | URL | Supports | Checked | Access |
|---|---|---|---|---|
| S1 | https://arxiv.org/pdf/2402.14172 | Origin of CHAOSS at the Linux Foundation | 2026-10-27 PT | Search result |
| S2 | https://zenodo.org/records/4627236 | Peer-reviewed description of CHAOSS's first four years | 2026-10-27 PT | Search result |
| S3 | https://sustainoss.org/academic-map/organizations/chaoss.html | Founders, funders | 2026-10-27 PT | Search result |
| S4 | https://unomaha.edu/news/2020/07/open-source-community-health-project-expands-funding-with-unoand-mu.php | $1.6m grant; Sloan and Mozilla | 2026-10-27 PT | Search result |
| S5 | https://github.com/CHAOSS | Pinned software; Augur mention | 2026-10-27 PT | Fetched |
| S6 | https://apis.io/providers/chaoss/ | Augur and CollectOSS change | 2026-10-27 PT | Fetched |
</content>
</invoke>
