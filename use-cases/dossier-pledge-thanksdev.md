# Dossier — Open Source Pledge + thanks.dev (linked loop)

> **Pass date:** 2026-09-24 PT  
> **Stage 0:** research candidate — **no Hard Gate passed**. Not a validated ORF transfer.  
> **Pillar codes:** **OMF** (maintainer cash) · **ORF Family D** (voluntary corporate social norm) · **ORF/OMF Routing** (thanks.dev dependency-graph split; S.1-adjacent Web2) · **dOSPO:** weak (transparency/reporting norm only)  
> **Catalog rows:** N1 + N2 in `web2-web3-prototypes-expansion.md` (treated here as **one linked loop**)  
> **Method:** live WebSearch / WebFetch / curl; primary pages preferred. **Site counters ≠ audited cash.**  
> **Errata:** do not reassert Protocol Guild dollar headlines or other `ORF_ERRATA.md` retractions.

---

## Mechanism — Open Source Pledge

The **Open Source Pledge** is a voluntary association of **companies** that commit to:

1. Pay a minimum of **US$2,000 per year per full-time-equivalent developer** on staff, in **cash**, to Open Source maintainers and/or foundations of the company’s choosing (eligible-payment rules on About).
2. **Publish** an annual post (developer count, total paid, breakdown).
3. **Renew** yearly to remain listed.

**Critical custody rule (About FAQ):** *“Payments are made directly to maintainers — we never handle any funds.”* The Pledge is a **norm + transparency** instrument, not a fiscal host or treasury.

Launch / Innovator badge: founding members who joined before launch on **08 Oct 2024**. Individuals cannot join as members (single-person companies may). About explicitly points individual donors to the **Open Source Endowment** instead. Unrelated to cryptocurrencies/DAOs per About.

Payment platforms named as common rails (still subject to Pledge eligibility filters): **thanks.dev**, Open Collective, GitHub Sponsors, ecosyste.ms Funds.

---

## Mechanism — thanks.dev

**thanks.dev** is an open-source **funding / routing platform** (commercial operator; SPA at thanks.dev — HTML shell notes maintainers register to become eligible). It does **not** create independent revenue; it **allocates a donor’s already-budgeted cash** across a scanned dependency tree.

**Algorithm (quoted via Canonical’s primary blog from thanks.dev’s own explanation):**  
(1) walk repositories; (2) grab manifest files; (3) collate dependency tree **up to 3 levels deep**; (4) trickle donation **breadth-first** across that tree. Donors can boost/reduce weights by language and GitHub org. Canonical states thanks.dev takes a **5%** commission for analysis, reports, outreach, and distribution.

**Sign-up bias:** only projects that register / claim can receive; unsigned dependencies in the tree get $0 for that cycle (documented in community discussion; partner writeups note maintainers often must be asked to set up payouts). This is **routing**, not replenishment under ORF taxonomy.

Meta description on thanks.dev: “Scan your dependancy tree… Maintainers can also register their projects to become eligible for funding.” Open Collective slug `thanks-dev` exists (HTTP 200) but is **not** treated here as the canonical magnitude source.

---

## Linked loop (how they fit together)

```
Company adopts Pledge norm ($2k/dev/yr + annual blog)
        │
        ├─► direct payments / foundations
        └─► thanks.dev (and/or OC / GitHub Sponsors) as allocation “easy button”
                    │
                    └─► registered maintainers in dependency graph receive split
```

**Sentry** (Innovator; multi-year reports on Pledge member page + Sentry blogs) is the clearest primary illustration: meets/exceeds Pledge minimum, publishes annually, and routes a large primary distribution through **thanks.dev** while also using Open Source Collective / Ecosyste.ms Funds and (historically) GitHub Sponsors. Sentry’s 6 Jan 2026 post calls thanks.dev “the easy button” for Pledge compliance.

