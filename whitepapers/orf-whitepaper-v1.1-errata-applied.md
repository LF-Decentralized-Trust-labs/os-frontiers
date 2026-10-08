# The Open Replenishment Framework (ORF)

## Closing the Loop on Open Source Sustainability in Web3

> **Edition:** v1.1 (errata-applied manuscript) · **Stage 0** Research Candidate  
> **Author:** Christian Taylor — CoFounder & Chief Open Source Officer, Open Source Cowboy Consulting  
> **Date:** 18 August 2026 (v1.0) · **Errata incorporated:** 1 October 2026 PT  
> **Organization:** Open Source Cowboy Consulting · Web3 Open Source and Governance Advisory Firm  
> **Series:** Third installment alongside dOSPO (who decides) and OMF (how resources go out). Each framework usable independently.  
> **Controlling citation rule:** Where this manuscript differs from `orf-v1.0.pdf`, **this text controls**. Source errata: `whitepapers/ORF_ERRATA.md` / `sources/ORF_ERRATA.md`.  
> **Honesty banner:** No Hard Gate is marked passed. Specifications under `orf/` remain Stage 0. Do not invent expert quotes or unaudited cash totals.

### Contributors (v1.0)

Terence “Tex” McCutcheon · Diane Mueller · Georg Link, Ph.D. · Hart Montgomery · Heather Meeker · Andrew Aitken

### Author's Note

This paper is the third and final installment in a series and is meant to be read alongside the dOSPO paper and the OMF paper. The dOSPO defines the governance coordination layer (who decides); the OMF defines the maintenance deployment layer (how resources go out); the ORF defines the replenishment layer (how resources come back). Together they describe a complete closed loop, but each framework can also be used independently. The instruments catalogued herein describe existing models and options observable in production today, not “must use” mandates for the ORF to operate.

---

## Status of this edition

| Item | Status |
|------|--------|
| Normative framework (§4–§20: thesis, MV-ORF, principles, families, gates, ratios, SCT, P/D scales) | Unchanged in substance from v1.0; still **Stage 0** |
| §2 landscape narratives + Evidence Summary + bibliography | **Rewritten** to incorporate ORF_ERRATA.md; university/foundation tone pass 1 Oct 2026 PT |
| Claim validation pack (OSFL) | 141 claims scored — see `claims/orf-claims-validated.md` (Researchy live-web: 0 flips) |
| PDF retypeset | This markdown is the **author paste target** for the next PDF |

---

## Glossary (selected)

| Term | Definition |
|------|------------|
| **ORF** | Open Replenishment Framework — portfolio design for identifying, validating, collecting, diversifying, measuring, and routing recurring economic value into maintenance of shared open-source infrastructure. |
| **Replenishment** | Conversion of economic value enabled by open infrastructure into recurring, auditable **net** inflows that finance ongoing maintenance. Distinct from funding (one-way disbursement) and routing (moving already-collected money). |
| **Revenue Family** | One of five categories: Structural Network Revenue; Enterprise Earned Revenue; Membership & Certification; Voluntary/Incentivized Contributions; Capital Income. |
| **PCR** | Portfolio Coverage Ratio — recurring non-inflationary net inflows ÷ verified cost floor. PCR ≥ 1.0 is Gate 3. |
| **RCR** | Revenue Concentration Ratio — largest single **payer** ÷ total net inflows; ≤ 0.25 (Gate 5). Not family-share. |
| **Service Capacity Test** | Five-condition test before selling contractual maintenance liability. |
| **P0–P5 / D0–D5** | External precedent vs local deployment evidence — deliberately separate scales. |

---

## Executive Summary

Open source software does not suffer from a lack of economic value. It suffers from a failure to connect the value created by open infrastructure with the resources required to maintain that infrastructure.

The first two papers in this series addressed governance and deployment. Both share an unstated dependency: capital must exist to deploy. In nearly every Web3 ecosystem today, that capital arrives through one-way mechanisms — token issuance, treasury reserves, grants, donations, and corporate sponsorship — that deplete without replenishing.

