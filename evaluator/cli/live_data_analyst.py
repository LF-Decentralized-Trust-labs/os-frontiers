#!/usr/bin/env python3
"""
Cardano Example Real-Time Data Analyst & Ecosystem Report Generator
LF Decentralized Trust · Open Source Frontiers Lab
Stage 0 Research Candidate Analysis Tool
"""

import sys
import os
import json
import urllib.request
import ssl
import io
from datetime import datetime, timezone

# Ensure UTF-8 output encoding on Windows terminals
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Standard secure TLS context
SSL_CTX = ssl.create_default_context()
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN") or os.environ.get("GITHUB_PERSONAL_ACCESS_TOKEN")

TARGET_REPOS = [
    "intersectmbo/cardano-node",
    "intersectmbo/cardano-ledger",
    "intersectmbo/ouroboros-network",
    "intersectmbo/cardano-db-sync",
    "intersectmbo/cardano-cli"
]

def get_headers():
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) OSF-Cardano-Analyst/1.0"}
    if GITHUB_TOKEN:
        headers["Authorization"] = f"Bearer {GITHUB_TOKEN}"
    return headers

def fetch_json(url):
    try:
        req = urllib.request.Request(url, headers=get_headers())
        with urllib.request.urlopen(req, context=SSL_CTX, timeout=10) as resp:
            return json.loads(resp.read().decode('utf-8'))
    except Exception as e:
        return None

def analyze_cardano_ecosystem():
    print("🔍 Fetching live ecosystem metrics for Cardano core repositories...")
    results = []

    for repo in TARGET_REPOS:
        data = fetch_json(f"https://api.github.com/repos/{repo}")
        if data:
            results.append({
                "repo": repo,
                "stars": data.get("stargazers_count", 0),
                "forks": data.get("forks_count", 0),
                "open_issues": data.get("open_issues_count", 0),
                "updated_at": data.get("updated_at", "N/A")
            })

    now_utc = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

    report_content = f"""# Real-Time Ecosystem Audit Report: Cardano (POSM Baseline)

> **Analysis Date**: {now_utc}  
> **Source Engine**: `evaluator/cli/live_data_analyst.py` (Stage 0 Research Candidate)

---

## 1. Observed Repository Metrics

| Repository | Stars | Forks | Open Issues | GitHub Last Updated |
|---|---|---|---|---|
"""
    for r in results:
        report_content += f"| `{r['repo']}` | {r['stars']} | {r['forks']} | {r['open_issues']} | {r['updated_at']} |\n"

    report_content += """
---

## 2. dOSPO Governance & Replenishment Synthesis

- **Governance Authority**: Intersect MBO (Cardano Open Source Committee & POSM Engine).
- **Core Maintenance Retainers**: Active 12-month maintainer retainer cohorts for core client developers.
- **Replenishment Model**: Treasury allocations supplemented by candidate ORF fee-sharing and stake pool mechanisms.
"""

    return report_content, results

def main():
    report_text, raw_data = analyze_cardano_ecosystem()

    output_dir = os.path.join("evaluator", "examples")
    os.makedirs(output_dir, exist_ok=True)

    report_path = os.path.join(output_dir, "CARDANO_POSM_LIVE_ANALYSIS.md")
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(report_text)

    print("\n=======================================================")
    print("📊 CARDANO ECOSYSTEM ANALYST REPORT GENERATED")
    print(f"💾 Saved Markdown Report to : {report_path}")
    print("=======================================================\n")

if __name__ == "__main__":
    main()
