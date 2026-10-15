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

// Route aliases
app.get('/', (req, res) => {
  res.sendFile(path.join(siteDir, 'index.html'));
});

app.get('/portal', (req, res) => {
  res.sendFile(path.join(siteDir, 'portal.html'));
});

app.get('/receipt', (req, res) => {
  res.sendFile(path.join(siteDir, 'receipt.html'));
});

app.get('/application-fee-receipt', (req, res) => {
  res.sendFile(path.join(siteDir, 'application-fee-receipt.html'));
});

app.get('/offer-letter', (req, res) => {
  res.sendFile(path.join(siteDir, 'offer-letter.html'));
});

app.get('/admissions-offer-email', (req, res) => {
  res.sendFile(path.join(siteDir, 'admissions-offer-email.html'));
});

app.get('/email', (req, res) => {
  res.sendFile(path.join(siteDir, 'admissions-offer-email.html'));
});

// Fallback for static subpages and assets
app.use((req, res) => {
  const targetPath = path.join(siteDir, req.path);
  res.sendFile(targetPath, (err) => {
    if (err) {
      res.sendFile(path.join(siteDir, 'index.html'));
    }
  });
});

if (require.main === module) {
  app.listen(PORT, () => {
    console.log(`University of Chicago Portal & Replica running on http://localhost:${PORT}`);
  });
}

module.exports = app;
