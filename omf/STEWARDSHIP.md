# Portfolio Stewardship

> Funding an individual project is an allocation decision. Funding an ecosystem's infrastructure is a portfolio discipline.
>
> OMF introduces portfolio-level thinking as a core operational function — the systematic management of funded programs as an interconnected portfolio of ecosystem dependencies, not a collection of independent grants.

---

## The Foundational Distinction

**Grant programs** fund the applications they receive. Selection is reactive: whoever submits a compelling proposal gets funded.

**Portfolio stewardship** actively maps ecosystem dependencies, identifies coverage gaps, and allocates funding toward the infrastructure that poses the highest systemic risk if it fails — whether or not that infrastructure has an articulate advocate writing proposals.

A critical library with no advocate receives funding because the centrality score demands it. A well-advocated project with low centrality receives less because the portfolio cannot justify the opportunity cost.

This is what separates OMF from all prior OSS funding initiatives.

---

## Portfolio Stewardship Functions

### Dependency Mapping
Systematic identification of all infrastructure the ecosystem depends on — direct dependencies, transitive dependencies, and foundational libraries. Reveals the actual dependency graph rather than relying on projects that self-identify as critical.

**Output**: A complete dependency map published publicly and updated at least annually.

### Centrality Scoring
Assessment of how many ecosystem components depend on each infrastructure piece. High-centrality dependencies represent concentrated systemic risk — a single failure point for many dependent projects.

**Primary risk metric**: `Dependency Centrality = count of ecosystem projects depending on this component`

High-centrality, low-sustainability infrastructure is the highest-priority sustainment target. A project with 1,000 dependents and one burned-out maintainer is a portfolio emergency. A project with 10 dependents and three healthy maintainers is not.

### Risk-Priority Scoring Formula

```
Priority Score = (Dependency Centrality × 0.30)
              + (Inverse Bus Factor × 0.25)
              + (Maintainer Burnout Risk × 0.25)
              + (Security Incident History × 0.20)
```

| Factor | Weight | Scoring |
|---|---|---|
| Dependency Centrality | 30% | Normalized 0–100; library depended on by 80% of ecosystem scores near 100 |
| Inverse Bus Factor | 25% | Bus factor of 1 = 100; bus factor of 2 = 50; bus factor of 5 = 20 |
| Maintainer Burnout Risk | 25% | Composite of self-reported availability, contribution trend, time-in-role, CHAOSS indicators |
| Security Incident History | 20% | Frequency and severity weighted by recency; unresolved critical vulnerabilities = 100 |

**These weights are defaults.** Ecosystems calibrate to their specific risk tolerances and publish the calibrated weights before each allocation cycle.

### Coverage Gap Analysis
Comparison of the dependency map against current OMF program coverage. Identifies critical infrastructure with no program support — the highest-risk gap in the ecosystem's sustainability posture.

**Output**: A gap matrix showing funded vs. unfunded dependencies, ranked by risk-priority score.

### Portfolio Rebalancing
Periodic review of the funded portfolio against updated dependency maps. The funding portfolio evolves with the dependency reality, not with historical momentum or legacy commitments.

### Sunset Discipline
Explicit criteria for program termination or renewal. Time-bounded commitments prevent legacy programs from crowding out emerging critical infrastructure. Every renewal is an active portfolio decision, not a default continuation.

### Opportunity Cost Accounting
Every funding commitment displaces alternatives. Portfolio stewardship makes opportunity cost explicit — governance can see not just what is funded, but what is not funded and why. This prevents the invisible accumulation of technical sustainability debt.

---

## The OMF Operating Cycle

Portfolio stewardship is not a one-time exercise — it is a recurring governance cycle. The six-phase cycle runs continuously, with each phase feeding into the next.

