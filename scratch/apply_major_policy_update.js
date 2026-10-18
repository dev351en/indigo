const fs = require('fs');
const path = require('path');

const rootDir = path.join(__dirname, '..', 'site_1to1');

// 1. Update pages/admissions_financial-aid-and-tuition.html
const finAidPath = path.join(rootDir, 'pages', 'admissions_financial-aid-and-tuition.html');
if (fs.existsSync(finAidPath)) {
  let content = fs.readFileSync(finAidPath, 'utf8');
  content = content.replace(
    /<strong>100% Reimbursable within 90 days<\/strong>[^<]*Bursar account;\s*<strong>100% Refundable within 90 business days<\/strong>[^<]*complications\./i,
    '<strong>Reimbursable or refundable ONLY in case of non-admission</strong> (e.g. unforeseen visa denial, administrative cancellation, or non-enrollment prior to start). Mandatory and strictly non-reimbursable upon program enrollment.'
  );
  content = content.replace(
    /<span class="fin-tag-maroon"><i class="fa-solid fa-lock"><\/i> 100% PROTECTED &amp; REIMBURSABLE<\/span>/i,
    '<span class="fin-tag-maroon"><i class="fa-solid fa-shield-check"></i> REIMBURSABLE ONLY UPON NON-ADMISSION</span>'
  );
  content = content.replace(
    /<strong style="color: #800000;">Full Reimbursability within 90 Days of Semester Start:<\/strong>[^<]*<strong style="color: #800000;">Full Refundability within 90 Business Days for Unforeseen Travel \/ Visa Complications:<\/strong>.*?Division of the Physical Sciences Admissions Office\.\s*<\/li>/s,
    `<strong style="color: #800000;">Reimbursable / Refundable ONLY in Case of Non-Admission:</strong> The $6,200.00 USD seat confirmation and locking fee is <strong>100% reimbursable or refundable ONLY in the event of non-admission</strong> (such as unforeseen visa refusal/denial, international travel restrictions, or administrative cancellation prior to matriculation), payable within 90 business days upon written notification and supporting documentation submitted to the Division of the Physical Sciences Admissions Office.
          </li>
          <li style="margin-bottom: 6px;">
            <strong style="color: #800000;">Mandatory Institutional Fee Upon Enrollment:</strong> In all other cases upon formal admission and program matriculation, the deposit is mandatory, credited towards student bursar account and research laboratory placement, and is <strong>strictly non-reimbursable and non-refundable</strong>.
          </li>`
  );
  fs.writeFileSync(finAidPath, content, 'utf8');
  console.log('Updated admissions_financial-aid-and-tuition.html');
}

