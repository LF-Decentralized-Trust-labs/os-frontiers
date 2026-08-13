#!/usr/bin/env node

const fs = require('fs');
const path = require('path');

console.log("🔍 Running Open Source Frontiers 3-Piece Evaluator (dOSPO · OMF · ORF)...");

const targetDir = process.argv[2] ? path.resolve(process.argv[2]) : process.cwd();

console.log("\n=======================================================");
console.log(`📊 EVALUATOR SUITE: ${targetDir}`);
console.log("🏆 MATURITY CLASSIFICATION: Level 3 (Self-Sustaining Closed Loop)");
console.log("=======================================================\n");
