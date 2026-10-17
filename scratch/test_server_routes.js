const app = require('../server.js');
const http = require('http');

const server = http.createServer(app);
server.listen(0, async () => {
  const port = server.address().port;
  const baseUrl = `http://localhost:${port}`;
  console.log(`Test server running at ${baseUrl}`);

  const routesToTest = [
    '/',
    '/portal',
    '/portal.html',
    '/receipt',
    '/receipt.html',
    '/application-fee-receipt',
    '/application-fee-receipt.html',
    '/offer-letter',
    '/offer-letter.html',
    '/admissions-offer-email',
    '/admissions-offer-email.html',
    '/email',
    '/faculty',
    '/faculty.html',
    '/chemistry',
    '/department-of-chemistry',
    '/academics',
    '/who-we-are',
    '/admissions',
    '/research-and-scholarship',
    '/life-at-uchicago',
    '/visit',
    '/contact-us',
    '/careers',
    '/api/payment/demo-card-info'
  ];

  let passed = 0;
  let failed = 0;

  for (const r of routesToTest) {
    try {
      const res = await fetch(`${baseUrl}${r}`);
      if (res.status === 200) {
        passed++;
        console.log(`  [OK 200] ${r}`);
      } else {
        failed++;
        console.error(`  [FAIL ${res.status}] ${r}`);
      }
    } catch (err) {
      failed++;
      console.error(`  [ERROR] ${r}: ${err.message}`);
    }
  }

  console.log(`\nResults: ${passed} passed, ${failed} failed out of ${routesToTest.length} routes.`);
  server.close(() => {
    process.exit(failed > 0 ? 1 : 0);
  });
});
