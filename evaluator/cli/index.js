#!/usr/bin/env node

const { spawnSync, execSync } = require('child_process');
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
const args = [pythonScript];

if (targetConfig && fs.existsSync(targetConfig) && targetConfig.endsWith('.json')) {
    args.push(targetConfig);
}

const result = spawnSync(pyBin, args, { encoding: 'utf-8' });

if (result.error) {
    console.error("❌ Error executing Python canonical evaluator:", result.error.message);
    process.exit(1);
}

if (result.stdout) {
    console.log(result.stdout);
}

if (result.stderr) {
    console.error(result.stderr);
}

process.exit(result.status || 0);
