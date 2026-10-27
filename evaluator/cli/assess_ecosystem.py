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

__version__ = "0.8.0-rc.1"

# Ensure UTF-8 output encoding on Windows terminals
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

GATE_NAMES = (
    (1, "Measurement"),
    (2, "Cash Evidence"),
    (3, "Net Coverage"),
    (4, "Multi-Class Diversity"),
    (5, "Concentration"),
    (6, "Stress Runway"),
    (7, "Liability Coverage"),
    (8, "Independent Audit"),
)


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Canonical 3-Piece Systems Assessor (75-Point Engine)"
    )
    parser.add_argument(
        "--version",
        action="version",
        version=__version__,
    )
    parser.add_argument(
        "config_file",
        nargs="?",
        default=None,
        help="Path to JSON system configuration file",
    )
    parser.add_argument(
        "--output-json",
        default=os.path.join("evaluator", "examples", "system_assessment_results.json"),
        help="Path to save JSON assessment results",
    )
    return parser.parse_args()


def score_indicator(val):
    # MUST check isinstance(val, bool) BEFORE isinstance(val, (int, float))
    # because bool is a subclass of int in Python!
    if isinstance(val, bool):
        return 5 if val else 0
    elif isinstance(val, (int, float)):
        if val >= 5:
            return 5
        elif val >= 3:
            return 3
        else:
            return 0
    return 0


def _as_number(value):
    """A real number. Booleans and strings are not evidence."""
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return None
    return float(value)


def _money(config, key):
    number = _as_number(config.get(key))
    return 0.0 if number is None else number


def _unique_classes(value):
    if not isinstance(value, list):
        return []
    seen = []
    for item in value:
        if not isinstance(item, str):
            continue
        name = item.strip()
        if name and name not in seen:
            seen.append(name)
    return seen


def evaluate_hard_gates(config):
    """Eight governance gates from orf/GOVERNANCE_RULES.md.

    A missing hard_gates object is not a pass. Every gate stays NOT MET until
    the input carries the evidence that gate asks for. The point-rubric
    replenishment ratio is a separate line and is not one of these gates.
    """
    raw = config.get("hard_gates", None)
    provided = isinstance(raw, dict)
    gates = raw if provided else {}

    budget = _as_number(config.get("annual_maintenance_budget_usd"))
    portfolio = None
    if budget is not None and budget > 0:
        portfolio = (
            _money(config, "annual_tx_fee_inflow_usd")
            + _money(config, "annual_earned_non_inflation_usd")
            + _money(config, "annual_yield_net_usd")
            + _money(config, "annual_pledges_net_usd")
        ) / budget

    def flagged(key):
        return gates.get(key) is True

    classes = _unique_classes(gates.get("revenue_classes"))
    share = _as_number(gates.get("largest_payer_share")) if "largest_payer_share" in gates else None
    stress_ratio = (
        _as_number(gates.get("stress_coverage_ratio"))
        if "stress_coverage_ratio" in gates
        else None
    )
    runway_months = (
        _as_number(gates.get("stressed_runway_months"))
        if "stressed_runway_months" in gates
        else None
    )

    met = {
        1: provided and flagged("measurement_verified") and budget is not None and budget > 0,
        2: provided and flagged("cash_evidence_audited"),
        3: provided and portfolio is not None and portfolio >= 1.0,
        4: provided and len(classes) >= 2,
        5: provided and share is not None and 0.0 <= share <= 0.25,
        6: (
            provided
            and stress_ratio is not None
            and runway_months is not None
            and stress_ratio >= 1.0
            and runway_months >= 24
        ),
        7: provided and flagged("liabilities_covered"),
        8: provided and flagged("independent_audit_published"),
    }

    listed = [{"id": gate_id, "name": name, "met": met[gate_id]} for gate_id, name in GATE_NAMES]
    return {
        "evidence_provided": provided,
        "portfolio_coverage_ratio": None if portfolio is None else round(portfolio, 4),
        "gates": listed,
        "all_met": all(item["met"] for item in listed),
    }


