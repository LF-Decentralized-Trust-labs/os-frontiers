> **Changelog: Reconciled with researchy-chain-check.md, 9 Oct 2026 (~04:08 PT).** All 58 Researchy rows applied (42 Validated · 7 Partial · 3 Needs update · 5 Unverified · 1 Broken). Inline tags read **[RC: status · source · 2026-10-09]**. Key edits:
> - OpenSats cumulative fixed (Broken → $29,914,999 / 352 grantees, live counter).
> - Zcash fund restated (lockbox ~68.5k ZEC ≈ $83M + 78.75k ZEC multisig; Unverified). Zcash end-height wording and NU7 dates (testnet 6 Oct, mainnet target 5 Nov 2026) added; veto reworded as announced intent.
> - Hyperliquid $14.58M confirmed on-chain (3 Oct 2026); DefiLlama Q3 fees $224.2M and AF stock added; ~93% stays Unverified; USDH grants → Partial.
> - TRON shown both ways ($701.4M self-reported vs ≈$77.8M DefiLlama; Partial). TBL $5M Validated.
> - BNB MVB terms completed (Partial); BNB Grants → Partial.
> - CleanCore and HRF Validated. Monero CCS examples updated. Solana treasury confirmed unpublished.
> - Protocol Guild Validated; ">$80M commitments" stays Unverified.
> - **No score, phase, or placement changes** (§6). §5 replaced by the post-reconciliation open-items table.

# Top 10 L1/L2 Networks: How They Fund Open Source, Scored Against ORF

> **Status:** OSFL research note. **Stage 0.** No ORF Hard Gate is marked passed for any ecosystem below, and none is passed for ORF itself.
> **Prepared:** 9 Oct 2026, ~03:50–04:30 PT. Executor research pass. **Not pushed to GitHub.**
> **Framework sources (repo `LF-Decentralized-Trust-labs/os-frontiers` @ `9a82a9c`, 8 Oct 2026 07:42 PT):** `whitepapers/ORF_ERRATA.md` (controls over `orf-v1.0.pdf`), `whitepapers/orf-whitepaper-v1.1-errata-applied.md`, `orf/START_HERE.md`, `orf/5_QUESTION_ASSESSMENT.md`, `orf/GOVERNANCE_RULES.md`, `orf/FORK_RESISTANCE_ANALYSIS.md`. (`whitepapers/ORF_WHITEPAPER.md` is an 11-line pointer file only.)
> **Rules for figures:** Every dollar figure carries a source and date. If I could not open a primary page for a dollar figure, it is marked **Unverified**. Anything unknown is marked **unknown**. Token amounts converted to USD by me are marked *derived* and use the 9 Oct 2026 CoinGecko price.

---

## 0. Ranking rule and snapshot

