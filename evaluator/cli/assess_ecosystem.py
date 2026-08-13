#!/usr/bin/env python3
"""
Canonical 3-Piece Ecosystem Systems Assessor (dOSPO · OMF · ORF)
LF Decentralized Trust · Open Source Frontiers Lab
Full 15-Indicator 75-Point Engine with Corrected Boolean / Numeric Handling & Level 3 Gate
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
        description="Canonical 3-Piece Systems Assessor (75-Point Engine)"
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

def score_indicator(val):
    # MUST check isinstance(val, bool) BEFORE isinstance(val, (int, float))
    # because bool is a subclass of int in Python!
    if isinstance(val, bool):
        return 5 if val else 0
    elif isinstance(val, (int, float)):
        if val >= 5: return 5
        elif val >= 3: return 3
        else: return 0
    return 0

def analyze_system_data(config):
    budget = config.get("annual_maintenance_budget_usd", 0)
    fees = config.get("annual_tx_fee_inflow_usd", 0)
    earned_rev = config.get("annual_earned_non_inflation_usd", 0)
    reserves = config.get("treasury_reserve_usd", 0)

    net_non_inflationary = fees + earned_rev
    
    # Raw ratio for strict unrounded thresholding
    raw_ratio = (net_non_inflationary / budget) if budget > 0 else 0.0
    net_replenishment_ratio = round(raw_ratio, 4)
    runway_years = round((reserves * 0.50) / budget, 1) if budget > 0 else 0.0

    # 1. dOSPO Governance Indicators (0–25 Pts)
    dospo_score = sum([
        score_indicator(config.get("indicator_1_legitimacy_charter")),
        score_indicator(config.get("indicator_2_neutrality_guarantee")),
        score_indicator(config.get("indicator_3_operator_replaceable")),
        score_indicator(config.get("indicator_4_policy_engine")),
        score_indicator(config.get("indicator_5_transparency_reporting"))
    ])

    # 2. OMF Maintenance Indicators (0–25 Pts)
    omf_score = sum([
        score_indicator(config.get("indicator_6_maintainer_retainers")),
        score_indicator(config.get("indicator_7_contributor_pathways")),
        score_indicator(config.get("indicator_8_tooling_stewardship")),
        score_indicator(config.get("indicator_9_autonomy_safeguard")),
        score_indicator(config.get("indicator_10_impact_metrics"))
    ])

    # 3. ORF Replenishment Indicators (0–25 Pts)
    ind_11_score = 0
    if raw_ratio >= 1.0:
        ind_11_score = 5
    elif raw_ratio >= 0.20:
        ind_11_score = 3
    else:
        ind_11_score = 0

    orf_score = sum([
        ind_11_score,
        score_indicator(config.get("indicator_12_fork_resistance")),
        score_indicator(config.get("indicator_13_benefit_bundling_slas")),
        score_indicator(config.get("indicator_14_ips_endowments")),
        score_indicator(config.get("indicator_15_independent_audit"))
    ])

    total_score = min(75, dospo_score + omf_score + orf_score)
    overall_pct = round((total_score / 75) * 100, 1)

    # Raw unrounded ratio threshold for Level 3 gate
    level_3_gate_passed = raw_ratio >= 1.0

    # Exact Point-Based Classification Rules per 3-Piece Assessment Rubric (65 Pts Threshold)
    if total_score >= 65 and level_3_gate_passed:
        level = "Level 3: Self-Sustaining Closed Loop"
    elif total_score >= 50:
        level = "Level 2: Fee-Supplemented Maintenance"
    elif total_score >= 25:
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
        "level_3_gate_passed": level_3_gate_passed,
        "metrics": {
            "annual_maintenance_budget_usd": budget,
            "net_replenishment_ratio": net_replenishment_ratio,
            "bear_market_runway_years": runway_years
        }
    }

def main():
    args = parse_arguments()

    if not args.config_file or not os.path.exists(args.config_file):
        print(f"❌ Error: Config file not provided or not found: {args.config_file}", file=sys.stderr)
        print("Usage: python evaluator/cli/assess_ecosystem.py <path_to_config.json>", file=sys.stderr)
        sys.exit(2)

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
    print(f"🏆 TOTAL POINT SCORE       : {results['total_score']} / 75 ({results['overall_pct']}%)")
    print(f"🔒 LEVEL 3 HARD GATE (>=1.0): {'PASSED' if results['level_3_gate_passed'] else 'NOT MET'}")
    print(f"🌱 MATURITY CLASSIFICATION : {results['level']}")
    print(f"💾 Results saved to        : {args.output_json}")
    print("=======================================================\n")

if __name__ == "__main__":
    main()