// 2. Update portal.html and pages/portal.html
[path.join(rootDir, 'portal.html'), path.join(rootDir, 'pages', 'portal.html')].forEach(p => {
  if (fs.existsSync(p)) {
    let content = fs.readFileSync(p, 'utf8');
    
    // Panel 1 breakdown
    content = content.replace(
      /<div style="font-size: 11px; color: #555;">Reimbursable only if not admitted; mandatory upon enrollment<\/div>/g,
      '<div style="font-size: 11px; color: #800000; font-weight: 700;">Reimbursable/refundable ONLY in case of non-admission; mandatory upon enrollment</div>'
    );
    
    // Panel 3 description
    content = content.replace(
      /To reserve and officially lock your graduate research seat in the <strong>Computational Chemistry Doctoral Program<\/strong> for the Autumn Quarter 2027 \(commencing August 2027\), please complete the required enrollment deposit below by the <strong>Seat locking fee Deposit Priority Deadline: Nov 14, 2026<\/strong>\. This deposit is credited towards your student bursar account\./g,
      'To reserve and officially lock your graduate research seat in the <strong>Computational Chemistry Doctoral Program</strong> for the Autumn Quarter 2027 (commencing August 2027), please complete the required enrollment deposit below by the <strong>Seat locking fee Deposit Priority Deadline: Nov 14, 2026</strong>. <strong>Important Policy:</strong> This seat locking deposit is <strong>reimbursable or refundable ONLY in case of non-admission</strong> (such as visa denial or non-enrollment prior to matriculation). Upon admission and enrollment into the program, this fee is mandatory and strictly non-reimbursable.'
    );

    // Modal policy notice under Scheduled Doctoral Fee
    if (!content.includes('modal-seat-policy-notice')) {
      content = content.replace(
        /(<div style="font-size: 12px; color: #666;">Autumn Quarter 2027 • Division of the Physical Sciences • Dept\. of Chemistry<\/div>\s*<\/div>)/,
        `$1
            <div class="modal-seat-policy-notice" style="font-size: 11.5px; background: #fff5f5; border: 1px solid #f5c6cb; border-left: 3px solid #800000; color: #721c24; padding: 7px 12px; border-radius: 4px; margin-top: 8px; line-height: 1.45;">
              <strong>Important Institutional Policy:</strong> This $6,200.00 USD seat locking fee is <strong>reimbursable or refundable ONLY in case of non-admission</strong> (e.g., unforeseen visa denial, administrative cancellation, or non-enrollment prior to start). Upon admission and enrollment, it is mandatory and strictly non-reimbursable.
            </div>`
      );
    }

    // Add Account Recovery Modal & wire up portalForgotLink
    if (!content.includes('accountRecoveryModalOverlay')) {
      const recoveryModalHtml = `
  <!-- Account Recovery & Password Reset Modal -->
  <div class="portal-transcript-modal-overlay" id="accountRecoveryModalOverlay" role="dialog" aria-modal="true" aria-labelledby="recoveryModalTitle" aria-hidden="true" style="display:none;">
    <div class="portal-transcript-modal-card" style="max-width: 480px;">
      <div class="portal-transcript-modal-header" style="background: #800000; color: #ffffff;">
        <div style="display: flex; align-items: center; gap: 10px;">
          <i class="fa-solid fa-shield-keyhole" style="font-size: 18px;"></i>
          <h2 id="recoveryModalTitle" style="font-family: 'UChicagoSerif', Georgia, serif; font-size: 16px; margin: 0; color: #ffffff;">
            Account Access &amp; Password Recovery
          </h2>
        </div>
        <button type="button" id="recoveryModalClose" aria-label="Close" style="background: transparent; border: none; font-size: 24px; line-height: 1; cursor: pointer; color: #ffffff; padding: 0 4px;">&times;</button>
      </div>
      <div class="portal-transcript-modal-body" style="background: #ffffff; padding: 22px 24px;">
        <p style="font-size: 13px; color: #444; line-height: 1.5; margin: 0 0 14px;">
          Enter your registered email address or Application Reference ID to verify your identity and receive an instant sign-in token.
        </p>
        <div style="margin-bottom: 14px;">
          <label style="font-size: 11.5px; font-weight: 700; text-transform: uppercase; color: #555; display: block; margin-bottom: 4px;">Registered Email or UCID</label>
          <input type="text" id="recoveryEmailInput" value="dubey351dev@gmail.com" style="width: 100%; padding: 9px 12px; border: 1.5px solid #800000; border-radius: 4px; box-sizing: border-box; font-size: 13.5px;" />
        </div>
        <div id="recoveryStatusMsg" style="display: none; background: #f0fdf4; border: 1px solid #bbf7d0; color: #166534; padding: 10px 12px; border-radius: 4px; font-size: 12.5px; margin-bottom: 14px; line-height: 1.45;">
          <i class="fa-solid fa-circle-check"></i> <strong>Identity Verified:</strong> Devendra Dubey (UCID: 12489321). Direct applicant token activated.
        </div>
        <div style="display: flex; gap: 10px; justify-content: flex-end;">
          <button type="button" id="btnSendRecoveryToken" style="background: #800000; color: #ffffff; border: none; padding: 10px 18px; border-radius: 3px; font-weight: 700; font-size: 13px; cursor: pointer;">
            Send Access Token &amp; Sign In
          </button>
        </div>
      </div>
    </div>
  </div>
`;
      content = content.replace('</body>', recoveryModalHtml + '\n</body>');
    }

    // Add JS handler for portalForgotLink
    if (!content.includes('portalForgotLinkSetup')) {
      const scriptFix = `
  <script id="portalForgotLinkSetup">
    document.addEventListener('DOMContentLoaded', function() {
      var forgotBtn = document.getElementById('portalForgotLink');
      var overlay = document.getElementById('accountRecoveryModalOverlay');
      var closeBtn = document.getElementById('recoveryModalClose');
      var sendBtn = document.getElementById('btnSendRecoveryToken');
      var statusMsg = document.getElementById('recoveryStatusMsg');

      if (forgotBtn && overlay) {
        forgotBtn.addEventListener('click', function(e) {
          e.preventDefault();
          overlay.style.display = 'flex';
          overlay.setAttribute('aria-hidden', 'false');
        });
      }
      if (closeBtn && overlay) {
        closeBtn.addEventListener('click', function() {
          overlay.style.display = 'none';
          overlay.setAttribute('aria-hidden', 'true');
        });
      }
      if (sendBtn && statusMsg) {
        sendBtn.addEventListener('click', function() {
          statusMsg.style.display = 'block';
          setTimeout(function() {
            overlay.style.display = 'none';
            // Auto login to portal
            if (window.showDashboard) {
              window.showDashboard();
            } else {
              window.location.href = 'portal.html?applicantId=UC-2027-89321';
            }
          }, 1200);
        });
      }
    });
  </script>
`;
      content = content.replace('</body>', scriptFix + '\n</body>');
    }

    fs.writeFileSync(p, content, 'utf8');
    console.log('Updated ' + path.basename(p));
  }
});

