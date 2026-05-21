# Security Policy

## Overview

The Open Source Frontiers Lab (OSFL) is an applied research and incubation
environment within [LF Decentralized Trust](https://lfdecentralizedtrust.org).
This repository contains guidance frameworks, reference architectures,
whitepapers, and implementation artifacts related to open source sustainability
in Web3 and decentralized ecosystems.

Although this repository does not ship executable software or run production
infrastructure, it does carry real security surface: the frameworks, templates,
and best-practice guidance produced here are adopted by downstream LFDT projects
and external ecosystems. Errors of fact, malicious content injected via
contribution, or compromised published artifacts can harm the communities that
depend on this work. We treat the integrity of this content with the same care
we would treat code.

---

## Scope

| In Scope | Out of Scope |
|---|---|
| Content integrity — incorrect, misleading, or maliciously altered guidance documents | Vulnerabilities in GitHub's own platform infrastructure |
| Injection of harmful or compromised links, scripts, or references into published artifacts | Third-party tools listed in `/tools` (report those to their respective maintainers) |
| Unauthorized changes to governance or policy documents | General content disagreements or editorial disputes (use Issues or Discussions) |
| Exposure of personally identifiable information (PII) in contributed content | |
| Supply chain concerns with referenced templates or tooling schemas | |
| Social engineering or impersonation targeting OSFL contributors or maintainers | |

> **Note:** If you discover a security issue in an LFDT project that _uses_ OSFL
> frameworks as a dependency, please report it to that project's security contact
> first. If the root cause traces back to guidance published in this repository,
> also report it here.

---

## Reporting a Vulnerability

We ask that you follow responsible disclosure: please **do not open a public
GitHub Issue** for security concerns. Public disclosure before a fix is in place
can put adopters of OSFL artifacts at risk.

### Preferred Channel

Report security concerns privately via GitHub's built-in mechanism:

**[Report a vulnerability →](https://github.com/LF-Decentralized-Trust-labs/os-frontiers/security/advisories/new)**

This opens a private advisory draft visible only to repository maintainers. It
is the fastest path to a coordinated response.

### Alternate Contact

If you are unable to use the GitHub advisory form, you may reach the LFDT
security team via the Linux Foundation's general security disclosure address:

**security@linuxfoundation.org**

Include `[os-frontiers]` in the subject line so the report is routed correctly.

---

## What to Include in Your Report

A useful report helps us act quickly. Please include as much of the following
as is relevant:

- A clear description of the issue and its potential impact
- The specific file(s), section(s), or artifact(s) affected (file path and line
  numbers where applicable)
- The nature of the concern — content integrity, broken/malicious link,
  PII exposure, compromised reference, etc.
- Steps to reproduce or verify the issue
- Whether the issue is already publicly known or referenced elsewhere
- Any suggested remediation if you have one

---

## Response Process

| Step | Target Timeline |
|---|---|
| Acknowledgment of receipt | Within 3 business days |
| Initial triage and severity assessment | Within 7 business days |
| Remediation plan communicated to reporter | Within 14 business days |
| Fix merged and advisory published (if warranted) | Coordinated with reporter |

For issues assessed as low severity (e.g. a stale external link), we may
resolve via the normal pull request process without a formal advisory.

For issues assessed as high severity (e.g. maliciously injected content in a
widely-adopted governance template), we will:

1. Remove or quarantine the affected content immediately
2. Notify known downstream adopters via LFDT communication channels
3. Publish a retrospective advisory once the fix is confirmed stable

We will keep reporters informed at each stage and credit them in any public
advisory unless they request otherwise.

---

## Content Integrity Standards

Because OSFL produces normative guidance rather than runnable code, our primary
security controls are editorial and process-based.

### For Contributors

- All substantive changes to frameworks, whitepapers, and reference
  architectures require at least one maintainer review before merge
- External links included in published artifacts should point to stable,
  reputable sources; shortened URLs or links to ephemeral content are discouraged
- Do not include PII (names, emails, wallet addresses, organizational credentials)
  in committed content without explicit consent from the individuals involved
- Reference implementations or tooling schemas linked from this repository
  should themselves be from open, auditable sources

### For Maintainers

- Branch protection is enabled on `main`; direct pushes are not permitted
- Signed commits are encouraged for maintainers with merge rights
- Periodic review of external links in published artifacts is recommended,
  particularly prior to major releases
- Changes to governance documents (`CODE_OF_CONDUCT.md`, this file,
  `LICENSE`) require explicit approval from the LFDT lab steering group

---

## Vulnerability Disclosure Philosophy

The Open Source Frontiers Lab is explicitly neutral — not tied to any specific
protocol, network, or commercial product. Our security posture reflects that
neutrality: we aim to be a trusted, uncompromised source of reference material
for decentralized ecosystems. A security incident in this repository — whether
a tampered whitepaper or a governance template that embeds harmful guidance —
could propagate silently across dozens of downstream projects.

We therefore treat responsible disclosure as an act of stewardship consistent
with the lab's broader mission, and we are committed to responding to reports
with transparency, speed, and genuine appreciation for the work of those who
surface problems.

---

## Supported Versions

This repository does not version software releases. All guidance artifacts are
maintained on the `main` branch. Older versions of documents accessible through
Git history are not actively maintained; if you discover a concern in a
historical artifact that has since been corrected, no action is required.

If you are unsure whether a concern applies to current content, check the
latest state of `main` before reporting.

---

## Attribution and Acknowledgments

We are grateful to everyone who helps keep OSFL's research artifacts trustworthy
and safe to adopt. Reporters who identify and responsibly disclose valid security
concerns will be acknowledged in the relevant advisory (with their consent).

This policy is maintained by the Open Source Frontiers Lab under LF Decentralized
Trust. It is subject to periodic review and improvement — contributions and
suggestions to this document itself are welcome via pull request.

---

*This security policy is adapted from practices recommended by the Linux
Foundation Security Team and the [OpenSSF Security Policy Working Group](https://openssf.org).*
