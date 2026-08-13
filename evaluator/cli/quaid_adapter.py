#!/usr/bin/env python3
"""
Experimental OSF QUAID-Inspired Security & Health Heuristic Adapter
LF Decentralized Trust · Open Source Frontiers Lab
Inspired by https://github.com/quaid/quaid-scanner
Stage 0 Research Candidate Adapter
"""

import sys
import os
import json
import urllib.request
import ssl
import io

# Ensure UTF-8 output encoding on Windows terminals
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Standard SSL verification
SSL_CTX = ssl.create_default_context()
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN") or os.environ.get("GITHUB_PERSONAL_ACCESS_TOKEN")

def get_headers():
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) OSF-Quaid-Heuristic/1.0"}
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

def analyze_repo_heuristics(repo_slug, local_base="."):
    print(f"🔍 Running Experimental QUAID-Inspired Heuristic Scan on target `{repo_slug}`...")

    repo_data = fetch_json(f"https://api.github.com/repos/{repo_slug}")
    if not repo_data:
        print(f"❌ Error: Unable to fetch live target repository data for `{repo_slug}`. Set GITHUB_TOKEN if rate limited.")
        return None

    stars = repo_data.get("stargazers_count", 0)
    forks = repo_data.get("forks_count", 0)
    open_issues = repo_data.get("open_issues_count", 0)

    # Auto-detect Maturity Level according to QUAID spec
    if stars > 1000 or forks > 200:
        maturity = "graduated"
    elif stars > 50:
        maturity = "incubating"
    else:
        maturity = "sandbox"

    findings = []

    # 1. Security Posture Pillar (30%)
    sec_score = 7.0
    sec_policy_data = fetch_json(f"https://api.github.com/repos/{repo_slug}/contents/SECURITY.md")
    if sec_policy_data:
        sec_score = 9.5
        findings.append({
            "severity": "PASS",
            "pillar": "security",
            "category": "security-policy",
            "message": "Target repository contains SECURITY.md vulnerability disclosure policy",
            "dataSource": "api"
        })
    else:
        findings.append({
            "severity": "WARNING",
            "pillar": "security",
            "category": "security-policy",
            "message": "Target repository SECURITY.md file not found",
            "suggestion": "Add a SECURITY.md vulnerability disclosure policy to target repository",
            "dataSource": "api"
        })

    # 2. Governance Soundness Pillar (25%)
    gov_score = 8.0
    gov_doc = fetch_json(f"https://api.github.com/repos/{repo_slug}/contents/GOVERNANCE.md")
    if gov_doc:
        gov_score = 9.5
        findings.append({
            "severity": "PASS",
            "pillar": "governance",
            "category": "governance-doc",
            "message": "Target repository GOVERNANCE.md charter verified",
            "dataSource": "api"
        })

    # 3. Community Sustainability Pillar (20%)
    comm_score = 8.0
    if open_issues > 200:
        comm_score = 6.0
        findings.append({
            "severity": "WARNING",
            "pillar": "community",
            "category": "issue-backlog",
            "message": f"High open issue backlog on target ({open_issues} issues)",
            "dataSource": "api"
        })

    # 4. AI-Native Readiness Pillar (15%)
    ai_score = 7.5

    # 5. Technical Rigor Pillar (10%)
    tech_score = 8.0

    overall_score = round(
        (sec_score * 0.30) +
        (gov_score * 0.25) +
        (comm_score * 0.20) +
        (ai_score * 0.15) +
        (tech_score * 0.10),
        1
    )

    risk_level = "LOW" if overall_score >= 8.0 else ("MEDIUM" if overall_score >= 5.0 else "HIGH")

    return {
        "repo": repo_slug,
        "overallScore": overall_score,
        "riskLevel": risk_level,
        "maturity": maturity,
        "pillars": {
            "security": {"score": sec_score, "weight": 0.30},
            "governance": {"score": gov_score, "weight": 0.25},
            "community": {"score": comm_score, "weight": 0.20},
            "ai_readiness": {"score": ai_score, "weight": 0.15},
            "technical": {"score": tech_score, "weight": 0.10}
        },
        "findings": findings
    }

def main():
    target_repo = sys.argv[1] if len(sys.argv) > 1 else "intersectmbo/cardano-node"
    report = analyze_repo_heuristics(target_repo, local_base=".")

    if not report:
        sys.exit(1)

    output_dir = os.path.join("evaluator", "examples")
    os.makedirs(output_dir, exist_ok=True)

    json_path = os.path.join(output_dir, "cardano_quaid_scanner_report.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)

    print("\n=======================================================")
    print(f"🛡️ EXPERIMENTAL QUAID HEURISTIC SCAN COMPLETE: {report['repo']}")
    print(f"🏆 Overall Heuristic Score : {report['overallScore']} / 10.0")
    print(f"⚠️ Risk Level Rating       : {report['riskLevel']}")
    print(f"🌱 Maturity Classification : {report['maturity']}")
    print(f"💾 Report saved to         : {json_path}")
    print("=======================================================\n")

if __name__ == "__main__":
    main()
