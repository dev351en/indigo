const fs = require('fs');
const path = require('path');

const a2zPath = path.join(__dirname, '..', 'site_1to1', 'pages', 'who-we-are_a2z.html');
if (fs.existsSync(a2zPath)) {
  let content = fs.readFileSync(a2zPath, 'utf8');
  
  // Check if X, Y, Z anchors are present
  ['X', 'Y', 'Z'].forEach(letter => {
    if (!content.includes(`id="${letter}"`) && !content.includes(`id='${letter}'`)) {
      console.log(`Adding anchor placeholder for ${letter}`);
      // Find where W ends or append before </main>
      const anchorBlock = `
      <div id="${letter}" class="LetterSection_container" style="padding: 20px 0; border-top: 1px solid #e0e0e0; margin-top: 20px;">
        <h2 style="font-family: 'UChicagoSerif', Georgia, serif; font-size: 24px; color: #800000; margin-bottom: 8px;">${letter}</h2>
        <p style="font-size: 13.5px; color: #666; font-style: italic;">No university departments, institutes, or offices currently indexed under letter ${letter}. For general inquiries, please refer to the <a href="contact-us.html" style="color: #800000; text-decoration: underline;">Campus Directory &amp; Contact Directory</a>.</p>
      </div>`;
      
      content = content.replace('</main>', anchorBlock + '\n</main>');
    }
  });
  
  fs.writeFileSync(a2zPath, content, 'utf8');
  console.log('Fixed A-Z anchors in who-we-are_a2z.html');
}
