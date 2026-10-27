# Framework glossary

Stage 0 definitions used in this repository. A definition here is not a claim that a gate has passed. Longer specifications are linked from each entry.

## dOSPO

Decentralized Open Source Program Office. The **who decides** layer: a bounded mandate, funding principles, neutrality rules, transparency standards, and operator replaceability. It does not hold the treasury. Start at [dospo/START_HERE.md](dospo/START_HERE.md).

## OMF

Open Maintenance Framework. The **how money goes out** layer: retainers, dependency audits, contributor ladders, and related programs. Start at [omf/START_HERE.md](omf/START_HERE.md).

## ORF

Open Replenishment Framework. The **how money comes back** layer: a portfolio of collection instruments, kept separate from routing rails. Start at [orf/START_HERE.md](orf/START_HERE.md).

## Hard gates

The eight conditions in [orf/GOVERNANCE_RULES.md](orf/GOVERNANCE_RULES.md) that must all hold before anyone calls an ecosystem self-sustaining. They are not a sum of points. The lab has marked none of them passed.

1. Measurement. A verified annual maintenance cost floor.
2. Cash evidence. Audited cash or stablecoin receipts, not a pledge or a projection.
3. Net coverage. Recurring non-inflationary net inflows at least equal the cost floor (portfolio coverage ratio at least 1.0).
4. Multi-class diversity. Inflows from at least two [correlation classes](#correlation-classes) that are materially uncorrelated.
5. Concentration limit. No single payer above 25% of recurring net inflows.
6. Stress runway. At least 24 months of operating liquidity under the compound stress case, and a stress coverage ratio of at least 1.0.
7. Liability coverage. Contractual obligations and retainers backed by capacity and wind-down reserves.
8. Independent audit. A public annual audit by an independent party.

## Replenishment ratios

The six ratios in [orf/GOVERNANCE_RULES.md](orf/GOVERNANCE_RULES.md). Names only:

- **IECR.** Incremental earned coverage: new commercial net income divided by the cost floor.
- **SPCR.** Structural protocol coverage: non-inflationary protocol-fee net divided by the cost floor.
- **PCR.** Portfolio coverage: recurring non-inflationary net across families, divided by the cost floor. Gate 3 uses this ratio.
- **SCR.** Stress coverage: stressed inflows divided by the austerity floor. Gate 6 uses this ratio.
- **RCR.** Revenue concentration: the largest payer's share. Gate 5 requires RCR at or below 0.25.
- **MCR.** Mechanism concentration: the largest mechanism's share. Disclosed every quarter. An MCR above 0.50 is a review trigger. It is not itself a hard gate.

## P-scale

External precedent, P0 through P5. It answers whether a mechanism already works somewhere else. The ORF paper (§14) names the ends of the scale: P0 Conceptual through P5 Cycle-Tested. The catalog also uses Operating (P2), Sustained (P3), and Scaled (P4). Names for the steps that the catalog does not print are not restated here. See [orf/INSTRUMENT_CATALOG.md](orf/INSTRUMENT_CATALOG.md). A high P-scale rating is not a local result.

## D-scale

Local deployment, D0 through D5. It answers whether **this** ecosystem has its own receipts. From [orf/START_HERE.md](orf/START_HERE.md):

| Rating | Name | Meaning |
|---|---|---|
| D0 | Hypothesis | No buyer interviews or technical specification completed |
| D1 | Buyer validated | Documented interviews or letters of intent |
| D2 | Paid pilot | Signed contracts and a first paying customer |
| D3 | Renewable | Renewals across a multi-quarter cycle |
| D4 | Scaled | A diversified customer base with positive net contribution after operating costs |
| D5 | Resilient | Multi-year history through a full market downturn |

A P4 elsewhere can still be D0 here.

## Correlation classes

The six revenue classes in [orf/GOVERNANCE_RULES.md](orf/GOVERNANCE_RULES.md). Gate 4 asks for at least two that do not move together.

1. Native network activity (protocol fees, sequencer splits).
2. Native token price (staking yield, validator pledges).
3. Enterprise contract revenue.
4. Membership and certification.
5. Capital-market return (endowment yield).
6. Philanthropic or voluntary money.

## QUAID

An external repository-health scanner. This lab ships an experimental adapter at [evaluator/cli/quaid_adapter.py](evaluator/cli/quaid_adapter.py). It is a heuristic. It is not one of the eight hard gates, and a run of it does not pass a gate.

## Net replenishment ratio

Non-inflationary income divided by baseline maintenance cost. In the fifteen-indicator scorer, indicator 11 awards 5 points at or above 1.0 and 3 points at or above 0.20. That point rule is not hard gate 3. Gate 3 is the portfolio coverage ratio in the governance rules, and it is not marked passed.

## DCO

Developer Certificate of Origin. A commit is signed off with `git commit -s`. See [CONTRIBUTING.md](CONTRIBUTING.md).

## POSM

Paid Open Source Model, a Cardano treasury program described as a precedent in [docs/precedents/CARDANO_POSM.md](docs/precedents/CARDANO_POSM.md). The Intersect POSM accelerator never launched. It was only described as intent in the scope of work.
