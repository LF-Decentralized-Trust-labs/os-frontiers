# Open Source Frontiers Evaluator Suite

> **Capital-Flow & Dynamic Ecosystem Assessor (dOSPO · OMF · ORF)**  
> *Linux Foundation CHAOSS, QUAID Scanner, and Live On-Chain Data Standards*  
> *LF Decentralized Trust · Open Source Frontiers Lab*

---

## Directory Architecture

```
evaluator/
├── README.md
├── cli/                                     <-- Assessor CLI Engines & Adapters
│   ├── quaid_adapter.py                     # Official QUAID Scanner 5-pillar adapter
│   ├── live_data_analyst.py                 # Dynamic GitHub & Cardano Treasury analyst
│   ├── assess_ecosystem.py                  # Capital-flow & dynamic maturity calculator
│   ├── index.js                             # Node.js CLI runner
│   └── package.json                         # Node package config
├── docs/                                    <-- Assessment Specs & Diagnostic Rubrics
│   └── 3-Piece Ecosystem Maturity Assessment.md
└── examples/                                <-- Real-World Example Reports & JSON Datasets
    ├── CARDANO_FULL_ECOSYSTEM_ANALYSIS.md   # Cardano Treasury & Developer Tooling Report
    ├── CARDANO_QUAID_SCANNER_REPORT.md      # QUAID 5-Pillar Security & Tech Audit
    ├── cardano_full_ecosystem_analysis.json # Full ecosystem JSON dataset
    └── cardano_quaid_scanner_report.json    # QUAID scan JSON dataset
```

---

## Quick Start CLI Commands

### 1. Run Official QUAID Scanner Audit (5 Core Technical Pillars)
```bash
python evaluator/cli/quaid_adapter.py intersectmbo/cardano-node
```

### 2. Run Dynamic Cardano Treasury Proposal & Developer Tooling Analyst
```bash
python evaluator/cli/live_data_analyst.py
```

### 3. Run Capital-Flow & Dynamic Maturity Calculator
```bash
python evaluator/cli/assess_ecosystem.py evaluator/examples/sample_input_config.json
```

---

## Standards Compliance

- **Linux Foundation CHAOSS**: Commit velocity, change request lead time, Bus Factor (Elephant Factor).
- **QUAID Scanner Specification**: Security posture, governance soundness, community sustainability, AI readiness, technical rigor (Inclusive Language removed).
- **Dynamic Capital Flow Engine**: Real-time GitHub REST API metrics, treasury fee splits, and bear market runway stress testing.
