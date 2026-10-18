const fs = require('fs');
const path = require('path');

const SITE_DIR = path.join(__dirname, '..', 'site_1to1');
const PAGES_DIR = path.join(SITE_DIR, 'pages');

const results = {
  pages_scanned: 0,
  links_checked: 0,
  dead_links: [],
  broken_anchors: [],
  unhandled_empty_clicks: [],
  missing_assets: [],
  design_anomalies: [],
  seat_locking_mentions: []
};

function getAllHtmlFiles(dir) {
  let files = [];
  const items = fs.readdirSync(dir);
  for (const item of items) {
    const fullPath = path.join(dir, item);
    const stat = fs.statSync(fullPath);
    if (stat.isDirectory()) {
      files = files.concat(getAllHtmlFiles(fullPath));
    } else if (item.endsWith('.html')) {
      files.push(fullPath);
    }
  }
  return files;
}

const htmlFiles = getAllHtmlFiles(SITE_DIR);
results.pages_scanned = htmlFiles.length;
console.log(`Found ${htmlFiles.length} HTML files to analyze.`);

htmlFiles.forEach((filePath) => {
  const relPath = path.relative(SITE_DIR, filePath).replace(/\\/g, '/');
  const content = fs.readFileSync(filePath, 'utf8');

  // Check seat locking mentions
  if (/(seat\s+locking|matriculation\s+fee|enrollment\s+deposit|reimbursable|refundable)/i.test(content)) {
    const matches = content.match(/[^<>\n]{0,100}(?:seat\s+locking|matriculation\s+fee|enrollment\s+deposit|reimbursable|refundable)[^<>\n]{0,100}/gi);
    if (matches) {
      results.seat_locking_mentions.push({
        file: relPath,
        matches: matches.slice(0, 4).map(s => s.trim())
      });
    }
  }

  // Check viewport
  if (!/<meta\s+name=["']viewport["']/i.test(content)) {
    results.design_anomalies.push({
      file: relPath,
      type: 'missing_viewport',
      details: 'Missing meta viewport tag'
    });
  }

  // Check title
  const titleMatch = content.match(/<title>([^<]*)<\/title>/i);
  if (!titleMatch || !titleMatch[1].trim()) {
    results.design_anomalies.push({
      file: relPath,
      type: 'missing_title',
      details: 'Missing or empty title tag'
    });
  }

  // Collect IDs on page
  const pageIds = new Set();
  const idRegex = /\sid=["']([^"']+)["']/gi;
  let idMatch;
  while ((idMatch = idRegex.exec(content)) !== null) {
    pageIds.add(idMatch[1]);
  }

  // Find all <a ...> tags
  const aRegex = /<a\s+([^>]*?)>/gi;
  let aMatch;
  while ((aMatch = aRegex.exec(content)) !== null) {
    results.links_checked++;
    const attrs = aMatch[1];
    const hrefMatch = attrs.match(/href=["']([^"']*)["']/i);
    const onclickMatch = attrs.match(/onclick=["']([^"']*)["']/i);
    const roleMatch = attrs.match(/role=["']([^"']*)["']/i);
    const dataToggleMatch = attrs.match(/data-(?:bs-)?(?:toggle|target)=["']([^"']*)["']/i);

    if (!hrefMatch) continue;
    const href = hrefMatch[1].trim();

    if (href === '' || href === '#') {
      if (!onclickMatch && !dataToggleMatch && (!roleMatch || roleMatch[1] !== 'tab')) {
        results.unhandled_empty_clicks.push({
          file: relPath,
          href,
          tag: aMatch[0].slice(0, 100)
        });
      }
      continue;
    }

    if (href.startsWith('javascript:')) {
      if (href === 'javascript:void(0)' || href === 'javascript:void(0);' || href === 'javascript:;') {
        if (!onclickMatch) {
          results.unhandled_empty_clicks.push({
            file: relPath,
            href,
            tag: aMatch[0].slice(0, 100)
          });
        }
      }
      continue;
    }

    if (href.startsWith('mailto:') || href.startsWith('tel:')) {
      continue;
    }

    if (href.startsWith('#')) {
      const targetId = href.slice(1);
      if (targetId && !pageIds.has(targetId)) {
        results.broken_anchors.push({
          file: relPath,
          anchor: href
        });
      }
      continue;
    }

    // Relative / local link
    let cleanHref = href.split('?')[0].split('#')[0];
    if (cleanHref.startsWith('http://') || cleanHref.startsWith('https://')) {
      try {
        const u = new URL(cleanHref);
        if (u.hostname === 'localhost' || u.hostname === 'uchicago.asia' || u.hostname === 'www.uchicago.asia') {
          cleanHref = u.pathname;
        } else {
          // External link
          continue;
        }
      } catch (e) {
        continue;
      }
    }

    const cleanPath = cleanHref.replace(/^\/+/, '');
    if (!cleanPath) continue;

    // Check existence
    const cand1 = path.join(SITE_DIR, cleanPath);
    const cand2 = path.join(SITE_DIR, cleanPath + '.html');
    const cand3 = path.join(PAGES_DIR, cleanPath);
    const cand4 = path.join(PAGES_DIR, cleanPath + '.html');
    const cand5 = path.join(path.dirname(filePath), cleanPath);
    const cand6 = path.join(path.dirname(filePath), cleanPath + '.html');

    const exists = (
      (fs.existsSync(cand1) && fs.statSync(cand1).isFile()) ||
      (fs.existsSync(cand2) && fs.statSync(cand2).isFile()) ||
      (fs.existsSync(cand3) && fs.statSync(cand3).isFile()) ||
      (fs.existsSync(cand4) && fs.statSync(cand4).isFile()) ||
      (fs.existsSync(cand5) && fs.statSync(cand5).isFile()) ||
      (fs.existsSync(cand6) && fs.statSync(cand6).isFile())
    );

    if (!exists) {
      results.dead_links.push({
        file: relPath,
        href,
        cleanPath
      });
    }
  }

  // Check <img> tags
  const imgRegex = /<img\s+([^>]*?)>/gi;
  let imgMatch;
  while ((imgMatch = imgRegex.exec(content)) !== null) {
    const attrs = imgMatch[1];
    const srcMatch = attrs.match(/src=["']([^"']*)["']/i);
    if (!srcMatch || !srcMatch[1].trim()) {
      results.missing_assets.push({
        file: relPath,
        type: 'missing_src',
        tag: imgMatch[0].slice(0, 100)
      });
      continue;
    }
    const src = srcMatch[1].trim();
    if (src.startsWith('data:') || src.startsWith('http://') || src.startsWith('https://')) {
      continue;
    }
    const cleanSrc = src.split('?')[0].split('#')[0].replace(/^\/+/, '');
    const cand1 = path.join(SITE_DIR, cleanSrc);
    const cand2 = path.join(path.dirname(filePath), cleanSrc);
    const cand3 = path.join(SITE_DIR, 'assets', 'subpage_media', path.basename(cleanSrc));
    const cand4 = path.join(SITE_DIR, 'assets', path.basename(cleanSrc));

    const exists = (
      (fs.existsSync(cand1) && fs.statSync(cand1).isFile()) ||
      (fs.existsSync(cand2) && fs.statSync(cand2).isFile()) ||
      (fs.existsSync(cand3) && fs.statSync(cand3).isFile()) ||
      (fs.existsSync(cand4) && fs.statSync(cand4).isFile())
    );

    if (!exists) {
      results.missing_assets.push({
        file: relPath,
        src
      });
    }
  }
});

fs.writeFileSync(path.join(__dirname, 'audit_report.json'), JSON.stringify(results, null, 2), 'utf8');

console.log('=== AUDIT SUMMARY ===');
console.log(`Pages scanned: ${results.pages_scanned}`);
console.log(`Links checked: ${results.links_checked}`);
console.log(`Dead links: ${results.dead_links.length}`);
console.log(`Broken anchors: ${results.broken_anchors.length}`);
console.log(`Unhandled empty/dead-end clicks: ${results.unhandled_empty_clicks.length}`);
console.log(`Missing assets: ${results.missing_assets.length}`);
console.log(`Design anomalies: ${results.design_anomalies.length}`);
console.log(`Seat locking files: ${results.seat_locking_mentions.length}`);
