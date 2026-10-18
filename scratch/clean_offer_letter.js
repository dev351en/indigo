const fs = require('fs');
const path = require('path');

const files = [
  path.join(__dirname, '..', 'site_1to1', 'offer-letter.html'),
  path.join(__dirname, '..', 'site_1to1', 'pages', 'offer-letter.html')
];

files.forEach(f => {
  if (!fs.existsSync(f)) return;
  let c = fs.readFileSync(f, 'utf8');
  c = c.replace(/<\/div>\s*<\/div>\s*<\/div>\s*\n\s*<!-- Page 1 Document Render/, '</div>\n    </div>\n\n    <!-- Page 1 Document Render');
  fs.writeFileSync(f, c, 'utf8');
  console.log('Cleaned extra div in ' + f);
});
