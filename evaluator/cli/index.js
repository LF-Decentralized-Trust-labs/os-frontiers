#!/usr/bin/env node

const fs = require('fs');
const path = require('path');

console.log("🔍 Running Open Source Frontiers 3-Piece Evaluator (dOSPO · OMF · ORF)...");

const targetDir = process.argv[2] ? path.resolve(process.argv[2]) : process.cwd();

if (!fs.existsSync(targetDir)) {
    console.error(`❌ Error: Target directory does not exist: ${targetDir}`);
    process.exit(1);
}

// Dynamic Repository Scanner
let dospoScore = 0;
let omfScore = 0;
let orfScore = 0;

const hasDospoDir = fs.existsSync(path.join(targetDir, 'dospo')) || fs.existsSync(path.join(targetDir, 'dOSPO'));
const hasOmfDir = fs.existsSync(path.join(targetDir, 'omf')) || fs.existsSync(path.join(targetDir, 'OMF'));
const hasOrfDir = fs.existsSync(path.join(targetDir, 'orf')) || fs.existsSync(path.join(targetDir, 'ORF'));
const hasSecurity = fs.existsSync(path.join(targetDir, 'SECURITY.md'));
const hasContracts = fs.existsSync(path.join(targetDir, 'contracts'));

if (hasDospoDir) dospoScore += 15;
if (hasSecurity) dospoScore += 10;

if (hasOmfDir) omfScore += 15;
if (hasContracts) omfScore += 10;

if (hasOrfDir) orfScore += 15;

const totalScore = dospoScore + omfScore + orfScore;
const totalPct = Math.round((totalScore / 75) * 100);

let level = "Level 0: Un-Architected / Fragile";
if (totalPct >= 85) {
    level = "Level 3: Self-Sustaining Closed Loop";
} else if (totalPct >= 65) {
    level = "Level 2: Fee-Supplemented Maintenance";
} else if (totalPct >= 40) {
    level = "Level 1: Governance & Retainers Bootstrapped";
}

console.log("\n=======================================================");
console.log(`📊 EVALUATOR SUITE TARGET: ${targetDir}`);
console.log(`🏛️ dOSPO Governance Score  : ${dospoScore} / 25`);
console.log(`🛠️ OMF Maintenance Score   : ${omfScore} / 25`);
console.log(`💰 ORF Replenishment Score : ${orfScore} / 25`);
console.log(`🏆 TOTAL SCORE             : ${totalScore} / 75 (${totalPct}%)`);
console.log(`🌱 MATURITY CLASSIFICATION : ${level}`);
console.log("=======================================================\n");
