# Security Incident Response Playbook

> **Purpose**: Ensure that when a vulnerability spans multiple ecosystem components, response is coordinated, fast, and does not create permanent authority expansion.
>
> **Key principle**: Emergency authority expands only under defined conditions and contracts immediately afterward. Security incidents must not justify standing powers.

---

## Roles

| Role | Responsibility | Filled By |
|---|---|---|
| **Incident Coordinator** | Single point of coordination during active incident | dOSPO Operator (pre-authorized) |
| **Severity Assessor** | Initial triage using shared taxonomy | Security Council member (rotating) |
| **Project Leads** | Patch development, deployment coordination | Affected project maintainers |
| **Communications Lead** | Operator/downstream user notification | dOSPO Operator |
| **Post-Incident Reviewer** | Retrospective and documentation | Security Council |

---

## Phase 1: Intake (0–4 hours)

- [ ] Report received via designated disclosure channel (see [`disclosure-policy.md`](disclosure-policy.md))
- [ ] Severity Assessor assigned within **2 hours** of receipt
- [ ] Initial severity classification applied using shared taxonomy (see [`severity-taxonomy.md`](severity-taxonomy.md))
- [ ] Incident Coordinator notified and activated
- [ ] Embargo period begins — no public disclosure until Phase 3

**Intake channels must be monitored continuously. No report should go unacknowledged for more than 4 hours.**

---

## Phase 2: Coordinated Response (4–72 hours, severity-dependent)

- [ ] Affected projects identified and leads contacted via private channel
- [ ] Cross-project impact scope assessed
- [ ] Patch development coordinated across teams
- [ ] Deployment timeline agreed and documented
- [ ] Downstream operator and user notification sequence drafted (not yet sent)
- [ ] Security Council briefed on status at defined intervals

**The Incident Coordinator facilitates. Project leads retain authority over their own codebases. The coordinator cannot mandate patch timelines — only facilitate agreement.**

---

## Phase 3: Coordinated Disclosure

- [ ] Patches deployed (or deployment confirmed imminent) by all affected projects
- [ ] Operator and downstream user notification sent per agreed sequence
- [ ] Public advisory published via [DESIGNATED CHANNEL]
- [ ] Embargo lifted

**Disclosure timing is set by the Security Council's embargo policy, not by the operator. The operator executes the agreed timeline.**

---

## Phase 4: Post-Incident (within 30 days)

- [ ] Incident timeline documented using [`../templates/incident-timeline-template.md`](../templates/incident-timeline-template.md)
- [ ] Post-mortem completed with affected project leads
- [ ] Root cause analysis documented
- [ ] Process gaps identified and remediation proposed to Security Council
- [ ] Expanded emergency authority formally closed — no lingering permissions
- [ ] Post-mortem published publicly

**Authority contraction is mandatory, not optional. Any emergency authority granted during the incident must be explicitly closed at this stage.**

---

## Escalation Paths

| Condition | Escalation |
|---|---|
| Project lead unresponsive after 24 hours | Security Council notified; Security Council may escalate to governance |
| Exploit active in the wild | Security Council may authorize accelerated disclosure timeline |
| Incident spans ecosystem-external dependencies | Security Council coordinates with external project security contacts |
| Operator conflict of interest identified | Security Council appoints independent coordinator |

---

## What the dOSPO Cannot Do in a Security Incident

- Cannot compel a maintainer to patch or merge code
- Cannot compel an operator to upgrade infrastructure
- Cannot retain expanded authority after the incident is closed
- Cannot make public disclosures outside Security Council-approved timelines
- Cannot use the incident to justify any standing power not already defined in the Security Domain charter

---

*The dOSPO reduces chaos, not malice. Enforcement occurs through incentives — eligibility for continuity funding, lifecycle designation, participation in coordinated response — not through command authority.*
