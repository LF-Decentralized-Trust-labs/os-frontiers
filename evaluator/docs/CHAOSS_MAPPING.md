# CHAOSS mapping

Stage 0 crosswalk between this lab's 15 indicators, the eight [hard gates](../../GLOSSARY.md#hard-gates), and published CHAOSS metrics. Checked 27 October 2026.

A row marked **Weak** means the CHAOSS page is about a nearby idea and does not decide the indicator. A row marked **No direct metric** means this lab did not find a CHAOSS metric that measures that indicator. Neither mark is a claim that the indicator has passed.

CHAOSS pages cited below:

- [Contributor Absence Factor](https://www.chaoss.community/kb/metric-contributor-absence-factor/) (the metric formerly called bus factor)
- [Organizational Diversity](https://www.chaoss.community/kb/metric-organizational-diversity/)
- [Issue Response Time](https://www.chaoss.community/kb/metric-issue-response-time/)
- [Starter Project Health](https://www.chaoss.community/kb/metrics-model-starter-project-health/)
- [Community Service and Support](https://www.chaoss.community/kb/metrics-model-community-service-and-support/)

Indicator names are the ones in [3_PIECE_ECOSYSTEM_MATURITY_ASSESSMENT.md](3_PIECE_ECOSYSTEM_MATURITY_ASSESSMENT.md).

## 15 indicators

| # | Indicator | CHAOSS | Mapping |
|---|---|---|---|
| 1 | Legitimacy | None | **No direct metric.** A charter is not a CHAOSS activity count. |
| 2 | Neutrality | Organizational Diversity | **Weak.** That metric counts organizational mix. It does not say whether funding can buy roadmap control. |
| 3 | Replaceability | Contributor Absence Factor | **Weak.** Absence factor is about how concentrated contributions are. It is not an annual vote to replace an operator. |
| 4 | Policy engine | None | **No direct metric.** |
| 5 | Transparency | Issue Response Time | **Weak.** Issue response time is not a quarterly public spending report. |
| 6 | Retainers | None | **No direct metric.** CHAOSS does not measure a retainer contract. |
| 7 | Pathways | Community Service and Support | **Weak.** That model looks at support practices. It does not record a funded contributor pathway. |
| 8 | Stewardship | None | **No direct metric.** |
| 9 | Autonomy | None | **No direct metric.** |
| 10 | Metrics | Starter Project Health | **Weak.** That model is a bundle of project-health signals. It is not an impact-metric program, and it is not OpenSSF Scorecard. |
| 11 | Replenishment ratio | None | **No direct metric.** This is a financial ratio. Indicator 11 in the assessor uses fees plus earned non-inflationary income, divided by the maintenance budget. |
| 12 | Fork resistance | None | **No direct metric.** |
| 13 | Benefit bundling | None | **No direct metric.** An SLA is not a CHAOSS metric. |
| 14 | Endowments (IPS) | None | **No direct metric.** |
| 15 | Independent audit | None | **No direct metric.** Publishing an audit is not the same as any CHAOSS activity metric. |

## Eight hard gates

The gates are defined in [orf/GOVERNANCE_RULES.md](../../orf/GOVERNANCE_RULES.md). None of them is a CHAOSS metric.

| Gate | CHAOSS | Mapping |
|---|---|---|
| 1 Measurement | None | **No direct metric.** |
| 2 Cash evidence | None | **No direct metric.** |
| 3 Net coverage | None | **No direct metric.** Portfolio coverage is an accounting ratio. |
| 4 Multi-class diversity | Organizational Diversity | **Weak.** Organizational diversity is about contributing organizations. Gate 4 is about uncorrelated revenue classes. Do not treat one as the other. |
| 5 Concentration | Contributor Absence Factor | **Weak.** A payer-share cap is not a contributor-absence factor. |
| 6 Stress runway | None | **No direct metric.** |
| 7 Liability coverage | None | **No direct metric.** |
| 8 Independent audit | None | **No direct metric.** |

## QUAID adapter

[evaluator/cli/quaid_adapter.py](../cli/quaid_adapter.py) checks whether a repository has `SECURITY.md` and `GOVERNANCE.md`, and it reads star, fork, and open-issue counts. That is not an implementation of Starter Project Health, and a score from the adapter does not pass a hard gate. Continuous integration runs it from a saved fixture and does not call the GitHub API.
