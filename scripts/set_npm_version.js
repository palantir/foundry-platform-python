const fs = require('fs');
const { execSync } = require('child_process');

const gitVersion = execSync('git describe --tags --abbrev=0').toString().trim();

console.log(`Setting version to ${gitVersion}...`);

const path = 'docs-snippets-npm/package.json';
const content = JSON.parse(fs.readFileSync(path, 'utf8'));
content.version = gitVersion;
fs.writeFileSync(path, JSON.stringify(content, null, 2));

console.log('Done!');
