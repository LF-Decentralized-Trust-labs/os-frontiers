# Web2 / Web3 Prototypes Catalog — OSFL Release-1

> Structured catalog of environments that could prototype **dOSPO**, **OMF**, and/or **ORF**.  
> Prefer primary or official URLs. Quotes and metrics only where cited; otherwise mark UNKNOWN.  
> Drafted 2026-09-24 PT · Deepened dossiers by USe Me (RESEARCH ENGINE) same day.
> **Stage 0.** Errata controls over ORF PDF. Dated source packets below for priority environments.  
> Pillar codes: **dOSPO** = governance; **OMF** = maintenance deployment; **ORF** = replenishment.

---

## How to read each entry

| Field | Meaning |
|-------|---------|
| Pillar(s) | Which OSFL layer(s) this environment most closely prototypes |
| Prototype fit | What it demonstrates in practice |
| Gaps vs OSFL models | What is missing relative to the closed-loop Stage 0 specs |
| Sources | Real URLs (no invented quotes) |

---

## 1. Corporate OSPOs (e.g. TODO Group / LF guides)

| | |
|--|--|
| **Pillar(s)** | dOSPO (partial); OMF (consumption-side); ORF (weak — usually one-way sponsorship) |
| **Prototype fit** | Organizational coordination of open-source use/contribution policy; membership and sponsorship of foundations; internal RACI-like ownership of OSS risk. |
| **Gaps vs OSFL** | Typically **custodial** corporate budget, not non-custodial community governance; no eight hard gates / PCR discipline; replenishment is episodic sponsorship, not diversified portfolio; maintainer autonomy vs corporate capture not enforced as OMF safeguards. |
| **Sources** | https://todogroup.org · https://www.linuxfoundation.org/resources/open-source-guides/setting-an-open-source-strategy · https://www.linuxfoundation.org/resources/open-source-guides/participating-in-open-source-communities |

---

## 2. Linux Foundation / CNCF / Apache Software Foundation

| | |
|--|--|
| **Pillar(s)** | dOSPO (membership governance analogs); OMF (project life-cycle / TAC); ORF Family C (membership dues, training, certification) |
| **Prototype fit** | Tiered membership funding; neutral foundation legal wrappers; CNCF Certified Kubernetes conformance (catalog C.2 precedent); LF training/certs (C.3). |
| **Gaps vs OSFL** | Not a Web3 closed loop; membership revenue is not measured against a published ecosystem **cost floor** with Gates 1–8; many projects still depend on corporate seconded labor rather than OMF retainers; no unified ORF portfolio across uncorrelated classes. |
| **Sources** | https://www.linuxfoundation.org · https://www.cncf.io · https://www.apache.org · ORF catalog cites CNCF Certified Kubernetes / LF CKA-CKAD in `orf/INSTRUMENT_CATALOG.md` |

---

## 3. GitHub Sponsors

| | |
|--|--|
| **Pillar(s)** | OMF (maintainer stipends); ORF Family D (voluntary) — routing-like platform |
| **Prototype fit** | Direct recurring sponsorship to maintainers/orgs; invoiced org billing; low friction for individuals. |
| **Gaps vs OSFL** | Voluntary / concentration risk; no net-contribution audit standard; not a Neutral Legal Entity + Service Capacity Test stack; does not implement Gate 5 RCR or Gate 8 independent audit for ecosystems. Fee structure for org sponsors differs from individual (see docs). |
| **Sources** | https://docs.github.com/en/sponsors/receiving-sponsorships-through-github-sponsors/about-github-sponsors-for-open-source-contributors · https://github.com/sponsors |

---

## 4. Open Collective

| | |
|--|--|
| **Pillar(s)** | OMF (transparent expenses); ORF Family D / fiscal hosting; weak dOSPO (collective budgets) |
| **Prototype fit** | Transparent collective ledgers; fiscal hosts; GitHub Sponsors partnership routing into Collective balances. |
| **Gaps vs OSFL** | Does not enforce ORF taxonomy (revenue vs routing); no eight hard gates; largely donation/grant inflows; not enterprise SLA / structural fee architecture. |
| **Sources** | https://opencollective.com · https://opencollective.com/github-sponsors · https://docs.opencollective.com |

---

