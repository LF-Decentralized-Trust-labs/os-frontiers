# Does the 3-piece model meet the needs of open-source projects?

**Project needs, taken from the Tidelift *State of the Open Source Maintainer* reports and corroborated by other surveys, set against dOSPO governance, OMF operations and ORF collection as written**

> **Status:** OSFL research note · **Stage 0** · **no Hard Gate is passed** by ORF or by any ecosystem named here.
> **Prepared:** 9 Oct 2026 (PT). Executor pass. **Not pushed to GitHub.** The driver-based version is archived at `surveys/archive/crisis-to-model-map.driver-version.md`.
>
> **Canon.** The dOSPO v1.0, OMF v1.0 and ORF v1.0 whitepapers, with `whitepapers/ORF_ERRATA.md` controlling over `orf-v1.0.pdf`. Source: repo `LF-Decentralized-Trust-labs/os-frontiers` @ `9a82a9c` (8 Oct 2026 07:42 PT; no newer commit on main at 9 Oct). **This note proposes no change to the model.** Programs are named only as **labelled examples** of things that already fit a written mechanism. Gaps are places where those written mechanisms need such programs.
>
> **References.**
> - Section refs use PDF page numbers of `dospo-whitepaper-v1.0.pdf`, `open-maintenance-framework-omf-v1.0.pdf` and `orf-v1.0.pdf`. Repo companion documents (e.g. `omf/PROGRAM_PORTFOLIO.md`) are cited by path and are not the whitepaper.
> - Evidence IDs (S01–S30, and Tidelift blocks T1–T11) point to `surveys/oss-survey-inventory.md`.
>
> **Spine.** The needs follow the order and question structure of the Tidelift reports:
> - 2024 edition (S01, n=437; per-question n given where used) as the latest, cited from its PDF (https://assets-eu-01.kc-usercontent.com/ef593040-b591-0198-9506-ed88b30bc023/d325a56f-05be-4379-bfd1-ee4776fcad41/2024-tidelift-state-of-the-open-source-maintainer-report-.pdf), not the tidelift.com survey page, which redirects;
> - 2023 (S02, n=339) and 2021 (S03, "nearly 400" respondents; dislikes n=335, S03 p15; 2021 PDF now opened directly) for trend.
> - Page numbers are PDF pages; Black Duck OSSRA 2026 (S12) is cited as PDF page with printed page in brackets (printed = PDF − 2).
>
> Other surveys appear only to corroborate or to flag a conflict.
>
> **Policy.**
> - Retro Funding, Gitcoin, Drips and Superfluid are not replenishment, and neither is issuance (ORF §2 p14 "Routing Mirage"; §18 p42).
> - Tidelift: Sonar announced a **definitive agreement** to acquire it. No closing announcement was found on 9 Oct 2026.

---

## 1. Verdict

**Short answer.** As written, the model meets **six of eight** survey-documented project needs **for projects inside a funded ecosystem's portfolio**:
- predictable pay;
- paid security and maintenance capacity;
- shared tooling;
- more maintainers and succession;
- contributor onboarding;
- governance and legal support.

It meets **one need only partly**: recognition and relief from user burden.

It has a **gap on one**: a way for a project to receive money. The gap is that no whitepaper describes a recipient-side route; missing funding metadata on most-used packages (S22) supports the need but does not show that maintainers cannot be paid.

It **does not reach projects outside a funded ecosystem's dependency map.** That is where the Tidelift majority is likely to sit: 60% describe themselves as unpaid hobbyists, and 78% of unpaid hobbyists work ≤10 h/week (S01 p4–5, p10).

Nothing yet shows any of this working. The model is at Stage 0, and no Hard Gate is passed.

| # | Project need (Tidelift question it comes from) | Key Tidelift figure | dOSPO | OMF | ORF | **Combined, as written** |
|---|---|---|---|---|---|---|
| N1 | **Predictable, sustained pay** (paid/unpaid status; preferred payment form) | 60% describe themselves as unpaid hobbyists (p4); **81% prefer predictable monthly income** (n=344, p11) | Partial | **Addresses** | Addresses (source side) | **Addresses in portfolio · Gap outside** |
| N2 | **Paid capacity for security and maintenance work** (what pay buys; time spent; practices) | Paid maintainers 55% more likely on average to adopt security and maintenance practices (p27); security time 4%→11% (p17) | **Addresses** | **Addresses** | Partial | **Addresses** |
| N3 | **A way to receive money** (who pays) | Donation programs 25%, companies directly 5% (p15–16) | Gap | Gap | Partial (rails recognized, not provided) | **Gap** |
| N4 | **Infrastructure and tooling** (security and maintenance practices) | Reproducible builds 53% today → 82% if paid (p30, p35) | Partial | **Addresses** | not applicable | **Addresses** |
| N5 | **More maintainers and succession** (support that would have kept them; practices) | 56% of those who quit or considered quitting wanted help finding a co-maintainer (S02 p31); succession plan 13% → 63% if paid (p36) | Partial | **Addresses** | not applicable | **Addresses in portfolio** |
| N6 | **Onboarding contributors and community building** (non-financial support; community efforts) | Marketing to find contributors 75% valuable; retaining contributors 74% (S02 p33) | not applicable | **Addresses** | not applicable | **Addresses in portfolio** |
| N7 | **Recognition and relief from user burden** (dislikes, 2024; quit reasons, 2023) | Dislikes: underappreciated 48%, stress 43%, users too demanding 39% (chart), lonely 32% (p38–39); 2023 quit reason burnout 44% (S02 p30) | Partial | Partial | Gap (and a guarded risk) | **Partial** |
| N8 | **Governance, compliance and legal support** (standards; documentation practices) | No time 38% / not paid 37% as reasons not to align with standards (n=119, p13); 54% want help understanding them (n=288, p14) (S02) | **Addresses** | **Addresses** | Partial | **Addresses in portfolio** |
| — | **Reach to the long tail** (cross-cutting) | 78% of unpaid hobbyists work ≤10 h/week (p10) | Gap (§9 p24) | Partial (App C p55) | Gap | **Gap** |

**Ratings**
- **Addresses:** a named mechanism in the whitepaper text meets the need.
- **Partial:** a mechanism covers part of the need, or meets it only under conditions the text states.
- **Gap:** no mechanism in the text.
- **not applicable:** outside that component's job.

The components divide the work as follows:
- dOSPO decides;
- OMF deploys money and services;
- ORF collects net, recurring money.

Under ORF's functional separation, ORF never pays a maintainer directly. Its rating on a need reflects whether it supplies the kind of money that need requires.

---

## 2. The needs, one by one

Each need gives:
- what Tidelift measures (exact figures, PDF page);
- trend, corroboration and conflicts from other surveys;
- which project types it hits;
- how each component meets it as written;
- labelled example programs.

Project types used throughout:
- **Solo:** a single-maintainer project.
- **Small:** a few maintainers, little or no institutional backing.
- **Critical infrastructure:** high-centrality libraries and tools.
- **Ecosystem/protocol:** chain clients, SDKs, registries, shared tooling of one ecosystem.

### N1. Predictable, sustained pay

**What Tidelift measures**
- **Status:** 60% describe themselves as unpaid hobbyists (16% wouldn't want pay; 44% would like it; single choice, n=437). 24% are semi-professional and 12% professional (S01 p4–5). 36% describe themselves as paid professionals or semi-professionals (p8). On a separate multi-select question (n=421), 47% report no maintainer income at all (p13). Both figures are valid if labelled.
- **Form:** **81% prefer predictable monthly income**; 7% prefer a lump sum (n=344, p11).
- **Source:** 24% are paid by an employer as an explicit job duty, against 28% in 2023 and 27% in 2021; Tidelift says the difference is likely not statistically significant (p14).
- **Dislikes:** "not financially compensated" is the top dislike: 50% in 2024 (n=338), 52% in 2023, 49% in 2021 (p38).
- **Quitting:** the 2024 report did not ask quit reasons. In 2023, among those who quit or considered it, "not paid enough" rose to 38% from 32% (S02 p30). More income was the joint most-chosen support that might have kept them (56% in the chart, tied with co-maintainer help; 57% in the p32 text) (S02 p31–32).
- **Trend:** the self-described unpaid share has held at 60% (S02 p3). Quit-or-considered is 59% / 58% / 60% for 2021 / 2023 / 2024 (S01 p40, n=350; S03 p19). The 2024 closing narrative's "almost two-thirds" (p59) is a loose restatement; 60% is used.

**Corroborate / conflict**
- STA's spring-2024 survey of 536 maintainers: 33% unpaid and wanting pay, about 30% paid but unable to live on it (S14), roughly 63% combined (derived). This direction is consistent with Tidelift.
- STA's Fellowship evaluation restates the same survey as 77% (S15). That figure cannot be reproduced from the published results: **Unverified, not used**. Its n=6 refers to the fellows evaluated, not to the 77%.
- LF/GitHub/Harvard 2024 funding survey (LF blog, 18 Dec 2024): respondent organizations' direct financial contributions totalled $162M, of which 4% went directly to maintainers (S07). This is not a Tidelift figure, and it counts direct payments only.

**Project types:** solo and small most of all; critical-infrastructure maintainers carry the risk.

**Model as written**
- **OMF — Addresses.** Maintainer Retainer is listed in §8 Program Architecture (p23). §9 Sustainment Programs covers retainers (p24). §12 Instrument 2, continuity-oriented funding (p32), describes recurring availability funding and cites Protocol Guild and Tidelift 2024. A monthly retainer is the payment form 81% of maintainers say they prefer.
- **ORF — Addresses on the source side.** ORF exists to supply recurring, net-accounted inflows:
  - the five families (§8 p23–25);
  - Gate 3, PCR ≥ 1.0, and Gate 6, a 24-month stressed runway (§12 p31);
  - correlation classes (§13 p33).

  ORF never pays a maintainer itself.
- **dOSPO — Partial.** §7 Funding and Cost Models (p20) sets funding principles and budget caps. It does not pay people.
- **Limit:** pay reaches only projects that an ecosystem's dependency audit selects. These are chosen by centrality and inverse bus factor: OMF §14 p37–38; App A p47; App E p61, where W2 has weight 0.25.

**Labelled examples (not spec changes)**
- **Protocol Guild vesting:** OMF §8 p23 and §12 Instr. 2 p32 name it (S27). The 2025 distribution total is a later-errata candidate and is not used here (`docs/chains/pg-followups.md` §4).
- **Tidelift-style recurring payments:** OMF §12 Instr. 2 p32 cites Tidelift 2024. 19% of maintainers report Tidelift income (S01 p15). The publisher itself pays, so treat this figure with care.
- **STA Fellowship:** OMF §9 p24 cites STA milestone contracts.
- **Open Source Pledge** as an ORF Family D inflow (§8 p25): $3,756,826 in the past year, self-reported (S20).

### N2. Paid capacity for security and maintenance work

**What Tidelift measures**
- **What pay buys** (paid maintainers, n=142, p8):
  - more time on maintenance 83%;
  - research and respond to security issues and bugs 52%;
  - improve secure-development practices 51%;
  - prioritize vulnerability remediation 45%.

  Professionals vs. semi-pros on vulnerability remediation: 64% vs 36% (p9).
- **Time spent:** security is 11% of maintainer time, up from 4% in 2021; Tidelift cautions that changed answer categories may explain part of this (p17; n=378 / 327, p18). Maintenance is 50% (53% before) (p17). Seeking financial support takes about 2% (p17–18). Paid vs. unpaid: security 13% vs 10% (p19).
- **Practices:**
  - implemented: 2FA 71%, static analysis 65%, disclosure plan 52%, secrets management 46% (p24);
  - across security **and maintenance** practices, paid maintainers are 8–26 percentage points (55% on average, relative) more likely to implement them (p27);
  - 2FA was 54% in 2023 (p26);
  - 40% of those aware of the OpenSSF Scorecard have no plans to align (p21).
- **Trend:** in 2023, among maintainers with no plans to align with standards (n=119), the top reasons were "no time" (38%) and "not paid" (37%) (S02 p13–14).

**Corroborate**
- 93% of 947 audited commercial codebases contain components with no development activity in over two years (S12 PDF p27, printed p25).
- 454,648 new malicious packages appeared in the year (S11 p20–21).
- The LF/Harvard 2020 survey found 2.27% of contributor time going to security (S04 p5). It used a different construct, but the direction matches Tidelift's 2021 baseline.
- The Tidelift paid-vs-unpaid differences are correlational and self-reported.

**Project types:** critical infrastructure; ecosystem/protocol.

**Model as written**
- **dOSPO — Addresses.** §6 Security Coordination (p19).
- **OMF — Addresses.**
  - §12 Instrument 1, delivery-oriented (p31): milestone sprints; names GitHub SOSF.
  - Instrument 2 (p32): ongoing availability.
  - §8 Resilience Programs (p23).
  - §9 Operational Support Services (p24): "security audit facilitation".
- **ORF — Partial.** Family B.1 assurance and B.2 LTS/SLA (§8 p24) would have enterprises pay for exactly this work, but only after the Service Capacity Test (§10 p28) and Gate 7 (§12 p31).

**Labelled examples**
- **Alpha-Omega:** $6,155,410 across 31 grants in 2025 (S17 p26). Fits OMF §12 Instr. 1–3 and dOSPO §6.
- **GitHub Secure Open Source Fund:** $10,000 per project (S18). Named in OMF §12 Instr. 1 p31.
- **Client-paid LTS:** ORF B.2.

### N3. A way to receive money

**What Tidelift measures**
- Income sources (n=421, p15):

  | Source | Share |
  |---|---|
  | Donation programs (GitHub Sponsors, Open Collective, Patreon) | 25% (16% in 2021) |
  | Employer | 24% |
  | Tidelift | 19% |
  | Companies directly | 5% (text p16) |
  | Individuals | 5% |
  | Foundations | 3% |
  | Governments | 1% |

- Tidelift does not ask whether a project has *any* route to receive money. The need is stated from the model side: no whitepaper provides a recipient-side route. The channel mix and the funding-metadata evidence below support it.

**Corroborate**
- 3.26% of packages carry funding links (S22).
- **72.8% of the ~10,000 most-used ("critical") packages list no funding link in their metadata** (S22). This measures missing funding metadata, not an inability to receive money.
- About a third (35%) of critical-package owners are individual accounts (S22 slide 43; the slide-51 summary restates this as packages).

**Project types:** solo and small; also many critical packages.

**Model as written**
- **OMF — Gap.** §9 (p24) defines retainers, credits and support services. No mechanism gives a recipient project a legal or financial route to receive money. Fiscal hosting is not in the text. This matches ref-check item #6.
- **dOSPO — Gap.**
- **ORF — Partial.** ORF recognizes routing rails as an infrastructure category: §6 p20 stage 4; §7 p22, "moves already-collected money … No". It keeps them out of revenue (§2 p14). It does not provide recipient rails.
- **Effect:** OMF cannot pay a maintainer it cannot reach. This is where the written mechanisms (§9 retainers, App C co-funding p55–56) need an outside program.

**Labelled examples (gap fillers, not spec changes)**
- **Fiscal hosts / donation platforms** (Open Collective, GitHub Sponsors): 25% of maintainers already receive through donation programs (S01 p15).
- **thanks.dev:** one donor reaching 358 recipients (S21). This is a routing rail, not revenue.
- **ecosyste.ms funding-route data** (S22): for OMF App A audits.

### N4. Infrastructure and tooling

**What Tidelift measures**
- Maintenance practices today vs. if paid (p30, p35):

  | Practice | Today | If paid |
  |---|---|---|
  | Reproducible/verifiable builds | 53% | 82% |
  | Dependency-management process | 40% | 66% |
  | Multi-reviewer peer review | 37% | 61% |

- Signed releases / provenance: paid maintainers are 22 points more likely to have them (p27).
- 2023 support wanted for standards: "help doing the work" 34% (S02 p14).

**Corroborate**
- Packaging repositories received 29.8% ($2,929,702) of Alpha-Omega's 2025 grants (S17 p26).
- Top-3 cloud providers draw 86.4% of Maven Central downloads from 32.5% of IPs (S11 p14). Registry load is concentrated.

**Project types:** all, through shared registries and CI; ecosystem/protocol most of all.

**Model as written**
- **OMF — Addresses.**
  - §12 Instrument 3, shared infrastructure (p33).
  - §9 Infrastructure Credits (p24): "computing, storage, or tooling".
  - §8 Resilience Programs (p23).
  - App C, cross-chain shared dependency standards (p55–56).
- **dOSPO — Partial.** §7 (p20) sets funding principles; it does not provide tooling.
- **ORF — not applicable.**

**Labelled examples**
- **Sovereign Tech Agency:** €41.1M across 118 technologies (S16). OMF §9 p24 cites its milestone contracts; it fits Instr. 3 as a co-funder (App C).
- **Alpha-Omega packaging-repository grants** (S17).

### N5. More maintainers and succession

**What Tidelift measures**
- 2023, support that might have kept them, asked only of those who quit or considered quitting (n=153, S02 p31):
  - help finding another experienced maintainer to join and share responsibilities 56%;
  - help finding another experienced maintainer to "take over some of my projects" 40%;
  - diverse collaborators 33%.
- 2023, non-financial support rated valuable: succession planning / finding co-maintainers 71% (S02 p33).
- 2024 practices: a succession plan is held by 13% today; 63% including those who would provide one if paid (stated intent, n=353; p36).
- What pay buys: "bring on additional maintainers" 26% (p8).
- **Graying:** maintainers under 26 fell from 25% to 12% to 10% (p58). 45% have maintained for more than 10 years (p59).
- 44% are solo maintainers (S02 p26, n=326). In 2024, solo maintenance is 61% among unpaid hobbyists vs 26% among paid maintainers (S01 p5–6).

**Corroborate / conflict**
- Among the top 50 non-npm projects, 17% have one developer and 40% have one or two developers doing >80% of commits (S06 p2).
- 136 developers wrote >80% of new code in the top 50 (S05 p20).
- **Conflict:** STA's survey reports 31% working alone (S14), vs Tidelift's 44%. The samples differ.

**Project types:** solo and critical infrastructure.

**Model as written**
- **OMF — Addresses for the portfolio.**
  - §8 Resilience Programs, "succession planning" (p23).
  - §8 Contributor Pathways (p23) and §10 (p26–27).
  - §11 lifecycle stages on attracting co-maintainers and succession (p28).
  - §14 centrality (p37–38).
  - App E inverse bus factor (p61).
  - App B ops spec (p51–52).
- **dOSPO — Partial.** It governs which programs run (§5 p16).
- **ORF — not applicable.**
- **Companion docs (not whitepaper):** the funded co-maintainer rule is in `omf/RISK_MITIGATION_PROTOCOLS.md`, not the OMF PDF.

**Labelled examples**
- **CNCF/LFX Mentorship:** 25 mentees became maintainers since 2020, cited in OMF §10 p26.
- **Protocol Guild membership registry:** OMF §12 p32–33.
- **STA Fellowship** (S15).

### N6. Onboarding contributors and community building

**What Tidelift measures**
- 2023 non-financial support rated valuable (n=261, S02 pp. 32–33):
  - improving user/contributor experience 89%;
  - documentation 87%;
  - marketing to find contributors 75%;
  - retaining contributors 74%.
- 2023 community efforts already made (S02 p34–35):
  - welcoming atmosphere 67%;
  - onboarding/outreach 35%;
  - mentorship (Outreachy, GSoC) 28%;
  - none 17%.
- 2024: a contributor guide is in place on 61% of projects (p32).
- **Tension:** 66% of maintainers aware of xz agree they are less trusting of pull requests from non-maintainer contributors or vet them more carefully (n=307, p43). Onboarding has to coexist with vetting.

**Project types:** small and ecosystem/protocol.

**Model as written**
- **OMF — Addresses.**
  - §10 Contributor Pathways (p26–27): "Recognize contributor milestones" (p27).
  - App D, Web3 contributor pathway adaptations (p58).
  - §8 Incubation (p23).
- **dOSPO and ORF — not applicable.**

**Labelled examples**
- **CNCF LFX Mentorship / GSoC / Outreachy:** OMF §10 p26.
- **Ethereum Protocol Fellowship** and **Polkadot Fellowship:** OMF §10 p26–27.

### N7. Recognition and relief from user burden

**What Tidelift measures**
- **What maintainers dislike** (S01 p38–39; n=338 in 2024, 253 in 2023, 335 in 2021, S03 p15):

  | Dislike | 2024 | 2023 | 2021 |
  |---|---|---|---|
  | Underappreciated / thankless | 48% | not asked | 40% |
  | Adds to personal stress | 43% | 54% | 45% |
  | Users too demanding | 39% (chart only) | 36% | 37% |
  | Can be lonely | 32% | 42% | 36% |

  These are dislikes, not quit reasons. The 2024 report did not ask why maintainers quit.
- **Why maintainers quit or considered quitting** (2023, latest edition that asked; S02 p30): other priorities 54%, lost interest 51%, burnout 44%, not paid enough 38%, took too much time 36%. The base is those who quit or considered quitting; the n captions disagree (265 vs 349).
- 2023 enjoyment: recognition 57%, up from 43% (S02 p24).
- 2023: "efforts to address burnout" were made on 20% of projects (S02 p35).
- Conflict-resolution process: 17% today vs 50% if paid (p36).

**Corroborate**
- The Heath 2025 burnout report names toxic behaviour, hyper-responsibility and workload as drivers alongside pay (S29).
- S15 reports reduced burnout among the 6 Fellows evaluated (qualitative, n=6).

**Project types:** all; popular solo projects most of all.

**Model as written**
- **OMF — Partial.**
  - §9 Coordination Support (p24): "community management and communication … reduces social overhead that contributes heavily to burnout".
  - §10 milestone recognition (p27).
  - §16 measures burnout (p42); App B weights burnout at 20% (p52).
  - **No mechanism for demanding or hostile users.**
- **dOSPO — Partial.** §9 (p24) names bureaucratic accretion as "the most common failure mode" of a coordination layer. That limits process load on maintainers but does not address users.
- **ORF — Gap, and a guarded risk.** B.2 SLAs put a price on maintainer availability, and stress is the #3 dislike. ORF §10 p28 and §18 p42 ("Liability Without Capacity") are written to guard against this.

**Labelled examples**
- **GitHub SOSF cohort structure:** OMF §9 p24 models operational support on it.
- **CNCF mentorship** (§10).
- **CHAOSS/STA impact toolkit** (S23): for OMF §16 measurement.
- **Toxic-user relief:** no example fits a written mechanism. It remains a Gap.

### N8. Governance, compliance and legal support

**What Tidelift measures**
- 39% dislike being "asked to comply with requirements I don't have time for" (2024 chart, p38; 38% in S02 p26).
- 2023, why maintainers don't align with standards: no time 38%, not paid 37%, don't understand which apply 29% (S02 p13–14).
- 2023, support wanted: help understanding 54%, getting paid 47% (S02 p14).
- 2024 documentation: code of conduct 53% (p32); conflict-resolution process 17% → 50% if paid (p36).

**Corroborate**
- Only 26% of organizations have an OSPO (S09 p5), so consumers often lack a counterpart for compliance.

**Project types:** small and critical infrastructure.

**Model as written**
- **dOSPO — Addresses.** §5 Governance Architecture and Enforcement (p16); §6 (p19).
- **OMF — Addresses for the portfolio.**
  - §8 Operational Support (p23): "security audit facilitation, legal review, documentation support, governance assistance".
  - §9 Operational Support Services (p24): "legal review, compliance documentation".
- **ORF — Partial.** ORF's neutral legal entity (§9 p26) serves collection, not projects. Family B.1 buyers fund assurance artefacts (§8 p24).

**Labelled examples**
- **GitHub SOSF training cohort:** OMF §9 p24.
- **OpenSSF Scorecard / SSDF guidance** (S01 p20).
- **Foundation-led stewardship:** OMF §12 Cost of Coordination (p34) prices it as including "legal standing … compliance". This is an operator model, not a project service.

---

## 3. Where the written mechanisms need programs (gaps, not spec changes)

| Gap | Need | Written mechanism that needs filling | Labelled example that would fill it |
|---|---|---|---|
| G1 Recipient rails | N3 | OMF §9 p24 retainers; App C p55–56 co-funding | Fiscal hosts / donation platforms; thanks.dev (routing); ecosyste.ms data |
| G2 Long-tail reach | N1, N3 | OMF App A p47 audit; §12 Instr. 3 p33; App C p55–56. dOSPO excludes small ecosystems (§9 p24); minimum cost $450K–$1.2M/yr (§7 p20–21) | Public co-funders (STA); breadth rails |
| G3 User burden and toxicity | N7 | OMF §9 Coordination Support p24; §16 p42 | Community-management programs. **No written mechanism for hostile users** |
| G4 Baseline | all | OMF §16 p42; ORF Gate 1 §12 p31 | Re-ask the Tidelift questions in-portfolio; CHAOSS/STA toolkit (S23) |
| G5 Cash evidence | all | ORF Gates 1–8 §12 p31; D0–D5 scale §14 | Any paid pilot under a charter |

---

## 4. Supporting note: where the money comes from (ORF examples; chains as secondary context)

- **ORF collection examples, labelled (§8 p23–25):**
  - A.1 protocol fee slice before burn/payout;
  - A.3 canonical fees + Family E endowment (ENS pattern; per errata, yield covers about a fifth of operating expenses);
  - B.1/B.2 assurance and LTS;
  - C membership/certification;
  - D Open Source Pledge and Protocol Guild-style pledges;
  - E endowment income.
- **Not replenishment:** Gitcoin, Optimism Retro Funding, Drips, Superfluid and issuance. These are allocation, routing or dilution.
- **Chains, brief:**
  - The pack's top-10 review found that fees are burned, paid to validators/miners or used for buybacks.
  - No top-10 chain has taken a routing decision for OSS, and none closes POSM P6 (`chains/top10-chains-orf-alignment.md` §5; `chains/posm-cycle-chain-map.md`).
  - So Family A, the source that would most directly fund N1, is D0 for those chains.
  - This is context for N1's source side only.

---

## 5. Conflicts, weak methods, Unverified

- **Tidelift internal inconsistencies:**
  - **Resolved:** 60% quit/considered (p40, n=350) is used; "almost two-thirds" (p59) is loose narrative.
  - **Resolved:** 60% unpaid hobbyists (single choice, n=437, p4) and 47% no maintainer income (multi-select, n=421, p13) answer different questions; both are used, labelled.
  - **Resolved:** 2023 "not compensated" is 52%. Both 52% and 53% appear in the S02 p26 text; the p25 chart shows only "+3%", and S01 p38 confirms 52%.
  - **Resolved:** users too demanding is 37% (2021), 36% (2023), 39% (2024, chart only). The S02 p26 text swaps the earlier years.
  - 2021 dislikes n=335 (S03 p15); the 2024 report's "n=253 (2021)" caption is an error.
  - 2023 quit-question n is Unverified (captions give 265 and 349).

  All samples are self-selected. Tidelift is also a payer of maintainers.
- **OMF whitepaper vs Tidelift 2024:** OMF writes "59% … considered quitting". Tidelift 2024 gives 60% quit-or-considered; 59% was the 2021 figure. Noted as evidence only.
- **STA:** both figures come from the same spring-2024 survey of 536 maintainers. 33% unpaid wanting pay + ~30% underpaid (~63%, derived) is used. The evaluation report's 77% (S15) is **Unverified and not used**; n=6 is the number of fellows evaluated.
- **Solo maintainers:** 44% (S02 p26) vs 31% (S14). Different samples and questions; a range is reported.
- **S07 vs S10:** different constructs; no ratio should be computed.
- **Protocol Guild membership:** not a conflict. It was 196 as of 22 May 2026 and 190 as of 5 Aug 2026 (Q3 audit); use 190. ">$80M commitments" is **Unverified**.
- **Unverified:**
  - thanks.dev aggregate totals;
  - Eghbal *Working in Public* (not opened);
  - AIxponential "44% … burnout", "8.8 h/week";
- **Context only:** JetBrains 2023 "73% of developers have experienced burnout" is confirmed at source, but it covers all developers (26,348 respondents), not maintainers. It is not used as maintainer evidence.
- **Tidelift corporate status:** definitive agreement only; closing not confirmed.

## 6. Reference corrections applied in this pass (see `surveys/section-2.7-ref-check.md`, Table B)

| Was | Now |
|---|---|
| OMF App A p48 | p47 |
| OMF App C p56 | p55–56 |
| "OMF Program 4 / Program 2" | OMF §8 p23 (Resilience Programs / Code Bounties). The numbering exists only in repo `omf/PROGRAM_PORTFOLIO.md` |
| "Protocol 1–4" cited as OMF | Repo `omf/RISK_MITIGATION_PROTOCOLS.md`, not the whitepaper |
| dOSPO "zero custody" | Attributed to repo `dospo/START_HERE.md` / `dospo/NON_POWERS.md` |

---

## Changelog

**9 Oct 2026, ~05:35–06:05 PT: Researchy page-check fixes applied** (`researchy-section2-pagecheck.md`, `researchy-survey-factcheck.md`, `data/tidelift-page-index.md`)
- S12 93% → PDF p27 (printed p25).
- 55% → security **and** maintenance practices.
- "Only 36% paid at all" → "36% describe themselves as paid", with 47% no maintainer income (p13, multi-select, n=421).
- 2023 56% / 40%: base is those who quit or considered quitting (n=153); wording "take over some of my projects".
- More income: joint most-chosen (56% chart / 57% text).
- N7 reframed: 2024 = dislikes; quit reasons from 2023 p30 (2024 did not ask). Dislike table filled for 2021/2023 (36/37, 42/36).
- $162M / 4%: LF/GitHub/Harvard (LF blog, 18 Dec 2024), respondent organizations' direct contributions; not Tidelift.
- N3 rescoped: the gap is no recipient-side route in the whitepapers; 72.8% = no funding link in package metadata (supporting evidence). S22 35% reworded as owners.
- n fixes: 2023 standards reasons n=119; 2021 dislikes n=335 (the 2024 caption's 253 is an error); 2023 quit-question n Unverified.
- Scope: "describe themselves as unpaid hobbyists"; Census III top 50 non-npm; stated-intent "if paid"; employer-pay change not significant; security-time category caveat; xz wording.
- §5 contradictions marked Resolved:
  - 60% (p40);
  - 60% vs 47% different questions;
  - 2023 52%;
  - 37/36/39.
- STA: same 536-respondent survey; ~63% derived; 77% Unverified, not used; n=6 = fellows.
- Protocol Guild 196 → 190: dated values, not a conflict.
- JetBrains 73% confirmed but covers all developers; context only.
- Still Unverified: thanks.dev totals, Protocol Guild >$80M, AIxponential 44% / 8.8 h.
- Tidelift 2024 cited by PDF URL; 2021 cited directly (S03).
- **Verdict:** unchanged (6/8 for portfolio projects; N3 Gap; N7 Partial; long tail out of reach; Stage 0). No rating moved: N3 remains a Gap because no whitepaper has a recipient-side route, whatever the metadata shows, and N7 remains Partial on dislike evidence plus 2023 burnout as a quit reason.

**9 Oct 2026, earlier:** restructured needs-first on the Tidelift spine; whitepaper ref corrections in §6. The driver-based version is archived.