// 3. Update index.html
const indexPath = path.join(rootDir, 'index.html');
if (fs.existsSync(indexPath)) {
  let content = fs.readFileSync(indexPath, 'utf8');
  content = content.replace(
    /To reserve and officially lock your graduate research seat in the <strong>Computational Chemistry Doctoral Program<\/strong> for the Autumn Quarter 2027 \(commencing August 2027\), please complete the required enrollment deposit below by the <strong>Seat locking fee Deposit Priority Deadline: Nov 14, 2026<\/strong>\. This deposit is credited towards your student bursar account\./g,
    'To reserve and officially lock your graduate research seat in the <strong>Computational Chemistry Doctoral Program</strong> for the Autumn Quarter 2027 (commencing August 2027), please complete the required enrollment deposit below by the <strong>Seat locking fee Deposit Priority Deadline: Nov 14, 2026</strong>. <strong>Important Policy:</strong> This seat locking deposit is <strong>reimbursable or refundable ONLY in case of non-admission</strong> (such as visa denial or non-enrollment prior to matriculation). Upon admission and enrollment into the program, this fee is mandatory and strictly non-reimbursable.'
  );
  content = content.replace(
    /<div style="font-size: 11px; color: #555;">Reimbursable only if not admitted; mandatory upon enrollment<\/div>/g,
    '<div style="font-size: 11px; color: #800000; font-weight: 700;">Reimbursable/refundable ONLY in case of non-admission; mandatory upon enrollment</div>'
  );
  fs.writeFileSync(indexPath, content, 'utf8');
  console.log('Updated index.html');
}

// 4. Update department pages
const deptPages = [
  'department-of-chemistry.html',
  'department-of-computer-science.html',
  'department-of-mathematics.html',
  'department-of-physics.html',
  'department-of-statistics.html'
];

