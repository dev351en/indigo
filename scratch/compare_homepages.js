const fs = require('fs');

const orig = fs.readFileSync('original_source.html', 'utf-8');
const full = fs.existsSync('full_homepage.html') ? fs.readFileSync('full_homepage.html', 'utf-8') : '';
const site = fs.readFileSync('site_1to1/index.html', 'utf-8');

console.log('original_source.html length:', orig.length);
console.log('full_homepage.html length:', full.length);
console.log('site_1to1/index.html length:', site.length);

function getComponents(html) {
  const matches = html.match(/class="([A-Za-z0-9_-]+_[a-zA-Z0-9_-]+)/g) || [];
  const comps = new Set();
  matches.forEach(m => {
    const cls = m.replace('class="', '');
    const prefix = cls.split('_')[0];
    if (prefix && prefix !== 'fa' && prefix !== 'dot' && prefix !== 'slick' && prefix !== 'slide' && prefix !== 'carousel') {
      comps.add(prefix);
    }
  });
  return Array.from(comps);
}

console.log('\nOrig components:');
console.log(getComponents(orig));

console.log('\nSite components:');
console.log(getComponents(site));

// Check scripts in site vs orig
function getScripts(html) {
  return html.match(/<script[^>]*>([\s\S]*?)<\/script>/gi) || [];
}
console.log('\nSite scripts count:', getScripts(site).length);
console.log('Orig scripts count:', getScripts(orig).length);

// Check if interactive_runtime.js is linked in site_1to1/index.html
console.log('\nDoes site link interactive_runtime.js?', site.includes('interactive_runtime.js'));
