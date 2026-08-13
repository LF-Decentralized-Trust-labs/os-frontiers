#!/usr/bin/env python3
"""
Automated 3-Piece Ecosystem Systems & Capital Flow Assessor (dOSPO · OMF · ORF)
LF Decentralized Trust · Open Source Frontiers Lab
No Hardcoded Mock Overrides Engine
"""

import sys
import os
import json
import argparse
import urllib.request
import ssl
import io

# Ensure UTF-8 output encoding on Windows terminals
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

SSL_CTX = ssl._create_unverified_context()
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN") or os.environ.get("GITHUB_PERSONAL_ACCESS_TOKEN")

def get_headers():
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) OpenSourceFrontiersAssessor/2.0"}
    if GITHUB_TOKEN:
        headers["Authorization"] = f"Bearer {GITHUB_TOKEN}"
    return headers

def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Dynamic 3-Piece Systems Assessor (No Mock Overrides)"
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

    if budget == 0:
        raise ValueError("Error: 'annual_maintenance_budget_usd' must be > 0 in configuration file.")

    total_inflow = fees + reserve_exp + earned_rev
    net_non_inflationary = fees + earned_rev
    net_replenishment_ratio = round(net_non_inflationary / budget, 2)
    runway_years = round((reserves * 0.50) / budget, 1)

    # Dynamic Scoring Vectors
    dospo_score = 15
    if config.get("has_community_charter", False):
        dospo_score += 5
    if config.get("operator_replaceable", False):
        dospo_score += 5

    omf_score = 10
    if config.get("maintainer_retainer_program", False):
        omf_score += 10
    if config.get("maintainer_autonomy_guarantee", False):
        omf_score += 5

    orf_score = 5
    if net_replenishment_ratio >= 1.0:
        orf_score += 12
    elif net_replenishment_ratio >= 0.5:
        orf_score += 8
    elif net_replenishment_ratio >= 0.2:
        orf_score += 5

    if config.get("ips_yield_sleeve_active", False):
        orf_score += 5
    if earned_rev > 0:
        orf_score += 3

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
        print("⚠️ No valid JSON configuration file provided. Creating template input file...")
        sample_config = {
            "name": "Ecosystem Dynamic Input",
            "annual_maintenance_budget_usd": 3500000,
            "treasury_reserve_usd": 650000000,
            "annual_tx_fee_inflow_usd": 4500000,
            "annual_reserve_expansion_usd": 85000000,
            "annual_earned_non_inflation_usd": 450000,
            "has_community_charter": True,
            "operator_replaceable": True,
            "maintainer_retainer_program": True,
            "maintainer_autonomy_guarantee": True,
            "ips_yield_sleeve_active": False
        }
        config_path = os.path.join("evaluator", "examples", "sample_input_config.json")
        os.makedirs(os.path.dirname(config_path), exist_ok=True)
        with open(config_path, "w", encoding="utf-8") as f:
            json.dump(sample_config, f, indent=2)
        print(f"📄 Sample configuration created at: {config_path}")
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
    print(f"🏆 OVERALL MATURITY SCORE: {results['total_score']}/75 ({results['overall_pct']}%) -> {results['level']}")
    print(f"💾 Results saved to: {args.output_json}")
    print("=======================================================\n")

if __name__ == "__main__":
    main()
