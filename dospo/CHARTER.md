# dOSPO Charter Template

> **Instructions**: Replace all `[BRACKETED]` fields with your ecosystem's specifics. The structural constraints in this document — policy-execution separation, time-bounded mandate, replaceability, transparency requirements — should not be removed. They are enforcement mechanisms, not cultural preferences.

---

## Charter for the [ECOSYSTEM NAME] Decentralized Open Source Program Office

**Version**: 1.0  
**Effective Date**: [DATE]  
**Mandate Expiry**: [DATE + 2–4 YEARS]  
**Issuing Authority**: [COMMUNITY GOVERNANCE BODY — e.g., DAO, Constitutional Committee]  
**Operator**: [ENTITY OR ROLE NAME]

---

## 1. Purpose and Scope

This charter establishes a time-bounded, community-mandated coordination function — the **[ECOSYSTEM] dOSPO** — to steward open source infrastructure within the [ECOSYSTEM NAME] ecosystem.

The dOSPO provides bounded execution capacity for coordination functions that the ecosystem cannot reliably perform through ad hoc alignment, including:

- Security incident coordination
- Lifecycle-aligned funding oversight
- Dependency risk management
- Cross-project alignment

This charter does **not** grant the operator authority to set ecosystem direction, own projects, control roadmaps, or persist beyond its mandate period.

---

## 2. Policy Domains and Governing Bodies

The operator executes within the frameworks defined by three community-mandated policy bodies:

| Domain | Governing Body | Primary Responsibility |
|---|---|---|
| Open Source | [Stewardship Committee / OS Council] | Lifecycle criteria, funding eligibility, contribution standards |
| Technical | [Technical Steering Group / Technical Council] | Cross-project standards, dependency management, architectural alignment |
| Security | [Security Council / Security Advisory Board] | Disclosure policy, severity taxonomy, incident coordination authority |

Policy bodies define frameworks. The operator does not define them.

---

## 3. Operator Authority and Constraints

### Granted Authority

The operator is authorized to:

- Maintain a single intake surface for ecosystem-wide proposals and issues
- Administer funding programs **as approved by governance** — not at operator discretion
- Facilitate cross-entity alignment where project dependencies overlap
- Organize security incident response within the Security Domain policy
- Produce and publish transparency reports on the schedule defined in Section 6
- Act with pre-authorized urgency during security incidents, under conditions defined by the Security Council

### Non-Powers (Hard Limits)

The operator is **explicitly prohibited** from:

- Setting ecosystem roadmaps unilaterally
- Allocating funds outside governance-approved programs
- Owning or conditioning support on intellectual property or repository control
- Replacing project maintainers absent a published governance process
- Operating any program without a sunset clause
- Expanding emergency security authority beyond the bounds set by the Security Council
- Persisting any function beyond this charter's expiry without community re-authorization

Violation of any non-power is grounds for immediate mandate review and potential early dissolution.

---

## 4. Mandate Period and Renewal

### Duration

This charter is valid for **[2–4 YEARS]** from the effective date.

The operator does not persist by default at expiry. Continuation requires affirmative community re-authorization.

### Renewal Process

At least **[90–120 days]** before mandate expiry, the operator must submit a **Renewal Proposal** to the issuing governance authority, including:

- Outcomes achieved against mandate criteria (see Section 6)
- Proposed scope for the next mandate period (may be narrower or broader)
- Updated budget request
- Any proposed changes to authority or non-powers list
- Assessment of whether the dOSPO remains justified given current ecosystem conditions

The community may:

- **Renew** with the same or modified scope
- **Narrow** the mandate without full renewal
- **Dissolve** the dOSPO if coordination cost now exceeds failure cost

### Early Dissolution

The issuing governance authority may dissolve this charter early if:

- The operator violates any non-power
- The operator becomes institutionally indispensable (ecosystem cannot function without it)
- Renewal fatigue allows continuation through inertia rather than re-justification
- A supermajority of the governance body votes for dissolution

---

## 5. Enforcement Mechanisms

Renewal is the primary accountability mechanism but is insufficient alone. Additional structural constraints apply:

**Automatic scope decay**: If no renewal action is taken 30 days before expiry, the operator's authority automatically narrows to security coordination only, pending full renewal deliberation.

**Budget cliffs**: Funding is allocated in discrete periods with hard expiration. Absent renewal, budgets do not roll over.

**Program sunset clauses**: Every program operated by the dOSPO must carry an explicit sunset date. Continuation requires evidence-based renewal, not advocacy.

**Mandatory re-chartering**: Every renewal cycle requires scope redefinition. Renewal by identical copy of a prior charter is not permitted.

---

## 6. Transparency Requirements

The operator must publish the following artifacts on a regular schedule:

| Artifact | Frequency | Audience |
|---|---|---|
| Intake backlog and triage rationale | Monthly | Public |
| Funding allocation report | Quarterly | Public |
| Outcome report (vs. mandate criteria) | Quarterly | Governance + Public |
| Incident timeline and post-mortem | Within 30 days of incident | Public |
| Renewal proposal | ≥90 days before expiry | Governance + Public |

All artifacts must be published to [DESIGNATED PUBLIC LOCATION — e.g., GitHub, governance forum].

Failure to publish required artifacts on schedule is a mandate violation.

---

## 7. Replaceability

The operator is replaceable without disrupting project ownership or governance continuity.

Projects in the ecosystem retain:

- Full ownership of their repositories and intellectual property
- The right to fork without institutional penalty
- The right to exit coordination programs at any time

If the operator is replaced, incoming operators must be able to resume all functions within **[30–60 days]** using published artifacts alone. Institutional knowledge must not be required for continuity.

---

## 8. Amendments

This charter may be amended by the issuing governance authority through [GOVERNANCE PROCESS — e.g., on-chain vote, supermajority committee vote].

Proposed amendments must be published for community comment for at least **[14–30 days]** before ratification.

The operator may not propose amendments that expand its own authority or extend its mandate period.

---

## 9. Signatures / Ratification

This charter is ratified by:

| Role | Name / Entity | Date |
|---|---|---|
| Issuing Governance Authority | [NAME] | [DATE] |
| Open Source Domain Body | [NAME] | [DATE] |
| Technical Domain Body | [NAME] | [DATE] |
| Security Domain Body | [NAME] | [DATE] |
| Operator | [NAME] | [DATE] |

---

*The defining test: if this dOSPO becomes institutionally indispensable — if the ecosystem cannot function without it — it has violated its design constraints and should be restructured or dismantled.*
