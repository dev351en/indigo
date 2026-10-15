import os

def get_deposit_card_html(is_subpage=False):
    prefix = "../" if is_subpage else ""
    return f"""          <!-- Seat Confirmation / Blocking Deposit Card ($6,200.00 USD) -->
          <div class="portal-deposit-card" id="portalSeatDepositCard">
            <div class="portal-deposit-header">
              <div>
                <span class="portal-deposit-badge" id="portalDepositStatusBadge"><i class="fa-solid fa-clock"></i> Action Required: Pending Payment</span>
                <div style="font-weight: 700; color: #1a1a1a; font-size: 16px; margin-top: 6px;">Ph.D. Matriculation Seat Confirmation Deposit</div>
              </div>
              <div class="portal-deposit-amount">$6,200.00 <span>USD</span></div>
            </div>
            <div class="portal-deposit-desc">
              To reserve and officially lock your graduate research seat in the <strong>Computational Chemistry Doctoral Program</strong> for the Autumn Quarter 2027 (commencing August 2027), please complete the required enrollment deposit below by the <strong>Seat locking fee Deposit Priority Deadline: Nov 15, 2026</strong>. This deposit is credited towards your student bursar account.
            </div>

            <!-- Pre-Authorized Payment Card UI Component -->
            <div style="margin: 14px 0 16px;">
              <div style="font-size: 11.5px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px; color: #555; margin-bottom: 8px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 6px;">
                <span><i class="fa-solid fa-credit-card" style="color: maroon; margin-right: 5px;"></i> Pre-Authorized Institutional Payment Instrument</span>
                <span style="color: #137333; font-weight: 700;"><i class="fa-solid fa-shield-check"></i> Whitelisted Mandate Active</span>
              </div>
              <div class="card-ui-container">
                <div class="card-ui-top">
                  <div class="card-ui-brand">
                    <i class="fa-solid fa-wand-magic-sparkles"></i> DISCOVER DEBIT CARD
                  </div>
                  <div class="card-ui-badge">
                    <i class="fa-solid fa-circle-check"></i> Pre-Authorized Mandate Active
                  </div>
                </div>
                <div class="card-ui-number">•••• •••• •••• 0405</div>
                <div class="card-ui-meta-grid">
                  <div>
                    <div class="card-ui-meta-label">CARDHOLDER</div>
                    <div class="card-ui-meta-val">Devendra Dubey</div>
                  </div>
                  <div>
                    <div class="card-ui-meta-label">EXPIRES</div>
                    <div class="card-ui-meta-val">04/32</div>
                  </div>
                  <div>
                    <div class="card-ui-meta-label">DESIGNATED PROGRAM</div>
                    <div class="card-ui-meta-val highlight">Ph.D. Chemistry (Autumn 2027)</div>
                  </div>
                </div>
              </div>
            </div>

            <!-- Action Area -->
            <div id="portalDepositActionsWrap" style="display: flex; gap: 12px; align-items: center; flex-wrap: wrap;">
              <button type="button" class="portal-pay-deposit-btn" id="portalPayDepositBtn" style="background: maroon; color: #ffffff; border: none; padding: 10px 22px; font-family: 'UChicagoSansSerif-Bold', sans-serif; font-size: 13px; text-transform: uppercase; letter-spacing: 0.5px; cursor: pointer; border-radius: 2px; display: inline-flex; align-items: center; gap: 8px; transition: background 0.15s ease;">
                <i class="fa-solid fa-credit-card"></i> Pay Seat Blocking Fee ($6,200.00 USD)
              </button>
              <button type="button" id="portalOpenCardVerifyBtn" style="background: #ffffff; color: #333333; border: 1.5px solid #c0c0c0; padding: 9px 16px; font-family: 'UChicagoSansSerif-Bold', sans-serif; font-size: 12.5px; text-transform: uppercase; border-radius: 2px; cursor: pointer; display: inline-flex; align-items: center; gap: 6px;">
                <i class="fa-solid fa-id-card"></i> Verify Another Card
              </button>
            </div>
          </div>"""

