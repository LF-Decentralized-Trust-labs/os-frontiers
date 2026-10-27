#!/usr/bin/env python3
"""Offline QUAID adapter tests. These must not call the GitHub API."""

import json
import os
import subprocess
import sys
import unittest
from unittest import mock

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "cli"))
import quaid_adapter

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
FIXTURE = os.path.join(ROOT, "evaluator", "fixtures", "quaid_cardano_node.json")


def load_fixture():
    with open(FIXTURE, "r", encoding="utf-8") as handle:
        return json.load(handle)


class TestQuaidFixture(unittest.TestCase):
    def test_fixture_does_not_call_the_network(self):
        def explode(*_args, **_kwargs):
            raise AssertionError("urlopen was called")

        with mock.patch("urllib.request.urlopen", explode):
            report = quaid_adapter.analyze_repo_heuristics(
                "intersectmbo/cardano-node",
                fixture=load_fixture(),
            )

        self.assertEqual(report["data_source"], "fixture")
        self.assertTrue(report["metrics_are_measurement"])
        self.assertEqual(report["metrics"]["stars"], 3175)
        self.assertEqual(report["metrics"]["forks"], 763)
        self.assertEqual(report["metrics"]["open_issues"], 84)
        self.assertNotEqual(report["metrics"]["stars"], 3200)
        self.assertEqual(report["maturity"], "graduated")
        self.assertEqual(report["pillars"]["security"]["score"], 9.5)
        self.assertEqual(report["pillars"]["governance"]["score"], 7.0)
        self.assertEqual(report["overallScore"], 8.1)
        self.assertEqual(report["riskLevel"], "LOW")
        self.assertTrue(all(item["dataSource"] == "fixture" for item in report["findings"]))
        self.assertIn("SECURITY.md", report["findings"][0]["message"])

    def test_fixture_slug_must_match(self):
        fixture = load_fixture()
        with self.assertRaises(ValueError):
            quaid_adapter.analyze_repo_heuristics("other/repo", fixture=fixture)

    def test_case_insensitive_slug(self):
        with mock.patch("urllib.request.urlopen", side_effect=AssertionError("network")):
            report = quaid_adapter.analyze_repo_heuristics(
                "IntersectMBO/cardano-node",
                fixture=load_fixture(),
            )
        self.assertEqual(report["repo"], "IntersectMBO/cardano-node")
        self.assertEqual(report["metrics"]["stars"], 3175)

    def test_offline_fallback_is_labeled_not_a_measurement(self):
        with mock.patch("quaid_adapter.fetch_json", return_value=None):
            report = quaid_adapter.analyze_repo_heuristics("example/example")
        self.assertEqual(report["data_source"], "offline-fallback")
        self.assertFalse(report["metrics_are_measurement"])
        self.assertEqual(report["metrics"]["stars"], 3200)
        self.assertEqual(report["metrics"]["forks"], 450)
        self.assertEqual(report["metrics"]["open_issues"], 75)
        self.assertTrue(any(item["category"] == "offline-fallback" for item in report["findings"]))

    def test_high_issue_backlog_and_missing_security(self):
        fixture = {
            "repo": {
                "full_name": "example/example",
                "stargazers_count": 10,
                "forks_count": 1,
                "open_issues_count": 201,
            },
            "files": {
                "SECURITY.md": {"present": False},
                ".github/SECURITY.md": {"present": False},
                "docs/SECURITY.md": {"present": False},
                "GOVERNANCE.md": {"present": True},
            },
        }
        with mock.patch("urllib.request.urlopen", side_effect=AssertionError("network")):
            report = quaid_adapter.analyze_repo_heuristics("example/example", fixture=fixture)
        self.assertEqual(report["maturity"], "sandbox")
        self.assertEqual(report["pillars"]["security"]["score"], 7.0)
        self.assertEqual(report["pillars"]["governance"]["score"], 9.5)
        self.assertEqual(report["pillars"]["community"]["score"], 6.0)
        self.assertTrue(any(item["category"] == "issue-backlog" for item in report["findings"]))

    def test_cli_fixture_exits_clean(self):
        proc = subprocess.run(
            [
                sys.executable,
                os.path.join(ROOT, "evaluator", "cli", "quaid_adapter.py"),
                "--fixture",
                FIXTURE,
                "intersectmbo/cardano-node",
            ],
            cwd=ROOT,
            capture_output=True,
            text=True,
            timeout=20,
            check=False,
        )
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertIn("saved fixture (no network)", proc.stdout)
        self.assertNotIn("3200", proc.stdout)


if __name__ == "__main__":
    unittest.main()
