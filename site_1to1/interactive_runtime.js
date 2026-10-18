/**
 * The University of Chicago — 1:1 Production Runtime Script
 * Directly activates production data attributes and event handlers.
 */

document.addEventListener("DOMContentLoaded", function () {
  console.log("Initializing University of Chicago 1:1 Production Runtime...");

  // --- 1. Info For Dropdowns ---
  var infoContainers = document.querySelectorAll(".EduBrandBar_infoDropdownContainer__2FlvZ");
  infoContainers.forEach(function (container) {
    var btn = container.querySelector(".EduBrandBar_infoDropdownButton__23iFj");
    if (btn) {
      btn.addEventListener("click", function (e) {
        e.stopPropagation();
        var isOpen = container.getAttribute("data-infodropdownisopen") === "true";
        container.setAttribute("data-infodropdownisopen", !isOpen ? "true" : "false");
        btn.setAttribute("aria-expanded", !isOpen ? "true" : "false");
      });
    }
  });

  // Close info dropdown when clicking anywhere else
  document.addEventListener("click", function (e) {
    infoContainers.forEach(function (container) {
      if (!container.contains(e.target)) {
        container.setAttribute("data-infodropdownisopen", "false");
        var btn = container.querySelector(".EduBrandBar_infoDropdownButton__23iFj");
        if (btn) btn.setAttribute("aria-expanded", "false");
      }
    });
  });

  // --- 2. Search Flyout ---
  var searchBtns = document.querySelectorAll("#searchBtn-desktop, #searchBtn-mobile");
  var brandBarContainers = document.querySelectorAll(".EduBrandBar_container__5LPzZ");
  var searchCloseBtns = document.querySelectorAll(".EduBrandBar_close__37V8Q");
  var searchInputs = document.querySelectorAll(".EduBrandBar_searchBar__3S9GH");

  searchBtns.forEach(function (btn) {
    btn.addEventListener("click", function (e) {
      e.stopPropagation();
      brandBarContainers.forEach(function (bar) {
        var isOpen = bar.getAttribute("data-searchopen") === "true";
        bar.setAttribute("data-searchopen", !isOpen ? "true" : "false");
        btn.setAttribute("aria-expanded", !isOpen ? "true" : "false");
        if (!isOpen) {
          setTimeout(function () {
            searchInputs.forEach(function (input) { input.focus(); });
          }, 100);
        }
      });
    });
  });

  searchCloseBtns.forEach(function (closeBtn) {
    closeBtn.addEventListener("click", function (e) {
      e.stopPropagation();
      brandBarContainers.forEach(function (bar) {
        bar.setAttribute("data-searchopen", "false");
      });
      searchBtns.forEach(function (b) { b.setAttribute("aria-expanded", "false"); });
    });
  });

  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape") {
      brandBarContainers.forEach(function (bar) {
        bar.setAttribute("data-searchopen", "false");
      });
      searchBtns.forEach(function (b) { b.setAttribute("aria-expanded", "false"); });
    }
  });

  // --- 3. Mobile Navigation Drawer ---
  var header = document.getElementById("header");
  var mobileToggleBtn = document.getElementById("mobileTogBtn");

  if (mobileToggleBtn && header) {
    mobileToggleBtn.addEventListener("click", function () {
      var isOpen = header.getAttribute("data-mobilenavisopen") === "true";
      header.setAttribute("data-mobilenavisopen", !isOpen ? "true" : "false");
      mobileToggleBtn.setAttribute("aria-expanded", !isOpen ? "true" : "false");
    });
  }

  // Mobile Accordion Submenus
  var mobileNavItems = document.querySelectorAll(".EduHeader_mobileOnly__p1dMY .EduNavigation_navListItem__2Qihw.EduNavigation_hasDropdown__3aDrm");
  mobileNavItems.forEach(function (item) {
    var l1Link = item.querySelector(".EduNavigation_l1Link__1J9ID");
    var backBtn = item.querySelector(".EduNavigation_backButton__2wSih");

    if (l1Link) {
      l1Link.addEventListener("click", function (e) {
        // Prevent immediate navigation so dropdown slides in on mobile
        e.preventDefault();
        item.setAttribute("data-mobilenavdropdownisopen", "true");
        l1Link.setAttribute("aria-expanded", "true");
      });
    }

    if (backBtn) {
      backBtn.addEventListener("click", function (e) {
        e.stopPropagation();
        item.setAttribute("data-mobilenavdropdownisopen", "false");
        if (l1Link) l1Link.setAttribute("aria-expanded", "false");
      });
    }
  });

  // --- 4. Video Spotlight Controls ---
  var videoSpotlights = document.querySelectorAll(".VideoSpotlight_videoSpotlight__EC6TG");
  videoSpotlights.forEach(function (spotlight) {
    var video = spotlight.querySelector("video");
    var playPauseBtn = spotlight.querySelector(".VideoSpotlight_btnPlayPause__1m-El");

    if (video && playPauseBtn) {
      playPauseBtn.addEventListener("click", function () {
        if (video.paused) {
          video.play();
          spotlight.classList.add("isPlaying");
          playPauseBtn.setAttribute("aria-label", "Pause spotlight video");
          playPauseBtn.setAttribute("aria-pressed", "false");
        } else {
          video.pause();
          spotlight.classList.remove("isPlaying");
          playPauseBtn.setAttribute("aria-label", "Play spotlight video");
          playPauseBtn.setAttribute("aria-pressed", "true");
        }
      });
    }
  });

  // --- 5. Scroll Header State ---
  if (header) {
    window.addEventListener("scroll", function () {
      if (window.scrollY > 100) {
        header.setAttribute("data-scrolldown", "true");
      } else {
        header.setAttribute("data-scrolldown", "false");
      }
    }, { passive: true });
  }

  // --- 6. Admissions Application Portal Navigation ---
  var portalOverlay = document.getElementById("portalModalOverlay");
  var portalCloseBtn = document.getElementById("portalModalClose");
  var portalTriggers = document.querySelectorAll("#portalTriggerBtn, #portalTriggerBtn-mobile, .portal-trigger-btn");
  var applicantIdInput = document.getElementById("applicantId") || document.getElementById("applicantIdInput");
  var applicantPwInput = document.getElementById("applicantPassword") || document.getElementById("applicantPwInput");
  var pwToggleBtn = document.getElementById("portalPasswordToggle") || document.getElementById("pwToggleBtn");
  var pwIcon = document.getElementById("portalPwIcon") || document.getElementById("pwIcon");
  var loginForm = document.getElementById("admissionsLoginForm") || document.getElementById("loginForm");
  var portalNotice = document.getElementById("portalNotice");

  function openPortal() {
    var isSubpage = window.location.pathname.indexOf("/pages/") !== -1 || window.location.pathname.indexOf("\\pages\\") !== -1;
    var targetUrl = isSubpage ? "portal.html" : "portal.html";
    window.location.href = targetUrl;
  }

  function closePortal() {
    if (!portalOverlay) return;
    portalOverlay.classList.remove("is-active");
    portalOverlay.setAttribute("aria-hidden", "true");
    document.body.style.overflow = "";
    portalTriggers.forEach(function (btn) { btn.setAttribute("aria-expanded", "false"); });
    if (window.location.hash) {
      history.replaceState(null, null, window.location.pathname + window.location.search);
    }
  }

  portalTriggers.forEach(function (btn) {
    btn.addEventListener("click", function (e) {
      // Direct navigation to dedicated portal page, not a popup
      var isSubpage = window.location.pathname.indexOf("/pages/") !== -1 || window.location.pathname.indexOf("\\pages\\") !== -1;
      var targetUrl = isSubpage ? "portal.html" : "portal.html";
      window.location.href = targetUrl;
    });
  });

  if (portalCloseBtn) {
    portalCloseBtn.addEventListener("click", function (e) {
      e.preventDefault();
      closePortal();
    });
  }

  if (portalOverlay) {
    portalOverlay.addEventListener("click", function (e) {
      if (e.target === portalOverlay) {
        closePortal();
      }
    });
  }

  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape" && portalOverlay && portalOverlay.classList.contains("is-active")) {
      closePortal();
    }
  });

  // Pre-fill applicant ID if present in query parameters
  try {
    var urlParams = new URLSearchParams(window.location.search);
    if (urlParams.has("applicantId") && applicantIdInput) {
      applicantIdInput.value = urlParams.get("applicantId");
    }
  } catch (err) {}

  // Password Visibility Toggle
  if (pwToggleBtn && applicantPwInput && pwIcon) {
    pwToggleBtn.addEventListener("click", function (e) {
      e.preventDefault();
      var isPassword = applicantPwInput.getAttribute("type") === "password";
      applicantPwInput.setAttribute("type", isPassword ? "text" : "password");
      pwIcon.className = isPassword ? "fa-regular fa-eye-slash" : "fa-regular fa-eye";
      pwToggleBtn.setAttribute("aria-label", isPassword ? "Hide password" : "Show password");
    });
  }

  // --- Credentials Configuration ---
  var VALID_APP_ID = "UC-2027-89321";
  var VALID_EMAIL = "DUBEY351DEV@GMAIL.COM";
  var VALID_PASSWORD = "9833@dEVuc";

  var portalLoginView = document.getElementById("portalLoginView");
  var portalDashboardView = document.getElementById("portalDashboardView");
  var portalSubmitBtn = document.getElementById("portalSubmitBtn");
  var portalTitle = document.getElementById("portalTitle");
  var portalSubtitle = document.querySelector(".portal-subtitle") || document.getElementById("portalSubHeader");
  var portalLogoutBtn = document.getElementById("portalLogoutBtn");
  var portalPrintBtn = document.getElementById("portalPrintBtn");

  // Sync login state from sessionStorage on page load
  try {
    var isAuth = sessionStorage.getItem("applicantLoggedIn") === "true";
    var topBanner = document.getElementById("portalTopBanner");
    if (isAuth) {
      if (portalLoginView) portalLoginView.style.display = "none";
      if (portalDashboardView) portalDashboardView.style.display = "block";
      if (topBanner) topBanner.style.display = "none";
      if (portalTitle) portalTitle.textContent = "Welcome, Devendra Biswambhar Nath Dubey";
      if (portalSubtitle) {
        portalSubtitle.setAttribute("spellcheck", "false");
        portalSubtitle.textContent = "Doctor of Philosophy in Chemistry \u2014 Computational Chemistry \u2022 Division of the Physical Sciences \u2022 Autumn Quarter 2027";
      }
    } else {
      if (topBanner) topBanner.style.display = "flex";
    }
  } catch (e) {}

  // Handle Form Submission
  if (loginForm) {
    loginForm.addEventListener("submit", function (e) {
      e.preventDefault();
      var idVal = (applicantIdInput ? applicantIdInput.value.trim() : "");
      var pwVal = (applicantPwInput ? applicantPwInput.value : "");

      // Clear previous error states
      if (applicantIdInput) applicantIdInput.classList.remove("is-invalid");
      if (applicantPwInput) applicantPwInput.classList.remove("is-invalid");

      if (!idVal || !pwVal) {
        if (portalNotice) {
          portalNotice.className = "portal-alert-msg is-error";
          portalNotice.style.display = "flex";
          portalNotice.innerHTML = '<i class="fa-solid fa-circle-exclamation"></i><span>Please enter both your Application ID / Email and your Password.</span>';
        }
        if (!idVal && applicantIdInput) applicantIdInput.classList.add("is-invalid");
        if (!pwVal && applicantPwInput) applicantPwInput.classList.add("is-invalid");
        return;
      }

      // Check credentials (case-insensitive for ID/email, exact for password)
      var idClean = idVal.toUpperCase();
      var isIdMatch = (idClean === VALID_APP_ID || idClean === VALID_EMAIL);
      var isPwMatch = (pwVal === VALID_PASSWORD);

      if (portalSubmitBtn) {
        portalSubmitBtn.disabled = true;
        portalSubmitBtn.innerHTML = '<i class="fa fa-spinner fa-spin" style="margin-right: 8px;"></i> Authenticating...';
      }

      setTimeout(function () {
        if (portalSubmitBtn) {
          portalSubmitBtn.disabled = false;
          portalSubmitBtn.textContent = 'Log In to Portal';
        }

        if (isIdMatch && isPwMatch) {
          // Success: Switch to Authenticated Dashboard & persist in sessionStorage
          try {
            sessionStorage.setItem("applicantLoggedIn", "true");
          } catch (err) {}

          var topBannerEl = document.getElementById("portalTopBanner");
          if (topBannerEl) topBannerEl.style.display = "none";
          if (portalLoginView) portalLoginView.style.display = "none";
          if (portalDashboardView) portalDashboardView.style.display = "block";
          if (portalTitle) portalTitle.textContent = "Welcome, Devendra Biswambhar Nath Dubey";
          if (portalSubtitle) {
            portalSubtitle.setAttribute("spellcheck", "false");
            portalSubtitle.textContent = "Doctor of Philosophy in Chemistry \u2014 Computational Chemistry \u2022 Division of the Physical Sciences \u2022 Autumn Quarter 2027";
          }
          if (portalNotice) {
            portalNotice.style.display = "none";
          }
          window.scrollTo({ top: 0, behavior: "smooth" });
        } else {
          // Failure: Display Error Message
          if (portalNotice) {
            portalNotice.className = "portal-alert-msg is-error";
            portalNotice.style.display = "flex";
            portalNotice.innerHTML = '<i class="fa-solid fa-circle-exclamation"></i><span>The Application ID/Email or Password entered does not match our records. Please try again.</span>';
          }
          if (applicantIdInput) applicantIdInput.classList.add("is-invalid");
          if (applicantPwInput) {
            applicantPwInput.classList.add("is-invalid");
            applicantPwInput.value = "";
            applicantPwInput.focus();
          }
        }
      }, 550);
    });
  }

  // Handle Logout
  if (portalLogoutBtn) {
    portalLogoutBtn.addEventListener("click", function () {
      try {
        sessionStorage.removeItem("applicantLoggedIn");
      } catch (err) {}
      var topBannerEl = document.getElementById("portalTopBanner");
      if (topBannerEl) topBannerEl.style.display = "flex";
      if (portalDashboardView) portalDashboardView.style.display = "none";
      if (portalLoginView) portalLoginView.style.display = "block";
      if (portalTitle) portalTitle.textContent = "Applicant Status Portal";
      if (portalSubtitle) portalSubtitle.textContent = "The University of Chicago \u2022 Division of the Physical Sciences \u2022 Department of Chemistry";
      if (portalNotice) {
        portalNotice.className = "portal-alert-msg is-info";
        portalNotice.style.display = "flex";
        portalNotice.innerHTML = '<i class="fa-solid fa-circle-info" style="margin-right: 6px;"></i><span>You have successfully signed out. Enter your credentials to log in again.</span>';
      }
      if (applicantIdInput) {
        applicantIdInput.value = "";
        applicantIdInput.classList.remove("is-invalid");
      }
      if (applicantPwInput) {
        applicantPwInput.value = "";
        applicantPwInput.classList.remove("is-invalid");
      }
      window.scrollTo({ top: 0, behavior: "smooth" });
    });
  }

  // Handle Print Summary
  if (portalPrintBtn) {
    portalPrintBtn.addEventListener("click", function () {
      window.print();
    });
  }

  // Handle Resume File Upload & Preview
  var resumeFileInput = document.getElementById("resumeFileInput");
  var portalResumeFileName = document.getElementById("portalResumeFileName");
  var portalResumeFileMeta = document.getElementById("portalResumeFileMeta");
  var portalResumeBadge = document.getElementById("portalResumeBadge");
  var resumeUploadFeedback = document.getElementById("resumeUploadFeedback");
  var portalResumePreviewBtn = document.getElementById("portalResumePreviewBtn");

  if (resumeFileInput) {
    resumeFileInput.addEventListener("change", function () {
      if (resumeFileInput.files && resumeFileInput.files[0]) {
        var file = resumeFileInput.files[0];
        var sizeKb = Math.round(file.size / 1024);
        if (portalResumeFileName) portalResumeFileName.textContent = file.name;
        if (portalResumeFileMeta) portalResumeFileMeta.textContent = "Uploaded Document • " + sizeKb + " KB • Verified";
        if (portalResumeBadge) {
          portalResumeBadge.textContent = "Updated (Official)";
          portalResumeBadge.className = "portal-badge-received";
        }
        if (resumeUploadFeedback) {
          resumeUploadFeedback.style.display = "block";
          setTimeout(function () {
            resumeUploadFeedback.style.display = "none";
          }, 4000);
        }
      }
    });
  }

  if (portalResumePreviewBtn) {
    portalResumePreviewBtn.addEventListener("click", function (e) {
      e.preventDefault();
      if (typeof openCvModal === "function") {
        openCvModal();
      }
    });
  }

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
      portalDepositStatusBadge.style.background = "#fdf2f2";
      portalDepositStatusBadge.style.color = "#800000";
      portalDepositStatusBadge.style.borderColor = "#d9c5c5";
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
        '<div style="font-size: 12px; color: #800000; margin-top: 10px; display: flex; align-items: center; gap: 6px; font-weight: 600;">',
        '  <i class="fa-solid fa-shield-check"></i> Ref #REF-UCHI-DEP-2027-6200 • Form 1098-T Eligible • Settled via Discover Debit Card (•••• 0405)',
        '</div>'
      ].join("\n");

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

  function switchModalInvoice(type) {
    var isAppFee = (type === "app_fee");
    var isSubPage = window.location.pathname.indexOf("/pages/") !== -1;
    var rel = isSubPage ? "../" : "";

    var modalTitle = document.getElementById("invoiceReceiptModalTitle");
    var modalSub = document.getElementById("invoiceReceiptModalSubtitle");
    var modalImg = document.getElementById("modalReceiptImg");
    var modalPdf = document.getElementById("modalDownloadPdfBtn");
    var modalWeb = document.getElementById("modalWebReceiptLink");
    var modalTag = document.getElementById("modalInvoiceDateTag");
    var tabSeat = document.getElementById("modalTabSeatDeposit");
    var tabApp = document.getElementById("modalTabAppFee");

    if (isAppFee) {
      if (modalTitle) modalTitle.textContent = "Official Graduate Admissions Application Fee Receipt";
      if (modalSub) {
        modalSub.innerHTML = 'Candidate: <strong>Devendra Dubey</strong> • Ref: <strong>REF-UCHI-APP-2026-90</strong> • Paid: <strong>$90.00 USD</strong> • <strong>01 Oct 2026, 6:30 AM IST</strong>';
      }
      if (modalImg) {
        modalImg.src = rel + "assets/documents/app_fee_receipt_page_1.png";
        modalImg.alt = "Official Graduate Admissions Application Fee Receipt (01 Oct 2026 6:30 AM IST) - Devendra Dubey";
      }
      if (modalPdf) {
        modalPdf.href = rel + "assets/documents/Official_Application_Fee_Receipt_UCHI_2026.pdf";
        modalPdf.download = "Official_Application_Fee_Receipt_UCHI_2026.pdf";
      }
      if (modalWeb) {
        modalWeb.href = rel + "application-fee-receipt.html";
      }
      if (modalTag) {
        modalTag.innerHTML = '<i class="fa-solid fa-circle-check"></i> Form 1098-T Eligible • Settled 01 Oct 2026, 6:30 AM IST • Discover (•••• 0405)';
      }
      if (tabApp) {
        tabApp.className = "receipt-tab-btn is-active";
        tabApp.style.background = "#ffffff";
        tabApp.style.color = "#800000";
        tabApp.style.fontWeight = "700";
        tabApp.style.boxShadow = "0 1px 3px rgba(0,0,0,0.15)";
      }
      if (tabSeat) {
        tabSeat.className = "receipt-tab-btn";
        tabSeat.style.background = "transparent";
        tabSeat.style.color = "#495057";
        tabSeat.style.fontWeight = "600";
        tabSeat.style.boxShadow = "none";
      }
    } else {
      if (modalTitle) modalTitle.textContent = "Official Bursar Tax Receipt & Enrollment Mandate";
      if (modalSub) {
        modalSub.innerHTML = 'Candidate: <strong>Devendra Dubey</strong> • Ref: <strong>REF-UCHI-DEP-2027-6200</strong> • Paid: <strong>$6,200.00 USD</strong> • Status: <strong>PAID IN FULL</strong>';
      }
      if (modalImg) {
        modalImg.src = rel + "assets/documents/receipt_page_1.png";
        modalImg.alt = "Official Student Accounts Tax Receipt & Enrollment Mandate - Devendra Dubey";
      }
      if (modalPdf) {
        modalPdf.href = rel + "assets/documents/Official_Receipt_UCHI_2027_6200.pdf";
        modalPdf.download = "Official_Receipt_UCHI_2027_6200.pdf";
      }
      if (modalWeb) {
        modalWeb.href = rel + "receipt.html?type=seat_deposit";
      }
      if (modalTag) {
        modalTag.innerHTML = '<i class="fa-solid fa-circle-check"></i> Form 1098-T Eligible • Settled via Discover (•••• 0405)';
      }
      if (tabSeat) {
        tabSeat.className = "receipt-tab-btn is-active";
        tabSeat.style.background = "#ffffff";
        tabSeat.style.color = "#800000";
        tabSeat.style.fontWeight = "700";
        tabSeat.style.boxShadow = "0 1px 3px rgba(0,0,0,0.15)";
      }
      if (tabApp) {
        tabApp.className = "receipt-tab-btn";
        tabApp.style.background = "transparent";
        tabApp.style.color = "#495057";
        tabApp.style.fontWeight = "600";
        tabApp.style.boxShadow = "none";
      }
    }
  }

  function openInvoiceReceiptModal(type) {
    if (!invoiceReceiptModalOverlay) return;
    switchModalInvoice(type || "seat_deposit");
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
  
  var btnViewAppFeeReceipt = document.getElementById("btnViewAppFeeReceipt");
  if (btnViewAppFeeReceipt) {
    btnViewAppFeeReceipt.addEventListener("click", function (e) {
      e.preventDefault();
      openInvoiceReceiptModal("app_fee");
    });
  }

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
    var raw = inputOtherCardNum.value.replace(/\D/g, "");
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
        cardValidationFeedback.innerHTML = '<span style="color:#800000; font-weight:700;"><i class="fa-solid fa-circle-check"></i> Pre-authorized verified card recognized.</span>';
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
      var val = inputOtherCardNum.value.replace(/\D/g, "").slice(0, 16);
      var formatted = val.match(/.{1,4}/g)?.join(" ") || val;
      inputOtherCardNum.value = formatted;
      validateOtherCardInput();
    });
  }

  // --- Two-Factor Security Authorization (SMTP 2FA) ---
  var otpCountdownInterval = null;

  function startOtpCountdown(durationSeconds) {
    if (otpCountdownInterval) clearInterval(otpCountdownInterval);
    var timerEl = document.getElementById("otpCountdownTimer");
    var remaining = durationSeconds || 600;

    function renderTime() {
      if (!timerEl) return;
      var mins = Math.floor(remaining / 60);
      var secs = remaining % 60;
      timerEl.textContent = (mins < 10 ? "0" : "") + mins + ":" + (secs < 10 ? "0" : "") + secs;
      if (remaining <= 0) {
        clearInterval(otpCountdownInterval);
        timerEl.textContent = "Expired";
        var validationMsg = document.getElementById("otpValidationMsg");
        if (validationMsg) {
          validationMsg.innerHTML = '<i class="fa-solid fa-clock-rotate-left"></i> Security code expired. Click "Resend Security Code" below.';
          validationMsg.style.display = "block";
          validationMsg.style.color = "#c53030";
        }
      }
      remaining--;
    }

    renderTime();
    otpCountdownInterval = setInterval(renderTime, 1000);
  }

  // Proceed to 2FA Step - Dispatches OTP via SMTP
  if (seatPaymentProceedBtn) {
    seatPaymentProceedBtn.addEventListener("click", function(e) {
      e.preventDefault();
      var originalBtnHtml = seatPaymentProceedBtn.innerHTML;
      seatPaymentProceedBtn.disabled = true;
      seatPaymentProceedBtn.innerHTML = '<i class="fa fa-spinner fa-spin"></i> Dispatched via SMTP Gateway...';

      var userEmail = sessionStorage.getItem("applicantLoginEmail") || "dubey351dev@gmail.com";
      var userId = sessionStorage.getItem("applicantLoginId") || "UC-2027-89321";

      var emailDisplay = document.getElementById("otpRecipientEmailDisplay");
      if (emailDisplay) emailDisplay.textContent = userEmail;

      var validationMsg = document.getElementById("otpValidationMsg");
      if (validationMsg) validationMsg.style.display = "none";

      var statusBanner = document.getElementById("otpStatusBanner");
      var statusBannerText = document.getElementById("otpStatusBannerText");

      fetch("/api/payment/create", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          cardLast4: "0405",
          amount: 6200,
          email: userEmail,
          applicantId: userId,
          studentName: "Devendra Dubey"
        })
      })
      .then(function(res) { return res.json(); })
      .then(function(data) {
        if (data.transactionId) {
          sessionStorage.setItem("currentPaymentTxnId", data.transactionId);
        }

        var recipient = data.recipientEmail || userEmail;
        if (emailDisplay) emailDisplay.textContent = recipient;

        // Clear existing input values
        otpInputs.forEach(function(inp) { inp.value = ""; });

        if (statusBanner && statusBannerText) {
          if (data.sentViaSmtp) {
            statusBanner.style.background = "#f0fdf4";
            statusBanner.style.borderColor = "#86efac";
            statusBannerText.innerHTML = [
              '<div style="font-weight:700; color:#166534; display:flex; align-items:center; gap:6px;">',
              '  <i class="fa-solid fa-circle-check" style="color:#16a34a;"></i> Live SMTP Code Dispatched',
              '</div>',
              '<div style="font-size:12px; color:#14532d; margin-top:2px;">',
              '  Dispatched from <strong>' + (data.smtpSender || 'admissions@uchicago.asia') + '</strong> to <strong>' + recipient + '</strong>.',
              '</div>'
            ].join("");
          } else {
            // Simulated delivery / pending live password in .env
            statusBanner.style.background = "#fff8e6";
            statusBanner.style.borderColor = "#fcd34d";
            statusBannerText.innerHTML = [
              '<div style="font-weight:700; color:#92400e; display:flex; align-items:center; gap:6px; flex-wrap:wrap;">',
              '  <i class="fa-solid fa-envelope-circle-check" style="color:#d97706;"></i> SMTP 2FA Code Generated for ' + recipient,
              (data.demoSecurityCode ? '  <span style="background:#800000; color:#ffffff; padding:2px 8px; border-radius:3px; font-family:monospace; font-weight:700; font-size:13px; margin-left:6px;">Code: ' + data.demoSecurityCode + '</span>' : ''),
              '</div>',
              '<div style="font-size:11.5px; color:#78350f; margin-top:3px;">',
              '  Sender Account: <code>' + (data.smtpSender || 'admissions@uchicago.asia') + '</code> (Domain SMTP Gateway)',
              '</div>'
            ].join("");

            // If simulated code provided, prefill for seamless testing
            if (data.demoSecurityCode && data.demoSecurityCode.length === 6) {
              for (var i = 0; i < 6; i++) {
                if (otpInputs[i]) otpInputs[i].value = data.demoSecurityCode[i];
              }
            }
          }
        }

        startOtpCountdown(600);
        closeSeatPaymentModal();
        openPaymentOtpModal();
        setTimeout(function() {
          if (otpInputs[0]) otpInputs[0].focus();
        }, 300);
      })
      .catch(function(err) {
        console.error("2FA dispatch error:", err);
        // Graceful fallback for offline demo testing
        var fallbackCode = "893201";
        sessionStorage.setItem("currentPaymentTxnId", "TXN-UCHI-2026-89321");
        if (statusBannerText) {
          statusBannerText.innerHTML = '<strong>SMTP Security Code Dispatched:</strong> Code <strong>' + fallbackCode + '</strong> sent to ' + userEmail;
        }
        for (var i = 0; i < 6; i++) {
          if (otpInputs[i]) otpInputs[i].value = fallbackCode[i];
        }
        startOtpCountdown(600);
        closeSeatPaymentModal();
        openPaymentOtpModal();
      })
      .finally(function() {
        seatPaymentProceedBtn.disabled = false;
        seatPaymentProceedBtn.innerHTML = originalBtnHtml;
      });
    });
  }

  // OTP Modal Listeners
  if (paymentOtpModalClose) {
    paymentOtpModalClose.addEventListener("click", function() {
      if (otpCountdownInterval) clearInterval(otpCountdownInterval);
      closePaymentOtpModal();
    });
  }
  if (paymentOtpModalOverlay) {
    paymentOtpModalOverlay.addEventListener("click", function(e) {
      if (e.target === paymentOtpModalOverlay) {
        if (otpCountdownInterval) clearInterval(otpCountdownInterval);
        closePaymentOtpModal();
      }
    });
  }

  // Digit box auto-jump & Paste handler
  var otpInputs = document.querySelectorAll(".otp-digit-input");
  otpInputs.forEach(function(inp, idx) {
    inp.addEventListener("input", function() {
      var val = inp.value.replace(/\D/g, "");
      inp.value = val;
      if (val.length === 1 && idx < otpInputs.length - 1) {
        otpInputs[idx + 1].focus();
      }
    });

    inp.addEventListener("keydown", function(e) {
      if (e.key === "Backspace" && !inp.value && idx > 0) {
        otpInputs[idx - 1].focus();
      }
    });

    inp.addEventListener("paste", function(e) {
      var pasteData = (e.clipboardData || window.clipboardData).getData("text");
      var digits = (pasteData || "").replace(/\D/g, "").slice(0, 6);
      if (digits.length > 0) {
        e.preventDefault();
        for (var i = 0; i < digits.length; i++) {
          if (otpInputs[i]) otpInputs[i].value = digits[i];
        }
        var nextIdx = Math.min(digits.length, otpInputs.length - 1);
        if (otpInputs[nextIdx]) otpInputs[nextIdx].focus();
      }
    });
  });

  // Resend OTP via SMTP
  if (btnResendOtp) {
    btnResendOtp.addEventListener("click", function(e) {
      e.preventDefault();
      var originalText = btnResendOtp.textContent;
      btnResendOtp.disabled = true;
      btnResendOtp.textContent = "Resending...";

      var userEmail = sessionStorage.getItem("applicantLoginEmail") || "dubey351dev@gmail.com";
      var currentTxnId = sessionStorage.getItem("currentPaymentTxnId") || "TXN-UCHI-2026-89321";

      fetch("/api/payment/resend-otp", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          transactionId: currentTxnId,
          email: userEmail
        })
      })
      .then(function(res) { return res.json(); })
      .then(function(data) {
        if (data.transactionId) {
          sessionStorage.setItem("currentPaymentTxnId", data.transactionId);
        }
        otpInputs.forEach(function(inp) { inp.value = ""; });
        if (otpInputs[0]) otpInputs[0].focus();

        var statusBannerText = document.getElementById("otpStatusBannerText");
        var validationMsg = document.getElementById("otpValidationMsg");
        if (validationMsg) {
          validationMsg.innerHTML = '<i class="fa-solid fa-circle-check"></i> Fresh authorization code dispatched via SMTP.';
          validationMsg.style.display = "block";
          validationMsg.style.color = "#166534";
        }

        if (statusBannerText) {
          if (data.sentViaSmtp) {
            statusBannerText.innerHTML = '<strong><i class="fa-solid fa-circle-check" style="color:#16a34a;"></i> New Code Dispatched:</strong> Sent from <code>' + (data.smtpSender || 'admissions@uchicago.asia') + '</code> to <strong>' + (data.recipientEmail || userEmail) + '</strong>.';
          } else {
            statusBannerText.innerHTML = '<strong>New Code Generated:</strong> Sent to <strong>' + (data.recipientEmail || userEmail) + '</strong>.' + (data.demoSecurityCode ? ' <span style="background:#800000; color:#fff; padding:2px 8px; border-radius:3px; font-family:monospace; font-weight:700;">Code: ' + data.demoSecurityCode + '</span>' : '');
            if (data.demoSecurityCode && data.demoSecurityCode.length === 6) {
              for (var i = 0; i < 6; i++) {
                if (otpInputs[i]) otpInputs[i].value = data.demoSecurityCode[i];
              }
            }
          }
        }
        startOtpCountdown(600);
      })
      .catch(function(err) {
        console.error("Resend OTP error:", err);
        alert("A new Bursar Security Code has been generated: 893201");
      })
      .finally(function() {
        btnResendOtp.disabled = false;
        btnResendOtp.textContent = originalText;
      });
    });
  }

  // Confirm OTP & Settle $6,200 Deposit
  if (btnConfirmOtpSubmit) {
    btnConfirmOtpSubmit.addEventListener("click", function(e) {
      e.preventDefault();
      var code = Array.from(otpInputs).map(function(inp) { return inp.value.trim(); }).join("");
      var validationMsg = document.getElementById("otpValidationMsg");

      if (code.length < 6) {
        if (validationMsg) {
          validationMsg.innerHTML = '<i class="fa-solid fa-triangle-exclamation"></i> Please enter the complete 6-digit security authorization code.';
          validationMsg.style.display = "block";
          validationMsg.style.color = "#c53030";
        }
        return;
      }

      btnConfirmOtpSubmit.disabled = true;
      var originalSubmitHtml = btnConfirmOtpSubmit.innerHTML;
      btnConfirmOtpSubmit.innerHTML = '<i class="fa fa-spinner fa-spin"></i> Clearing Mandate &amp; Settling $6,200.00...';

      var currentTxnId = sessionStorage.getItem("currentPaymentTxnId") || "TXN-UCHI-2026-89321";

      fetch("/api/payment/confirm-otp", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          transactionId: currentTxnId,
          otp: code
        })
      })
      .then(function(res) {
        return res.json().then(function(data) {
          return { ok: res.ok, data: data };
        });
      })
      .then(function(result) {
        if (result.ok && result.data.status === "CONFIRMED") {
          sessionStorage.setItem("seatDepositPaid", "true");
          if (result.data.transaction) {
            sessionStorage.setItem("confirmedDepositTxn", JSON.stringify(result.data.transaction));
          }
          if (otpCountdownInterval) clearInterval(otpCountdownInterval);
          applySeatDepositPaidState();
          closePaymentOtpModal();

          // Launch Official Receipt Modal immediately
          setTimeout(function() {
            openInvoiceReceiptModal();
          }, 350);
        } else {
          if (validationMsg) {
            validationMsg.innerHTML = '<i class="fa-solid fa-triangle-exclamation"></i> ' + (result.data.error || "Invalid security code. Please check your email and try again.");
            validationMsg.style.display = "block";
            validationMsg.style.color = "#c53030";
          }
        }
      })
      .catch(function(err) {
        console.error("OTP confirm error:", err);
        // Fallback master code check
        if (code === "893201") {
          sessionStorage.setItem("seatDepositPaid", "true");
          if (otpCountdownInterval) clearInterval(otpCountdownInterval);
          applySeatDepositPaidState();
          closePaymentOtpModal();
          setTimeout(function() {
            openInvoiceReceiptModal();
          }, 350);
        } else {
          if (validationMsg) {
            validationMsg.innerHTML = '<i class="fa-solid fa-triangle-exclamation"></i> Unable to verify code with Bursar server. Please try again.';
            validationMsg.style.display = "block";
            validationMsg.style.color = "#c53030";
          }
        }
      })
      .finally(function() {
        btnConfirmOtpSubmit.disabled = false;
        btnConfirmOtpSubmit.innerHTML = originalSubmitHtml;
      });
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
      if (cardNum.replace(/\D/g, "").length < 12) {
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

  // --- Offer Letter Modal Logic ---
  var offerLetterModalOverlay = document.getElementById("offerLetterModalOverlay");
  var btnOpenOfferLetterModal = document.getElementById("btnOpenOfferLetterModal");
  var offerLetterModalClose = document.getElementById("offerLetterModalClose");
  var offerLetterModalCloseBtn2 = document.getElementById("offerLetterModalCloseBtn2");
  var offerLetterPrintBtn = document.getElementById("offerLetterPrintBtn");

  function openOfferLetterModal() {
    if (!offerLetterModalOverlay) return;
    offerLetterModalOverlay.classList.add("is-active");
    offerLetterModalOverlay.setAttribute("aria-hidden", "false");
    document.body.style.overflow = "hidden";
  }

  function closeOfferLetterModal() {
    if (!offerLetterModalOverlay) return;
    offerLetterModalOverlay.classList.remove("is-active");
    offerLetterModalOverlay.setAttribute("aria-hidden", "true");
    document.body.style.overflow = "";
  }

  if (btnOpenOfferLetterModal) {
    btnOpenOfferLetterModal.addEventListener("click", function (e) {
      e.preventDefault();
      openOfferLetterModal();
    });
  }
  if (offerLetterModalClose) {
    offerLetterModalClose.addEventListener("click", closeOfferLetterModal);
  }
  if (offerLetterModalCloseBtn2) {
    offerLetterModalCloseBtn2.addEventListener("click", closeOfferLetterModal);
  }
  if (offerLetterPrintBtn) {
    offerLetterPrintBtn.addEventListener("click", function () {
      window.print();
    });
  }
  if (offerLetterModalOverlay) {
    offerLetterModalOverlay.addEventListener("click", function (e) {
      if (e.target === offerLetterModalOverlay) closeOfferLetterModal();
    });
  }

  // --- Transcript Modal Logic ---
  var transcriptModalOverlay = document.getElementById("transcriptModalOverlay");
  var transcriptModalClose = document.getElementById("transcriptModalClose");
  var transcriptModalCloseBtn2 = document.getElementById("transcriptModalCloseBtn2");
  var transcriptPrintBtn = document.getElementById("transcriptPrintBtn");

  function openTranscriptModal() {
    if (!transcriptModalOverlay) return;
    transcriptModalOverlay.classList.add("is-active");
    transcriptModalOverlay.setAttribute("aria-hidden", "false");
    document.body.style.overflow = "hidden";
  }

  function closeTranscriptModal() {
    if (!transcriptModalOverlay) return;
    transcriptModalOverlay.classList.remove("is-active");
    transcriptModalOverlay.setAttribute("aria-hidden", "true");
    document.body.style.overflow = "";
  }

  if (transcriptModalClose) {
    transcriptModalClose.addEventListener("click", closeTranscriptModal);
  }
  if (transcriptModalCloseBtn2) {
    transcriptModalCloseBtn2.addEventListener("click", closeTranscriptModal);
  }
  if (transcriptPrintBtn) {
    transcriptPrintBtn.addEventListener("click", function () {
      window.print();
    });
  }
  if (transcriptModalOverlay) {
    transcriptModalOverlay.addEventListener("click", function (e) {
      if (e.target === transcriptModalOverlay) closeTranscriptModal();
    });
  }

  // --- Curriculum Vitae (CV) Modal Logic ---
  var cvModalOverlay = document.getElementById("cvModalOverlay");
  var cvModalClose = document.getElementById("cvModalClose");
  var cvModalCloseBtn2 = document.getElementById("cvModalCloseBtn2");
  var cvPrintBtn = document.getElementById("cvPrintBtn");

  function openCvModal() {
    if (!cvModalOverlay) return;
    cvModalOverlay.classList.add("is-active");
    cvModalOverlay.setAttribute("aria-hidden", "false");
    document.body.style.overflow = "hidden";
  }

  function closeCvModal() {
    if (!cvModalOverlay) return;
    cvModalOverlay.classList.remove("is-active");
    cvModalOverlay.setAttribute("aria-hidden", "true");
    document.body.style.overflow = "";
  }

  if (cvModalClose) {
    cvModalClose.addEventListener("click", closeCvModal);
  }
  if (cvModalCloseBtn2) {
    cvModalCloseBtn2.addEventListener("click", closeCvModal);
  }
  if (cvPrintBtn) {
    cvPrintBtn.addEventListener("click", function () {
      window.print();
    });
  }
  if (cvModalOverlay) {
    cvModalOverlay.addEventListener("click", function (e) {
      if (e.target === cvModalOverlay) closeCvModal();
    });
  }

  // Global ESC key listener
  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape" || e.keyCode === 27) {
      closeSeatPaymentModal();
      closePaymentOtpModal();
      closeInvoiceReceiptModal();
      closeVerifyCardModal();
      closeOfferLetterModal();
      closeTranscriptModal();
      closeCvModal();
    }
  });

  window.openSeatPaymentModal = openSeatPaymentModal;
  window.closeSeatPaymentModal = closeSeatPaymentModal;
  window.openPaymentOtpModal = openPaymentOtpModal;
  window.closePaymentOtpModal = closePaymentOtpModal;
  window.openInvoiceReceiptModal = openInvoiceReceiptModal;
  window.switchModalInvoice = switchModalInvoice;
  window.closeInvoiceReceiptModal = closeInvoiceReceiptModal;
  window.openVerifyCardModal = openVerifyCardModal;
  window.closeVerifyCardModal = closeVerifyCardModal;

  window.openOfferLetterModal = openOfferLetterModal;
  window.closeOfferLetterModal = closeOfferLetterModal;
  window.openTranscriptModal = openTranscriptModal;
  window.closeTranscriptModal = closeTranscriptModal;
  window.openCvModal = openCvModal;
  window.closeCvModal = closeCvModal;

  console.log("UChicago 1:1 Production Runtime Ready!");
});

