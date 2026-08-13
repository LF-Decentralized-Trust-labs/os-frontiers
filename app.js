// Open Source Frontiers Lab · 3-Piece Framework Suite (app.js)

// Master Collection Instruments Data (20+ items from July 2026 Whitepaper)
const catalogData = [
  {
    name: "Fee & Expansion Split",
    layer: "Protocol",
    anchor: "Canonical ledger rules",
    status: "live",
    statusText: "🟢 Cardano treasury (CIP-1694 / Monetary Policy)",
    tier: "Tier 1 (0-18m)",
    desc: "Fixed share of transaction fees and reserve expansion automatically routed to treasury."
  },
  {
    name: "Surplus Sequencer / Priority Tithe",
    layer: "Protocol",
    anchor: "Sequencing & ledger activity",
    status: "live",
    statusText: "🟢 Optimism sequencer allocation / RetroPGF",
    tier: "Tier 3 (36m+)",
    desc: "Governed share of sequencing surplus or priority fee revenue directed to sustainability."
  },
  {
    name: "Slashing & Penalty Routing",
    layer: "Protocol",
    anchor: "Canonical ledger rules",
    status: "live",
    statusText: "🟢 Polkadot directs slashed tokens to Treasury",
    tier: "Tier 3 (36m+)",
    desc: "Redirects protocol penalties and validator slashes directly to maintenance treasury."
  },
  {
    name: "Certification-Gated Contribution",
    layer: "Application",
    anchor: "Brand, registry & support bundle",
    status: "partial",
    statusText: "🟡 Protocol Guild + Tidelift partial analog",
    tier: "Tier 1 (0-18m)",
    desc: "Applications routing fee share receive official 'Sustains the Commons' badge and priority SLA."
  },
  {
    name: "Dependency-Directed Revenue Share",
    layer: "Application",
    anchor: "Verified dependency graph",
    status: "partial",
    statusText: "🟡 Drips live graph; tea proof of contribution",
    tier: "Tier 2 (18-36m)",
    desc: "Automated recurring dependency graph splitting based on verified manifests and attestations."
  },
  {
    name: "Verifiable Attestation Pools",
    layer: "Application",
    anchor: "Attested graph & reproducible builds",
    status: "partial",
    statusText: "🟡 Drips / ZK attestation research",
    tier: "Tier 2 (18-36m)",
    desc: "Governed dependency pool distributing rewards using reproducible build evidence and ZK attestations."
  },
  {
    name: "AI-Assisted Dependency Allocation",
    layer: "Application",
    anchor: "Verified graph, model competition",
    status: "partial",
    statusText: "🟡 Deep Funding pilot model",
    tier: "Tier 2 (18-36m)",
    desc: "Competing models estimate graph value supported by human spot checks and appeal processes."
  },
  {
    name: "Streaming Revenue Distribution",
    layer: "Application",
    anchor: "On-chain stream contracts",
    status: "live",
    statusText: "🟢 Superfluid infrastructure live",
    tier: "Tier 2 (18-36m)",
    desc: "Continuous payment streaming rails for real-time maintainer retainers and grant distribution."
  },
  {
    name: "Ecosystem-Owned Services",
    layer: "Application",
    anchor: "Canonical service & network effects",
    status: "live",
    statusText: "🟢 ENS registration revenue to DAO treasury",
    tier: "Tier 2 (18-36m)",
    desc: "Canonical ecosystem services (registries, naming, indexing) direct registration fees to treasury."
  },
  {
    name: "Maintenance SLAs & LTS Services",
    layer: "Enterprise",
    anchor: "Relationships & release commitments",
    status: "live",
    statusText: "🟢 Red Hat Extended Lifecycle & Tidelift",
    tier: "Tier 1 (0-18m)",
    desc: "Enterprise patch windows, compatibility guidance, and SLA response commitments for open source."
  },
  {
    name: "Supply-Chain SLA + Reciprocal Clause",
    layer: "Enterprise",
    anchor: "Assurance relationship & contract right",
    status: "partial",
    statusText: "🟡 Tidelift / Red Hat + recoverable funding",
    tier: "Tier 1 (0-18m)",
    desc: "Maintenance purchase combined with capped revenue share return clause for commercial grants."
  },
  {
    name: "Training & Certification",
    layer: "Enterprise",
    anchor: "Brand & credential verification value",
    status: "live",
    statusText: "🟢 Linux Foundation LFX training",
    tier: "Tier 1 (0-18m)",
    desc: "Paid developer training, security attestation certifications, and corporate workshops."
  },
  {
    name: "Foundation-Hosted Consortium",
    layer: "Enterprise",
    anchor: "Neutral brand & membership commitments",
    status: "live",
    statusText: "🟢 Apache Foundation & Linux Foundation",
    tier: "Tier 1 (0-18m)",
    desc: "Corporate membership tier separating enterprise sponsorship from technical project authority."
  },
  {
    name: "Recoverable / Reciprocal Funding",
    layer: "Enterprise",
    anchor: "Contract & treasury repayment rights",
    status: "live",
    statusText: "🟢 Program-Related Investments (PRIs)",
    tier: "Tier 1 (0-18m)",
    desc: "Grants to commercial projects with capped revenue share, warrants, or repayable advances."
  },
  {
    name: "Governed Endowment Policy",
    layer: "Capital",
    anchor: "Treasury & IPS authority",
    status: "live",
    statusText: "🟢 ENS Investment Policy Statement (EP 6.46)",
    tier: "Tier 1 (IPS) / Tier 3",
    desc: "Governance-approved IPS defining liquidity, manager replaceability, and capital preservation."
  },
  {
    name: "Perpetual Auction Treasury Funding",
    layer: "Capital",
    anchor: "Auction contract & brand demand",
    status: "live",
    statusText: "🟢 Nouns daily 24h auction",
    tier: "Tier 2 (18-36m)",
    desc: "Daily 24-hour NFT auction generating continuous inflow for community-governed treasury."
  },
  {
    name: "Autonomous Revenue Networks",
    layer: "Capital",
    anchor: "Immutable treasury & redemption rules",
    status: "research",
    statusText: "🔵 Revnet emerging architecture",
    tier: "Tier 3 (36m+)",
    desc: "Smart contracts locking staged issuance, payment processing, and treasury cash-out rules."
  },
  {
    name: "Yield-Donating Settlement Assets",
    layer: "Capital",
    anchor: "Reserve yield & payment adoption",
    status: "live",
    statusText: "🟢 Glo Dollar stablecoin model",
    tier: "Tier 2 (18-36m)",
    desc: "Stablecoin reserve backing directs yield to public-goods maintenance without user fees."
  },
  {
    name: "Strategic Venture Positions",
    layer: "Capital",
    anchor: "Treasury equity or warrants",
    status: "research",
    statusText: "🔵 Mission investment analog (High Risk)",
    tier: "Tier 3 (36m+)",
    desc: "Ring-fenced treasury equity or warrant allocations in core ecosystem startups."
  },
  {
    name: "Infrastructure Bonds",
    layer: "Capital",
    anchor: "Future governed fee revenue",
    status: "research",
    statusText: "🔵 Revenue-bond analog (Research)",
    tier: "Tier 3 (36m+)",
    desc: "Securitized bonds backed by anticipated future protocol transaction fees."
  },
  {
    name: "Security Mutual Premiums",
    layer: "Capital",
    anchor: "Risk pool & underwriting capacity",
    status: "live",
    statusText: "🟢 Nexus Mutual capital pool",
    tier: "Tier 2 (18-36m)",
    desc: "Regulated risk pool premiums entering capital pool to cover smart contract failures."
  },
  {
    name: "Hybrid Yield + Risk Pool",
    layer: "Capital",
    anchor: "Governed IPS & reserves",
    status: "partial",
    statusText: "🟡 ENS Endowment + Nexus Mutual hybrid",
    tier: "Tier 2 (18-36m)",
    desc: "Combines governed endowment investment yield with discretionary incident cover pools."
  },
  {
    name: "Public-Goods Stake Pools",
    layer: "Delegation",
    anchor: "Stake, certification, wallet surfacing",
    status: "live",
    statusText: "🟢 Cardano mission-driven pools",
    tier: "Tier 1 (0-18m)",
    desc: "Validator operators pledge margin share to sustainability treasury, surfaced in wallets."
  },
  {
    name: "Cross-Chain Delegation Registry",
    layer: "Delegation",
    anchor: "Verifiable commitments & discovery",
    status: "partial",
    statusText: "🟡 Neutral cross-chain registry proposal",
    tier: "Tier 2 (18-36m)",
    desc: "Neutral multi-chain registry surfacing verifiable validator pledges across PoS networks."
  }
];

