# Automated 3-Piece Ecosystem Assessor & Experimental Tooling Suite

> **Edition**: July 2026 Research Candidate (v0.8.0-rc.1)  
> **Status**: Stage 0 Research Candidate Engine

---

## 1. Assessor Engine Overview

The **Canonical 3-Piece Ecosystem Assessor** computes ecosystem sustainability across 15 indicators (5 dOSPO, 5 OMF, 5 ORF) for a total maximum score of 75 Pts.

- **Python Assessor (`cli/assess_ecosystem.py`)**: Canonical engine implementing 0/3/5 indicator scoring, exact point thresholds, and the point-rubric replenishment line (`net_replenishment_ratio >= 1.0`). The eight governance hard gates are reported separately and stay NOT MET when `hard_gates` is absent. Version `0.8.0-rc.1` (`--version`).
- **Node CLI Wrapper (`cli/index.js`)**: Executable wrapper invoking the Python engine. `cli/analyze_system.js` is a JavaScript port used for a parity test. It is not a second scorer with different rules.
- **Experimental QUAID Heuristic Adapter (`cli/quaid_adapter.py`)**: Stage 0 research candidate. Pass `--fixture` to score a saved GitHub API snapshot. Continuous integration uses `fixtures/quaid_cardano_node.json` and does not call the network. The offline star/fork/issue placeholders are not a measurement.
- **Schema**: [`schema/sample_input_config.schema.json`](schema/sample_input_config.schema.json).
- **Package**: [`pyproject.toml`](pyproject.toml) defines `os-frontiers-assess` at `0.8.0-rc.1`. TODO (Christian): PyPI and npm publishing are not done.
- **CHAOSS**: [`docs/CHAOSS_MAPPING.md`](docs/CHAOSS_MAPPING.md). Weak mappings are marked.

---

## 2. Usage Instructions

```bash
# Run canonical 15-indicator assessor
python evaluator/cli/assess_ecosystem.py evaluator/examples/sample_input_config.json

# Score the saved cardano-node snapshot. This does not call the GitHub API.
python evaluator/cli/quaid_adapter.py --fixture evaluator/fixtures/quaid_cardano_node.json intersectmbo/cardano-node
```

---

## 3. Local scorer preview

Open [`preview/index.html`](./preview/index.html) from this directory's `preview/` folder (`app.js` and `style.css` sit beside it). The same page is published at <https://lf-decentralized-trust-labs.github.io/os-frontiers/> (checked 27 October 2026). Scoring logic is unchanged.