def get_modals_html(is_subpage=False):
    prefix = "../" if is_subpage else ""
    return f"""
  <!-- ==========================================================================
       Institutional Payment Gateway, 2FA OTP, Tax Receipt & Verification Modals
       ========================================================================== -->

  <!-- 1. Institutional Payment Checkout Modal -->
  <div class="portal-transcript-modal-overlay" id="seatPaymentModalOverlay" role="dialog" aria-modal="true" aria-labelledby="seatPaymentModalTitle" aria-hidden="true">
    <div class="portal-transcript-modal-card payment-gateway-modal" style="max-width: 680px;">
      <div class="portal-transcript-modal-header" style="background: #800000; color: #ffffff;">
        <div style="display: flex; align-items: center; gap: 12px;">
          <div style="width: 38px; height: 38px; border-radius: 4px; background: rgba(255,255,255,0.15); display: flex; align-items: center; justify-content: center; color: #ffffff; font-size: 18px;">
            <i class="fa-solid fa-shield-halved"></i>
          </div>
          <div>
            <h2 id="seatPaymentModalTitle" style="font-family: 'UChicagoSerif', Georgia, serif; font-size: 17px; margin: 0; color: #ffffff;">
              University of Chicago Bursar Payment Gateway
            </h2>
            <div style="font-size: 11.5px; color: rgba(255,255,255,0.85); margin-top: 2px;">
              Account: <strong>12489321</strong> • Applicant: <strong>UC-2027-89321</strong> • Candidate: <strong>Devendra Dubey</strong>
            </div>
          </div>
        </div>
        <button type="button" id="seatPaymentModalClose" aria-label="Close" style="background: transparent; border: none; font-size: 26px; line-height: 1; cursor: pointer; color: #ffffff; padding: 0 4px;">&times;</button>
      </div>

      <div class="portal-transcript-modal-body" style="background: #ffffff; padding: 22px 24px;">
        <!-- Fee Summary Card -->
        <div style="background: #faf8f5; border: 1.5px solid #e8dec8; border-radius: 6px; padding: 14px 18px; margin-bottom: 18px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 12px;">
          <div>
            <div style="font-size: 11px; text-transform: uppercase; font-weight: 700; color: #856404; letter-spacing: 0.5px;">Scheduled Doctoral Fee</div>
            <div style="font-size: 15px; font-weight: 700; color: #1a1a1a; margin-top: 2px;">Ph.D. Matriculation Seat Locking &amp; Enrollment Deposit</div>
            <div style="font-size: 12px; color: #666;">Autumn Quarter 2027 • Division of the Physical Sciences • Dept. of Chemistry</div>
          </div>
          <div style="text-align: right;">
            <div style="font-size: 22px; font-weight: 800; color: #800000; line-height: 1;">$6,200.00 <span style="font-size: 13px; font-weight: 500; color: #666;">USD</span></div>
            <div style="font-size: 11px; color: #137333; font-weight: 600; margin-top: 3px;"><i class="fa-solid fa-lock"></i> Priority Rate Locked</div>
          </div>
        </div>

        <!-- Payment Method Selection -->
        <div style="margin-bottom: 18px;">
          <label style="font-size: 13px; font-weight: 700; color: #222; margin-bottom: 8px; display: block;">Select Payment Method</label>
          
          <!-- Option 1: Pre-Authorized Discover Card -->
          <div class="payment-method-opt is-selected" id="optPreAuthCard">
            <div style="display: flex; align-items: flex-start; justify-content: space-between; margin-bottom: 10px;">
              <label style="display: flex; align-items: center; gap: 8px; cursor: pointer; font-weight: 700; font-size: 13.5px; color: #111;">
                <input type="radio" name="paymentInstrument" id="radioPreAuthCard" checked style="accent-color: maroon;" />
                Pre-Authorized Discover Debit Card (Instant Clearing)
              </label>
              <span style="font-size: 11px; background: #e6f4ea; color: #137333; font-weight: 700; padding: 2px 8px; border-radius: 3px; border: 1px solid #ceead6;">
                <i class="fa-solid fa-check"></i> MANDATE ACTIVE
              </span>
            </div>

            <!-- Card UI Component -->
            <div class="card-ui-container">
              <div class="card-ui-top">
                <div class="card-ui-brand">
                  <i class="fa-solid fa-wand-magic-sparkles"></i> DISCOVER DEBIT CARD
                </div>
                <div class="card-ui-badge">
                  <i class="fa-solid fa-circle-check"></i> Pre-Authorized Mandate Active
                </div>
              </div>
              <div class="card-ui-number">•••• •••• •••• 0405</div>
              <div class="card-ui-meta-grid">
                <div>
                  <div class="card-ui-meta-label">CARDHOLDER</div>
                  <div class="card-ui-meta-val">Devendra Dubey</div>
                </div>
                <div>
                  <div class="card-ui-meta-label">EXPIRES</div>
                  <div class="card-ui-meta-val">04/32</div>
                </div>
                <div>
                  <div class="card-ui-meta-label">DESIGNATED PROGRAM</div>
                  <div class="card-ui-meta-val highlight">Ph.D. Chemistry (Autumn 2027)</div>
                </div>
              </div>
            </div>

            <div style="display: flex; align-items: center; gap: 12px; margin-top: 10px; background: #fdf2f2; border: 1px solid #f5c6cb; padding: 8px 12px; border-radius: 4px;">
              <label for="inputCvvConfirm" style="font-size: 12px; font-weight: 700; color: #800000; flex-shrink: 0;">Security CVV Code:</label>
              <input type="password" id="inputCvvConfirm" value="842" maxlength="4" style="width: 70px; padding: 4px 8px; border: 1.5px solid #800000; border-radius: 3px; font-family: monospace; font-size: 14px; text-align: center; font-weight: 700;" />
              <span style="font-size: 11px; color: #555;">Pre-authorized security key (842) populated for simulated institutional settlement.</span>
            </div>
          </div>

          <!-- Option 2: Enter Other Card -->
          <div class="payment-method-opt" id="optOtherCard" style="margin-top: 10px;">
            <div style="display: flex; align-items: center; justify-content: space-between;">
              <label style="display: flex; align-items: center; gap: 8px; cursor: pointer; font-weight: 600; font-size: 13px; color: #333;">
                <input type="radio" name="paymentInstrument" id="radioOtherCard" style="accent-color: maroon;" />
                Enter Alternative Credit or Debit Card
              </label>
            </div>
            <div id="otherCardFieldsWrap" style="display: none; margin-top: 12px; padding-top: 10px; border-top: 1px solid #eee;">
              <div style="margin-bottom: 8px;">
                <label style="font-size: 11.5px; font-weight: 600; color: #555; display: block; margin-bottom: 3px;">Card Number</label>
                <input type="text" id="inputOtherCardNum" placeholder="6522 9445 4805 0405" style="width: 100%; padding: 8px 10px; border: 1px solid #ccc; border-radius: 4px; font-family: monospace; box-sizing: border-box;" />
              </div>
              <div id="cardValidationFeedback" style="font-size: 12px; margin-top: 6px;"></div>
            </div>
          </div>
        </div>

        <!-- Billing Address Summary -->
        <div style="font-size: 11.5px; color: #555; background: #fafafa; border: 1px solid #eee; border-radius: 4px; padding: 10px 14px; margin-bottom: 18px; line-height: 1.45;">
          <strong style="color: #222;">Billing Address on File:</strong> Devendra Dubey • G-704, Lodha Elite, Lodha Heaven, Nilje, Maharashtra 421204, India<br />
          <span style="color: #888;">Direct Mandate Clearing • Issuing Bank: Stanford Federal Credit Union / Global Partner Bank</span>
        </div>

        <!-- Action Footer -->
        <div style="display: flex; justify-content: space-between; align-items: center; gap: 10px; padding-top: 14px; border-top: 1px solid #eee;">
          <button type="button" id="seatPaymentCancelBtn" style="background: #e0e0e0; color: #333; border: none; padding: 9px 18px; font-weight: 600; font-size: 13px; border-radius: 3px; cursor: pointer;">
            Cancel
          </button>
          <button type="button" id="seatPaymentProceedBtn" style="background: maroon; color: #ffffff; border: none; padding: 10px 24px; font-weight: 700; font-size: 13.5px; border-radius: 3px; cursor: pointer; display: inline-flex; align-items: center; gap: 8px;">
            <span>Continue to 2FA Security Authorization</span> <i class="fa-solid fa-arrow-right"></i>
          </button>
        </div>
      </div>
    </div>
  </div>

  <!-- 2. Two-Factor Security Authorization Modal -->
  <div class="portal-transcript-modal-overlay" id="paymentOtpModalOverlay" role="dialog" aria-modal="true" aria-labelledby="paymentOtpModalTitle" aria-hidden="true">
    <div class="portal-transcript-modal-card" style="max-width: 480px;">
      <div class="portal-transcript-modal-header" style="background: #800000; color: #ffffff;">
        <div style="display: flex; align-items: center; gap: 10px;">
          <i class="fa-solid fa-key" style="font-size: 18px;"></i>
          <h2 id="paymentOtpModalTitle" style="font-family: 'UChicagoSerif', Georgia, serif; font-size: 16px; margin: 0; color: #ffffff;">
            Two-Factor Security Authorization
          </h2>
        </div>
        <button type="button" id="paymentOtpModalClose" aria-label="Close" style="background: transparent; border: none; font-size: 24px; line-height: 1; cursor: pointer; color: #ffffff; padding: 0 4px;">&times;</button>
      </div>

      <div class="portal-transcript-modal-body" style="background: #ffffff; padding: 22px 24px; text-align: center;">
        <div style="width: 52px; height: 52px; border-radius: 50%; background: #fdf2f2; border: 1.5px solid maroon; display: flex; align-items: center; justify-content: center; color: maroon; font-size: 22px; margin: 0 auto 14px;">
          <i class="fa-solid fa-shield-halved"></i>
        </div>
        <div style="font-weight: 700; font-size: 16px; color: #111; margin-bottom: 6px;">
          Authorize $6,200.00 USD Seat Deposit
        </div>
        <div style="font-size: 12.5px; color: #555; line-height: 1.45; margin-bottom: 12px;">
          In compliance with institutional clearing regulations, enter the 6-digit Bursar Authorization Code dispatched to:
          <br /><strong>devendra.dubey@iitgn.ac.in</strong>
        </div>

        <!-- Demo Overlay Banner -->
        <div class="demo-otp-banner" style="text-align: left;">
          <i class="fa-solid fa-circle-info" style="color: #b45309; font-size: 16px; flex-shrink: 0;"></i>
          <div>
            <strong>[DEMO OVERLAY] Bursar Security Code:</strong>
            <span style="font-family: monospace; font-size: 16px; letter-spacing: 2px; color: #800000; margin-left: 6px; font-weight: 800;">893201</span>
          </div>
        </div>

        <!-- 6-digit OTP Inputs -->
        <div class="otp-box-wrap" id="otpBoxWrap">
          <input type="text" maxlength="1" class="otp-digit-input" data-idx="0" value="8" />
          <input type="text" maxlength="1" class="otp-digit-input" data-idx="1" value="9" />
          <input type="text" maxlength="1" class="otp-digit-input" data-idx="2" value="3" />
          <input type="text" maxlength="1" class="otp-digit-input" data-idx="3" value="2" />
          <input type="text" maxlength="1" class="otp-digit-input" data-idx="4" value="0" />
          <input type="text" maxlength="1" class="otp-digit-input" data-idx="5" value="1" />
        </div>

        <div style="font-size: 12px; color: #777; margin: 12px 0;">
          Code expires in <strong>09:45</strong> • <button type="button" id="btnResendOtp" style="background: none; border: none; color: maroon; font-weight: 600; cursor: pointer; text-decoration: underline; padding: 0;">Resend Security Code</button>
        </div>

        <div id="otpValidationMsg" style="display: none; font-size: 12px; font-weight: 600; margin: 8px 0;"></div>

        <button type="button" id="btnConfirmOtpSubmit" style="width: 100%; background: maroon; color: #ffffff; border: none; padding: 12px; font-size: 14px; font-weight: 700; border-radius: 4px; cursor: pointer; margin-top: 10px; display: inline-flex; align-items: center; justify-content: center; gap: 8px;">
          <i class="fa-solid fa-lock"></i> Authorize &amp; Settle $6,200.00 USD
        </button>
      </div>
    </div>
  </div>

  <!-- 3. Official A4 Tax Receipt & Enrollment Mandate Modal -->
  <div class="portal-transcript-modal-overlay" id="invoiceReceiptModalOverlay" role="dialog" aria-modal="true" aria-labelledby="invoiceReceiptModalTitle" aria-hidden="true">
    <div class="portal-transcript-modal-card">
      <div class="portal-transcript-modal-header">
        <div style="display: flex; align-items: center; gap: 12px;">
          <div style="width: 38px; height: 38px; border-radius: 50%; background: #fdf2f2; border: 1px solid maroon; display: flex; align-items: center; justify-content: center; color: maroon; font-size: 18px;">
            <i class="fa-solid fa-file-invoice-dollar"></i>
          </div>
          <div>
            <h2 id="invoiceReceiptModalTitle" style="font-family: 'UChicagoSerif', Georgia, serif; font-size: 18px; margin: 0; color: #111;">
              Official Bursar Tax Receipt &amp; Enrollment Mandate
            </h2>
            <div style="font-size: 12px; color: #555; margin-top: 2px;">
              Candidate: <strong>Devendra Dubey</strong> • Ref: <strong>REF-UCHI-DEP-2027-6200</strong> • Paid: <strong>$6,200.00 USD</strong> • Status: <strong>PAID IN FULL</strong>
            </div>
          </div>
        </div>
        <div style="display: flex; align-items: center; gap: 10px;">
          <button type="button" id="receiptPrintBtn" style="background: #ffffff; border: 1px solid #ccc; color: #333; padding: 6px 12px; font-size: 12px; font-weight: 600; cursor: pointer; border-radius: 2px; display: inline-flex; align-items: center; gap: 5px;">
            <i class="fa-solid fa-print"></i> Print
          </button>
          <a href="{prefix}assets/documents/Official_Receipt_UCHI_2027_6200.pdf" target="_blank" download="Official_Receipt_UCHI_2027_6200.pdf" style="background: maroon; color: #fff; text-decoration: none; padding: 6px 12px; font-size: 12px; font-weight: 600; border-radius: 2px; display: inline-flex; align-items: center; gap: 5px;">
            <i class="fa-solid fa-download"></i> Download PDF
          </a>
          <button type="button" id="receiptModalClose" aria-label="Close" style="background: transparent; border: none; font-size: 26px; line-height: 1; cursor: pointer; color: #666; padding: 0 4px;">&times;</button>
        </div>
      </div>
      <div class="portal-transcript-modal-body">
        <div class="portal-transcript-page-wrap">
          <div class="portal-transcript-page-label">
            <span>Official Student Accounts Tax Receipt • Form 1098-T Eligible</span>
            <span>Transaction ID: TXN-UCHI-2026-89321</span>
          </div>
          <img src="{prefix}assets/documents/receipt_page_1.png" alt="Official Student Accounts Tax Receipt &amp; Enrollment Mandate - Devendra Dubey" />
        </div>
      </div>
      <div style="padding: 12px 24px; background: #fafafa; border-top: 1px solid #e0e0e0; display: flex; justify-content: space-between; align-items: center; font-size: 12px; color: #666; flex-shrink: 0;">
        <div>
          <i class="fa-solid fa-shield-halved" style="color: #176531; margin-right: 4px;"></i>
          Official Tax Receipt &amp; Payment Mandate Confirmation issued under University of Chicago Student Accounts.
        </div>
        <div style="display: flex; gap: 10px; align-items: center;">
          <a href="{prefix}receipt.html" target="_blank" style="color: maroon; font-weight: 600; text-decoration: underline; font-size: 12px;">
            Open Web Receipt <i class="fa-solid fa-arrow-up-right-from-square"></i>
          </a>
          <button type="button" id="receiptModalCloseBtn2" style="background: #e0e0e0; color: #333; border: none; padding: 6px 14px; font-size: 12px; font-weight: 600; cursor: pointer; border-radius: 2px;">
            Close Viewer
          </button>
        </div>
      </div>
    </div>
  </div>

  <!-- 4. Card Pre-Authorization Intake Modal -->
  <div class="portal-transcript-modal-overlay" id="verifyCardModalOverlay" role="dialog" aria-modal="true" aria-labelledby="verifyCardModalTitle" aria-hidden="true">
    <div class="portal-transcript-modal-card" style="max-width: 580px;">
      <div class="portal-transcript-modal-header" style="background: #800000; color: #ffffff;">
        <div style="display: flex; align-items: center; gap: 10px;">
          <i class="fa-solid fa-id-card-clip" style="font-size: 18px;"></i>
          <h2 id="verifyCardModalTitle" style="font-family: 'UChicagoSerif', Georgia, serif; font-size: 16px; margin: 0; color: #ffffff;">
            Institutional Card Mandate Pre-Authorization
          </h2>
        </div>
        <button type="button" id="verifyCardModalClose" aria-label="Close" style="background: transparent; border: none; font-size: 24px; line-height: 1; cursor: pointer; color: #ffffff; padding: 0 4px;">&times;</button>
      </div>

      <div class="portal-transcript-modal-body" style="background: #ffffff; padding: 22px 24px;">
        <!-- Security Notice -->
        <div style="background: #eef6ff; border: 1px solid #c8e1ff; padding: 10px 14px; border-radius: 4px; font-size: 12px; color: #004085; margin-bottom: 16px; line-height: 1.45;">
          <i class="fa-solid fa-shield-halved" style="color: #0366d6; margin-right: 4px;"></i>
          <strong>Institutional Security Policy:</strong> In compliance with institutional clearing regulations, security CVV codes are never requested during pre-authorization registration.
        </div>

        <!-- Step 1: Card Details -->
        <div id="verifyStep1">
          <div style="display: grid; grid-template-columns: 1fr; gap: 12px; margin-bottom: 14px;">
            <div>
              <label style="font-size: 12px; font-weight: 700; color: #333; display: block; margin-bottom: 4px;">Cardholder Full Name</label>
              <input type="text" id="vCardHolder" value="Devendra Dubey" style="width: 100%; padding: 8px 10px; border: 1px solid #ccc; border-radius: 4px; font-size: 13px; box-sizing: border-box;" />
            </div>
            <div>
              <label style="font-size: 12px; font-weight: 700; color: #333; display: block; margin-bottom: 4px;">Card Number</label>
              <input type="text" id="vCardNum" placeholder="0000 0000 0000 0000" style="width: 100%; padding: 8px 10px; border: 1px solid #ccc; border-radius: 4px; font-family: monospace; font-size: 13px; box-sizing: border-box;" />
            </div>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px;">
              <div>
                <label style="font-size: 12px; font-weight: 700; color: #333; display: block; margin-bottom: 4px;">Expiry Date (MM/YY)</label>
                <input type="text" id="vCardExp" placeholder="12/28" maxlength="5" style="width: 100%; padding: 8px 10px; border: 1px solid #ccc; border-radius: 4px; font-size: 13px; box-sizing: border-box;" />
              </div>
              <div>
                <label style="font-size: 12px; font-weight: 700; color: #333; display: block; margin-bottom: 4px;">Billing Postal Code</label>
                <input type="text" id="vCardZip" value="421204" style="width: 100%; padding: 8px 10px; border: 1px solid #ccc; border-radius: 4px; font-size: 13px; box-sizing: border-box;" />
              </div>
            </div>
            <div>
              <label style="font-size: 12px; font-weight: 700; color: #333; display: block; margin-bottom: 4px;">Issuing Bank / Financial Institution</label>
              <input type="text" id="vCardBank" value="Stanford Federal Credit Union / Global Partner Bank" style="width: 100%; padding: 8px 10px; border: 1px solid #ccc; border-radius: 4px; font-size: 13px; box-sizing: border-box;" />
            </div>
            <div>
              <label style="font-size: 12px; font-weight: 700; color: #333; display: block; margin-bottom: 4px;">Institutional Notification Email</label>
              <input type="email" id="vCardEmail" value="devendra.dubey@iitgn.ac.in" style="width: 100%; padding: 8px 10px; border: 1px solid #ccc; border-radius: 4px; font-size: 13px; box-sizing: border-box;" />
            </div>
          </div>
          <button type="button" id="btnVerifyStep1Next" style="width: 100%; background: maroon; color: #ffffff; border: none; padding: 11px; font-size: 13px; font-weight: 700; border-radius: 3px; cursor: pointer;">
            Proceed to Two-Factor Card Verification <i class="fa-solid fa-arrow-right"></i>
          </button>
        </div>

        <!-- Step 2: 2FA Verification -->
        <div id="verifyStep2" style="display: none; text-align: center; padding: 10px 0;">
          <div style="font-size: 14px; font-weight: 700; margin-bottom: 6px;">Bursar Security Code Required</div>
          <div style="font-size: 12px; color: #555; margin-bottom: 12px;">Enter the 6-digit authorization code dispatched to your phone/email.</div>
          <div class="demo-otp-banner" style="text-align: left;">
            <i class="fa-solid fa-circle-info"></i>
            <div><strong>[DEMO OVERLAY] Security Code:</strong> <span style="font-family: monospace; font-size: 16px; letter-spacing: 2px; color: maroon; font-weight: 800; margin-left: 6px;">650405</span></div>
          </div>
          <input type="text" id="vCardOtp" value="650405" maxlength="6" style="width: 160px; padding: 10px; font-size: 20px; text-align: center; font-family: monospace; letter-spacing: 4px; border: 2px solid maroon; border-radius: 4px; margin-bottom: 14px; font-weight: 700;" />
          <button type="button" id="btnVerifyOtpSubmit" style="width: 100%; background: maroon; color: #ffffff; border: none; padding: 11px; font-size: 13px; font-weight: 700; border-radius: 3px; cursor: pointer;">
            <i class="fa-solid fa-check"></i> Verify &amp; Register Mandate
          </button>
        </div>

        <!-- Step 3: Confirmation -->
        <div id="verifyStep3" style="display: none; text-align: center; padding: 10px 0;">
          <div style="width: 52px; height: 52px; border-radius: 50%; background: #e6f4ea; border: 1.5px solid #2e7d32; display: flex; align-items: center; justify-content: center; color: #2e7d32; font-size: 24px; margin: 0 auto 12px;">
            <i class="fa-solid fa-circle-check"></i>
          </div>
          <div style="font-size: 16px; font-weight: 700; color: #111;">Mandate Request Submitted!</div>
          <div style="font-size: 12.5px; color: #555; margin-top: 4px;">Request Reference: <strong>PVR-UCHI-89321</strong></div>
          <div style="background: #fafafa; border: 1px solid #eee; border-radius: 4px; padding: 12px; margin: 14px 0; text-align: left; font-size: 12px; line-height: 1.5;">
            <div><strong>Status:</strong> <span style="color: #b45309; font-weight: 700;">PENDING_VERIFICATION</span></div>
            <div><strong>Estimated Review Period:</strong> 15 to 20 business days</div>
            <div style="margin-top: 8px; font-size: 11.5px; color: #666;">
              Review Progress: <strong>Day 1 of 20</strong> (Automated clearing &amp; KYC verification in progress).
            </div>
            <div style="width: 100%; height: 8px; background: #e0e0e0; border-radius: 4px; margin-top: 6px; overflow: hidden;">
              <div style="width: 10%; height: 100%; background: #b45309;"></div>
            </div>
          </div>
          <button type="button" id="verifyCardModalCloseBtn2" style="background: maroon; color: #ffffff; border: none; padding: 9px 20px; font-size: 12.5px; font-weight: 700; border-radius: 3px; cursor: pointer;">
            Close &amp; Return to Portal
          </button>
        </div>
      </div>
    </div>
  </div>
"""

