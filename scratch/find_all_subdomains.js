const fs = require('fs');
const path = require('path');

const baseDir = path.resolve(__dirname, '..');
const subdomains = new Set();
const regex = /https?:\/\/([a-zA-Z0-9_\-]+)\.uchicago\.asia/g;

function scanDir(dir) {
  if (dir.includes('node_modules') || dir.includes('.git')) return;
  let entries;
  try {
    entries = fs.readdirSync(dir, { withFileTypes: true });
  } catch (e) {
    return;
  }
  for (const ent of entries) {
    const full = path.join(dir, ent.name);
    if (ent.isDirectory()) {
      scanDir(full);
    } else if (ent.isFile() && /\.(html|js|json|py)$/i.test(ent.name)) {
      try {
        const content = fs.readFileSync(full, 'utf8');
        let m;
        while ((m = regex.exec(content)) !== null) {
          subdomains.add(m[1].toLowerCase());
        }
      } catch (e) {}
    }
  }
}

scanDir(baseDir);
const list = Array.from(subdomains).sort();
console.log(JSON.stringify(list, null, 2));
