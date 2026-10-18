const app = require('../server.js');
const http = require('http');

const server = http.createServer(app);
server.listen(0, async () => {
  const port = server.address().port;
  const tests = [
    { host: 'portal.uchicago.asia', path: '/', expect: 'Applicant' },
    { host: 'chemistry.uchicago.asia', path: '/', expect: 'Chemistry' },
    { host: 'directory.uchicago.asia', path: '/', expect: 'Faculty' },
    { host: 'uchicago.asia', path: '/', expect: 'Chicago' }
  ];

  let failed = 0;
  for (const t of tests) {
    try {
      const res = await fetch(`http://localhost:${port}${t.path}`, {
        headers: { 'Host': t.host }
      });
      const text = await res.text();
      const match = text.includes(t.expect);
      if (match) {
        console.log(`[PASS] Host: ${t.host} -> matched "${t.expect}" (Status: ${res.status})`);
      } else {
        console.error(`[FAIL] Host: ${t.host} -> did NOT match "${t.expect}"`);
        failed++;
      }
    } catch (e) {
      console.error(`[ERROR] ${t.host}: ${e.message}`);
      failed++;
    }
  }

  server.close(() => {
    process.exit(failed > 0 ? 1 : 0);
  });
});
