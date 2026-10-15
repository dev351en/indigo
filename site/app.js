/**
 * The University of Chicago — Interactive Replica Client Script
 * Implements accessible navigation, search overlay, video controls, and responsive drawers.
 */

document.addEventListener("DOMContentLoaded", () => {
  // --- 1. Info For Dropdown ---
  const infoBtn = document.getElementById("infoDropdownBtn");
  const infoMenu = document.getElementById("infoDropdownMenu");
  const infoWrap = document.querySelector(".info-dropdown-wrap");

  if (infoBtn && infoMenu) {
    infoBtn.addEventListener("click", (e) => {
      e.stopPropagation();
      const isExpanded = infoBtn.getAttribute("aria-expanded") === "true";
      infoBtn.setAttribute("aria-expanded", !isExpanded);
      infoMenu.hidden = isExpanded;
      infoWrap.classList.toggle("open", !isExpanded);
    });

    // Close when clicking outside
    document.addEventListener("click", (e) => {
      if (!infoWrap.contains(e.target)) {
        infoBtn.setAttribute("aria-expanded", "false");
        infoMenu.hidden = true;
        infoWrap.classList.remove("open");
      }
    });
  }

  // --- 2. Search Flyout Overlay ---
  const searchBtn = document.getElementById("searchToggleBtn");
  const searchFlyout = document.getElementById("searchFlyout");
  const searchCloseBtn = document.getElementById("searchCloseBtn");
  const searchInput = document.getElementById("searchInput");

  function openSearch() {
    searchFlyout.hidden = false;
    searchBtn.setAttribute("aria-expanded", "true");
    setTimeout(() => searchInput && searchInput.focus(), 50);
  }

  function closeSearch() {
    searchFlyout.hidden = true;
    searchBtn.setAttribute("aria-expanded", "false");
  }

  if (searchBtn && searchFlyout && searchCloseBtn) {
    searchBtn.addEventListener("click", (e) => {
      e.stopPropagation();
      if (searchFlyout.hidden) {
        openSearch();
      } else {
        closeSearch();
      }
    });

    searchCloseBtn.addEventListener("click", closeSearch);

    // Escape key closes search
    document.addEventListener("keydown", (e) => {
      if (e.key === "Escape" && !searchFlyout.hidden) {
        closeSearch();
      }
    });
  }

  // --- 3. Mobile Navigation Drawer & Accordions ---
  const mobileToggle = document.getElementById("mobileMenuToggle");
  const mobileDrawer = document.getElementById("mobileNavDrawer");

  if (mobileToggle && mobileDrawer) {
    mobileToggle.addEventListener("click", () => {
      const isExpanded = mobileToggle.getAttribute("aria-expanded") === "true";
      mobileToggle.setAttribute("aria-expanded", !isExpanded);
      mobileDrawer.hidden = isExpanded;
    });

    // Sub-accordion buttons
    const accordionBtns = mobileDrawer.querySelectorAll(".mobile-accordion-btn");
    accordionBtns.forEach((btn) => {
      btn.addEventListener("click", () => {
        const isCurrentOpen = btn.getAttribute("aria-expanded") === "true";
        const panel = btn.nextElementSibling;
        
        btn.setAttribute("aria-expanded", !isCurrentOpen);
        if (panel) {
          panel.hidden = isCurrentOpen;
        }
      });
    });
  }

  // --- 4. Hero Video Play / Pause Toggle ---
  const heroVideo = document.getElementById("heroVideo");
  const playPauseBtn = document.getElementById("videoPlayPauseBtn");
  const playPauseIcon = document.getElementById("playPauseIcon");

  if (heroVideo && playPauseBtn && playPauseIcon) {
    playPauseBtn.addEventListener("click", () => {
      if (heroVideo.paused) {
        heroVideo.play();
        playPauseIcon.className = "fa fa-pause";
        playPauseBtn.setAttribute("aria-label", "Pause spotlight video");
        playPauseBtn.setAttribute("aria-pressed", "false");
      } else {
        heroVideo.pause();
        playPauseIcon.className = "fa fa-play";
        playPauseBtn.setAttribute("aria-label", "Play spotlight video");
        playPauseBtn.setAttribute("aria-pressed", "true");
      }
    });
  }

  // --- 5. Campaign Carousel Dots ---
  const dots = document.querySelectorAll(".carousel-dots .dot-btn");
  dots.forEach((dot, idx) => {
    dot.addEventListener("click", () => {
      dots.forEach((d) => d.classList.remove("active"));
      dot.classList.add("active");
    });
  });

  // --- 6. Scroll Detection on Header ---
  const header = document.getElementById("header");
  if (header) {
    window.addEventListener("scroll", () => {
      if (window.scrollY > 80) {
        header.setAttribute("data-scrolldown", "true");
      } else {
        header.setAttribute("data-scrolldown", "false");
      }
    }, { passive: true });
  }

  // --- 7. Admissions Application Portal Modal ---
  const portalOverlay = document.getElementById("portalModalOverlay");
  const portalCloseBtn = document.getElementById("portalModalClose");
  const portalTriggers = document.querySelectorAll("#portalTriggerBtn, #portalTriggerBtn-mobile, .portal-trigger-btn");
  const applicantIdInput = document.getElementById("applicantId");
  const applicantPwInput = document.getElementById("applicantPassword");
  const pwToggleBtn = document.getElementById("portalPasswordToggle");
  const pwIcon = document.getElementById("portalPwIcon");
  const loginForm = document.getElementById("admissionsLoginForm");
  const portalNotice = document.getElementById("portalNotice");

  function openPortal() {
    if (!portalOverlay) return;
    portalOverlay.classList.add("is-active");
    portalOverlay.setAttribute("aria-hidden", "false");
    document.body.style.overflow = "hidden";
    portalTriggers.forEach((btn) => btn.setAttribute("aria-expanded", "true"));
    setTimeout(() => {
      if (applicantIdInput) applicantIdInput.focus();
    }, 150);
  }

  function closePortal() {
    if (!portalOverlay) return;
    portalOverlay.classList.remove("is-active");
    portalOverlay.setAttribute("aria-hidden", "true");
    document.body.style.overflow = "";
    portalTriggers.forEach((btn) => btn.setAttribute("aria-expanded", "false"));
    if (window.location.hash === "#portal" || window.location.hash === "#login") {
      history.replaceState(null, null, " ");
    }
  }

  portalTriggers.forEach((btn) => {
    btn.addEventListener("click", (e) => {
      e.preventDefault();
      openPortal();
    });
  });

  if (portalCloseBtn) {
    portalCloseBtn.addEventListener("click", (e) => {
      e.preventDefault();
      closePortal();
    });
  }

  if (portalOverlay) {
    portalOverlay.addEventListener("click", (e) => {
      if (e.target === portalOverlay) {
        closePortal();
      }
    });
  }

  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape" && portalOverlay && portalOverlay.classList.contains("is-active")) {
      closePortal();
    }
  });

  if (pwToggleBtn && applicantPwInput && pwIcon) {
    pwToggleBtn.addEventListener("click", (e) => {
      e.preventDefault();
      const isPassword = applicantPwInput.getAttribute("type") === "password";
      applicantPwInput.setAttribute("type", isPassword ? "text" : "password");
      pwIcon.className = isPassword ? "fa-regular fa-eye-slash" : "fa-regular fa-eye";
      pwToggleBtn.setAttribute("aria-label", isPassword ? "Hide password" : "Show password");
    });
  }

  // --- Credentials Configuration ---
  const VALID_APP_ID = "UC-2027-89321";
  const VALID_EMAIL = "DUBEY351DEV@GMAIL.COM";
  const VALID_PASSWORD = "9833@dEVuc";

  const portalLoginView = document.getElementById("portalLoginView");
  const portalDashboardView = document.getElementById("portalDashboardView");
  const portalSubmitBtn = document.getElementById("portalSubmitBtn");
  const portalTitle = document.getElementById("portalTitle");
  const portalSubtitle = document.querySelector(".portal-subtitle");
  const portalLogoutBtn = document.getElementById("portalLogoutBtn");
  const portalPrintBtn = document.getElementById("portalPrintBtn");

  if (loginForm) {
    loginForm.addEventListener("submit", (e) => {
      e.preventDefault();
      const idVal = applicantIdInput ? applicantIdInput.value.trim() : "";
      const pwVal = applicantPwInput ? applicantPwInput.value : "";

      // Clear previous error states
      if (applicantIdInput) applicantIdInput.classList.remove("is-invalid");
      if (applicantPwInput) applicantPwInput.classList.remove("is-invalid");

      if (!idVal || !pwVal) {
        if (portalNotice) {
          portalNotice.className = "portal-alert-msg is-error";
          portalNotice.innerHTML = '<i class="fa-solid fa-circle-exclamation"></i><span>Please enter both your Application ID / Email and your Password.</span>';
        }
        if (!idVal && applicantIdInput) applicantIdInput.classList.add("is-invalid");
        if (!pwVal && applicantPwInput) applicantPwInput.classList.add("is-invalid");
        return;
      }

      // Check credentials (case-insensitive for ID/email, exact for password)
      const idClean = idVal.toUpperCase();
      const isIdMatch = (idClean === VALID_APP_ID || idClean === VALID_EMAIL);
      const isPwMatch = (pwVal === VALID_PASSWORD);

      if (portalSubmitBtn) {
        portalSubmitBtn.disabled = true;
        portalSubmitBtn.innerHTML = '<i class="fa fa-spinner fa-spin" style="margin-right: 8px;"></i> Authenticating...';
      }

      setTimeout(() => {
        if (portalSubmitBtn) {
          portalSubmitBtn.disabled = false;
          portalSubmitBtn.textContent = 'Log In to Portal';
        }

        if (isIdMatch && isPwMatch) {
          // Success: Switch to Authenticated Dashboard
          if (portalLoginView) portalLoginView.style.display = "none";
          if (portalDashboardView) portalDashboardView.style.display = "block";
          if (portalTitle) portalTitle.textContent = "Welcome, Devendra Biswambhar Nath Dubey";
          if (portalSubtitle) {
            portalSubtitle.setAttribute("spellcheck", "false");
            portalSubtitle.textContent = "Doctor of Philosophy in Chemistry \u2014 Computational Chemistry \u2022 Division of the Physical Sciences \u2022 Autumn Quarter 2027";
          }
        } else {
          // Failure: Display Error Message
          if (portalNotice) {
            portalNotice.className = "portal-alert-msg is-error";
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
    portalLogoutBtn.addEventListener("click", () => {
      if (portalDashboardView) portalDashboardView.style.display = "none";
      if (portalLoginView) portalLoginView.style.display = "block";
      if (portalTitle) portalTitle.textContent = "Applicant Status Portal";
      if (portalSubtitle) portalSubtitle.textContent = "Log in with your UChicago Account to review your application status, upload supplementary materials, and access admissions updates.";
      if (portalNotice) {
        portalNotice.className = "portal-alert-msg is-info";
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
    });
  }

  // Handle Print Summary
  if (portalPrintBtn) {
    portalPrintBtn.addEventListener("click", () => {
      window.print();
    });
  }

  // Handle Resume File Upload & Preview
  const resumeFileInput = document.getElementById("resumeFileInput");
  const portalResumeFileName = document.getElementById("portalResumeFileName");
  const portalResumeFileMeta = document.getElementById("portalResumeFileMeta");
  const portalResumeBadge = document.getElementById("portalResumeBadge");
  const resumeUploadFeedback = document.getElementById("resumeUploadFeedback");
  const portalResumePreviewBtn = document.getElementById("portalResumePreviewBtn");

  if (resumeFileInput) {
    resumeFileInput.addEventListener("change", () => {
      if (resumeFileInput.files && resumeFileInput.files[0]) {
        const file = resumeFileInput.files[0];
        const sizeKb = Math.round(file.size / 1024);
        if (portalResumeFileName) portalResumeFileName.textContent = file.name;
        if (portalResumeFileMeta) portalResumeFileMeta.textContent = `Uploaded Document • ${sizeKb} KB • Verified`;
        if (portalResumeBadge) {
          portalResumeBadge.textContent = "Updated (Official)";
          portalResumeBadge.className = "portal-badge-received";
        }
        if (resumeUploadFeedback) {
          resumeUploadFeedback.style.display = "block";
          setTimeout(() => {
            resumeUploadFeedback.style.display = "none";
          }, 4000);
        }
      }
    });
  }

  if (portalResumePreviewBtn) {
    portalResumePreviewBtn.addEventListener("click", () => {
      const currentName = portalResumeFileName ? portalResumeFileName.textContent : "Curriculum Vitae";
      alert(`Opening verified document for preview:\n${currentName}\n\nUChicago Admissions Management System`);
    });
  }

  // Handle Seat Confirmation Deposit ($6,200.00 USD)
  const portalPayDepositBtn = document.getElementById("portalPayDepositBtn");
  const portalDepositStatusBadge = document.getElementById("portalDepositStatusBadge");
  const portalDepositReceiptWrap = document.getElementById("portalDepositReceiptWrap");

  function applySeatDepositPaidState() {
    if (portalDepositStatusBadge) {
      portalDepositStatusBadge.className = "portal-deposit-badge is-paid";
      portalDepositStatusBadge.innerHTML = '<i class="fa-solid fa-circle-check"></i> Seat Secured &amp; Deposit Paid';
    }
    if (portalPayDepositBtn) {
      portalPayDepositBtn.disabled = true;
      portalPayDepositBtn.style.background = "#176531";
      portalPayDepositBtn.innerHTML = '<i class="fa-solid fa-check"></i> Deposit Paid ($6,200.00 Received)';
    }
    if (portalDepositReceiptWrap) {
      portalDepositReceiptWrap.style.display = "inline-block";
    }
  }

  if (sessionStorage.getItem("seatDepositPaid") === "true") {
    applySeatDepositPaidState();
  }

  if (portalPayDepositBtn) {
    portalPayDepositBtn.addEventListener("click", () => {
      const confirmPay = confirm(
        "University of Chicago - Division of the Physical Sciences\n\n" +
        "Ph.D. Matriculation Seat Confirmation Deposit\n" +
        "Program: Ph.D. in Chemistry (Computational Chemistry)\n" +
        "Term: Autumn Quarter 2027 (August 2027)\n" +
        "Amount: $6,200.00 USD\n\n" +
        "Do you wish to authorize this payment via UChicago Secure Bursar Services?"
      );

      if (confirmPay) {
        portalPayDepositBtn.disabled = true;
        portalPayDepositBtn.innerHTML = '<i class="fa fa-spinner fa-spin"></i> Processing $6,200.00 Payment...';

        setTimeout(() => {
          sessionStorage.setItem("seatDepositPaid", "true");
          applySeatDepositPaidState();
          alert(
            "Payment Successful!\n\n" +
            "Transaction Ref: #UCHI-DEP-2027-6200\n" +
            "Amount Paid: $6,200.00 USD\n" +
            "Status: Graduate Seat Confirmed for Autumn 2027 (August 2027)\n" +
            "An official receipt has been sent to dubey351dev@gmail.com."
          );
        }, 800);
      }
    });
  }

  console.log("University of Chicago Replica initialized successfully.");
});


