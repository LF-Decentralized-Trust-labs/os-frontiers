#!/usr/bin/env python3
"""
Comprehensive Unit Test Suite for 3-Piece Ecosystem Assessor (evaluator/cli/assess_ecosystem.py)
Tests 15-indicator scoring, 0/3/5 partial scores, Level 0 reachability, and Level 3 Hard-Gate
"""

import sys
import os
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "cli"))
from assess_ecosystem import analyze_system_data

class TestEcosystemAssessor(unittest.TestCase):

    def test_level_0_unarchitected(self):
        """Zero indicators satisfied must return Level 0 (0% score)."""
        empty_config = {
            "name": "Empty Test System",
            "annual_maintenance_budget_usd": 1000000,
            "treasury_reserve_usd": 0,
            "annual_tx_fee_inflow_usd": 0,
            "annual_reserve_expansion_usd": 0,
            "annual_earned_non_inflation_usd": 0
        }
        res = analyze_system_data(empty_config)
        self.assertEqual(res["total_score"], 0)
        self.assertEqual(res["overall_pct"], 0.0)
        self.assertEqual(res["level"], "Level 0: Un-Architected / Fragile")

    def test_partial_scoring_support(self):
        """Indicators with partial score (3 Pts) must accumulate correctly."""
        partial_config = {
            "name": "Partial Test System",
            "annual_maintenance_budget_usd": 1000000,
            "annual_tx_fee_inflow_usd": 100000,
            "indicator_1_legitimacy_charter": 3,
            "indicator_6_maintainer_retainers": 3
        }
        res = analyze_system_data(partial_config)
        self.assertEqual(res["dospo_score"], 3)
        self.assertEqual(res["omf_score"], 3)
        self.assertEqual(res["total_score"], 6)

    def test_level_3_hard_gate_enforcement(self):
        """Ecosystem with 100% dOSPO + OMF but Replenishment Ratio < 1.0 CANNOT reach Level 3."""
        config = {
            "name": "High Governance Low Replenishment Test",
            "annual_maintenance_budget_usd": 3000000,
            "annual_tx_fee_inflow_usd": 600000,  # Ratio = 0.20 (20%)
            "annual_earned_non_inflation_usd": 0,
            "indicator_1_legitimacy_charter": 5,
            "indicator_2_neutrality_guarantee": 5,
            "indicator_3_operator_replaceable": 5,
            "indicator_4_policy_engine": 5,
            "indicator_5_transparency_reporting": 5,
            "indicator_6_maintainer_retainers": 5,
            "indicator_7_contributor_pathways": 5,
            "indicator_8_tooling_stewardship": 5,
            "indicator_9_autonomy_safeguard": 5,
            "indicator_10_impact_metrics": 5,
            "indicator_12_fork_resistance": 5,
            "indicator_13_benefit_bundling_slas": 5,
            "indicator_14_ips_endowments": 5,
            "indicator_15_independent_audit": 5
        }
        res = analyze_system_data(config)
        self.assertFalse(res["level_3_gate_passed"])
        self.assertNotEqual(res["level"], "Level 3: Self-Sustaining Closed Loop")
        self.assertEqual(res["level"], "Level 2: Fee-Supplemented Maintenance")

    def test_level_3_success_when_gate_passed(self):
        """Ecosystem with high governance + Replenishment Ratio >= 1.0 MUST reach Level 3."""
        config = {
            "name": "Full Sustainable Loop System",
            "annual_maintenance_budget_usd": 3000000,
            "annual_tx_fee_inflow_usd": 3500000,  # Ratio = 1.1667 (>= 1.0)
            "annual_earned_non_inflation_usd": 500000,
            "indicator_1_legitimacy_charter": 5,
            "indicator_2_neutrality_guarantee": 5,
            "indicator_3_operator_replaceable": 5,
            "indicator_4_policy_engine": 5,
            "indicator_5_transparency_reporting": 5,
            "indicator_6_maintainer_retainers": 5,
            "indicator_7_contributor_pathways": 5,
            "indicator_8_tooling_stewardship": 5,
            "indicator_9_autonomy_safeguard": 5,
            "indicator_10_impact_metrics": 5,
            "indicator_12_fork_resistance": 5,
            "indicator_13_benefit_bundling_slas": 5,
            "indicator_14_ips_endowments": 5,
            "indicator_15_independent_audit": 5
        }
        res = analyze_system_data(config)
        self.assertTrue(res["level_3_gate_passed"])
        self.assertEqual(res["level"], "Level 3: Self-Sustaining Closed Loop")

if __name__ == "__main__":
    unittest.main()
