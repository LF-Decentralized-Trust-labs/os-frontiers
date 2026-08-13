#!/usr/bin/env node

const { execSync } = require('child_process');
const path = require('path');
const fs = require('fs');

console.log("🔍 Running Open Source Frontiers 3-Piece Evaluator (dOSPO · OMF · ORF)...");

const targetConfig = process.argv[2] ? path.resolve(process.argv[2]) : '';

const pythonScript = path.join(__dirname, 'assess_ecosystem.py');

try {
    const cmd = targetConfig && fs.existsSync(targetConfig) && targetConfig.endsWith('.json')
        ? `python "${pythonScript}" "${targetConfig}"`
        : `python "${pythonScript}"`;
    
    const output = execSync(cmd, { encoding: 'utf-8' });
    console.log(output);
} catch (err) {
    console.error("❌ Error executing Python canonical evaluator:", err.message);
    process.exit(1);
}
