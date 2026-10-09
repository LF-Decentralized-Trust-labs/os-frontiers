### 2.7 Closing the gaps, need by need (proposals)

> **Stage 0. Every item in this section is a PROPOSAL, not a finding. No Hard Gate is claimed as passed, for ORF or for any ecosystem named here.** The dOSPO, OMF and ORF version 1.0 whitepapers remain the specification, with `ORF_ERRATA.md` controlling over the ORF PDF. **Nothing here changes the specification.** Each item is tagged:
> - **Fits as written:** it applies a mechanism the whitepaper text already defines. Running it would change nothing in the text.
> - **Extension:** it goes beyond the published text. It is recorded here as a gap the text leaves open, not as a change to the text. It would need author review before it could enter the specification.
>
> Every named program is an **example** of activity that already exists. Naming one is not an endorsement and does not report a result.

The needs table in §2.3 (N1–N8, plus long-tail reach) finds that, within a funded ecosystem's portfolio, the whitepapers have a named mechanism for six of the eight needs. It rates **N7 recognition and relief from user burden** as **Partial** and **N3 a way to receive money** as a **Gap**. Reach to projects outside a funded ecosystem's dependency map is also a **Gap**. This section takes the needs in the same order as §2.3, which follows the order of Tidelift's questions. For each need it gives §2's verdict with its Tidelift 2024 citation, then the proposals that serve that need. Tidelift figures come first; other surveys only support them.

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
*§2.3 verdict: Gap. No whitepaper describes a way for projects to receive money. Donation programs pay 25% of maintainers and companies pay 5% directly [S01, pp. 15–16]. Supporting evidence only: 72.8% of critical packages have no funding link in their package metadata [S22].*

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
*§2.3 verdict: Addresses within a funded portfolio. In 2023, among maintainers who quit or considered quitting, 56% said finding someone to take over some of their projects would have helped [S02, p. 31]. Thirteen percent have a succession plan today, and 63% would if paid [S01, p. 36].*

There is no separate proposal for N5. R1 (under N7) strengthens the Contributor Pathways pipeline that OMF §10 (p. 26) ties to new maintainers. G3 (under N2) puts inverse bus factor into the audit (App. E, p. 61). Succession planning is already written into Resilience Programs (§8, p. 23).

**N6. Onboarding contributors and community building.**
*§2.3 verdict: Addresses within a funded portfolio. In 2023, help marketing to find contributors was rated valuable by 75% of maintainers and help retaining contributors by 74% [S02, p. 33].*

R1 serves N6 as well as N7. It is set out under N7. There is no other proposal.

**N7. Recognition and relief from user burden (PARTIAL).**
*§2.3 verdict: Partial. In 2024, among the things maintainers dislike about the work, 48% named being thankless or underappreciated, 43% added personal stress, 39% users being too demanding (chart only) and 32% loneliness [S01, pp. 38–39]. These are dislikes; the 2024 report did not ask why people quit.* Supporting: the 2023 figures were 42% for loneliness and 36% for demanding users (37% in 2021) [S02, p. 26]. The latest quit reasons are from 2023: burnout was a reason for 44% of those who quit or considered quitting [S02, p. 30]. Heath's report names toxic behaviour and hyper-responsibility alongside pay [S29].

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
  - *Evidence:* users too demanding 39% [S01, p. 38]. A code of conduct is in place on 53% of projects [S01, p. 32]. A conflict-resolution process exists on 17% of projects, and 50% would adopt one if paid [S01, p. 36]. Supporting: demanding users 36% in 2023 and 37% in 2021 [S02, p. 26].

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
