# Dependency Audit Template
## The 60-Day Walkthrough

> **This is the first step.** The dependency audit is the non-negotiable prerequisite for all OMF portfolio decisions. Without it, funding decisions are based on who submits proposals rather than what the ecosystem actually depends on.
>
> This template provides a concrete 60-day walkthrough for a mid-sized Web3 ecosystem. Adapt timing and scope to your ecosystem's size and existing tooling.

---

## Pre-Audit Checklist

Before starting the audit, confirm:

- [ ] Governance authorization to conduct the audit and publish results
- [ ] Access to all ecosystem-critical repositories (GitHub orgs, GitLab groups, or equivalent)
- [ ] Budget for contractor engagement (~$15–30K for a thorough 60-day audit)
- [ ] Tooling access: CHAOSS Augur or GrimoireLab instance (or equivalent analytics platform)
- [ ] Designated point of contact within the ecosystem for maintainer interviews

---

## Phase 1: Automated Scanning (Weeks 1–2)

### Objective
Run language-specific dependency scanners across all ecosystem-critical repositories. Generate SBOMs. Aggregate into a unified dependency graph.

### Step 1: Repository inventory

List all repositories that fall within scope. Scope typically includes:
- Core protocol clients and node software
- Cryptographic libraries
- SDKs used by dApp developers
- Developer tooling (build tools, testing frameworks, CI infrastructure)
- Wallet libraries
- Indexers and data infrastructure

*Document the inclusion/exclusion criteria. Any repository excluded from scope is a potential blind spot — document why.*

### Step 2: Language-specific dependency scanning

Run the appropriate tooling for each technology stack in your ecosystem:

| Stack | Primary Tools | Output |
|---|---|---|
| **Rust** (Polkadot, Solana, NEAR, Substrate) | `cargo audit`, `cargo deny`, `cargo tree` | Cargo.lock → SBOM |
| **Go** (Cosmos SDK, Tendermint-based chains) | `go mod graph`, `govulncheck` | go.sum → dependency graph |
| **Haskell** (Cardano core) | `cabal-plan-bounds`, `stack` | Cabal freeze file |
| **Solidity / EVM** (Ethereum, L2s) | Slither, Hardhat/Foundry dependency resolution | Manual enumeration required |
| **TypeScript/JavaScript** (dApps, SDKs, tooling) | `npm audit`, `yarn audit`, `npm ls`, Dependabot | package-lock.json → SBOM |
| **Python** (tooling, scripts) | `pip-audit`, `safety`, `pipdeptree` | requirements.txt → dependency graph |

**For Solidity/EVM**: Library dependencies often require manual enumeration because Solidity's import model differs from package managers. Supplement automated scanning with manual review.

### Step 3: SBOM generation

Generate SBOMs in SPDX or CycloneDX format for each major repository.

**Recommended tooling**:
- `syft` (anchore/syft) — generates SBOMs from container images and filesystems, supports SPDX and CycloneDX
- `cdxgen` — CycloneDX generator with multi-language support
- Language-specific: `cargo sbom`, `cyclonedx-gomod`, `jake` (Python)

**SBOM format guidance**:
- Use **CycloneDX** for security-focused analysis (native VEX support, vulnerability matching)
- Use **SPDX** for license compliance and cross-ecosystem portability (ISO standard)
- Use **Package URL (purl)** for cross-ecosystem component identification

**Output**: One SBOM per major repository, aggregated into a unified dependency graph.

### Step 4: Aggregation

Combine individual repository SBOMs into an ecosystem-level dependency graph. Tools:
- `cdx-merge` (CycloneDX merging)
- CHAOSS Augur (automated aggregation and analysis)
- Custom tooling using Package URL as the common identifier

---

## Phase 2: Manual Supplement (Weeks 3–4)

### Objective
Capture non-scannable dependencies that automated tooling cannot detect.

### Non-scannable dependency categories

| Category | Discovery Method |
|---|---|
| **Proprietary/closed-source indexers** | Ecosystem survey of operators; direct interviews with infrastructure teams |
| **Oracle networks and bridge infrastructure** | Survey of protocols using cross-chain functionality |
| **RPC providers and hosted infrastructure** | Survey of dApp developers about infrastructure dependencies |
| **Forked or vendored libraries** | Manual repository review; `git log` analysis for copied code |
| **Undocumented internal dependencies** | Maintainer interviews |

### Maintainer interview protocol

Conduct structured interviews with maintainers of the top-20 most-used repositories. 30–45 minutes each. Recommended questions:

1. What does this project depend on that isn't captured in the package manifest?
2. Are there any upstream projects that, if they stopped being maintained, would break this project?
3. Are there any projects you personally depend on outside this organization that you use in this work?
4. What would happen to this project if you stopped being available?
5. Who else understands this codebase well enough to maintain it?
6. What's your current bandwidth? Are you feeling sustainable in this role?

*Question 6 is the most important for burnout risk scoring. Document responses carefully.*

### Declared dependency survey

