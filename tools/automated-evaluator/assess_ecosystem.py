#!/usr/bin/env python3
"""
Automated 3-Piece Ecosystem Systems & Capital Flow Assessor (dOSPO · OMF · ORF)
LF Decentralized Trust · Open Source Frontiers Lab
"""

import sys
import os
import json
import argparse
import io

# Ensure UTF-8 output encoding on Windows terminals
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Ecosystem Presets with System & Capital Flow Parameters
ECOSYSTEM_PRESETS = {
    "cardano": {
        "name": "Cardano (Paid Open Source Model / POSM Pilot)",
        "chain_type": "UTXO / Proof-of-Stake (NPoS)",
        "governance_model": "CIP-1694 (DReps, SPOs, Constitutional Committee, Intersect MBO)",
        "treasury_inflow_mechanism": "20% Treasury Fee Split (Monetary Expansion + Tx Fees)",
        "annual_maintenance_budget_usd": 3500000,
        "treasury_reserve_usd": 650000000, # Approx 1.4B ADA @ ~$0.45
        "annual_tx_fee_inflow_usd": 4500000,
        "annual_reserve_expansion_usd": 85000000,
        "annual_earned_non_inflation_usd": 450000, # Initial SLA & Mission pool margin pledges
        "maintainer_retainer_program": True, # POSM Retainer pilot via Intersect OSC
        "maintainer_autonomy_guarantee": True,
        "independent_audit_published": True,
        "ips_yield_sleeve_active": False, # Reserves held primarily in native ADA
    },
    "optimism": {
        "name": "Optimism Superchain",
        "chain_type": "EVM L2 Rollup",
        "governance_model": "Optimism Collective (Token House & Citizens' House)",
        "treasury_inflow_mechanism": "Sequencer Tithe (Surplus transaction fees)",
        "annual_maintenance_budget_usd": 8000000,
        "treasury_reserve_usd": 450000000,
        "annual_tx_fee_inflow_usd": 12000000,
        "annual_reserve_expansion_usd": 60000000,
        "annual_earned_non_inflation_usd": 1200000,
        "maintainer_retainer_program": False, # Primary RetroPGF grant rounds
        "maintainer_autonomy_guarantee": True,
        "independent_audit_published": False,
        "ips_yield_sleeve_active": False,
    },
    "ethereum": {
        "name": "Ethereum & EVM Ecosystem",
        "chain_type": "EVM L1 Proof-of-Stake",
        "governance_model": "Off-chain EIP / Protocol Guild / ENS DAO (EP 6.46)",
        "treasury_inflow_mechanism": "ENS Registrar Fees + Protocol Guild 1% Pledge (EIP-1559 Burn Countermodel)",
        "annual_maintenance_budget_usd": 15000000,
        "treasury_reserve_usd": 250000000,
        "annual_tx_fee_inflow_usd": 0, # EIP-1559 burns base fee
        "annual_reserve_expansion_usd": 0,
        "annual_earned_non_inflation_usd": 18000000, # ENS Registrar + Octant Staking Yield
        "maintainer_retainer_program": True, # Protocol Guild vesting & retainers
        "maintainer_autonomy_guarantee": True,
        "independent_audit_published": True,
        "ips_yield_sleeve_active": True, # ENS EP 6.46 Endowment active
    }
}

def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Automated 3-Piece Systems & Capital Flow Assessor (dOSPO · OMF · ORF)"
    )
    parser.add_argument(
        "target",
        nargs="?",
        default="cardano",
        help="Ecosystem preset ('cardano', 'optimism', 'ethereum') or path to custom JSON system config"
    )
    parser.add_argument(
        "--output-json",
        default="cardano_system_assessment.json",
        help="Path to save JSON assessment results"
    )
    parser.add_argument(
        "--output-md",
        default="CARDANO_SYSTEM_ASSESSMENT.md",
        help="Path to save Markdown assessment report"
    )
    return parser.parse_args()