// Ecosystem & Tooling Profiles Data (Reconciled Repository Directory Paths)
const profilesData = [
  {
    title: "Cardano Profile",
    category: "Use Case (UTXO / PoS)",
    badge: "POSM Pilot",
    fileLink: "use-cases/Cardano (Paid Open Source Model or POSM)",
    desc: "CIP-1694 Lovelace Treasury, Paid Open Source Model (POSM) retainers via Intersect OSC, mission pools, and CIP-159 multi-asset groundwork."
  },
  {
    title: "Optimism Superchain Profile",
    category: "Use Case (EVM Rollup)",
    badge: "RetroFunding",
    fileLink: "use-cases/Optimism Superchain (Sequencer Tithe & RetroFunding)",
    desc: "Sequencer revenue tithe, RetroFunding (RetroPGF) rounds, and Open Source Observer (OSO) repository metrics integration."
  },
  {
    title: "Polkadot Profile",
    category: "Use Case (Substrate / PoS)",
    badge: "OpenGov",
    fileLink: "use-cases/Polkadot (OpenGov & Substrate Treasury)",
    desc: "OpenGov spender tracks, Technical Fellowship whitelist, Treasury slash routing, and Polkadot Community Foundation (PCF) legal sleeve."
  },
  {
    title: "Ethereum & EVM Profile",
    category: "Use Case (EVM L1)",
    badge: "Endowments",
    fileLink: "use-cases/Ethereum & EVM Ecosystem (EIP-1559, Protocol Guild, ENS EP 6.46)",
    desc: "EIP-1559 base fee burn countermodel, Protocol Guild 1% pledge, ENS Registrar revenue, and ENS EP 6.46 IPS endowment."
  },
  {
    title: "Drips Protocol Profile",
    category: "Tool / Protocol",
    badge: "Dependency Splitting",
    fileLink: "tools/Drips Protocol (Dependency Graph Distribution)",
    desc: "On-chain dependency graph splitting and streaming distributions across EVM networks and Filecoin."
  },
  {
    title: "Superfluid Profile",
    category: "Tool / Protocol",
    badge: "Money Streaming",
    fileLink: "tools/Superfluid (Real-Time Money Streaming)",
    desc: "Real-time, continuous token streaming rails for maintainer retainers and subscription memberships."
  },
  {
    title: "Open Source Observer Profile",
    category: "Tool / Analytics",
    badge: "OSO Impact",
    fileLink: "tools/Open Source Observer",
    desc: "Open-source data infrastructure measuring repository metrics, developer retention, and dependency graphs."
  }
];

