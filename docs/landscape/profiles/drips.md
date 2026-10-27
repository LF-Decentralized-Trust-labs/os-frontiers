# Drips (Drips Network)

> **Pass date:** 2026-10-27 PT
> **Stage 0 reference profile.** No Hard Gate is passed. Nothing here is an audit.
> **Category:** Routing rail (on-chain streaming and dependency splits) and program operator
> **OSF mapping:** ORF/OMF **routing rail** · OMF (Drips Wave contribution cycles) · **not replenishment**
> **Related files in this repo:** [`tools/DRIPS_PROTOCOL.md`](../../../tools/DRIPS_PROTOCOL.md)

## What they do

An Ethereum-based protocol and app, built by Drips Org within the Radworks ecosystem. Anyone can create a "Drip List" of up to 200 recipients (GitHub repositories, Ethereum addresses or other lists) and fund it by continuous stream or one-time gift in any ERC-20 token. Funds are split after each settlement period (monthly on Ethereum mainnet, daily on other networks). Maintainers who claim a repository can forward a share of what they receive to their own dependencies. Drips also runs retroactive funding rounds for ecosystems, and since January 2026 "Drips Wave", recurring cycles that reward contributions to an ecosystem's open source projects.

## Evidence

| Claim | Figure or fact | Source | Class | Confidence |
|---|---|---|---|---|
| Drip List size | Up to 200 recipients; lists can nest | [S1] | Protocol docs | Sourced |
| Settlement | Monthly on Ethereum mainnet; daily on other networks | [S1] | Protocol docs | Sourced |
| Wave with Stellar | First full Wave began 21 January 2026; three Waves completed by the Q1 roundup | [S2], [S3] | Operator blog | Medium |
| Wave activity | Over 1,000 new developers joined Stellar via Wave in Q1 2026; over 30,000 pull requests merged in the Stellar Wave program | [S4] | Operator governance update | Medium |
| Other partners | Filecoin (retroactive funding rounds); UNICEF Venture Fund pilot for digital public goods | [S4], [S5] | Operator update; partner page | Medium |
| Operator finances | Wave revenue roughly covers monthly personnel costs; Q1 2026 ended over budget | [S4] | Operator governance update | Medium |
| 2025 targets | $15m flowing through Drips; 75% of projects with at least one dependency (targets, not results) | [S6] | Governance proposal | Low |
| Cumulative funds streamed | Not stated on the pages opened | — | — | Unverified |
| Fees | Not stated in the docs opened | — | — | Unverified |

## OSF fit

| OSF layer | What maps | What does not |
|---|---|---|
| dOSPO | Collaborative lists where invited members vote on recipients | The owner of a nested list can change it at any time |
| OMF | Wave: recurring, contribution-based payment cycles | Rewards contributions, not ongoing maintenance retainers |
| ORF | Rail for ecosystem treasuries and donors | Not a source of money; issuance and grants pass through it |

## Gaps and cautions

- Most published numbers are targets or activity counts, not dollars paid.
- The Radworks proposal sets goals for 2025; no page opened reports results against them.

## Sources

| ID | URL | Supports | Checked | Access |
|---|---|---|---|---|
| S1 | https://docs.drips.network/support-your-dependencies/overview | Lists, nesting, settlement, tokens | 2026-10-27 PT | Fetched |
| S2 | https://www.drips.network/blog/posts/q4-2025-roundup | Wave start date | 2026-10-27 PT | Search result |
| S3 | https://www.drips.network/blog/posts/q1-2026-roundup | Three Waves completed; UNICEF; Lit Protocol update | 2026-10-27 PT | Search result |
| S4 | https://community.radworks.org/t/drips-org-q1-2026-update/3721 | Wave activity, partners, finances | 2026-10-27 PT | Fetched |
| S5 | https://www.unicef.org/hope-hct/stories/advancing-sustainable-funding-unicef-digital-public-goods | UNICEF Drip List pilot | 2026-10-27 PT | Search result |
| S6 | https://community.radworks.org/t/formal-review-drips-org-proposal-2025/3614 | 2025 targets | 2026-10-27 PT | Search result |
</content>
</invoke>
