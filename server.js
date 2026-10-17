const express = require('express');
const path = require('path');
const cors = require('cors');

const app = express();
const PORT = process.env.PORT || 3000;

app.use(cors());
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Load Payment API router if present
try {
  const { paymentRouter } = require('./server/paymentRouter');
  if (paymentRouter) {
    app.use('/api/payment', paymentRouter);
  }
} catch (e) {
  console.log('Payment router notice:', e.message);
}

// Serve static assets from site_1to1 directory
const siteDir = path.join(__dirname, 'site_1to1');
app.use(express.static(siteDir));

// Load Node FileSystem
const fs = require('fs');

// Primary route aliases
const aliases = {
  '/': 'index.html',
  '/portal': 'portal.html',
  '/portal.html': 'portal.html',
  '/receipt': 'receipt.html',
  '/receipt.html': 'receipt.html',
  '/application-fee-receipt': 'application-fee-receipt.html',
  '/application-fee-receipt.html': 'application-fee-receipt.html',
  '/offer-letter': 'offer-letter.html',
  '/offer-letter.html': 'offer-letter.html',
  '/admissions-offer-email': 'admissions-offer-email.html',
  '/admissions-offer-email.html': 'admissions-offer-email.html',
  '/email': 'admissions-offer-email.html',
  '/faculty': 'faculty.html',
  '/faculty.html': 'faculty.html',
  '/chemistry': 'pages/department-of-chemistry.html',
  '/department-of-chemistry': 'pages/department-of-chemistry.html',
  '/academics': 'pages/academics.html',
  '/who-we-are': 'pages/who-we-are.html',
  '/admissions': 'pages/admissions.html',
  '/research-and-scholarship': 'pages/research-and-scholarship.html',
  '/life-at-uchicago': 'pages/life-at-uchicago.html',
  '/visit': 'pages/visit.html',
  '/contact-us': 'pages/contact-us.html',
  '/careers': 'pages/careers.html',
  '/medicine': 'pages/medicine.html',
  '/students': 'pages/students.html',
  '/accreditation': 'pages/accreditation.html',
  '/non-discrimination': 'pages/non-discrimination.html',
  '/university-reports': 'pages/university-reports.html'
};

for (const [route, file] of Object.entries(aliases)) {
  app.get(route, (req, res) => {
    res.sendFile(path.join(siteDir, file));
  });
}

// Fallback handler with intelligent clean-URL resolution for all 240+ pages and assets
app.use((req, res) => {
  const cleanPath = req.path.replace(/^\/+|\/+$/g, '');
  if (!cleanPath) {
    return res.sendFile(path.join(siteDir, 'index.html'));
  }

  // 1. Direct file in siteDir
  const directPath = path.join(siteDir, cleanPath);
  if (fs.existsSync(directPath) && fs.statSync(directPath).isFile()) {
    return res.sendFile(directPath);
  }

  // 2. cleanPath + .html in siteDir
  const htmlPath = path.join(siteDir, cleanPath + '.html');
  if (fs.existsSync(htmlPath) && fs.statSync(htmlPath).isFile()) {
    return res.sendFile(htmlPath);
  }

  // 3. Direct file in siteDir/pages/
  const pagePath = path.join(siteDir, 'pages', cleanPath);
  if (fs.existsSync(pagePath) && fs.statSync(pagePath).isFile()) {
    return res.sendFile(pagePath);
  }

  // 4. cleanPath + .html in siteDir/pages/
  const pageHtmlPath = path.join(siteDir, 'pages', cleanPath + '.html');
  if (fs.existsSync(pageHtmlPath) && fs.statSync(pageHtmlPath).isFile()) {
    return res.sendFile(pageHtmlPath);
  }

  // 5. Default fallback to index.html
  res.sendFile(path.join(siteDir, 'index.html'));
});

if (require.main === module) {
  app.listen(PORT, () => {
    console.log(`University of Chicago Portal & Replica running on http://localhost:${PORT}`);
  });
}

module.exports = app;
