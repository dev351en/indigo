const fs = require('fs');

const orig = fs.readFileSync('original_source.html', 'utf-8');
const live = fs.readFileSync('C:/Users/brode/.gemini/antigravity-ide/brain/9ca19f0c-5510-4103-96d5-fdd67a3c2a60/.system_generated/steps/36/content.md', 'utf-8');
const site = fs.readFileSync('site_1to1/index.html', 'utf-8');

console.log('--- Checking major sections ---');

function analyzeFile(name, html) {
  console.log(`\n=== ${name} ===`);
  console.log('Has EduHeader:', html.includes('EduHeader_container'));
  console.log('Has VideoSpotlight:', html.includes('VideoSpotlight_videoSpotlight'));
  console.log('Has CTABarSpotlight:', html.includes('CTABarSpotlight_container'));
  console.log('Has NewsFeatured:', html.includes('NewsFeatured_container'));
  console.log('Has CalloutBannerList:', html.includes('CalloutBannerList_container'));
  console.log('Has PhotoTabs:', html.includes('PhotoTabs_container'));
  console.log('Has HeadlineBar:', html.includes('HeadlineBar_container'));
  console.log('Has ImageTileGrid:', html.includes('ImageTileGrid_container'));
  console.log('Has CalloutTiles:', html.includes('CalloutTiles_container'));
  console.log('Has CalendarEmbed:', html.includes('CalendarEmbed_container'));
  console.log('Has Footer:', html.includes('Footer_container'));
}

analyzeFile('original_source.html', orig);
analyzeFile('live uchicago.edu', live);
analyzeFile('site_1to1/index.html', site);
