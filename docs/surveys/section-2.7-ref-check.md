# Reference check: `release1-section-2.7-closing-the-gaps.md` (Give me Purposise draft) and my own §2 refs

> **Checked:** 9 Oct 2026, ~05:30–05:45 PT. Repo clone `/workspace/osfl-repo` pulled from `origin/main`: still at `9a82a9c` (8 Oct 2026 07:42 PT); no new commits.
> **Canon checked against:** `whitepapers/open-maintenance-framework-omf-v1.0.pdf` (70 pp.), `whitepapers/dospo-whitepaper-v1.0.pdf` (26 pp.), `whitepapers/orf-v1.0.pdf` (50 pp.) with `whitepapers/ORF_ERRATA.md` controlling, using `pdftotext -layout` text. Page numbers are **PDF pages**. `OMF_WHITEPAPER.md` and `DOSPO_WHITEPAPER.md` are 13-line pointer files with no section text.
> **Section map verified from the PDFs.**
> - OMF: §1 Web3 Maintainer Crisis p8 · §2 Landscape p10 · §3 Missing p12 · §4 Introducing OMF p14 · §5 Principles p17 · §6 Institutional Legitimacy p19 · §7 Ecosystem Architecture p21 · §8 Program Architecture p23 · §9 Maintainer Sustainment Mechanisms p24 · §10 Contributor Pathways p26 · §11 Infrastructure Lifecycle Support p28 · §12 Funding Architecture p30 (Instrument 1 p31, Instrument 2 p32, Instrument 3 p33) · §13 Operational Governance p36 · §14 Portfolio Stewardship p37 (Dependency Centrality Metric p38) · §15 Implementation Models p40 · §16 Measuring Ecosystem Health p42 · §17 Risks p44 · App A p47 · App B p51 · App C p55 (Federated Co-Funding p56) · App D p58 · App E p61.
> - dOSPO: §3 p13 ("What a dOSPO Is Not" / "Hard Boundaries" p14) · §5 p16 · §6 p19 · §7 p20–21 · §9 p24.
> - ORF: §2 p13 (Routing Mirage p14) · §5 p19 · §7 p22 · §8 p23 · §9 p26 · §10 p28 · §11 p29 · §12 p31 · §13 p33 · §14 p35 · §18 p42.
> **Purposise's file was not edited.**

## A. Purposise draft §2.7: item by item

