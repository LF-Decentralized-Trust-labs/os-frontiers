# Closing the Loop: Governance, Maintenance Deployment, and Replenishment for Open Infrastructure

> **OSFL Release-1 Research Draft** · Open Source Frontiers Lab (LF Decentralized Trust labs · `os-frontiers`)  
> **Series:** dOSPO (governance) · OMF (maintenance deployment) · ORF (replenishment) — ORF dated 18 Aug 2026 completes the trilogy; each pillar usable alone.  
> **Author:** Christian Taylor · Open Source Frontiers Lab synthesis pack  
> **Affiliation options:** Open Source Cowboy Consulting; LF Decentralized Trust Labs (Stage 0 Research Candidate)  
> **Date:** 2026-09-24 America/Los_Angeles · **Revised:** 2026-10-09 PT (Tidelift needs map folded in as §2; later sections renumbered). Pre-revision copy: `synthesis/archive/release1-research.pre-needs-foldin-2026-10-09.md`  
> **Status:** **Stage 0** research candidate. No Hard Gate marked passed. Where `ORF_ERRATA.md` differs from `orf-v1.0.pdf`, **errata controls**.  
> **Evidence pack:** `claims/orf-claims-validated.md` (141; SUPPORTS 99 · PARTIAL 35 · ERRATA 5 · CONFLICTS 2; Researchy delta: 0 flips); `use-cases/web2-web3-prototypes.md`; `use-cases/web2-web3-prototypes-expansion.md` (N1–N12); `use-cases/researchy-validation.md`; `claims/implementation-validation.md`; `synthesis/gaps.md`; `surveys/oss-survey-inventory.md` (S01–S30); `surveys/crisis-to-model-map.md`; `surveys/release1-section-2-survey-crisis-map.md`; `surveys/release1-section-2.7-closing-the-gaps.md`  
> **Integrity rule:** No fabricated citations, expert quotes, or unaudited cash totals.

---

## Abstract

**Verdict.** For projects inside a funded ecosystem's portfolio, the dOSPO (who decides), OMF (how money goes out) and ORF (how money comes back) whitepapers as written cover six of the eight needs that the Tidelift *State of the Open Source Maintainer* reports identify (N1–N8, in the order of Tidelift's 2024 questions, §2): predictable pay; paid security and maintenance capacity; infrastructure and tooling; more maintainers and succession; contributor onboarding; and governance, compliance and legal support. **N3, a way to receive money, is a gap:** no whitepaper describes a recipient-side route by which a project can receive money. **N7, recognition and relief from user burden, is partial.** Small projects outside a funded ecosystem's portfolio (the long tail) are not reached. That is where most of the 60% who describe themselves as unpaid hobbyists are likely to be [S01, pp. 4–5, 10], and dOSPO §9 (p. 24) says a dOSPO is inappropriate for small, experimental ecosystems. The whitepapers and errata are the specification; programs and chains are examples only.

§2.7 sets out proposals need by need. Four of them are **Extensions**: proposals that go beyond the published text. They are examples, not spec changes, and would need author review: G4, a fiscal host or other recipient payment route, for N3; R3 (named credit for maintainers) and R5 (moderation and code-of-conduct support) for N7; and G5, a shared dOSPO for several small ecosystems, for N8. The other proposals apply mechanisms the text already defines. Gaps are recorded, not closed; nothing in §2.7 changes the specification.

The rest of the paper supports the verdict: the three-pillar model and Minimum Viable ORF (§3); Web2/Web3 prototypes mapped as examples (§4), including a short note on the ten largest chains as a possible source of N1 money, where no chain closes the ORF loop (§4.3); the 141-claim validation pass under errata discipline (§5); feasibility notes (§6); an implementation path (§7); and risks and a research agenda (§8). Every rating describes design fit, not observed results. **Release 1 is at Stage 0: no ecosystem reviewed here clears all eight Hard Gates or demonstrates PCR ≥ 1.0 under ORF rules, and no Hard Gate is passed.** Running ORF (MV-ORF) is deliberately separable from claiming self-sustainability.

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

### 1.5 The question for Release 1

**The answer.** For projects inside a funded ecosystem's portfolio, the dOSPO, OMF and ORF whitepapers as written cover six of the eight needs that the Tidelift maintainer reports identify (N1–N8, in Tidelift's 2024 order). N3 (a way to receive money) is a gap, because no whitepaper describes a recipient-side route by which a project can receive money. N7 (recognition and relief from user burden) is partial. Small projects outside a funded ecosystem's portfolio (the long tail) are not reached. That is where most of the 60% who describe themselves as unpaid hobbyists are likely to be [S01, pp. 4–5, 10], and dOSPO §9 (p. 24) says a dOSPO is inappropriate for small, experimental ecosystems. The model is at Stage 0, with no Hard Gate passed. **Handoff to §2.** §2 sets out the evidence need by need. §2.7 lists the proposals, including four Extensions: G4 for N3; R3 and R5 for N7; G5 for N8. These are proposals given as examples, not spec changes, and would need author review. §3 onward describes the model and its evidence.

---

## 2. What Open Source Projects Need, and How Far the Three-Part Model Meets It

### 2.1 Finding

This section asks whether the three-part model meets the needs that open source projects report:
- the decentralized Open Source Program Office (dOSPO) for governance;
- the Open Maintenance Framework (OMF) for operations;
- the Open Replenishment Framework (ORF) for collection.

The needs are taken from the Tidelift *State of the Open Source Maintainer* reports and set out in the order of Tidelift's own questions. Other surveys are used only to corroborate or qualify them.

The model is read strictly as written in the dOSPO, OMF and ORF version 1.0 whitepapers, with the ORF errata controlling. No change to the model is proposed. Where a need has no written mechanism, this section records a gap; the four Extensions in §2.7 are labelled examples of what could fill those gaps, not spec changes.

The answer is qualified.

**What the model meets.** For projects inside a governed ecosystem's funded portfolio, the whitepapers contain a named mechanism for six of the eight needs identified:
- predictable pay;
- paid security and maintenance capacity;
- shared infrastructure and tooling;
- additional maintainers and succession;
- contributor onboarding;
- governance, compliance and legal support.

The fit on payment form is close. Eighty-one percent of maintainers say they prefer predictable monthly income [S01, p. 11], and OMF's retainers and continuity instrument describe such income.

**What it meets only in part.** Recognition and relief from user burden. OMF provides coordination support and measures burnout, but no whitepaper addresses demanding or hostile users.

**Where it has a gap.** A means for a project to receive money. No whitepaper describes a recipient-side route, such as fiscal hosting, by which a project can receive a retainer. Survey data supports the need without measuring it directly: 72.8% of the roughly 10,000 most-used packages list no funding link in their metadata [S22]. That shows a missing route in the metadata, not that maintainers cannot be paid.

**Reach.** The model does not reach projects outside a funded ecosystem's dependency map. On Tidelift's figures, that is where most of the 60% who describe themselves as unpaid hobbyists are likely to be [S01, pp. 4–5, 10].

Because the model is at Stage 0, every positive rating below describes design fit, not observed results.

### 2.2 Evidence base and method

**The Tidelift reports.** The needs taxonomy is built on:
- the 2024 report (437 respondents);
- the 2023 report (339 respondents);
- the 2021 report ("nearly 400" respondents; 335 on the dislikes question), cited directly [S03, pp. 2, 15].

The reports' question structure gives the order:
- paid or unpaid status and preferred payment;
- what payment changes;
- who pays;
- how time is spent;
- security and maintenance practices;
- what maintainers dislike (2024, 2023, 2021);
- why they quit or consider quitting (asked in 2023 and 2021, not in 2024);
- what support they say they need.