This paper introduces the **Open Replenishment Framework (ORF)**: an economic and governance framework designed to close that loop. ORF is not a single revenue mechanism. It treats sustainability as a **portfolio design problem**, organizing replenishment across five revenue families while strictly separating revenue generation from routing rails and allocation engines. The framework enforces measurement discipline through six formal replenishment ratios, eight hard gates for declaring self-sustainability, correlation-aware diversification, a mandatory Service Capacity Test before contractual liability may be sold, and paired P0–P5 / D0–D5 scales.

Critically, ORF does **not** propose monetizing open source code. The code remains open. Value is captured around economic assets that cannot be reproduced by copying a repository: maintainer capacity, verified compatibility, canonical network activity, trusted certification, enterprise response commitments, and institutional coordination.

The evidence base is substantial but incomplete. Optimism demonstrates structural sequencer revenue at production scale. ENS demonstrates canonical service revenue feeding a governed endowment. Tidelift-class assurance demonstrates enterprise willingness to pay. Protocol Guild demonstrates structured voluntary pledges. Polkadot demonstrates neutral legal execution beneath decentralized governance. **Yet no reviewed ecosystem combines these mechanisms into a complete, measured, closed-loop architecture.** ORF’s contribution is that synthesis — presented here as a **Stage 0 research candidate**: a testable architecture, not a solved problem.

### What this paper contributes

- **Portfolio economic architecture** — governance-agnostic, chain-agnostic, organizationally neutral.
- **Revenue / routing separation** — payment infrastructure is not sustainability.
- **Measurement discipline** — six ratios, six correlation classes, twelve-field reporting, eight non-compensable gates.
- **Liability safeguards** — Service Capacity Test + Neutral Legal Entity separation.
- **Evidence honesty** — P≠D scales; Stage 0 designation that declines to overstate what ORF has proven.

---

## Framework Summary: The Complete Series

| Layer | Question | Role |
|-------|----------|------|
| **dOSPO** | Who decides? | Community-mandated coordination; policy vs execution separation |
| **OMF** | How resources go out? | Retainers, bounties, pathways, operational support, incubation, resilience |
| **ORF** | How resources come back? | Five families, net-contribution accounting, diversification, hard gates, evidence standards |

**Legitimacy safeguards:** Counter-Value Requirement · Governance Authorization for Structural Collection · Service Capacity Test · Neutral Legal Entity Separation · Independent Audit.

---

## 1. The Problem: One-Way Funding and the Depletion Cycle

Web3 ecosystems have built heavily capitalized funding mechanisms — multi-billion-dollar treasuries, programmable disbursement, transparent on-chain accounting — yet nearly all of this capital flows in one direction. Infrastructure enables enormous commercial and network activity; little of the resulting value returns to the maintenance system that produced it. The model can **fund** open source. It does not **sustain** open source.

### Research finding (cite carefully)

Open source components appeared in **96%** of the commercial codebases analyzed in Synopsys’ 2024 Open Source Security and Risk Analysis (as stated on Synopsys’s 17 March 2024 SBOM post; that page also contains a conflicting “2,400 codebases / 81%” line — do not collapse them). Separately, **Hoffmann**, Nagle & Zhou (HBS Working Paper 24-038) estimate supply-side replacement value of widely used open source at approximately **$4.15 billion** and demand-side value at approximately **$8.8 trillion**. The Synopsys 27 February 2024 press release announces the report and states a high-risk finding (74%); it does **not** restate 96%. Maintain the Synopsys / Hoffmann split — do **not** copy the OMF paper’s erroneous “$4.15 trillion” merge.

### Web3-specific amplifiers

1. Native-token treasuries correlate maintenance capacity with market stress.  
2. Monetary expansion disguises depletion: newly issued tokens feel like revenue but are dilution.  
3. Structural fee success can create false confidence that fees alone solve sustainability (correlation, concentration, legitimacy).

### Documented costs of depletion (illustrative)

- Treasury drawdown without return.  
- Token-correlated collapse of purchasing power.  
- Payer concentration shock (Optimism / Base stack transition as exit-dependency illustration).  
- Endowment mirage: generating ~$3M/year at 3–5% real yield implies ~$60–100M+ principal; ENS yield covers roughly one-fifth of opex (see §2 — dated closes).

**Series diagnosis:** Governance without deployment is inert; deployment without replenishment is terminal.

---

## 2. The Replenishment Landscape

A meaningful set of production mechanisms now exists. The survey below situates ORF relative to those strengths and gaps — mechanism first, magnitudes only when dated or explicitly marked Unverified.