## 5. Protocol Labs / Filecoin

| | |
|--|--|
| **Pillar(s)** | OMF (ecosystem grants / research); ORF partial (network-adjacent funding); dOSPO-like foundation governance UNKNOWN depth |
| **Prototype fit** | Large ecosystem R&D and public-goods funding around Filecoin/IPFS stack; Drips also notes Filecoin network support for dependency splits. |
| **Gaps vs OSFL** | No sourced claim in this draft that PL operates the full dOSPO→OMF→ORF loop with PCR/Gates; grant-era funding risks Treasury Relabeling if counted as replenishment. Magnitude of closed-loop coverage: **UNKNOWN** (needs primary financial disclosure review). |
| **Sources** | https://protocol.ai · https://filecoin.io · Drips tool note: https://drips.network · repo `tools/DRIPS_PROTOCOL.md` |

---

## 6. Ethereum (Protocol Guild, Project Odin, ENS adjacency)

| | |
|--|--|
| **Pillar(s)** | OMF (Protocol Guild retainers); ORF Family D (pledges); dOSPO-like (EF / MetaGov patterns); ENS separately closest ORF closed-loop |
| **Prototype fit** | Protocol Guild voluntary 1% pledges + vesting; Project Odin as funding-coordination precedent (repo: not a rail). |
| **Gaps vs OSFL** | Guild is Family D — revocable; dollar scale claims subject to ORF_ERRATA (do not republish High until annual report quoted); EF grant programs are deployment, not ORF replenishment. |
| **Sources** | https://www.protocolguild.org · repo `docs/precedents/ETHEREUM_EVM.md`, `docs/precedents/PROJECT_ODIN.md` · ERRATA: https://www.protocolguild.org/blog/20260604-Q2-quarterly-audit |

---

## 7. Optimism / Superchain

| | |
|--|--|
| **Pillar(s)** | ORF Family A (sequencer profit contribution); OMF (Retro Funding deployment); dOSPO-like bicameral Collective |
| **Prototype fit** | Strongest structural L2 revenue precedent: greater of 15% net / 2.5% gross for standard chains; OP Mainnet 100% per current docs (errata); Retro Funding uses OSO impact metrics. |
| **Gaps vs OSFL** | Partial loop; payer concentration / Base stack transition risk; Retro Funding is **allocation/deployment** not replenishment (ERRATA); Foundation operating budget from initial token allocation per Year 3 update — not from ETH fee line. |
| **Sources** | https://docs.optimism.io/governance/capital-allocation · https://gov.optimism.io/t/collective-year-3-budget-update-and-year-4-budget-outlook/10057 · https://optimism.io/blog/op-token-buybacks · repo `docs/precedents/OPTIMISM_SUPERCHAIN.md` |

---

## 8. Polkadot / OpenGov / PCF

| | |
|--|--|
| **Pillar(s)** | dOSPO (OpenGov + PCF neutral executor); OMF (treasury-funded development); ORF partial (fees/issuance mix) |
| **Prototype fit** | Cayman PCF as unopinionated legal executor directed by OpenGov — Neutral Legal Entity template. |
| **Gaps vs OSFL** | Issuance-heavy inflows must be decomposed under ORF; 2025 treasury spend magnitudes marked **unverified** in Evidence Register / ERRATA this pass; Fellowship ranks are OMF-adjacent career ladder, not ORF. |
| **Sources** | https://wiki.polkadot.com/general/pcf/ · repo `docs/precedents/POLKADOT_OPENGOV.md` |

---

## 9. Cardano / Intersect POSM

| | |
|--|--|
| **Pillar(s)** | dOSPO (OSC oversight); OMF (retainers, Code for Us, bounties, incubation); ORF weak (treasury-funded; 20% reward-pot cut is mixed fees+issuance) |
| **Prototype fit** | Strongest Web3 lab for OMF programming under Intersect MBO. |
| **Gaps vs OSFL** | Explicitly **not replenishment** in ORF §2 table; ADA budget / bounty dollar figures **unverified** on Intersect explainer per Evidence Register / ERRATA. |
| **Sources** | https://www.intersectmbo.org/news/the-paid-open-source-model · repo `docs/precedents/CARDANO_POSM.md` |

---

