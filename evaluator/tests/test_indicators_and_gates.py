#!/usr/bin/env python3
"""Indicator, level-boundary, and eight-gate tests for the ecosystem assessor."""

import os
import sys
import json
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "cli"))
from assess_ecosystem import analyze_system_data

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

SCORED_INDICATORS = [
    (1, "indicator_1_legitimacy_charter", "dospo_score"),
    (2, "indicator_2_neutrality_guarantee", "dospo_score"),
    (3, "indicator_3_operator_replaceable", "dospo_score"),
    (4, "indicator_4_policy_engine", "dospo_score"),
    (5, "indicator_5_transparency_reporting", "dospo_score"),
    (6, "indicator_6_maintainer_retainers", "omf_score"),
    (7, "indicator_7_contributor_pathways", "omf_score"),
    (8, "indicator_8_tooling_stewardship", "omf_score"),
    (9, "indicator_9_autonomy_safeguard", "omf_score"),
    (10, "indicator_10_impact_metrics", "omf_score"),
    (12, "indicator_12_fork_resistance", "orf_score"),
    (13, "indicator_13_benefit_bundling_slas", "orf_score"),
    (14, "indicator_14_ips_endowments", "orf_score"),
    (15, "indicator_15_independent_audit", "orf_score"),
]

VALUE_CASES = [
    (5, 5),
    (3, 3),
    (0, 0),
    (True, 5),
    (False, 0),
    (4, 3),
    (2, 0),
    ("5", 0),
]


def zero_ratio_config():
    return {
        "name": "Indicator case",
        "annual_maintenance_budget_usd": 1000,
        "annual_tx_fee_inflow_usd": 0,
        "annual_earned_non_inflation_usd": 0,
        "treasury_reserve_usd": 0,
    }


def with_indicators(values, budget=1000, fees=0, earned=0):
    config = {
        "name": "Level case",
        "annual_maintenance_budget_usd": budget,
        "annual_tx_fee_inflow_usd": fees,
        "annual_earned_non_inflation_usd": earned,
        "treasury_reserve_usd": 0,
    }
    config.update(values)
    return config


class TestEachIndicator(unittest.TestCase):
    def test_indicators_1_through_10_and_12_through_15(self):
        self.assertEqual(len(SCORED_INDICATORS), 14)
        for number, key, bucket in SCORED_INDICATORS:
            for raw, expected in VALUE_CASES:
                config = zero_ratio_config()
                config[key] = raw
                result = analyze_system_data(config)
                self.assertEqual(
                    result[bucket],
                    expected,
                    f"indicator {number} ({key}) value {raw!r} should score {expected}",
                )
            missing = analyze_system_data(zero_ratio_config())
            self.assertEqual(
                missing[bucket],
                0,
                f"indicator {number} ({key}) should score 0 when the key is absent",
            )

    def test_indicator_11_boundaries(self):
        exact_cover = analyze_system_data(with_indicators({}, budget=1000, fees=1000))
        self.assertEqual(exact_cover["orf_score"], 5)
        self.assertTrue(exact_cover["level_3_gate_passed"])

        exact_fifth = analyze_system_data(with_indicators({}, budget=1000, fees=200))
        self.assertEqual(exact_fifth["orf_score"], 3)
        self.assertEqual(exact_fifth["metrics"]["net_replenishment_ratio"], 0.2)

        just_under = analyze_system_data(with_indicators({}, budget=1000, fees=199))
        self.assertEqual(just_under["orf_score"], 0)
        self.assertLess(just_under["metrics"]["net_replenishment_ratio"], 0.2)

        zero_budget = analyze_system_data(with_indicators({}, budget=0, fees=500, earned=500))
        self.assertEqual(zero_budget["orf_score"], 0)
        self.assertFalse(zero_budget["level_3_gate_passed"])

    def test_yield_and_pledges_do_not_change_indicator_11(self):
        config = with_indicators({}, budget=100, fees=0, earned=0)
        config["annual_yield_net_usd"] = 80
        config["annual_pledges_net_usd"] = 20
        result = analyze_system_data(config)
        self.assertEqual(result["orf_score"], 0)
        self.assertFalse(result["level_3_gate_passed"])
        self.assertEqual(result["hard_gates"]["portfolio_coverage_ratio"], 1.0)
        self.assertFalse(result["hard_gates"]["gates"][2]["met"])


