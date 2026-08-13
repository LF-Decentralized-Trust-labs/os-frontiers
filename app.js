// Interactive Web Application for Open Source Frontiers Lab (LF Decentralized Trust)
// Version: Research Candidate v0.8.0-rc.1

document.addEventListener("DOMContentLoaded", () => {
  console.log("🚀 Open Source Frontiers Dashboard Loaded (v0.8.0-rc.1)");

  // 1. Navigation Tab Switching
  const navTabs = document.querySelectorAll(".nav-tab");
  const tabPanes = document.querySelectorAll(".tab-pane");

  navTabs.forEach((tab) => {
    tab.addEventListener("click", () => {
      navTabs.forEach((t) => t.classList.remove("active"));
      tabPanes.forEach((p) => p.classList.remove("active"));

      tab.classList.add("active");
      const targetId = tab.getAttribute("data-tab");
      const targetPane = document.getElementById(targetId);
      if (targetPane) {
        targetPane.classList.add("active");
      }
    });
  });

  // 2. Interactive 15-Indicator Evaluator Engine
  const evalInputs = document.querySelectorAll(".eval-indicator-input");
  const dospoMeter = document.getElementById("dospo-score");
  const omfMeter = document.getElementById("omf-score");
  const orfMeter = document.getElementById("orf-score");
  const totalMeter = document.getElementById("total-score");
  const levelOutput = document.getElementById("eval-level");

  function calculateMaturityScore() {
    let dospo = 0, omf = 0, orf = 0;

    evalInputs.forEach((input) => {
      const val = parseInt(input.value) || 0;
      const type = input.getAttribute("data-pillar");
      if (type === "dospo") dospo += val;
      if (type === "omf") omf += val;
      if (type === "orf") orf += val;
    });

    const replRatio = parseFloat(document.getElementById("eval-repl-ratio")?.value || "0.0");
    const total = dospo + omf + orf;
    const totalPct = Math.round((total / 75) * 100);

    if (dospoMeter) dospoMeter.textContent = `${dospo} / 25`;
    if (omfMeter) omfMeter.textContent = `${omf} / 25`;
    if (orfMeter) orfMeter.textContent = `${orf} / 25`;
    if (totalMeter) totalMeter.textContent = `${total} / 75 (${totalPct}%)`;

    let level = "Level 0: Un-Architected / Fragile";
    if (total >= 64 && replRatio >= 1.0) {
      level = "Level 3: Self-Sustaining Closed Loop";
    } else if (total >= 50) {
      level = "Level 2: Fee-Supplemented Maintenance";
    } else if (total >= 25) {
      level = "Level 1: Governance & Retainers Bootstrapped";
    }

    if (levelOutput) levelOutput.textContent = level;
  }

  evalInputs.forEach((input) => input.addEventListener("change", calculateMaturityScore));
  document.getElementById("eval-repl-ratio")?.addEventListener("input", calculateMaturityScore);

  // 3. Pro-Forma Calculator
  const calcBudget = document.getElementById("calc-budget");
  const calcSlas = document.getElementById("calc-slas");
  const calcCerts = document.getElementById("calc-certs");
  const calcBadges = document.getElementById("calc-badges");
  const calcPools = document.getElementById("calc-pools");
  const calcTxFees = document.getElementById("calc-tx-fees");

  const calcNetInflow = document.getElementById("calc-net-inflow");
  const calcRatio = document.getElementById("calc-ratio");
  const calcSurplus = document.getElementById("calc-surplus");

  function runProFormaCalculator() {
    const budget = parseFloat(calcBudget?.value || "3000000");
    const slas = (parseInt(calcSlas?.value || "15")) * 75000 * 0.65; // 35% cost
    const certs = (parseInt(calcCerts?.value || "600")) * 750 * 0.70; // 30% cost
    const badges = (parseInt(calcBadges?.value || "30")) * 25000 * 0.80; // 20% cost
    const pools = (parseInt(calcPools?.value || "40")) * 7500 * 0.90; // 10% cost
    const txFees = parseFloat(calcTxFees?.value || "1500000");

    const netInflow = slas + certs + badges + pools + txFees;
    const ratio = budget > 0 ? (netInflow / budget).toFixed(2) : "0.00";
    const surplus = netInflow - budget;

    if (calcNetInflow) calcNetInflow.textContent = `$${Math.round(netInflow).toLocaleString()} USD`;
    if (calcRatio) calcRatio.textContent = `${ratio}x`;
    if (calcSurplus) calcSurplus.textContent = `$${Math.round(surplus).toLocaleString()} USD`;
  }

  [calcBudget, calcSlas, calcCerts, calcBadges, calcPools, calcTxFees].forEach((el) => {
    el?.addEventListener("input", runProFormaCalculator);
  });

  calculateMaturityScore();
  runProFormaCalculator();
});
