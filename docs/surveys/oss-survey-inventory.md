# OSS Maintainer Sustainability & Funding — Survey and Study Inventory (2019 – Oct 2026)

> **Status:** OSFL research note · **Stage 0** · no ORF Hard Gate is passed by anything in this file.
> **Prepared:** 9 Oct 2026, 05:17–05:45 PT, executor research pass. **Not pushed to GitHub.**
> **Role of this file:** supporting evidence for `crisis-to-model-map.md` (verdict + scorecard) and `release1-section-2-survey-crisis-map.md`. The whitepapers (dOSPO v1.0, OMF v1.0, ORF v1.0 as corrected by `whitepapers/ORF_ERRATA.md`) are canonical; nothing here proposes changes to them.
> **Access date for every URL:** 9 Oct 2026 (PT) unless noted. Raw captures are in `surveys/data/` (PDFs, HTML, and `pdftotext -layout` text). Page numbers are **PDF page numbers** of the captured file.
> **Rules applied:** live/primary sources only; no invented numbers; Tidelift is described as under a **definitive agreement** announced by Sonar (Dec 2024) — no closing announcement was found on 9 Oct 2026; anything not opened from a primary page is marked **Unverified**.

## Count

**30 entries.** 26 were opened from a primary capture in this pass (S01, S02, S04–S12, S14–S24, S26, S28–S30). 4 were not re-captured by me: S03 (Tidelift 2021; since opened directly from Researchy's capture in `surveys/sources/`), S13 (Synopsys 2024, carried from the repo's errata), S25 (Eghbal, not opened — Unverified), S27 (Protocol Guild, captured earlier in `chains/data/`). Of the 30, 21 are surveys or measured studies of maintainers, users, codebases or registries; the rest are program reports, methodology or qualitative works used as context for how money moves.

Confidence key: **High** = primary document opened, method stated, figure located on page. **Medium** = primary page opened but method thin, self-reported, vendor sample, or extrapolated. **Low** = secondary or counter-only. **Unverified** = not located on a primary page.

## Summary table

