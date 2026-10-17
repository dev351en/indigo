const fs = require('fs');

const full = fs.readFileSync('full_homepage.html', 'utf-8');
const site = fs.readFileSync('site_1to1/index.html', 'utf-8');

console.log('--- Head differences ---');
const fullHead = full.split('</head>')[0];
const siteHead = site.split('</head>')[0];
console.log('Full head links:');
(fullHead.match(/<link[^>]+>/g) || []).forEach(l => console.log(' ', l));

console.log('\nSite head links:');
(siteHead.match(/<link[^>]+>/g) || []).forEach(l => console.log(' ', l));

console.log('\n--- Checking sections in site_1to1/index.html ---');
const siteSections = site.match(/<section[^>]*class="([^"]*)"/g) || [];
console.log('Site section classes:');
siteSections.forEach(s => console.log(' ', s));

console.log('\n--- Checking sections in full_homepage.html ---');
const fullSections = full.match(/<section[^>]*class="([^"]*)"/g) || [];
console.log('Full section classes:');
fullSections.forEach(s => console.log(' ', s));
