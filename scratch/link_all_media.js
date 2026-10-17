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

function getFallbackImage(filename) {
  const lower = filename.toLowerCase();
  if (lower.includes('aerial') || lower.includes('campus') || lower.includes('quad')) {
    return localFilesMap['aerial_hydepark.png'] || localFilesMap['mainquadfall.png'];
  }
  if (lower.includes('student') || lower.includes('grad') || lower.includes('master') || lower.includes('doctoral')) {
    return localFilesMap['fallleaves_students.png'] || localFilesMap['harris-students-networking.jpg'];
  }
  if (lower.includes('lab') || lower.includes('science') || lower.includes('research')) {
    return localFilesMap['sisrm-research-meeting-1600.jpg'];
  }
  if (lower.includes('safe') || lower.includes('transport') || lower.includes('shuttle') || lower.includes('drive')) {
    return localFilesMap['fall-campus-safety-22.jpg'] || localFilesMap['bluelight.jpg'];
  }
  if (lower.includes('art') || lower.includes('culture') || lower.includes('music')) {
    return localFilesMap['artsgraycenter.png'];
  }
  return localFilesMap['mainquadfall.png'] || 'mainquadfall.png';
}

const comprehensiveRegex = /(https?:\/\/(?:www\.)?uchicago\.asia)?\/-\/media\/[^\s"'()]+\/([^/\s"'()?#]+\.(?:jpg|jpeg|png|svg|webp|gif))/gi;
const singleLevelRegex = /(https?:\/\/(?:www\.)?uchicago\.asia)?\/-\/media\/([^/\s"'()?#]+\.(?:jpg|jpeg|png|svg|webp|gif))/gi;

let filesUpdated = 0;
let totalReplacements = 0;

for (const hf of htmlFiles) {
  const isSubpage = hf.includes(path.join(siteDir, 'pages'));
  const assetPrefix = isSubpage ? '../assets/subpage_media/' : 'assets/subpage_media/';
  
  let content = fs.readFileSync(hf, 'utf-8');
  let countInFile = 0;
  
  function replaceHandler(match, domain, filename) {
    const lower = filename.toLowerCase();
    countInFile++;
    totalReplacements++;
    if (localFilesMap[lower]) {
      return assetPrefix + localFilesMap[lower];
    }
    const fallback = getFallbackImage(filename);
    return assetPrefix + fallback;
  }
  
  let newContent = content.replace(comprehensiveRegex, replaceHandler);
  newContent = newContent.replace(singleLevelRegex, replaceHandler);
  
  if (countInFile > 0) {
    fs.writeFileSync(hf, newContent, 'utf-8');
    filesUpdated++;
  }
}

console.log(`Files updated: ${filesUpdated}, Total media replacements: ${totalReplacements}`);
