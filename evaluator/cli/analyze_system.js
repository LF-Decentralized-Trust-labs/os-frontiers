#!/usr/bin/env node
"use strict";

/**
 * JavaScript port of assess_ecosystem.analyze_system_data and evaluate_hard_gates.
 * The command-line entry remains index.js, which calls the Python assessor.
 * This file reads one JSON config on stdin and writes the result JSON to stdout.
 * It exists so tests can check the two implementations against the same inputs.
 */

const GATE_NAMES = [
  [1, "Measurement"],
  [2, "Cash Evidence"],
  [3, "Net Coverage"],
  [4, "Multi-Class Diversity"],
  [5, "Concentration"],
  [6, "Stress Runway"],
  [7, "Liability Coverage"],
  [8, "Independent Audit"],
];

function pythonRound(value, ndigits) {
  if (!Number.isFinite(value)) return value;
  const factor = 10 ** ndigits;
  const shifted = value * factor;
  const sign = shifted < 0 ? -1 : 1;
  const abs = Math.abs(shifted);
  const base = Math.floor(abs);
  const diff = abs - base;
  let whole;
  if (diff > 0.5) whole = base + 1;
  else if (diff < 0.5) whole = base;
  else whole = base % 2 === 0 ? base : base + 1;
  const out = (sign * whole) / factor;
  return Object.is(out, -0) ? 0 : out;
}

function scoreIndicator(val) {
  if (typeof val === "boolean") return val ? 5 : 0;
  if (typeof val === "number" && !Number.isNaN(val)) {
    if (val >= 5) return 5;
    if (val >= 3) return 3;
    return 0;
  }
  return 0;
}

function asNumber(value) {
  if (typeof value === "boolean") return null;
  if (typeof value === "number" && !Number.isNaN(value)) return value;
  return null;
}

function money(config, key) {
  const number = asNumber(config[key]);
  return number === null ? 0 : number;
}

function uniqueClasses(value) {
  if (!Array.isArray(value)) return [];
  const seen = [];
  for (const item of value) {
    if (typeof item !== "string") continue;
    const name = item.trim();
    if (name && !seen.includes(name)) seen.push(name);
  }
  return seen;
}

function evaluateHardGates(config) {
  const raw = Object.prototype.hasOwnProperty.call(config, "hard_gates")
    ? config.hard_gates
    : null;
  const provided = raw !== null && typeof raw === "object" && !Array.isArray(raw);
  const gates = provided ? raw : {};
  const budget = asNumber(config.annual_maintenance_budget_usd);
  let portfolio = null;
  if (budget !== null && budget > 0) {
    portfolio =
      (money(config, "annual_tx_fee_inflow_usd") +
        money(config, "annual_earned_non_inflation_usd") +
        money(config, "annual_yield_net_usd") +
        money(config, "annual_pledges_net_usd")) /
      budget;
  }

  const flagged = (key) => gates[key] === true;
  const classes = uniqueClasses(gates.revenue_classes);
  const share = Object.prototype.hasOwnProperty.call(gates, "largest_payer_share")
    ? asNumber(gates.largest_payer_share)
    : null;
  const stressRatio = Object.prototype.hasOwnProperty.call(gates, "stress_coverage_ratio")
    ? asNumber(gates.stress_coverage_ratio)
    : null;
  const runwayMonths = Object.prototype.hasOwnProperty.call(gates, "stressed_runway_months")
    ? asNumber(gates.stressed_runway_months)
    : null;

  const met = {
    1: provided && flagged("measurement_verified") && budget !== null && budget > 0,
    2: provided && flagged("cash_evidence_audited"),
    3: provided && portfolio !== null && portfolio >= 1.0,
    4: provided && classes.length >= 2,
    5: provided && share !== null && share >= 0 && share <= 0.25,
    6:
      provided &&
      stressRatio !== null &&
      runwayMonths !== null &&
      stressRatio >= 1.0 &&
      runwayMonths >= 24,
    7: provided && flagged("liabilities_covered"),
    8: provided && flagged("independent_audit_published"),
  };

  const listed = GATE_NAMES.map(([id, name]) => ({ id, name, met: met[id] }));
  return {
    evidence_provided: provided,
    portfolio_coverage_ratio: portfolio === null ? null : pythonRound(portfolio, 4),
    gates: listed,
    all_met: listed.every((item) => item.met),
  };
}