## 10. Sovereign Tech Fund (Sovereign Tech Agency)

| | |
|--|--|
| **Pillar(s)** | OMF (maintenance investment in base technologies); ORF absent (public budget inflows, not earned portfolio) |
| **Prototype fit** | Public-sector investment in critical OSS base tech; ongoing applications; minimum contract size stated on agency site (€50,000). |
| **Gaps vs OSFL** | Annual Bundestag / public budget dependence — one-way sovereign capital, not net commercial replenishment; no Gate 3 PCR from earned families; selection process ≠ Neutral Legal Entity commercial SLAs. |
| **Sources** | https://www.sovereign.tech/programs/fund · https://www.sovereign.tech/news/new-proposals-criteria-process-timeline |

---

## 11. OpenSSF (Open Source Security Foundation)

| | |
|--|--|
| **Pillar(s)** | OMF (security programs, Alpha-Omega-style maintainer support); dOSPO-like (LF cross-industry governance); ORF Family C (membership) |
| **Prototype fit** | Industry coalition to sustainably secure OSS development/maintenance/consumption; tooling (Scorecards, SLSA, Sigstore, etc.). |
| **Gaps vs OSFL** | Security-focused mandate, not full five-family ORF portfolio; membership funds foundation programs rather than measured ecosystem cost-floor coverage; no published eight-gate self-sustainability claim in sources reviewed here. |
| **Sources** | https://openssf.org/about/ · https://openssf.org/ · https://openssf.org/blog/2023/11/20/openssf-publishes-mission-vision-values-and-strategy/ |

---

## 12. CHAOSS / GrimoireLab metrics

| | |
|--|--|
| **Pillar(s)** | dOSPO / OMF **measurement support** (not revenue); Gate 1 cost-floor / health indicators enablers |
| **Prototype fit** | Community health analytics; Perceval retrieval; SortingHat identity resolution — informs retainer and pathway decisions. |
| **Gaps vs OSFL** | Metrics ≠ money; does not collect replenishment; must not be confused with PCR cash evidence (Gate 2). |
| **Sources** | https://chaoss.community · repo `tools/GRIMOIRELAB_CHAOSS.md` · https://chaoss.github.io/grimoirelab/ |

---

## 13. Drips Protocol

| | |
|--|--|
| **Pillar(s)** | OMF/ORF **Routing Rail S.1** only |
| **Prototype fit** | Recursive dependency-graph splits; continuous streams on EVM/Filecoin. |
| **Gaps vs OSFL** | Explicitly **not independent revenue**; zero replenishment under ORF taxonomy. |
| **Sources** | https://drips.network · https://docs.drips.network · https://github.com/radicle-dev/drips-contracts · repo `tools/DRIPS_PROTOCOL.md` |

---

## 14. Superfluid

| | |
|--|--|
| **Pillar(s)** | OMF/ORF **Routing Rail S.2** |
| **Prototype fit** | Constant Flow Agreements for per-second maintainer stipends with real-time cancellation. |
| **Gaps vs OSFL** | Moves existing money; does not originate net contribution. |
| **Sources** | https://www.superfluid.finance · repo `tools/SUPERFLUID.md` |

---

## 15. Merit Systems

| | |
|--|--|
| **Pillar(s)** | OMF (attribution / contributor rewards); ORF adjacent (agentic commerce rails) — research horizon |
| **Prototype fit** | GitHub commit attribution and AgentCash / x402-style payment gateway experiments for contributor compensation. |
| **Gaps vs OSFL** | Not a five-family portfolio; commercial/agentic rails need Gate 2 cash-evidence discipline; Stage maturity vs ORF D-scale: treat as early unless local receipts proven. |
| **Sources** | repo `tools/MERIT_SYSTEMS.md` (primary for this catalog) · project URLs as listed therein — verify before quoting metrics |

---

## 16. Andamio

| | |
|--|--|
| **Pillar(s)** | OMF (contributor pathways / onboarding); dOSPO support (credentialed ladders); treasury escrow rail |
| **Prototype fit** | Cardano Plutus course validators; tokenized contributor credentials unlocking tasks and escrow payouts. |
| **Gaps vs OSFL** | Onboarding/credentialing ≠ replenishment; escrow is routing of already-budgeted funds. |
| **Sources** | https://andamio.io · https://docs.andamio.io · https://github.com/andamio-platform · repo `tools/ANDAMIO.md` |