### Grants-era insert (before the comparative table)

The prior Web3 answer was not a fee. It was a round. **Gitcoin Grants** has run quarterly since 2019. Its program page describes quadratic funding: a matching pool raised from donors, allocated by the number of contributors rather than by the size of any one check, with the operator keeping none of the funds. The page displays, without an audit trail on the page itself, 3,715 projects, 3.8 million unique donations, and more than $50 million. Those counters describe a substantial public-goods institution. Under this framework they do **not** constitute replenishment. Gitcoin is Family D money plus an allocation engine: value already raised, then divided. Optimism’s own budget narrative makes the same cut inside one ecosystem. The June 2025 Year 3 update reports ETH collected from chain revenue in one line and OP committed through Retro Funding in another, and it notes that the Foundation’s operating budget comes from the initial token allocation rather than from that ETH. **Retro Funding deploys resources. It does not replenish them.** OMF is the appropriate layer for that deployment. ORF begins where the round ends.

Sources: https://gitcoin.co/program · Optimism Year 3 forum post (below). Site counters are site counters — do not upgrade them.

### Overview of major precedents (mechanism-first; magnitudes dated or Unverified)

| Initiative | Revenue model | What is sourced this edition | Loop? |
|------------|---------------|------------------------------|-------|
| Optimism Superchain | Greater of 2.5% Chain Revenue or 15% Net Onchain Profit (standard chains); OP Mainnet 100% | Year 3 narrative + buyback vote (see below) | Partial |
| ENS DAO / Endowment | Canonical `.eth` fees + governed endowment | Two dated closes (KPK; EP 6.46) — do not stack | Closest |
| Tidelift | Enterprise assurance subscriptions | Named customers; Sonar **definitive agreement** to acquire | Partial |
| Protocol Guild | Voluntary ~1% pledges, vesting, revocable | **196** funded members (22 May 2026); dollar totals not High | Partial |
| Polkadot / PCF | Fees, slashes, issuance; Cayman executor | Legal design sourced; 2025 spend magnitudes Unverified | Partial |
| Octant (Golem) | Staking yield → public goods | 100k ETH stake announcement sourced; epoch totals Unverified | No |
| Cardano POSM | Treasury-funded maintenance programs | Program shape sourced; ADA/$ bounty figures Unverified | No (deployment) |
| Drips / Superfluid / Deep Funding | Rails / allocation engines | Taxonomy: **zero replenishment**; Deep Funding $ figures Unverified | n/a |

### Optimism — The Structural Revenue Model

Optimism’s Superchain is the strongest native protocol-revenue precedent reviewed here. In Optimism’s own terms, **Standard OP Chains** contribute the greater of 2.5% of Chain Revenue or 15% of Net Onchain Profit to the Optimism Collective.

The formula above is the **standard-chain rule**. Current Collective documentation carves out **OP Mainnet**, which contributes **100%** of its revenue to the shared treasury rather than the greater-of split. The August 2024 Collective post that introduced the formula said there were no exceptions. That sentence is superseded.  
— https://docs.optimism.io/governance/capital-allocation

Governance approved, in late January 2026, a **twelve-month pilot** beginning in February that allocates 50% of Superchain sequencer revenue to OP buybacks. The Foundation’s 8 January post describes the proposal as 50% of **incoming** Superchain revenue; contemporaneous reporting of the vote describes it as 50% of **net** Superchain sequencer revenue, passed with 84.4% in favor. **Cite the vote, not only the proposal.**  
— https://optimism.io/blog/op-token-buybacks · https://www.coindesk.com/business/2026/01/28/optimism-governance-approves-op-token-buyback-plan-tied-to-superchain-revenue

**Cumulative figures (Foundation narrative, Medium under Gate 2):** The Optimism Foundation’s Year 3 budget update (Collective forum, 24 June 2025) states 17,756 ETH in all-time Superchain revenue, described as primarily driven by Base revenue share (6,210 ETH) and OP Mainnet (11,170 ETH), and 26.4M OP committed via Retro Funding across 437 grantees. Those two chain figures do not sum to the all-time total; the residual is not itemized. This is a Foundation budget narrative, not an independent audit. The 8 January 2026 buyback proposal reports 5,868 ETH collected over the preceding twelve months — a different window, not a revision of the all-time figure.  
— https://gov.optimism.io/t/collective-year-3-budget-update-and-year-4-budget-outlook/10057