// Template Text Definitions
const templateDocs = {
  orf_charter: `# ORF Collection Instrument Charter Template
instrument_name: "[Name of Instrument]"
layer: "Protocol | Application | Enterprise & Services | Capital | Delegation"
precedent_status: "Live Precedent | Partial Analog | Research-Stage Proposal"
mandate_id: "dOSPO-MANDATE-YYYY-XXX"

## 1. Value Alignment & Fork-Resistance Anchor
- Point of Value Realization: [Protocol / App / Enterprise / Treasury Yield]
- Fork-Resistant Anchor: [Canonical state / Liquidity / Registry Badge / Support Team]

## 2. Benefit Bundle
- Enterprise LTS Patch Windows
- Defined SLA Response Targets
- "Sustains the Commons" Official Certification Badge
*Universal Safety*: Vulnerability intake and emergency security triage remain free and universal.

## 3. Governance & Audit
- dOSPO Authorization Mandate
- Annual Cost-to-Collect Audit Requirement
- Sunset & Wind-Down Customer Continuity Plan`,

  "5_q_assessment": `# ORF Replenishment Posture Evaluation Sheet
1. Ratio: What is your replenishment ratio today? [ Score: / 5 ]
2. Anchors: Does collection attach to fork-resistant anchors? [ Score: / 5 ]
3. Bundles: Is payment attached to independently valuable benefits? [ Score: / 5 ]
4. Mandate: Are collection rails chartered and independently audited? [ Score: / 5 ]
5. Runway: Can baseline maintenance survive a 2-3 year bear market? [ Score: / 5 ]
TOTAL SCORE: / 25`,

  ips: `# Capital Layer Investment Policy Statement (IPS) Template
1. Investment Objectives: Preserve capital in real terms while generating non-inflationary yield for open-source maintenance.
2. Spending Rule: Only net yield above inflation may be spent; principal reserves remain intact.
3. Asset Allocation Limits:
   - Tier 1 Liquid Stables: 30% - 50%
   - Tier 2 Staked Native Assets: 40% - 60%
   - Tier 3 Fixed Income & T-Bills: 20% - 30%
4. Manager Replaceability: Governance retains 51% vote authority to replace any manager or terminate vault delegates.`,

  sla: `# Enterprise Maintenance SLA & Reciprocal Funding Agreement
1. Scope of Maintenance Services:
   - Defined 24/36 month Extended Lifecycle (LTS) patch windows.
   - Severity 1 SLA response target within 2 hours.
   - Official "Sustains the Commons" enterprise registry badge.
2. Reciprocal Funding Clause:
   - Client agrees to route 1.0% - 3.0% of net commercial application revenue back to treasury, capped at 150% - 200% of initial grant.
3. Maintenance Autonomy Safeguard: Payment purchases support services; it never purchases technical roadmap authority.`,

  audit: `# ORF Independent Collection Audit Report
Audit Period: Q[X] YYYY
Audit Firm: [Independent Auditor]
Total Gross Inflows: $[ Amount ]
Total Cost to Collect: $[ Amount ]
Net Treasury Replenishment: $[ Amount ]
Net Replenishment Ratio: [ Net Collection / Deployed Budget ]
Attribution Integrity Score: [ % ]`,

  dospo_charter: `# dOSPO Governance Authority Charter
1. Purpose: Bounded, community-mandated coordination body holding the governance triangle (Legitimacy, Neutrality, Execution).
2. Scope: Authorizes spending mandates under OMF and collection policies under ORF.
3. Operator Replaceability: Governance mandate subject to annual evidence-based renewal vote by community delegates.`,

  omf_retainer: `# OMF Maintainer Retainer Agreement
1. Retainer Scope: Recurring monthly stipend for core maintainers of [Repository Name].
2. Availability Commitment: Security patch availability, PR reviews, and quarterly health reporting.
3. Autonomy Guarantee: Funding supports maintenance capacity; technical decision-making remains autonomous.`
};

