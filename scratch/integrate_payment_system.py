import os
import re

def update_files():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    site_dir = os.path.join(base_dir, "..", "site_1to1")

    # 1. Update interactive_runtime.js
    runtime_path = os.path.join(site_dir, "interactive_runtime.js")
    with open(runtime_path, "r", encoding="utf-8") as f:
        runtime_js = f.read()

    # Create the complete Payment, Card UI, 2FA, Receipt, and Card Verification JS logic
    payment_runtime_code = """
  // ==========================================================================
  // Institutional Payment Gateway, Card Verification & A4 Receipt Engine
  // ==========================================================================

  var portalSeatDepositCard = document.getElementById("portalSeatDepositCard");
  var portalPayDepositBtn = document.getElementById("portalPayDepositBtn");
  var portalDepositStatusBadge = document.getElementById("portalDepositStatusBadge");
  var portalDepositReceiptWrap = document.getElementById("portalDepositReceiptWrap");
  var portalOpenCardVerifyBtn = document.getElementById("portalOpenCardVerifyBtn");

  var seatPaymentModalOverlay = document.getElementById("seatPaymentModalOverlay");
  var seatPaymentModalClose = document.getElementById("seatPaymentModalClose");
  var seatPaymentCancelBtn = document.getElementById("seatPaymentCancelBtn");
  var seatPaymentProceedBtn = document.getElementById("seatPaymentProceedBtn");

  var paymentOtpModalOverlay = document.getElementById("paymentOtpModalOverlay");
  var paymentOtpModalClose = document.getElementById("paymentOtpModalClose");
  var btnConfirmOtpSubmit = document.getElementById("btnConfirmOtpSubmit");
  var btnResendOtp = document.getElementById("btnResendOtp");
  var otpValidationMsg = document.getElementById("otpValidationMsg");

  var invoiceReceiptModalOverlay = document.getElementById("invoiceReceiptModalOverlay");
  var receiptModalClose = document.getElementById("receiptModalClose");
  var receiptModalCloseBtn2 = document.getElementById("receiptModalCloseBtn2");
  var receiptPrintBtn = document.getElementById("receiptPrintBtn");

  var verifyCardModalOverlay = document.getElementById("verifyCardModalOverlay");
  var verifyCardModalClose = document.getElementById("verifyCardModalClose");
  var verifyCardModalCloseBtn2 = document.getElementById("verifyCardModalCloseBtn2");
  var verifyCardForm = document.getElementById("verifyCardForm");
  var verifyStep1 = document.getElementById("verifyStep1");
  var verifyStep2 = document.getElementById("verifyStep2");
  var verifyStep3 = document.getElementById("verifyStep3");
  var btnVerifyStep1Next = document.getElementById("btnVerifyStep1Next");
  var btnVerifyOtpSubmit = document.getElementById("btnVerifyOtpSubmit");

  // Radio toggles for payment method
  var radioPreAuthCard = document.getElementById("radioPreAuthCard");
  var radioOtherCard = document.getElementById("radioOtherCard");
  var optPreAuthCard = document.getElementById("optPreAuthCard");
  var optOtherCard = document.getElementById("optOtherCard");
  var otherCardFieldsWrap = document.getElementById("otherCardFieldsWrap");
  var inputOtherCardNum = document.getElementById("inputOtherCardNum");
  var cardValidationFeedback = document.getElementById("cardValidationFeedback");

  function isSeatDepositPaid() {
    return sessionStorage.getItem("seatDepositPaid") === "true";
  }

  function applySeatDepositPaidState() {
    if (portalDepositStatusBadge) {
      portalDepositStatusBadge.className = "portal-deposit-badge is-paid";
      portalDepositStatusBadge.style.background = "#e6f4ea";
      portalDepositStatusBadge.style.color = "#137333";
      portalDepositStatusBadge.style.borderColor = "#ceead6";
      portalDepositStatusBadge.innerHTML = '<i class="fa-solid fa-circle-check"></i> Seat Secured &amp; Deposit Paid ($6,200.00 Received)';
    }

    var depositActionsWrap = document.getElementById("portalDepositActionsWrap");
    if (depositActionsWrap) {
      depositActionsWrap.innerHTML = [
        '<div style="display: flex; gap: 10px; align-items: center; flex-wrap: wrap;">',
        '  <button type="button" class="portal-view-receipt-btn" id="portalViewReceiptBtn" style="background: maroon; color: #ffffff; border: none; padding: 9px 18px; font-family: \'UChicagoSansSerif-Bold\', sans-serif; font-size: 13px; text-transform: uppercase; letter-spacing: 0.5px; cursor: pointer; border-radius: 2px; display: inline-flex; align-items: center; gap: 7px; transition: background 0.15s ease;">',
        '    <i class="fa-solid fa-file-invoice-dollar"></i> View Official Tax Receipt &amp; A4 Invoice',
        '  </button>',
        '  <a href="' + (window.location.pathname.indexOf('/pages/') !== -1 ? '../' : '') + 'assets/documents/Official_Receipt_UCHI_2027_6200.pdf" target="_blank" download="Official_Receipt_UCHI_2027_6200.pdf" style="background: #ffffff; color: #333333; border: 1.5px solid #c0c0c0; padding: 8px 16px; font-family: \'UChicagoSansSerif-Bold\', sans-serif; font-size: 12.5px; text-transform: uppercase; text-decoration: none; border-radius: 2px; display: inline-flex; align-items: center; gap: 6px;">',
        '    <i class="fa-solid fa-download"></i> Download Tax PDF',
        '  </a>',
        '  <a href="' + (window.location.pathname.indexOf('/pages/') !== -1 ? '' : 'pages/') + 'receipt.html" target="_blank" style="font-size: 12.5px; color: maroon; font-weight: 700; text-decoration: none; display: inline-flex; align-items: center; gap: 4px; margin-left: 6px;">',
        '    <i class="fa-solid fa-arrow-up-right-from-square"></i> Web Receipt',
        '  </a>',
        '</div>',
        '<div style="font-size: 12px; color: #137333; margin-top: 10px; display: flex; align-items: center; gap: 6px; font-weight: 600;">',
        '  <i class="fa-solid fa-shield-check"></i> Ref #REF-UCHI-DEP-2027-6200 • Form 1098-T Eligible • Settled via Discover Debit Card (•••• 0405)',
        '</div>'
      ].join("\\n");

      var newReceiptBtn = document.getElementById("portalViewReceiptBtn");
      if (newReceiptBtn) {
        newReceiptBtn.addEventListener("click", function(e) {
          e.preventDefault();
          openInvoiceReceiptModal();
        });
      }
    }

    if (portalDepositReceiptWrap) {
      portalDepositReceiptWrap.style.display = "inline-block";
    }

    // Update Bursar sidebar card
    var bursarSidebarCard = document.getElementById("bursarSidebarReceiptLinkWrap");
    if (bursarSidebarCard) {
      bursarSidebarCard.style.display = "block";
    }
  }

  // --- Modal Open / Close Helpers ---
  function openSeatPaymentModal() {
    if (!seatPaymentModalOverlay) return;
    seatPaymentModalOverlay.classList.add("is-active");
    seatPaymentModalOverlay.setAttribute("aria-hidden", "false");
    document.body.style.overflow = "hidden";
  }

  function closeSeatPaymentModal() {
    if (!seatPaymentModalOverlay) return;
    seatPaymentModalOverlay.classList.remove("is-active");
    seatPaymentModalOverlay.setAttribute("aria-hidden", "true");
    document.body.style.overflow = "";
  }

  function openPaymentOtpModal() {
    if (!paymentOtpModalOverlay) return;
    paymentOtpModalOverlay.classList.add("is-active");
    paymentOtpModalOverlay.setAttribute("aria-hidden", "false");
    document.body.style.overflow = "hidden";
  }

  function closePaymentOtpModal() {
    if (!paymentOtpModalOverlay) return;
    paymentOtpModalOverlay.classList.remove("is-active");
    paymentOtpModalOverlay.setAttribute("aria-hidden", "true");
    document.body.style.overflow = "";
  }

  function openInvoiceReceiptModal() {
    if (!invoiceReceiptModalOverlay) return;
    invoiceReceiptModalOverlay.classList.add("is-active");
    invoiceReceiptModalOverlay.setAttribute("aria-hidden", "false");
    document.body.style.overflow = "hidden";
  }

  function closeInvoiceReceiptModal() {
    if (!invoiceReceiptModalOverlay) return;
    invoiceReceiptModalOverlay.classList.remove("is-active");
    invoiceReceiptModalOverlay.setAttribute("aria-hidden", "true");
    document.body.style.overflow = "";
  }

  function openVerifyCardModal() {
    if (!verifyCardModalOverlay) return;
    verifyCardModalOverlay.classList.add("is-active");
    verifyCardModalOverlay.setAttribute("aria-hidden", "false");
    document.body.style.overflow = "hidden";
  }

  function closeVerifyCardModal() {
    if (!verifyCardModalOverlay) return;
    verifyCardModalOverlay.classList.remove("is-active");
    verifyCardModalOverlay.setAttribute("aria-hidden", "true");
    document.body.style.overflow = "";
  }

  // Check initial state
  if (isSeatDepositPaid()) {
    applySeatDepositPaidState();
  }

  // Event Listeners for Payment Gateway Trigger
  if (portalPayDepositBtn) {
    portalPayDepositBtn.addEventListener("click", function (e) {
      e.preventDefault();
      if (isSeatDepositPaid()) {
        openInvoiceReceiptModal();
      } else {
        openSeatPaymentModal();
      }
    });
  }

  if (portalOpenCardVerifyBtn) {
    portalOpenCardVerifyBtn.addEventListener("click", function (e) {
      e.preventDefault();
      openVerifyCardModal();
    });
  }

  // Payment Modal Close Listeners
  if (seatPaymentModalClose) {
    seatPaymentModalClose.addEventListener("click", closeSeatPaymentModal);
  }
  if (seatPaymentCancelBtn) {
    seatPaymentCancelBtn.addEventListener("click", closeSeatPaymentModal);
  }
  if (seatPaymentModalOverlay) {
    seatPaymentModalOverlay.addEventListener("click", function(e) {
      if (e.target === seatPaymentModalOverlay) closeSeatPaymentModal();
    });
  }

  // Radio Toggles
  if (radioPreAuthCard && radioOtherCard) {
    radioPreAuthCard.addEventListener("change", function() {
      if (radioPreAuthCard.checked) {
        optPreAuthCard.classList.add("is-selected");
        optOtherCard.classList.remove("is-selected");
        if (otherCardFieldsWrap) otherCardFieldsWrap.style.display = "none";
        if (seatPaymentProceedBtn) {
          seatPaymentProceedBtn.disabled = false;
          seatPaymentProceedBtn.style.opacity = "1";
        }
      }
    });

    radioOtherCard.addEventListener("change", function() {
      if (radioOtherCard.checked) {
        optOtherCard.classList.add("is-selected");
        optPreAuthCard.classList.remove("is-selected");
        if (otherCardFieldsWrap) otherCardFieldsWrap.style.display = "block";
        validateOtherCardInput();
      }
    });
  }

  function validateOtherCardInput() {
    if (!inputOtherCardNum) return;
    var raw = inputOtherCardNum.value.replace(/\\D/g, "");
    var isValid = (raw.endsWith("0405") || raw === "6522944548050405" || raw.endsWith("4242"));
    
    if (!raw) {
      if (cardValidationFeedback) {
        cardValidationFeedback.innerHTML = '<span style="color:#666;">Enter a 16-digit card number.</span>';
      }
      if (seatPaymentProceedBtn) {
        seatPaymentProceedBtn.disabled = true;
        seatPaymentProceedBtn.style.opacity = "0.5";
      }
      return;
    }

    if (isValid) {
      if (cardValidationFeedback) {
        cardValidationFeedback.innerHTML = '<span style="color:#137333; font-weight:700;"><i class="fa-solid fa-circle-check"></i> Pre-authorized verified card recognized.</span>';
      }
      if (seatPaymentProceedBtn) {
        seatPaymentProceedBtn.disabled = false;
        seatPaymentProceedBtn.style.opacity = "1";
      }
    } else {
      if (cardValidationFeedback) {
        cardValidationFeedback.innerHTML = [
          '<div style="background:#fff3cd; border:1px solid #ffeeba; color:#856404; padding:8px 12px; border-radius:4px; margin-top:4px;">',
          '  <i class="fa-solid fa-triangle-exclamation"></i> <strong>Card not verified.</strong> It will take 15 to 20 days of verification.',
          '  <button type="button" id="btnLaunchCardVerifyFromAlert" style="margin-left:8px; background:maroon; color:#fff; border:none; padding:3px 9px; border-radius:2px; font-size:11px; cursor:pointer; font-weight:700;">Initiate Pre-Authorization</button>',
          '</div>'
        ].join("");

        var btnLaunch = document.getElementById("btnLaunchCardVerifyFromAlert");
        if (btnLaunch) {
          btnLaunch.addEventListener("click", function() {
            closeSeatPaymentModal();
            openVerifyCardModal();
          });
        }
      }
      if (seatPaymentProceedBtn) {
        seatPaymentProceedBtn.disabled = true;
        seatPaymentProceedBtn.style.opacity = "0.5";
      }
    }
  }

  if (inputOtherCardNum) {
    inputOtherCardNum.addEventListener("input", function() {
      // Auto-format spaces 0000 0000 0000 0000
      var val = inputOtherCardNum.value.replace(/\\D/g, "").slice(0, 16);
      var formatted = val.match(/.{1,4}/g)?.join(" ") || val;
      inputOtherCardNum.value = formatted;
      validateOtherCardInput();
    });
  }

  // Proceed to 2FA Step
  if (seatPaymentProceedBtn) {
    seatPaymentProceedBtn.addEventListener("click", function(e) {
      e.preventDefault();
      closeSeatPaymentModal();
      openPaymentOtpModal();
    });
  }

  // OTP Modal Listeners
  if (paymentOtpModalClose) {
    paymentOtpModalClose.addEventListener("click", closePaymentOtpModal);
  }
  if (paymentOtpModalOverlay) {
    paymentOtpModalOverlay.addEventListener("click", function(e) {
      if (e.target === paymentOtpModalOverlay) closePaymentOtpModal();
    });
  }

  // Digit box auto-jump
  var otpInputs = document.querySelectorAll(".otp-digit-input");
  otpInputs.forEach(function(inp, idx) {
    inp.addEventListener("input", function() {
      if (inp.value.length === 1 && idx < otpInputs.length - 1) {
        otpInputs[idx + 1].focus();
      }
    });
    inp.addEventListener("keydown", function(e) {
      if (e.key === "Backspace" && !inp.value && idx > 0) {
        otpInputs[idx - 1].focus();
      }
    });
  });

  if (btnResendOtp) {
    btnResendOtp.addEventListener("click", function(e) {
      e.preventDefault();
      alert("New Bursar Security Code dispatched to devendra.dubey@iitgn.ac.in\n\nCode: 893201");
    });
  }

  if (btnConfirmOtpSubmit) {
    btnConfirmOtpSubmit.addEventListener("click", function(e) {
      e.preventDefault();
      btnConfirmOtpSubmit.disabled = true;
      btnConfirmOtpSubmit.innerHTML = '<i class="fa fa-spinner fa-spin"></i> Clearing Mandate &amp; Settling $6,200.00...';

      setTimeout(function() {
        sessionStorage.setItem("seatDepositPaid", "true");
        applySeatDepositPaidState();
        closePaymentOtpModal();
        btnConfirmOtpSubmit.disabled = false;
        btnConfirmOtpSubmit.innerHTML = '<i class="fa-solid fa-lock"></i> Authorize &amp; Settle $6,200.00 USD';

        // Launch Official Receipt Modal immediately
        openInvoiceReceiptModal();
      }, 900);
    });
  }

  // Receipt Modal Listeners
  if (receiptModalClose) {
    receiptModalClose.addEventListener("click", closeInvoiceReceiptModal);
  }
  if (receiptModalCloseBtn2) {
    receiptModalCloseBtn2.addEventListener("click", closeInvoiceReceiptModal);
  }
  if (receiptPrintBtn) {
    receiptPrintBtn.addEventListener("click", function() {
      window.print();
    });
  }
  if (invoiceReceiptModalOverlay) {
    invoiceReceiptModalOverlay.addEventListener("click", function(e) {
      if (e.target === invoiceReceiptModalOverlay) closeInvoiceReceiptModal();
    });
  }

  // Card Verification Flow Modal Listeners
  if (verifyCardModalClose) {
    verifyCardModalClose.addEventListener("click", closeVerifyCardModal);
  }
  if (verifyCardModalCloseBtn2) {
    verifyCardModalCloseBtn2.addEventListener("click", closeVerifyCardModal);
  }
  if (verifyCardModalOverlay) {
    verifyCardModalOverlay.addEventListener("click", function(e) {
      if (e.target === verifyCardModalOverlay) closeVerifyCardModal();
    });
  }

  if (btnVerifyStep1Next) {
    btnVerifyStep1Next.addEventListener("click", function(e) {
      e.preventDefault();
      var cardNum = (document.getElementById("vCardNum") || {}).value || "";
      if (cardNum.replace(/\\D/g, "").length < 12) {
        alert("Please enter a valid card number for pre-authorization.");
        return;
      }
      if (verifyStep1) verifyStep1.style.display = "none";
      if (verifyStep2) verifyStep2.style.display = "block";
    });
  }

  if (btnVerifyOtpSubmit) {
    btnVerifyOtpSubmit.addEventListener("click", function(e) {
      e.preventDefault();
      btnVerifyOtpSubmit.disabled = true;
      btnVerifyOtpSubmit.innerHTML = '<i class="fa fa-spinner fa-spin"></i> Registering Mandate...';
      
      setTimeout(function() {
        if (verifyStep2) verifyStep2.style.display = "none";
        if (verifyStep3) verifyStep3.style.display = "block";
        btnVerifyOtpSubmit.disabled = false;
        btnVerifyOtpSubmit.innerHTML = '<i class="fa-solid fa-check"></i> Verify &amp; Register Mandate';
      }, 800);
    });
  }

  // Global ESC key listener
  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape" || e.keyCode === 27) {
      closeSeatPaymentModal();
      closePaymentOtpModal();
      closeInvoiceReceiptModal();
      closeVerifyCardModal();
    }
  });

  window.openSeatPaymentModal = openSeatPaymentModal;
  window.closeSeatPaymentModal = closeSeatPaymentModal;
  window.openPaymentOtpModal = openPaymentOtpModal;
  window.closePaymentOtpModal = closePaymentOtpModal;
  window.openInvoiceReceiptModal = openInvoiceReceiptModal;
  window.closeInvoiceReceiptModal = closeInvoiceReceiptModal;
  window.openVerifyCardModal = openVerifyCardModal;
  window.closeVerifyCardModal = closeVerifyCardModal;
"""

    # Replace the legacy alert seat deposit code in interactive_runtime.js
    pattern = re.compile(r'// Handle Seat Confirmation Deposit \(\$6,200\.00 USD\).*?window\.closeCvModal = closeCvModal;', re.DOTALL)
    
    replacement = payment_runtime_code.strip() + "\n\n  window.openTranscriptModal = openTranscriptModal;\n  window.closeTranscriptModal = closeTranscriptModal;\n  window.openCvModal = openCvModal;\n  window.closeCvModal = closeCvModal;"

    new_runtime_js, count = pattern.subn(lambda m: replacement, runtime_js)
    if count == 0:
        print("Warning: regex pattern did not match in interactive_runtime.js, appending instead.")
        new_runtime_js = runtime_js + "\n" + payment_runtime_code

    with open(runtime_path, "w", encoding="utf-8") as f:
        f.write(new_runtime_js)
    print("Successfully updated interactive_runtime.js!")

if __name__ == "__main__":
    update_files()