A critical limitation follows: Base moved toward a Base-managed unified software stack while maintaining a transitional support relationship with Optimism, illustrating exit and dependency risk even inside a “structural” mechanism. Structural revenue is not diversification. Retro Funding remains **OMF deployment**, not ORF replenishment.

### ENS — The Closest Closed-Loop Approximation

Among reviewed precedents, ENS is the closest approximation of a working closed loop — and the financial figures must be dated, or they appear to contradict one another. Canonical registration revenue is documented. The **KPK 2025 review**, posted 21 January 2026, reports $18.22 million in operational revenue and $17.54 million in operational expenses, with endowment revenues covering **20.3%** of those expenses, and a December 2025 endowment AUM of $113.86 million. The passed May 2026 Investment Policy Statement (**EP 6.46**) describes a later snapshot: approximately $93.4 million in non-custodial assets under management and more than $8 million in net DeFi returns since inception, and it sizes the three-year stablecoin runway off a different 2025 expense figure, $16.4 million per Steakhouse. **Same institution, two closes.** The instructive limitation survives either print: endowment yield covers roughly one-fifth of operating expenses — a resilience layer, not a complete foundation for opex.  
— https://discuss.ens.domains/t/kpk-2025-review-for-the-ens-endowment/21829 · https://docs.ens.domains/dao/proposals/6.46/

### Tidelift — The Enterprise Demand Proof

Tidelift — **under a definitive agreement announced by Sonar to acquire Tidelift**, pending any later closing announcement — supplies the strongest reviewed evidence that enterprises will pay recurring subscription revenue for assurance around open infrastructure, and that such revenue can flow upstream to maintainers via SBOM-based allocation. Named customers on that release include Cisco, Fannie Mae, and the U.S. Air Force. As a template for Web3 ecosystems, the operational bar is high: professional sales, support, and legal capacity that most ecosystems lack, and that ORF’s Neutral Legal Entity design is intended to supply.  
— https://www.sonarsource.com/company/press-releases/sonar-to-acquire-tidelift/

### Protocol Guild — The Voluntary Pledge Commons

Protocol Guild demonstrates coordinated voluntary replenishment as a **mechanism**: voluntary ≈1% token/yield pledges, vesting, and revocability. That is Family D contribution material — useful diversification — not a foundation for guaranteed operating liabilities.

Protocol Guild’s Q2 2026 membership audit records **196 funded members as of 22 May 2026**, up from 187 the previous quarter. Dollar totals widely repeated for 2025 — including $7.2 million from 6,202 donors, and commitments above $80 million — were **not recoverable** from a rendered primary page in this review and must not be published as High until the 2025 annual report is quoted directly.  
— https://www.protocolguild.org/blog/20260604-Q2-quarterly-audit

### Polkadot / PCF, Cardano POSM, Octant — what is and is not attached

- **Polkadot PCF:** Wiki supports Cayman foundation legal design (Neutral Legal Entity template). Figures such as “~$70.6M 2025 treasury spend,” Anemoy “$1.5M,” and referenda #1122/#1416/#1591 remain **Unverified** — primary citations not yet recovered. https://wiki.polkadot.com/general/pcf/  
- **Cardano POSM:** Intersect explainer supports program shape (OSC/OSO, retainers, Code for Us, incubation) — deployment precedent, not replenishment. “5.885M ADA” and “$300K bounty fully utilized” are **not** on that explainer. https://www.intersectmbo.org/news/the-paid-open-source-model  
- **Octant:** 8 August 2023 announcement that the Foundation stakes 100,000 ETH (validators not yet fully online on that page). “Epoch 8: ~460 ETH (~$1.7M)” remains **Unverified** — primary citation not yet recovered. https://golem.foundation/2023/08/08/announcing-octant.html

### The Routing Mirage

Drips (dependency-tree splits), Superfluid (per-second streaming), and allocation experiments such as Deep Funding are frequently cited as sustainability solutions. They are valuable infrastructure — and they generate **zero replenishment**. They move and divide money that something else must first collect. Deep Funding dollar/repo/dependency aggregates remain **Unverified** until a primary challenge report is quoted. ORF’s taxonomy exists in large part to prevent revenue/routing conflation.