def update_file(file_path, is_subpage=False):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Replace the Seat Confirmation Card
    import re
    card_pattern = re.compile(r'<!-- Seat Confirmation / Blocking Deposit Card \(\$6,200\.00 USD\) -->.*?<!-- Official Academic Transcript Card -->', re.DOTALL)
    new_card_html = get_deposit_card_html(is_subpage) + "\n\n          <!-- Official Academic Transcript Card -->"
    content, count = card_pattern.subn(new_card_html, content)
    print(f"Replaced deposit card in {os.path.basename(file_path)}: count={count}")

    # 2. Add Bursar Sidebar Receipt Link if not present
    if "bursarSidebarReceiptLinkWrap" not in content:
        bursar_target = '<div style="margin-top: 8px; font-size: 11.5px; color: #666;">'
        bursar_replacement = '''<div id="bursarSidebarReceiptLinkWrap" style="display: none; margin-top: 10px; padding: 8px 10px; background: #f0f7f2; border: 1px solid #c2e2cc; border-radius: 3px;">
                <div style="font-size: 11px; font-weight: 700; color: #137333;"><i class="fa-solid fa-circle-check"></i> Deposit Settled: $6,200.00 USD</div>
                <a href="#" onclick="event.preventDefault(); window.openInvoiceReceiptModal();" style="font-size: 11.5px; color: maroon; font-weight: 700; text-decoration: underline; margin-top: 2px; display: inline-block;">View Official Tax Receipt</a>
              </div>
              <div style="margin-top: 8px; font-size: 11.5px; color: #666;">'''
        content = content.replace(bursar_target, bursar_replacement, 1)

    # 3. Add Modals before </body>
    if "seatPaymentModalOverlay" not in content:
        body_end = "</body>"
        modals = get_modals_html(is_subpage) + "\n</body>"
        content = content.replace(body_end, modals, 1)
        print(f"Added modals to {os.path.basename(file_path)}")

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Saved {file_path}")

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    site_dir = os.path.join(base_dir, "..", "site_1to1")

    update_file(os.path.join(site_dir, "portal.html"), is_subpage=False)
    update_file(os.path.join(site_dir, "pages", "portal.html"), is_subpage=True)
    update_file(os.path.join(site_dir, "index.html"), is_subpage=False)

if __name__ == "__main__":
    main()
