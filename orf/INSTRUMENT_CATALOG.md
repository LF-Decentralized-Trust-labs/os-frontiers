# Open Replenishment Framework — Instrument Catalog

> **LF Decentralized Trust · Open Source Frontiers Lab Specification**  
> *Stage 0 Research Candidate · Release Edition: `v0.8.0-rc.1`*

---

## 1. Catalog Architecture & Two-Dimensional Classification

The **ORF Instrument Catalog** provides a rigorous, modular inventory of mechanisms for ecosystem replenishment. To eliminate conceptual confusion, every entry is explicitly classified across two primary dimensions: **Value-Origin Layer** (*Protocol, Application, Enterprise, Capital, Delegation*) and **Instrument Type** (*Revenue Source, Contribution Source, Routing Rail, Allocation Mechanism, Capital Management, Financial/Risk Product*).

Furthermore, every entry carries two ratings. **External Precedent (P0–P5)** describes how mature the mechanism is where it already operates. **Local Deployment (D0–D5)** describes what this ecosystem has proven with its own receipts, renewals, and net contribution. External precedent is not a local D rating. A program can be P4 somewhere else and D0 here until this ecosystem has receipts. Local D4 still means a diversified customer base with positive net contribution after operating costs.

---

## 2. Family A — Structural Network Revenue

### Instrument A.1: Protocol Fee Routing ($\tau$ Split)
- **Layer**: Protocol Layer · **Type**: Revenue Source · **Correlation Class**: Native Network Activity
- **External Precedent**: 🟢 Cardano treasury cut; Polkadot fee split — **P4 Scaled** (L1)
- **Local Deployment**: **D0 Hypothesis** until this ecosystem has authorized a fee split and cash has arrived. · **Transferability**: Medium
- **Description**: Protocol-level rules automatically route a fixed percentage ($\tau$) of all L1 transaction fees directly into the governed ecosystem treasury.
- **Operational Mechanics**: Smart contract rules intercept fee collection at block validation, executing zero-overhead transfers before rewards are paid to validators.
- **Counter-Value / Legitimacy**: Requires explicit governance legitimacy from network stakeholders. Provides permanent, non-inflationary baseline funding.

### Instrument A.2: Sequencer Profit Contribution
- **Layer**: Protocol Layer · **Type**: Revenue Source · **Correlation Class**: Native Network Activity
- **External Precedent**: 🟢 Optimism Superchain: greater of 15% net profit or 2.5% gross fees — **P4 Scaled** (L2)
- **Local Deployment**: **D0 Hypothesis** until this ecosystem's governance has authorized a split and cash has arrived. · **Transferability**: High (for L2 ecosystems)
- **Description**: Layer-2 rollup chains joining a shared network execute standardized contracts transferring sequencing profits to a shared treasury.
- **Operational Mechanics**: Sequencer nodes execute automated profit calculations at batch submission, routing fee-takes to the Collective Treasury.

### Instrument A.3: Canonical Protocol Service Fees
- **Layer**: Protocol Layer · **Type**: Revenue Source · **Correlation Class**: Native Network Activity
- **External Precedent**: 🟢 ENS Registrar `.eth` registration and renewal — **P4 Scaled**
- **Local Deployment**: **D0 Hypothesis** for an ecosystem without its own canonical namespace. · **Transferability**: Low / Contextual
- **Description**: Canonical, un-forkable protocol registration services generate recurring protocol fees paid by users.
- **Operational Mechanics**: Smart contract registrars burn or deposit registration fees into the ecosystem treasury.

### Instrument A.4: Monetary Expansion Allocation
- **Layer**: Protocol Layer · **Type**: Contribution / Issuance Source · **Correlation Class**: Native Token Price
- **External Precedent**: 🟢 Cardano monetary expansion; Polkadot unspent token issuance. Issuance is not non-inflationary revenue.
- **Local Deployment**: **D0 Hypothesis** until this ecosystem has its own receipts. · **Transferability**: High (for inflationary protocols)
- **CRITICAL POLICY NOTICE**: *Monetary expansion represents token dilution, NOT new economic revenue. It acts as a transitional funding source and CANNOT count toward non-inflationary self-sustainability metrics.*

