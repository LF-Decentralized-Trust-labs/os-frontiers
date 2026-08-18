# Open Replenishment Framework — Instrument Catalog

> **LF Decentralized Trust · Open Source Frontiers Lab Specification**  
> *Stage 0 Research Candidate · Release Edition: `v0.8.0-rc.1`*

---

## 1. Catalog Architecture & Two-Dimensional Classification

The **ORF Instrument Catalog** provides a rigorous, modular inventory of mechanisms for ecosystem replenishment. To eliminate conceptual confusion, every entry is explicitly classified across two primary dimensions: **Value-Origin Layer** (*Protocol, Application, Enterprise, Capital, Delegation*) and **Instrument Type** (*Revenue Source, Contribution Source, Routing Rail, Allocation Mechanism, Capital Management, Financial/Risk Product*).

Furthermore, every entry includes both an **External Precedent Rating** (observed real-world market precedents) and an **ORF Deployment Evidence Rating (D0 to D5)** representing its operational readiness for deployment.

---

## 2. Family A — Structural Network Revenue

### Instrument A.1: Protocol Fee Routing ($\tau$ Split)
- **Layer**: Protocol Layer · **Type**: Revenue Source · **Correlation Class**: Native Network Activity
- **External Precedent**: 🟢 Live Precedent (Cardano 20% treasury cut, Polkadot fee split)
- **Deployment Status**: **D4 Scaled** (Proven on L1 networks) · **Transferability**: Medium
- **Description**: Protocol-level rules automatically route a fixed percentage ($\tau$) of all L1 transaction fees directly into the governed ecosystem treasury.
- **Operational Mechanics**: Smart contract rules intercept fee collection at block validation, executing zero-overhead transfers before rewards are paid to validators.
- **Counter-Value / Legitimacy**: Requires explicit governance legitimacy from network stakeholders. Provides permanent, non-inflationary baseline funding.

### Instrument A.2: Sequencer Profit Contribution
- **Layer**: Protocol Layer · **Type**: Revenue Source · **Correlation Class**: Native Network Activity
- **External Precedent**: 🟢 Live Precedent (Optimism Superchain: greater of 15% net profit or 2.5% gross fees)
- **Deployment Status**: **D4 Scaled** (Proven across L2 rollup chains) · **Transferability**: High (for L2 ecosystems)
- **Description**: Layer-2 rollup chains joining a shared network execute standardized contracts transferring sequencing profits to a shared treasury.
- **Operational Mechanics**: Sequencer nodes execute automated profit calculations at batch submission, routing fee-takes to the Collective Treasury.

### Instrument A.3: Canonical Protocol Service Fees
- **Layer**: Protocol Layer · **Type**: Revenue Source · **Correlation Class**: Native Network Activity
- **External Precedent**: 🟢 Live Precedent (ENS Registrar `.eth` domain registration and renewal fees)
- **Deployment Status**: **D4 Scaled** (ENS generates $M+/yr) · **Transferability**: Low / Contextual
- **Description**: Canonical, un-forkable protocol registration services generate recurring protocol fees paid by users.
- **Operational Mechanics**: Smart contract registrars burn or deposit registration fees into the ecosystem treasury.

### Instrument A.4: Monetary Expansion Allocation
- **Layer**: Protocol Layer · **Type**: Contribution / Issuance Source · **Correlation Class**: Native Token Price
- **External Precedent**: 🟢 Live Precedent (Cardano monetary expansion, Polkadot unspent token issuance)
- **Deployment Status**: **D4 Scaled** · **Transferability**: High (for inflationary protocols)
- **CRITICAL POLICY NOTICE**: *Monetary expansion represents token dilution, NOT new economic revenue. It acts as a transitional funding source and CANNOT count toward non-inflationary self-sustainability metrics.*

---

## 3. Family B — Enterprise Earned Revenue

### Instrument B.1: Open Infrastructure Assurance Subscription (Product A)
- **Layer**: Enterprise Layer · **Type**: Revenue Source · **Correlation Class**: Enterprise Contract Revenue
- **External Precedent**: 🟢 Live Precedent (Tidelift Enterprise Package Assurance)
- **Deployment Status**: **D1 Buyer Validated** · **Transferability**: High
- **Description**: Commercial subscribers pay an annual subscription ($25k–$100k+) for open infrastructure risk reduction without buying maintainer control.
- **Operational Mechanics**: Customer receives maintained-project status, dependency vulnerability interpretation, direct escalation channels, planned-change briefings, quarterly risk reports, and official sustainer listing.
- **Service Capacity Requirement**: Low/Medium. Does not promise 24/7 emergency code patching.