// Application State
let activeLayerFilter = "all";
let activeStatusFilter = "all";
let searchQuery = "";

// Initialize App
document.addEventListener("DOMContentLoaded", () => {
  setupNavigation();
  renderCatalog();
  renderProfiles();
  setupCatalogControls();
  setupQuiz();
  setupCalculator();
  setupTemplateExporter();
});

// Navigation Function
function setupNavigation() {
  const navBtns = document.querySelectorAll(".nav-btn");
  navBtns.forEach(btn => {
    btn.addEventListener("click", () => {
      const tabId = btn.getAttribute("data-tab");
      switchTab(tabId);
    });
  });
}

function switchTab(tabId) {
  document.querySelectorAll(".nav-btn").forEach(b => b.classList.remove("active"));
  document.querySelectorAll(".tab-pane").forEach(p => p.classList.remove("active"));

  const targetBtn = document.querySelector(`.nav-btn[data-tab="${tabId}"]`);
  const targetPane = document.getElementById(tabId);

  if (targetBtn) targetBtn.classList.add("active");
  if (targetPane) targetPane.classList.add("active");

  window.scrollTo({ top: 0, behavior: "smooth" });
}

// Catalog Controls & Rendering
function setupCatalogControls() {
  const searchInput = document.getElementById("catalog-search");
  if (searchInput) {
    searchInput.addEventListener("input", (e) => {
      searchQuery = e.target.value.toLowerCase();
      renderCatalog();
    });
  }

  const layerBtns = document.querySelectorAll("[data-filter-layer]");
  layerBtns.forEach(btn => {
    btn.addEventListener("click", () => {
      layerBtns.forEach(b => b.classList.remove("active"));
      btn.classList.add("active");
      activeLayerFilter = btn.getAttribute("data-filter-layer");
      renderCatalog();
    });
  });

  const statusBtns = document.querySelectorAll("[data-filter-status]");
  statusBtns.forEach(btn => {
    btn.addEventListener("click", () => {
      statusBtns.forEach(b => b.classList.remove("active"));
      btn.classList.add("active");
      activeStatusFilter = btn.getAttribute("data-filter-status");
      renderCatalog();
    });
  });
}