Publish a short survey to ecosystem developers and operators asking:
- What infrastructure does your project depend on that you consider ecosystem-critical?
- What would break if [specific high-centrality library] went unmaintained tomorrow?
- Are there any "hidden" dependencies you think the ecosystem doesn't know about?

---

## Phase 3: Centrality Scoring (Weeks 5–6)

### Objective
Apply risk-priority scoring to the dependency graph to produce a ranked list of highest-risk dependencies.

### Step 1: Dependency centrality calculation

For each identified dependency, calculate:

```
Centrality = count of ecosystem projects that directly or transitively depend on this component
```

Weight transitive dependencies less than direct dependencies (suggested: direct = 1.0, one-hop transitive = 0.7, two-hop = 0.5).

**Tooling**: CHAOSS Augur provides centrality scoring. PageRank-style algorithms can be applied to the dependency graph using NetworkX (Python) or similar graph analysis libraries.

### Step 2: Risk-priority scoring

Apply the OMF risk-priority formula to each dependency:

```
Priority Score = (Dependency Centrality × 0.30)
              + (Inverse Bus Factor × 0.25)
              + (Maintainer Burnout Risk × 0.25)
              + (Security Incident History × 0.20)
```

**Bus factor data source**: Contributor interview data + GitHub contributor analytics (CHAOSS Augur, GrimoireLab)

**Burnout risk data source**: Maintainer interview responses + contribution trend analysis (declining commit frequency, increasing issue response time)

**Security incident data source**: GitHub Security Advisories, CVE database, ecosystem-specific disclosure records

### Step 3: Cross-reference with CHAOSS contributor health metrics

For the top-50 scored dependencies, pull CHAOSS contributor sustainability metrics:
- Contributor attrition rate (last 12 months)
- Time in role (maintainer tenure)
- Organizational diversity (are all contributors from one employer?)
- First response time trend (increasing = potential capacity issue)
- Release frequency trend (decreasing = potential health issue)

**Tooling**: CHAOSS Augur, GrimoireLab 2.0, OpenSSF Scorecard

---

## Phase 4: Publication (Weeks 7–8)

### Objective
Publish the dependency map, centrality scores, and coverage gap analysis. Present to governance for portfolio allocation decisions.

### Required publication artifacts

**1. Ecosystem Dependency Map**
- Visual dependency graph (can be generated from SBOM data using graphviz or D3)
- Complete list of all identified dependencies with centrality scores
- Methodology documentation (how centrality was calculated, what was included/excluded)

**2. Top-20 Risk Register**
The 20 highest risk-priority scored dependencies with:
- Dependency name and current version
- Centrality score and dependent project count
- Bus factor
- Maintainer burnout risk rating
- Security incident history summary
- Current OMF program coverage status (funded / unfunded / in transition)

**3. Coverage Gap Analysis**
- Which of the top-20 dependencies are currently supported by an OMF program?
- Which have no program support? (These are the highest-priority funding gaps)
- What is the estimated cost to bring all top-10 into a Retainer program?

**4. Governance Recommendations**
A 1–2 page summary suitable for governance consumption recommending:
- Which projects should be prioritized for Retainer programs
- Which projects should be prioritized for Resilience programs
- Estimated budget requirement for recommended initial programs

### Baseline metrics for ongoing monitoring

Record the following baseline values at audit completion. These become the starting point for ecosystem health tracking:
- Average Libyears score across top-20 dependencies
- Average bus factor across top-20 dependencies
- Percentage of top-20 with documented succession plans
- Percentage of top-20 with at least one Retainer-funded maintainer

---

## Audit Output Checklist

Before closing the audit, confirm all required outputs are complete:

- [ ] Complete SBOM set generated and archived (SPDX or CycloneDX)
- [ ] Ecosystem dependency map published (visual + machine-readable)
- [ ] Centrality scores calculated and documented with methodology
- [ ] Top-20 risk register published
- [ ] Coverage gap analysis complete
- [ ] Baseline health metrics recorded
- [ ] Governance recommendation report submitted
- [ ] Audit methodology documented for future replication

---

## Tooling Reference

| Tool | Purpose | Link |
|---|---|---|
| CHAOSS Augur | Dependency scanning, centrality scoring, contributor health | chaoss.community |
| GrimoireLab 2.0 | Historical data, identity management, ecosystem-level analysis | chaoss.github.io/grimoirelab |
| syft | SBOM generation from repositories and containers | github.com/anchore/syft |
| cdxgen | CycloneDX SBOM generation (multi-language) | github.com/CycloneDX/cdxgen |
| OpenSSF Scorecard | Security hygiene scoring | scorecard.dev |
| cargo-audit | Rust vulnerability scanning | crates.io/crates/cargo-audit |
| govulncheck | Go vulnerability scanning | pkg.go.dev/golang.org/x/vuln/cmd/govulncheck |
| npm audit | JavaScript vulnerability scanning | docs.npmjs.com |

---

## References

- CHAOSS Community: chaoss.community/metrics
- Cox et al. 2015: Measuring Dependency Freshness in Software Systems
- OpenSSF Scorecard: scorecard.dev
- SPDX: spdx.dev
- CycloneDX: cyclonedx.org
- Package URL specification: github.com/package-url
