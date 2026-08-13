# OMF Program Portfolio

> These programs represent the operational portfolio that governance authorizes and the OMF operator executes. Each addresses a distinct dimension of infrastructure sustainability. Programs can be implemented independently or in combination — begin with one or two and expand as operational capacity develops.
>
> No program is a prerequisite for another. The dependency audit is the only prerequisite for everything.

---

## Program Selection Guide

Before selecting programs, answer these questions:

1. **What is your highest-risk gap?** (Use centrality + sustainability scoring from the dependency audit)
2. **What stage are your highest-risk projects at?** (Emerging / Growing / Mature / Sustaining)
3. **Do you have maintainers or do you need to grow them?** (Retainers vs Pathways emphasis)
4. **What is your governance's risk tolerance for novel program design?** (Start with the most validated models)

The typical starting point for most ecosystems is: **Maintainer Retainers** (2–5 projects) + **Contributor Pathways** (1 cohort). These two programs address the most immediate risks (maintainer burnout, pipeline gap) at manageable initial cost.

---

## The Six Programs

### 1. Maintainer Retainer

**Purpose**: Ongoing financial support tied to maintenance responsibilities — not specific deliverables.

**The problem it solves**: Grants and bounties compensate completed work. They cannot compensate availability. A maintainer who responds to a security incident at 2am on a Saturday is not delivering a discrete feature — they are fulfilling an operational responsibility that no bounty can be structured to compensate. The Maintainer Retainer is the mechanism that funds this responsibility.

**Key design requirements**:
- Role tiers: minimum two tiers (Senior Steward / Contributor), with explicitly differentiated responsibilities and authority
- 30-day evaluation period for new participants before ongoing funding is confirmed
- Quarterly review cadence (contribution activity, security practices, documentation, community engagement)
- Annual renewal review: effectiveness, relevance, succession planning
- Appeals mechanism (14-day window for negative evaluation appeals)
- Dual oversight: technical review AND governance/compliance review, structurally separated

**Primary funding instrument**: Continuity-oriented

**Reference implementations**:
- Ethereum Protocol Guild (on-chain registry, time-weighted allocation, custody-free disbursement)
- Sentry maintainer fund ($500K to 500+ maintainers; "even modest stipends bring great motivation")
- Cardano POSM (two-tier roles, 30-day evaluation, dual-committee oversight)

**Warning**: The most common failure mode is using this program for projects that have not yet established ecosystem-critical status. Use centrality scoring to enforce selection discipline. Governance priority alignment should carry the lowest weight (10%) in selection rubrics — the highest weights belong to centrality (30%) and bus factor (25%).

→ Full specification: [`maintainer-retainer.md`](maintainer-retainer.md)

---

### 2. Code Bounties

**Purpose**: Funded delivery of specific, scoped, verifiable work — features, bug fixes, security remediations, testing improvements.

**The problem it solves**: Delivery-oriented work with defined completion criteria. Complements retainers by incentivizing targeted development without requiring ongoing commitment. Effective for work that has a clear definition of done.

**Key design requirements**:
- Dual eligibility criteria: separate requirements for projects requesting work and developers fulfilling bounties
- Approval-to-payment workflow: project approval → bounty creation with acceptance criteria → developer selection → implementation → technical evaluation → 30-day post-delivery verification → payment
- Performance benchmarks: feature completeness, security compliance, code quality, test coverage, documentation
- Reapplication timeline: developers with repeated rejections wait 3 months before reapplying

**Primary funding instrument**: Delivery-oriented

**Reference implementations**: Gitcoin Grants ecosystem, GitHub Secure OSS Fund ($10K per project against defined security milestones)

**Warning**: Do not use code bounties to fund ongoing maintenance responsibilities. "Bounty hunter" is not "steward." If a project needs ongoing availability funded, use a Retainer.

→ Full specification: [`code-bounties.md`](code-bounties.md)

---

### 3. Contributor Pathways

**Purpose**: Structured mentorship and onboarding programs to grow the future maintainer pipeline.

**The problem it solves**: Retainer programs sustain existing maintainers. Without a contributor pipeline, maintainer programs eventually exhaust their pool — and no amount of retainer funding prevents an ecosystem from collapsing if no new maintainers are being cultivated.

**Key design requirements**:
- Tiered progression: minimum 4 stages (Entry Contributor → Regular Committer → Trusted Committer → Core Maintainer) with explicit criteria for each transition
- Mentorship pairing: new contributors paired with experienced maintainers for structured guidance
- Maintenance-oriented early tasks: bug triage, documentation, test coverage, dependency updates — filters for stewardship orientation and filters out speculative participants
- Staged financial incentives: minimal early compensation, tied to sustained contribution and progression
- Anti-sybil design: verified contribution history requirements, reputation-weighted progression
- On-chain contribution attestation where possible (verifiable, portable proof of contributor status)

**Primary funding instrument**: Delivery-oriented (primary) + Continuity supplement

**Reference implementation**: CNCF LFX Mentorship — 25 mentees became project maintainers since 2020. Structured pairing, stipend support, defined contribution milestones. The reference implementation for this program.

**Also reference**: Polkadot Fellowship (rank 0–9 explicit progression), Ethereum Protocol Fellowship, Cardano Contribution Ladder (4-stage framework)