def analyze_system_capital_flow(config):
    print(f"📊 Analyzing Capital Flow & System Architecture for: {config['name']}...")

    budget = config["annual_maintenance_budget_usd"]
    fees = config["annual_tx_fee_inflow_usd"]
    reserve_exp = config["annual_reserve_expansion_usd"]
    earned_rev = config["annual_earned_non_inflation_usd"]
    reserves = config["treasury_reserve_usd"]

    # 1. Capital Flow Metrics
    total_inflow = fees + reserve_exp + earned_rev
    net_non_inflationary_inflow = fees + earned_rev
    
    # Net Replenishment Ratio (Non-Inflationary Income / Maintenance Budget)
    net_replenishment_ratio = round(net_non_inflationary_inflow / budget, 2) if budget > 0 else 0
    
    # Gross Coverage Ratio (Total Inflow / Maintenance Budget)
    gross_coverage_ratio = round(total_inflow / budget, 2) if budget > 0 else 0
    
    # Treasury Bear Market Runway (Years of budget fundable under 50% price crash)
    bear_market_reserves = reserves * 0.50
    runway_years = round(bear_market_reserves / budget, 1) if budget > 0 else 0

    # 2. Vector Scoring (Out of 25 Pts per Vector)
    
    # Vector 1: dOSPO Governance Authority (WHO)
    dospo_score = 15 # Baseline for structured governance
    if "CIP-1694" in config["governance_model"] or "OpenGov" in config["governance_model"]:
        dospo_score += 5
    if config["independent_audit_published"]:
        dospo_score += 5
    dospo_score = min(25, dospo_score)

    # Vector 2: OMF Deployment & Maintainer Retainers (HOW SPEND)
    omf_score = 10
    if config["maintainer_retainer_program"]:
        omf_score += 10
    if config["maintainer_autonomy_guarantee"]:
        omf_score += 5
    omf_score = min(25, omf_score)

    # Vector 3: ORF Value Replenishment & Capital Flow (HOW COLLECT)
    orf_score = 5
    if net_replenishment_ratio >= 1.0:
        orf_score += 12
    elif net_replenishment_ratio >= 0.5:
        orf_score += 8
    elif net_replenishment_ratio >= 0.2:
        orf_score += 5
    
    if config["ips_yield_sleeve_active"]:
        orf_score += 5
    if earned_rev > 0:
        orf_score += 3
    orf_score = min(25, orf_score)

    # 3. Overall Scoring & Classification
    total_score = dospo_score + omf_score + orf_score
    overall_pct = round((total_score / 75) * 100, 1)

    if overall_pct >= 85:
        level = "Level 3: Self-Sustaining Closed Loop"
        action = "Maintain IPS yield sleeve & expand enterprise SLA reciprocal contracts."
    elif overall_pct >= 65:
        level = "Level 2: Fee-Supplemented Maintenance"
        action = "Capital flow active. Deploy productive IPS endowment sleeve to cover remaining gap."
    elif overall_pct >= 40:
        level = "Level 1: Governance & Retainers Bootstrapped"
        action = "dOSPO & OMF retainers active. Pilot Tier 1 Enterprise Maintenance SLAs."
    else:
        level = "Level 0: Un-Architected / Fragile"
        action = "High reserve drawdown risk. Establish time-limited dOSPO charter."

    return {
        "config": config,
        "dospo_score": dospo_score,
        "dospo_pct": round((dospo_score / 25) * 100, 1),
        "omf_score": omf_score,
        "omf_pct": round((omf_score / 25) * 100, 1),
        "orf_score": orf_score,
        "orf_pct": round((orf_score / 25) * 100, 1),
        "total_score": total_score,
        "overall_pct": overall_pct,
        "level": level,
        "action": action,
        "capital_metrics": {
            "maintenance_budget_usd": budget,
            "tx_fee_inflow_usd": fees,
            "reserve_expansion_usd": reserve_exp,
            "earned_non_inflation_usd": earned_rev,
            "net_non_inflationary_inflow_usd": net_non_inflationary_inflow,
            "net_replenishment_ratio": net_replenishment_ratio,
            "gross_coverage_ratio": gross_coverage_ratio,
            "bear_market_runway_years": runway_years
        }
    }

