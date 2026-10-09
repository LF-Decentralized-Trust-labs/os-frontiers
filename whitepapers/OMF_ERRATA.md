# OMF v1.0 citation errata

This file is a citation layer for [`open-maintenance-framework-omf-v1.0.pdf`](./open-maintenance-framework-omf-v1.0.pdf) (70 pp., dated 7 March 2026). It is not a second paper. Where this file differs from that PDF, this file controls, until the author pastes these sentences into a new PDF.

The sentences below are the author's paste-ready repairs. This commit does not retypeset the PDF. Page numbers are PDF pages; on the pages affected the printed page number is the same.

## Tidelift maintainer figures — "59% considered quitting" and "60% work unpaid" (approved 9 October 2026)

The paper attributes "59% … considered quitting" to Tidelift 2024. That is wrong in two ways. The 2024 report gives **60%**; 59% is the **2021** figure. And Tidelift's measure is "**quit or** considered quitting", not "considered quitting" alone: in 2024, 38% had considered quitting and 22% had quit. The companion figure "60% work unpaid" has the right number but the wrong wording. Tidelift's 60% is maintainers who describe themselves as unpaid hobbyists (single choice). On a multi-select income question, 47% report no maintainer income.

> "This year the percentage of maintainers who have either quit or considered quitting their work was 60%, which is consistent with the 58% in 2023 and 59% in 2021."
> — Tidelift, *The 2024 Tidelift State of the Open Source Maintainer Report* (September 2024), PDF p40. Chart, same page: 22% "Yes, I have quit"; 38% "Yes, I have considered quitting"; 40% "No"; n=350 (2024).
>
> "60% of maintainers are (still) not paid for their work" (p4); "the percentage of maintainers who describe themselves as unpaid hobbyists stayed identical: 60%." (p5); "only 47% report that they do not get paid to maintain projects." (p13)
> — same report. https://assets-eu-01.kc-usercontent.com/ef593040-b591-0198-9506-ed88b30bc023/d325a56f-05be-4379-bfd1-ee4776fcad41/2024-tidelift-state-of-the-open-source-maintainer-report-.pdf
>
> "a whopping 59% of maintainers we surveyed have quit or considered quitting maintaining a project."
> — Tidelift, *The 2021 Tidelift Open Source Maintainer Survey*, PDF p19. https://assets-eu-01.kc-usercontent.com/ef593040-b591-0198-9506-ed88b30bc023/79c06b71-8002-479f-981a-10c7f72471d7/2021_Tidelift_Maintainer_Survey_FINAL-1.pdf (identical file: https://www.sonarsource.com/the-tidelift-maintainer-survey.pdf)

Do not cite `https://tidelift.com/open-source-maintainer-survey-2024`. It now redirects to a different document, *The 2024 Tidelift Maintainer Impact Report* (November 2024). Also avoid the 2024 report's closing narrative (p59, "Almost two-thirds of maintainers have quit or considered quitting"); it conflicts with the report's own data on p40.

### §1, "The Documented Costs of Inaction" table, Maintainer Burnout row (PDF p8)

Replace:

> 59% of maintainers have considered quitting; 60% work unpaid. The Kubernetes Ingress NGINX project announced no further security patches after March 2026 — because its maintainers burned out. (Tidelift 2024; Caceres 2025)

with:

> 60% of maintainers have quit or considered quitting (22% quit, 38% considered), consistent with 58% in 2023 and 59% in 2021; 60% describe themselves as unpaid hobbyists. The Kubernetes Ingress NGINX project announced no further security patches after March 2026 — because its maintainers burned out. (Tidelift 2024, pp. 4–5, 40; Caceres 2025)

The Ingress NGINX / Caceres sentence was not checked in this pass and is left unchanged.

### Evidence Summary table, Tidelift row (PDF p45)

The table of contents lists the Evidence Summary at p46, but this row prints on p45. Replace:

> 60% unpaid maintainers; 59% considered quitting | Tidelift State of Maintainer Report (2024) | High

with:

> 60% self-described unpaid hobbyist maintainers; 60% quit or considered quitting (59% in 2021) | Tidelift State of the Open Source Maintainer Report (2024), pp. 4–5, 40 | High (self-selected sample)

### §12, Instrument 2 (PDF p32)

Replace:

> … and 60% of OSS maintainers currently work entirely unpaid.

with:

> … and 60% of maintainers describe themselves as unpaid hobbyists (47% report no maintainer income at all).

Source: Tidelift 2024, PDF pp. 4–5 and 13 (quotes above). "Entirely unpaid" fits the 47% multi-select answer better than the 60% self-description. Cite the Tidelift 2024 PDF, not the redirecting tidelift.com page. Do not cite STA's 77% (Unverified).

Confidence: High. Both figures were read directly from the publisher's PDFs on 9 October 2026. Tidelift samples are self-selected. Page-by-page verification: [`docs/surveys/researchy-section2-pagecheck.md`](../docs/surveys/researchy-section2-pagecheck.md) and [`docs/surveys/data/tidelift-page-index.md`](../docs/surveys/data/tidelift-page-index.md).

## Bibliography lines to add

The existing line "Tidelift (2024). State of the open source maintainer report." already cites the kc-usercontent PDF URL above, which is live and byte-identical to the file checked (SHA-256 prefix `f40e80b70403ec13`). No change is needed there. Because the corrected sentences keep the 2021 figure, add:

> Tidelift (2021). The 2021 Tidelift open source maintainer survey. https://assets-eu-01.kc-usercontent.com/ef593040-b591-0198-9506-ed88b30bc023/79c06b71-8002-479f-981a-10c7f72471d7/2021_Tidelift_Maintainer_Survey_FINAL-1.pdf