### Instrument B.2: Extended Lifecycle Support (LTS) & SLA Agreement (Product B)
- **Layer**: Enterprise Layer · **Type**: Revenue Source · **Correlation Class**: Enterprise Contract Revenue
- **External Precedent**: 🟢 Live Precedent (Red Hat ELC, Canonical Ubuntu Advantage)
- **Deployment Status**: **D0 Hypothesis** (For generic DAOs without contracted support orgs) · **Transferability**: Medium
- **Description**: High-value commercial support contracts ($75k–$250k+) promising 24/36-month backport patch windows, 2-hour Sev-1 acknowledgements, and dedicated resolution paths under `ORFSlaVault.sol`.
- **CRITICAL GOVERNANCE REQUIREMENT**: *Must pass a formal Service Capacity Test before being offered to buyers. Requires contracted maintainers and a dedicated support escalation organization.*

---

## 4. Family C — Ecosystem Membership & Certification

### Instrument C.1: Ecosystem Sustaining Consortium Membership
- **Layer**: Ecosystem / Enterprise Layer · **Type**: Revenue Source · **Correlation Class**: Membership Revenue
- **External Precedent**: 🟢 Live Precedent (Linux Foundation Project Hosting & Membership Tiers)
- **Deployment Status**: **D4 Scaled** (Proven across global open-source foundations) · **Transferability**: High
- **Description**: Enterprise adopters join formal membership tiers (*Supporter, Sustainer, Strategic Sustainer*) paying annual dues ($10k–$250k+) to support shared infrastructure.
- **Operational Mechanics**: Neutral legal entity handles invoicing, membership benefits, working group participation, and executive briefings. Technical governance remains 100% independent of membership status.

### Instrument C.2: Certified Ecosystem Provider / Sustainer Program
- **Layer**: Application / Enterprise Layer · **Type**: Revenue Source · **Correlation Class**: Credential Market
- **External Precedent**: 🟢 Live Precedent (CNCF Certified Kubernetes Conformance Program — 90+ certified offerings)
- **Deployment Status**: **D4 Scaled** (CNCF model) · **Transferability**: High
- **Description**: Replaces naked "sustainability badges" with objective technical certification. Commercial providers pay annual fees ($10k–$50k) to submit to objective test suites, earning official trademark usage, registry listings, and enterprise referral routing.
- **Key Principle**: *Payment buys participation and testing services. Certification requires passing objective technical standards.*

### Instrument C.3: Professional Developer Certification & Training Bundles
- **Layer**: Application Layer · **Type**: Revenue Source · **Correlation Class**: Credential Market
- **External Precedent**: 🟢 Live Precedent (Linux Foundation CKA/CKAD Certifications, Linux Foundation Education)
- **Deployment Status**: **D3 Renewable** (For mature ecosystems) · **Transferability**: Medium (Requires employer demand)
- **Description**: Administering proctored technical certification exams ($300–$750) and developer training bundles for ecosystem engineers.

---

## 5. Family D — Voluntary / Incentivized Contributions

### Instrument D.1: Protocol Guild-Style Project Token/Yield Pledges
- **Layer**: Application Layer · **Type**: Contribution Source · **Correlation Class**: Philanthropic / Voluntary Pledges
- **External Precedent**: 🟢 Live Precedent (Protocol Guild — $80M+ committed by Arbitrum, Optimism, Lido, ENS)
- **Deployment Status**: **D4 Scaled** · **Transferability**: High
- **Description**: Successful ecosystem dApps and protocols voluntarily pledge 1% of token supply or protocol yield into a locked maintainer split contract.

### Instrument D.2: Validator Stake Pool Maintenance Pledges
- **Layer**: Delegation Layer · **Type**: Contribution Source · **Correlation Class**: Native Token Price
- **External Precedent**: 🟡 Partial Analog (Cardano Mission-Driven Pools / POSM Community Pools)
- **Deployment Status**: **D2 Paid Pilot** · **Transferability**: Medium
- **Description**: Validator node operators pledge a portion of their variable pool margin to fund open-source maintenance.

---

## 6. Family E — Capital Income

### Instrument E.1: Governed Endowment IPS & Liquid Reserve Yield
- **Layer**: Capital Layer · **Type**: Capital Management · **Correlation Class**: Capital-Market Return
- **External Precedent**: 🟢 Live Precedent (ENS DAO EP 6.46 Endowment — $90M+ AUM, Octant 100k ETH Staking)
- **Deployment Status**: **D4 Scaled** (For large capitalized treasuries) · **Transferability**: High (if capitalized)
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