def generate_markdown_assessment(results):
    c = results["config"]
    m = results["capital_metrics"]
    
    return f"""# 3-Piece Systems & Capital Flow Assessment Report: {c['name']}

> **Target Ecosystem**: `{c['name']}` ({c['chain_type']})  
> **Governance Architecture**: `{c['governance_model']}`  
> **Inflow Mechanism**: `{c['treasury_inflow_mechanism']}`  
> **Evaluator Engine**: Open Source Frontiers Systems Engine v2.0 (LF Decentralized Trust)

---

## 1. Executive Summary & Maturity Classification

- **Overall Maturity Score**: **{results['total_score']} / 75 Points** ({results['overall_pct']}%)
- **System Maturity Level**: **{results['level']}**
- **Net Replenishment Ratio**: **{m['net_replenishment_ratio']}x** (`[ Non-Inflationary Income / Annual Maintenance Cost ]`)
- **Bear Market Treasury Runway**: **{m['bear_market_runway_years']} Years** (Stress-tested at 50% price drawdown)
- **Strategic Recommendation**: {results['action']}

---

## 2. Capital Flow & Financial Health Breakdown

| Financial Metric | Amount (USD / Year) | Assessment & Capital Impact |
|---|---|---|
| **Annual OMF Maintenance Budget** | **${m['maintenance_budget_usd']:,}** | Baseline cost floor to sustain core repos & retainers. |
| **Tx Fee Treasury Inflow** | **${m['tx_fee_inflow_usd']:,}** | Protocol-layer automatic fee split inflow. |
| **Monetary Reserve Expansion** | **${m['reserve_expansion_usd']:,}** | Reserve drawdown / monetary expansion subsidy. |
| **Earned Non-Inflationary Revenue** | **${m['earned_non_inflation_usd']:,}** | Maintenance SLAs, training, and stake pool pledges. |
| **TOTAL NON-INFLATIONARY INFLOW** | **${m['net_non_inflationary_inflow_usd']:,}** | **Net Replenishment Ratio: {m['net_replenishment_ratio']}x** |

---

## 3. 3-Piece Framework Pillar Diagnostics

### 🏛️ dOSPO Governance Authority (Score: {results['dospo_score']}/25 — {results['dospo_pct']}%)
- **Governance Model**: {c['governance_model']}
- **Legitimacy & Mandates**: Structured on-chain referenda (CIP-1694 DReps & SPOs) authorize spending.
- **Operator Replaceability**: Intersect MBO committees operate under time-limited community renewal votes.

### 🛠️ OMF Operational Deployment (Score: {results['omf_score']}/25 — {results['omf_pct']}%)
- **Maintainer Retainers**: Active Paid Open Source Model (POSM) retainer program deployed via Intersect OSC.
- **Maintainer Autonomy**: **Verified**. Retainer stipends support maintenance capacity without taking technical roadmap control.

### 💰 ORF Value Replenishment & Capital Flow (Score: {results['orf_score']}/25 — {results['orf_pct']}%)
- **Replenishment Posture**: Non-inflationary fee inflow (${m['tx_fee_inflow_usd']:,}) covers **{round((m['tx_fee_inflow_usd']/m['maintenance_budget_usd'])*100, 1)}%** of baseline maintenance.
- **Capital Layer IPS Sleeve**: **{ 'Active' if c['ips_yield_sleeve_active'] else 'Missing (Reserves held in native asset)' }**.
- **Action Plan**: Launch Tier 1 Enterprise Maintenance SLAs and enact an Investment Policy Statement (IPS) to convert native reserves into productive yield.

---

*Report generated by LF Decentralized Trust Open Source Frontiers Lab (`opensourcecowboy.org`)*
"""

def main():
    args = parse_arguments()
    preset_key = args.target.lower()
    
    if preset_key in ECOSYSTEM_PRESETS:
        config = ECOSYSTEM_PRESETS[preset_key]
    elif os.path.exists(args.target):
        with open(args.target, "r", encoding="utf-8") as f:
            config = json.load(f)
    else:
        print(f"Unknown preset or file '{args.target}'. Defaulting to 'cardano' preset...")
        config = ECOSYSTEM_PRESETS["cardano"]

    results = analyze_system_capital_flow(config)

    # Print summary to console
    m = results["capital_metrics"]
    print("\n=======================================================")
    print(f"📊 SYSTEMS & CAPITAL FLOW ASSESSMENT: {config['name']}")
    print("=======================================================")
    print(f"🏛️ dOSPO Governance Score : {results['dospo_score']}/25 ({results['dospo_pct']}%)")
    print(f"🛠️ OMF Deployment Score   : {results['omf_score']}/25 ({results['omf_pct']}%)")
    print(f"💰 ORF Replenishment Score: {results['orf_score']}/25 ({results['orf_pct']}%)")
    print(f"📈 Net Replenishment Ratio: {m['net_replenishment_ratio']}x")
    print(f"⏳ Bear Market Runway      : {m['bear_market_runway_years']} Years")
    print(f"🏆 OVERALL MATURITY       : {results['overall_pct']}% -> {results['level']}")
    print("=======================================================\n")

    # Save JSON Report
    with open(args.output_json, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)
    print(f"💾 JSON system assessment saved to: {args.output_json}")

    # Save Markdown Report
    md_content = generate_markdown_assessment(results)
    with open(args.output_md, "w", encoding="utf-8") as f:
        f.write(md_content)
    print(f"💾 Markdown report saved to: {args.output_md}")

if __name__ == "__main__":
    main()
