# Gitcoin (Gitcoin Grants)

> **Pass date:** 2026-10-27 PT
> **Stage 0 reference profile.** No Hard Gate is passed. Nothing here is an audit.
> **Category:** Allocation program (crowdfunding with matching pools)
> **OSF mapping:** OMF allocation · dOSPO-like delegation (Gitcoin 3.0 "domain allocators") · **not replenishment** (repo policy: Gitcoin is allocation)
> **Related files in this repo:** [`docs/surveys/oss-survey-inventory.md`](../../surveys/oss-survey-inventory.md) (S28)

## What they do

A program that funds open source and public goods, mainly in the Ethereum ecosystem, through rounds where small donations are matched from a pool using quadratic funding (a formula that rewards broad support over large single gifts). In April 2025 it wound down its software division, Gitcoin Labs, including Grants Stack and the Allo Protocol, citing no realistic path to profitability; the grants program continued. Under "Gitcoin 3.0", rounds are run by community-appointed domain operators who each choose a mechanism. GG24 (October–November 2025) was the first round on that model.

## Evidence

| Claim | Figure or fact | Source | Class | Confidence |
|---|---|---|---|---|
| Lifetime distributed | Over $60m through the Grants Program | [S1] | Press | Medium |
| Lifetime (site counter) | $50,000,000+ towards public goods; 3,715 projects; 3.8m donations | [S2] | Site counter | Low |
| Software wind-down | Gitcoin Labs, Grants Stack and Allo Protocol wound down, announced 25 April 2025 | [S1] | Press | Medium |
| Program runway | Grants Program funded until "2029ish", per co-founder Kevin Owocki | [S1] | Press | Medium |
| GG24 total | Over $1.8m across six domains: $1.175m Gitcoin matching, about $632,500 from external partners | [S3] | Operator case study | Medium |
| GG24 open source rounds | 78 projects; about 1,300 donors gave $36,657, amplified by $300,000 matching | [S3] | Operator case study | Medium |
| GG24 mechanisms | Quadratic funding, private voting (MACI), peer-reviewed hypercerts, milestone grants, conviction voting, retroactive rewards | [S3] | Operator case study | Medium |

## OSF fit

| OSF layer | What maps | What does not |
|---|---|---|
| dOSPO | Gitcoin 3.0 separates who runs rounds (domain operators) from who funds them | Domain operators are appointed, with terms not published on the pages opened |
| OMF | Many small allocations; wide choice of mechanisms | One-off rounds, not predictable pay |
| ORF | — | Matching pools come from treasury and partners; not replenishment |

## Gaps and cautions

- Lifetime totals disagree: over $60m (press, April 2025) vs $50m+ (site counter, October 2026). Neither is audited.
- In GG24's open source rounds, matching ($300,000) was about eight times the direct donations ($36,657). Most money came from the pool, not the crowd.

## Sources

| ID | URL | Supports | Checked | Access |
|---|---|---|---|---|
| S1 | https://theblock.co/post/352055/ethereum-public-goods-funding-protocol-gitcoin-winding-down-its-software-division | Wind-down, lifetime total, runway | 2026-10-27 PT | Fetched |
| S2 | https://gitcoin.co/program | Site counters | 2026-10-09 PT | Repo capture (`docs/surveys/data/gitcoin-program-2026-10-09.txt`) |
| S3 | https://gitcoin.co/case-studies/gg24-first-funding-round-of-gitcoin-3-0 | Gitcoin 3.0, GG24 figures | 2026-10-27 PT | Fetched |
</content>
</invoke>