---

## 3. What the Landscape Is Missing

- No deliberately diversified portfolio across uncorrelated classes with measured coverage targets among precedents reviewed.  
- Gross-revenue thinking without cost-to-collect.  
- Revenue conflated with routing.  
- Issuance conflated with income.  
- No published hard, non-compensable self-sustainability test (ORF proposes eight gates).  
- External precedent collapsed into local proof (ORF separates P and D scales).

ORF is portable: any Web3 ecosystem can implement it without dependency on or license from any specific prior program.

---

## 4–20. Framework body (v1.0 substance retained)

> The full normative architecture — Core Thesis, Five Economic Questions, Minimum Viable ORF, five principles, six-stage loop, two-dimensional taxonomy, five revenue families, Neutral Legal Entity, Service Capacity Test, six ratios, eight Hard Gates, correlation classes, P0–P5/D0–D5, Tier 1 feasibility (illustrative), reporting standard, failure modes, research status, adversarial review — is unchanged in substance from `orf-v1.0.pdf` / `sources/orf-whitepaper.txt`. Specs: `orf/INSTRUMENT_CATALOG.md`, `orf/GOVERNANCE_RULES.md`.

### Core thesis (restated)

An open source ecosystem becomes financially resilient when a sufficient portion of the economic value enabled by its infrastructure can be converted into diversified, recurring, auditable **net** inflows capable of financing the ongoing cost of maintaining that infrastructure.

### Minimum Viable ORF (all five)

1. Verified cost floor (published methodology)  
2. Classified inflow inventory (issuance & routing excluded from replenishment totals)  
3. ≥1 earned instrument collecting real receipts (net contribution)  
4. Net-contribution reporting (quarterly public)  
5. Ratio and gate review cadence  

An ecosystem meeting these five is **running ORF** even with PCR ≪ 1.0.

### Eight Hard Gates (none marked passed)

1 Measurement · 2 Cash Evidence · 3 Net Coverage (PCR ≥ 1.0) · 4 Multi-Class Diversity · 5 Concentration (RCR ≤ 0.25) · 6 Stress Runway · 7 Liability Coverage · 8 Independent Audit  

No gate compensates for another. Additive maturity scoring is rejected.

### Critical policy notices

- Monetary expansion / issuance **cannot** count toward non-inflationary self-sustainability metrics.  
- Do not sell maintenance guarantees the ecosystem lacks capacity to fulfill (Service Capacity Test).  
- Payment must not purchase a certification passing result.  
- Capital income is a late-stage resilience layer, not a Day-1 bootstrap.

---

## Conclusion

This series began with a governance question and ends with an economic one. The answer is not a token, a smart contract, a subscription, an endowment, a tax, or any single funding mechanism. It is a **portfolio architecture** held to measurement discipline.

The evidence from production systems supports each **segment** of the loop. What no ecosystem yet demonstrates is the connected whole — and that synthesis, held to Stage 0 honesty, is what this series places on the table.

> Open source infrastructure does not sustain itself.  
> It survives because institutions emerge to support it — and those institutions survive only if value flows back to them.  
> The dOSPO provides the mandate. The OMF provides the machinery. The Open Replenishment Framework closes the loop.

---

## Evidence Summary (v1.1)

