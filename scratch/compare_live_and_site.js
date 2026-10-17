const fs = require('fs');

const live = fs.readFileSync('C:/Users/brode/.gemini/antigravity-ide/brain/9ca19f0c-5510-4103-96d5-fdd67a3c2a60/.system_generated/steps/36/content.md', 'utf-8');
const site = fs.readFileSync('site_1to1/index.html', 'utf-8');

function getHeadLinks(html) {
  const head = html.split('</head>')[0];
  const links = head.match(/<link[^>]+>/gi) || [];
  return links;
}

console.log('--- Live UChicago Head Links ---');
console.log(getHeadLinks(live));

console.log('\n--- site_1to1/index.html Head Links ---');
console.log(getHeadLinks(site));

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

console.log('\nLive components:');
console.log(getComponents(live));

console.log('\nSite components:');
console.log(getComponents(site));
