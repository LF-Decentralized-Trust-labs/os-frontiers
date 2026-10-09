# Researchy fact-check: OSS survey inventory, STA conflict, release-1 §2 headline figures

> **Desk:** Researchy (fact-check only; no model changes proposed). **Check date for every item: 2026-10-09** (PT, 05:20–05:50).
> **Method:** live web only (WebSearch, WebFetch, curl). Nothing was signed up for, posted to or contacted. Every PDF was re-downloaded live and hash-compared with the capture in `surveys/data/`. Tidelift 2024/2023, STA evaluation, Census III, HBS and Black Duck were all byte-identical to the captures. The Tidelift 2021 PDF is new.
> **Pages are PDF page numbers** unless marked "printed".
> **Files not edited:** survey files, QA files (`chains/top100-qa-*.md`), whitepapers.
> **Companion outputs:**
> - `surveys/researchy-section2-pagecheck.md`: page-by-page check of the rebuilt §2;
> - `surveys/data/tidelift-page-index.md`: Tidelift quote/page index;
> - `surveys/errata-draft-omf-59pct.md`: OMF erratum draft;
> - `surveys/sources/`: official Tidelift 2021/2023/2024 PDFs plus STA, LF and ecosyste.ms captures, with SHA256SUMS.

## Verdict counts

| Part | CONFIRMED | CORRECTED | UNVERIFIED | CONFLICT | Total |
|---|---|---|---|---|---|
| 1. Inventory: Unverified / conflict items | 9 | 3 | 4 | 4 | 20 |
| 4. Release-1 §2 headline figures | 4 | 3 | 0 | 0 | 7 |
| **All** | **13** | **6** | **4** | **4** | **27** |

## 1. Inventory items (`oss-survey-inventory.md`: per-survey notes, Unverified flags, conflicts)

