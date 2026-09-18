# ORF v1.0 citation errata

This file is a citation layer for [`orf-v1.0.pdf`](./orf-v1.0.pdf). It is not a second paper. Where this file differs from that PDF, this file controls, until the author pastes these sentences into a new PDF.

The sentences below are the author's paste-ready repairs. This commit does not retypeset the PDF.

## Evidence summary — replace the Low Superchain row

> Cumulative Superchain revenue and Retro Funding totals are stated in the Optimism Foundation's Year 3 budget update (Collective forum, 24 June 2025): 17,756 ETH in all-time Superchain revenue, described as primarily driven by Base revenue share (6,210 ETH) and OP Mainnet (11,170 ETH), and 26.4M OP committed via Retro Funding across 437 grantees. Those two chain figures do not sum to the all-time total; the residual is not itemized. This is a Foundation budget narrative, not an independent audit. A later primary post, the 8 January 2026 buyback proposal, reports 5,868 ETH collected over the preceding twelve months — a different window, not a revision of the all-time figure.
> — https://gov.optimism.io/t/collective-year-3-budget-update-and-year-4-budget-outlook/10057 ; https://optimism.io/blog/op-token-buybacks

Confidence: High for the existence of the statements; Medium for treating them as audited cash. Under Gate 2 they are still a single publisher's report.

## Section 2, Optimism paragraph — one sentence after the mechanism

> The formula above is the standard-chain rule. Current Collective documentation carves out OP Mainnet, which contributes 100% of its revenue to the shared treasury rather than the greater-of split. The August 2024 Collective post that introduced the formula said there were no exceptions. That sentence is superseded.
> — https://docs.optimism.io/governance/capital-allocation

Replace "approving the routing of 50% of revenue to OP buybacks" with:

> Governance approved, in late January 2026, a twelve-month pilot beginning in February that allocates 50% of Superchain sequencer revenue to OP buybacks. The Foundation's 8 January post describes the proposal as 50% of incoming Superchain revenue; contemporaneous reporting of the vote describes it as 50% of net Superchain sequencer revenue, passed with 84.4% in favor. Cite the vote, not only the proposal.
> — https://optimism.io/blog/op-token-buybacks ; https://www.coindesk.com/business/2026/01/28/optimism-governance-approves-op-token-buyback-plan-tied-to-superchain-revenue

## Section 2, ENS paragraph — replace the stacked sentence

> ENS is the closest thing the industry has to a working closed loop, and the numbers have to be dated or they contradict each other. Canonical registration revenue is real: the KPK 2025 review, posted 21 January 2026, reports $18.22 million in operational revenue and $17.54 million in operational expenses, with endowment revenues covering 20.3% of those expenses, and a December 2025 endowment AUM of $113.86 million. The passed May 2026 Investment Policy Statement (EP 6.46) describes a later snapshot: approximately $93.4 million in non-custodial assets under management and more than $8 million in net DeFi returns since inception, and it sizes the three-year stablecoin runway off a different 2025 expense figure, $16.4 million per Steakhouse. Same institution, two closes. The instructive limitation survives either print: endowment yield covers about a fifth of operating expenses. It is a resilience layer, not a foundation.
> — https://discuss.ens.domains/t/kpk-2025-review-for-the-ens-endowment/21829 ; https://docs.ens.domains/dao/proposals/6.46/

Also fix the spelling in the research-finding box and the bibliography: **Hoffmann**, not Hoffman. The HBS page is https://www.hbs.edu/faculty/Pages/item.aspx?num=65230 . Do not change the ORF draft's split between Synopsys (96% of codebases, as stated on Synopsys's own 17 March 2024 SBOM post) and Hoffmann/Nagle/Zhou ($4.15 billion supply-side, $8.8 trillion demand-side). The OMF paper merges those and writes "$4.15 trillion." Leave OMF for a separate erratum. Do not copy the error forward.