---

## 3. Family B — Enterprise Earned Revenue

### Instrument B.1: Open Infrastructure Assurance Subscription (Product A)
- **Layer**: Enterprise Layer · **Type**: Revenue Source · **Correlation Class**: Enterprise Contract Revenue
- **External Precedent**: 🟢 Tidelift enterprise assurance — **P4** externally
- **Local Deployment**: **D1 Buyer Validated**, the usual local rating for this product before this ecosystem has receipts. · **Transferability**: High
- **Description**: Commercial subscribers pay an annual subscription ($25k–$100k+) for open infrastructure risk reduction without buying maintainer control.
- **Operational Mechanics**: Customer receives maintained-project status, dependency vulnerability interpretation, direct escalation channels, planned-change briefings, quarterly risk reports, and official sustainer listing.
- **Service Capacity Requirement**: Low/Medium. Does not promise 24/7 emergency code patching.

### Instrument B.2: Extended Lifecycle Support (LTS) & SLA Agreement (Product B)
- **Layer**: Enterprise Layer · **Type**: Revenue Source · **Correlation Class**: Enterprise Contract Revenue
- **External Precedent**: 🟢 Live Precedent (Red Hat ELC, Canonical Ubuntu Advantage)
- **Deployment Status**: **D0 Hypothesis** (For generic DAOs without contracted support orgs) · **Transferability**: Medium
- **Description**: High-value commercial support contracts ($75k–$250k+) promising 24/36-month backport patch windows, 2-hour Sev-1 acknowledgements, and dedicated resolution paths. The reference contract `ORFSlaVault.sol` was removed on 20 August 2026 and is not an implementation.
- **CRITICAL GOVERNANCE REQUIREMENT**: *Must pass a formal Service Capacity Test before being offered to buyers. Requires contracted maintainers and a dedicated support escalation organization.*

---

## 4. Family C — Ecosystem Membership & Certification

### Instrument C.1: Ecosystem Sustaining Consortium Membership
- **Layer**: Ecosystem / Enterprise Layer · **Type**: Revenue Source · **Correlation Class**: Membership Revenue
- **External Precedent**: 🟢 Linux Foundation membership tiers — **P4 Scaled**
- **Local Deployment**: **D0 Hypothesis** until this ecosystem has membership receipts. · **Transferability**: High
- **Description**: Enterprise adopters join formal membership tiers (*Supporter, Sustainer, Strategic Sustainer*) paying annual dues ($10k–$250k+) to support shared infrastructure.
- **Operational Mechanics**: Neutral legal entity handles invoicing, membership benefits, working group participation, and executive briefings. Technical governance remains 100% independent of membership status.

### Instrument C.2: Certified Ecosystem Provider / Sustainer Program
- **Layer**: Application / Enterprise Layer · **Type**: Revenue Source · **Correlation Class**: Credential Market
- **External Precedent**: 🟢 CNCF Certified Kubernetes Conformance Program — 90+ certified offerings — **P4 Scaled**. Payment buys testing, not a passing result.
- **Local Deployment**: **D0 Hypothesis** until this ecosystem runs its own conformance suite. · **Transferability**: High
- **Description**: Replaces naked "sustainability badges" with objective technical certification. Commercial providers pay annual fees ($10k–$50k) to submit to objective test suites, earning official trademark usage, registry listings, and enterprise referral routing.
- **Key Principle**: *Payment buys participation and testing services. Certification requires passing objective technical standards.*

### Instrument C.3: Professional Developer Certification & Training Bundles
- **Layer**: Application Layer · **Type**: Revenue Source · **Correlation Class**: Credential Market
- **External Precedent**: 🟢 Linux Foundation CKA/CKAD — **P3 Sustained**
- **Local Deployment**: **D0 Hypothesis** until this ecosystem has receipts. · **Transferability**: Medium (Requires employer demand)
- **Description**: Administering proctored technical certification exams ($300–$750) and developer training bundles for ecosystem engineers.

---

## 5. Family D — Voluntary / Incentivized Contributions