| # | Item | Verdict | Exact quote | URL · page | Note |
|---|---|---|---|---|---|
| 1 | S01: 60% quit/considered (p40) vs "almost two-thirds" (p59) | CONFLICT (inside the source; resolved) | p40: "This year the percentage of maintainers who have either quit or considered quitting their work was 60%, which is consistent with the 58% in 2023 and 59% in 2021." p59: "Almost two-thirds of maintainers have quit or considered quitting their maintenance work." | Tidelift 2024 PDF¹ · pp. 40, 59 | Same question and base (n=350). p59 is narrative with no supporting figure. **Use 60%.** |
| 2 | S01: 60% unpaid (single choice) vs 47% not paid (multi-select) | CONFIRMED | p13: "even though the earlier question taught us that 60% of maintainers consider themselves unpaid hobbyists, when prompted with a set of potential income sources, only 47% report that they do not get paid to maintain projects." | Tidelift 2024¹ · pp. 4, 13–14 | Different questions (n=437 vs n=421). Both are valid. |
| 3 | S02: 52% vs 53% "not compensated" | CONFLICT (inside the source; resolved) | p26: "from 49% to 52%" and, on the same page, "(53% in 2023 vs. 49% in 2021)". p25 chart: "+3%" only. Tidelift 2024 p38: "(49% in 2021 and 52% in 2023)" | Tidelift 2023 PDF² · pp. 25–26; 2024¹ p38 | Same question and base (n=253). **Use 52%.** Correction to the inventory: both numbers are in the p26 *text*. It is not "chart vs text". |
| 4 | Repo note: OMF says "59% … considered quitting; 60% work unpaid (Tidelift 2024)" | CONFIRMED (OMF needs an erratum) | Tidelift 2024 p40 (quote in #1). Tidelift 2021 p19: "a whopping 59% of maintainers we surveyed have quit or considered quitting maintaining a project." | 2024¹ p40; 2021³ p19 | Erratum drafted: `errata-draft-omf-59pct.md`. |
| 5 | S03 Tidelift 2021 "not opened directly" (59%; 49/45/40; n=335) | CONFIRMED (primary now opened; upgrade to High) | p15: "Not financially compensated enough / at all for my work \| 49%", "Adds to my personal stress \| 45%", "Feel underappreciated or like the work is thankless \| 40%", "n=335"; p19 quote in #4 | 2021³ · pp. 15, 19 | Also at https://www.sonarsource.com/the-tidelift-maintainer-survey.pdf (same SHA-256). The 2024 report's p38 caption "n=253 (2021)" conflicts with the 2021 report's n=335. 335 is correct. |
| 6 | Tidelift corporate status: definitive agreement, no closing announcement | CONFIRMED (closing UNVERIFIED) | "Sonar … today announced that it has signed a definitive agreement to acquire Tidelift" | https://www.sonarsource.com/company/press-releases/sonar-to-acquire-tidelift/ (17 Dec 2024) | No primary closing notice found. Circumstantial: tidelift.com now 301-redirects to sonarsource.com, and SiliconANGLE (19 Feb 2025, secondary) says Sonar "bought" Tidelift. Keep "definitive agreement". |
| 7 | S07: $7.7B is an extrapolation from 159 orgs | CONFIRMED | "159 organizations from the survey provided either labor or financial contribution information that was greater than zero." … "we estimate that organizations contribute $7.7 billion annually to OSS." … "Our primary assumption is that the distribution of organization contribution in the wider population follows the distribution of observed commits to public GitHub repositories" | https://opensourcefundingsurvey2024.com/ · Key Findings | Order-of-magnitude estimate. |
| 8 | Don't divide S10 $8.8T by S07 $7.7B | CONFIRMED | HBS p3: "the demand-side value is much larger at $8.8 trillion"; LF: "approximately $7.7 billion is invested across the entire open source ecosystem annually" | HBS⁴ p3; LF blog⁵ | Different constructs: replacement value vs organizational investment. |
| 9 | S14 33% + ~30% vs S15 77% | CONFLICT: 77% UNVERIFIED | See §3 | STA post⁶; STA eval⁷ PDF p8 | Same survey. 77% is not derivable from the published figures. |
| 10 | Solo maintainers: Tidelift 2023 44% vs STA 31% | CONFIRMED (both correct; different samples and questions) | S02 p26 chart: "44% SOLO MAINTAINER" ("Do you have any co-maintainers? If so, how many?", n=326). STA: "31% of participants work alone on their projects." | 2023² p26; STA post⁶ | Add Tidelift 2024 p5: solo 61% of unpaid hobbyists vs 26% of paid (n=227 / 133). Present the range, not a point. |
| 11 | S21 thanks.dev aggregate totals | UNVERIFIED | No platform-wide total found. Canonical case confirmed: "We've committed to donating US$120,000 to open source developers over the next 12 months, transferred at $10,000 per month" … "the first 10 out of 358" … "(5%)" commission | https://canonical.com/blog/canonical-thanks-dev-giving-back-to-open-source-developers | https://opencollective.com/thanks-dev shows "Total amount contributed $165,797.02 USD". That covers only the Open Collective leg, so it is **not** an aggregate. Do not use it. |
| 12 | S25 Eghbal, *Working in Public* | UNVERIFIED (contents) | Book page exists: "Stripe Press — Working in Public" | https://press.stripe.com/working-in-public | The book was not opened, and no figures are used. Keep as context only. |
| 13 | S27 Protocol Guild ">$80M commitments" | UNVERIFIED | No primary source. Possible origin: CryptoSlate (secondary, Dec 2024): Eigen Foundation pledged 1% of EIGEN, "valued at approximately $80 million" | https://cryptoslate.com/eigen-foundation-pledges-1-of-eigen-token-8m-to-support-ethereum-development/ | A token-valued pledge, not cash. Keep UNVERIFIED, as `ORF_ERRATA.md` already says. |
| 14 | S27 PG membership 196 vs 190 "not reconciled" | CORRECTED (not a conflict; different dates) | Q3 audit (per `ORF_ERRATA.md` re-check): "membership is now 190, with a net decrease of 6 (-3.1%) members from 196 of last quarter." Live docs today: the 29 team headings sum to **190** | https://protocol-guild.readthedocs.io/en/latest/01-membership.html (last-modified 31 Aug 2026 06:44 PT); https://www.protocolguild.org/blog/20260826-q3-quarterly-audit | 196 as of 22 May 2026; 190 as of 5 Aug 2026. **Use 190 (as of 5 Aug 2026).** |
| 15 | S13 Synopsys OSSRA 2024: 96% and "2,400 / 81%" on the SBOM blog | CONFIRMED (blog); the 74% press-release figure was not re-checked | "According to the 2024 'Open Source Security Risk and Analysis' (OSSRA) report, 96% of the codebases scanned contained open source." … "The OSSRA report found that 81% of the 2,400 audited codebases had at least one public open source vulnerability." | https://www.blackduck.com/blog/software-bill-of-materials-bom.html (17 Mar 2024; the old synopsys.com URL redirects here) | Update the URL to the blackduck.com location. |
| 16 | AIxponential "44% cite burnout as primary reason", "8.8 hours per week" | UNVERIFIED | No primary source found. "44% … burnout" matches Tidelift 2023 p30, which has a different meaning: "just under half (44%) said they were experiencing burnout", a multi-select reason among those who quit or considered quitting, not a "primary reason". No source found for "8.8 hours" | 2023² p30 | Do not use. If burnout is needed, cite Tidelift 2023 p30 with its base. |
| 17 | JetBrains 2023 "73% experienced burnout" (was secondary via S29) | CONFIRMED (primary found) | "Sadly, 73% of developers have experienced burnout in their career." | https://blog.jetbrains.com/team/2023/11/20/the-state-of-developer-ecosystem-2023/ ; https://www.jetbrains.com/lp/devecosystem-2023/ | Population is *all developers* (26,348 respondents), not maintainers. Context only. |
| 18 | S12 Black Duck 93% page "p24–25, p30" / R1 "p. 25" | CORRECTED (page) | PDF p27 (printed 25): "93% of codebases contain components with no development activity in over two years." Also PDF p30 (printed 28) and the chart on PDF p24 (printed 22) | https://www.blackduck.com/content/dam/black-duck/en-us/reports/rep-ossra.pdf | Printed = PDF − 2. Cite "PDF p27 (printed 25)". 947 codebases, submitted Nov 2024–Oct 2025 (PDF p6). |
| 19 | S22 "35% of critical packages are maintained by individuals" | CORRECTED (wording) | Slide 43: "Breakdown of Owners of critical packages 65% 35% Organisations Users". Slide 51 summary: "35% of critical packages are owned by individual maintainers" | https://github.com/andrew/state-of-oss-funding (slides.pdf, pp. 43, 51) | The chart is a share of *owners*; the summary restates it as *packages*. Write "about a third of critical-package owners are individual accounts" or quote slide 51 with the caveat. |
| 20 | "Users too demanding": 2024 chart's earlier columns disagree with the 2023 text | CONFLICT (resolved) | S02 p26 text: "37% of respondents (36% in previous survey)". S03 p15: "Users are too demanding and expect too much of me \| 37%" (2021). S02 p25 chart: "-1%". S01 p38 chart: 37 / 36 / 39 | 2021³ p15; 2023² pp. 25–26; 2024¹ p38 | Three sources against one. The 2023 text has the years swapped. **Use 37% (2021), 36% (2023), 39% (2024).** |

## 2. Priority item: OMF "59%"

**Verdict: the OMF figure is WRONG for 2024.** USe Me's reading is correct.
- Tidelift 2024 reports **60%** "quit or considered quitting" (22% quit + 38% considered).
- 59% is the **2021** figure.
- The measure is "quit or considered quitting", not "considered quitting".

Quotes:
- **2024, PDF p40:** "This year the percentage of maintainers who have either quit or considered quitting their work was 60%, which is consistent with the 58% in 2023 and 59% in 2021." (n=350)
  URL: https://assets-eu-01.kc-usercontent.com/ef593040-b591-0198-9506-ed88b30bc023/d325a56f-05be-4379-bfd1-ee4776fcad41/2024-tidelift-state-of-the-open-source-maintainer-report-.pdf
- **2021, PDF p19:** "a whopping 59% of maintainers we surveyed have quit or considered quitting maintaining a project."
  URL: https://assets-eu-01.kc-usercontent.com/ef593040-b591-0198-9506-ed88b30bc023/79c06b71-8002-479f-981a-10c7f72471d7/2021_Tidelift_Maintainer_Survey_FINAL-1.pdf

OMF locations (text extraction `sources/omf-whitepaper.txt`):
- line 322: PDF p8, §1 "Documented Costs of Inaction";
- line 1939: PDF p45, Evidence Summary.

The draft erratum, with current and corrected text, is in `surveys/errata-draft-omf-59pct.md`.

Side finding: an STA post (1 Aug 2024) also uses the 2021 figure without a date: "The Tidelift Maintainer Study found that 59% of maintainers have quit or considered quitting" (https://www.sovereign.tech/news/introducing-the-fellowship-for-maintainers). Its link to the Tidelift blog now redirects to a Sonar 404.

## 3. Sovereign Tech Agency unpaid-maintainer figures

**Primary sources**
- **(a) STA news post, "What open source maintainers shared with us"** (Mirko Swillus, 9 Oct 2024).
  URL: https://www.sovereign.tech/news/what-open-source-maintainers-shared-with-us · checked 2026-10-09.
  > "of the 536 respondents, around 60% said that they would be interested in a program like this."
  > "33% of respondents stated that they are not currently paid for their work as maintainers, but would like to be. Another large proportion, around 30%, are paid, but not enough to make a living from it."
  > "31% of participants work alone on their projects."
- **(b) *2025 Sovereign Tech Fellowship – Pilot Round Evaluation*** (Near Field Research for STA; PDF dated 2 Dec 2025), PDF p8 (printed 6).
  URL: https://www.sovereign.tech/public/SovereignTechFellowship-2025-Evaluation-Report-EN.pdf · checked 2026-10-09.
  > "In spring 2024, Sovereign Tech Agency conducted a large-scale survey of open source maintainers … The survey¹ found that a significant portion (77%) of maintainers are either unpaid or cannot make a living from their work, despite a desire for financial compensation."

  **Footnote 1 cites (a):** "https://www.sovereign.tech/news/what-open-source-maintainers-shared-with-us".

**Resolution**
- **Same population, same survey.** Both figures describe the spring-2024 STA maintainer survey (536 respondents). The evaluation report's n=6 applies to the fellows evaluated, not to the 77%. The inventory's "S15, n=6" label for the 77% is therefore misleading.
- **The 77% does not follow from the cited source.** 33% + ~30% ≈ 63% of all respondents. No published STA page gives 77% or a denominator that would produce it. Possible explanations, all **UNVERIFIED**:
  - a different base, such as only respondents who answered the pay question;
  - other categories folded in;
  - confusion with Tidelift 2023's unrelated "77% of the maintainers who are not paid would prefer to get paid" (Tidelift 2023 PDF p4, n=194).
- **Secondary restatement.** GitHub's policy blog (Felix Reda, 23 Jul 2025) rounds the same survey to "a third of them are not paid at all … Another third earns some income … but is not able to make a living off this work". That gives roughly two-thirds, not 77%.
  URL: https://github.blog/open-source/maintainers/we-need-a-european-sovereign-tech-fund/

**Correct framing**
> In the Sovereign Tech Agency's spring-2024 survey of 536 maintainers, 33% were unpaid but wanted to be paid and about 30% were paid but could not make a living from it [STA, 9 Oct 2024], roughly 63% combined. STA's later Fellowship evaluation restates this as 77% while citing the same post; that figure cannot be reproduced from the published results and is not used.

## 4. Release-1 §2 headline figures

| # | Planned headline | Verdict | Exact quote | URL · page | Correct framing |
|---|---|---|---|---|---|
| H1 | 60% of maintainers are unpaid | CONFIRMED (framing) | "60% of maintainers are (still) not paid for their work" (p4); "describe themselves as unpaid hobbyists stayed identical: 60%" (p5) | Tidelift 2024¹ pp. 4–5 | "60% describe themselves as unpaid hobbyists" (single choice, n=437). 47% report no maintainer income (p13). |
| H2 | 4% of $162M direct corporate OSS spending reaches maintainers (Tidelift 2024; LF/GitHub/Harvard) | CORRECTED (attribution and scope) | "Respondents invest $162MM financially to contractors (57%), foundations and projects/communities (37%), maintainers (4%), and bounties (1%)." | LF blog⁵ (Hilary Carter and Martin Woodward, 18 Dec 2024); survey by GitHub, LF and Harvard LISH | **Not Tidelift**: the Tidelift 2024 report contains no $162M figure. Write "**respondent organizations'** direct financial contributions ($162M)". Respondents include non-profits, not only corporations; 501 organizations responded and 159 gave non-zero data. The 4% is **direct** payment to maintainers; money to foundations and contractors may also reach maintainers. |
| H3 | Quit reasons: no pay 50%, underappreciated 48%, stress 43% | CORRECTED (mislabelled) | p38: "selected by slightly more maintainers (50%) … 'not financially compensated enough/at all for my work'"; "almost half (48%)"; "(43% this year vs. 45% in 2021)" | Tidelift 2024¹ p38 (n=338) | These are **dislikes**, not quit reasons. The 2024 report did not ask why people quit. The latest quit reasons are 2023 (S02 p30): other priorities 54%, lost interest 51%, burnout 44%, not paid enough 38%. The release-1 text already says "dislikes"; keep it that way. |
| H4 | 40% of top packages have 1–2 people doing 80%+ of commits | CONFIRMED (scope) | p2: "Among top 50 non-npm projects, 17% had only one developer & 40% had one or two developers"; p24: "40% of projects had only one or two developers accounting for more than 80% of commits authored" | Census III⁸ pp. 2, 24 | "Among the top 50 non-npm projects (2023 commits), 40% had one or two developers accounting for more than 80% of commits." |
| H5 | 5% of developers create 96% of the value | CONFIRMED (scope) | p3: "96% of the demand-side value is created by only 5% of OSS developers."; p22: "those last five percent generate over 96% of the demand side value" | HBS WP 24-038⁴ PDF pp. 3, 22 | Say "**demand-side** value", measured in their sample of widely used packages. Supply-side is 93% (p22). |
| H6 | 93% of audited codebases have components untouched 2+ years | CONFIRMED (page) | "93% of codebases contain components with no development activity in over two years." | Black Duck OSSRA 2026 PDF p27 (printed 25) | 947 commercial codebases audited by Black Duck (PDF p6). This is an audit sample, not a random one. |
| H7 | 72.8% of critical packages have no way to receive money | CORRECTED (wording) | Slide 51: "72.8% of critical packages have no obvious way to financially support them"; slide 20: "Critical Package Funding Links 2,661 27.2%"; slide 17: "The critical packages are the top ~10,000 most used packages" | ecosyste.ms / Nesbitt, CHAOSScon NA 2025, slides dated 28 Jun 2025 (https://github.com/andrew/state-of-oss-funding) | "72.8% of the ~10,000 most-used ('critical') packages list **no funding link** in their metadata." This does not show that maintainers *cannot* receive money. R1's "no funding route" is close; "no way to receive money" overstates it. |

**Headline figures that are wrong or need changing:** H2 (wrong attribution to Tidelift; "corporate" overstates), H3 (dislikes mislabelled as quit reasons), H7 (overstated). None is unconfirmable.

## Footnoted URLs (all checked 2026-10-09)
1. Tidelift 2024: https://assets-eu-01.kc-usercontent.com/ef593040-b591-0198-9506-ed88b30bc023/d325a56f-05be-4379-bfd1-ee4776fcad41/2024-tidelift-state-of-the-open-source-maintainer-report-.pdf
2. Tidelift 2023: https://assets-eu-01.kc-usercontent.com/ef593040-b591-0198-9506-ed88b30bc023/d3df3f32-2b39-419a-8a99-7a4915a4e9ca/Tidelift-2023-open-source-maintainer-survey-1.pdf
3. Tidelift 2021: https://assets-eu-01.kc-usercontent.com/ef593040-b591-0198-9506-ed88b30bc023/79c06b71-8002-479f-981a-10c7f72471d7/2021_Tidelift_Maintainer_Survey_FINAL-1.pdf
4. HBS WP 24-038: https://www.hbs.edu/ris/Publication%20Files/24-038_51f8444f-502c-4139-8bf2-56eb4b65c58a.pdf
5. LF blog: https://www.linuxfoundation.org/blog/understanding-the-state-of-open-source-funding-in-2024
6. STA post: https://www.sovereign.tech/news/what-open-source-maintainers-shared-with-us
7. STA evaluation: https://www.sovereign.tech/public/SovereignTechFellowship-2025-Evaluation-Report-EN.pdf
8. Census III: https://www.linuxfoundation.org/hubfs/LF%20Research/lfr_censusiii_120424a.pdf