---

## 17. Additional prototypes named in repo prior art (brief)

| Environment | Pillar(s) | Gap note | Source |
|-------------|-----------|----------|--------|
| ENS DAO / Endowment | ORF A+E (+ dOSPO-like) | Closest closed loop; yield ~⅕ expenses; two AUM closes | https://docs.ens.domains/dao/proposals/6.46/ · https://discuss.ens.domains/t/kpk-2025-review-for-the-ens-endowment/21829 |
| Tidelift / Sonar | ORF B (+ OMF) | Enterprise assurance proof; definitive acquisition agreement (closing status per errata) | https://www.sonarsource.com/company/press-releases/sonar-to-acquire-tidelift/ |
| Octant (Golem) | ORF E | Capitalized staking yield; Epoch payouts unverified this pass | https://golem.foundation/2023/08/08/announcing-octant.html |
| Nouns DAO | ORF scarces-asset auction | Cultural demand dependency; magnitudes unverified this pass | Evidence Register: unverified |
| Gitcoin Grants | OMF allocation + Family D | Quadratic funding rounds ≠ replenishment (ERRATA) | https://gitcoin.co/program |
| Open Source Observer | OMF allocation metrics | Impact tracing for Retro Funding; not revenue | repo `tools/OPEN_SOURCE_OBSERVER.md` · https://www.opensource.observer |
| LFX Crowdfunding | ORF C / D platform | LF invoicing for corporate contributions | https://crowdfunding.linuxfoundation.org/for-companies |

---

## Summary counts

| Category | Count in this draft |
|----------|--------------------:|
| Primary catalog entries (§1–§16) | **16** |
| Additional brief rows (§17) | **7** |
| **Total prototype rows** | **23** |
| Mapped to dOSPO (primary or partial) | 12 |
| Mapped to OMF | 18 |
| Mapped to ORF (incl. rails / partial) | 20 |

---

## Method notes / blockers

- Magnitudes flagged **unverified** or errata-controlled must not be cited as High confidence in release-1 prose.
- Expert interviews for transferability judgments: **not done** (see `synthesis/gaps.md`).
- Filecoin / Protocol Labs closed-loop financials: **UNKNOWN** pending primary disclosure review.


---

# Deep dossiers (priority environments)

> Each packet lists **only** claims with a dated primary URL or an explicit Unverified/Errata flag. No invented expert quotes.

## Dossier A — Optimism / Superchain (Family A + OMF adjacency)

