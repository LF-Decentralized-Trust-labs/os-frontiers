#!/usr/bin/env node

const { execSync } = require('child_process');
const path = require('path');
const fs = require('fs');

console.log("🔍 Running Open Source Frontiers 3-Piece Evaluator (dOSPO · OMF · ORF)...");

const targetConfig = process.argv[2] ? path.resolve(process.argv[2]) : '';
const pythonScript = path.join(__dirname, 'assess_ecosystem.py');

function getPythonExecutable() {
    try {
        execSync('python3 --version', { stdio: 'ignore' });
        return 'python3';
    } catch (e) {
        return 'python';
    }
}

const pyBin = getPythonExecutable();

try {
    const cmd = targetConfig && fs.existsSync(targetConfig) && targetConfig.endsWith('.json')
        ? `${pyBin} "${pythonScript}" "${targetConfig}"`
        : `${pyBin} "${pythonScript}"`;
    
    const output = execSync(cmd, { encoding: 'utf-8' });
    console.log(output);
} catch (err) {
    console.error("❌ Error executing Python canonical evaluator:", err.message);
    process.exit(1);
}