function renderCatalog() {
  const container = document.getElementById("catalog-container");
  if (!container) return;

  const filtered = catalogData.filter(item => {
    const matchesLayer = activeLayerFilter === "all" || item.layer.toLowerCase() === activeLayerFilter.toLowerCase();
    const matchesStatus = activeStatusFilter === "all" || item.status === activeStatusFilter;
    const matchesSearch = searchQuery === "" || 
      item.name.toLowerCase().includes(searchQuery) ||
      item.anchor.toLowerCase().includes(searchQuery) ||
      item.statusText.toLowerCase().includes(searchQuery) ||
      item.desc.toLowerCase().includes(searchQuery);

    return matchesLayer && matchesStatus && matchesSearch;
  });

  if (filtered.length === 0) {
    container.innerHTML = `<div style="grid-column: 1/-1; text-align:center; padding: 2rem; color: var(--text-muted);">No collection instruments found matching your filter criteria.</div>`;
    return;
  }

  container.innerHTML = filtered.map(item => `
    <div class="catalog-item-card">
      <div class="item-header">
        <div class="item-name">${item.name}</div>
        <span class="item-layer-tag layer-${item.layer.toLowerCase()}">${item.layer}</span>
      </div>
      <p style="font-size: 0.88rem; color: var(--text-muted); margin-bottom: 0.8rem;">${item.desc}</p>
      <div class="item-anchor"><strong>Anchor:</strong> ${item.anchor}</div>
      <div class="item-precedent">
        <div><strong>Status:</strong> ${item.statusText}</div>
        <div style="margin-top: 0.2rem; color: var(--accent-cyan);"><strong>Sequence:</strong> ${item.tier}</div>
      </div>
    </div>
  `).join("");
}

// Profiles Section Rendering
function renderProfiles() {
  const container = document.getElementById("profiles-grid");
  if (!container) return;

  container.innerHTML = profilesData.map(p => `
    <div class="catalog-item-card">
      <div class="item-header">
        <div class="item-name">${p.title}</div>
        <span class="badge badge-primary">${p.badge}</span>
      </div>
      <div style="font-size: 0.78rem; color: var(--accent-cyan); font-weight: 600; margin-bottom: 0.5rem;">${p.category}</div>
      <p style="font-size: 0.88rem; color: var(--text-muted); margin-bottom: 1rem;">${p.desc}</p>
      <div class="item-precedent">
        <a href="${p.fileLink}" target="_blank" style="color: var(--accent-cyan); text-decoration: none; font-weight: 600; font-size: 0.85rem;">View Document &rarr;</a>
      </div>
    </div>
  `).join("");
}

// 5-Question Quiz Setup
function setupQuiz() {
  const radios = document.querySelectorAll('.options-group input[type="radio"]');
  radios.forEach(radio => {
    radio.addEventListener("change", updateQuizScore);
  });

  updateQuizScore();
}

function updateQuizScore() {
  let totalScore = 0;
  for (let i = 1; i <= 5; i++) {
    const checked = document.querySelector(`input[name="q${i}"]:checked`);
    if (checked) {
      totalScore += parseInt(checked.value, 10);
    }
  }

  const scoreDisplay = document.getElementById("total-score");
  const meterFill = document.getElementById("meter-fill");
  const phaseBadge = document.getElementById("phase-badge");
  const phaseDesc = document.getElementById("phase-desc");

  if (scoreDisplay) scoreDisplay.textContent = `${totalScore} / 25`;
  if (meterFill) meterFill.style.width = `${(totalScore / 25) * 100}%`;

  if (totalScore <= 9) {
    if (phaseBadge) {
      phaseBadge.textContent = "Phase 1: Reserve-Funded (Bootstrap)";
      phaseBadge.className = "badge badge-primary";
    }
    if (phaseDesc) phaseDesc.textContent = "Reserves carry the budget. Focus on dOSPO charters, voluntary app bundles, and Enterprise SLA pilots.";
  } else if (totalScore <= 18) {
    if (phaseBadge) {
      phaseBadge.textContent = "Phase 2: Fee-Supplemented";
      phaseBadge.className = "badge badge-accent";
    }
    if (phaseDesc) phaseDesc.textContent = "Earned and captured revenue covers 40-60% of baseline maintenance. Expand SLA sales and attestation pools.";
  } else {
    if (phaseBadge) {
      phaseBadge.textContent = "Phase 3: Self-Sustaining";
      phaseBadge.className = "badge badge-success";
    }
    if (phaseDesc) phaseDesc.textContent = "Net replenishment ratio ≥ 1.0. Governed IPS endowment yield + earned revenue cover baseline maintenance floor.";
  }
}

