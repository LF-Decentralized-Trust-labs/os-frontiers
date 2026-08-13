# Automated 3-Piece Ecosystem Assessor & Experimental Tooling Suite

> **Edition**: July 2026 Research Candidate (v0.8.0-rc.1)  
> **Status**: Stage 0 Research Candidate Engine

---

## 1. Assessor Engine Overview

The **Canonical 3-Piece Ecosystem Assessor** computes ecosystem sustainability across 15 indicators (5 dOSPO, 5 OMF, 5 ORF) for a total maximum score of 75 Pts.

- **Python Assessor (`cli/assess_ecosystem.py`)**: Canonical engine implementing 0/3/5 indicator scoring, exact point thresholds, and the Level 3 replenishment hard-gate (`net_replenishment_ratio >= 1.0`).
- **Node CLI Wrapper (`cli/index.js`)**: Executable wrapper invoking the Python engine under the hood.
- **Experimental QUAID Heuristic Adapter (`cli/quaid_adapter.py`)**: Stage 0 research candidate adapter inspecting security and health heuristics on target repositories.

---

## 2. Usage Instructions

```bash
# Run canonical 15-indicator assessor
python evaluator/cli/assess_ecosystem.py evaluator/examples/sample_input_config.json

# Run experimental QUAID-inspired scanner heuristic
python evaluator/cli/quaid_adapter.py intersectmbo/cardano-node
```
