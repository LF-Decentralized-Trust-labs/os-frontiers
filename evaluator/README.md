# Open Source Frontiers Evaluator Suite

> **Unified Ecosystem Assessment Engine (dOSPO · OMF · ORF)**  
> *Linux Foundation CHAOSS, QUAID Scanner, and Live On-Chain Data Standards*  
> *LF Decentralized Trust · Open Source Frontiers Lab*

---

## Directory Overview

```
evaluator/
├── README.md
├── cli/                                     <-- Assessment CLI Engines & Adapters
│   ├── assess_ecosystem.py                  # Multi-preset system assessor
│   ├── live_data_analyst.py                 # Live Koios API & CoinGecko analyst
│   ├── quaid_adapter.py                     # Official QUAID Scanner 5-pillar adapter
│   ├── index.js                             # Node.js CLI runner
│   └── package.json                         # Node package config
├── docs/                                    <-- Assessment Specs & Rubrics
│   └── 3-Piece Ecosystem Maturity Assessment.md
└── examples/                                <-- Real-World Ecosystem Reports (Cardano Test Case)
    ├── CARDANO_FULL_ECOSYSTEM_ANALYSIS.md   # Cardano Treasury & Tooling Report
    ├── CARDANO_CHAOSS_HEALTH_REPORT.md      # Linux Foundation CHAOSS Audit
    ├── CARDANO_QUAID_SCANNER_REPORT.md      # QUAID 5-Pillar Security & Tech Audit
    ├── CARDANO_LIVE_SYSTEM_REPORT.md       # Live Koios & CoinGecko On-Chain Report
    └── *.json                               # Machine-readable JSON datasets
```

---

## Quick Start CLI Commands

### 1. Run Official QUAID Scanner Audit (5 Core Technical Pillars)
```bash
python evaluator/cli/quaid_adapter.py intersectmbo/cardano-node
```

### 2. Run Real-Time Live On-Chain & Systems Data Analyst
```bash
python evaluator/cli/live_data_analyst.py
```

### 3. Run Systems & Capital Flow Assessor
```bash
python evaluator/cli/assess_ecosystem.py cardano
```

---

## Standards Compliance

- **Linux Foundation CHAOSS**: Commit velocity, change request lead time, Bus Factor (Elephant Factor).
- **QUAID Scanner Specification**: Security posture, governance soundness, community sustainability, AI readiness, technical rigor.
- **Koios Cardano REST API**: Real-time Lovelace treasury balances and epoch parameters.
