# Automated 3-Piece Ecosystem Assessment CLI Tool

> **Automated CLI Assessor for dOSPO, OMF, and ORF Repository & Governance Maturity**  
> *LF Decentralized Trust · Open Source Frontiers Lab*

---

## Overview

The **Automated 3-Piece Ecosystem Assessment CLI Tool** automatically scans a local repository directory or GitHub repository to evaluate maturity across all 3 framework pillars:
- **dOSPO**: Governance Authority & Mandate Charters
- **OMF**: Maintenance Deployment & Maintainer Retainers
- **ORF**: Value Replenishment, Enterprise SLAs & IPS Endowments

---

## Quick Usage

### Python Assessor Script
```bash
python tools/automated-evaluator/assess_ecosystem.py .
```

### Node.js Assessor Script
```bash
node tools/automated-evaluator/index.js .
```

---

## Output Artifacts Generated

1. `assessment_report.json`: Machine-readable JSON output containing pillar scores, percentages, and detected artifacts.
2. `ASSESSMENT_REPORT.md`: Formatted Markdown summary report ready for governance forum publication.
