#!/usr/bin/env python3
"""
Canonical 3-Piece Ecosystem Systems & Capital Flow Assessor (dOSPO · OMF · ORF)
LF Decentralized Trust · Open Source Frontiers Lab
Full 15-Indicator Spec Engine with Level 3 Replenishment Hard-Gate (Ratio >= 1.0)
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
        description="Canonical 3-Piece Systems Assessor (15-Indicator Spec Engine)"
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
    net_replenishment_ratio = round(net_non_inflationary / budget, 4) if budget > 0 else 0.0
    runway_years = round((reserves * 0.50) / budget, 1) if budget > 0 else 0.0

    # 1. dOSPO Governance Indicators (0–25 Pts)
    dospo_score = 0
    if config.get("indicator_1_legitimacy_charter", False): dospo_score += 5
    if config.get("indicator_2_neutrality_guarantee", False): dospo_score += 5
    if config.get("indicator_3_operator_replaceable", False): dospo_score += 5
    if config.get("indicator_4_policy_engine", False): dospo_score += 5
    if config.get("indicator_5_transparency_reporting", False): dospo_score += 5

    # 2. OMF Maintenance Indicators (0–25 Pts)
    omf_score = 0
    if config.get("indicator_6_maintainer_retainers", False): omf_score += 5
    if config.get("indicator_7_contributor_pathways", False): omf_score += 5
    if config.get("indicator_8_tooling_stewardship", False): omf_score += 5
    if config.get("indicator_9_autonomy_safeguard", False): omf_score += 5
    if config.get("indicator_10_impact_metrics", False): omf_score += 5

    # 3. ORF Replenishment Indicators (0–25 Pts)
    orf_score = 0
    if net_replenishment_ratio >= 1.0:
        orf_score += 5
    elif net_replenishment_ratio >= 0.5:
        orf_score += 3
    elif net_replenishment_ratio >= 0.2:
        orf_score += 1

    if config.get("indicator_12_fork_resistance", False): orf_score += 5
    if config.get("indicator_13_benefit_bundling_slas", False): orf_score += 5
    if config.get("indicator_14_ips_endowments", False): orf_score += 5
    if config.get("indicator_15_independent_audit", False): orf_score += 5

    total_score = min(75, dospo_score + omf_score + orf_score)
    overall_pct = round((total_score / 75) * 100, 1)

    # Classification Logic with Hard-Gate on Level 3 (Requires net_replenishment_ratio >= 1.0)
    if overall_pct >= 85 and net_replenishment_ratio >= 1.0:
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
        "level_3_gate_passed": net_replenishment_ratio >= 1.0,
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
            "name": "Cardano Ecosystem Fully-Architected Input",
            "annual_maintenance_budget_usd": 3500000,
            "treasury_reserve_usd": 650000000,
            "annual_tx_fee_inflow_usd": 4500000,
            "annual_reserve_expansion_usd": 85000000,
            "annual_earned_non_inflation_usd": 450000,
            "indicator_1_legitimacy_charter": True,
            "indicator_2_neutrality_guarantee": True,
            "indicator_3_operator_replaceable": True,
            "indicator_4_policy_engine": True,
            "indicator_5_transparency_reporting": True,
            "indicator_6_maintainer_retainers": True,
            "indicator_7_contributor_pathways": True,
            "indicator_8_tooling_stewardship": True,
            "indicator_9_autonomy_safeguard": True,
            "indicator_10_impact_metrics": True,
            "indicator_12_fork_resistance": True,
            "indicator_13_benefit_bundling_slas": True,
            "indicator_14_ips_endowments": True,
            "indicator_15_independent_audit": True
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
    print(f"📊 CANONICAL SYSTEMS ASSESSMENT: {results['config_source']}")
    print(f"🏛️ dOSPO Governance Score  : {results['dospo_score']} / 25")
    print(f"🛠️ OMF Maintenance Score   : {results['omf_score']} / 25")
    print(f"💰 ORF Replenishment Score : {results['orf_score']} / 25")
    print(f"🏆 OVERALL SCORE           : {results['total_score']}/75 ({results['overall_pct']}%)")
    print(f"🔒 LEVEL 3 HARD GATE (>=1.0): {'PASSED' if results['level_3_gate_passed'] else 'NOT MET'}")
    print(f"🌱 MATURITY CLASSIFICATION : {results['level']}")
    print(f"💾 Results saved to        : {args.output_json}")
    print("=======================================================\n")

if __name__ == "__main__":
    main()
