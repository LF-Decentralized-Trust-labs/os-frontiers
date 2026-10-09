# Closing the Loop: Governance, Maintenance Deployment, and Replenishment for Open Infrastructure

> **OSFL Release-1 Research Draft** · Open Source Frontiers Lab (LF Decentralized Trust labs · `os-frontiers`)  
> **Series:** dOSPO (governance) · OMF (maintenance deployment) · ORF (replenishment) — ORF dated 18 Aug 2026 completes the trilogy; each pillar usable alone.  
> **Author:** Christian Taylor · Open Source Frontiers Lab synthesis pack  
> **Affiliation options:** Open Source Cowboy Consulting; LF Decentralized Trust Labs (Stage 0 Research Candidate)  
> **Date:** 2026-09-24 America/Los_Angeles  
> **Status:** **Stage 0** research candidate. No Hard Gate marked passed. Where `ORF_ERRATA.md` differs from `orf-v1.0.pdf`, **errata controls**.  
> **Evidence pack:** `claims/orf-claims-validated.md` (141; SUPPORTS 99 · PARTIAL 35 · ERRATA 5 · CONFLICTS 2; Researchy delta: 0 flips); `use-cases/web2-web3-prototypes.md`; `use-cases/web2-web3-prototypes-expansion.md` (N1–N12); `use-cases/researchy-validation.md`; `claims/implementation-validation.md`; `synthesis/gaps.md`  
> **Integrity rule:** No fabricated citations, expert quotes, or unaudited cash totals.

---

## Abstract

Open infrastructure creates outsized economic value, yet maintenance funding still travels mostly one way: grants, sponsorship, token treasuries, and voluntary pledges that deplete under stress. The Open Source Frontiers Lab (OSFL) series proposes a closed institutional loop — **dOSPO** (who decides), **OMF** (how money goes out), and **ORF** (how money comes back) — without monetizing open-source code itself.

This release-1 draft synthesizes the Stage 0 ORF architecture for university and foundation readers. It (1) states the problem and Web3 amplifiers, (2) summarizes the three-pillar model and Minimum Viable ORF, (3) maps live Web2/Web3 prototypes to gaps (core catalog plus twelve live-web expansion rows), (4) reports a 141-claim validation pass under errata discipline, (5) outlines an implementation path for adopters, and (6) lists risks and an explicit research agenda. **No ecosystem reviewed here clears all eight Hard Gates or demonstrates PCR ≥ 1.0 under ORF rules.** Running ORF (MV-ORF) is deliberately separable from claiming self-sustainability.

---

## 1. Problem & related work

### 1.1 One-way funding and depletion

Across Web2 sponsorship and Web3 treasuries, capital typically arrives as issuance, reserves, grants, donations, or corporate sponsorship — mechanisms that can fund deployment for a time without replenishing the capacity they consume (`C-006`: PARTIAL as census claim; pattern diagnosis supported in-repo). OMF without ORF is terminal: even a perfect deployment architecture depletes without replenishment behind it (`C-019`).

### 1.2 Documented value vs maintenance dependence

- Synopsys OSSRA 2024: open-source components in **96%** of analyzed commercial codebases — cite carefully; errata notes conflicting lines on related Synopsys pages (`C-013`, PARTIAL).  
- Hoffmann, Nagle & Zhou (HBS WP 24-038): supply-side replacement ≈ **$4.15B**; demand-side ≈ **$8.8T** (`C-014`, SUPPORTS; spelling **Hoffmann** per errata `C-108`).  
- The OMF paper’s “$4.15 trillion” figure is a documented merge error and is excluded from this draft (`C-109`).

### 1.3 Web3 amplifiers

Token-denominated treasuries couple maintenance capacity to market cycles (`C-015`, PARTIAL). Monetary expansion can **feel** like revenue while representing dilution rather than captured external value (`C-016`). Structural fees alone do not solve sustainability under correlation, buyer concentration, and legitimacy constraints (`C-017`, PARTIAL).

### 1.4 Series diagnosis

Governance without deployment is inert; deployment without replenishment is terminal. ORF is the third installment, meant to be read with dOSPO and OMF, and usable independently (`C-001`–`C-003`).