def analyze_system_data(config):
    budget = config.get("annual_maintenance_budget_usd", 0)
    fees = config.get("annual_tx_fee_inflow_usd", 0)
    earned_rev = config.get("annual_earned_non_inflation_usd", 0)
    reserves = config.get("treasury_reserve_usd", 0)

    net_non_inflationary = fees + earned_rev

    # Raw ratio for strict unrounded thresholding.
    # Indicator 11 uses fees and earned income only. Yield and pledges are
    # part of portfolio coverage (gate 3) and are not added here.
    raw_ratio = (net_non_inflationary / budget) if budget > 0 else 0.0
    net_replenishment_ratio = round(raw_ratio, 4)
    runway_years = round((reserves * 0.50) / budget, 1) if budget > 0 else 0.0

    # 1. dOSPO Governance Indicators (0–25 Pts)
    dospo_score = sum(
        [
            score_indicator(config.get("indicator_1_legitimacy_charter")),
            score_indicator(config.get("indicator_2_neutrality_guarantee")),
            score_indicator(config.get("indicator_3_operator_replaceable")),
            score_indicator(config.get("indicator_4_policy_engine")),
            score_indicator(config.get("indicator_5_transparency_reporting")),
        ]
    )

    # 2. OMF Maintenance Indicators (0–25 Pts)
    omf_score = sum(
        [
            score_indicator(config.get("indicator_6_maintainer_retainers")),
            score_indicator(config.get("indicator_7_contributor_pathways")),
            score_indicator(config.get("indicator_8_tooling_stewardship")),
            score_indicator(config.get("indicator_9_autonomy_safeguard")),
            score_indicator(config.get("indicator_10_impact_metrics")),
        ]
    )

    # 3. ORF Replenishment Indicators (0–25 Pts)
    if raw_ratio >= 1.0:
        ind_11_score = 5
    elif raw_ratio >= 0.20:
        ind_11_score = 3
    else:
        ind_11_score = 0

    orf_score = sum(
        [
            ind_11_score,
            score_indicator(config.get("indicator_12_fork_resistance")),
            score_indicator(config.get("indicator_13_benefit_bundling_slas")),
            score_indicator(config.get("indicator_14_ips_endowments")),
            score_indicator(config.get("indicator_15_independent_audit")),
        ]
    )

    total_score = min(75, dospo_score + omf_score + orf_score)
    overall_pct = round((total_score / 75) * 100, 1)

    # Raw unrounded ratio threshold for the point-rubric Level 3 line.
    # This is not the eight governance hard gates.
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
            "bear_market_runway_years": runway_years,
        },
        "hard_gates": evaluate_hard_gates(config),
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

    output_dir = os.path.dirname(args.output_json)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
    with open(args.output_json, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)

    print("\n=======================================================")
    print(f"📊 CANONICAL SYSTEMS ASSESSMENT: {results['config_source']}")
    print(f"🏛️ dOSPO Governance Score  : {results['dospo_score']} / 25")
    print(f"🛠️ OMF Maintenance Score   : {results['omf_score']} / 25")
    print(f"💰 ORF Replenishment Score : {results['orf_score']} / 25")
    print(f"🏆 TOTAL POINT SCORE       : {results['total_score']} / 75 ({results['overall_pct']}%)")
    print(f"🔒 LEVEL 3 HARD GATE (>=1.0): {'PASSED' if results['level_3_gate_passed'] else 'NOT MET'}")
    if "hypothetical" in str(results["config_source"]).lower():
        print("   This ratio line is hypothetical sample output. It is not the eight governance hard gates.")
    print("Eight governance hard gates (missing evidence is NOT MET):")
    for gate in results["hard_gates"]["gates"]:
        state = "MET" if gate["met"] else "NOT MET"
        print(f"  Gate {gate['id']} {gate['name']}: {state}")
    print(f"  All eight: {'MET' if results['hard_gates']['all_met'] else 'NOT MET'}")
    print(f"💾 Results saved to        : {args.output_json}")
    print("=======================================================\n")


if __name__ == "__main__":
    main()
