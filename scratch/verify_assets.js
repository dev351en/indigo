const fs = require('fs');
const path = require('path');

const html = fs.readFileSync(path.join(__dirname, '../site_1to1/index.html'), 'utf8');

// Check src attributes
const srcMatches = html.match(/src="([^"]+)"/g) || [];
console.log('--- Checking src attributes ---');
srcMatches.forEach(match => {
  const url = match.slice(5, -1);
  if (!url.startsWith('http') && !url.startsWith('//') && !url.startsWith('data:')) {
    const fullPath = path.join(__dirname, '../site_1to1', url);
    const exists = fs.existsSync(fullPath);
    if (!exists) {
      console.log('MISSING:', url);
    } else {
      console.log('OK:', url);
    }
  }
});

// Check url(...) in style attributes
const styleMatches = html.match(/url\(([^)]+)\)/g) || [];
console.log('--- Checking style background urls ---');
styleMatches.forEach(match => {
  const url = match.slice(4, -1).replace(/['"]/g, '');
  if (url && !url.startsWith('http') && !url.startsWith('//') && !url.startsWith('data:')) {
    const fullPath = path.join(__dirname, '../site_1to1', url);
    const exists = fs.existsSync(fullPath);
    if (!exists) {
      console.log('MISSING style url:', url);
    } else {
      console.log('OK style url:', url);
    }
  }
});