**Prior art** in-repo (`sources/PRIOR_ART_AND_COMPETITIVE_ANALYSIS.md`, precedents/, tools/) situates Optimism, ENS, POSM, LF/CNCF, Protocol Guild, Tidelift-class assurance, and rails (Drips, Superfluid) as **partial** prototypes — not complete closed loops under ORF naming (`C-011`).

---

## 2. Institutional model (pillars)

| Pillar | Question | Primary artifacts |
|--------|----------|-------------------|
| **dOSPO** | Who decides? | `dospo/` charter & non-powers; dOSPO whitepaper |
| **OMF** | How money goes out? | `omf/` program portfolio; OMF whitepaper |
| **ORF** | How money comes back? | `orf/INSTRUMENT_CATALOG.md`, `GOVERNANCE_RULES.md`, ORF PDF + **ERRATA** |

### 2.1 Closed-loop stages

Value Generation → ORF Collection → Governed Treasury → Routing & Allocation → OMF Deployment → Sustained Infrastructure (`C-047`). **Architectural rule:** distribution must not be mistaken for replenishment; counting routing/allocation as revenue is counting a conveyor belt as a factory (`C-048`).

### 2.2 What ORF is / is not

ORF is a **portfolio design problem** across five revenue families, not a single mechanism (`C-007`). It strictly separates revenue generation from routing rails and allocation engines (`C-008`). It does **not** monetize open-source code; value attaches to fork-resilient anchors (maintainer capacity, certification trust, canonical network activity, enterprise response, governance legitimacy) (`C-010`, `C-046`).

### 2.3 Minimum Viable ORF vs self-sustaining

**MV-ORF** (all five): (1) verified cost floor, (2) classified inflow inventory, (3) ≥1 earned instrument with real receipts, (4) net-contribution reporting, (5) ratio/gate review cadence (`C-040`). Meeting MV-ORF means the ecosystem is **running ORF even if PCR ≪ 1.0** (`C-041`).

**Self-sustaining** requires **all eight Hard Gates simultaneously** — no compensatory scoring (`C-091`):

| Gate | Requirement |
|------|-------------|
| 1 Measurement | Empirically verified annual maintenance cost floor |
| 2 Cash Evidence | Audited cash/stablecoin receipts (not forecasts/pledges) |
| 3 Net Coverage | PCR ≥ 1.0 |
| 4 Multi-Class Diversity | ≥2 materially uncorrelated classes via 3-step independence |
| 5 Concentration | RCR ≤ 0.25 (counterparty, not family-share) |
| 6 Stress Runway | SCR ≥ 1.0 with ≥24 months liquid reserve under compound stress |
| 7 Liability Coverage | SLAs/retainers/refunds backed by capacity + wind-down |
| 8 Independent Audit | Annual independent financial & operational audits published |

**Release-1 fact:** no ORF gate is marked passed (`C-101`).

Core ratios (definitions SUPPORTS): SPCR, PCR, SCR, RCR (`C-075`–`C-079`); plus reporting obligations including MCR in the quarterly audit pack (`C-099`).

---

## 3. Comparative use-case map

Method: map environments to pillar fit and gaps (`use-cases/web2-web3-prototypes.md`). Deep dossiers A–E carry dated source packets. Live-web hygiene and **12 new prototype rows** are in `use-cases/researchy-validation.md` and `use-cases/web2-web3-prototypes-expansion.md` (2026-09-24 PT). No new claim IDs minted; USe Me re-score reported **0 status flips** on the 141 (`claims/researchy-claim-deltas.md`).

### 3.1 Core catalog (pre-expansion)

