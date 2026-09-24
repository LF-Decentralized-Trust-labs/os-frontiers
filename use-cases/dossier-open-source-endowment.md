# Dossier — Open Source Endowment (OSE)

> **Pass date:** 2026-09-24 PT  
> **Stage 0:** research candidate — **no Hard Gate passed**. Not a validated ORF transfer.  
> **Pillar codes:** **ORF Family E** (endowment spend-rate) · **OMF** (microgrants / awards to critical underfunded projects) · **dOSPO-like** (member-elected board; weak)  
> **Catalog row:** N5 in `web2-web3-prototypes-expansion.md`  
> **Method:** live WebSearch / WebFetch / curl; primary pages preferred; cite About/FAQ figures as **publisher figures**, not Gate 2 audited cash.  
> **Errata:** do not stack or reassert ENS endowment closes from `sources/ORF_ERRATA.md`; OSE is a separate institution.

---

## Mechanism (how money / governance / maintenance actually works)

**Open Source Endowment Foundation** is a US **501(c)(3)** public charity (EIN **33-3502715**). FAQ: incorporated **14 February 2025**. Donations go into an invested corpus; **only investment returns** fund grants (principal not spent as operating grant capital under the stated model).

**Investing (About / FAQ, publisher):** early holdings in US Treasuries (~5%/yr narrative on About); portfolio transferring to professional asset manager **Infinite Giving** (board-chosen, US-nonprofit specialist); target **7–8%** return with **5%** annual spend rate on grants; remainder reinvested after operating costs.

**Grant model (About / FAQ, publisher):** member-developed open data-driven selection; Value + Risk scores; eligibility requires open-source license, active, **nonprofit / no strong corporate affiliation**, funding intent. Target format: **microgrants up to $5,000** after board due diligence. Framing prioritizes deep infrastructure / “long tail” and explicitly **excludes** corporate-tied projects (examples on FAQ: Kubernetes, ClickHouse). Forward-looking grants and backward-looking awards both described.

**Governance (About, publisher counters on page):** donors; **Members** at **≥ $1,000/year** advise grant model, join closed events, appoint/elect directors (membership policy referenced); **Board of Directors** (all must be Members) appoints Executive Director and Advisors. Institutional donors welcomed for capital but **without governing rights** (FAQ). Key docs / minutes pointed to site Docs + GitHub `osendowment`.

**Board / staff named on About (checked 2026-09-24 PT):** Directors — Konstantin Vinogradov (Chair), Amy Parker (Secretary), Maxim Konovalov (Treasurer), Chad Whitacre (Director). Executive Director — Jonathan Starr. Advisor listed — Vlad-Stefan Harbuz (also Pledge / thanks.dev adjacency).

---

## Prototype fit to dOSPO / OMF / ORF

| OSFL layer | What maps | What does not |
|---|---|---|
| **ORF Family E** | Endowment corpus + published spend-rate target; long-horizon resilience design | Treating early corpus as university-scale foundation; Day-1 bootstrap via yield alone |
| **OMF** | Microgrants / awards aimed at maintainer sustainability gaps | Recurring retainer employment architecture (POSM/Geomys-class) |
| **dOSPO-like** | Member skin-in-the-game board elections; published bylaws/membership policy posture | Non-custodial token governance; full dOSPO policy-domain replaceability |
| **ORF Family A/B/C/D** | — | No structural fee, assurance product, membership dues engine, or corporate pledge norm **as OSE’s own** replenishment (Pledge is complementary external rail) |

---

## Gaps vs OSFL Stage 0 specs

- **Corpus scale vs cost floor:** About states **$765K** current fund size (publisher). At 5% spend ≈ **~$38K/year** illustrative grant capacity — **not** an ecosystem C_base; far below illustrative ORF Tier-1 operating models elsewhere in the series (do not invent a floor here).
- **Gate 2 / audited cash:** site figures are single-publisher; no independent audit pack claimed on pages reviewed.
- **PCR / eight Hard Gates:** not claimed.
- **Neutral Legal Entity:** 501(c)(3) is a real legal wrapper for philanthropy — **not** the same as OSFL Neutral Entity + Service Capacity Test for fee/SLA collection.
- **Family A pairing:** absent; OSE is pure E (+ grant deployment).
- **Corporate-tied exclusion:** deliberate; limits coverage of many critical but vendor-adjacent projects.
- **First funding round:** FAQ says first profit generated and first round “underway” — outcomes/receipts **UNKNOWN** on pages reviewed this pass.
- **ENS comparison hygiene:** do **not** stack OSE $765K with ENS KPK / EP 6.46 AUM closes.