function getOr(config, key, fallback) {
  if (!Object.prototype.hasOwnProperty.call(config, key) || config[key] === undefined) {
    return fallback;
  }
  return config[key];
}

function analyzeSystemData(config) {
  const budget = getOr(config, "annual_maintenance_budget_usd", 0);
  const fees = getOr(config, "annual_tx_fee_inflow_usd", 0);
  const earned = getOr(config, "annual_earned_non_inflation_usd", 0);
  const reserves = getOr(config, "treasury_reserve_usd", 0);
  const net = fees + earned;
  const rawRatio = budget > 0 ? net / budget : 0;
  const netReplenishmentRatio = pythonRound(rawRatio, 4);
  const runwayYears = budget > 0 ? pythonRound((reserves * 0.5) / budget, 1) : 0;

  const dospo = [
    "indicator_1_legitimacy_charter",
    "indicator_2_neutrality_guarantee",
    "indicator_3_operator_replaceable",
    "indicator_4_policy_engine",
    "indicator_5_transparency_reporting",
  ].reduce((sum, key) => sum + scoreIndicator(config[key]), 0);

  const omf = [
    "indicator_6_maintainer_retainers",
    "indicator_7_contributor_pathways",
    "indicator_8_tooling_stewardship",
    "indicator_9_autonomy_safeguard",
    "indicator_10_impact_metrics",
  ].reduce((sum, key) => sum + scoreIndicator(config[key]), 0);

  let ind11 = 0;
  if (rawRatio >= 1.0) ind11 = 5;
  else if (rawRatio >= 0.2) ind11 = 3;

  const orf =
    ind11 +
    [
      "indicator_12_fork_resistance",
      "indicator_13_benefit_bundling_slas",
      "indicator_14_ips_endowments",
      "indicator_15_independent_audit",
    ].reduce((sum, key) => sum + scoreIndicator(config[key]), 0);

  const total = Math.min(75, dospo + omf + orf);
  const overallPct = pythonRound((total / 75) * 100, 1);
  const level3 = rawRatio >= 1.0;
  let level;
  if (total >= 65 && level3) level = "Level 3: Self-Sustaining Closed Loop";
  else if (total >= 50) level = "Level 2: Fee-Supplemented Maintenance";
  else if (total >= 25) level = "Level 1: Governance & Retainers Bootstrapped";
  else level = "Level 0: Un-Architected / Fragile";

  return {
    config_source: Object.prototype.hasOwnProperty.call(config, "name") && config.name !== undefined
      ? config.name
      : "Custom Input",
    dospo_score: dospo,
    omf_score: omf,
    orf_score: orf,
    total_score: total,
    overall_pct: overallPct,
    level,
    level_3_gate_passed: level3,
    metrics: {
      annual_maintenance_budget_usd: budget,
      net_replenishment_ratio: netReplenishmentRatio,
      bear_market_runway_years: runwayYears,
    },
    hard_gates: evaluateHardGates(config),
  };
}

async function readStdin() {
  const chunks = [];
  for await (const chunk of process.stdin) chunks.push(chunk);
  return Buffer.concat(chunks).toString("utf8");
}

if (require.main === module) {
  readStdin()
    .then((text) => {
      if (!text.trim()) {
        console.error("Pass one JSON object on stdin.");
        process.exit(2);
      }
      const config = JSON.parse(text);
      process.stdout.write(JSON.stringify(analyzeSystemData(config)));
    })
    .catch((err) => {
      console.error(err.message);
      process.exit(1);
    });
}

module.exports = { analyzeSystemData, evaluateHardGates, scoreIndicator };
