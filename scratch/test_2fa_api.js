const http = require('http');

function post(path, data) {
  return new Promise((resolve, reject) => {
    const payload = JSON.stringify(data);
    const req = http.request({
      hostname: 'localhost',
      port: 3000,
      path,
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Content-Length': Buffer.byteLength(payload)
      }
    }, res => {
      let body = '';
      res.on('data', chunk => body += chunk);
      res.on('end', () => {
        try {
          resolve({ status: res.statusCode, data: JSON.parse(body) });
        } catch (e) {
          resolve({ status: res.statusCode, raw: body });
        }
      });
    });
    req.on('error', reject);
    req.write(payload);
    req.end();
  });
}

async function run() {
  console.log('Testing 1: POST /api/payment/create');
  const createRes = await post('/api/payment/create', {
    cardLast4: '0405',
    amount: 6200,
    email: 'dubey351dev@gmail.com',
    applicantId: 'UC-2027-89321',
    studentName: 'Devendra Dubey'
  });
  console.log('Create Response:', JSON.stringify(createRes, null, 2));

  const txnId = createRes.data.transactionId;
  const code = createRes.data.demoSecurityCode || '893201';

  console.log('\nTesting 2: POST /api/payment/confirm-otp with code:', code);
  const confirmRes = await post('/api/payment/confirm-otp', {
    transactionId: txnId,
    otp: code
  });
  console.log('Confirm Response:', JSON.stringify(confirmRes, null, 2));

  console.log('\nTesting 3: POST /api/payment/resend-otp');
  const resendRes = await post('/api/payment/resend-otp', {
    transactionId: txnId,
    email: 'dubey351dev@gmail.com'
  });
  console.log('Resend Response:', JSON.stringify(resendRes, null, 2));
}

run().catch(console.error);