class TestLevelBoundaries(unittest.TestCase):
    def test_edges_with_ratio_at_least_one(self):
        fees = 1000
        cases = [
            (24, "Level 0: Un-Architected / Fragile", {"indicator_1_legitimacy_charter": 5, "indicator_2_neutrality_guarantee": 5, "indicator_3_operator_replaceable": 3, "indicator_4_policy_engine": 3, "indicator_5_transparency_reporting": 3}),
            (25, "Level 1: Governance & Retainers Bootstrapped", {"indicator_1_legitimacy_charter": 5, "indicator_2_neutrality_guarantee": 5, "indicator_3_operator_replaceable": 5, "indicator_4_policy_engine": 5}),
            (49, "Level 1: Governance & Retainers Bootstrapped", {
                "indicator_1_legitimacy_charter": 5,
                "indicator_2_neutrality_guarantee": 5,
                "indicator_3_operator_replaceable": 5,
                "indicator_4_policy_engine": 5,
                "indicator_5_transparency_reporting": 3,
                "indicator_6_maintainer_retainers": 3,
                "indicator_7_contributor_pathways": 3,
                "indicator_8_tooling_stewardship": 3,
                "indicator_9_autonomy_safeguard": 3,
                "indicator_10_impact_metrics": 3,
                "indicator_12_fork_resistance": 3,
                "indicator_13_benefit_bundling_slas": 3,
            }),
            (50, "Level 2: Fee-Supplemented Maintenance", {f"indicator_{n}_" + name: 5 for n, name in [
                (1, "legitimacy_charter"),
                (2, "neutrality_guarantee"),
                (3, "operator_replaceable"),
                (4, "policy_engine"),
                (5, "transparency_reporting"),
                (6, "maintainer_retainers"),
                (7, "contributor_pathways"),
                (8, "tooling_stewardship"),
                (9, "autonomy_safeguard"),
            ]}),
            (64, "Level 2: Fee-Supplemented Maintenance", {}),
        ]
        # 64 is filled below so the dict stays readable.
        sixty_four = {f"indicator_{n}_{name}": 5 for n, name in [
            (1, "legitimacy_charter"),
            (2, "neutrality_guarantee"),
            (3, "operator_replaceable"),
            (4, "policy_engine"),
            (5, "transparency_reporting"),
            (6, "maintainer_retainers"),
            (7, "contributor_pathways"),
            (8, "tooling_stewardship"),
            (9, "autonomy_safeguard"),
            (10, "impact_metrics"),
        ]}
        sixty_four.update({
            "indicator_12_fork_resistance": 3,
            "indicator_13_benefit_bundling_slas": 3,
            "indicator_14_ips_endowments": 3,
        })
        cases[4] = (64, "Level 2: Fee-Supplemented Maintenance", sixty_four)

        sixty_five = {key: 5 for key in [
            "indicator_1_legitimacy_charter",
            "indicator_2_neutrality_guarantee",
            "indicator_3_operator_replaceable",
            "indicator_4_policy_engine",
            "indicator_5_transparency_reporting",
            "indicator_6_maintainer_retainers",
            "indicator_7_contributor_pathways",
            "indicator_8_tooling_stewardship",
            "indicator_9_autonomy_safeguard",
            "indicator_10_impact_metrics",
            "indicator_12_fork_resistance",
            "indicator_13_benefit_bundling_slas",
        ]}
        cases.append((65, "Level 3: Self-Sustaining Closed Loop", sixty_five))

        for expected_score, expected_level, values in cases:
            result = analyze_system_data(with_indicators(values, budget=1000, fees=fees))
            self.assertEqual(result["total_score"], expected_score, values)
            self.assertEqual(result["level"], expected_level)
            self.assertTrue(result["level_3_gate_passed"])

    def test_sixty_five_without_ratio_stays_level_2(self):
        values = {key: 5 for _n, key, _bucket in SCORED_INDICATORS}
        values["indicator_15_independent_audit"] = 0
        result = analyze_system_data(with_indicators(values, budget=1000, fees=0))
        self.assertEqual(result["total_score"], 65)
        self.assertFalse(result["level_3_gate_passed"])
        self.assertEqual(result["level"], "Level 2: Fee-Supplemented Maintenance")


def passing_gates():
    return {
        "measurement_verified": True,
        "cash_evidence_audited": True,
        "revenue_classes": ["protocol fees", "enterprise contracts"],
        "largest_payer_share": 0.25,
        "stress_coverage_ratio": 1.0,
        "stressed_runway_months": 24,
        "liabilities_covered": True,
        "independent_audit_published": True,
    }