**Warning**: Web3-specific contributor pathways must address unique challenges: higher technical barriers, cryptographic correctness requirements, and economic incentives that attract contributors motivated by token appreciation rather than long-term stewardship. Program structure must filter for stewardship orientation.

→ Full specification: [`contributor-pathways.md`](contributor-pathways.md)

---

### 4. Operational Support

**Purpose**: Administrative and coordination services that reduce non-code overhead for maintainers.

**The problem it solves**: Maintainer burnout is not exclusively a technical problem. Community management, security audit facilitation, legal review, documentation support, and governance assistance all consume time that maintainers cannot redirect to code. Operational Support provides shared access to these services without requiring each maintainer to source them individually.

**Services covered**:
- Security audit facilitation and coordination
- Legal review (licensing, contribution agreements)
- Documentation support and editing
- Community management assistance
- Governance process assistance
- CI/CD configuration and tooling support

**Key design requirement**: All support must reduce operational burden, not add to it. A program that requires more administrative work from maintainers than the support it provides is counterproductive. This is the most common failure mode in well-intentioned OSS support programs.

**Primary funding instrument**: Delivery-oriented (scoped service engagements)

**Reference implementation**: GitHub Secure OSS Fund cohort model (security training + tooling + mentorship combined)

→ Full specification: [`operational-support.md`](operational-support.md)

---

### 5. Incubation Program

**Purpose**: Structured support for early-stage critical projects to reach maturity without burning out founding maintainers.

**The problem it solves**: Early-stage projects that show promise as future critical infrastructure need structured support to reach maturity before they attract co-maintainers. Without this, founding maintainers burn out before the project achieves the adoption level that would justify retainer funding.

**Lifecycle position**: Emerging → Growing transition. Incubation ends when a project either graduates to Retainer-eligible status or is determined not to be on a critical infrastructure trajectory.

**Key design requirements**:
- Clear eligibility criteria: projects must show evidence of ecosystem-critical trajectory (dependency adoption curve, not just technical quality)
- Defined exit criteria: what does "graduation" look like? What triggers program exit?
- Time-bounded by design: incubation programs should have explicit maximum duration to prevent permanent incubation of projects that never reach critical status
- Milestone-based structure (not time-based retainer): funding tied to adoption and maturity milestones

**Primary funding instrument**: Delivery-oriented (primary) → Continuity transition at graduation

**Reference implementation**: Germany's Sovereign Tech Agency milestone-based contracts for emerging projects

→ Full specification: [`incubation.md`](incubation.md)

---

### 6. Resilience Programs

**Purpose**: Succession planning, bus-factor reduction, and knowledge documentation for high-centrality infrastructure.

**The problem it solves**: A project with 1,000 dependents and one maintainer who reports burnout is a portfolio emergency. Bus-factor-of-1 failures have taken down critical infrastructure in recent Web3 history (Kubernetes Ingress NGINX: no further security patches after March 2026 because its maintainers burned out). Resilience Programs address this before the crisis.

**Program components**:
- **Succession planning**: document succession paths; identify and train designated successors for top-centrality projects
- **Knowledge documentation**: capture architectural decisions, undocumented system knowledge, and operational runbooks
- **Dependency audits**: per-project dependency health assessment (distinct from the ecosystem-level audit)
- **Bus-factor reduction**: active work to bring a second or third maintainer to deep codebase knowledge
- **Continuity tooling**: shared tooling for automated dependency updates, CI/CD health monitoring

**Trigger conditions**: Any top-20 centrality project with bus factor of 1 triggers immediate Resilience Program activation. Do not wait for the maintainer to signal distress.

**Primary funding instrument**: All three instruments (Delivery for audits, Continuity for succession, Shared Infrastructure for tooling)

**Reference**: The Kubernetes NGINX case is the canonical failure-of-absence example. The Apache Software Foundation's project lifecycle and emeritus process are positive reference implementations.

→ Full specification: [`resilience.md`](resilience.md)

---

## The Full System

While each program can be implemented independently, they are most effective as a coherent system:

```
Contributor Pathways ──────────────────────────────────────────┐
  grows the future maintainer pool that feeds                   │
                                                                ▼
Maintainer Retainers ◄─────────────────────── sustained by the pipeline
  which create institutional knowledge
  preserved by
                                                                │
Resilience Programs ◄─────────────────────────────────────────┘
  reducing single-points-of-failure across the portfolio

Operational Support
  reduces burden on all funded maintainers
  making Retainer support go further

Code Bounties
  targets discrete improvements in ecosystem-critical projects
  complementing Retainers without duplicating them

Incubation
  identifies and supports the next generation of critical
  infrastructure before it becomes mission-critical without support
```

The portfolio is precisely what the infrastructure stewardship layer executes — the programs governance authorizes, OMF defines.

---

## Program Governance Requirements (All Programs)

Every OMF program, regardless of type, must have:

- A published charter defining authorized scope, budget envelope, and selection criteria
- An explicit sunset clause (no program operates indefinitely by default)
- Quarterly transparency reporting
- Annual renewal review with evidence-based continuation decisions
- Dual oversight: technical review and governance/compliance review
- A published appeals mechanism for program participants

Programs that do not meet these requirements are not OMF-compliant programs, regardless of their intentions.