**Canonical** (13 May 2025 blog on canonical.com): committed **US$120,000** over 12 months via thanks.dev at **$10,000/month**, citing the four-step algorithm and **5%** commission.

Pledge About and OSE About/FAQ also cross-link **individuals → OSE** vs **companies → Pledge**, with overlapping people (e.g. Chad Whitacre, Vlad-Stefan Harbuz) — governance adjacency, not shared custody.

---

## Prototype fit to dOSPO / OMF / ORF

| OSFL layer | What maps | What does not |
|---|---|---|
| **ORF Family D** | Voluntary, revocable corporate norm with public reporting | Primary path to PCR ≥ 1.0; Neutral Entity collection |
| **OMF** | Cash reaching maintainers/foundations | Retainer employment guarantees; SCT-backed SLAs |
| **Routing (S.1-adjacent)** | thanks.dev dependency-graph split of **existing** budgets | Independent earned replenishment |
| **dOSPO** | Annual disclose-and-renew habit (consumption-side policy light) | Non-custodial governance replaceability |
| **Family A/B/C/E** | — as Pledge/thanks.dev themselves | Structural fees, assurance products, membership dues engines, endowment spend (see OSE dossier for E) |

---

## Gaps vs OSFL Stage 0 specs

- **No Neutral Legal Entity / no fund custody** by design (Pledge) — strength for conflict avoidance; gap vs OSFL collection architecture.
- **Family D concentration / participation risk:** voluntary; members can leave (Former Member section lists dropouts); minimum is a floor, not a cost-floor cover test.
- **thanks.dev ≠ revenue:** routes corporate opex; **5%** platform take is fee-for-routing, not ORF income.
- **Sign-up bias / Gate 2:** unregistered projects invisible to payouts; site-wide donor leaderboards and Pledge homepage counters are **publisher/site counters**, not audits.
- **PCR / eight gates / ecosystem cost floor:** not claimed.
- **Rails ≠ retainers:** annual lump or monthly platform drips ≠ OMF retainer contracts with legitimacy safeguards.
- **GitHub Sponsors mothball narrative** appears on Sentry’s 2026 blog (Sentry publisher) — treat as that author’s claim when discussing rail diversification.

---

## Dated source packet

| URL | What it supports | Checked | HTTP |
|---|---|---|---|
| https://opensourcepledge.com/about/ | Problem/solution; **$2,000/dev/yr**; **does not handle funds**; eligibility; Innovator date 08 Oct 2024; OSE pointer | 2026-09-24 PT | 200 |
| https://opensourcepledge.com/join/ | Pay → publish → promote → renew steps | 2026-09-24 PT | 200 |
| https://opensourcepledge.com/members/ | Member roster; **site counters** since-launch / past-year; $/dev table; Former Members | 2026-09-24 PT | 200 |
| https://opensourcepledge.com/members/sentry/ | Sentry multi-year reported payments (member filings) | 2026-09-24 PT | 200 |
| https://thanks.dev/ / https://www.thanks.dev/ | Platform live; JS SPA (noscript warns JS required); meta: scan tree + maintainer register | 2026-09-24 PT | 200 |
| https://canonical.com/blog/canonical-thanks-dev-giving-back-to-open-source-developers | Canonical **$120k / 12 mo**; algorithm quote; **5%** commission; dated **13 May 2025** | 2026-09-24 PT | 200 |
| https://ubuntu.com/blog/canonical-thanks-dev-giving-back-to-open-source-developers | Mirror of Canonical post on Ubuntu host | 2026-09-24 PT | **503** (WAF/upstream fail this pass; use canonical.com) |
| https://blog.sentry.io/we-just-gave-750-000-dollars-to-open-source-maintainers/ | Sentry 2024: $750k budget; thanks.dev **$381,500** (+ managed total narrative) | 2026-09-24 PT | 200 |
| https://blog.sentry.io/another-year-another-750-000-to-open-source-maintainers/ | Sentry 6 Jan 2026: $750k; thanks.dev primary **$375k**; Pledge members “**$4.5M**” claim; foundations table (incl. Geomys $15k) | 2026-09-24 PT | 200 |
| https://opencollective.com/thanks-dev | Collective page live | 2026-09-24 PT | 200 |