// Calculator Setup
function setupCalculator() {
  const calcInputs = [
    "calc-sla-count", "calc-sla-val", "calc-sla-cost",
    "calc-cert-count", "calc-cert-val",
    "calc-app-count", "calc-pool-count", "calc-omf-cost"
  ];

  calcInputs.forEach(id => {
    const el = document.getElementById(id);
    if (el) el.addEventListener("input", runCalculator);
  });

  runCalculator();
}

function runCalculator() {
  const slaCount = parseFloat(document.getElementById("calc-sla-count")?.value || 0);
  const slaVal = parseFloat(document.getElementById("calc-sla-val")?.value || 0);
  const slaCostPct = parseFloat(document.getElementById("calc-sla-cost")?.value || 0) / 100;

  const certCount = parseFloat(document.getElementById("calc-cert-count")?.value || 0);
  const certVal = parseFloat(document.getElementById("calc-cert-val")?.value || 0);

  const appCount = parseFloat(document.getElementById("calc-app-count")?.value || 0);
  const poolCount = parseFloat(document.getElementById("calc-pool-count")?.value || 0);
  const omfCost = parseFloat(document.getElementById("calc-omf-cost")?.value || 1);

  // Math Models
  const slaGross = slaCount * slaVal;
  const certGross = certCount * certVal;
  const appGross = appCount * 15000;
  const poolGross = poolCount * 5000;

  const grossTotal = slaGross + certGross + appGross + poolGross;

  // Servicing Costs
  const slaServicingCost = slaGross * slaCostPct;
  const certServicingCost = certGross * 0.40;
  const appServicingCost = appGross * 0.30;
  const poolServicingCost = poolGross * 0.15;

  const totalCost = slaServicingCost + certServicingCost + appServicingCost + poolServicingCost;
  const netReplenishment = grossTotal - totalCost;
  const coveragePct = (netReplenishment / omfCost) * 100;

  // Render
  document.getElementById("res-gross").textContent = `$${grossTotal.toLocaleString()}`;
  document.getElementById("res-cost").textContent = `$${Math.round(totalCost).toLocaleString()}`;
  document.getElementById("res-net").textContent = `$${Math.round(netReplenishment).toLocaleString()}`;
  document.getElementById("res-coverage").textContent = `${coveragePct.toFixed(1)}%`;
}

// Template Exporter Setup
function setupTemplateExporter() {
  const select = document.getElementById("template-select");
  const preview = document.getElementById("template-preview-code");
  const btnCopy = document.getElementById("btn-copy-template");
  const btnDownload = document.getElementById("btn-download-template");

  if (select && preview) {
    select.addEventListener("change", () => {
      const key = select.value;
      preview.textContent = templateDocs[key] || "Template content not available.";
    });
    preview.textContent = templateDocs[select.value];
  }

  if (btnCopy) {
    btnCopy.addEventListener("click", () => {
      const text = preview.textContent;
      navigator.clipboard.writeText(text).then(() => {
        btnCopy.textContent = "✅ Copied!";
        setTimeout(() => btnCopy.textContent = "📋 Copy Markdown", 2000);
      });
    });
  }

  if (btnDownload) {
    btnDownload.addEventListener("click", () => {
      const text = preview.textContent;
      const filename = `${select.value}.md`;
      const blob = new Blob([text], { type: "text/markdown" });
      const url = URL.createObjectURL(blob);
      const a = document.createElement("a");
      a.href = url;
      a.download = filename;
      a.click();
      URL.revokeObjectURL(url);
    });
  }
}
