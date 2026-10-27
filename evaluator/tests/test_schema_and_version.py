#!/usr/bin/env python3
"""Schema, version, and Python/JavaScript parity checks."""

import json
import os
import subprocess
import sys
import tomllib
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "cli"))
import assess_ecosystem

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))


def load(path):
    with open(path, "r", encoding="utf-8") as handle:
        return json.load(handle)


class TestSchemaAndVersion(unittest.TestCase):
    def test_versions_match_the_tagged_release(self):
        with open(os.path.join(ROOT, "evaluator", "pyproject.toml"), "r", encoding="utf-8") as handle:
            pyproject = tomllib.loads(handle.read())
        package = load(os.path.join(ROOT, "evaluator", "cli", "package.json"))
        self.assertEqual(pyproject["project"]["version"], "0.8.0-rc.1")
        self.assertEqual(package["version"], "0.8.0-rc.1")
        self.assertEqual(assess_ecosystem.__version__, "0.8.0-rc.1")
        self.assertEqual(pyproject["project"]["authors"][0]["name"], "OSF Lab contributors")
        self.assertEqual(package["author"], "OSF Lab contributors")

    def test_cli_version_flags(self):
        python = subprocess.run(
            [sys.executable, os.path.join(ROOT, "evaluator", "cli", "assess_ecosystem.py"), "--version"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        node = subprocess.run(
            ["node", os.path.join(ROOT, "evaluator", "cli", "index.js"), "--version"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(python.returncode, 0, python.stderr)
        self.assertEqual(python.stdout.strip(), "0.8.0-rc.1")
        self.assertEqual(node.returncode, 0, node.stderr)
        self.assertEqual(node.stdout.strip(), "0.8.0-rc.1")

    def test_sample_matches_schema_and_a_wrong_type_does_not(self):
        jsonschema = __import__("jsonschema")
        schema = load(os.path.join(ROOT, "evaluator", "schema", "sample_input_config.schema.json"))
        jsonschema.Draft202012Validator.check_schema(schema)
        validator = jsonschema.Draft202012Validator(schema)
        sample = load(os.path.join(ROOT, "evaluator", "examples", "sample_input_config.json"))
        self.assertEqual(list(validator.iter_errors(sample)), [])

        broken = dict(sample)
        broken["indicator_1_legitimacy_charter"] = {"score": 5}
        self.assertTrue(list(validator.iter_errors(broken)))

        extra = dict(sample)
        extra["invented_field"] = 1
        self.assertTrue(list(validator.iter_errors(extra)))


def assert_close(testcase, actual, expected, path):
    if isinstance(expected, float) or isinstance(actual, float):
        testcase.assertAlmostEqual(float(actual), float(expected), places=9, msg=path)
    elif isinstance(expected, dict):
        testcase.assertEqual(set(actual), set(expected), path)
        for key in expected:
            assert_close(testcase, actual[key], expected[key], f"{path}.{key}")
    elif isinstance(expected, list):
        testcase.assertEqual(len(actual), len(expected), path)
        for index, (left, right) in enumerate(zip(actual, expected)):
            assert_close(testcase, left, right, f"{path}[{index}]")
    else:
        testcase.assertEqual(actual, expected, path)


class TestJavaScriptParity(unittest.TestCase):
    def test_node_matches_python_on_shared_inputs(self):
        sample = load(os.path.join(ROOT, "evaluator", "examples", "sample_input_config.json"))
        configs = [
            sample,
            {
                "name": "Empty",
                "annual_maintenance_budget_usd": 0,
                "annual_tx_fee_inflow_usd": 10,
            },
            {
                "name": "Boolean and string",
                "annual_maintenance_budget_usd": 1000,
                "treasury_reserve_usd": 650000000,
                "annual_tx_fee_inflow_usd": 200,
                "indicator_1_legitimacy_charter": True,
                "indicator_6_maintainer_retainers": False,
                "indicator_12_fork_resistance": "5",
                "hard_gates": {
                    "measurement_verified": "true",
                    "cash_evidence_audited": True,
                    "revenue_classes": ["a", " a ", "b"],
                    "largest_payer_share": 0.25,
                    "stress_coverage_ratio": 1,
                    "stressed_runway_months": 24,
                    "liabilities_covered": True,
                    "independent_audit_published": False,
                },
            },
            {
                "annual_maintenance_budget_usd": 3500000,
                "annual_tx_fee_inflow_usd": 4500000,
                "annual_earned_non_inflation_usd": 450000,
                "annual_yield_net_usd": 10,
                "annual_pledges_net_usd": 5,
                "treasury_reserve_usd": 650000000,
                "indicator_3_operator_replaceable": 4,
                "indicator_10_impact_metrics": 2,
            },
        ]
        for config in configs:
            expected = assess_ecosystem.analyze_system_data(config)
            proc = subprocess.run(
                ["node", os.path.join(ROOT, "evaluator", "cli", "analyze_system.js")],
                input=json.dumps(config),
                cwd=ROOT,
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(proc.returncode, 0, proc.stderr)
            actual = json.loads(proc.stdout)
            assert_close(self, actual, expected, config.get("name", "unnamed"))


if __name__ == "__main__":
    unittest.main()