The Synopsys bibliography URL is the SBOM blog, which does contain the 96% sentence and also a conflicting "2,400 codebases / 81%" line. Add the 27 February 2024 press release as the report announcement and note that the press release states the high-risk finding (74%) and does not restate 96%.

## Protocol Guild — downgrade, do not delete the precedent

Keep the mechanism (voluntary 1% pledges, vesting, revocable). Replace the scale sentence until the annual-report body is captured:

> Protocol Guild's Q2 2026 membership audit records 196 funded members as of 22 May 2026, up from 187 the previous quarter. Dollar totals widely repeated for 2025 — including $7.2 million from 6,202 donors, and commitments above $80 million — were not recoverable from a rendered primary page in this review and should not be published as High until the 2025 annual report is quoted directly.
> — https://www.protocolguild.org/blog/20260604-Q2-quarterly-audit

## Claims to mark unverified, not to invent replacements for

Move these from High to "citation not yet attached" until a page is opened:

- Polkadot "~$70.6M 2025 treasury spend," Anemoy "$1.5M," referenda #1122, #1416, #1591. The wiki page supports the legal design only: https://wiki.polkadot.com/general/pcf/
- POSM "5.885M ADA" and "$300K bounty fully utilized." The Intersect explainer does not contain them: https://www.intersectmbo.org/news/the-paid-open-source-model
- Octant "Epoch 8: ~460 ETH (~$1.7M)." The fetched source is the 8 August 2023 announcement that the Foundation stakes 100,000 ETH, with validators not yet fully online: https://golem.foundation/2023/08/08/announcing-octant.html
- Deep Funding "$220K," "34 seed repos," "5,000+ dependencies." Not fetched.
- Tidelift: change "acquired by Sonar" to "under a definitive agreement announced by Sonar to acquire Tidelift," unless a closing announcement is added. Named customers hold.

## Bibliography lines to add

> Optimism Foundation (2025). Collective Year 3 Budget Update and Year 4 Budget Outlook. 24 June 2025. https://gov.optimism.io/t/collective-year-3-budget-update-and-year-4-budget-outlook/10057
>
> Optimism (current). Capital allocation. https://docs.optimism.io/governance/capital-allocation
>
> CoinDesk (2026). Optimism governance approves OP token buyback plan tied to superchain revenue. 28 January 2026. https://www.coindesk.com/business/2026/01/28/optimism-governance-approves-op-token-buyback-plan-tied-to-superchain-revenue
>
> Hoffmann, M., Nagle, F., and Zhou, Y. (2024). The Value of Open Source Software. Harvard Business School Working Paper 24-038. https://www.hbs.edu/faculty/Pages/item.aspx?num=65230
>
> Gitcoin. Grants Program. https://gitcoin.co/program

Point the existing buybacks URL at the 8 January 2026 proposal explicitly, so a reader does not think it is the vote record.

## Section 2 — grants-era insert, before the table

> The prior Web3 answer was not a fee. It was a round. Gitcoin Grants has run quarterly since 2019. Its own program page describes quadratic funding: a matching pool raised from donors, allocated by the number of contributors rather than by the size of any one check, with the operator keeping none of the funds. The page displays, without an audit trail on the page itself, 3,715 projects, 3.8 million unique donations, and more than $50 million. That is a serious public-goods institution. Under this framework it is not replenishment. It is Family D money plus an allocation engine: value that was already raised, then divided. Optimism's own budget narrative makes the same cut inside one ecosystem. The June 2025 Year 3 update reports ETH collected from chain revenue in one line and OP committed through Retro Funding in another, and it notes that the Foundation's operating budget comes from the initial token allocation rather than from that ETH. Retro Funding deploys resources. It does not replenish them. OMF is the right layer for that deployment. ORF starts where the round ends.

Source URLs for that paragraph: https://gitcoin.co/program and the Year 3 forum post already cited. The displayed Gitcoin counters are the site's counters. The paragraph already says so. Do not upgrade them.
