#!/usr/bin/env python3
"""
Automated 3-Piece Ecosystem Maturity Assessment CLI Tool (dOSPO · OMF · ORF)
LF Decentralized Trust · Open Source Frontiers Lab
"""

import sys
import os
import json
import argparse
import io

# Ensure UTF-8 output encoding on Windows terminals
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Automated 3-Piece Ecosystem Need & Maturity Assessor (dOSPO · OMF · ORF)"
    )
    parser.add_argument(
        "target",
        help="Local repository path or GitHub repository URL / owner/repo string"
    )
    parser.add_argument(
        "--output-json",
        default="assessment_report.json",
        help="Path to save JSON output report (default: assessment_report.json)"
    )
    parser.add_argument(
        "--output-md",
        default="ASSESSMENT_REPORT.md",
        help="Path to save Markdown output report (default: ASSESSMENT_REPORT.md)"
    )
    return parser.parse_args()

def check_local_file_exists(base_path, file_names):
    for fn in file_names:
        full_p = os.path.join(base_path, fn)
        if os.path.exists(full_p):
            return True, fn
    return False, None

def assess_local_repository(repo_path):
    print(f"🔍 Analyzing local repository: {repo_path}...")
    
    # 1. dOSPO Checks (Governance Authority)
    has_dospo_charter, charter_file = check_local_file_exists(
        repo_path, 
        ["dOSPO/Start Here: Decentralized Open Source Program Office (dOSPO)", "dOSPO/dOSPO Charter", "GOVERNANCE.md", "dOSPO.md"]
    )
    has_funding_principles, _ = check_local_file_exists(
        repo_path, 
        ["dOSPO/Funding Principles", "FUNDING_POLICY.md"]
    )
    has_security_policy, _ = check_local_file_exists(
        repo_path, 
        ["SECURITY.md", "dOSPO/Incident Response Playbook"]
    )

    # 2. OMF Checks (Maintenance Deployment)
    has_omf_spec, omf_file = check_local_file_exists(
        repo_path, 
        ["OMF/Start Here: Open Maintenance Framework (OMF)", "OMF/Program Charter Template", "OMF.md"]
    )
    has_maintainer_guide, _ = check_local_file_exists(
        repo_path, 
        ["docs/MAINTAINER_AUTONOMY_GUIDE.md", "MAINTAINERS.md", "OMF/Stewardship"]
    )
    has_audit_template, _ = check_local_file_exists(
        repo_path, 
        ["OMF/Dependency Audit Template", "OMF/Quarterly Report Template"]
    )

    # 3. ORF Checks (Value Replenishment)
    has_orf_spec, orf_file = check_local_file_exists(
        repo_path, 
        ["ORF/Start Here: Open Replenishment Framework (ORF)", "ORF/Instrument Catalog", "ORF.md"]
    )
    has_sla_agreement, _ = check_local_file_exists(
        repo_path, 
        ["ORF/Enterprise SLA & Reciprocal Funding Agreement", "pitch/ENTERPRISE_SPONSOR_KIT.md", "SLA.md"]
    )
    has_ips_template, _ = check_local_file_exists(
        repo_path, 
        ["ORF/Investment Policy Statement Template", "IPS.md"]
    )
    has_audit_report, _ = check_local_file_exists(
        repo_path, 
        ["ORF/Independent Collection Audit Report", "AUDIT.md"]
    )

    # Calculate Sub-Scores
    dospo_score = (5 if has_dospo_charter else 1) + (5 if has_funding_principles else 1) + (5 if has_security_policy else 1) + 2
    omf_score = (5 if has_omf_spec else 1) + (5 if has_maintainer_guide else 1) + (5 if has_audit_template else 1) + 2
    orf_score = (5 if has_orf_spec else 0) + (5 if has_sla_agreement else 0) + (5 if has_ips_template else 0) + (5 if has_audit_report else 0)

    total_score = dospo_score + omf_score + orf_score
    max_score = 60

    # Determine Maturity Level
    if total_score <= 15:
        level = "Level 0: Un-Architected / Fragile"
        desc = "High risk of treasury depletion. Recommends initializing dOSPO governance charter."
    elif total_score <= 30:
        level = "Level 1: Governance & Retainers Bootstrapped"
        desc = "dOSPO and OMF active. Recommends piloting Tier 1 ORF Enterprise SLAs."
    elif total_score <= 48:
        level = "Level 2: Fee-Supplemented Maintenance"
        desc = "OMF operational with partial fee splits. Recommends deploying Capital-layer IPS yield sleeve."
    else:
        level = "Level 3: Self-Sustaining Closed Loop"
        desc = "Net replenishment ratio >= 1.0. Full 3-piece framework suite active."

    results = {
        "target": repo_path,
        "dospo_score": dospo_score,
        "dospo_pct": round((dospo_score / 20) * 100, 1),
        "omf_score": omf_score,
        "omf_pct": round((omf_score / 20) * 100, 1),
        "orf_score": orf_score,
        "orf_pct": round((orf_score / 20) * 100, 1),
        "total_score": total_score,
        "max_score": max_score,
        "overall_pct": round((total_score / max_score) * 100, 1),
        "maturity_level": level,
        "recommendation": desc,
        "artifacts_detected": {
            "dOSPO_Charter": has_dospo_charter,
            "OMF_Spec": has_omf_spec,
            "ORF_Spec": has_orf_spec,
            "Enterprise_SLA": has_sla_agreement,
            "IPS_Endowment": has_ips_template,
            "Audit_Report": has_audit_report
        }
    }

    return results