| ID | Publisher · title | Year | Sample / method | Headline findings (exact, with location) | URL | Conf. |
|---|---|---|---|---|---|---|
| S01 | Tidelift · *2024 State of the Open Source Maintainer Report* | Sep 2024 | 437 maintainers, social campaign Jul–Aug 2024, self-selected, screened (p2). Per-question n varies (e.g. n=338 on dislikes, p38) | 60% self-describe as unpaid hobbyists (16% don't want pay + 44% would like it), 12% professional, 24% semi-pro (p4–5). Multi-select: 47% report not being paid (p13–14). Only 5% get income directly from companies; 3% from foundations; 1% from governments (p16). 60% have quit (22%) or considered quitting (38%), vs 58% 2023, 59% 2021 (p40). 48% feel underappreciated/thankless; 50% dislike not being compensated; 43% say it adds to personal stress (p38). Paid maintainers on average 55% more likely to implement critical security/maintenance practices (p27). 82% of professionals work >20 h/wk; 78% of unpaid hobbyists ≤10 h/wk (p10). 13% have a succession plan, 63% would if paid (p36). 66% of those aware of xz are less trusting of contributors (p43) | [PDF](https://assets-eu-01.kc-usercontent.com/ef593040-b591-0198-9506-ed88b30bc023/d325a56f-05be-4379-bfd1-ee4776fcad41/2024-tidelift-state-of-the-open-source-maintainer-report-.pdf) | High (self-selected sample) |
| S02 | Tidelift · *2023 State of the Open Source Maintainer Report* | Apr 2023 | 339 maintainers (378 in prior wave), Tidelift email lists + social, Nov–Dec 2022 | 60% unpaid hobbyists (p3). "Almost 60%" quit or considered quitting (p28). Stress #1 dislike, 54% (vs 45%); not compensated 52% (p26; the same page's text also prints 53%, a typo, and S01 p38 confirms 52%); lonely 42% (vs 36%); "users are too demanding" 36% (vs 37% in 2021; the p26 text swaps the years, per S02 p25 chart "-1%", S03 p15 and S01 p38); "asked to comply with requirements I don't have time for" 38% (p26). 44% are solo maintainers (p26) | [PDF](https://assets-eu-01.kc-usercontent.com/ef593040-b591-0198-9506-ed88b30bc023/d3df3f32-2b39-419a-8a99-7a4915a4e9ca/Tidelift-2023-open-source-maintainer-survey-1.pdf) | High |
| S03 | Tidelift · *2021 Tidelift open source maintainer survey* | 2021 | "Nearly 400" maintainers (p2); dislikes n=335 (p15); pay question n=378 (p3) | 59% quit or considered quitting (p19). Dislikes: not compensated 49%, stress 45%, underappreciated 40%, users too demanding 37%, lonely 36% (p15) | [PDF](https://assets-eu-01.kc-usercontent.com/ef593040-b591-0198-9506-ed88b30bc023/79c06b71-8002-479f-981a-10c7f72471d7/2021_Tidelift_Maintainer_Survey_FINAL-1.pdf) (opened via Researchy's capture `surveys/sources/tidelift-2021-open-source-maintainer-survey.pdf`) | High (self-selected sample) |
| S04 | Linux Foundation + Harvard LISH · *Report on the 2020 FOSS Contributor Survey* | Dec 2020 | 1,196 respondents completing demographics + ≥1 contribution question (p4) | Contributors spend on average 2.27% of contribution time on security and do not wish to increase it (p5). 48.7% are paid by their employer to contribute (p6, p14); 51.65% paid to develop FOSS (p4) | [PDF](https://www.linuxfoundation.org/hubfs/2020FOSSContributorSurveyReport_121020.pdf) | High |
| S05 | LF + Harvard LISH · *Census II of FOSS — Application Libraries* | Mar 2022 | >500,000 SCA usage observations from 2020 (Snyk, Synopsys, FOSSA) | In one dataset, 136 developers were responsible for >80% of lines of code added to the top 50 packages (p20). Legacy packages persist | [PDF](https://www.linuxfoundation.org/hubfs/Census%20II%20FINAL%202March2022.pdf) | High |
| S06 | LF Research + OpenSSF + Harvard LISH · *Census III of FOSS* | Dec 2024 | >12 million SCA data points on 2023 usage from >10,000 companies (FOSSA, Snyk, Sonatype, Black Duck) (p5, p11) | Among top 50 non-npm projects, 17% had one developer and 40% had one or two developers accounting for >80% of commits (p2). Many top packages sit under individual (not org) accounts (p2) | [PDF](https://www.linuxfoundation.org/hubfs/LF%20Research/lfr_censusiii_120424a.pdf) | High |
| S07 | LF Research + GitHub + Harvard · *2024 Open Source Software Funding Report* | 2024 | 501 organizations responded; 159 gave non-zero contribution data; extrapolated using GitHub commit distribution | Respondents invest $1.7B/yr; extrapolated ≈$7.7B/yr across organizations; 86% labor, 14% direct financial; median org $520,600; the $162M direct financial goes 57% contractors, 37% foundations/projects, **4% maintainers**, 1% bounties (LF blog "Understanding the State of Open Source Funding in 2024", Hilary Carter and Martin Woodward, 18 Dec 2024; report site §Key findings). The $162M is **respondent organizations'** direct financial contributions only (501 responded, 159 gave non-zero data; includes non-profits), and the 4% is direct payment to maintainers; money via foundations or contractors may also reach maintainers. **Not a Tidelift figure.** | [blog](https://www.linuxfoundation.org/blog/understanding-the-state-of-open-source-funding-in-2024) · [report](https://opensourcefundingsurvey2024.com/) | Medium (extrapolation) |
| S08 | LF Research · *Open Source Maintainers* | 2023 | Qualitative interviews with 32 "super maintainers" of critical projects | Qualitative: workload, community building, and remuneration challenges; no prevalence figures | [PDF](https://project.linuxfoundation.org/hubfs/LF%20Research/Open%20Source%20Maintainers%202023%20-%20Report.pdf) | High (qualitative only) |
| S09 | LF Research · *The State of Global Open Source 2025* | Oct 2025 | 851 survey responses (p6) | Only 26% of organizations have an OSPO; 34% have a clear OSS strategy (p5, p9) | [PDF](https://www.linuxfoundation.org/hubfs/Research%20Reports/2025GlobalSpotlight%5FOct-27-2025%20V4.pdf) | High |
| S10 | Hoffmann, Nagle, Zhou · *The Value of Open Source Software* (HBS WP 24-038) | 2024 | Census II usage data + labor-market replacement costs | Supply-side value $4.15B; demand-side $8.8T; firms would spend 3.5× more on software without OSS; 96% of demand-side value created by 5% of OSS developers (p3; p19–23) | [PDF](https://www.hbs.edu/ris/Publication%20Files/24-038_51f8444f-502c-4139-8bf2-56eb4b65c58a.pdf) · [page](https://www.hbs.edu/faculty/Pages/item.aspx?num=65230) | High |
| S11 | Sonatype · *2026 State of the Software Supply Chain* (covers 2025) | 2026 | Vendor telemetry: Maven Central, PyPI, npm, NuGet, Hugging Face | 9.8T downloads in 2025 (p7); 454,648 new malicious packages in 2025, 1,233,219 cumulative since 2019 (p20–21). Top 3 cloud providers = 32.5% of IPs but 86.4% of Maven Central downloads (p14). "Volunteer maintainers absorb the strain" (p8). Growing dependence on EOL/abandoned components (p32) | [PDF](https://www.sonatype.com/hubfs/1-2025_Website-Assets/SSCR_2025/SSCR_2026_final.pdf) | Medium (vendor data) |
| S12 | Black Duck · *2026 OSSRA* | Feb 2026 | 947 commercial codebases audited by Black Duck Audit Services (p6) | OSS in 98% of codebases (p8). 93% contain components with no development activity in 2+ years (PDF p27, printed p25; chart PDF p24); 92% contain components 4+ years out of date (PDF p30, printed p28). Printed page = PDF − 2 | [PDF](https://www.blackduck.com/content/dam/black-duck/en-us/reports/rep-ossra.pdf) | Medium (audit sample, not random) |
| S13 | Synopsys · OSSRA 2024 (repo-cited) | 2024 | Audited codebases | 96% of codebases contain OSS (SBOM blog); press release states 74% high-risk; conflicting "2,400 codebases / 81%" line on same blog — per `ORF_ERRATA.md` | per errata | Medium (carried from repo) |
| S14 | Sovereign Tech Agency · Maintainer fellowship survey | 2024 | 536 respondents, open survey (STA news post) | 33% unpaid but want pay; ~30% paid but can't make a living; 31% work alone; ~60% interested in a fellowship | [post](https://www.sovereign.tech/news/what-open-source-maintainers-shared-with-us) | Medium (open survey; summary only) |
| S15 | STA / Near Field Research · *Sovereign Tech Fellowship 2025 Evaluation* | 2025/26 | Evaluation of 6 fellows (p8, p10) | Restates S14's survey (same spring-2024 survey of 536, cited in its footnote 1) as "77% unpaid or cannot make a living" (PDF p8). That cannot be reproduced from S14's 33% + ~30% (~63%): **77% Unverified, not used**. Fellowship model reported to reduce technical debt and burnout (qualitative; n=6 is the fellows evaluated, not the 77%) | [PDF](https://www.sovereign.tech/public/SovereignTechFellowship-2025-Evaluation-Report-EN.pdf) | Medium |
| S16 | STA · Technologies page (program data) | live | Program counter | 118 technologies supported since Oct 2022; €41.1M invested in commissioned work; 195 critical technologies identified | [page](https://www.sovereign.tech/tech) | Medium (counter) |
| S17 | Alpha-Omega (LF/OpenSSF) · *2025 Annual Report* | Jul 2026 | Program report | 31 grants to 18 organizations in 2025, $6,155,410 total, average $198,562; packaging repositories 29.8% of 2025 grants ($2,929,702); $19,674,118 since inception (p26). Backers: AWS, Citi, Google, Microsoft | [PDF](https://alpha-omega.dev/wp-content/uploads/sites/22/2026/07/Alpha-Omega-Annual-Report-2025_073126a.pdf) | High (program report) |
| S18 | GitHub · Secure Open Source Fund results | 2025–26 | Program reports (blog) | Each project gets $10,000 (≈$6,000 during the sprint); across sessions: 138 projects, 219 maintainers, $1.38M, 191 new CVEs (Session 3 post); Sessions 1–2: 125 maintainers / 71 projects, >1,100 CodeQL vulnerabilities remediated | [S1–2](https://github.blog/open-source/maintainers/securing-the-supply-chain-at-scale-starting-with-71-important-open-source-projects/) · [S3](https://github.blog/open-source/maintainers/securing-the-ai-software-supply-chain-security-results-across-67-open-source-projects/) | Medium (self-reported outcomes) |
| S19 | GitHub · *Octoverse 2025* | Oct 2025 | Platform telemetry | 180M+ developers; 36M+ joined in a year; 1.12B contributions to public repos (+13%) | [blog](https://github.blog/news-insights/octoverse/octoverse-a-new-developer-joins-github-every-second-as-ai-leads-typescript-to-1/) | High (context only — no funding data) |
| S20 | Open Source Pledge · member reports | live | Self-reported member annual reports; Pledge "does not carry out any in-depth validation" (member pages) | Members have paid maintainers $7,421,535 total, $3,756,826 in the past year; norm is $2,000 per FTE developer per year; Pledge handles no funds | [members](https://opensourcepledge.com/members/) · [about](https://opensourcepledge.com/about/) | Medium (self-reported) |
| S21 | thanks.dev | — | No aggregate report found | Case only: Canonical committed $120,000 over 12 months ($10,000/month), split across 358 recipients by dependency usage, 5% platform commission (Canonical blog, 2025) | [Canonical](https://canonical.com/blog/canonical-thanks-dev-giving-back-to-open-source-developers) | Low (aggregate **Unverified**) |
| S22 | ecosyste.ms / A. Nesbitt · *State of OSS Funding Data* (CHAOSScon NA 2025) | 2025 | Dataset: 11.4M packages, 262M repos, 1.7M maintainers, 22B dependencies | Only 3.26% of packages have funding links; 72.8% of the ~10,000 most-used ("critical") packages list no funding link in their metadata (slide 51: "no obvious way to financially support them"); this is missing metadata, not an inability to receive money. About a third of critical-package owners are individual accounts (35%, slide 43; slide 51 restates it as packages); well-funded maintainers concentrate on more critical packages | [repo](https://github.com/andrew/state-of-oss-funding) | Medium (talk README; slides not parsed) |
| S23 | CHAOSS / STA / NGI Commons / LF · *Toolkit for Measuring the Impacts of Public Funding on OSS* | 2024 | Methodology paper | No prevalence figures; mixed-methods impact measurement | [STA post](https://www.sovereign.tech/news/measuring-the-impact-of-our-funding) | Medium (method only) |
| S24 | Ford Foundation · *Roads and Bridges* (Eghbal) + Ford/Sloan *Critical Digital Infrastructure Research* | 2016 / 2019 | Qualitative report; 13 funded research projects ($1.3M) | Baseline (pre-window): infrastructure maintained by volunteers; money alone won't fix it; recommends long-term, decentralized stewardship. 2019–20 cohort reported burnout across projects (qualitative) | [R&B](https://www.fordfoundation.org/wp-content/uploads/2016/07/roads-and-bridges-the-unseen-labor-behind-our-digital-infrastructure.pdf) · [CDI](https://www.fordfoundation.org/learning/library/learning-reflections/critical-digital-infrastructure-research/) | High (qualitative) |
| S25 | Eghbal · *Working in Public* (Stripe Press) | 2020 | Book | Not opened; no figures used | — | **Unverified** |
| S26 | Electric Capital · *2024 Crypto Developer Report* | Dec 2024 | GitHub commit analysis | Total developers down 7% in 2024; 39,148 new developers; established (2+ yr) developers +27% and 70% of commits. Annual report retired from 2025 (replaced by Open Dev Data) | [2024](https://electriccapital.substack.com/p/2024-crypto-developer-report) · [retirement](https://electriccapital.substack.com/p/announcing-open-dev-data) | Medium |
| S27 | Protocol Guild (pack capture) | 2026 | Annual report + quarterly audits | $12.4M distributed in 2025; $7,231,668 raised from 6,202 donors (Validated in `chains/top10-chains-orf-alignment.md`). Membership: 190 as of 5 Aug 2026 (Q3 audit: net −6 from 196 the prior quarter, which is the 22 May 2026 figure in `ORF_ERRATA.md`). Not a conflict; use 190. ">$80M commitments" **Unverified** | `chains/data/pg-*` | Medium |
| S28 | Gitcoin program counters · Optimism Retro Funding (errata) | live / 2025 | Site counters; Foundation budget narrative | Gitcoin: 3,715 projects, 3.8M donations, $50M+ (site counters, no audit trail). Optimism: 26.4M OP via Retro Funding to 437 grantees (Year 3 update). **Neither is replenishment** under ORF | [gitcoin](https://gitcoin.co/program) · errata | Low/Medium |
| S29 | Heath · *Report on Burnout in OSS* (funded by Sentry / Open Source Pledge) | Nov 2025 | Interviews + literature + 50 community texts | Six drivers: difficulty getting paid, workload, unrewarding maintenance, toxic behaviour, hyper-responsibility, pressure to prove oneself; recommends pay with preserved autonomy | [PDF](https://mirandaheath.website/static/oss_burnout_report_mh_25.pdf) | Medium (qualitative) |
| S30 | Perforce OpenLogic + OSI + Eclipse · *2026 State of Open Source* | 2026 | 700+ OSS users | Among enterprises with 5,000+ employees, 60% spend at least half their time on maintenance/production issues (OSI blog) | [OSI](https://opensource.org/blog/the-2026-state-of-open-source-report) | Medium (secondary summary; report gated) |


## Per-survey notes (method caveats and conflicts)

- **S01/S02/S03 Tidelift.** The most-cited maintainer series and the only one asking the same questions across three waves, which makes the trend lines (stable ~60% unpaid; ~58–60% quit/considered) its strongest feature. Weaknesses: self-selected respondents recruited via Tidelift channels and social media; per-question n drops (338 of 437 on dislikes). Internal inconsistencies: S01 says 60% quit/considered (p40) but its conclusion says "almost two-thirds" (p59); single-choice 60% unpaid (p4) vs multi-select 47% not paid (p13) — both are correct answers to different questions; quote the one that matches the claim. S02 prints both 52% and 53% for "not compensated" in the p26 text (the p25 chart shows only "+3%"); use 52%, as S01 p38 does. Resolved: use 60% quit/considered (p40, n=350); p59's "almost two-thirds" is loose narrative. 60% (single choice, n=437, p4) and 47% (multi-select, n=421, p13) are both valid if labelled. **Repo note:** the OMF whitepaper's crisis table states "59% of maintainers have considered quitting; 60% work unpaid (Tidelift 2024)". The 2024 report says 60% quit *or* considered quitting (59% was 2021), and 60% *self-describe as unpaid hobbyists*. Reported here as evidence only; whitepaper text is not changed by this note.
- **Tidelift corporate status.** Sonar announced a definitive agreement to acquire Tidelift (17 Dec 2024). No closing announcement found on 9 Oct 2026. The Heath report (S29) says "acquired by Sonar in 2024"; that is secondary and not adopted.
- **S04** is the strongest evidence on security time (2.27%), but it is 2020 data.
- **S05/S06 Census II/III** are usage censuses built from SCA vendor scans, not surveys of people. Their concentration findings are measured from commit/LOC data and are the best evidence for "critical infrastructure rests on few people".
- **S07** $7.7B is an extrapolation from 159 organizations under a stated assumption; treat as an order-of-magnitude estimate. **Do not divide S10's $8.8T by S07's $7.7B** — one is demand-side value, the other organizational investment; they are different constructs.
- **S11/S12** are vendor datasets (registry telemetry; M&A-style audits). Sonatype's 2025 malware count is dominated by Q4 automated campaigns (Q4 blog). Useful for direction and magnitude of security debt, not prevalence among maintainers.
- **S14 vs S15.** Both describe the same spring-2024 STA survey of 536 maintainers. Use S14: 33% unpaid-wanting-pay + ~30% underpaid (~63%, derived). S15's 77% cannot be reproduced from the published results: **Unverified, not used**. S15's n=6 is the number of fellows evaluated.
- **Solo-maintainer conflict.** Tidelift 2023: 44% solo (S02 p26). STA 2024: 31% work alone (S14). Different samples and question wording; the range, not a point, is defensible.
- **S20 Pledge** totals are self-reported, unvalidated; Pledge holds no funds — it is a norm, not an intermediary.
- **S21 thanks.dev** has no aggregate report on a primary page; only a single donor case.
- **S26 Electric Capital** measures developer activity, not pay or burnout.
- **S27/S28** are Web3 funding mechanisms. Under the ORF policy notices, Retro Funding, Gitcoin, Drips and Superfluid are allocation or routing, **not replenishment**, and issuance never counts.
- **Not used (secondary, unverifiable):** AIxponential (Apr 2026) "44% cite burnout as primary reason" and "8.8 hours per week" — no primary source located (**Unverified**). JetBrains 2023 "73% of developers have experienced burnout" is confirmed at source (https://blog.jetbrains.com/team/2023/11/20/the-state-of-developer-ecosystem-2023/), but its population is **all developers** (26,348 respondents), not maintainers. Context only; not used as maintainer evidence. Also still **Unverified**: thanks.dev aggregate totals; Protocol Guild ">$80M".

## Tidelift detail (spine for the project-needs taxonomy)

The needs taxonomy in `crisis-to-model-map.md` and in section 2 follows the Tidelift reports' own question structure. All figures are exact, with PDF page. "2024" = S01 (n=437), "2023" = S02 (n=339), "2021" = S03 (opened directly; dislikes n=335, S03 p15). Tidelift 2024 is cited by its PDF URL (S01 row), not the tidelift.com survey page, which now redirects. Per-question n is given where Tidelift prints it.

**T1. Paid vs. unpaid status (2024 Headline #1)**
- 60% describe themselves as unpaid hobbyists (single choice, n=437; 16% wouldn't want pay + 44% would like it); 24% semi-professional; 12% professional (p4–5). 2023: 60% unpaid; 13% professional; 23% semi-pro (S02 p3).
- 36% describe themselves as paid (professional or semi-professional) (p8). Not "paid at all": see next line.
- Multi-select framing (n=421): 47% report receiving no maintainer income at all (46% in both earlier surveys) (p13–14).

**T2. What pay buys; how maintainers want to be paid (Headline #2)**
- Paid maintainers (n=142), improvements made because they are paid (p8):
  - 83% spend more time maintaining
  - 64% work on feature requests
  - 52% research and respond to security issues and bugs
  - 51% improve secure-development practices
  - 45% prioritize remediating vulnerabilities
  - 26% bring on additional maintainers
- Professionals vs. semi-pros: 96% vs 77% spend more time; 64% vs 36% prioritize vulnerability remediation (p9–10).
- Time worked: 82% of professionals work >20 h/week; 78% of unpaid hobbyists work ≤10 h/week (p10).
- **Payment form: 81% prefer predictable monthly income; 7% prefer a one-time lump sum; 13% not sure/other (n=344) (p11).**

**T3. Who pays (Headline #3)**
- 32% receive income from another organization or individual (31% in 2023, 32% in 2021) (p14).
- 24% are paid by their employer as an explicit job duty (28% in 2023, 27% in 2021) (p14–15).
- Sources (n=421, p15):

  | Source | 2024 | Earlier |
  |---|---|---|
  | Donation programs (GitHub Sponsors, Open Collective, Patreon) | 25% | 16% (2021), 24% (2023) |
  | Tidelift | 19% | 15% (2021), 16% (2023) |
  | Direct from companies | 5% | — |
  | Direct from individuals | 5% | 10% (2021) |
  | Foundations | 3% | — |
  | Governments | 1% | — |

- Note: the publisher is itself a payment source. 70% of respondents were not Tidelift partners (p15). Tidelift is now under a definitive agreement announced by Sonar.

**T4. Time allocation (Headline #4)**
- Security work: 11% of maintainer time vs 4% in 2021.
- Day-to-day maintenance: 50% vs 53%. New features: 35% vs 25%.
- Seeking financial support/sponsors: 2% (n=378) (p17–18).
- Paid vs. unpaid: security 13% vs 10%; maintenance 53% vs 48% (p19).

**T5. Security standards and practices (Headlines #5–6)**
- Awareness: 40% know the OpenSSF Scorecard (28% in 2023); 39% know NIST SSDF; 40% are aware of none (52% in 2023) (p20).
- Scorecard alignment: 30% of aware maintainers have begun aligning; 40% have no plans (p21).
- Practices implemented (p24):

  | Practice | Share |
  |---|---|
  | 2FA | 71% (54% in 2023, p26) |
  | Static analysis | 65% |
  | Fixes and recommendations for vulnerabilities | 60% |
  | Disclosure plan | 52% |
  | Secrets management | 46% |

- Paid maintainers are 8–26 points (on average 55%) more likely to implement these. Gaps: disclosure plan +23, signed releases/provenance +22, secrets management +19 (p27).
- 2023, why maintainers don't plan to align with standards (asked of the 48% with no plans; n=119, p13): no time 38%; not paid 37%; not enough resources 24%.
- 2023, support that would help them align: help understanding standards 54%; getting paid 47%; help doing the work 34% (p14).

**T6. Maintenance and documentation practices (Headline #7)**
- Implemented today, and the share including those who say they would implement if paid (stated intent, n=359) (p30, p35):

  | Practice | Today | If paid |
  |---|---|---|
  | Reproducible/verifiable builds | 53% | 82% |
  | Backward-compatibility policy | 46% | 77% |
  | Dependency-management process | 40% | 66% |
  | Multi-reviewer peer review | 37% | 61% |
  | PR/issue prioritization process | 14% | 53% |

- Documentation implemented today: license 93%; release notes 76%; contributor guide 61%; code of conduct 53% (p32).
- Succession plan: 13% today, 63% including those who would if paid (n=353). Conflict-resolution process: 17% today, 50% including would-if-paid (p36). Both are stated intent.

**T7. Dislikes (Headline #8)**
- Shares (n=338 in 2024; n=253 in 2023; n=335 in 2021, per S03 p15 and S02 p25; the S01 p38 caption "n=253 (2021)" is an error) (p38–39):

  | Dislike | 2024 | 2023 | 2021 |
  |---|---|---|---|
  | Not financially compensated | 50% | 52% | 49% |
  | Underappreciated/thankless | 48% | not asked | 40% |
  | Adds to personal stress | 43% | 54% | 45% |
  | Users too demanding | 39% (chart only) | 36% | 37% (S03 p15) |
  | Asked to comply with requirements I don't have time for | 39% (chart) | 38% (S02 p26) | — |
  | Can be lonely | 32% (p39) | 42% | 36% (S03 p15) |
  | Takes too much time | 17% | 21% | 31% |

- "Users too demanding" settled: 37% (2021), 36% (2023), 39% (2024). The S02 p26 text ("37% … 36% previous") swaps the years; the S02 p25 chart ("-1%"), S03 p15 and the S01 p38 chart agree on 37/36.
- These are **dislikes**. The 2024 report did not ask quit reasons; the latest quit reasons are 2023 (T8).

**T8. Quitting and what would have kept maintainers (2024 p40; 2023 Headlines #8–9)**
- 60% quit (22%) or considered quitting (38%) in 2024; 58% in 2023 (22% + 36%); 59% in 2021 (S01 p40, n=350 for 2024; S03 p19 for 2021; S02 p29).
- 2023 reasons, among those who quit or considered it (n=265 or 349, Unverified: captions disagree; S02 p30):
  - other priorities 54%
  - lost interest 51%
  - burnout 44%
  - not paid enough 38% (up from 32%)
  - took too much time 36% (down from 44%)
- 2023 support that might have kept them, asked **only of those who quit or considered quitting** (n=153; S02 p31):
  - more income 56% (chart; the p32 text says 57%), joint top with co-maintainer help
  - help finding a maintainer to share responsibilities 56%
  - help finding another experienced maintainer to "take over some of my projects so I can focus on those that interest me most" 40% (not a full successor)
  - diverse collaborators 33%
  - community/networking 21%
  - mentorship on security/maintenance requirements 14%
- 2023 value of non-financial support, "extremely or somewhat valuable" (n=261; S02 p32–33):
  - improving user/contributor experience 89%
  - documentation 87%
  - marketing to find contributors 75%
  - retaining contributors 74%
  - succession planning / finding co-maintainers 71%
  - triage of issues/PRs 69%

**T9. Community-building efforts (2023 Headline #10; S02 p34–35)**
- Welcoming atmosphere 67%
- Onboarding/outreach 35%
- Mentorship (Outreachy, GSoC) 28%
- Tools for non-developer contributions 27%
- Efforts to address project burnout 20%
- Conflict-resolution process 14%
- None 17%

**T10. What maintainers enjoy (2023 Headline #6; S02 p24)**
- Working on projects that matter 83% (59% previously)
- Receiving recognition 57% (43% previously)
- Getting paid 35% (21% previously)

**T11. Trust, AI, demographics (2024 Headlines #9–12)**
- 66% of those aware of xz are less trusting of contributors or vet them more (n=307, p43).
- 45% expect AI coding tools to have a negative impact (p47).
- Maintainers under 26: 25% (2021) → 12% (2023) → 10% (2024) (p58). 45% have maintained for more than 10 years (p59).


## Captures (`surveys/data/`)
`tidelift-2024-maintainer-report.pdf`, `tidelift-2023-maintainer-report.pdf`, `lf-harvard-foss-contributor-survey-2020.pdf`, `lf-census-ii-2022.pdf`, `lf-census-iii-2024.pdf`, `lf-oss-funding-2024.html`, `lf-funding-blog-2024.html`, `lf-open-source-maintainers-2023.pdf`, `lf-global-os-2025.pdf`, `hbs-value-of-oss-24-038.pdf`, `sonatype-sscr-2026.pdf`, `blackduck-ossra-2026.pdf`, `sta-maintainers-shared-2026-10-09.html`, `sta-fellowship-eval-2025.pdf`, `sta-tech-2026-10-09.html`, `alpha-omega-annual-2025.pdf`, `github-sosf-sessions1-2.html`, `github-sosf-session3.html`, `octoverse-2025-2026-10-09.html`, `opensourcepledge-members-2026-10-09.html`, `opensourcepledge-about-2026-10-09.html`, `canonical-thanksdev-2025.html`, `ecosystems-state-of-oss-funding-README.md`, `ford-roads-and-bridges-2016.pdf`, `ford-cdi-research-2019.html`, `electric-capital-2024-report.html`, `electric-open-dev-data.html`, `gitcoin-program-2026-10-09.html`, `heath-burnout-report-2025.pdf`, plus `.txt` extractions and `SHA256SUMS.txt`.

---

## Changelog

**9 Oct 2026, ~05:35–06:05 PT: Researchy fact-check fixes applied** (rows where the figure appears)
- S02: 52% (not chart vs text); users too demanding 36% (2023) / 37% (2021).
- S03: upgraded to primary (2021 PDF; n "nearly 400"; dislikes n=335; 59% p19); confidence High.
- S07: $162M attributed to the LF/GitHub/Harvard blog (18 Dec 2024); respondent organizations' direct contributions only; not Tidelift.
- S12: 93% at PDF p27 (printed p25); printed = PDF − 2.
- S14/S15: same survey; ~63% derived; 77% Unverified, not used; n=6 = fellows.
- S22: 72.8% = no funding link in metadata; 35% = owners.
- S27: 190 as of 5 Aug 2026 (196 was the prior quarter); not a conflict.
- Notes: Tidelift contradictions resolved (60% p40; 60% vs 47% both valid; 52%); JetBrains 73% confirmed, all developers, context only; still Unverified: thanks.dev totals, Protocol Guild >$80M, AIxponential.
- Tidelift blocks:
  - T1: "describe themselves" wording; 36% paid vs 47% no income.
  - T5: n=119 for standards reasons.
  - T6: stated intent noted.
  - T7: 2021 n=335; 2021/2023 cells filled; dislikes ≠ quit reasons.
  - T8: quit n Unverified; base and "take over some of my projects" wording; 56/57 note.
- Tidelift 2024 cited by PDF URL.