**Rule (from the team's scope update):** top 10 **layer-1 and layer-2 networks**, ranked by the market cap of the **native token**. Excluded: stablecoins (USDT, USDC, USDS, USDe, DAI, USD1, …), wrapped/pegged assets, RWA tokens (Figure Heloc), exchange tokens that aren't their own chain (LEO, WBT), and application/oracle tokens that aren't an L1/L2 (LINK, UNI, AAVE, …).
- **Edge cases (my calls):** **BNB is included.** It started as an exchange token, but it is now the native gas and staking token of BNB Smart Chain. **WBT is excluded.** WhiteBIT's token has a chain (Whitechain), but its value comes mostly from the exchange. If you rank it as a chain, it would land between DOGE and XMR, so flag this if you disagree. **HYPE is included** because it is the native token of the Hyperliquid L1 (HyperCore/HyperEVM).
- **There's no L2 in the top 10.** By CoinGecko rank, the largest L2 native token today is Mantle (MNT, **#56 on CoinGecko**, ~$1.81B; #47 on CMC). Next are ARB (CG #70) and POL (CG #78). **[RC: Validated]** The repo's Optimism precedent is outside this set.

**Primary source:** CoinGecko `/coins/markets` API, `last_updated` 2026-10-09T10:51:48Z (**03:51 PT, 9 Oct 2026**). Raw JSON saved as `chains/data/coingecko-markets-2026-10-09.json`.
**Re-pull (Researchy, 03:58 PT; data 03:56:49 PT):** same order and overall ranks, with caps drifting under 0.3% (e.g. BTC $1,656.70B, ZEC $20.65B, HYPE $19.03B, XMR $10.08B). **[RC: Validated · https://api.coingecko.com/api/v3/coins/markets · 2026-10-09]**
**Cross-check:** coinmarketcap.com homepage, fetched 03:53 PT on 9 Oct 2026 (`chains/data/coinmarketcap-home-2026-10-09.html`). The two sources list the same ten networks. The only difference is that CMC puts HYPE (~$21.79B) above ZEC (~$20.68B).

| Chain rank | Network | Token | CoinGecko overall rank | Market cap (CoinGecko, USD) | Price | CMC market cap (USD) |
|---|---|---|---|---|---|---|
| 1 | Bitcoin | BTC | 1 | $1,655.55B | $82,384 | $1,654.82B |
| 2 | Ethereum | ETH | 2 | $303.77B | $2,487.50 | $304.19B |
| 3 | BNB Chain | BNB | 4 | $98.77B | $741.76 | $98.71B |
| 4 | XRP Ledger | XRP | 5 | $87.22B | $1.38 | $87.67B |
| 5 | Solana | SOL | 7 | $64.41B | $109.41 | $64.52B |
| 6 | TRON | TRX | 8 | $31.53B | $0.332 | $31.53B |
| 7 | Zcash | ZEC | 10 | $20.66B | $1,217.21 | $20.68B |
| 8 | Hyperliquid | HYPE | 11 | $19.04B | $85.57 | $21.79B |
| 9 | Dogecoin | DOGE | 12 | $13.14B | $0.0841 | $14.49B |
| 10 | Monero | XMR | 14 | $10.11B | $537.27 | $10.11B |
| *(11; holds only if WBT stays excluded) [RC: Validated]* | *Cardano (repo POSM precedent)* | *ADA* | *17* | *$8.88B* | *$0.236* | *$8.70B* |

---

## 1. ORF criteria used (taken from the repo, not invented)

1. **5-Question Posture Assessment** (`orf/5_QUESTION_ASSESSMENT.md`). Each question scores 0–5, for a total out of 25. 0–9 = *Phase 1 Reserve-Funded*, 10–18 = *Phase 2 Fee-Supplemented*, 19–25 = *Phase 3 Self-Sustaining*. The rubric only defines anchors at 0, 3, and 5, so intermediate scores are my interpolation and each one has a written rationale.
   - **Q1 Ratio**: replenishment vs one-way funding (grants, drawdown, dilution).
   - **Q2 Anchors**: fork resistance. Does collection attach to a non-copyable asset (canonical state or liquidity, a registry, an SLA)?
   - **Q3 Bundles**: benefit bundling. Is it "sold, not taxed"?
   - **Q4 Mandate**: chartered, time-bounded, publicly reported collection.
   - **Q5 Runway**: survives a 2–3 year bear market without an emergency draw.
2. **Five revenue families** (`orf/START_HERE.md` §4): **A** Structural Network Revenue · **B** Enterprise Earned · **C** Membership & Certification · **D** Voluntary/Incentivized · **E** Capital Income.
3. **Policy exclusions** (v1.1 manuscript, "Critical policy notices"; `START_HERE` §2): issuance or monetary expansion **cannot** count toward non-inflationary sustainability. **Routing rails and allocation engines are not revenue.** Retro Funding, Gitcoin, Drips, and Superfluid are **not** replenishment.
4. **Eight Hard Gates** (`orf/GOVERNANCE_RULES.md` §2): Measurement · Cash Evidence · Net Coverage (PCR ≥ 1.0) · Multi-Class Diversity · Concentration (RCR ≤ 0.25) · Stress Runway · Liability Coverage · Independent Audit. **No ecosystem below is marked as passing any gate.** Public evidence isn't enough to assess them, and ORF rejects additive scoring.
5. **Correlation classes** (`GOVERNANCE_RULES` §4). Staking yield is **Class 2 (native token price)**, not Class 5 capital-market return. This matters for Ethereum.

"Revenue family present" below means a family that funds **open-source/public-goods maintenance** for that ecosystem. Burns, validator rewards, and buybacks aren't counted as present because they don't flow to maintenance.

---

## 2. Summary table

Q columns are 5-Question scores (0–5). Family columns: ✅ present · ◐ partial or caveated · ❌ missing · ? unknown.

| # | Network | Q1 Ratio | Q2 Anchors | Q3 Bundles | Q4 Mandate | Q5 Runway | **Total /25** | ORF phase | A | B | C | D | E | Primary OSS funding mode today |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Bitcoin | 1 | 0 | 0 | 2 | 2 | **5** | Phase 1 | ❌ | ❌ | ❌ | ✅ | ? | Donor nonprofits (OpenSats, Brink, HRF BDF) + corporate sponsor (Spiral) |
| 2 | Ethereum | 1 | 2 | 1 | 2 | 3 | **9** | Phase 1 (top) | ◐ (L2/app layer only) | ❌ | ❌ | ✅ | ◐ (EF staking yield = Class 2) | Foundation treasury drawdown (EF) + voluntary pledges (Protocol Guild) |
| 3 | BNB Chain | 0 | 1 | 0 | 0 | 0 | **1** | Phase 1 | ❌ | ❌ | ❌ | ◐ (corporate/VC sponsor) | ? | Corporate builder fund (YZi Labs + BNB Chain), partly equity (SAFE) |
| 4 | XRP Ledger | 0 | 1 | 0 | 1 | 0 | **2** | Phase 1 | ❌ | ❌ | ❌ | ◐ (corporate sponsor) | ? | Ripple corporate funding → distributed funders (XRPL Commons, XAO DAO) |
| 5 | Solana | 0 | 1 | 1 | 1 | 1 | **4** | Phase 1 | ❌ | ❌ | ❌ | ◐ (foundation reserve) | ? | Solana Foundation grants (incl. convertible grants), delegation program |
| 6 | TRON | 0 | 1 | 0 | 1 | 0 | **2** | Phase 1 | ❌ | ❌ | ❌ | ◐ (TRON DAO incubator) | ? | TRON DAO / TRON Builders League incubation |
| 7 | Zcash | 2 | 3 | 0 | 4 | 2 | **11 (raw)** † | Phase 1 (policy cap) † | ◐ (protocol stream, but **issuance**: excluded) | ❌ | ❌ | ✅ | ? | **Protocol-level dev fund** (8% ZCG + 12% coinholder-controlled fund, from block subsidy) |
| 8 | Hyperliquid | 0 | 3 | 1 | 1 | 0 | **5** ‡ | Phase 1 ‡ | ◐ (fee capture exists, routed to **buyback/burn**, not maintenance) | ❌ | ❌ | ◐ (foundation, ad hoc) | ? | Hyper Foundation, ad hoc. L1 source **not open** |
| 9 | Dogecoin | 0 | 0 | 0 | 1 | 0 | **1** | Phase 1 | ❌ | ❌ | ❌ | ◐ (Foundation CoreFund) | ❌ | Fixed 5M DOGE CoreFund paid per Core release |
| 10 | Monero | 1 | 0 | 0 | 2 | 1 | **4** | Phase 1 | ❌ | ❌ | ❌ | ✅ | ❌ | Community Crowdfunding System (CCS) + General Fund |

† **Zcash cap:** the raw sum is 11, which would read as Phase 2 "Fee-Supplemented". But Zcash's funding comes from **block-subsidy issuance, not fees**, and ORF policy says issuance cannot count toward non-inflationary sustainability. I cap the reported phase at Phase 1 and show the raw score so the cap is visible. I treat this as an application of policy, not a gate result.
‡ **Hyperliquid caveat:** the HyperCore L1 source code isn't public (see §3.8). ORF's premise is *open* infrastructure, so this chain is partly **out of frame** until the source is opened.

**Overall:** all ten are **Phase 1 (Reserve-Funded / one-way)** under ORF. **Zero of ten** meet Minimum Viable ORF: none publishes a verified cost floor, a classified inflow inventory that excludes issuance, net-contribution reporting, and a ratio/gate review cadence. Ethereum and Zcash are closest, for different reasons.

---

## 3. Per-chain sections

### 3.1 Bitcoin (BTC): donor-funded commons, no protocol funding

**How OSS is funded**
- **Protocol level:** none. There's no treasury, dev fee, or fee split. Block subsidy and fees go entirely to miners.
- **OpenSats** (501(c)(3)), *2025 Year in Review*, 27 Jan 2026: allocated **$2,328,000** to long-term support (LTS) and **$5,639,789** to non-LTS General Fund grants in 2025. It received **674 donations totalling $3,158,680** in 2025, and says it sends "roughly $1,000,000 USD worth of sats" per month. Operations are funded separately, partly by HRF. — https://opensats.org/blog/2025-year-in-review **[RC: Validated · Researchy check 2026-10-09]**. **Cumulative (fixed; the earlier "$32,142,244 / 377 grantees" was Broken, not on the cited page):** the live counter reads **$29,914,999 to 352 grantees in 40 countries** (https://opensats.org/funds, read 9 Oct 2026). The year-in-review page's own counter reads $21,646,000 and its text says "over 370 grants". **[RC: Broken → fixed · Researchy check 2026-10-09]**
- **Brink**, *2025 Annual Report*, 26 May 2026: donors contributed **~$7,800,000** in 2025, and total expenses were **~$2,600,000** (~87% programs). It funded 8 engineers and completed Bitcoin Core's first third-party security audit. **2026 plans** include a bug bounty program and "experimenting with enterprise testing software". — https://brink.dev/blog/2026/05/26/2025-annual-report/ **[RC: Validated · Researchy check 2026-10-09]**
- **HRF Bitcoin Development Fund**, 2026 rounds: 13 Jan 2026, 22 projects, 1.3B sats; 1 Apr 2026, 26 projects, 1.5B sats; 25 Aug 2026, 16 projects, 500M+ sats. — https://hrf.org/latest/hrfs-bitcoin-development-fund-announces-support-for-22-projects-worldwide/ · https://hrf.org/latest/hrfs-bitcoin-development-fund-announces-support-for-26-projects-worldwide/ · https://hrf.org/latest/hrf-grants-500m-satoshis-to-16-freedom-tech-projects-worldwide/ **[RC: Validated, pages opened · Researchy check 2026-10-09]**
- **Spiral (Block Inc.):** corporate grants for Bitcoin OSS. The total is **unknown**. — https://spiral.xyz/grants/ **[RC: Unverified (no total published) · Researchy check 2026-10-09]**

**ORF alignment (5 / 25)**
- Q1 = 1: donation inflows recur, but there's no replenishment ratio, and no value generated by Bitcoin flows back structurally. OpenSats donations ($3.16M) were well below its 2025 allocations ($7.97M), so it's drawing on prior gifts (a depletion signature).
- Q2 = 0: none of the collection is attached to a fork-resilient anchor.
- Q3 = 0: donations are unbundled. Brink's enterprise-testing experiment is the first Family-B-shaped seed, but it's D0 (hypothesis).
- Q4 = 2: strong transparency (OpenSats quarterly financials, Brink annual report) but no community-chartered collection mandate.
- Q5 = 2: Brink's 2025 inflows were about 3× its expenses, which suggests a reserve, but its runway isn't published. Holdings are BTC-correlated.
- **Families:** D ✅. A, B, C ❌. E unknown.
- **Verdict:** a well-run donor commons. A one-way, Family D-only model.

### 3.2 Ethereum (ETH): largest foundation treasury, moving to an endowment model

**How OSS is funded**
- **Protocol level:** the EIP-1559 base fee is **burned**. There's no protocol share for maintenance.
- **Ethereum Foundation treasury:** "As of October 31 2024 … approximately **$970.2 million** split between **$788.7 million in crypto** [99.45% ETH] and **$181.5 million** in non-crypto." This is the latest published total. **No 2025/2026 total was found (unknown).** — EF Report 2024 PDF, https://ethereum.foundation/report-2024.pdf (opened) **[RC: Validated · Researchy check 2026-10-09]** Researchy found no EF report for 2025 or 2026 (report-2025.pdf and report-2026.pdf return 404). A *secondary* estimate puts EF ETH holdings at ~$209M (CryptoRank, late Jun 2026) after 2026 OTC sales (The Block, 1 May 2026: ~$47M to BitMine). That's wallet holdings only and not primary, so the total stays **unknown**.
- **EF Treasury Policy** (4 Jun 2025): annual opex target A = **15% of treasury**, fiat opex buffer B = **2.5 years**. Opex to be reduced "roughly linearly over the next five years, ending at a long-term **5% baseline** common for endowment-based organizations." — https://blog.ethereum.org/2025/06/04/ef-treasury-policy **[RC: Validated · Researchy check 2026-10-09]** (It's a ~5-year linear glide from 15% to a 5% long-run baseline, not a cut per year.)
- **EF treasury staking** (24 Feb 2026): "Approximately **70,000 ETH** is being staked with rewards directed back to the EF treasury." — https://blog.ethereum.org/2026/02/24/staking **[RC: Validated · Researchy check 2026-10-09]**
- **EF ESP grants:** Q1 2026 total awarded **$9,856,014.14**; Q2 2026 **$5,502,930.20**. — https://blog.ethereum.org/2026/04/29/allocation-q1-26 · https://blog.ethereum.org/2026/08/18/allocation-q2-26. ESP paused open applications on 29 Aug 2025 and reopened on 3 Nov 2025 as Wishlist and RFP tracks. — https://blog.ethereum.org/2025/08/29/esp-next-chapter · https://blog.ethereum.org/2025/11/03/new-esp-grants **[RC: Validated · Researchy check 2026-10-09]**
- **Protocol Guild**, *Annual Report 2025* (29 Jan 2026): raised **$7,231,668** in 2025 (valued at donation; $2,634,505 at report-date value) from **6,202 unique donors**. **$12.4M** vested and distributed to members in 2025 (median ~$62k/member). All-time inflows **$183M** at time of donation. The 1% pledge accounts for ~83% of total funding to date. Launched "Sponsor a Core Dev" in 2025. — https://www.protocolguild.org/blog/20260129-annual-report-2025 **[RC: Validated · Researchy check 2026-10-09]** (309,183 total donations; "Sponsor a Core Dev" announced 18 Dec 2025, https://www.protocolguild.org/blog/20251218-sponsor-core-devs). The errata's "commitments above $80 million" isn't in the report and stays **Unverified [RC]**. **Q3 2026 audit** (26 Aug 2026): **190 members** as of 5 Aug 2026, down from 196. — https://www.protocolguild.org/blog/20260826-q3-quarterly-audit **[RC: Validated · Researchy check 2026-10-09]**
- **Gitcoin, Octant, Optimism Retro Funding** operate in the ecosystem. Under ORF these are **Family D money + allocation engines, not replenishment** (repo hard rule).
- **L2/app layer:** Optimism's Superchain revenue share and ENS's `.eth` fees are the repo's main Family A precedents. They fund *those* collectives, not Ethereum L1 maintenance. See the repo §2 text, and don't stack the ENS KPK and EP 6.46 closes.

**ORF alignment (9 / 25)**
- Q1 = 1: EF opex is mostly a drawdown of the genesis allocation (the repo's v1.1 manuscript notes the Optimism Foundation makes the same split). Staking yield and PG pledges are real recurring inflows, but no replenishment ratio is published.
- Q2 = 2: staking yield is anchored to canonical consensus, which is fork-resilient, but it's Class 2 native-token-correlated. Protocol fees are burned, not captured.
- Q3 = 1: PG's 1% pledges are mostly unbundled. "Sponsor a Core Dev" is closer to a named benefit, and LayerZero's 2024 airdrop-claim donation was a forced bundle, not a sold one.
- Q4 = 2: the treasury policy is published (A/B parameters, ETH-sale cadence) and ESP reports quarterly. But the EF is a foundation, not a community-mandated collector, and there's no sunset or charter on collection.
- Q5 = 3: the policy holds a 2.5-year fiat opex buffer (the rubric's 3-point anchor is 12–18 months of stable assets) plus a productive sleeve (staking). It's still highly ETH-correlated.
- **Families:** D ✅. E ◐ (staking yield returns to treasury, but it's Class 2, not Class 5). A ◐ at L2/app layer only. B and C ❌.
- **Verdict:** best-capitalized and most transparent, and moving toward an endowment model. Still one-way at L1.

### 3.3 BNB Chain (BNB): burn-centric tokenomics, corporate/VC builder funding

**How OSS is funded**
- **Protocol level:** fees go to validators. **BEP-95** burns a governed share of block gas fees (initially 10%). — https://github.com/bnb-chain/BEPs/blob/master/BEPs/BEP95.md **[RC: Validated · Researchy check 2026-10-09]**. **Quarterly Auto-Burn**: the 36th burn (Jul 2026) destroyed **1,615,827.795 BNB**, leaving 133,166,127.91 BNB. — https://www.bnbchain.org/en/blog/36th-bnb-burn (page opened; "at time of writing 15 July, 2026"; burn value ~$931.7M) **[RC: Validated · Researchy check 2026-10-09]**. None of it is routed to maintenance.
- **$1B Builder Fund** "backed by YZi Labs", announced **8 Oct 2025**. — https://www.bnbchain.org/en/blog/1b-builder-fund-to-empower-builders-backed-by-yzi-labs-and-bnb-chain (opened) **[RC: Validated · Researchy check 2026-10-09]**. The headline is a *commitment*. **Disbursed amount unknown.**
- **MVB accelerator:** 200+ projects over ten seasons (same post; **[RC: Validated]**). **Terms (corrected):** up to **$500,000** = **$150,000 for 5% equity via SAFE** (plus other rights) **+ an additional $350,000 on an uncapped SAFE**. That is **equity investment, not grants**. MVB now runs inside YZi Labs' EASY Residency, and MVB 11 applications closed 6 Sep 2025. — https://www.bnbchain.org/en/blog/mvb-11-where-founders-break-through (20 Aug 2025) · https://www.yzilabs.com/easy-residency **[RC: Partial; the earlier text omitted the $350K uncapped SAFE · Researchy check 2026-10-09]**
- **BNB Chain Grants:** "up to **$200,000**" appears only in a 2024 BNB Chain blog (MVB alumni eligible for Builder Grants). The grants page URL now returns 404, so there's no current primary. — https://www.bnbchain.org/id-ID/blog/a-guide-to-web3-development-in-2024 **[RC: Partial · Researchy check 2026-10-09]**
- Foundation or treasury size for core client maintenance: **unknown**.

**ORF alignment (1 / 25)**: Q1 0 · Q2 1 (canonical chain activity exists but isn't captured for maintenance) · Q3 0 (equity-for-capital isn't a benefit bundle) · Q4 0 (no chartered collection, and the fund is corporate) · Q5 0 (unknown; scored 0 for lack of evidence).
- **Families:** D ◐ (corporate/VC sponsor). A, B, C ❌. E unknown.
- **Verdict:** value is burned or paid to validators, and builder funding is corporate/VC. Not aligned with ORF.

### 3.4 XRP Ledger (XRP): corporate sponsor decentralizing its grant channels

**How OSS is funded**
- **Protocol level:** XRPL transaction costs are "irrevocably destroyed" (burned), not paid to anyone. — https://xrpl.org/docs/concepts/transactions/transaction-cost **[RC: Validated · Researchy check 2026-10-09]**
- **Ripple**, *Supporting Innovation on the XRP Ledger: What's Changing in 2026*, 26 Feb 2026: "Since 2017, more than **$550 million** … deployed directly into XRPL ecosystem initiatives" (grants, incentives, partnerships), supporting "nearly 200 projects" since 2021. In 2026 Ripple moves to a "more distributed model": FinTech Builder Program, **XAO DAO** (microgrants), **XRPL Commons** (GLOW retro program, the Aquarium incubator), **XRP Asia**, UDAX, and VC partners. — https://ripple.com/insights/supporting-innovation-on-the-xrp-ledger (opened) **[RC: Validated · Researchy check 2026-10-09]** (still self-reported). The $550M is Ripple's own figure and hasn't been audited (Gate 2).
- Ripple's XRP escrow and treasury as an OSS funding source: **unknown / not itemized** for OSS.

**ORF alignment (2 / 25)**: Q1 0 · Q2 1 · Q3 0 · Q4 1 (published program structure. XAO DAO adds community voting on *allocation*, not collection) · Q5 0 (unknown).
- **Families:** D ◐ (corporate sponsor). A, B, C, E ❌/?. Note that XRPL Commons' GLOW is retroactive funding, which under the repo rule is **not replenishment**.
- **Verdict:** a corporate-sponsor model. 2026 changes decentralize *allocation*, not *collection*.

### 3.5 Solana (SOL): foundation reserve plus monetary-policy governance

**How OSS is funded**
- **Protocol level:** inflation and fees go to validators and stakers. **SIMD-0096** (activated 12 Feb 2025) sends 100% of priority fees to the block producer. Base fees remain 50% burned / 50% to the validator. — https://github.com/solana-foundation/solana-improvement-documents/pull/96 · https://solana.com/docs/core/fees/fee-structure **[RC: Validated · Researchy check 2026-10-09]** (the SIMD-0096 activation date wasn't re-checked by Researchy). No protocol share for maintenance.
- **Solana Foundation grants:** rolling, milestone-based grants for public goods, **convertible grants** for projects with commercial components, and RFPs. — https://solana.org/grants-funding **[RC: Validated]**. The page's only aggregate is an undated cumulative "500+ projects funded / $100M+ in funding". Annual grant totals: **unknown**. **Foundation treasury size: not published** (the Foundation-commissioned Blockworks Q2-2026 report has no treasury figure; The Block, 9 Oct 2025, says the Foundation didn't respond) **[RC: Validated as unknown · Researchy check 2026-10-09]**. Foundation *delegation* stake ~20.83M SOL (Jun 2026, epoch 989) per Phase, a secondary source, and Blockworks Q2-2026 says delegation subsidies were wound down. That's delegation, not treasury. — https://www.phase.cc/blog/solana-foundation-delegation-program-data **[RC: Partial · Researchy check 2026-10-09]**
- **Client development:** Anza (Agave) and Jump (Firedancer) are privately funded. Amounts are **unknown**.
- **Governance (monetary, not funding):** SIMD-0228 (market-based inflation) failed to reach quorum in 2025. **SIMD-0550 / SGP-0002 "Double Disinflation"** passed on **28 Aug 2026 with 67.001%** of participating stake, but activation still needs client implementation. — Blockdaemon update 2 Sep 2026, https://www.blockdaemon.com/blog/what-is-simd-0550-and-why-does-it-matter-for-institutional-staking · https://github.com/solana-foundation/solana-improvement-documents/pull/550 **[RC: Validated · Researchy check 2026-10-09]**. The SGP text says "No separate funding request is proposed."

**ORF alignment (4 / 25)**: Q1 0 (foundation drawdown) · Q2 1 · Q3 1 (convertible grants are the only counter-value or return-of-capital mechanism among the ten, and they function as a capital-recovery instrument, not a sold benefit) · Q4 1 (stake-weighted on-chain governance exists, but it's used for monetary policy, not OSS funding) · Q5 1 (unknown).
- **Families:** D ◐ (foundation reserve). A, B, C ❌. E unknown.
- **Verdict:** the governance machinery exists but is pointed at issuance, not replenishment.

### 3.6 TRON (TRX): very large fee base, none of it routed to maintenance

**How OSS is funded**
- **Protocol level:** TRX is burned when users lack staked Bandwidth/Energy. **Two fee figures, different methods (shown side by side) [RC: Partial · Researchy check 2026-10-09]:** (a) **TRON DAO's State of TRON Q3 2026** (published 6 Oct 2026) reports **$701.4M in "network fees"** ($234.6M Jul / $231.3M Aug / $235.5M Sep), apparently including the value of staked-resource usage; the report is internally inconsistent ($7.56M vs $7.62M/day). — https://trondao.org/research/state-of-tron-q3-2026-tron-passes-the-30-trillion-mark (self-reported, not audited). (b) **DefiLlama chain fees, Q3 2026 ≈ $77.8M**, roughly matching 234.5M TRX burned × ~$0.33. — https://api.llama.fi/summary/fees/tron?dataType=dailyFees. The TRON DAO figure is about 9× the burn-based figure. Supply: 360.2M TRX generated, 234.5M burned, net issuance 125.8M TRX (TRON DAO).
- **TRON Builders League (TBL):** rolling incubator, "Up to $5,000,000 in Funding", staged by milestones. — https://trondao.org/tron-builders-league **[RC: Validated, raw HTML · Researchy check 2026-10-09]**
- **TRON DAO Reserve:** backs USDD. It's not an OSS fund.
- Core (java-tron) maintenance funding source and amount: **unknown**.

**ORF alignment (2 / 25)**: Q1 0 · Q2 1 · Q3 0 · Q4 1 (SR proposals such as Proposal 107, approved 25/27 SRs, show working parameter governance; **[RC: Validated]**) · Q5 0 (unknown).
- **Families:** D ◐. A ❌, even though the chain has one of the largest fee bases in crypto. B, C ❌. E unknown.
- **Verdict:** the clearest example of the ORF depletion diagnosis: very large value generation with no return path.

### 3.7 Zcash (ZEC): the only protocol-level dev fund, but funded by issuance

**How OSS is funded**
- **Protocol level (consensus-enforced):** under NU6 (ZIP 1015) and its extension (ZIP 1016 / ZIP 271), **8% of the block subsidy goes to Zcash Community Grants (ZCG)** (FS_FPF_ZCG_H3) and **12% to a Coinholder-Controlled Fund** (FS_CCF_H3). Both streams end at the **3rd halving**. In ZIP 214 terms the pre-NU7 Mainnet heights are 3,146,400 → 4,406,400. Under ZIP 214 Rev 3 (NU7), the end height becomes A + 3·(4,406,400 − A), where A is the NU7 activation height; the wall-clock date is the same. — https://zips.z.cash/zip-0214 · https://github.com/zcash/zips/blob/main/zips/zip-1016.md · https://zips.z.cash/zip-0271 **[RC: Partial; the end-height wording was corrected · Researchy check 2026-10-09]**
- **ZIP 214 Revision 3** (Draft, last updated 24 Sep 2026) keeps those streams to the post-NU7 third-halving height under 25-second blocks. — https://zips.z.cash/zip-0214 **[RC: Validated · Researchy check 2026-10-09]**
- **Coinholder-Controlled Fund balance (corrected) [RC: Needs update → updated · Researchy check 2026-10-09]:** (a) the **in-protocol lockbox** now holds about **68,463–68,471 ZEC**, which is only the accrual since NU6.1 (height 3,146,400), ≈ **$83.3M** at $1,216 (*derived*). (b) ZIP 271 had already disbursed the earlier **78,750 ZEC** lockbox contents to a 2-of-3 Key-Holder multisig, so the **full Coinholder-Controlled Fund** (lockbox + multisig) is ≈ **146,675 ZEC ≈ $178M**, per OpenZcash (third-party). **Both are Unverified** (third-party chain readers, no node RPC). The earlier "63,962 ZEC ≈ $95M" (Coinotag, 18 Sep 2026) is stale and counted only the lockbox. — https://zecstats.org/shielded · https://zecview.com/tools/shielded-dashboard/ · https://openzcash.org/lockbox · https://github.com/zcash/zips/blob/main/zips/zip-0271.md
- **Governance controls:** coinholder votes, with a ZIP 1016 quorum of "a minimum of 420,000 ZEC (2% of the total eventual supply)" **[RC: Validated · https://github.com/zcash/zips/blob/main/zips/zip-1016.md]**. Key-Holder Organizations (Zcash Foundation, Shielded Labs, ECC/now contested) hold a **veto**. On **16 Mar 2026** (10:36 PT) ZF and Shielded Labs stated "we intend to veto" the coinholder-approved **$2,673,974** Q4 2025 retroactive grant to Bootstrap/ECC after the ECC team left to form **ZODL**. Researchy found no separate "veto executed" post, so this is an **announced intent**. — https://forum.zcashcommunity.com/t/statement-on-the-bootstrap-ecc-q4-2025-retroactive-grant/54988 **[RC: Validated]**. Figures in that thread's comments (~$10M ECC treasury retained, $8M settlement) are one commenter's claims (17 Mar 2026): **Unverified [RC: Unverified]**.
- **2026 debate:** in Sept 2026, Dragonfly's Haseeb Qureshi argued publicly that this should be the final dev fund, and others argued for or against continuing it (secondary report above; the X posts exist). **No on-chain proposal had been submitted**; that holds as of 9 Oct 2026 at Medium confidence. **NU7: testnet 6 Oct 2026, mainnet target 5 Nov 2026.** — https://forum.zcashcommunity.com/t/nu7-timeline/57655 **[RC: Validated · Researchy check 2026-10-09]**

**ORF alignment (raw 11, reported Phase 1)**
- Q1 = 2: a recurring, rules-based stream exists, which is unique among the ten. It's **issuance**, so ORF excludes it from non-inflationary coverage, and no replenishment ratio is published.
- Q2 = 3: the stream is enforced by consensus on the canonical chain (a fork would have to give up the canonical chain to avoid it), which is a strong anchor. It's still a native-token anchor, not an SLA or registry.
- Q3 = 0: it's a mandatory subsidy carve-out (a "tax" in rubric terms), not a sold benefit.
- Q4 = 4: **the strongest mandate of the ten.** Streams are time-bounded by ZIP and end at the halving (effectively a sunset clause). Recipients carry ZIP 1014/1015 transparency duties. There's a coinholder vote and a published veto process. It lacks independent cost-to-collect audit and a dOSPO-style policy/execution split.
- Q5 = 2: the reserve is native-token-denominated and price-correlated.
- **Families:** A ◐ (structural but issuance, which ORF excludes). D ✅ (ZF and Shielded Labs donations). B, C ❌. E unknown.
- **Verdict:** the closest match to ORF's mandate and governance discipline among the ten, but on the wrong money (inflation, not captured value).

### 3.8 Hyperliquid (HYPE): heavy fee capture, routed to buybacks, closed-source L1

**How OSS is funded**
- **Protocol level:** official docs say fees go "entirely … to the community (HLP, the assistance fund, and deployers)". Spot and HIP-3 deployers can keep up to 50%. The Assistance Fund "converts trading fees to HYPE in a fully automated manner … HYPE in the assistance fund is **burned**." — https://hyperliquid.gitbook.io/hyperliquid-docs/trading/fees **[RC: Validated]**. The share of fees going to the AF is **not published officially**: a community wiki says ~93% and press says ~99%. — https://hyperliquid-co.gitbook.io/wiki/architecture/hypercore/vault **[RC: Unverified]**. **Fee scale (new):** DefiLlama fees Q3 2026 **$224.2M** (30d $90.84M; 1y $928.4M; all-time $1.648B); revenue Q3 2026 $173.9M (all-time $1.334B). Third-party methodology. — https://api.llama.fi/summary/fees/hyperliquid?dataType=dailyFees **[RC: Validated · Researchy check 2026-10-09]**. **AF stock:** 47,929,862.66 HYPE spot (≈ $4.10B at $85.55, *derived*) per the Hyperliquid info API (spotClearinghouseState, 0xfefe…fefe). Researchy reads the API's entryNtl of $1,358.9M as cumulative cost basis; that reading is theirs, so treat it as *derived*. **[RC: Validated · Researchy check 2026-10-09]**
- **USDC reserve yield to buybacks (AQAv2):** **14,580,774.69 USDC** sent from the system interest address 0x5000…0000 to the AF (0xfefe…fefe) on **3 Oct 2026 17:00 PT**, confirmed on-chain (Hyperliquid info API, userNonFundingLedgerUpdates). Docs say deployers share ~90% of cost-adjusted reserve yield. — https://api.hyperliquid.xyz/info · https://hyperliquid.gitbook.io/hyperliquid-docs/hypercore/aligned-quote-assets **[RC: Validated on-chain; was Unverified · Researchy check 2026-10-09]**
- **Hyper Foundation grants:** ~**$10M** for USDH-sunset migration and wind-down (deadline end of July 2026). Several outlets report it consistently (crypto.news; CryptoBriefing 28 Jun 2026; Bitget 29 Jun 2026), but no Hyper Foundation primary post was opened. — https://crypto.news/hyper-foundation-allocates-10m-in-grants-to-support-usdh-migration/ **[RC: Partial · Researchy check 2026-10-09]**. This is a one-off remediation grant, not maintenance funding.
- **Open-source status:** the official wiki states the L1 source isn't public. The node repo ships **signed binaries**. Hyperliquid says it will open-source after HyperCore reaches feature completion. — https://github.com/hyperliquid-dex/node · OpenSourceForU, 2 Jul 2026, https://www.opensourceforu.com/2026/07/hyperliquids-validator-model-faces-open-source-scrutiny/ **[RC: Validated · Researchy check 2026-10-09]**

**ORF alignment (5 / 25, partly out of frame)**: Q1 0 (nothing flows to maintenance) · Q2 3 (fees attach to canonical liquidity, a strong fork-resilient anchor, but the core is closed so "fork" isn't even possible yet) · Q3 1 (trading fees *are* sold for a service, but none of the proceeds go to OSS) · Q4 1 (validator votes, e.g. the 2025 USDH issuer vote, but no chartered collection for maintenance) · Q5 0 (unknown).
- **Families:** A ◐ (the structural-revenue machinery exists, but it's pointed at token buybacks). D ◐ (ad hoc foundation grants). B, C ❌. E unknown.
- **Verdict:** the collection layer ORF wants already exists, but it routes to token holders, not maintainers, and the core isn't open source.

### 3.9 Dogecoin (DOGE): fixed CoreFund, no recurring source

**How OSS is funded**
- **Protocol level:** none. Block rewards go to miners.
- **Dogecoin Foundation CoreFund** (31 Dec 2022): **5,000,000 DOGE** in a 3-of-5 multisig. **500,000 DOGE** is distributed per qualifying Core release (≥25 substantive PRs) to credited contributors. — https://foundation.dogecoin.com/announcements/2022-12-31-corefund/ (opened) **[RC: Validated · Researchy check 2026-10-09]**. Current balance: **unknown**.
- **House of Doge / CleanCore "Official Dogecoin Treasury"**: a **$175,000,420** private placement, closed per GlobeNewswire on 5 Sep 2025 (https://www.globenewswire.com/news-release/2025/09/05/3145445/0/en/CleanCore-Solutions-Announces-Closing-of-175-000-420-Private-Placement.html). Holdings of **710M DOGE** per a Nasdaq-hosted CleanCore release (7 Oct 2025; https://www.nasdaq.com/press-release/cleancore-solutions-provides-dogecoin-treasury-update-current-holdings-include-710m). CleanCore trades on **NYSE American: ZONE**. **[RC: Validated · Researchy check 2026-10-09]**. It's a corporate treasury vehicle, **not** OSS funding.

**ORF alignment (1 / 25)**: Q1 0 · Q2 0 · Q3 0 · Q4 1 (the CoreFund's disbursement rules are published and rules-based, a small but real mandate artifact) · Q5 0.
- **Families:** D ◐ (a one-off Foundation allocation). A, B, C, E ❌.
- **Verdict:** a fixed one-time fund paid out per release. Pure depletion.

### 3.10 Monero (XMR): crowdfunding by principle

**How OSS is funded**
- **Protocol level:** none, by community choice. The CCS page says the project "is unable or unwilling to partake in" ICOs, dev fees, or decentralized treasuries. — https://ccs.getmonero.org/what-is-ccs/ **[RC: Validated · Researchy check 2026-10-09]**
- **CCS:** milestone-based proposals with Core Team escrow. Unspent or failed funds go to the **Monero General Fund**, and work must be permissively licensed (**[RC: Validated]**). **2026 examples (updated) [RC: Needs update → updated · https://ccs.getmonero.org/work-in-progress/ · 2026-10-09]:** **jeffro256 2026Q2** full-time, 120 XMR, now **fully funded** (in Work in Progress, 2 of 3 milestones); **selsta** 3-month, 79 XMR (posted 1 Sep 2026), now **fully funded** (1 of 3 milestones); **vtnerd** current entry "Full-time 2026 Q3", 97.06 XMR. The earlier "80 received", "27 received as of 7 Oct", and "vtnerd 2026 Q2 59.94 XMR" figures are stale or not re-located. Aggregate annual CCS volume: **unknown**.
- Also present: MAGIC Monero Fund (amount **unknown**).

**ORF alignment (4 / 25)**: Q1 1 (recurring but unmeasured voluntary inflows) · Q2 0 · Q3 0 · Q4 2 (public proposals, milestone escrow, and a published fallback rule, but no sunset or charter) · Q5 1.
- **Families:** D ✅. A, B, C, E ❌.
- **Verdict:** principled and transparent voluntary funding. Family D only, so it's structurally one-way.

---

## 4. Cross-cutting findings

1. **Value capture is common, and redirecting it to maintenance is rare.** TRON ($701.4M Q3-2026 "network fees" self-reported vs ≈$77.8M burn-based per DefiLlama; **Partial**), Hyperliquid (DefiLlama Q3-2026 fees $224.2M, routed to HLP/AF buyback-burn, with 14.58M USDC of reserve yield added on 3 Oct 2026), BNB (BEP-95 plus Auto-Burn), and XRP (fee burn) all have a working Stage 1→2 *collection* path, but it ends in **burns, buybacks, or validator income**. In ORF terms, the hardest part of the loop to build (structural collection) already exists. What's missing is a **governed redirection** of a slice (τ) to Stage 3. That is a governance-legitimacy problem (`START_HERE` principle 1), not a technical one.
2. **The only protocol-level dev fund in the top 10 (Zcash) is funded by issuance**, which ORF explicitly excludes from non-inflationary sustainability. Its Coinholder-Controlled Fund is now ≈146.7k ZEC (lockbox ~68.5k + multisig 78.75k; ≈$178M; Unverified, third-party). It is also under live political pressure: the March 2026 key-holders' announced intent to veto and the September 2026 sunset debate. It shows both the strength of chartered, time-bounded mandates (Q4 = 4) and the risk ORF's v1.1 text flags: a large native-token balance invites politicization.
3. **Ethereum is moving toward an endowment model, not a replenishment model.** The EF's published 15%→5% opex glide path, 2.5-year fiat buffer, and 70k-ETH staking match ORF's Family E logic. Under the repo's correlation classes, though, staking yield is Class 2 (native-token-correlated), so it doesn't diversify away from ETH price risk (Gate 4). EF ESP awards also fell from ~$9.86M in Q1 to ~$5.50M in Q2 2026.

Other notes:
- **Protocol Guild's 2025 dollar totals are now primary-sourced.** The repo errata says they were "not recoverable from a rendered primary page". The 29 Jan 2026 annual report states $7,231,668 / 6,202 unique donors and $12.4M distributed. **Candidate claim upgrade** for `ORF_ERRATA.md` and the v1.1 manuscript, pending author decision. Membership is now **190 (5 Aug 2026)**, which supersedes 196 (22 May 2026).
- **Bitcoin's Brink plans "enterprise testing software" (2026).** It's the only Family-B-shaped seed among the ten, and it's D0.
- **Solana's convertible grants** are the only return-of-capital instrument found among the ten foundations.

## 5. Claims still open after the Researchy reconciliation (do not publish as High)

| Claim | Status after reconciliation (Researchy check 2026-10-09) |
|---|---|
| Zcash Coinholder-Controlled Fund: lockbox ~68.5k ZEC (≈$83M) + multisig 78.75k ZEC (total ≈146.7k ZEC ≈ $178M) | **Unverified** (third-party chain readers; no node RPC). Replaces the stale 63,962 ZEC / $95M |
| ZODL/Bootstrap "~$10M ECC treasury" and "$8M settlement" | **Unverified** (forum commenter, 17 Mar 2026) |
| Zcash KHO veto of the $2,673,974 grant: executed? | Intent announced 16 Mar 2026 (**Validated**). Execution not separately confirmed |
| Hyperliquid "~93% of fees to AF" (press: ~99%) | **Unverified**. Official docs publish no HLP/AF split |
| Hyper Foundation ~$10M USDH grants | **Partial** (consistent multi-outlet reporting; no primary post) |
| BNB MVB terms ($150K SAFE for 5% + $350K uncapped SAFE) | **Partial** in Researchy's status column. Terms are on the primary page (20 Aug 2025) and the live YZi page; the earlier text was incomplete |
| BNB Grants "up to $200K" | **Partial** (2024 blog only; grants page 404) |
| BNB $1B Builder Fund *disbursed*; BNB core-client funding | **Unknown** (not published) |
| TRON Q3-2026 fees: $701.4M (TRON DAO "network fees") vs ≈$77.8M (DefiLlama, burn-based) | **Partial**. Both shown; methodology-dependent; self-reported figure not reproducible from burn data |
| Solana Foundation delegation ~20.83M SOL (Jun 2026) | **Partial** (secondary, Phase) |
| Solana Foundation treasury size; annual grant totals; Anza/Firedancer funding | **Unknown / not published** (Validated as unknown) |
| EF 2025/2026 treasury total | **Unknown** (latest primary: $970.2M, 31 Oct 2024; secondary ~$209M ETH-wallet estimate, Jun 2026, not used) |
| Spiral grant total | **Unverified** (not published) |
| Protocol Guild "commitments above $80 million" | **Unverified** (not in the 2025 annual report) |
| Monero vtnerd 2026 Q2 "59.94 XMR" | Not re-located (current entry: 2026 Q3, 97.06 XMR). Treat Q2 figure as **stale** |
| Monero annual CCS volume; MAGIC fund | **Unknown** |
| Ripple "$550M since 2017"; TRON $701.4M | Primary but **self-reported**, unaudited (Gate 2) |

Upgraded to **Validated** by Researchy (no longer open): Hyperliquid 14,580,774.69 USDC AQAv2 payment (on-chain, 3 Oct 2026 17:00 PT) · TRON Builders League "Up to $5,000,000" · CleanCore $175,000,420 PIPE (GlobeNewswire 5 Sep 2025) and 710M DOGE · HRF 2026 rounds · ZIP 1016 420,000 ZEC quorum · Protocol Guild $7,231,668 / 6,202 unique donors / $12.4M / 190 members.

**Repo-errata note (not applied; repo not edited):** Researchy agrees that the Protocol Guild correction belongs in a **new `ORF_ERRATA.md` entry that supersedes the current PG paragraph**, because that file is the controlling citation layer. A proposed sentence is in `researchy-chain-check.md` §2. Archive a rendered capture of the PG report (it's a JS SPA) before marking it High.

**Update 9 Oct 2026:** Christian Taylor approved the Protocol Guild errata entry. It is applied in `whitepapers/ORF_ERRATA.md` (supersedes the earlier PG paragraph) with rendered captures archived in `data/pg-20260129-annual-report-2025-2026-10-09.{pdf,html}` and `data/pg-20260826-q3-quarterly-audit-2026-10-09.{pdf,html}`. Confidence: High. ">$80M commitments" stays Unverified.

## 6. Did any score, phase, or placement change after reconciliation?

| Chain | Score / phase change? | Why |
|---|---|---|
| Bitcoin | **No** (5, Phase 1) | OpenSats cumulative corrected ($29.9M / 352 live counter). 2025 flows unchanged; Q1 rationale holds |
| Ethereum | **No** (9, Phase 1) | All EF and PG figures Validated. EF 2025/26 total still unknown |
| BNB | **No** (1) | MVB terms fuller (more equity); still not a bundle or replenishment |
| XRP | **No** (2) | Validated as-is |
| Solana | **No** (4) | Treasury confirmed unpublished, so Q5 = 1 stays (no evidence either way) |
| TRON | **No** (2) | Fee magnitude now shown two ways; A is still ❌ (nothing routed to maintenance) |
| Zcash | **No** (raw 11, Phase 1 policy cap) | A larger fund (≈146.7k ZEC incl. multisig) doesn't change Q5 = 2, because it's still a native-token, price-correlated reserve funded by issuance |
| Hyperliquid | **No** (5, partly out of frame) | Fees and AF stock are confirmed large, but the AF's HYPE is designated for burn, not maintenance runway. Q1 and Q5 stay 0 |
| Dogecoin | **No** (1) | The CleanCore figures are corporate treasury, not OSS |
| Monero | **No** (4) | CCS proposals fully funded; no change to the voluntary-only structure |

*Stage 0. No Hard Gate passed. No expert quotes are reproduced as endorsements. The Qureshi, Huang, and Samani positions are paraphrased from the cited news reports.*
