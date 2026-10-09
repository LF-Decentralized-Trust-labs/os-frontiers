## 2. What Open Source Projects Need, and How Far the Three-Part Model Meets It

*Christian Taylor, Open Source Frontiers Lab, LF Decentralized Trust*
*Release 1 draft section; follows §1. Status: Stage 0 research candidate. No Hard Gate is claimed as passed for ORF or for any ecosystem discussed. Prepared 9 October 2026.*

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

**Caveats.** The samples are self-selected, and per-question bases vary; the base is given where it matters. Where a report's chart and text disagree, the figure that agrees with the other editions is used: 52% for 2023 "not compensated" [S02, p. 26]; 37%, 36% and 39% for "users too demanding" in 2021, 2023 and 2024 [S03, p. 15; S01, p. 38, chart]. The 2024 report's closing narrative says "almost two-thirds" have quit or considered quitting [S01, p. 59]; the measured figure, 60% [S01, p. 40], is used. The 2024 report has two different pay questions: 60% describe themselves as unpaid hobbyists (single choice, n=437) [S01, p. 4], and 47% report no maintainer income at all (multi-select, n=421) [S01, p. 13]. Both are valid if labelled. Tidelift also pays maintainers, and its corporate status is currently subject to a definitive agreement announced by Sonar.

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
  - 39% found users too demanding (chart; 36% in 2023, 37% in 2021 [S03, p. 15]);
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

**Chains.** Of the ten largest layer-1 networks reviewed for this release, none routes protocol fees to open source maintenance; fees are burned, paid to validators or miners, or used for buybacks. ORF's structural fee instrument (§8 A.1, p. 23) therefore remains unexercised by those networks. This bears on where N1 funding could come from, not on what projects need.

### 2.6 Remaining gaps

Each gap marks a place where a written mechanism needs an external program before it can work. None is a proposal to change the model.
1. **Recipient rails (N3).** OMF retainers (§9, p. 24) and federated co-funding (App. C, pp. 55–56) presuppose that a recipient can be paid.
2. **Long-tail reach.** By its own test, dOSPO is inappropriate for small, experimental ecosystems (§9, p. 24). Small projects can benefit only as recipients of a larger ecosystem's OMF (§12, p. 33; App. C, pp. 55–56).
3. **User burden (N7).** Coordination support exists (OMF §9, p. 24). No mechanism addresses hostile or demanding users.
4. **Baseline.** OMF's health measurement (§16, p. 42) and ORF Gate 1 (§12, p. 31) would benefit from asking Tidelift's questions within a funded portfolio, so that later results can be compared with the figures above.
5. **Evidence.** No ORF Hard Gate has been passed by any ecosystem. The ratings in this section describe design fit only.

---

#### Changelog

**9 Oct 2026, ~05:35–06:05 PT: Researchy page-check fixes applied** (`researchy-section2-pagecheck.md`, `researchy-survey-factcheck.md`)
- **Black Duck 93%:** now PDF p. 27 (printed p. 25), with a note that the sample is 947 audited commercial codebases.
- **55% average:** applies to security *and* maintenance practices; 8–26 percentage points [S01, p. 27].
- **"Only 36% paid at all":** replaced by "36% describe themselves as paid", with the p. 13 multi-select figure alongside (47% receive no maintainer income).
- **2023 56% / 40% items:**
  - base made explicit: only those who quit or considered quitting, n=153;
  - "successor" replaced by "take over some of their projects".
- **N7 reframed:**
  - 2024 figures (48/43/39/32) are labelled as dislikes;
  - the 2024 report did not ask quit reasons;
  - the latest quit reasons are given from 2023 [S02, p. 30].
- **$162M / 4%:** attributed to the LF/GitHub/Harvard funding survey; respondent organizations' direct contributions only.
- **N3 rescoped:**
  - the gap is the absence of a recipient-side route in the whitepapers;
  - 72.8% is stated as missing funding links in package metadata, used as support rather than as proof that maintainers cannot be paid.
- **Sample sizes:** 2023 standards reasons n=119; support n=288; 2021 dislikes n=335. Other per-question n added (344, 338, 359, 261, 307).
- **Scope wording:**
  - "describe themselves as unpaid hobbyists";
  - "top 50 non-npm projects";
  - stated-intent "if paid" figures;
  - employer-pay change "likely not statistically significant";
  - security-time category caveat;
  - xz statement wording.
- **Contradictions resolved in §2.2:** 60% (p. 40); 60% vs 47% labelled as different questions; 52% for 2023; 37/36/39 for "users too demanding".
- **STA:** same spring-2024 survey; ~63% derived; 77% not used.
- **Citations:** Tidelift 2024 cited by PDF URL; Tidelift 2021 cited directly (S03).
- **Verdict:** unchanged. Six of eight needs are met for portfolio projects, N3 is a gap, N7 is partial, the long tail is out of reach, and the model is at Stage 0. The N3 and N7 reframings change the evidence wording, not the ratings.

**9 Oct 2026, earlier:** restructured needs-first on the Tidelift spine. The driver-based version is archived at `surveys/archive/release1-section-2.driver-version.md`.

- 2026-10-09 05:47 PT: Protocol Guild $12.4M swapped for validated $7,231,668 / 6,202 donors ($12.4M held for later errata); bridging sentence added between 'no change proposed' and the section 2.7 Extensions.
