const fs = require('fs');
const path = require('path');

const file = path.join(__dirname, '../site_1to1/index.html');
const html = fs.readFileSync(file, 'utf8');
const search = '<script src="interactive_runtime.js"></script>';
const idx = html.indexOf(search);
console.log('Index:', idx);
if (idx !== -1) {
  // Remove it from current place and put right before </body>
  const without = html.replace(search, '');
  const finalHtml = without.replace('</body></html>', '<script src="interactive_runtime.js"></script>\n</body></html>');
  fs.writeFileSync(file, finalHtml, 'utf8');
  console.log('Moved interactive_runtime.js to before </body>');
}
