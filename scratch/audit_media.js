const fs = require('fs');
const path = require('path');
const siteDir = path.join(__dirname, '..', 'site_1to1');
const pagesDir = path.join(siteDir, 'pages');

const files = fs.readdirSync(pagesDir).filter(f => f.endsWith('.html'));
const missingUrls = new Set();

for (const f of files) {
  const content = fs.readFileSync(path.join(pagesDir, f), 'utf-8');
  const matches = content.match(/https?:\/\/(?:www\.)?uchicago\.asia\/[^\s"'()]+/gi) || [];
  for (const m of matches) {
    if (m.match(/\.(jpg|jpeg|png|svg|webp|gif)/i)) {
      missingUrls.add(m);
    }
  }
}

console.log('Total remote media URLs still remaining in subpages:', missingUrls.size);
console.log(Array.from(missingUrls).slice(0, 30));