**Caveats.** The samples are self-selected, and per-question bases vary; the base is given where it matters. Where a report's chart and text disagree, the figure that agrees with the other editions is used: 52% for 2023 "not compensated" [S02, p. 26]; 37%, 36% and 39% for "users too demanding" in 2021, 2023 and 2024 [S03, p. 15; S02, p. 25, chart; S01, p. 38, chart]. The 2024 report's closing narrative says "almost two-thirds" have quit or considered quitting [S01, p. 59]; the measured figure, 60% [S01, p. 40], is used. The 2024 report has two different pay questions: 60% describe themselves as unpaid hobbyists (single choice, n=437) [S01, p. 4], and 47% report no maintainer income at all (multi-select, n=421) [S01, p. 13]. Both are valid if labelled. Tidelift also pays maintainers, and its corporate status is currently subject to a definitive agreement announced by Sonar.

**Other sources.** Corroborating sources are drawn from the inventory `surveys/oss-survey-inventory.md` (S01–S30):
- the Census II and III studies;
- the Sovereign Tech Agency survey;
- the Linux Foundation funding and OSPO reports;
- Sonatype, Black Duck;
- ecosyste.ms.

**Citation.** Figures cite the inventory ID and PDF page; where a printed page differs, both are given. The Tidelift 2024 report is cited from its PDF (https://assets-eu-01.kc-usercontent.com/ef593040-b591-0198-9506-ed88b30bc023/d325a56f-05be-4379-bfd1-ee4776fcad41/2024-tidelift-state-of-the-open-source-maintainer-report-.pdf), not the tidelift.com survey page, which now redirects. Whitepaper references give section and PDF page.

### 2.3 Needs assessment

| Need | Survey evidence | dOSPO | OMF | ORF | Combined |
|---|---|---|---|---|---|
| **N1 Predictable, sustained pay** | 60% describe themselves as unpaid hobbyists [S01, pp. 4–5]; 81% prefer predictable monthly income (n=344) [S01, p. 11]; lack of pay the leading dislike at 50% [S01, p. 38] | Partial (§7, p. 20) | Addresses (§8, p. 23; §9, p. 24; §12 Instrument 2, p. 32) | Addresses, source side (§8, pp. 23–25; §12, p. 31) | Addresses within portfolio; gap outside |
| **N2 Paid security and maintenance capacity** | Security work 11% of time, from 4% in 2021 [S01, p. 17]; paid maintainers on average 55% more likely to adopt security and maintenance practices [S01, p. 27] | Addresses (§6, p. 19) | Addresses (§12 Instruments 1–2, pp. 31–32; §9, p. 24) | Partial (§8 B.1/B.2, p. 24, gated by §10, p. 28) | Addresses |
| **N3 A way to receive money** | Donation programs 25%, companies directly 5% [S01, pp. 15–16]; 72.8% of the most-used packages list no funding link in metadata [S22] | Gap | Gap | Partial (rails recognized, §7, p. 22) | Gap |
| **N4 Infrastructure and tooling** | Reproducible builds 53% today, 82% if paid [S01, pp. 30, 35] | Partial (§7, p. 20) | Addresses (§12 Instrument 3, p. 33; §9, p. 24) | not applicable | Addresses |
| **N5 More maintainers and succession** | 56% of those who quit or considered quitting would have valued help finding a co-maintainer [S02, p. 31]; succession plans 13% today, 63% if paid [S01, p. 36] | Partial (§5, p. 16) | Addresses (§8, p. 23; §10, pp. 26–27; §14, pp. 37–38; App. E, p. 61) | not applicable | Addresses within portfolio |
| **N6 Onboarding contributors** | Help marketing to find contributors valued by 75%, retaining contributors by 74% [S02, p. 33] | not applicable | Addresses (§10, pp. 26–27; App. D, p. 58) | not applicable | Addresses within portfolio |
| **N7 Recognition and relief from user burden** | Dislikes (2024): underappreciated 48%, stress 43%, demanding users 39% (chart), loneliness 32% [S01, pp. 38–39]; quit reason (2023): burnout 44% [S02, p. 30] | Partial (§9, p. 24) | Partial (§9 Coordination Support, p. 24; §10, p. 27; §16, p. 42) | Gap; B.2 risk guarded (§10, p. 28; §18, p. 42) | Partial |
| **N8 Governance, compliance and legal support** | 54% wanted help understanding security standards [S02, p. 14] | Addresses (§5, p. 16) | Addresses (§8, p. 23; §9, p. 24) | Partial (§9, p. 26) | Addresses within portfolio |
| **Reach to the long tail** | 78% of unpaid hobbyists work ten hours a week or less [S01, p. 10] | Gap (§9, p. 24) | Partial (App. C, pp. 55–56) | Gap | Gap |

*Addresses:* a named mechanism in the whitepaper meets the need.
*Partial:* a mechanism meets part of the need, or meets it only under stated conditions.
*Gap:* no mechanism.

ORF never pays maintainers directly. Its rating reflects whether it supplies the kind of money a need requires.

### 2.4 The needs in detail

**N1. Predictable, sustained pay.**
- *Evidence.* In 2024, 60% of maintainers described themselves as unpaid hobbyists: 16% did not want payment and 44% would have liked it [S01, pp. 4–5]. Thirty-six percent describe themselves as paid professionals or semi-professionals [S01, p. 8]; on a separate multi-select question, 47% report receiving no maintainer income at all [S01, p. 13]. Asked how they would prefer to be paid, 81% chose predictable monthly income and 7% a one-time payment (n=344) [S01, p. 11]. Employer-paid maintenance was 24% in 2024, against 28% in 2023 and 27% in 2021; the report notes that the difference is likely not statistically significant [S01, p. 14]. Not being paid was the leading dislike, at 50% (49% in 2021, 52% in 2023; n=338) [S01, p. 38]. The 2024 report did not ask why maintainers quit. In the 2023 report, among those who had quit or considered quitting, "not paid enough" rose from 32% to 38% [S02, p. 30].
- *Corroboration.* In the Sovereign Tech Agency's spring-2024 survey of 536 maintainers, 33% were unpaid but wished to be paid and about 30% were paid but unable to live on it [S14], roughly 63% combined (derived). In the 2024 open source funding survey by the Linux Foundation, GitHub and Harvard, respondent organizations' direct financial contributions totalled $162 million, of which 4% was paid directly to maintainers [S07]. This counts direct payments only; money paid to foundations and contractors may also reach maintainers.
- *Model.* OMF's Maintainer Retainer (§8, p. 23), its sustainment retainers (§9, p. 24) and its continuity-oriented funding instrument (§12, p. 32) describe exactly this form of income. ORF exists to make such commitments fundable from recurring, net-accounted inflows, tested against a 24-month stressed runway (§12, p. 31).

**N2. Paid capacity for security and maintenance work.**
- *Evidence.* Paid maintainers report that payment let them spend more time on maintenance (83%), respond to security issues and bugs (52%), improve secure-development practices (51%) and prioritize vulnerability remediation (45%) [S01, p. 8]. Security work rose from 4% of maintainers' time in 2021 to 11% in 2024; the report cautions that changed answer categories may account for part of the rise [S01, p. 17]. Across the security and maintenance practices surveyed, paid maintainers were 8 to 26 percentage points (on average 55%) more likely to have implemented them [S01, p. 27]. These are correlational, self-reported differences. In 2023, the leading reasons given by maintainers with no plans to align with security standards were lack of time (38%) and lack of pay (37%) (n=119) [S02, pp. 13–14].
- *Corroboration.* In Black Duck's audit of 947 commercial codebases, 93% contain components with no development activity in over two years [S12, PDF p. 27 (printed p. 25)].
- *Model.* dOSPO coordinates security (§6, p. 19). OMF funds it through delivery-oriented and continuity-oriented instruments (§12, pp. 31–32) and security audit facilitation (§9, p. 24). ORF's assurance and long-term-support families (§8, p. 24) could have enterprises pay for this work, but only after the Service Capacity Test (§10, p. 28).

**N3. A way to receive money.**
- *Evidence.* Tidelift records how maintainers are paid, not whether they can be:
  - donation programs 25%;
  - employers 24%;
  - Tidelift 19%;
  - companies directly 5%;
  - individuals 5%;
  - foundations 3%;
  - governments 1% [S01, pp. 15–16].
- *Corroboration.* The ecosyste.ms dataset finds funding links on 3.26% of packages. Of the roughly 10,000 most-used ("critical") packages, 72.8% list no funding link in their metadata [S22]. This measures missing funding metadata, not an inability to receive money, but it indicates how often a funder would find no route to pay.
- *Model.* The gap is in the whitepapers: none describes a recipient-side route. ORF recognizes routing rails as infrastructure that moves money already collected (§7, p. 22) and does not count them as revenue (§2, p. 14). Neither OMF nor dOSPO provides a way for a project without a legal or financial home to receive a retainer. This is a gap in the model as written.

**N4. Infrastructure and tooling.**
- *Evidence.* Reproducible or verifiable builds are in place on 53% of projects. A dependency-management process is in place on 40% and multi-reviewer peer review on 37%. Counting maintainers who say they would implement them if paid, the shares rise to 82%, 66% and 61% (stated intent, n=359) [S01, pp. 30, 35].
- *Corroboration.* Packaging repositories received 29.8% of Alpha-Omega's 2025 grants [S17, p. 26].
- *Model.* OMF's shared-infrastructure instrument (§12, p. 33) and infrastructure credits (§9, p. 24) address this at portfolio level.

**N5. More maintainers and succession.**
- *Evidence.* The 2023 report asked only maintainers who had quit or considered quitting what support might have kept them (n=153) [S02, p. 31]:
  - 56% chose help finding another experienced maintainer to join the project and share responsibilities;
  - 40% chose help finding another experienced maintainer to take over some of their projects.

  Only 13% have a succession plan; including those who would provide one if paid, the share is 63% (stated intent) [S01, p. 36]. The share of maintainers under 26 fell from 25% to 10% across the three surveys [S01, p. 58].
- *Corroboration.* Among the top 50 non-npm projects in Census III, 17% had one developer, and 40% one or two developers, accounting for more than 80% of commits [S06, p. 2]. The Sovereign Tech Agency's survey reports 31% working alone [S14], against Tidelift's 44% solo maintainers in 2023 [S02, p. 26]. Tidelift 2024 reports solo maintenance for 61% of unpaid hobbyists and 26% of paid maintainers [S01, pp. 5–6]. The samples and questions differ, so a range is reported.
- *Model.* OMF provides:
  - succession planning under Resilience Programs (§8, p. 23);
  - contributor pathways (§10, pp. 26–27);
  - selection by dependency centrality and inverse bus factor (§14, pp. 37–38; App. E, p. 61).

**N6. Onboarding contributors and community building.**
- *Evidence.* In 2023, maintainers rated these forms of non-financial support valuable (n=261) [S02, pp. 32–33]:
  - improving the user and contributor experience (89%);
  - documentation (87%);
  - help marketing to find contributors (75%);
  - help retaining contributors (74%).

  Sixty-six percent of maintainers aware of the xz incident agreed that they are less trusting of pull requests from non-maintainer contributors or vet them more carefully (n=307) [S01, p. 43], so onboarding has to be balanced against vetting.
- *Model.* OMF's contributor pathways (§10, pp. 26–27), including recognition of contributor milestones (p. 27), and its Web3 pathway adaptations (App. D, p. 58).

**N7. Recognition and relief from user burden.**
- *Evidence: what maintainers dislike (2024, n=338)* [S01, pp. 38–39]:
  - 48% found the work underappreciated or thankless (40% in 2021);
  - 43% said it added to personal stress (54% in 2023, 45% in 2021);
  - 39% found users too demanding (chart; 36% in 2023 [S02, p. 25, chart], 37% in 2021 [S03, p. 15]);
  - 32% found it lonely (42% in 2023, 36% in 2021).

  These are dislikes, not reasons for quitting. The 2024 report did not ask why maintainers quit.
- *Evidence: why maintainers quit or considered quitting (2023, latest available)* [S02, p. 30]: other priorities 54%, lost interest 51%, burnout 44%, not paid enough 38%. The base is maintainers who had quit or considered quitting; the report's sample-size captions for this question are inconsistent.
- *Corroboration.* Heath's 2025 report on burnout in open source identifies toxic behaviour, hyper-responsibility and workload alongside difficulty getting paid [S29].
- *Model.* OMF provides coordination support intended to reduce "social overhead that contributes heavily to burnout" (§9, p. 24), recognizes contributor milestones (§10, p. 27) and measures burnout (§16, p. 42). No whitepaper addresses demanding or hostile users. ORF's sale of service-level guarantees could add pressure; its Service Capacity Test and failure-mode safeguards are written to prevent selling capacity that does not exist (§10, p. 28; §18, p. 42).

**N8. Governance, compliance and legal support.**
- *Evidence.* Thirty-nine percent of maintainers dislike being asked to comply with requirements they lack time for (chart) [S01, p. 38]. In 2023, 54% wanted help understanding which security standards apply (n=288) [S02, p. 14]. A conflict-resolution process exists on 17% of projects; including those who would adopt one if paid, the share is 50% (stated intent) [S01, p. 36].
- *Model.* dOSPO's governance architecture (§5, p. 16). OMF's operational support: "security audit facilitation, legal review, documentation support, governance assistance" (§8, p. 23; §9, p. 24).

### 2.5 Existing programs that fit the model as written

The programs below are **examples**. They are not recommendations and imply no change to the specifications. Each already fits a mechanism named in the whitepapers.

| Example | Mechanism it fits | Needs | Evidence |
|---|---|---|---|
| Protocol Guild vesting registry | OMF §8, p. 23; §12 Instrument 2, p. 32 | N1, N5 | $7,231,668 raised from 6,202 unique donors in 2025 [S27, Validated] |
| Sovereign Tech Agency contracts and Fellowship | OMF §9, p. 24; §12 Instrument 3, p. 33; App. C, pp. 55–56 | N1, N4, N5 | €41.1 million across 118 technologies [S16] |
| Alpha-Omega | OMF §12 Instruments 1–3; dOSPO §6, p. 19 | N2, N4 | $6,155,410 in 31 grants in 2025 [S17, p. 26] |
| GitHub Secure Open Source Fund | OMF §12 Instrument 1, p. 31; §9, p. 24 | N2, N8 | $10,000 per project [S18] |
| CNCF / LFX Mentorship, GSoC, Outreachy | OMF §10, p. 26 | N5, N6 | Cited in OMF §10 |
| Donation platforms and fiscal hosts | Fills the N3 gap ahead of OMF §9 retainers | N3 | 25% of maintainers already paid through donation programs [S01, p. 15] |
| Client-paid assurance and long-term support | ORF §8 B.1/B.2, p. 24; §10, p. 28 | N2 (source) | Abandonment debt [S12, PDF p. 27] |
| Open Source Pledge | ORF §8 Family D, p. 25 | N1 (source) | $3,756,826 in the past year, self-reported [S20] |

**Not replenishment.** Gitcoin rounds, Optimism Retro Funding, Drips, Superfluid and token issuance are allocation, routing or dilution under ORF (§2, p. 14; §18, p. 42). They are not replenishment.

**Chains.** Of the ten largest layer-1 and layer-2 networks reviewed for this release, none routes protocol fees to open source maintenance; fees are burned, paid to validators or miners, or used for buybacks. ORF's structural fee instrument (§8 A.1, p. 23) therefore remains unexercised by those networks. This bears on where N1 funding could come from, not on what projects need. See §4.3.

### 2.6 Remaining gaps

Each gap marks a place where a written mechanism needs an external program before it can work. None is a proposal to change the model.
1. **Recipient rails (N3).** OMF retainers (§9, p. 24) and federated co-funding (App. C, pp. 55–56) presuppose that a recipient can be paid.
2. **Long-tail reach.** By its own test, dOSPO is inappropriate for small, experimental ecosystems (§9, p. 24). Small projects can benefit only as recipients of a larger ecosystem's OMF (§12, p. 33; App. C, pp. 55–56).
3. **User burden (N7).** Coordination support exists (OMF §9, p. 24). No mechanism addresses hostile or demanding users.
4. **Baseline.** OMF's health measurement (§16, p. 42) and ORF Gate 1 (§12, p. 31) would benefit from asking Tidelift's questions within a funded portfolio, so that later results can be compared with the figures above.
5. **Evidence.** No ORF Hard Gate has been passed by any ecosystem. The ratings in this section describe design fit only.

### 2.7 Closing the gaps, need by need (proposals)

> **Stage 0. Every item in this section is a PROPOSAL, not a finding. No Hard Gate is claimed as passed, for ORF or for any ecosystem named here.** The dOSPO, OMF and ORF version 1.0 whitepapers remain the specification, with `ORF_ERRATA.md` controlling over the ORF PDF. **Nothing here changes the specification.** Each item is tagged:
> - **Fits as written:** it applies a mechanism the whitepaper text already defines. Running it would change nothing in the text.
> - **Extension:** it goes beyond the published text. It is recorded here as a gap the text leaves open, not as a change to the text. It is an example, not a spec change, and would need author review.
>
> Every named program is an **example** of activity that already exists. Naming one is not an endorsement and does not report a result.

The needs table in §2.3 (N1–N8, plus long-tail reach) finds that, within a funded ecosystem's portfolio, the whitepapers have a named mechanism for six of the eight needs. It rates **N7 recognition and relief from user burden** as **Partial** and **N3 a way to receive money** as a **Gap**. Reach to small projects outside a funded ecosystem's portfolio (the long tail) is also a **Gap**. This section takes the needs in the same order as §2.3, which follows the order of Tidelift's questions. For each need it gives §2's verdict with its Tidelift 2024 citation, then the proposals that serve that need. Tidelift figures come first; other surveys only support them.

*Labels.* G1–G5 and R1–R5 are this section's own item labels. They are not the gap labels G1–G5 in `surveys/crisis-to-model-map.md` §3.

#### 2.7.1 Summary by need

| Need (§2.3) | §2.3 verdict | Fits as written | Extension |
|---|---|---|---|
| N1 Predictable, sustained pay | Addresses within portfolio; gap outside | G2 | none |
| N2 Paid security and maintenance work | Addresses | G3 | none |
| **N3 A way to receive money** | **Gap** | none | **G4** |
| N4 Infrastructure and tooling | Addresses | G1 | none |
| N5 More maintainers and succession | Addresses within portfolio | no separate item (R1 and G3 contribute) | none |
| N6 Onboarding contributors | Addresses within portfolio | R1 (shared with N7) | none |
| **N7 Recognition and relief from user burden** | **Partial** | R1, R2, R4 | **R3**, **R5** |
| N8 Governance, compliance and legal support | Addresses within portfolio | none | G5 |
| **Reach to the long tail** (cross-cutting) | **Gap** | G1, G2, G3, but only inside a funded dependency graph | G4, G5 |

#### 2.7.2 The needs and the proposals

**N1. Predictable, sustained pay.**
*§2.3 verdict: Addresses within a funded portfolio; gap outside. 81% of maintainers prefer predictable monthly income [S01, p. 11], and 60% describe themselves as unpaid hobbyists [S01, pp. 4–5].*

- **G2. Co-fund one retainer for a small library that several ecosystems depend on.** Each ecosystem contributes in proportion to its dependency centrality on the library, and each governance body votes on its share independently. **Fits as written.** OMF Appendix C, Federated Co-Funding Model (pp. 55–56): contributions are proportional to centrality, and "No cross-chain voting or shared treasury mechanism is required." The text's own example is libp2p across Ethereum, Filecoin and Polkadot. The retainer itself is OMF §8 (p. 23) and §9 (p. 24).
  - *Example:* none found. The evidence base contains no cross-ecosystem co-funded retainer, so the mechanism is described in the text but not demonstrated.
  - *Evidence:* the 81% preference for monthly income [S01, p. 11]. Supporting: among the top 50 non-npm projects, 40% had one or two developers accounting for more than 80% of commits [S06, p. 2].

**N2. Paid capacity for security and maintenance work.**
*§2.3 verdict: Addresses. Security work rose from 4% of maintainers' time in 2021 to 11% in 2024 [S01, p. 17]. On average, paid maintainers were 55% more likely to have implemented security and maintenance practices [S01, p. 27].*

- **G3. Run the dependency audit across transitive dependencies, so the long-tail packages that critical components rely on are found, scored and can be paid.** **Fits as written.** The text already covers transitive dependencies, so this applies the written scope in full rather than widening it. OMF §14 (p. 37): dependency mapping covers "direct dependencies, transitive dependencies, and foundational libraries." Appendix A (p. 47) and its audit walkthrough (p. 49) say "Identify all direct and transitive dependencies." Appendix E (p. 61) gives the scoring: centrality, inverse bus factor, maintainer burnout risk and security incident history. G3 also serves N1, N5 and long-tail reach.
  - *Cadence.* The whitepaper requires transparent reporting at least quarterly and a review of the portfolio against the dependency map at least annually (OMF §4, p. 15). The quarterly audit cadence comes from repo companion `omf/STEWARDSHIP.md`, not from the whitepaper.
  - *Example:* dependency-graph and funding-link data such as ecosyste.ms [S22]. Under ORF this is data and **routing, not revenue**.
  - *Evidence:* security time 11% [S01, p. 17]. Supporting: 72.8% of critical packages have no funding link in their package metadata, and 3.26% of packages carry funding links [S22].

**N3. A way to receive money (GAP).**
*§2.3 verdict: Gap. No whitepaper describes a recipient-side route by which a project can receive money. Donation programs pay 25% of maintainers and companies pay 5% directly [S01, pp. 15–16]. Supporting evidence only: 72.8% of critical packages have no funding link in their package metadata [S22].*

This is the model's clearest gap. **No whitepaper describes a recipient-side payment route.**
- OMF's retainers (§9, p. 24) and federated co-funding (App. C, pp. 55–56) assume the recipient can already be paid.
- dOSPO's four funding principles (§7, p. 20) do not cover how a recipient is paid. They are lifecycle alignment, time-bounded support, evidence-based renewal and portfolio discipline.
- ORF classes a routing rail as something that "moves already-collected money down the supply chain" and does not count it as revenue (§7, p. 22; the Routing Mirage, §2, p. 14). It recognizes rails but does not provide them.

- **G4. Give maintainers who have no payment route a way to receive funds, for example through a fiscal host, so a funded ecosystem can actually pay a long-tail recipient.** **Extension.** No whitepaper contains a fiscal-host mechanism or any other recipient payment route. The closest written text is the program list in OMF §8 (p. 23) and the retainers in §9 (p. 24), and both assume a recipient that can be paid. Nothing in the specification sets this up. It needs a program outside the model, and adding it to the model would need author review.
  - *Examples:* fiscal hosting and donation platforms such as Open Collective and GitHub Sponsors. thanks.dev is documented in one donor case reaching 358 recipients [S21]; thanks.dev totals are UNVERIFIED. All of these are **routing, not revenue**: they move money that something else has already collected.
  - *Evidence:* 25% of maintainers already receive money through donation programs [S01, p. 15]. Supporting: 72.8% of critical packages have no funding link in their package metadata, which shows missing funding signals, not that maintainers cannot receive money [S22].

*What remains.* N3 stays a **Gap**. G4 is an Extension. Until a recipient route exists, OMF cannot pay a maintainer it cannot reach.

**N4. Infrastructure and tooling.**
*§2.3 verdict: Addresses. Reproducible or verifiable builds are in place on 53% of projects and would be on 82% if maintainers were paid [S01, pp. 30, 35].*

- **G1. Fund shared tooling that many small projects depend on at portfolio level, so that no single small project has to apply.** **Fits as written.** OMF §12, Instrument 3, Shared Infrastructure Support (p. 33), states that the instrument is "explicitly portfolio-scoped rather than project-scoped". The dOSPO whitepaper names the same funding class (§7, p. 20).
  - *Example:* the Sovereign Tech Agency's funding of base technologies, with 118 technologies supported and €41.1M invested [S16]. The OMF definition box credits the "STA and OSE models".
  - *Evidence:* a dependency-management process is in place on 40% of projects and would be on 66% if maintainers were paid [S01, pp. 30, 35]. Supporting: 72.8% of critical packages have no funding link in their package metadata [S22].

**N5. More maintainers and succession.**
*§2.3 verdict: Addresses within a funded portfolio. In 2023, among maintainers who quit or considered quitting (n=153), 56% would have valued help finding another experienced maintainer to join and share responsibilities, and 40% help finding someone to take over some of their projects [S02, p. 31]. Thirteen percent have a succession plan today, and 63% would if paid [S01, p. 36].*

There is no separate proposal for N5. R1 (under N7) strengthens the Contributor Pathways pipeline that OMF §10 (p. 26) ties to new maintainers. G3 (under N2) puts inverse bus factor into the audit (App. E, p. 61). Succession planning is already written into Resilience Programs (§8, p. 23).

**N6. Onboarding contributors and community building.**
*§2.3 verdict: Addresses within a funded portfolio. In 2023, help marketing to find contributors was rated valuable by 75% of maintainers and help retaining contributors by 74% [S02, p. 33].*

R1 serves N6 as well as N7. It is set out under N7. There is no other proposal.

**N7. Recognition and relief from user burden (PARTIAL).**
*§2.3 verdict: Partial. In 2024, among the things maintainers dislike about the work, 48% named being thankless or underappreciated, 43% added personal stress, 39% users being too demanding (chart only) and 32% loneliness [S01, pp. 38–39]. These are dislikes; the 2024 report did not ask why people quit.* Supporting: the 2023 figures were 42% for loneliness [S02, p. 26] and 36% for demanding users [S02, p. 25, chart]; the 2021 figure was 37% [S03, p. 15]. The latest quit reasons are from 2023: burnout was a reason for 44% of those who quit or considered quitting [S02, p. 30]. Heath's report names toxic behaviour and hyper-responsibility alongside pay [S29].

The OMF text covers more of the recognition side than of the user side. R1 to R4 use mechanisms the text already contains. The user side has only partial written cover (R2), and the rest is an Extension (R5).

*Recognition*
- **R1. Make milestone recognition a funded, reported part of every Contributor Pathways cohort, not an optional extra.** **Fits as written.** OMF §10's design list (p. 27) includes "Recognize contributor milestones to reinforce long-term engagement". Reporting it falls within the minimum transparent-reporting requirement (OMF §4, p. 15). R1 also serves N6.
  - *Example:* CNCF's mentorship programs (LFX Mentorship, GSoC, Outreachy). OMF §10 (p. 26) cites 25 mentees who became project maintainers since 2020.
  - *Evidence:* underappreciated 48% [S01, p. 38].
- **R3. Credit maintainers' work by name, with their consent, in the OMF quarterly report and the dOSPO transparency report, so funders and users can see the maintenance.** **Extension.** No whitepaper sentence requires naming maintainers; OMF's transparent-reporting requirement (§4, p. 15) is the nearest basis, and adding names to the required reporting would add to the spec. The templates are repo companion documents, not whitepaper text: `omf/QUARTERLY_REPORT_TEMPLATE.md` has a maintainer roster table ("[Name/Project] … Active / Under review / Exiting"), and `dospo/TRANSPARENCY_REPORT_TEMPLATE.md` reports by program.
  - *Example:* Protocol Guild's published membership and quarterly audits [S27].
  - *Evidence:* underappreciated 48% [S01, p. 38].
- **R4. Run a short, repeatable maintainer-conditions survey in each funded portfolio, so burnout risk is measured over time rather than inferred.** **Fits as written.** Under Maintainer Sustainability, OMF §16 (p. 42) lists "self-reported burnout" and notes that "CHAOSS and Tidelift surveys both measure these dimensions". Burnout risk is already weighted in the program selection rubric (App. B, p. 52, 20%) and in risk-priority scoring (App. E, p. 61, W3 = 0.25). Repo companion `omf/DEPENDENCY_AUDIT_TEMPLATE.md` (lines 139–140) uses the same weight. Asking Tidelift's own questions would make results comparable with §2 (see §2.6, item 4).
  - *Examples:* the Tidelift survey instrument, run in comparable waves [S01, S02], and the CHAOSS/STA impact toolkit [S23].
  - *Evidence:* 60% quit or considered quitting [S01, p. 40].

*User burden*
- **R2. Fund community management and communication support as a service to maintainers, so that this work is not unpaid labour on top of code.** **Fits as written.** OMF §9 Coordination Support (p. 24) provides "assistance with community management and communication work" and "reduces social overhead that contributes heavily to burnout". Operational Support Services (§9, p. 24) take on audit, legal and compliance work. Moderation and handling of users are **not** in §9. The OMF whitepaper mentions "community moderation" only inside a quoted practitioner view (Caceres, 2025, in §4, p. 14), not as a mechanism. That part has moved to R5.
  - *Example:* GitHub Secure Open Source Fund cohorts. OMF §9 models Operational Support Services on their structured support [S18].
  - *Evidence:* users too demanding 39%, lonely 32% [S01, pp. 38–39].
- **R5. Back funded maintainers in moderating and handling users and in enforcing a code of conduct against abusive users, with moderation staff and escalation support.** **Extension.** No whitepaper addresses demanding or hostile users. The OMF, dOSPO and ORF texts contain no mechanism for codes of conduct, moderation or harassment.
  - *Example:* foundation-level code-of-conduct committees (qualitative; no figure used).
  - *Evidence:* users too demanding 39% [S01, p. 38]. A code of conduct is in place on 53% of projects [S01, p. 32]. A conflict-resolution process exists on 17% of projects, and 50% would adopt one if paid [S01, p. 36]. Supporting: demanding users 36% in 2023 [S02, p. 25, chart] and 37% in 2021 [S03, p. 15].

*A risk the text already guards.* ORF's LTS and SLA family (§8 Family B, Extended Lifecycle Support, p. 24) would put a price on maintainer availability, which could add to user pressure. The Service Capacity Test (§10, p. 28) and the "Liability Without Capacity" failure mode (§18, p. 42) are written to stop an ecosystem selling capacity it does not have. This section adds nothing to them.

*What remains.* N7 stays **Partial**. R1 to R4 work on recognition, isolation and measurement through existing text. R2 covers community management but not moderation. R5 is outside the published text.

**N8. Governance, compliance and legal support.**
*§2.3 verdict: Addresses within a funded portfolio. In 2023, 54% of maintainers wanted help understanding which security standards apply [S02, p. 14]. In 2024, 39% disliked being asked to meet requirements they lack time for [S01, p. 38].*

- **G5. Let several small ecosystems share one dOSPO-style governance body and one OMF portfolio, instead of each running its own.** **Extension.** The dOSPO whitepaper **does not address shared dOSPOs**. The closest written analog points the other way: OMF Appendix C (p. 56) says cross-ecosystem coordination is "informational, not structural". Any shared body would have to be weighed against the stated minimum cost of about $450K to $1.2M a year (dOSPO §7, p. 21) and against the suitability test (dOSPO §9, p. 24).
  - *Already written for small ecosystems.* dOSPO §9 (p. 24) says that for ecosystems where a dOSPO is inappropriate, "DAOs, foundations, or informal governance may be more effective". OMF prices DAO-only coordination at about $0 to $150K a year, "suitable only for very early-stage ecosystems with minimal infrastructure dependency" (§12, Cost of Coordination, p. 33).
  - *Example:* umbrella foundations that host many projects, such as the Linux Foundation's project hosting (qualitative).
  - *Evidence:* 54% wanted help understanding standards [S02, p. 14].

**Reach to the long tail: the small-projects limit.**
*§2.3 verdict: Gap. Seventy-eight percent of unpaid hobbyists work ten hours a week or less [S01, p. 10].*

dOSPO §9 (p. 24) states that a dOSPO "is inappropriate when the ecosystem is small and experimental, dependency depth is shallow, failures are localized and recoverable…". dOSPO §7 (p. 21) puts a minimum viable dOSPO at about $450K to $1.2M a year. So none of these proposals asks a small project to run the model. They ask how an ecosystem that already runs it can reach small projects as recipients:
- G1, G2 and G3 **fit as written**, but reach a small project only if it sits inside the dependency graph of an ecosystem that runs OMF.
- G4 (**Extension**) would be needed to pay a small project that has no payment route.
- G5 (**Extension**) would widen the reach, but it is not in the specification.

**A small project that no funded ecosystem depends on stays outside the model.** This section does not change that.

#### 2.7.3 What this changes in the assessment

**Nothing in §2.3 is re-rated.** Proposals are not results, and the model remains at Stage 0. If the Fits-as-written items were run in a funded pilot, these are candidate measures to watch, by need:

| Need | Items | Candidate pilot measure |
|---|---|---|
| N1 | G2 | Whether any App C co-funded retainer is authorized by two or more governance bodies; the share of high-centrality audited dependencies under a retainer |
| N2 (and long tail) | G3 | The share of transitive dependencies scored in the audit under App E |
| N3 | G4 (Extension; measure only if an outside route exists) | The share of audited long-tail dependencies with a working payment route |
| N4 | G1 | Shared tooling funded under Instrument 3, and the number of portfolio projects using it |
| N6, N7 | R1, R3 | Milestone recognitions per pathway cohort; consented named credits per report |
| N7 | R4 | Change in maintainer-conditions survey results across waves, asked in Tidelift's wording so they compare with [S01] |
| N8 | G5 (Extension) | None until author review |

These would be candidate evidence for a Stage 1 review. They are not a substitute for that review, and none of them bears on any ORF Hard Gate.

*Sources.*
- *Whitepapers (specification):* the dOSPO v1.0, OMF v1.0 and ORF v1.0 PDFs as published in the repo, with `ORF_ERRATA.md` controlling. Citations give section and PDF page.
- *Repo companion files (not whitepaper text):* `omf/STEWARDSHIP.md`, `omf/DEPENDENCY_AUDIT_TEMPLATE.md`, `omf/QUARTERLY_REPORT_TEMPLATE.md`, `dospo/TRANSPARENCY_REPORT_TEMPLATE.md`.
- *Survey evidence:* `surveys/oss-survey-inventory.md` (S01–S30). Tidelift 2024 [S01] is cited first; the others only support it. Tidelift's corporate status is subject to a definitive agreement announced by Sonar.

---

## 3. Institutional model (pillars)

| Pillar | Question | Primary artifacts |
|--------|----------|-------------------|
| **dOSPO** | Who decides? | `dospo/` charter & non-powers; dOSPO whitepaper |
| **OMF** | How money goes out? | `omf/` program portfolio; OMF whitepaper |
| **ORF** | How money comes back? | `orf/INSTRUMENT_CATALOG.md`, `GOVERNANCE_RULES.md`, ORF PDF + **ERRATA** |

### 3.1 Closed-loop stages

Value Generation → ORF Collection → Governed Treasury → Routing & Allocation → OMF Deployment → Sustained Infrastructure (`C-047`). **Architectural rule:** distribution must not be mistaken for replenishment; counting routing/allocation as revenue is counting a conveyor belt as a factory (`C-048`).

### 3.2 What ORF is / is not

ORF is a **portfolio design problem** across five revenue families, not a single mechanism (`C-007`). It strictly separates revenue generation from routing rails and allocation engines (`C-008`). It does **not** monetize open-source code; value attaches to fork-resilient anchors (maintainer capacity, certification trust, canonical network activity, enterprise response, governance legitimacy) (`C-010`, `C-046`).

### 3.3 Minimum Viable ORF vs self-sustaining

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

## 4. Comparative use-case map

Method: map environments to pillar fit and gaps (`use-cases/web2-web3-prototypes.md`). Deep dossiers A–E carry dated source packets. Live-web hygiene and **12 new prototype rows** are in `use-cases/researchy-validation.md` and `use-cases/web2-web3-prototypes-expansion.md` (2026-09-24 PT). No new claim IDs minted; USe Me re-score reported **0 status flips** on the 141 (`claims/researchy-claim-deltas.md`).

### 4.1 Core catalog (pre-expansion)

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

### 4.2 Expansion rows (N1–N12) — Researchy live-web

Row IDs N1–N12 in this subsection are prototype rows from `use-cases/web2-web3-prototypes-expansion.md`; they are not the project needs N1–N8 in §2. Stage 0 prototypes only. Site counters and vendor marketing figures stay **publisher claims**, not Gate 2 cash. Full source packets: `use-cases/web2-web3-prototypes-expansion.md`.

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

### 4.3 The ten largest chains against ORF and the POSM cycle

*Supporting note only.* This subsection bears on one point: where the money for N1 (predictable pay, §2.3) could come from. No chain closes the ORF loop. It does not change any rating in §2.

> **Stage 0.** No Hard Gate is marked passed for any chain, for Cardano, or for ORF itself. Snapshot: CoinGecko, 9 Oct 2026 03:51 PT (CoinMarketCap cross-check swaps Hyperliquid and Zcash). Every figure below is carried from `chains/top10-chains-orf-alignment.md` and `chains/posm-cycle-chain-map.md` after Researchy's 58-row live check (`chains/researchy-chain-check.md`, 9 Oct 2026). Statuses travel with the figures; nothing here upgrades them.

**Scope.** The ten largest layer-1 and layer-2 networks by native-token market cap: Bitcoin, Ethereum, BNB Chain, XRP Ledger, Solana, TRON, Zcash, Hyperliquid, Dogecoin, Monero. No layer-2 enters the top ten (the largest, Mantle, is #56). Cardano (#11 when WBT is excluded; #12 under the top-100 gas-token scope rule, which counts WBT, CRO and OKB; top-100 CoinGecko snapshot fetched 9 Oct 2026 05:19 PT, data as of 05:17:50 PT, see `chains/top100-method.md`; the top-10 table uses the separate 03:51 PT snapshot) is included as the reference implementation of Intersect's Paid Open Source Model (POSM), because the POSM cycle diagram (Intersect whitepaper, 20 Dec 2024, p.11) is the frame this section uses alongside the ORF closed loop.

**Two frames, one question.** POSM's cycle runs P1 Funding In → P2 Steward Governance & Programs (Code for Us, Maintainer Retainer) → P3 Outputs → P4 Commercialization Channels → P5 Commercial Adoption → P6 Return to Treasury. Read against the three pillars, P1–P3 is the dOSPO and OMF half (who decides, how money goes out), and P6 is the ORF half (how money comes back). The question for each chain is therefore the same in both frames: does value generated by use of the network return, measured and governed, to the people maintaining it?

**Result.** None of the ten does. All ten score Phase 1 (reserve-funded, one-way) on the repo's 5-Question Posture Assessment, none meets Minimum Viable ORF, and none closes the POSM loop at P6 for open source. Cardano does not close it either: its P6 edge exists, but by Researchy's derivation from on-chain epoch totals (not an official figure) about 0.2% of treasury inflow is fee-derived and about 99.8% is reserve issuance (derived), which ORF excludes from replenishment.

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
- *Web3 foundations:* the question to bring is not "what new revenue could fund maintenance" but "what share of revenue you already collect could be redirected under a chartered, sunset-bound mandate, and who would govern it." Zcash shows the mandate pattern; Optimism (§4.1) shows the Family A routing pattern; neither yet shows a passed gate.
- *Universities and researchers:* the ten chains form a natural comparative sample with public, dated evidence. The open measurement problems are the fee-versus-issuance split (Cardano's is derived, not published), the absence of published treasuries (Solana Foundation; Ethereum Foundation after Oct 2024), and how to attribute adoption-driven fees to specific open-source components.
- *Maintainers and advisors:* POSM-style retainers are the deployable piece today. Anything presented as "self-sustaining" should be checked against the issuance exclusion before it is repeated.

**Open items carried forward (do not cite as High).** Zcash Coinholder-Controlled Fund size (≈146.7k ZEC, third-party readers, Unverified); Hyperliquid's fee share to the Assistance Fund (Unverified); BNB Builder Fund disbursement (unknown); Solana Foundation and post-2024 Ethereum Foundation treasury totals (unknown); TRON fee magnitude (Partial, methodology-dependent); Cardano fee/issuance split (derived, not official); OSC 2026–27 request status (text exists, no on-chain action). Protocol Guild's 2025 figures ($7,231,668 from 6,202 donors; 190 members as of 5 Aug 2026) are Validated by Researchy; the errata entry was approved by Christian Taylor on 9 Oct 2026 and is applied in `ORF_ERRATA.md` and the §4.1 Protocol Guild row (Confidence: High; captures in `chains/data/pg-*`). "Commitments above $80 million" stays Unverified.

Sources: `chains/top10-chains-orf-alignment.md`, `chains/posm-cycle-chain-map.md`, `chains/paid-oss-cycle-chain-map.md`, `chains/researchy-chain-check.md`, `chains/data/POSM-SOURCES.md`.

---

## 5. Claims register & validation method

### 5.1 Method

Imported 141 claims from the foundation draft; scored against whitepaper extracts, `ORF_ERRATA.md` (controlling), Evidence Register, VALIDATION.md, orf-docs, precedents, and tools. Statuses: SUPPORTS / PARTIAL / CONFLICTS / ERRATA / UNVERIFIABLE.

### 5.2 Results (release-1)

| Status | Count |
|--------|------:|
| SUPPORTS | 99 |
| PARTIAL | 35 |
| ERRATA | 5 |
| CONFLICTS | 2 |
| UNVERIFIABLE | 0 |
| **Total** | **141** |

Full worksheet: `claims/orf-claims-validated.md`. Hard flags in that file’s banner are binding on any derivative brief or slide deck.

### 5.3 Lifecycle

Stage 0 → Stage 1 peer review (≥2 independent experts) → Stage 2 piloted precursors → Stage 3 validated production (`VALIDATION.md`). This draft remains **Stage 0**.

---

## 6. Feasibility notes (illustrative only)

The Tier 1 feasibility model uses an illustrative ~**$3.0M** baseline maintenance cost floor and a compound stress scenario (protocol fees −50%, enterprise −40%, membership −30%, capital yield −40%, certification flat) (`C-098`). It requires ecosystem-specific tuning. It is **not** evidence that any named ecosystem clears Gate 3 or Gate 6.

Endowment arithmetic: ~$3M/year spendable income at 3–5% real yield implies on the order of **$60M–$100M+** productive principal — the Endowment Fantasy check (`C-018`).

Evaluator / preview tooling that shows sample `PASSED` is a teaching aid only; it is not a Hard Gate result.

---

## 7. Implementation path (for adopters and advisors)

Sequence derived from the release-1 outline §6 and `synthesis/end-user-needs.md`. Aimed at foundations and research groups evaluating pilots—not a product brochure.

1. **Discovery** — classify inflows with the five economic questions (Origin, Legitimacy, Cost, Risk, Coverage) (`C-039`); publish a Gate 1 cost-floor method.  
2. **First instruments** — prefer B.1 assurance (when capacity exists) or C.1 membership design; withhold B.2 LTS/SLA until the Service Capacity Test passes (`C-058`, `C-073`–`C-074`).  
3. **Legal** — designate or stand up a Neutral Legal Entity; set tax-reserve policy with counsel (Polkadot PCF as design reference only; spend magnitudes remain Unverified in this pack).  
4. **Reporting** — adopt the 12-field tracker and a quarterly replenishment audit (gross, cost-to-collect, net, RCR, MCR, SCR, SLA/wind-down) (`C-099`).  
5. **Pilot completion criteria** — one earned instrument, net-contribution reporting, and a review cadence justify an MV-ORF claim; PCR may remain below 1.0.  
6. **Measurement aids** — CHAOSS/GrimoireLab and Open Source Observer inform deployment decisions; they do not substitute for Gate 2 cash evidence.  
7. **Accompanying materials** — this Stage 0 paper; `INSTRUMENT_CHARTER_TEMPLATE`; enterprise sponsor kit pointers in the upstream repo.

---

## 8. Limitations, risks, research agenda

### 8.1 Risks / anti-patterns

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

### 8.2 Gaps blocking Stage 1+

See `synthesis/gaps.md`: expert interviews not done; no independent eight-gate audit of any ecosystem; longitudinal POSM retention pending; several landscape magnitudes Unverified; OMF trillion erratum still needed; no OSFL-owned C_base reference implementation; SLA vault code removed. Expansion hunt still thin on restaking/yield beyond Octant, naming-revenue peers beyond ENS, Asia public funds, university tech-transfer endowments, and non-Optimism L2 fee loops (`web2-web3-prototypes-expansion.md`).

### 8.3 Research agenda (actionable)

1. Stage 1 expert panel using `synthesis/expert-critique-angles.md` (questions only until dispositions exist).  
2. Publish empirical Gate 1 cost-floor methodology.  
3. Build eight-quarter correlation datasets for Gate 4 Step 1 where history allows.  
4. Refresh primary packets for Unverified magnitudes (Guild dollars, Polkadot spend, POSM budget lines, Octant epochs, Deep Funding).  
5. Retypeset ORF PDF incorporating errata; add OMF erratum for the trillion merge.  
6. Optional: publish the interactive GitHub Pages scaffold under `site/` once the author approves.

---

## 9. Conclusion

**The verdict.** For projects inside a funded ecosystem's portfolio, the dOSPO (who decides), OMF (how money goes out) and ORF (how money comes back) whitepapers as written cover six of the eight needs the Tidelift maintainer reports identify. N3 (a way to receive money) is a gap, because no whitepaper describes a recipient-side route by which a project can receive money. N7 (recognition and relief from user burden) is partial. The model does not reach small projects outside a funded ecosystem's portfolio (the long tail), which is where most of the 60% who describe themselves as unpaid hobbyists are likely to be [S01, pp. 4–5, 10], and dOSPO §9 (p. 24) says a dOSPO is inappropriate for small, experimental ecosystems.

**What could address the gaps (proposals, not findings).** §2.7 names four Extensions that go beyond the published text: G4, a fiscal host or other recipient payment route, for N3; R3 and R5 for N7 (named credit for maintainers; moderation and code-of-conduct support); and G5, a shared dOSPO for several small ecosystems, for N8. They are examples, not spec changes, and would need author review; they change nothing in the specification. The chain review (§4.3) is a supporting note on where N1 money could come from; no chain closes the ORF loop.

**What Release 1 contributes.** It does not claim that open infrastructure is already self-sustaining. It offers a **falsifiable architecture**: a vocabulary that separates governance, deployment and replenishment; a portfolio taxonomy that refuses to count routing rails as revenue; gates and ratios that make "sustainable" costly to assert; and an evidence discipline that prefers ERRATA and PARTIAL over persuasive fiction. The needs ratings in §2 describe design fit, not observed results.

For universities, the claim matrix, the errata layer and the Tidelift-ordered needs map are teachable methods. For foundations, the honesty spine and gate set are treasury red-team tools. Adjacent practitioners (enterprise buyers, maintainer programs, advisors) can adopt MV-ORF pilots without asserting Hard Gates that no reviewed ecosystem has cleared.

**Stage 0. No Hard Gate passed. Errata controls.**

---

## Bibliography (primary pointers)

**Specification (controls)**
- `whitepapers/orf-v1.0.pdf` + controlling `whitepapers/ORF_ERRATA.md` / `sources/ORF_ERRATA.md`  
- dOSPO & OMF whitepapers (`whitepapers/dospo-whitepaper-v1.0.pdf`, `whitepapers/open-maintenance-framework-omf-v1.0.pdf`; text extracts `sources/dospo-whitepaper.txt`, `sources/omf-whitepaper.txt`). Citations give section and PDF page.  
- `orf/INSTRUMENT_CATALOG.md`, `orf/GOVERNANCE_RULES.md`, `VALIDATION.md`, `docs/EVIDENCE_REGISTER.md`  
- Repo companion files (not whitepaper text): `omf/STEWARDSHIP.md`, `omf/DEPENDENCY_AUDIT_TEMPLATE.md`, `omf/QUARTERLY_REPORT_TEMPLATE.md`, `dospo/TRANSPARENCY_REPORT_TEMPLATE.md`

**Survey and study sources (S-IDs from `surveys/oss-survey-inventory.md`; URLs accessed 9 Oct 2026 PT)**
- [S01] Tidelift, *2024 State of the Open Source Maintainer Report* (Sep 2024; n=437) — PDF: https://assets-eu-01.kc-usercontent.com/ef593040-b591-0198-9506-ed88b30bc023/d325a56f-05be-4379-bfd1-ee4776fcad41/2024-tidelift-state-of-the-open-source-maintainer-report-.pdf  
- [S02] Tidelift, *2023 State of the Open Source Maintainer Report* (Apr 2023; n=339) — https://assets-eu-01.kc-usercontent.com/ef593040-b591-0198-9506-ed88b30bc023/d3df3f32-2b39-419a-8a99-7a4915a4e9ca/Tidelift-2023-open-source-maintainer-survey-1.pdf  
- [S03] Tidelift, *2021 Tidelift open source maintainer survey* ("nearly 400" respondents) — https://assets-eu-01.kc-usercontent.com/ef593040-b591-0198-9506-ed88b30bc023/79c06b71-8002-479f-981a-10c7f72471d7/2021_Tidelift_Maintainer_Survey_FINAL-1.pdf  
- Tidelift corporate status: Sonar–Tidelift **definitive agreement** announcement (wording per `C-112`; no closing announcement found on 9 Oct 2026)  
- [S06] LF Research, OpenSSF & Harvard LISH, *Census III of Free and Open Source Software* (Dec 2024) — https://www.linuxfoundation.org/hubfs/LF%20Research/lfr_censusiii_120424a.pdf  
- [S07] LF Research, GitHub & Harvard, *2024 Open Source Software Funding Report*; LF blog, "Understanding the State of Open Source Funding in 2024" (18 Dec 2024) — https://www.linuxfoundation.org/blog/understanding-the-state-of-open-source-funding-in-2024 · https://opensourcefundingsurvey2024.com/  
- [S10] Hoffmann, Nagle & Zhou, *The Value of Open Source Software*, HBS Working Paper 24-038 — https://www.hbs.edu/faculty/Pages/item.aspx?num=65230  
- [S12] Black Duck, *2026 Open Source Security and Risk Analysis* (Feb 2026) — https://www.blackduck.com/content/dam/black-duck/en-us/reports/rep-ossra.pdf  
- [S13] Synopsys OSSRA 2024 materials (cite with errata caution, `C-013`)  
- [S14] Sovereign Tech Agency, "What open source maintainers shared with us" (spring-2024 survey, 536 respondents) — https://www.sovereign.tech/news/what-open-source-maintainers-shared-with-us  
- [S16] Sovereign Tech Agency, Technologies page (program counter) — https://www.sovereign.tech/tech  
- [S17] Alpha-Omega, *2025 Annual Report* (Jul 2026) — https://alpha-omega.dev/wp-content/uploads/sites/22/2026/07/Alpha-Omega-Annual-Report-2025_073126a.pdf  
- [S18] GitHub Secure Open Source Fund results (Sessions 1–3) — https://github.blog/open-source/maintainers/securing-the-supply-chain-at-scale-starting-with-71-important-open-source-projects/ · https://github.blog/open-source/maintainers/securing-the-ai-software-supply-chain-security-results-across-67-open-source-projects/  
- [S20] Open Source Pledge member reports (self-reported) — https://opensourcepledge.com/members/ · https://opensourcepledge.com/about/  
- [S21] thanks.dev, Canonical case (2025; aggregate totals Unverified) — https://canonical.com/blog/canonical-thanks-dev-giving-back-to-open-source-developers  
- [S22] ecosyste.ms / A. Nesbitt, *State of OSS Funding Data* (CHAOSScon NA 2025) — https://github.com/andrew/state-of-oss-funding  
- [S23] CHAOSS, STA, NGI Commons & LF, *Toolkit for Measuring the Impacts of Public Funding on OSS* (2024) — https://www.sovereign.tech/news/measuring-the-impact-of-our-funding  
- [S27] Protocol Guild annual report and quarterly membership audits (pack capture `chains/data/pg-*`; Q3 2026 audit capture: 190 members as of 5 Aug 2026)  
- [S29] Heath, *Report on Burnout in Open Source Software* (Nov 2025) — https://mirandaheath.website/static/oss_burnout_report_mh_25.pdf  
- Inventory entries not cited in this draft: S04, S05, S08, S09, S11, S15, S19, S24, S25, S26, S28, S30 (see `surveys/oss-survey-inventory.md`).

**Ecosystem and program sources**
- Optimism docs / Year 3 budget update / buyback vote materials (see errata URLs in `C-103`–`C-106`)  
- ENS KPK review thread; EP 6.46 (cite as separate closes)  
- Intersect POSM explainer; Intersect whitepaper (20 Dec 2024, POSM cycle diagram p.11)  
- Linux Foundation / CNCF certification & membership pages  
- Chain review: `chains/top10-chains-orf-alignment.md`, `chains/posm-cycle-chain-map.md`, `chains/paid-oss-cycle-chain-map.md`, `chains/researchy-chain-check.md`, `chains/data/POSM-SOURCES.md`

**In-pack worksheets**
- `claims/orf-claims-validated.md`, `claims/researchy-claim-deltas.md`, `use-cases/web2-web3-prototypes.md`, `use-cases/web2-web3-prototypes-expansion.md`, `use-cases/researchy-validation.md`, `claims/implementation-validation.md`  
- `surveys/oss-survey-inventory.md`, `surveys/crisis-to-model-map.md`, `surveys/section-2.7-ref-check.md`, `surveys/researchy-section2-pagecheck.md`, `surveys/researchy-survey-factcheck.md`

Dated access for this draft: 2026-09-24 America/Los_Angeles; survey sources (§2) accessed 2026-10-09 PT.