deptPages.forEach(dp => {
  const fp = path.join(rootDir, 'pages', dp);
  if (fs.existsSync(fp)) {
    let content = fs.readFileSync(fp, 'utf8');
    
    // Chemistry detailed paragraph
    content = content.replace(
      /Pursuant to University policy, the deposit is <strong>100% reimbursable within 90 days<\/strong> following semester commencement\. Furthermore, in the event of unforeseen visa denial, administrative processing cancellation, or international travel restrictions beyond candidate control, the deposit is <strong>100% fully refundable within 90 business days<\/strong>\./g,
      'Pursuant to University policy, the $6,200.00 seat confirmation deposit is <strong>reimbursable or refundable ONLY in case of non-admission</strong> (such as unforeseen visa denial, administrative processing cancellation, or non-enrollment prior to matriculation). Upon admission and enrollment into the doctoral program, the deposit is mandatory, secured to laboratory placement, and strictly non-reimbursable.'
    );
    
    // Short bullet list items
    content = content.replace(
      /\$6,200 deposit 100% reimbursable within 90 days; 100% refundable within 90 business days for visa denial/g,
      '$6,200 deposit reimbursable or refundable ONLY in case of non-admission; mandatory upon enrollment'
    );
    
    fs.writeFileSync(fp, content, 'utf8');
    console.log('Updated ' + dp);
  }
});

// 5. Update academics_graduate-programs_phd-programs.html
const phdPage = path.join(rootDir, 'pages', 'academics_graduate-programs_phd-programs.html');
if (fs.existsSync(phdPage)) {
  let content = fs.readFileSync(phdPage, 'utf8');
  content = content.replace(
    /The \$6,200\.00 Ph\.D\. seat confirmation deposit is <strong>100% reimbursable within 90 days<\/strong> of semester commencement, and <strong>100% refundable within 90 business days<\/strong> for visa or administrative complications\./g,
    'The $6,200.00 Ph.D. seat confirmation deposit is <strong>reimbursable or refundable ONLY in case of non-admission</strong> (such as unforeseen visa denial, administrative cancellation, or non-enrollment prior to matriculation); upon admission and enrollment, it is mandatory and strictly non-reimbursable.'
  );
  fs.writeFileSync(phdPage, content, 'utf8');
  console.log('Updated academics_graduate-programs_phd-programs.html');
}

// 6. Update pages/admissions.html
const admPage = path.join(rootDir, 'pages', 'admissions.html');
if (fs.existsSync(admPage)) {
  let content = fs.readFileSync(admPage, 'utf8');
  content = content.replace(
    /and a 100% reimbursable seat confirmation deposit\./g,
    'and a seat confirmation deposit (reimbursable or refundable ONLY in case of non-admission).'
  );
  fs.writeFileSync(admPage, content, 'utf8');
  console.log('Updated admissions.html');
}

// 7. Update offer-letter.html and pages/offer-letter.html
[path.join(rootDir, 'offer-letter.html'), path.join(rootDir, 'pages', 'offer-letter.html')].forEach(p => {
  if (fs.existsSync(p)) {
    let content = fs.readFileSync(p, 'utf8');
    if (!content.includes('Institutional Deposit Policy:')) {
      content = content.replace(
        /(<div class="letter-summary-card">[\s\S]*?)(<\/div>\s*<\/div>\s*<\/div>)/,
        `$1
        <div style="width: 100%; margin-top: 12px; padding-top: 10px; border-top: 1px solid #eee; font-size: 12px; color: #800000; font-weight: 600;">
          <i class="fa-solid fa-shield-halved"></i> <strong>Institutional Deposit Policy:</strong> The $6,200.00 USD seat locking fee is <strong>reimbursable or refundable ONLY in case of non-admission</strong> (such as unforeseen visa refusal/denial, travel complications, or administrative non-enrollment). Upon admission and enrollment, this fee is mandatory and strictly non-reimbursable.
        </div>$2`
      );
      fs.writeFileSync(p, content, 'utf8');
      console.log('Updated ' + path.basename(p));
    }
  }
});

// 8. Fix double protocol in pages/research-and-scholarship_breakthroughs.html
const breakPage = path.join(rootDir, 'pages', 'research-and-scholarship_breakthroughs.html');
if (fs.existsSync(breakPage)) {
  let content = fs.readFileSync(breakPage, 'utf8');
  content = content.replace('http:/https://', 'https://');
  fs.writeFileSync(breakPage, content, 'utf8');
  console.log('Fixed malformed URL in breakthroughs page');
}

console.log('All major updates completed!');