### Mapping
| OSFL layer | What maps | What does not |
|---|---|---|
| **ORF Family A** | Standard-chain sequencer contribution (greater of 15% net profit or 2.5% gross fees); OP Mainnet 100% of revenue to shared treasury | Treating Retro Funding OP commitments as replenishment |
| **OMF** | Retro Funding as deployment/allocation of already-held resources | — |
| **dOSPO-like** | Bicameral Collective (Token House / Citizens' House) | Full dOSPO policy-domain replaceability proof |

### Dated source packet
| Date | Document | What it supports | Confidence |
|---|---|---|---|
| Current (docs) | https://docs.optimism.io/governance/capital-allocation | Standard-chain greater-of rule; OP Mainnet 100% carve-out (ERRATA supersedes older “no exceptions” line) | Medium |
| 2025-06-24 | https://gov.optimism.io/t/collective-year-3-budget-update-and-year-4-budget-outlook/10057 | 17,756 ETH all-time Superchain revenue; Base share 6,210 ETH; OP Mainnet 11,170 ETH; 26.4M OP Retro / 437 grantees; Foundation budget from initial 30% supply | Medium (Foundation narrative, not audit) |
| 2026-01-08 | https://optimism.io/blog/op-token-buybacks | Proposal: 50% of **incoming** Superchain revenue; 5,868 ETH prior-12-month collection | Medium — proposal, not vote |
| 2026-01-28 | vote.optimism.io proposal (SUCCEEDED) + https://www.coindesk.com/business/2026/01/28/optimism-governance-approves-op-token-buyback-plan-tied-to-superchain-revenue | 12-month pilot from February; CoinDesk reports 84.4% and “net” wording | Sourced for vote status; Medium for percent (CoinDesk of portal) |

### ORF gate lens (honest)
- **Gate 2:** figures are single-publisher Foundation reports → remain Medium, not cash-audit passed.
- **Gate 5 / Exit Risk:** Base stack transition cited in paper/register as concentration illustration.
- **PCR ≥ 1.0 / eight gates:** not claimed; partial loop only.
- **Local D for a non-Optimism adopter:** D0 until that ecosystem authorizes a split and has receipts (`INSTRUMENT_CATALOG` A.2).

### Repo crosswalk
`sources/precedents/OPTIMISM_SUPERCHAIN.md` · `sources/EVIDENCE_REGISTER.md` §2–3 · `sources/ORF_ERRATA.md` · claims `C-020`–`C-022`, `C-103`–`C-106`, `C-125`

---

## Dossier B — ENS DAO / Endowment (Family A + E; closest closed-loop judgment)

### Mapping
| OSFL layer | What maps | What does not |
|---|---|---|
| **ORF Family A** | Canonical `.eth` registration/renewal fees | — |
| **ORF Family E** | Governed endowment under EP 6.46 IPS | Treating yield alone as Day-1 bootstrap |
| **dOSPO-like** | DAO governance of endowment manager / IPS | Full series closed loop under OSFL names |

### Dated source packet
| Date | Document | What it supports | Confidence |
|---|---|---|---|
| 2026-01-21 | https://discuss.ens.domains/t/kpk-2025-review-for-the-ens-endowment/21829 | Ops revenue $18.22M; ops expenses $17.54M; endowment revenues covering **20.3%** of those expenses; Dec AUM $113.86M (European comma on page) | Medium — one close |
| Passed (EP 6.46); footnote period `apr_2026` | https://docs.ens.domains/dao/proposals/6.46/ | Later snapshot: ~$93.4M non-custodial AUM; >$8M net DeFi returns since inception; 2025 opex $16.4M per Steakhouse | Medium — **different close** from KPK |

### Hard rule for writers
**Do not stack** KPK December AUM with EP 6.46 AUM into one cell. Same institution, two closes (`C-023`, `C-107`). Instructive constant across both: endowment yield ≈ one-fifth of opex — resilience layer, not a foundation.

### ORF gate lens
- Closest closed-loop **judgment** in register — not an eight-gate pass.
- Family E: late-stage resilience (`C-066`).

### Repo crosswalk
`sources/precedents/ETHEREUM_EVM.md` · `sources/EVIDENCE_REGISTER.md` ENS rows · `sources/ORF_ERRATA.md` · `orf-docs/INVESTMENT_POLICY_STATEMENT.md` · claims `C-023`–`C-024`, `C-107`, `C-126`, `C-135`

---

## Dossier C — Cardano / Intersect POSM (OMF precursor; ORF weak)

### Mapping
| OSFL layer | What maps | What does not |
|---|---|---|
| **dOSPO** | OSC oversight / OSO execution pattern (Intersect explainer) | Claiming full dOSPO Stage 3 |
| **OMF** | Maintainer retainers, Code for Us, incubation, contribution ladder | — |
| **ORF** | Limited — treasury-funded programs; reward-pot cut mixes fees + issuance (`A.4` critical notice) | Calling POSM “replenishment proof” |

### Dated source packet
| Date | Document | What it supports | Confidence |
|---|---|---|---|
| Intersect explainer (opened 2026-09-18 per register) | https://www.intersectmbo.org/news/the-paid-open-source-model | Program list: OSC oversight, OSO execution, retainers, Code for Us, incubation; language that model “supports commercial adoption, replenishing the treasury” | **Sourced** for program description |
| — | Same page | 2025 ADA budget, bounty-pool totals, “5.885M ADA”, “$300K bounty fully utilized” | **Unverified** — not on explainer (ERRATA) |
| Catalog / paper | `orf-docs/INSTRUMENT_CATALOG.md` A.4; D.2 | 20% epoch reward-pot cut = mixed fees+issuance; Mission-Driven / community pools as Family D analog (P2/D2 catalog ratings) | PARTIAL — exact 20% wording needs dated Cardano monetary-policy cite before Hard use |

### ORF gate lens
- VALIDATION.md: OMF Retainers Stage 0 grounded in POSM pilot cohort; longitudinal retention still open.
- High transferability for **OMF program shape**; **not ORF proof**.

### Repo crosswalk
`sources/precedents/CARDANO_POSM.md` · `sources/EVIDENCE_REGISTER.md` Cardano rows · `sources/VALIDATION.md` · claims `C-029`, `C-055`–`C-056`, `C-134`

---

## Dossier D — Linux Foundation / CNCF (Family C Web2 production)

### Mapping
| OSFL layer | What maps | What does not |
|---|---|---|
| **ORF Family C** | Membership dues (C.1); Certified Kubernetes conformance (C.2); CKA/CKAD training (C.3) | Web3 closed-loop PCR against an ecosystem cost floor |
| **dOSPO-like** | Neutral foundation / TAC / membership governance analogs | Non-custodial token-holder replaceability |
| **OMF-like** | Project lifecycle, seconded labor common | OMF retainer + legitimacy safeguards as specified |

### Dated source packet
| Document | What it supports | Confidence |
|---|---|---|
| https://www.linuxfoundation.org | Membership / foundation wrapper pattern | Qualitative SUPPORTS for C.1 precedent class |
| https://www.cncf.io (Certified Kubernetes program) | Conformance certification; payment buys testing not a passing result (`C-064`) | Qualitative SUPPORTS; **“90+ offerings”** count is catalog assertion — PARTIAL until recounted on a dated page |
| LF training / CKA–CKAD pages | Professional certification credential market | PARTIAL — indicative $300–$750 exam band is catalog guidance (`C-063`) |
| `orf-docs/INSTRUMENT_CATALOG.md` C.1–C.3 | P4 / P3 external ratings; local D0 until receipts | Stage 0 catalog |

### ORF gate lens
- Strongest **Web2** Family C production analog.
- Gaps: no published eight-gate self-sustainability claim; many projects still corporate-seconded labor.

### Repo crosswalk
Use-case §2 · claims `C-061`–`C-064`, `C-130`–`C-132`

---

## Dossier E — Protocol Guild (Family D; mechanism strong, dollars downgraded)

### Mapping
| OSFL layer | What maps | What does not |
|---|---|---|
| **ORF Family D** | Voluntary ~1% token/yield pledges; vesting; revocable | Primary path to PCR ≥ 1.0 |
| **OMF** | Time-weighted tenure streams to core client maintainers | — |

### Dated source packet
| Date | Document | What it supports | Confidence |
|---|---|---|---|
| 2026-05-22 (as of) / Q2 2026 audit post | https://www.protocolguild.org/blog/20260604-Q2-quarterly-audit | **196 funded members** (up from 187 prior quarter) | Membership: recoverable per ERRATA |
| — | Same / annual report body | $7.2M from 6,202 donors (2025); $80M+ committed | **Unverified** this pass — do not publish as High (`C-026`, `C-110`) |
| Docs / contracts | https://protocol-guild.readthedocs.io/ · https://github.com/protocolguild/protocol-guild | Mechanism: eligibility, vesting, split contract | Mechanism SUPPORTS |

### ORF gate lens
- Keep mechanism; downgrade scale.
- Family D = diversification / alignment, weak foundation for guaranteed operating liabilities (`C-065`).

### Repo crosswalk
`sources/precedents/ETHEREUM_EVM.md` · `sources/ORF_ERRATA.md` Protocol Guild · claims `C-026`, `C-110`, `C-133`

---

## Cross-dossier synthesis note (for @Give me Purposise)

| Audience | Lead with | Never lead with |
|---|---|---|
| Foundations | Honesty spine (Stage 0; no complete loop; P≠D) + Neutral Legal Entity (PCF) + Family C/E patterns | Invented “self-sustaining” PCR stories |
| Universities | Claim matrix + errata discipline + research contribution = synthesis architecture | Deleted `ORFSlaVault.sol` as live implementation |
| Enterprises | Family B assurance vs SCT-gated SLA; Tidelift definitive-agreement wording | Selling liability without capacity |
| Maintainers | OMF POSM / Protocol Guild retainer patterns; rails ≠ pay | Guild dollar headlines |