---

## Dated source packet

| URL | What it supports | Checked | HTTP |
|---|---|---|---|
| https://endowment.dev/ | Home; schema.org Nonprofit501c3 / EIN / foundingDate 2025-02-14 | 2026-09-24 PT | 200 |
| https://endowment.dev/about/ | Mission; 501(c)(3); donors/members/board counts; grant model; invest strategy; **$765K** / **5%** spend; board & staff names | 2026-09-24 PT | 200 |
| https://endowment.dev/faq/ | Legal status; incorporate date; Member $1k; Infinite Giving; 7–8% target; microgrant model; corporate donor rules; EIN | 2026-09-24 PT | 200 |
| https://endowment.dev/docs/ | Docs index (bylaws / minutes / policies landing) | 2026-09-24 PT | 200 |
| https://github.com/osendowment | Public repo for transparency / model materials | 2026-09-24 PT | 200 |
| https://opensourcepledge.com/about/ | Pledge FAQ points individuals to OSE as complementary individual-donor endowment | 2026-09-24 PT | 200 |

---

## Magnitudes

| Claim | Figure | Source class | Notes |
|---|---|---|---|
| Current fund size | **$765K** | About page publisher | **Not** Gate 2 audited AUM |
| Spend rate (grants) | **5%** / year (target) | About / FAQ publisher | Illustrative |
| Return target | **7–8%** | About / FAQ publisher | With Infinite Giving narrative |
| Microgrant ceiling | **up to $5,000** | About / FAQ publisher | Target format |
| Member threshold | **≥ $1,000 / year** | About / FAQ | One year membership per $1k (FAQ) |
| Donors / Members / Directors | **120** / **69** / **4** | About page counters | Site counters; snapshot on fetch day |
| Institutional donors | **6** (FAQ narrative) | FAQ publisher | — |
| EIN | **33-3502715** | About / FAQ / schema.org | Legal identifier |
| Incorporate date | **2025-02-14** | FAQ + schema.org | — |
| Grants disbursed to date / round outcomes | **UNKNOWN** | — | “First funding round underway” only |
| Audited financials / Form 990 body | **UNKNOWN** this pass | — | Not opened |

---

## Audience lead / don’t-lead

| Audience | Lead | Don’t-lead |
|---|---|---|
| **Foundations** | Family E spend-rate discipline + member-elected neutrality design; complement to corporate Pledge cash | “Endowment solves maintenance” without corpus math |
| **Universities** | Classic endowment applied to OSS; open selection model as research object | Equating $765K publisher figure with mature university endowments or ENS closes |
| **Enterprises** | Optional donate path; **no** governance rights for institutions (by design) | Buying assurance/SLA from OSE (it is not that product) |
| **Maintainers** | Nonprofit / no-corp-tie eligibility; microgrant + award framing | Expecting retainer-scale pay from 5% of $765K |
| **Consultants** | Clean Family E exemplar for ORF taxonomy teaching | Claiming PCR ≥ 1.0 or eight-gate pass |

---

## What would transfer (honest judgment)

OSE is a **Stage 0 research candidate** for **ORF Family E** (corpus → spend-rate → grants) with a light **OMF deployment** layer and **member-skin-in-the-game** governance. What transfers is the **legal + IPS-shaped story** (invest principal, spend ~5%, member-directed grant model, corporate capital without corporate capture of the board). What does **not** transfer yet: scale against any published ecosystem cost floor, Gate 2 audit-grade receipts, pairing with Family A earned fees, or proof that microgrants change maintainer retention. Relative to ENS, OSE is earlier and smaller — use it as a **Web2 philanthropic E** specimen, not as a closed-loop registrar+endowment peer. Local maturity for any adopter copying the pattern remains **D0** until corpus, IPS, and grant receipts exist in that adopter’s own books.