| Environment | Pillars (prototype) | Gap vs closed loop | Confidence notes |
|-------------|---------------------|--------------------|------------------|
| Optimism Superchain | ORF A.2 collection; OMF Retro (deploy ≠ replenish) | Concentration; standard-chain vs OP Mainnet 100%; buyback is timed pilot | Medium under Gate 2; cite vote (`C-020`–`C-021`, `C-105`–`C-106`) |
| ENS | ORF A.3 registrar + E.1 endowment | Two closes — do not stack KPK & EP 6.46; endowment ≠ full opex | Sourced closes separately (`C-107`) |
| Cardano POSM | OMF retainers strong; ORF weak / mixed A.4 | Issuance≠replenishment; budget figures often Unverified | High OMF transfer; not ORF proof |
| LF / CNCF | ORF Family C live (Web2) | No published eight-gate claim; seconded labor common | Qualitative SUPPORTS for C.1–C.3 class |
| Protocol Guild | ORF Family D mechanism | Voluntary money; weak base for guaranteed liabilities. ">$80M commitments" stays Unverified | **High** per `ORF_ERRATA.md` (PG errata, approved 9 Oct 2026): 2025 donations $7,231,668 valued at time of donation, 6,202 unique donors (Annual Report 2025, 29 Jan 2026); membership 190 as of 5 Aug 2026, net decrease of 6 from 196 (Q3 2026 audit, 26 Aug 2026). Captures in `chains/data/` (supersedes `C-110` downgrade) |
| Tidelift / Sonar | ORF Family B assurance | Wording: **definitive agreement**, not acquired | `C-112` |
| GitHub Sponsors / Open Collective | Voluntary / fiscal host | Concentration; not Neutral Entity + SCT stack | Qualitative |
| Drips / Superfluid / Deep Funding | Rails / engines | **Not revenue** | RAIL-ONLY / RESEARCH |
| Sovereign Tech Fund | Public maintenance investment | Not earned portfolio; ratios unmapped | Fieldwork gap |

### 3.2 Expansion rows (N1–N12) — Researchy live-web

Stage 0 prototypes only. Site counters and vendor marketing figures stay **publisher claims**, not Gate 2 cash. Full source packets: `use-cases/web2-web3-prototypes-expansion.md`.

**Narrative priorities (top three):**

1. **Geomys (N3)** — professional maintainer employment / retainer firm (OMF strong; Family B-adjacent). Clearest “maintainer-of-last-resort as a business” peer to POSM without claiming Neutral Entity governance.  
2. **Open Source Endowment (N5)** — Web2 Family E spend-rate 501(c)(3); complements ENS endowment examples without stacking Unverified Web3 epoch payouts. Cite fund size/spend-rate as publisher figures only.  
3. **Open Source Pledge + thanks.dev (N1–N2)** — corporate ≥$2k/FTE-dev/year social norm (Family D) plus dependency-graph **routing** (thanks.dev). Pledge does not custody funds; thanks.dev is not independent revenue.

| ID | Environment | Pillars (prototype) | Gap vs closed loop |
|----|-------------|---------------------|--------------------|
| N1 | Open Source Pledge | OMF cash; ORF Family D norm | Voluntary/revocable; no SCT / eight-gate PCR |
| N2 | thanks.dev | Routing (S.1-adjacent Web2) | Routes budgeted cash; not replenishment |
| N3 | Geomys | OMF retainers; B-adjacent | Vendor firm ≠ Neutral Entity; Go-portfolio scope |
| N4 | HeroDevs NES | ORF Family B EOL continuity | Vendor assurance; upstream retainers not automatic |
| N5 | Open Source Endowment | ORF Family E; OMF microgrants | Early corpus; not paired with Family A fees |
| N6 | NLnet / NGI Zero → Restack | OMF grants | One-way public/philanthropic capital |
| N7 | Prototype Fund (DE) | OMF prototype stipends | Public sprint funding ≠ replenishment |
| N8 | CURIOSS + UC OSPO Network | dOSPO campus; OMF weak ORF | Grant/institutional budgets; thin tech-transfer→retainer path |
| N9 | Rust Foundation | ORF Family C + Maintainers Fund | Membership ≠ measured cost-floor coverage |
| N10 | Alpha-Omega (OpenSSF) | OMF security staffing; C-adjacent underwriting | Grant-era / member underwriting, not five-family earned stack |
| N11 | Polar.sh | OMF maintainer MoR / subscriptions | Platform fees ≠ ecosystem treasury |
| N12 | Digital Public Goods Alliance | dOSPO-like registry; OMF advocacy | Coordination > operating treasury; mobilization targets ≠ receipts |

**Themes still thin** (expansion hunt): restaking/yield public goods beyond Octant; attestation/naming revenue beyond ENS; Asia public OSS funds with primary closed-loop disclosures; university tech-transfer → maintainer endowments; L2 sequencer-fee→maintenance loops outside Optimism’s clarity.