| Claim | Primary sources | Confidence |
|-------|-----------------|------------|
| Synopsys 96% OSS in analyzed commercial codebases (SBOM blog); Hoffmann/Nagle/Zhou ~$4.15B / ~$8.8T | Synopsys SBOM 17 Mar 2024 (+ note conflicting 81% line); HBS WP 24-038; press release 27 Feb 2024 (74% high-risk, no 96%) | High for existence of statements; cite carefully |
| Optimism standard-chain greater-of rule; OP Mainnet 100% carve-out; Jan 2026 buyback pilot | docs.optimism.io/governance/capital-allocation; buybacks blog; CoinDesk 28 Jan 2026 | High for mechanism/vote existence; Medium as audited cash |
| Cumulative Superchain 17,756 ETH; Base 6,210; OP Mainnet 11,170; 26.4M OP Retro / 437 grantees; residual not itemized; 5,868 ETH prior-12-mo in buyback proposal | Year 3 forum 24 Jun 2025; buybacks blog 8 Jan 2026 | Medium (Foundation narrative; Gate 2) |
| ENS: dated KPK vs EP 6.46 closes; ~20% opex from endowment | KPK review 21 Jan 2026; EP 6.46 | Medium — do not stack AUM cells |
| Protocol Guild: 196 members (22 May 2026); dollars not High | Q2 2026 audit post | Membership High for audit statement; dollars Unverified |
| Tidelift: definitive agreement to acquire; named customers | Sonar press release | Sourced for agreement + names |
| Polkadot PCF legal design | wiki.polkadot.com/general/pcf/ | Sourced design; spend Unverified |
| POSM program shape | Intersect explainer | Sourced programs; budget Unverified |
| Octant 100k ETH announcement | Golem 8 Aug 2023 | Sourced announcement; epochs Unverified |
| Gitcoin = Family D + allocation; ≠ replenishment | gitcoin.co/program + Year 3 cut | Taxonomy High; counters are site counters |
| No complete closed loop under ORF names among reviewed ecosystems | OSFL Evidence Register judgment | Judgment |

---

## Bibliography (additions / corrections for v1.1)

- Optimism Foundation (2025). Collective Year 3 Budget Update and Year 4 Budget Outlook. 24 June 2025. https://gov.optimism.io/t/collective-year-3-budget-update-and-year-4-budget-outlook/10057  
- Optimism (current). Capital allocation. https://docs.optimism.io/governance/capital-allocation  
- Optimism (2026). OP token buybacks (proposal, 8 January 2026). https://optimism.io/blog/op-token-buybacks  
- CoinDesk (2026). Optimism governance approves OP token buyback plan tied to superchain revenue. 28 January 2026. https://www.coindesk.com/business/2026/01/28/optimism-governance-approves-op-token-buyback-plan-tied-to-superchain-revenue  
- Hoffmann, M., Nagle, F., and Zhou, Y. (2024). The Value of Open Source Software. Harvard Business School Working Paper 24-038. https://www.hbs.edu/faculty/Pages/item.aspx?num=65230  
- Gitcoin. Grants Program. https://gitcoin.co/program  
- KPK (2026). KPK 2025 review for the ENS endowment. 21 January 2026. https://discuss.ens.domains/t/kpk-2025-review-for-the-ens-endowment/21829  
- ENS DAO. EP 6.46 Investment Policy Statement. https://docs.ens.domains/dao/proposals/6.46/  
- Protocol Guild. Q2 2026 Quarterly Audit. https://www.protocolguild.org/blog/20260604-Q2-quarterly-audit  
- Sonar. Sonar to acquire Tidelift (definitive agreement announcement). https://www.sonarsource.com/company/press-releases/sonar-to-acquire-tidelift/  
- Polkadot Wiki. Polkadot Community Foundation. https://wiki.polkadot.com/general/pcf/  
- Intersect. The Paid Open Source Model. https://www.intersectmbo.org/news/the-paid-open-source-model  
- Golem Foundation (2023). Announcing Octant. 8 August 2023. https://golem.foundation/2023/08/08/announcing-octant.html  

Retain remaining v1.0 bibliography entries with **Hoffmann** spelling corrected wherever Hoffman appeared.

---

## About Open Source Cowboy

The Open Replenishment Framework was developed by Open Source Cowboy (opensourcecowboy.org) as the third installment of an ongoing body of work on decentralized open source governance, operations, and economic sustainability, alongside the dOSPO and OMF whitepapers and the Open Source Frontiers research repository at LF Decentralized Trust. ORF is designed to be adopted, adapted, and improved through use.

---

## Companion OSFL pack (not part of the PDF body)

| Artifact | Path |
|----------|------|
| Validated claims (141) | `claims/orf-claims-validated.md` |
| Implementation validation | `claims/implementation-validation.md` |
| Use-case catalog + dossiers | `use-cases/web2-web3-prototypes.md` |
| Researchy expansion (N1–N12) | `use-cases/web2-web3-prototypes-expansion.md` |
| University/foundation synthesis | `synthesis/release1-research.md` |
| Gaps | `synthesis/gaps.md` |

**Stage 0. No Hard Gate passed. Errata incorporated in this manuscript.**
