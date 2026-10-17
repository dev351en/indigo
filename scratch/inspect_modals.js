const fs = require('fs');
const path = require('path');

const html = fs.readFileSync(path.join(__dirname, '../site_1to1/index.html'), 'utf8');

const regex = /<div[^>]+id="([^"]+)"[^>]*>/g;
let m;
console.log('--- Divs with IDs after footer ---');
const footerIdx = html.indexOf('</footer>');
while ((m = regex.exec(html)) !== null) {
  if (m.index > footerIdx) {
    console.log('ID:', m[1], 'Match:', m[0].substring(0, 150));
  }
}