**Implementation scorecard** (`claims/implementation-validation.md`), unchanged by Researchy’s pass: no turnkey ORF production system in-repo; strongest collection precedents = Optimism / ENS / LF-CNCF / Tidelift-class (**HeroDevs NES** now sits beside Tidelift as a Family B peer with a different product shape); strongest deployment precedents = POSM / Guild streams / Retro (**Geomys** adds employment-retainer texture); SLA vault contracts **absent** (removed 2026-08-20). Pledge/thanks.dev strengthen the Family D + routing story without converting rails into revenue.

### 3.3 The ten largest chains against ORF and the POSM cycle

> **Stage 0.** No Hard Gate is marked passed for any chain, for Cardano, or for ORF itself. Snapshot: CoinGecko, 9 Oct 2026 03:51 PT (CoinMarketCap cross-check swaps Hyperliquid and Zcash). Every figure below is carried from `chains/top10-chains-orf-alignment.md` and `chains/posm-cycle-chain-map.md` after Researchy's 58-row live check (`chains/researchy-chain-check.md`, 9 Oct 2026). Statuses travel with the figures; nothing here upgrades them.

**Scope.** The ten largest layer-1 and layer-2 networks by native-token market cap: Bitcoin, Ethereum, BNB Chain, XRP Ledger, Solana, TRON, Zcash, Hyperliquid, Dogecoin, Monero. No layer-2 enters the top ten (the largest, Mantle, is #56). Cardano (#11 when WBT is excluded; #12 under the top-100 gas-token scope rule, which counts WBT, CRO and OKB; top-100 CoinGecko snapshot fetched 9 Oct 2026 05:19 PT, data as of 05:17:50 PT, see `chains/top100-method.md`; the top-10 table uses the separate 03:51 PT snapshot) is included as the reference implementation of Intersect's Paid Open Source Model (POSM), because the POSM cycle diagram (Intersect whitepaper, 20 Dec 2024, p.11) is the frame this section uses alongside the ORF closed loop.

**Two frames, one question.** POSM's cycle runs P1 Funding In → P2 Steward Governance & Programs (Code for Us, Maintainer Retainer) → P3 Outputs → P4 Commercialization Channels → P5 Commercial Adoption → P6 Return to Treasury. Read against the three pillars, P1–P3 is the dOSPO and OMF half (who decides, how money goes out), and P6 is the ORF half (how money comes back). The question for each chain is therefore the same in both frames: does value generated by use of the network return, measured and governed, to the people maintaining it?

**Result.** None of the ten does. All ten score Phase 1 (reserve-funded, one-way) on the repo's 5-Question Posture Assessment, none meets Minimum Viable ORF, and none closes the POSM loop at P6 for open source. Cardano does not close it either: its P6 edge exists, but by Researchy's derivation from on-chain epoch totals (not an official figure) about 0.2% of treasury inflow is fee-derived and about 99.8% is reserve issuance, which ORF excludes from replenishment.

| Chain | ORF score /25 | POSM position now | Families present for OSS | Direction of travel (dated) |
|---|---|---|---|---|
| Bitcoin | 5 | P3: donor stewards (OpenSats, Brink, HRF) | D | Brink's 2026 "enterprise testing software" plan is a faint Family B seed (D0); otherwise stationary |
| Ethereum | 9 | P3, with a capital-side return | D; E partial (staking yield is native-token correlated) | Toward an endowment: EF opex glide 15% → 5% (4 Jun 2025) and 70k ETH staked (24 Feb 2026). Capital return, not adoption return |
| BNB Chain | 1 | P5, value leaks (burns, validators) | D partial (corporate/VC) | Deeper into venture-style P5: $1B Builder Fund commitment (8 Oct 2025), MVB terms are SAFE equity (Partial) |
| XRP Ledger | 2 | P5, value leaks (fee burn) | D partial (corporate sponsor) | Allocation decentralizing (26 Feb 2026: XRPL Commons, XAO DAO); collection unchanged |
| Solana | 4 | P5, value leaks (validators, burn) | D partial (foundation reserve) | Governance pointed at issuance (SGP-0002, 28 Aug 2026). Convertible grants are the only return-of-capital instrument among the ten; amounts unknown, treasury unpublished |
| TRON | 2 | P5, value leaks (burn) | D partial | Stationary. Q3 2026 fees are $701.4M self-reported vs ≈$77.8M on DefiLlama (Partial) |
| Zcash | 11 raw, capped to Phase 1 | P2: protocol stream to governed grants | A partial but issuance (excluded); D | Contested: streams kept to the third halving (ZIP 214 r3, Draft), key-holders' announced intent to veto a grant (16 Mar 2026), Sept 2026 "final dev fund" debate with no on-chain proposal |
| Hyperliquid | 5, partly out of frame (closed L1) | P5, fee capture routed to buyback/burn | A partial (pointed at buybacks); D partial | More buyback inputs: 14,580,774.69 USDC to the Assistance Fund on 3 Oct 2026 (Validated on-chain). Open-sourcing promised, undated |
| Dogecoin | 1 | P2: fixed CoreFund paid per release | D partial | No change found since 2022 |
| Monero | 4 | P2: CCS milestone escrow | D | Stationary by design |
| *Cardano (ref.)* | *not scored* | *P1–P5 live; P6 ≈99.8% issuance (derived)* | *A thin fee share; deployment strong* | *Stalled: ₳5.885M enacted 12 Aug 2025 (on-chain); the ₳4.601M 2026–27 request was never submitted on-chain as of epoch 660* |

**Three findings for the release-1 argument.**

1. **For most large chains the collection layer already exists; what is missing is a governed decision to route a slice of it.** TRON, Hyperliquid, BNB Chain and XRP Ledger all collect substantial fee flows, but those flows end in burns, buybacks or validator income. In ORF terms the hardest technical stage (structural collection, Family A) is in place, and the gap is legitimacy: a chartered, time-bounded, publicly reported redirection of a share to maintenance. That reframes the adoption question from "invent new revenue" to "persuade a governance body to divert existing revenue", which is a dOSPO problem as much as an ORF one.
2. **The strongest mandate runs on the wrong money.** Zcash is the only top-ten chain with a protocol-level dev fund, and on mandate discipline (time-bounded streams, coinholder vote, published veto) it scores highest of the ten. But it is funded by block-subsidy issuance, which ORF excludes, and its native-token balance is already the subject of political contest. It is the clearest live illustration of why ORF separates mandate quality from money quality.
3. **Endowment is not replenishment, and adoption is not return.** Ethereum's move toward an endowment model is real and well documented, but staking yield is native-token correlated (Class 2) and does not diversify price risk. At the other end, the accelerator-heavy chains (BNB, XRP, Solana, TRON) push projects to venture capital at P5. POSM's own diagram lists "Venture Capitalists" among adopters; ORF would count only client-paid services (Family B) or membership and certification (Family C) from that arm, and no receipts for either were found (D0).

**What this means for POSM.** The comparison sharpens rather than weakens the repo's existing classification: POSM is the strongest deployment precedent in the set (retainers, scoped bounties, a governed steward), and its return edge is asserted rather than measured. ORF's contribution is to make P6 measurable: a cost floor, net-contribution reporting, and an inflow inventory that separates fees from issuance. That is the concrete bridge between the two models, and it is the most useful thing release 1 can offer to Cardano and to any chain that adopts a POSM-style program.

**Audience reading.**
- *Web3 foundations:* the question to bring is not "what new revenue could fund maintenance" but "what share of revenue you already collect could be redirected under a chartered, sunset-bound mandate, and who would govern it." Zcash shows the mandate pattern; Optimism (§3.1) shows the Family A routing pattern; neither yet shows a passed gate.
- *Universities and researchers:* the ten chains form a natural comparative sample with public, dated evidence. The open measurement problems are the fee-versus-issuance split (Cardano's is derived, not published), the absence of published treasuries (Solana Foundation; Ethereum Foundation after Oct 2024), and how to attribute adoption-driven fees to specific open-source components.
- *Maintainers and advisors:* POSM-style retainers are the deployable piece today. Anything presented as "self-sustaining" should be checked against the issuance exclusion before it is repeated.

**Open items carried forward (do not cite as High).** Zcash Coinholder-Controlled Fund size (≈146.7k ZEC, third-party readers, Unverified); Hyperliquid's fee share to the Assistance Fund (Unverified); BNB Builder Fund disbursement (unknown); Solana Foundation and post-2024 Ethereum Foundation treasury totals (unknown); TRON fee magnitude (Partial, methodology-dependent); Cardano fee/issuance split (derived, not official); OSC 2026–27 request status (text exists, no on-chain action). Protocol Guild's 2025 figures ($7,231,668 from 6,202 donors; 190 members as of 5 Aug 2026) are Validated by Researchy; the errata entry was approved by Christian Taylor on 9 Oct 2026 and is applied in `ORF_ERRATA.md` and the §3.1 Protocol Guild row (Confidence: High; captures in `chains/data/pg-*`). "Commitments above $80 million" stays Unverified.

Sources: `chains/top10-chains-orf-alignment.md`, `chains/posm-cycle-chain-map.md`, `chains/paid-oss-cycle-chain-map.md`, `chains/researchy-chain-check.md`, `chains/data/POSM-SOURCES.md`.

---

## 4. Claims register & validation method

### 4.1 Method

Imported 141 claims from the foundation draft; scored against whitepaper extracts, `ORF_ERRATA.md` (controlling), Evidence Register, VALIDATION.md, orf-docs, precedents, and tools. Statuses: SUPPORTS / PARTIAL / CONFLICTS / ERRATA / UNVERIFIABLE.

### 4.2 Results (release-1)

| Status | Count |
|--------|------:|
| SUPPORTS | 99 |
| PARTIAL | 35 |
| ERRATA | 5 |
| CONFLICTS | 2 |
| UNVERIFIABLE | 0 |
| **Total** | **141** |

Full worksheet: `claims/orf-claims-validated.md`. Hard flags in that file’s banner are binding on any derivative brief or slide deck.

### 4.3 Lifecycle

Stage 0 → Stage 1 peer review (≥2 independent experts) → Stage 2 piloted precursors → Stage 3 validated production (`VALIDATION.md`). This draft remains **Stage 0**.

---

## 5. Feasibility notes (illustrative only)

The Tier 1 feasibility model uses an illustrative ~**$3.0M** baseline maintenance cost floor and a compound stress scenario (protocol fees −50%, enterprise −40%, membership −30%, capital yield −40%, certification flat) (`C-098`). It requires ecosystem-specific tuning. It is **not** evidence that any named ecosystem clears Gate 3 or Gate 6.

Endowment arithmetic: ~$3M/year spendable income at 3–5% real yield implies on the order of **$60M–$100M+** productive principal — the Endowment Fantasy check (`C-018`).

Evaluator / preview tooling that shows sample `PASSED` is a teaching aid only; it is not a Hard Gate result.

---

## 6. Implementation path (for adopters and advisors)

Sequence derived from the release-1 outline §6 and `synthesis/end-user-needs.md`. Aimed at foundations and research groups evaluating pilots—not a product brochure.

1. **Discovery** — classify inflows with the five economic questions (Origin, Legitimacy, Cost, Risk, Coverage) (`C-039`); publish a Gate 1 cost-floor method.  
2. **First instruments** — prefer B.1 assurance (when capacity exists) or C.1 membership design; withhold B.2 LTS/SLA until the Service Capacity Test passes (`C-058`, `C-073`–`C-074`).  
3. **Legal** — designate or stand up a Neutral Legal Entity; set tax-reserve policy with counsel (Polkadot PCF as design reference only; spend magnitudes remain Unverified in this pack).  
4. **Reporting** — adopt the 12-field tracker and a quarterly replenishment audit (gross, cost-to-collect, net, RCR, MCR, SCR, SLA/wind-down) (`C-099`).  
5. **Pilot completion criteria** — one earned instrument, net-contribution reporting, and a review cadence justify an MV-ORF claim; PCR may remain below 1.0.  
6. **Measurement aids** — CHAOSS/GrimoireLab and Open Source Observer inform deployment decisions; they do not substitute for Gate 2 cash evidence.  
7. **Accompanying materials** — this Stage 0 paper; `INSTRUMENT_CHARTER_TEMPLATE`; enterprise sponsor kit pointers in the upstream repo.

---

## 7. Limitations, risks, research agenda

### 7.1 Risks / anti-patterns

| Risk | Mitigation in model |
|------|---------------------|
| Treasury Relabeling | Gate 2 cash evidence |
| Endowment Fantasy | Principal reality check; IPS + receipts |
| Routing Mirage | Taxonomy exclusion of rails/engines |
| Issuance as income | Decompose fees vs expansion (A.4) |
| Liability without capacity | Service Capacity Test |
| Operator / customer capture | Replaceability; membership ≠ technical control |
| Concentration | Gates 5–6; RCR/MCR |
| Pay-to-pass certification | Payment buys testing only |
| Premature “self-sustaining” | All eight gates simultaneous |

### 7.2 Gaps blocking Stage 1+

See `synthesis/gaps.md`: expert interviews not done; no independent eight-gate audit of any ecosystem; longitudinal POSM retention pending; several landscape magnitudes Unverified; OMF trillion erratum still needed; no OSFL-owned C_base reference implementation; SLA vault code removed. Expansion hunt still thin on restaking/yield beyond Octant, naming-revenue peers beyond ENS, Asia public funds, university tech-transfer endowments, and non-Optimism L2 fee loops (`web2-web3-prototypes-expansion.md`).

### 7.3 Research agenda (actionable)

1. Stage 1 expert panel using `synthesis/expert-critique-angles.md` (questions only until dispositions exist).  
2. Publish empirical Gate 1 cost-floor methodology.  
3. Build eight-quarter correlation datasets for Gate 4 Step 1 where history allows.  
4. Refresh primary packets for Unverified magnitudes (Guild dollars, Polkadot spend, POSM budget lines, Octant epochs, Deep Funding).  
5. Retypeset ORF PDF incorporating errata; add OMF erratum for the trillion merge.  
6. Optional: publish the interactive GitHub Pages scaffold under `site/` once the author approves.

---

## 8. Conclusion

Release-1 does not claim that open infrastructure is already self-sustaining. Its contribution is a **falsifiable architecture**: a vocabulary that separates governance, deployment, and replenishment; a portfolio taxonomy that refuses to count routing rails as revenue; gates and ratios that make “sustainable” costly to assert; and an evidence discipline that prefers ERRATA and PARTIAL over persuasive fiction.

For universities, the claim matrix and errata layer are teachable methods. For foundations, the honesty spine and gate set are treasury red-team tools. Adjacent practitioners (enterprise buyers, maintainer programs, advisors) can adopt MV-ORF pilots without asserting Hard Gates that no reviewed ecosystem has cleared.

**Stage 0. No Hard Gate passed. Errata controls.**

---

## Bibliography (primary pointers)

- `whitepapers/orf-v1.0.pdf` + controlling `whitepapers/ORF_ERRATA.md` / `sources/ORF_ERRATA.md`  
- dOSPO & OMF whitepapers (`sources/dospo-whitepaper.txt`, `sources/omf-whitepaper.txt`)  
- `orf/INSTRUMENT_CATALOG.md`, `orf/GOVERNANCE_RULES.md`, `VALIDATION.md`, `docs/EVIDENCE_REGISTER.md`  
- Hoffmann, Nagle & Zhou, HBS Working Paper 24-038 — https://www.hbs.edu/faculty/Pages/item.aspx?num=65230  
- Synopsys OSSRA 2024 materials (cite with errata caution)  
- Optimism docs / Year 3 budget update / buyback vote materials (see errata URLs in `C-103`–`C-106`)  
- ENS KPK review thread; EP 6.46 (cite as separate closes)  
- Intersect POSM explainer; Protocol Guild Q2 2026 membership audit; Protocol Guild Annual Report 2025 (29 Jan 2026, https://www.protocolguild.org/blog/20260129-annual-report-2025) and Q3 2026 Membership Audit (26 Aug 2026, https://www.protocolguild.org/blog/20260826-q3-quarterly-audit), rendered captures in `docs/chains/data/` (accessed 9 Oct 2026)  
- Linux Foundation / CNCF certification & membership pages  
- Sonar–Tidelift definitive agreement announcement (wording per `C-112`)  
- In-pack validated worksheets: `claims/orf-claims-validated.md`, `claims/researchy-claim-deltas.md`, `use-cases/web2-web3-prototypes.md`, `use-cases/web2-web3-prototypes-expansion.md`, `use-cases/researchy-validation.md`, `claims/implementation-validation.md`

Dated access for this draft: 2026-09-24 America/Los_Angeles.
