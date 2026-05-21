# Contributing to Open Source Frontiers Lab

Thank you for your interest in contributing to the Open Source Frontiers Lab
(OSFL). This repository is an applied research and incubation environment within
[LF Decentralized Trust](https://lfdecentralizedtrust.org), and the work here
directly shapes how open source projects across decentralized ecosystems are
funded, governed, and maintained.

Contributions are what keep this work grounded in reality. Whether you are
a foundation steward, a protocol contributor, an independent researcher, or a
practitioner who has learned hard lessons about open source sustainability, your
perspective belongs here.

---

## Table of Contents

- [What We Work On](#what-we-work-on)
- [Ways to Contribute](#ways-to-contribute)
- [Before You Start](#before-you-start)
- [Contribution Workflow](#contribution-workflow)
- [Content Standards](#content-standards)
- [Folder Structure](#folder-structure)
- [Review Process](#review-process)
- [Discussions and Community](#discussions-and-community)
- [Code of Conduct](#code-of-conduct)
- [License](#license)

---

## What We Work On

OSFL produces reference material — not software — across five areas:

| Focus Area | Examples |
|---|---|
| **Open source sustainability and maintenance models** | Funding frameworks, maintainer health patterns, burnout prevention models |
| **Decentralized coordination structures and governance design** | DAO governance templates, committee charters, voting mechanism analysis |
| **Contributor incentives, funding flows, and resource allocation** | Incentive design patterns, treasury routing models, grant evaluation rubrics |
| **Lifecycle management of open source projects** | Incubation checklists, maturity criteria, deprecation and archival guidance |
| **Cross-ecosystem interoperability of governance and sustainability practices** | Comparative analyses, portability frameworks, ecosystem mapping |

Artifacts live in the following directories:

```
/OS Program Architectures   — structural models and reference designs
/best practices             — operational guidance and checklists
/tools                      — tool evaluations and submission templates
/use-cases                  — real-world case studies and applied examples
/whitepapers                — long-form research and position papers
```

---

## Ways to Contribute

### Report an Issue

Found something wrong — a factual error, a broken link, outdated guidance, or
missing context for an important ecosystem? Open a
[GitHub Issue](https://github.com/LF-Decentralized-Trust-labs/os-frontiers/issues)
describing the problem and where it appears.

Good issue titles are specific:
- ✅ `Governance template in /best practices missing quorum definition guidance`
- ❌ `Something looks wrong`

### Improve Existing Content

Corrections, clarifications, expanded examples, updated references, and
improved structure are all welcome via pull request. You do not need to file
an issue first for small, clearly scoped improvements.

### Contribute a New Artifact

New frameworks, whitepapers, use cases, tool evaluations, or reference
architectures can be proposed via an issue before you invest significant
effort writing them. This lets maintainers signal whether the topic fits
the lab's current focus and avoids duplication with work in progress.

For tool submissions, use the template in `/tools`.

### Share a Use Case

Practitioners with direct experience deploying governance models, funding
structures, or sustainability programs in real ecosystems are especially
valuable contributors. Use cases ground abstract frameworks in evidence.
See `/use-cases` for format examples.

### Review Open Pull Requests

Reviewing others' contributions is one of the most impactful ways to help.
Constructive, specific feedback on accuracy, completeness, and practical
applicability is always appreciated.

### Participate in Discussions

The
[Discussions tab](https://github.com/LF-Decentralized-Trust-labs/os-frontiers/discussions)
is the right place for open-ended questions, emerging topic proposals,
and ecosystem observations that are not yet ready to become pull requests.

---

## Before You Start

### Sign the Developer Certificate of Origin (DCO)

All contributions to LFDT projects must include a DCO sign-off. This certifies
that you wrote or have the right to submit the contribution under the project's
open source license (Apache 2.0).

Add the following to each commit message:

```
Signed-off-by: Your Name <your.email@example.com>
```

You can configure Git to add this automatically:

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
git commit -s
```

Commits without a DCO sign-off will not be merged.

### Check for Existing Work

Before starting a significant new artifact, search open Issues, open PRs, and
the Discussions tab to ensure you are not duplicating work already in progress.
If in doubt, open a Discussion to check.

### Understand the Neutrality Principle

OSFL is explicitly neutral — not tied to any specific protocol, network, or
commercial product. Contributions must reflect this. Guidance should be
broadly applicable across ecosystems, and where ecosystem-specific examples
are used, they should be clearly labeled as illustrative rather than
prescriptive.

---

## Contribution Workflow

1. **Fork** the repository and create a branch from `main`.
   Use a descriptive branch name:
   - `add-treasury-coordination-framework`
   - `fix-governance-template-quorum-section`
   - `use-case-filecoin-maintenance-funding`

2. **Make your changes** following the [Content Standards](#content-standards)
   below.

3. **Commit** with a clear message and DCO sign-off:
   ```
   Add contributor incentive design patterns to best practices

   Signed-off-by: Your Name <your@email.com>
   ```

4. **Open a pull request** against `main`. Fill in the PR template:
   - What does this add or change?
   - Which focus area does it address?
   - Are there related Issues or Discussions?
   - Does it introduce any ecosystem-specific assumptions?

5. **Respond to review feedback.** Maintainers aim to provide initial review
   within 10 business days. Substantive changes require at least one
   maintainer approval before merge.

6. Once approved, a maintainer will **merge** your PR. You retain attribution
   in the commit history.

---

## Content Standards

### Accuracy and Evidence

- Claims should be grounded in evidence: cite sources, reference real ecosystems,
  and note where guidance is based on emerging practice rather than established
  precedent.
- Where you are aware of conflicting approaches or unresolved debates, represent
  that tension honestly rather than flattening it.

### Neutrality

- Do not advocate for a specific protocol, chain, vendor, or commercial product
  as the definitive answer to any problem.
- Ecosystem-specific examples are welcome as illustrations; they should not
  imply that the reader must use that ecosystem to apply the guidance.

### Format and Structure

- Use Markdown. Follow the existing structure of the directory your artifact
  belongs to.
- Use clear, descriptive headings. Avoid jargon where plain language works;
  define jargon where it is necessary.
- Use tables for comparisons, checklists for process steps, and prose for
  rationale and context. Avoid over-formatting simple content.
- File names should be lowercase with hyphens: `governance-design-patterns.md`,
  not `Governance Design Patterns.md`.

### Links and References

- Link to stable, authoritative sources. Avoid shortened URLs.
- If you reference a tool or project, link to its primary repository or
  documentation rather than a secondary summary.
- External links should be verified at time of submission. Flag links you
  believe may be unstable in your PR description.

### PII and Sensitive Information

- Do not include personally identifiable information (names, emails, wallet
  addresses) in committed content without explicit consent from those individuals.
- If a use case involves real organizations or individuals, get confirmation
  that they are comfortable being cited, or anonymize appropriately.

---

## Folder Structure

When deciding where a contribution belongs:

| If your contribution is... | It belongs in... |
|---|---|
| A structural model, reference design, or program architecture | `/OS Program Architectures` |
| Operational guidance, a checklist, or a how-to | `/best practices` |
| An evaluation of a specific tool or a tool submission | `/tools` |
| A real-world example of a sustainability or governance approach | `/use-cases` |
| A long-form research paper or position paper | `/whitepapers` |

If you are unsure, open a Discussion before investing significant writing effort.

---

## Review Process

All pull requests are reviewed by OSFL maintainers. The review evaluates:

- **Accuracy** — Is the content factually correct and internally consistent?
- **Neutrality** — Does it avoid advocating for specific ecosystems or products?
- **Scope** — Does it fit within OSFL's focus areas?
- **Quality** — Is it clearly written, well-structured, and properly sourced?
- **DCO** — Is every commit signed?

Maintainers may request changes, ask clarifying questions, or (rarely) decline
a contribution that falls outside scope. Feedback will always explain the
reasoning. If you disagree with a review decision, open a Discussion to
continue the conversation — we are committed to transparent, good-faith
editorial dialogue.

---

## Discussions and Community

The [Discussions tab](https://github.com/LF-Decentralized-Trust-labs/os-frontiers/discussions)
is the right home for:

- Emerging topic proposals that are not yet ready for a PR
- Questions about how to apply OSFL frameworks in a specific context
- Observations from the field that might seed future work
- Feedback on published artifacts that goes beyond a simple correction

For real-time conversation, OSFL participates in the broader LF Decentralized
Trust community. Information about community calls and async channels is
available on the [LFDT website](https://lfdecentralizedtrust.org).

---

## Code of Conduct

All contributors are expected to abide by the
[Contributor Covenant Code of Conduct](./CODE_OF_CONDUCT.md). This community
is committed to being open, welcoming, and harassment-free for everyone.

Reports of conduct violations may be made to the community leaders listed in
the Code of Conduct.

---

## License

By contributing to this repository, you agree that your contributions will be
licensed under the [Apache License 2.0](./LICENSE) that covers the project.

---

*This document is itself a living artifact. If you find it unclear, incomplete,
or out of date, please open a PR to improve it.*
