# Tidelift (Sonar)

> **Pass date:** 2026-10-27 PT
> **Stage 0 reference profile.** No Hard Gate is passed. Nothing here is an audit.
> **Category:** Commercial maintainer-payment model, now inside a code-quality vendor
> **OSF mapping:** ORF **Family B** (enterprise subscriptions fund payments to maintainers) · OMF (maintainers paid to meet published practice standards)
> **Related files in this repo:** [`docs/PRIOR_ART_AND_COMPETITIVE_ANALYSIS.md`](../../PRIOR_ART_AND_COMPETITIVE_ANALYSIS.md) §4.6, [`docs/EVIDENCE_REGISTER.md`](../../EVIDENCE_REGISTER.md), [`docs/surveys/oss-survey-inventory.md`](../../surveys/oss-survey-inventory.md) (S01–S03)

## What they do

Tidelift sold enterprises a subscription for validated data about the open source packages they use, and paid partnered maintainers ("lifters") to meet standards such as license annotation, security policies, dependency tracking and two-factor authentication. Payments depend on customer usage and how important a package is. Sonar, a code-quality and security company, announced a definitive agreement to buy Tidelift in December 2024. Tidelift also published the most-cited maintainer surveys.

## Evidence

| Claim | Figure or fact | Source | Class | Confidence |
|---|---|---|---|---|
| Acquisition agreement | Sonar agreed to acquire Tidelift (December 2024) | [S1], [S2] | Company press release; secondary | Sourced |
| Current branding | Sonar's own pages are labelled "Tidelift: a Sonar company" and describe Tidelift as "now a Sonar company" | [S3], [S4] | Acquirer's pages | Medium |
| Maintainer program | Pays partnered maintainers to meet published standards; pay depends on usage and strategic importance | [S4] | Acquirer's maintainer page | Sourced |
| Security effect | Paid maintainers 55% more likely to implement critical security and maintenance practices | [S1]; Tidelift 2024 report p27 (repo S01) | Vendor survey | Medium |
| Named customers | Cisco, Fannie Mae, U.S. Air Force | [S1] | Company press release | Sourced |
| Sonar size | More than 28,000 enterprise customers (2025) | [S2] | Secondary | Low |

## OSF fit

| OSF layer | What maps | What does not |
|---|---|---|
| dOSPO | Published standards maintainers agree to meet | A company decides standards and pay |
| OMF | Close to a maintainer retainer tied to practice standards | Pay is per package, set by the vendor |
| ORF | Family B: recurring enterprise revenue funds maintainers | Revenue belongs to the vendor; how much reaches maintainers is not published |

## Gaps and cautions

- **Update to this repo's stance.** The survey inventory and evidence register say no closing announcement was found. Sonar now presents Tidelift as "now a Sonar company" on its own pages, which indicates the deal closed. No closing date or terms were found. Suggest changing "definitive agreement" to "acquired (closing date not published)" with this source.
- After the acquisition, the pages opened no longer describe a separate Tidelift product; open source data appears under Sonar's SCA and Advanced Security products. Whether maintainer payments continue at the same scale is **Unverified**.

## Sources

| ID | URL | Supports | Checked | Access |
|---|---|---|---|---|
| S1 | https://sonarsource.com/company/press-releases/sonar-to-acquire-tidelift | Agreement, 55% figure, customers | 2026-10-27 PT | Search result |
| S2 | https://en.wikipedia.org/wiki/Sonar_(company) | December 2024 agreement; Sonar size | 2026-10-27 PT | Fetched |
| S3 | https://www.sonarsource.com/resources/open-source-resources/ | "Now a Sonar company" branding | 2026-10-27 PT | Fetched |
| S4 | https://www.sonarsource.com/open-source-maintainers | Maintainer program description | 2026-10-27 PT | Search result |
</content>
</invoke>
