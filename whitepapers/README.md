# Open Source Frontiers — Whitepaper Series

> **LF Decentralized Trust · Stage 0 Research Candidate Series**  
> *Release Candidate Edition: `v0.8.0-rc.1` · Master Architecture Whitepapers & PDF Documents*

---

## Executive Overview

The **Open Source Frontiers (OSF) Whitepaper Series** establishes the theoretical, legal, economic, and operational foundations for open-source software sustainability in decentralized ecosystems.

## Series position

The OMF PDF's sentence that dOSPO and OMF "together constitute a complete institutional model" does not include replenishment and is not the series position. The 18 August 2026 ORF paper is the third installment. The return path is part of the loop. Each framework can still be used alone.

## Which text controls

- **ORF.** The canonical text is the v1.1 errata-applied manuscript, [`orf-whitepaper-v1.1-errata-applied.md`](./orf-whitepaper-v1.1-errata-applied.md). Where it differs from [`orf-v1.0.pdf`](./orf-v1.0.pdf), the v1.1 markdown controls. [`ORF_ERRATA.md`](./ORF_ERRATA.md) is the citation layer that the manuscript already folds in. The v1.0 PDF stays in the tree as the previous edition. A v1.1 PDF is built in CI from the markdown (workflow `whitepaper-pdf.yml`) and uploaded as an artifact. It is not committed.
- **dOSPO.** The v1.0 PDF is the paper. [`DOSPO_WHITEPAPER.md`](./DOSPO_WHITEPAPER.md) is a pointer, dated March 3, 2026. There is no v1.1 manuscript in this tree.
- **OMF.** The v1.0 PDF is the paper. [`OMF_WHITEPAPER.md`](./OMF_WHITEPAPER.md) is a pointer, dated March 7, 2026. Where [`OMF_ERRATA.md`](./OMF_ERRATA.md) differs from the PDF, the errata controls until those sentences are in a new edition. There is no v1.1 OMF manuscript in this tree.

No hard gate is marked passed. Specifications under `orf/` remain Stage 0.

The figure below is the series, not a claim that every box has a v1.1 markdown edition:

```text
               ┌──────────────────────────────────────────┐
               │    OSF MASTER ARCHITECTURAL WHITEPAPERS   │
               └────────────────────┬─────────────────────┘
                                    │
         ┌──────────────────────────┼──────────────────────────┐
         ▼                          ▼                          ▼
┌─────────────────┐        ┌─────────────────┐        ┌─────────────────┐
│ dOSPO Whitepaper│        │  OMF Whitepaper │        │  ORF Whitepaper │
│ (Governance)    │        │  (Deployment)   │        │ (Replenishment) │
└─────────────────┘        └─────────────────┘        └─────────────────┘
```

---

## 1. Files

- **dOSPO v1.0 PDF**: [`dospo-whitepaper-v1.0.pdf`](./dospo-whitepaper-v1.0.pdf). Pointer: [`DOSPO_WHITEPAPER.md`](./DOSPO_WHITEPAPER.md).
- **OMF v1.0 PDF**: [`open-maintenance-framework-omf-v1.0.pdf`](./open-maintenance-framework-omf-v1.0.pdf). Pointer: [`OMF_WHITEPAPER.md`](./OMF_WHITEPAPER.md). Errata: [`OMF_ERRATA.md`](./OMF_ERRATA.md).
- **ORF v1.1 manuscript (canonical)**: [`orf-whitepaper-v1.1-errata-applied.md`](./orf-whitepaper-v1.1-errata-applied.md). Previous edition: [`orf-v1.0.pdf`](./orf-v1.0.pdf). Errata record: [`ORF_ERRATA.md`](./ORF_ERRATA.md).

---

## Primary Specifications Directory

- **dOSPO Specification**: [`../dospo/START_HERE.md`](../dospo/START_HERE.md)
- **OMF Portfolio Specification**: [`../omf/PROGRAM_PORTFOLIO.md`](../omf/PROGRAM_PORTFOLIO.md)
- **ORF Instrument Catalog**: [`../orf/INSTRUMENT_CATALOG.md`](../orf/INSTRUMENT_CATALOG.md)
- **Primary-Source Evidence Register**: [`../docs/EVIDENCE_REGISTER.md`](../docs/EVIDENCE_REGISTER.md)
- **Prior Art & Ecosystem Analysis**: [`../docs/PRIOR_ART_AND_COMPETITIVE_ANALYSIS.md`](../docs/PRIOR_ART_AND_COMPETITIVE_ANALYSIS.md)