```
         ┌──────────────────────────────────────────┐
         │                                          │
         ▼                                          │
┌─────────────────┐                                 │
│  01             │                                 │
│  DEPENDENCY     │  Systematic mapping of all      │
│  MAPPING        │  ecosystem dependencies.        │
│                 │  Generate/update SBOMs.         │
└────────┬────────┘  Score centrality.              │
         │                                          │
         ▼                                          │
┌─────────────────┐                                 │
│  02             │                                 │
│  RISK           │  Apply risk-priority scoring.   │
│  ANALYSIS       │  Identify coverage gaps.        │
│                 │  Flag portfolio emergencies.    │
└────────┬────────┘                                 │
         │                                          │
         ▼                                          │
┌─────────────────┐                                 │
│  03             │  Match instruments to programs. │
│  PROGRAM        │  Authorize new programs.        │
│  ALLOCATION     │  Sunset ineffective programs.   │
│                 │  Set budget envelopes.          │
└────────┬────────┘                                 │
         │                                          │
         ▼                                          │
┌─────────────────┐                                 │
│  04             │  Execute retainers, bounties,   │
│  MAINTAINER     │  pathways, resilience.          │
│  SUPPORT        │  Report on program activity.    │
│                 │  Facilitate cross-project work. │
└────────┬────────┘                                 │
         │                                          │
         ▼                                          │
┌─────────────────┐                                 │
│  05             │  Track CHAOSS health metrics.   │
│  HEALTH         │  Monitor centrality changes.    │
│  METRICS        │  Publish quarterly reports.     │
│                 │  Flag governance triggers.      │
└────────┬────────┘                                 │
         │                                          │
         ▼                                          │
┌─────────────────┐                                 │
│  06             │  Evidence-based renewal.        │
│  GOVERNANCE     │  Portfolio rebalancing.         │
│  REVIEW         │  Scope reconfirmation.          │
│                 │  Feeds back to Phase 01 ────────┘
└─────────────────┘
```

The cycle has no natural termination point — it runs as long as the ecosystem depends on open source infrastructure. Each governance review produces an updated portfolio allocation that feeds directly into the next dependency mapping cycle, closing the loop between evidence and action.

---

## Governance Decision Rules

Metrics without decision rules are reports, not governance tools. Each baseline target must trigger a specific governance action:

| Trigger | Condition | Action |
|---|---|---|
| **Automatic renewal** | All KPI thresholds met for 2 consecutive quarters | Renewal proceeds to governance for simple ratification; no full re-evaluation required |
| **Review** | Any baseline target missed for 1 quarter | Operator initiates formal review; improvement targets set; funding continues during review |
| **Escalation** | Critical target missed 1 quarter OR non-critical missed 2 consecutive quarters | Governance body directly involved; funding may be modified or suspended |
| **Portfolio rebalancing** | Centrality increases >50% between annual audits | Immediate coverage gap assessment regardless of current funding status |
| **Emergency** | Top-20 project: bus factor = 1 AND maintainer signals departure intent | Immediate Resilience Program activation; succession and pathway acceleration |

---

## Key Health Indicators

| Indicator | Target | Source |
|---|---|---|
| Maintainer attrition rate | < 15% annually across funded projects | CHAOSS + Tidelift surveys |
| Security vulnerability response | Median < 30 days; CVSS 9.0+ < 7 days | Per-project tracking |
| Bus factor (top-20 projects) | ≥ 2 for all top-20 centrality projects | Contributor data + interviews |
| Contributor-to-maintainer conversion | > 5% per pathway cohort within 18 months | Pathway tracking |
| Dependency freshness (Libyears) | Below ecosystem-defined threshold | Augur / CHAOSS tooling |
| Release frequency | ≥ 1 release/quarter for all funded projects | Repository activity |

**These targets are starting recommendations, not absolutes.** They are governance discussion triggers — calibrate them to your ecosystem's specific context during the first dependency audit.

---

## SBOM as the Data Foundation

Accurate centrality scoring depends on complete, machine-readable dependency data. OMF treats Software Bills of Materials (SBOMs) in SPDX or CycloneDX format as the essential data substrate for portfolio stewardship.

SBOMs make dependency graphs:
- **Auditable** — any stakeholder can verify the dependency map
- **Repeatable** — the same tooling produces the same results
- **Portable** — data is shareable across ecosystems using cross-chain interoperability standards

Without SBOMs, centrality scoring is only as reliable as the manual inventory it draws from. Manual inventories degrade over time and miss transitive dependencies — the most dangerous category.

→ See [`appendices/sbom-standards.md`](../appendices/sbom-standards.md) for implementation guidance.

---

*Portfolio stewardship is what separates OMF from all prior funding initiatives. STA funds what its expert committee recommends. GitHub funds a security cohort. Protocol Guild funds Ethereum protocol contributors. OMF funds what the ecosystem's dependency graph says is at risk — systematically, transparently, and with governance authority over every decision.*