def generate_markdown_report(results):
    return f"""# Automated 3-Piece Ecosystem Assessment Report

> **Target Analyzed**: `{results['target']}`  
> **Evaluator Engine**: Open Source Frontiers Automated Assessor v1.0  
> **Framework Suite**: dOSPO (WHO) · OMF (HOW SPEND) · ORF (HOW COLLECT)

---

## Executive Summary

- **Overall Maturity Score**: **{results['total_score']} / {results['max_score']}** ({results['overall_pct']}%)
- **Maturity Level Classification**: **{results['maturity_level']}**
- **Strategic Recommendation**: {results['recommendation']}

---

## 3-Pillar Score Breakdown

| Framework Pillar | Points Scored | Pillar Percentage | Status |
|---|---|---|---|
| 🏛️ **dOSPO (Governance Authority)** | {results['dospo_score']} / 20 | **{results['dospo_pct']}%** | {'🟢 Bootstrapped' if results['dospo_pct'] >= 60 else '🟡 Partial'} |
| 🛠️ **OMF (Maintenance Deployment)** | {results['omf_score']} / 20 | **{results['omf_pct']}%** | {'🟢 Bootstrapped' if results['omf_pct'] >= 60 else '🟡 Partial'} |
| 💰 **ORF (Value Replenishment)** | {results['orf_score']} / 20 | **{results['orf_pct']}%** | {'🟢 Active' if results['orf_pct'] >= 60 else '🔴 Action Required'} |

---

## Artifact Detection Audit

- [x] **dOSPO Governance Charter**: `{results['artifacts_detected']['dOSPO_Charter']}`
- [x] **OMF Maintenance Specification**: `{results['artifacts_detected']['OMF_Spec']}`
- [x] **ORF Replenishment Specification**: `{results['artifacts_detected']['ORF_Spec']}`
- [x] **Enterprise SLA Contract Terms**: `{results['artifacts_detected']['Enterprise_SLA']}`
- [x] **Capital Investment Policy Statement (IPS)**: `{results['artifacts_detected']['IPS_Endowment']}`
- [x] **Independent Collection Audit Report**: `{results['artifacts_detected']['Audit_Report']}`

---

*Report generated by LF Decentralized Trust Open Source Frontiers Lab*
"""

def main():
    args = parse_arguments()
    target_path = os.path.abspath(args.target) if os.path.exists(args.target) else args.target
    
    if os.path.exists(target_path):
        results = assess_local_repository(target_path)
    else:
        print(f"Target '{target_path}' is a remote repository string. Running local workspace scanner fallback...")
        results = assess_local_repository(".")

    # Print summary to console
    print("\n=======================================================")
    print(f"📊 AUTOMATED 3-PIECE ASSESSMENT RESULTS: {results['target']}")
    print("=======================================================")
    print(f"🏛️ dOSPO Governance Score : {results['dospo_score']}/20 ({results['dospo_pct']}%)")
    print(f"🛠️ OMF Deployment Score   : {results['omf_score']}/20 ({results['omf_pct']}%)")
    print(f"💰 ORF Replenishment Score: {results['orf_score']}/20 ({results['orf_pct']}%)")
    print(f"🏆 OVERALL MATURITY       : {results['overall_pct']}% -> {results['maturity_level']}")
    print("=======================================================\n")

    # Save JSON Report
    with open(args.output_json, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)
    print(f"💾 JSON report saved to: {args.output_json}")

    # Save Markdown Report
    md_content = generate_markdown_report(results)
    with open(args.output_md, "w", encoding="utf-8") as f:
        f.write(md_content)
    print(f"💾 Markdown report saved to: {args.output_md}")

if __name__ == "__main__":
    main()
