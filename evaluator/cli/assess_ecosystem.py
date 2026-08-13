#!/usr/bin/env python3
"""
Automated 3-Piece Ecosystem Systems & Capital Flow Assessor (dOSPO · OMF · ORF)
LF Decentralized Trust · Open Source Frontiers Lab
Strict Dynamic Scoring Engine (0 Base Score, Level 0 Reachable)
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
        description="Dynamic 3-Piece Systems Assessor (Strict 0 Base Scoring)"
    )
    parser.add_argument(
        "config_file",
        nargs="?",
        default=None,
        help="Path to JSON system configuration file"
    )
    parser.add_argument(
        "--output-json",
        default=os.path.join("evaluator", "examples", "system_assessment_results.json"),
        help="Path to save JSON assessment results"
    )
    return parser.parse_args()

def analyze_system_data(config):
    budget = config.get("annual_maintenance_budget_usd", 0)
    fees = config.get("annual_tx_fee_inflow_usd", 0)
    reserve_exp = config.get("annual_reserve_expansion_usd", 0)
    earned_rev = config.get("annual_earned_non_inflation_usd", 0)
    reserves = config.get("treasury_reserve_usd", 0)

    net_non_inflationary = fees + earned_rev
    net_replenishment_ratio = round(net_non_inflationary / budget, 2) if budget > 0 else 0.0
    runway_years = round((reserves * 0.50) / budget, 1) if budget > 0 else 0.0

    # Dynamic Scoring Vectors starting strictly at 0 Base Score
    dospo_score = 0
    if config.get("has_community_charter", False):
        dospo_score += 10
    if config.get("operator_replaceable", False):
        dospo_score += 10
    if config.get("independent_audit_published", False):
        dospo_score += 5

    omf_score = 0
    if config.get("maintainer_retainer_program", False):
        omf_score += 12
    if config.get("maintainer_autonomy_guarantee", False):
        omf_score += 8
    if config.get("has_dependency_audit", False):
        omf_score += 5

    orf_score = 0
    if net_replenishment_ratio >= 1.0:
        orf_score += 15
    elif net_replenishment_ratio >= 0.5:
        orf_score += 10
    elif net_replenishment_ratio >= 0.2:
        orf_score += 5

    if config.get("ips_yield_sleeve_active", False):
        orf_score += 5
    if earned_rev > 0:
        orf_score += 5

    total_score = min(75, dospo_score + omf_score + orf_score)
    overall_pct = round((total_score / 75) * 100, 1)

    if overall_pct >= 85:
        level = "Level 3: Self-Sustaining Closed Loop"
    elif overall_pct >= 65:
        level = "Level 2: Fee-Supplemented Maintenance"
    elif overall_pct >= 40:
        level = "Level 1: Governance & Retainers Bootstrapped"
    else:
        level = "Level 0: Un-Architected / Fragile"

    return {
        "config_source": config.get("name", "Custom Input"),
        "dospo_score": dospo_score,
        "omf_score": omf_score,
        "orf_score": orf_score,
        "total_score": total_score,
        "overall_pct": overall_pct,
        "level": level,
        "metrics": {
            "annual_maintenance_budget_usd": budget,
            "net_replenishment_ratio": net_replenishment_ratio,
            "bear_market_runway_years": runway_years
        }
    }

def main():
    args = parse_arguments()

    if not args.config_file or not os.path.exists(args.config_file):
        sample_config = {
            "name": "Ecosystem Input Example",
            "annual_maintenance_budget_usd": 3500000,
            "treasury_reserve_usd": 650000000,
            "annual_tx_fee_inflow_usd": 4500000,
            "annual_reserve_expansion_usd": 85000000,
            "annual_earned_non_inflation_usd": 450000,
            "has_community_charter": True,
            "operator_replaceable": True,
            "independent_audit_published": True,
            "maintainer_retainer_program": True,
            "maintainer_autonomy_guarantee": True,
            "has_dependency_audit": True,
            "ips_yield_sleeve_active": False
        }
        config = sample_config
    else:
        with open(args.config_file, "r", encoding="utf-8") as f:
            config = json.load(f)

    results = analyze_system_data(config)

    os.makedirs(os.path.dirname(args.output_json), exist_ok=True)
    with open(args.output_json, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)

    print("\n=======================================================")
    print(f"📊 DYNAMIC SYSTEMS ASSESSMENT: {results['config_source']}")
    print(f"🏛️ dOSPO Governance Score  : {results['dospo_score']} / 25")
    print(f"🛠️ OMF Maintenance Score   : {results['omf_score']} / 25")
    print(f"💰 ORF Replenishment Score : {results['orf_score']} / 25")
    print(f"🏆 OVERALL SCORE           : {results['total_score']}/75 ({results['overall_pct']}%)")
    print(f"🌱 MATURITY CLASSIFICATION : {results['level']}")
    print(f"💾 Results saved to        : {args.output_json}")
    print("=======================================================\n")

if __name__ == "__main__":
    main()