| # | Item | Cited ref | Actual location in canon | Result |
|---|---|---|---|---|
| 1 | dOSPO inappropriate for small/experimental/shallow ecosystems | dOSPO §9 | dOSPO §9 "When Not to Use a dOSPO", p24: "inappropriate when the ecosystem is small and experimental, dependency depth is shallow…" | **PASS** |
| 2 | Minimum cost $450K–$1.2M/yr | dOSPO §7 | dOSPO §7 "Cost of Coordination", p21 ("A minimum viable dOSPO … costs approximately $450K to $1.2M") | **PASS** |
| 3 | G1 shared tooling funded at portfolio level, **Fits as written** | OMF §12, Instrument 3 | OMF §12 Instrument 3 "Shared Infrastructure Support", p33: "OMF addresses this through portfolio-level funding decisions". The definition box credits "STA and OSE models", so the STA example is apt | **PASS** |
| 4 | G2 federated co-funding by centrality, independent votes, libp2p example, **Fits as written** | OMF Appendix C | OMF App C (starts p55), "Federated Co-Funding Model" p56; libp2p in Ethereum, Filecoin and Polkadot; "No cross-chain voting or shared treasury mechanism is required" | **PASS** (ref). **FIX (evidence wording):** "40% of top packages" should read "among the top 50 non-npm projects, 40% had one or two developers accounting for >80% of commits" (Census III p2, S06) |
| 5 | G3 extend audit to second-order dependencies, **Fits as written (scope choice)** | OMF Appendix A; `DEPENDENCY_AUDIT_TEMPLATE.md` | OMF App A p47 ("direct and transitive dependencies"); p49 audit walkthrough: "Identify all direct and transitive dependencies". Template is `omf/DEPENDENCY_AUDIT_TEMPLATE.md`. Quarterly cadence: OMF p15 ("minimum on a quarterly basis") and `omf/STEWARDSHIP.md` | **PASS**. Note: transitive coverage is already in the text, so "scope choice" understates it |
| 6 | G4 fiscal-host payment route, **Fits as written (OMF delivery detail)** | "OMF Program 1–2 delivery; dOSPO funding principles" | **Not found.** The OMF whitepaper has no "Program 1/Program 2" numbering. Programs are named in §8 p23 (Maintainer Retainer, Code Bounties, …); the numbering exists only in repo companion doc `omf/PROGRAM_PORTFOLIO.md`. No mention of fiscal hosting, fiscal sponsors or Open Collective in OMF, dOSPO or ORF text. dOSPO §7 funding principles (p20) are lifecycle alignment, time-bounded support, evidence-based renewal and portfolio discipline; none covers recipient payment routes. ORF §7 (p22) treats rails as routing infrastructure, not recipient onboarding | **FIX:** re-tag as **Extension** (not in published text), or as a gap the text leaves open. Correct the ref to "OMF §8 (p23) program list; no written mechanism" |
| 7 | G5 shared dOSPO/OMF across several small ecosystems, **Extension** | dOSPO §7, §9 | Correctly flagged. dOSPO text describes a dOSPO for an ecosystem and says nothing about shared dOSPOs. "Assumes one ecosystem per dOSPO" is an inference, not a quote. The closest written analog is OMF App C p56 (coordination "informational, not structural") | **PASS** (flag correct). **Minor FIX:** "does not address shared dOSPOs" rather than "assumes one ecosystem per dOSPO" |
| 8 | 48% underappreciated, 50% not paid | S01 p38 | Tidelift 2024 p38 | **PASS** |
| 9 | Loneliness 42%, demanding users 37% | S02 p26 | Tidelift 2023 p26 (text). Tidelift 2024 reports lonely **32%** (p39) and users-too-demanding **39%** (p38 chart, 2024 column) | **PASS** for 2023 figures. **Suggest** adding the 2024 values, since 2024 is the latest edition |
| 10 | R1 milestone recognition in Contributor Pathways, **Fits as written** | OMF §10 | OMF §10 p27: "Recognize contributor milestones to reinforce long-term engagement" (exact). CNCF "25 mentees became project maintainers since 2020": §10 p26 and §8 p23 | **PASS** |
| 11 | R2 fund community management **and moderation**, **Fits as written** | OMF §9 Coordination Support + Operational Support Services | OMF §9 p24: Coordination Support = "community management and communication work … Reduces social overhead that contributes heavily to burnout". Operational Support Services = security audit facilitation, legal review, compliance documentation, "Modeled on the structured support components of GitHub's Secure Fund training cohort" | **PASS** for community management and the GitHub citation. **Minor FIX:** "moderation" and "user handling" are not in the text; mark that part as beyond the text (it overlaps R5) |
| 12 | R3 credit maintainers by name in reports, **Fits as written** | `omf-docs/QUARTERLY_REPORT_TEMPLATE.md`; `dospo-docs/TRANSPARENCY_REPORT_TEMPLATE.md` | Repo paths are `omf/QUARTERLY_REPORT_TEMPLATE.md` (maintainer roster table, line 71: "[Name/Project] … Active / Under review / Exiting") and `dospo/TRANSPARENCY_REPORT_TEMPLATE.md`. The `*-docs/` paths are local pack copies (`osfl/sources/`), not repo paths. These are companion templates, not whitepaper text | **FIX (paths).** Tag is acceptable as a reporting practice inside existing templates |
| 13 | R4 repeatable maintainer-conditions survey, **Fits as written** | OMF §16; burnout-risk weight in dependency audit scoring | OMF §16 p42 "Maintainer Sustainability: Maintainer attrition rate; time-in-role; self-reported burnout; compensation adequacy". §16 also recommends periodic off-chain CHAOSS-aligned surveys. Burnout weight: OMF App E p61 (Risk-Priority Scoring, "Maintainer Burnout Risk (W3 = 0.25)") and App B p52 selection rubric ("Maintainer capacity and burnout risk (Weight: 20%)"); repo `omf/DEPENDENCY_AUDIT_TEMPLATE.md` lines 139–140 | **PASS**. Precise location: Appendix E (allocation scoring) and Appendix B (selection rubric) |
| 14 | R5 back code-of-conduct enforcement against abusive users, **Extension** | OMF (none) | No match for "code of conduct", "toxic", "harass" or "moderation" in the OMF, dOSPO or ORF PDFs | **PASS** (correctly flagged) |
| 15 | "§2.3 rates … long tail (Gap as operator) … burnout (Partial)" | my §2.3 | Matches my driver table as it stood. **My §2 is now restructured needs-first** (§2.3 is now the needs assessment), so this cross-reference needs updating to the new need numbers (N3 receive money, N7 recognition/user burden) | **FIX (dependency)** |
| 16 | Framing | n/a | The draft labels items "PROPOSAL" and includes three items that go beyond the published text (G4 once corrected, G5, R5). Christian's current instruction is no spec changes, with programs as labelled examples. Extensions should be presented as gaps the text leaves open, not as proposals | **FLAG for parent/author** (not a ref error) |

