#!/usr/bin/env python3
"""
Unit Test Suite for 3-Piece Ecosystem Systems Assessor (evaluator/cli/assess_ecosystem.py)
Tests 15-indicator scoring, Level 0 reachability, and Level 3 Replenishment Ratio Hard-Gate
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

    def test_level_3_hard_gate_enforcement(self):
        """Ecosystem with 100% dOSPO + OMF but Replenishment Ratio < 1.0 CANNOT reach Level 3."""
        config = {
            "name": "High Governance Low Replenishment Test",
            "annual_maintenance_budget_usd": 3000000,
            "annual_tx_fee_inflow_usd": 600000,  # Ratio = 0.20 (20%)
            "annual_earned_non_inflation_usd": 0,
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
        res = analyze_system_data(config)
        self.assertTrue(res["level_3_gate_passed"])
        self.assertEqual(res["level"], "Level 3: Self-Sustaining Closed Loop")

if __name__ == "__main__":
    unittest.main()