class TestEightHardGates(unittest.TestCase):
    def _result(self, **overrides):
        config = with_indicators({}, budget=100, fees=40, earned=30)
        config["annual_yield_net_usd"] = 20
        config["annual_pledges_net_usd"] = 10
        config["hard_gates"] = passing_gates()
        config.update(overrides)
        return analyze_system_data(config)

    def test_missing_object_is_not_met(self):
        config = with_indicators({}, budget=100, fees=200)
        result = analyze_system_data(config)
        self.assertFalse(result["hard_gates"]["evidence_provided"])
        self.assertFalse(result["hard_gates"]["all_met"])
        for gate in result["hard_gates"]["gates"]:
            self.assertFalse(gate["met"], gate["name"])
        self.assertEqual(len(result["hard_gates"]["gates"]), 8)

    def test_complete_evidence_meets_all_eight(self):
        result = self._result()
        self.assertTrue(result["hard_gates"]["all_met"])
        self.assertEqual(
            [gate["name"] for gate in result["hard_gates"]["gates"]],
            [
                "Measurement",
                "Cash Evidence",
                "Net Coverage",
                "Multi-Class Diversity",
                "Concentration",
                "Stress Runway",
                "Liability Coverage",
                "Independent Audit",
            ],
        )

    def test_string_true_is_not_evidence(self):
        gates = passing_gates()
        for key in (
            "measurement_verified",
            "cash_evidence_audited",
            "liabilities_covered",
            "independent_audit_published",
        ):
            gates[key] = "true"
        gates["largest_payer_share"] = "0.2"
        gates["stress_coverage_ratio"] = "1"
        result = self._result(hard_gates=gates)
        met = {gate["id"]: gate["met"] for gate in result["hard_gates"]["gates"]}
        self.assertFalse(met[1])
        self.assertFalse(met[2])
        self.assertTrue(met[3])
        self.assertTrue(met[4])
        self.assertFalse(met[5])
        self.assertFalse(met[6])
        self.assertFalse(met[7])
        self.assertFalse(met[8])
        self.assertFalse(result["hard_gates"]["all_met"])

    def test_gate_1_needs_a_positive_budget(self):
        result = self._result(annual_maintenance_budget_usd=0, annual_tx_fee_inflow_usd=0)
        met = {gate["id"]: gate["met"] for gate in result["hard_gates"]["gates"]}
        self.assertFalse(met[1])
        self.assertFalse(met[3])

    def test_gate_3_exact_cover_and_just_under(self):
        covered = self._result()
        self.assertTrue(covered["hard_gates"]["gates"][2]["met"])
        under = with_indicators({}, budget=100, fees=99)
        under["hard_gates"] = passing_gates()
        under_result = analyze_system_data(under)
        self.assertFalse(under_result["hard_gates"]["gates"][2]["met"])
        self.assertFalse(under_result["hard_gates"]["all_met"])

    def test_gate_4_class_edges(self):
        for classes, expected in (
            (["protocol fees"], False),
            (["protocol fees", "protocol fees"], False),
            (["protocol fees", " enterprise contracts "], True),
            (["protocol fees", ""], False),
            (["protocol fees", 2], False),
            ("protocol fees", False),
        ):
            gates = passing_gates()
            gates["revenue_classes"] = classes
            result = self._result(hard_gates=gates)
            self.assertEqual(result["hard_gates"]["gates"][3]["met"], expected, classes)

    def test_gate_5_share_edges(self):
        for share, expected in ((-0.01, False), (0, True), (0.25, True), (0.2500001, False), (None, False)):
            gates = passing_gates()
            if share is None:
                del gates["largest_payer_share"]
            else:
                gates["largest_payer_share"] = share
            result = self._result(hard_gates=gates)
            self.assertEqual(result["hard_gates"]["gates"][4]["met"], expected, share)

    def test_gate_6_stress_edges(self):
        for ratio, months, expected in (
            (1.0, 24, True),
            (1.0, 23.999, False),
            (0.999, 24, False),
            (True, 24, False),
            (1.0, True, False),
        ):
            gates = passing_gates()
            gates["stress_coverage_ratio"] = ratio
            gates["stressed_runway_months"] = months
            result = self._result(hard_gates=gates)
            self.assertEqual(result["hard_gates"]["gates"][5]["met"], expected, (ratio, months))

    def test_sample_config_does_not_pass_the_eight_gates(self):
        path = os.path.join(ROOT, "evaluator", "examples", "sample_input_config.json")
        with open(path, "r", encoding="utf-8") as handle:
            sample = json.load(handle)
        result = analyze_system_data(sample)
        self.assertIn("hypothetical", result["config_source"].lower())
        self.assertTrue(result["level_3_gate_passed"])
        self.assertFalse(result["hard_gates"]["all_met"])
        self.assertTrue(all(not gate["met"] for gate in result["hard_gates"]["gates"]))


if __name__ == "__main__":
    unittest.main()