---

## Magnitudes

| Claim | Figure | Source class | Notes |
|---|---|---|---|
| Pledge minimum | **$2,000 / FTE dev / year** | opensourcepledge.com/about | Norm, not audit |
| Members page “since launch” | **$7,354,739** | members page **site counter** | **≠ audited cash** |
| Members page “past year” | **$3,706,030** | members page **site counter** | **≠ audited cash** |
| Active member companies (slug count ex-Former section) | **37** | members page HTML structure 2026-09-24 PT | Roster snapshot; not a financial audit |
| Former members named on page | Laravel, Pixee, Browserbase, Rector | members page | Participation churn signal |
| Sentry reported payments (member page) | 2025: **$750,000** / 132 devs; 2024: **$750,000** / 129; … | opensourcepledge.com/members/sentry | Self-reported member filings |
| Sentry blog: Pledge members collective | **$4.5M** since launch | Sentry 2026-01-06 blog | **Sentry publisher** — do not stack with $7.35M counter as one audited cell |
| Sentry → thanks.dev 2025 primary | **$375,000** | Sentry 2026-01-06 blog | Publisher |
| Sentry → thanks.dev 2024 | **$381,500** (within broader platform narrative) | Sentry 2024-11-12 blog | Publisher |
| Canonical via thanks.dev | **$120,000** / 12 months @ **$10,000**/mo | Canonical 2025-05-13 blog | Publisher commitment |
| thanks.dev commission | **5%** | Canonical blog citing platform | Partner writeup; confirm on thanks.dev UI when citing as High |
| thanks.dev global GMV / maintainer count | **UNKNOWN** from non-JS primary fetch this pass | SPA | Do not invent from marketing tiles |
| Open Collective thanks-dev balance/income | **UNKNOWN** / not used | JSON endpoint noisy | Prefer Pledge/Sentry/Canonical primaries |

---

## Audience lead / don’t-lead

| Audience | Lead | Don’t-lead |
|---|---|---|
| **Foundations** | Family D norm that can steer cash **toward** maintainer-paying foundations; Pledge does not compete for custody | Counting Pledge counters as foundation revenue or PCR proof |
| **Universities** | Comparative case: voluntary disclose-and-pay vs endowment spend-rate (OSE) vs retainer firms (Geomys) | Treating $7.35M site counter as audited economics paper input |
| **Enterprises** | Clear procurement-sized ask ($2k/dev) + thanks.dev as ops path; Sentry/Canonical worked examples | Equating Pledge membership with supply-chain assurance / SLA |
| **Maintainers** | Real cash via registered payout rails; demand retainers still where appropriate | Assuming graph allocation replaces negotiation or covers unregistered work |
| **Consultants** | Best Stage 0 exhibit of **norm + router** loop (D + S.1-adjacent) | “Closed loop” language; rails ≠ replenishment |

---

## What would transfer (honest judgment)

Pledge + thanks.dev together are a **Stage 0 research candidate** for a **Family D social norm** coupled to a **dependency-aware router**. What transfers is the **measurable corporate ask**, the **no-custody transparency rule**, annual public reporting, and evidence that multiple companies will use an algorithmic split to reach deep-tree maintainers. What does **not** transfer: Neutral Entity collection, an ecosystem cost floor with Gates 1–8, independence from corporate budget cycles, or removal of sign-up bias. Under OSFL honesty spine, this loop **moves and allocates** already-raised operating spend — it does **not** replenish a treasury. Local D for any adopter: **D0** until that organization’s own receipts, eligibility policy, and (if claimed) coverage vs a published cost floor exist.
