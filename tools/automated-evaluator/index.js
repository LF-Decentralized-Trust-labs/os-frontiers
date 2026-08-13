#!/usr/bin/env node

const fs = require('fs');
const path = require('path');

console.log("🔍 Running Automated 3-Piece Ecosystem Assessment (dOSPO · OMF · ORF)...");

const targetDir = process.argv[2] ? path.resolve(process.argv[2]) : process.cwd();

function checkFileExists(base, files) {
  for (const f of files) {
    if (fs.existsSync(path.join(base, f))) return true;
  }
  return false;
}

const hasDOSPO = checkFileExists(targetDir, [
  'dOSPO/Start Here: Decentralized Open Source Program Office (dOSPO)',
  'dOSPO/dOSPO Charter',
  'GOVERNANCE.md'
]);

const hasOMF = checkFileExists(targetDir, [
  'OMF/Start Here: Open Maintenance Framework (OMF)',
  'OMF/Program Charter Template',
  'OMF.md'
]);

const hasORF = checkFileExists(targetDir, [
  'ORF/Start Here: Open Replenishment Framework (ORF)',
  'ORF/Instrument Catalog',
  'ORF.md'
]);

const hasSLA = checkFileExists(targetDir, [
  'ORF/Enterprise SLA & Reciprocal Funding Agreement',
  'pitch/ENTERPRISE_SPONSOR_KIT.md'
]);

const hasIPS = checkFileExists(targetDir, [
  'ORF/Investment Policy Statement Template',
  'IPS.md'
]);

const dospoScore = hasDOSPO ? 18 : 5;
const omfScore = hasOMF ? 18 : 5;
const orfScore = (hasORF ? 10 : 0) + (hasSLA ? 5 : 0) + (hasIPS ? 5 : 0);
const totalScore = dospoScore + omfScore + orfScore;
const overallPct = Math.round((totalScore / 60) * 100);

let level = "Level 0: Un-Architected";
if (overallPct >= 80) level = "Level 3: Self-Sustaining Loop";
else if (overallPct >= 55) level = "Level 2: Fee-Supplemented Maintenance";
else if (overallPct >= 30) level = "Level 1: Governance & Retainers Bootstrapped";

console.log("\n=======================================================");
console.log(`📊 AUTOMATED ASSESSMENT REPORT: ${targetDir}`);
console.log("=======================================================");
console.log(`🏛️ dOSPO Governance Score : ${dospoScore}/20 (${Math.round(dospoScore/20*100)}%)`);
console.log(`🛠️ OMF Deployment Score   : ${omfScore}/20 (${Math.round(omfScore/20*100)}%)`);
console.log(`💰 ORF Replenishment Score: ${orfScore}/20 (${Math.round(orfScore/20*100)}%)`);
console.log(`🏆 OVERALL MATURITY       : ${overallPct}% -> ${level}`);
console.log("=======================================================\n");

const report = {
  target: targetDir,
  dospoScore,
  omfScore,
  orfScore,
  totalScore,
  overallPct,
  level
};

fs.writeFileSync(path.join(targetDir, 'assessment_report.json'), JSON.stringify(report, null, 2));
console.log("💾 Output report saved to assessment_report.json");
