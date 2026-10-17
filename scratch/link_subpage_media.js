const fs = require('fs');
const path = require('path');

const siteDir = path.join(__dirname, '..', 'site_1to1');
const subpageMediaDir = path.join(siteDir, 'assets', 'subpage_media');

let localFilesMap = {};
if (fs.existsSync(subpageMediaDir)) {
  const files = fs.readdirSync(subpageMediaDir);
  for (const f of files) {
    localFilesMap[f.toLowerCase()] = f;
  }
}

console.log('Total local subpage media files:', Object.keys(localFilesMap).length);

function getHtmlFiles(dir) {
  let results = [];
  const list = fs.readdirSync(dir);
  for (const file of list) {
    const fullPath = path.join(dir, file);
    const stat = fs.statSync(fullPath);
    if (stat && stat.isDirectory()) {
      results = results.concat(getHtmlFiles(fullPath));
    } else if (file.endsWith('.html')) {
      results.push(fullPath);
    }
  }
  return results;
}

const htmlFiles = getHtmlFiles(siteDir);
console.log('Total HTML files found:', htmlFiles.length);

const mediaRegex = /(https?:\/\/(?:www\.)?uchicago\.asia)?\/-\/media\/[^"'()\s]+\/([^"'()\s?#]+\.(?:jpg|jpeg|png|svg|webp|gif))/gi;

let filesUpdated = 0;
let totalReplacements = 0;

for (const hf of htmlFiles) {
  const isSubpage = hf.includes(path.join(siteDir, 'pages'));
  const assetPrefix = isSubpage ? '../assets/subpage_media/' : 'assets/subpage_media/';
  
  let content = fs.readFileSync(hf, 'utf-8');
  let countInFile = 0;
  
  const newContent = content.replace(mediaRegex, (match, domain, filename) => {
    const lower = filename.toLowerCase();
    if (localFilesMap[lower]) {
      countInFile++;
      totalReplacements++;
      return assetPrefix + localFilesMap[lower];
    }
    return match;
  });
  
  if (countInFile > 0) {
    fs.writeFileSync(hf, newContent, 'utf-8');
    filesUpdated++;
  }
}

console.log(`Files updated: ${filesUpdated}, Total media replacements: ${totalReplacements}`);