**Purposise draft tally (each item counted once, by its worst outcome):** 16 items. **PASS 9** (#1, 2, 3, 5, 8, 9, 10, 13, 14) · **FIX 6** (#4 evidence wording; #6 G4 must be re-tagged Extension and its ref corrected; #7 minor wording; #11 "moderation" beyond the text; #12 file paths; #15 cross-reference after restructure) · **FLAG 1** (#16 framing vs. no-spec-change instruction). The one substantive error is #6.

## B. My own files: refs checked and corrected

| # | My citation (old) | Actual | Result / action |
|---|---|---|---|
| 1 | dOSPO §7 p20 (continuity funding) | §7 "Funding Instruments", p20 | PASS |
| 2 | dOSPO §7 p21 ($450K–$1.2M) | p21 | PASS |
| 3 | dOSPO §9 p24 | p24 | PASS |
| 4 | dOSPO §6 p19 (security coordination) | p19 | PASS |
| 5 | dOSPO §3, §5 (non-powers) | §3 "What a dOSPO Is Not" / "Hard Boundaries" p14; §5 p16 | PASS. **Fixed:** "zero custody" is from repo `dospo/START_HERE.md` / `NON_POWERS.md`, not the whitepaper; now attributed |
| 6 | OMF §9 p24 (retainers, coordination, operational support) | p24 | PASS |
| 7 | OMF §10 (pathways) | p26–27 | PASS |
| 8 | OMF §12 Instr. 1/2/3 | p31 / p32 / p33 | PASS; page numbers added |
| 9 | OMF §14 p38 (centrality) | §14 starts p37; metric p38 | PASS |
| 10 | OMF §16 p42 | p42 | PASS |
| 11 | OMF App A p48 | **p47** (p48 is the printed TOC page) | **FIXED** |
| 12 | OMF App C p56 | App C starts **p55**; Federated Co-Funding p56 | **FIXED** to "App C p55–56" |
| 13 | OMF App E p61 | p61 | PASS |
| 14 | OMF §6 (autonomy safeguard) | §6 p19–20 ("Maintainer Autonomy", p20) | PASS |
| 15 | "OMF Program 4 (Resilience & Security)", "OMF Program 2" | No program numbering in the whitepaper. §8 p23 names "Resilience Programs" and "Code Bounties"; the numbering exists only in repo `omf/PROGRAM_PORTFOLIO.md` | **FIXED** → "OMF §8 p23 (Resilience Programs / Code Bounties)" |
| 16 | "Protocol 1–4" (co-maintainer rule, 60-day notice, 12-month reserve buffer, austerity budget, vendor capture) | **Not in the OMF whitepaper.** These are in repo companion doc `omf/RISK_MITIGATION_PROTOCOLS.md`. The whitepaper has co-maintainers in §8/§11 (p23, p28) but no requirement, buffer or notice period | **FIXED:** now cited as repo companion doc, not whitepaper; ratings that leaned on them are footnoted |
| 17 | ORF §2 "Routing Mirage" | p14 | PASS |
| 18 | ORF §5 Principle 1 (governance legitimacy) | §5 p19 "Legitimacy & Counter-Value" | PASS |
| 19 | ORF §8 p23; §9 p26; §10 p28; §12; §13; §18 p42 | p23 / p26 / p28 / p31 / p33 / p42 | PASS; pages added |
| 20 | ORF §14 D0–D5 | p35 | PASS |

**My files tally:** 20 refs checked. **PASS 15 · FIXED 5** (#5 attribution, #11, #12, #15, #16).

## C. Status after the needs-first restructure (9 Oct 2026, PT)

- **Table B fixes applied.** All five are now in `crisis-to-model-map.md` (§6 of that file lists them) and in `release1-section-2-survey-crisis-map.md`. The driver-based versions are archived under `surveys/archive/`.
- **Item #15 cross-reference.** My §2.3 is now the *needs assessment*: rows N1–N8, plus long-tail reach, ordered on the Tidelift question structure. It replaces the driver table D1–D10. Any reference in the 2.7 draft to "§2.3 drivers" or to D-numbers should point to the N-numbers. Suggested mapping, for Purposise to decide:
  - small-project items → N3 (a way to receive money) and the long-tail row;
  - recognition items R1–R5 → N7.
- **Gap labels.** My gap list (crisis map §3; section 2.6) now runs G1 recipient rails, G2 long-tail reach, G3 user burden, G4 baseline, G5 evidence. The 2.7 draft's own G1–G5 labels are independent of these. Aligning them is Purposise's call; I have not edited that file.