### Instrument D.1: Protocol Guild-Style Project Token/Yield Pledges
- **Layer**: Application Layer · **Type**: Contribution Source · **Correlation Class**: Philanthropic / Voluntary Pledges
- **External Precedent**: 🟢 Protocol Guild voluntary 1% pledges, vesting, revocable. Dollar totals are not restated in this catalog.
- **Local Deployment**: **D0 Hypothesis** until this ecosystem has receipts. · **Transferability**: High
- **Description**: Successful ecosystem dApps and protocols voluntarily pledge 1% of token supply or protocol yield into a locked maintainer split contract.

### Instrument D.2: Validator Stake Pool Maintenance Pledges
- **Layer**: Delegation Layer · **Type**: Contribution Source · **Correlation Class**: Native Token Price
- **External Precedent**: 🟡 Cardano Mission-Driven Pools / POSM community pools — **P2 Operating**
- **Local Deployment**: **D2 Paid Pilot** (the local rating already used for this analog). · **Transferability**: Medium
- **Description**: Validator node operators pledge a portion of their variable pool margin to fund open-source maintenance.

---

## 6. Family E — Capital Income

### Instrument E.1: Governed Endowment IPS & Liquid Reserve Yield
- **Layer**: Capital Layer · **Type**: Capital Management · **Correlation Class**: Capital-Market Return
- **External Precedent**: 🟢 ENS endowment (EP 6.46) and the Octant staking announcement. Dollar and ETH magnitudes are not restated on this rating line.
- **Local Deployment**: **D0 Hypothesis** until this ecosystem has receipts under its own IPS. · **Transferability**: High (if capitalized)
- **Description**: Deploying accumulated treasury capital into a governed Investment Policy Statement (IPS) targeting 3–5% real yield from low-risk assets (US Treasuries, stablecoins, ETH staking).
- **CRITICAL REALITY CHECK**: *Requires $60M–$100M+ principal to generate $3M/yr spendable yield. Functions as late-stage diversification, NOT a Day-1 bootstrap solution.*

---

## 7. Supporting Infrastructure & Allocation Engines

### Rail S.1: Dependency Graph Fund Splitting (Drips Protocol)
- **Layer**: Application Layer · **Type**: **Routing Rail** (Moves existing money)
- **External Precedent**: 🟢 Live Precedent (Drips Network `DripsHub` smart contracts)
- **Description**: Automated EVM smart contracts that recursively split incoming enterprise or grant revenue down the open-source software dependency tree.

### Rail S.2: Continuous Token Streaming (Superfluid CFA)
- **Layer**: Application Layer · **Type**: **Routing Rail** (Moves existing money)
- **External Precedent**: 🟢 Live Precedent (Superfluid Constant Flow Agreements)
- **Description**: Smart contract primitives that stream maintainer retainers continuously per second with real-time cancellation rights.

### Engine S.3: AI-Assisted Impact & Dependency Allocation
- **Layer**: Application Layer · **Type**: **Allocation Mechanism** (Determines split percentages)
- **External Precedent**: 🔵 Research-Stage (Deep Funding, Gitcoin AI allocation experiments)
- **Description**: Machine-learning models parsing GitHub dependency trees, commit churn, and user traffic to recommend fund distribution weights.

---

## 8. Advanced Financial & Risk Products (Research Horizon)

### Risk P.1: Open Source Security Mutuals
- **Layer**: Enterprise / Capital Layer · **Type**: Financial / Risk Product · **Deployment Status**: **D0 Hypothesis**
- **Description**: Underwriting security pools where projects pay risk-adjusted premiums to access guaranteed incident response funds.

### Risk P.2: Recoverable Mission Funding (RMF / Program-Related Investments)
- **Layer**: Capital Layer · **Type**: Financial / Risk Product · **Deployment Status**: **D1 Buyer Validated**
- **Description**: Repayable mission investments structured under strict IRS Program-Related Investment (PRI) guidelines, where funding is repaid from future commercial success.

### Risk P.3: Infrastructure Revenue Bonds
- **Layer**: Capital Layer · **Type**: Financial / Risk Product · **Deployment Status**: **D0 Hypothesis**
- **Description**: Issuing debt instruments backed by verified recurring enterprise SLA or protocol fee cash flows.
