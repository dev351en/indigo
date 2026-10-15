import os

file_path = "site_1to1/interactive_runtime.js"

with open(file_path, "r", encoding="utf-8") as f:
    code = f.read()

# 1. Replace openInvoiceReceiptModal implementation
old_modal_func = '''  function openInvoiceReceiptModal() {
    if (!invoiceReceiptModalOverlay) return;
    invoiceReceiptModalOverlay.classList.add("is-active");
    invoiceReceiptModalOverlay.setAttribute("aria-hidden", "false");
    document.body.style.overflow = "hidden";
  }'''

new_modal_func = '''  function switchModalInvoice(type) {
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
  }'''

if old_modal_func in code:
    code = code.replace(old_modal_func, new_modal_func, 1)
    print("Replaced openInvoiceReceiptModal with switchModalInvoice support")
else:
    print("WARNING: old_modal_func not found directly")

# 2. Add listener for #btnViewAppFeeReceipt
btn_app_fee_code = '''
  var btnViewAppFeeReceipt = document.getElementById("btnViewAppFeeReceipt");
  if (btnViewAppFeeReceipt) {
    btnViewAppFeeReceipt.addEventListener("click", function (e) {
      e.preventDefault();
      openInvoiceReceiptModal("app_fee");
    });
  }
'''

if "btnViewAppFeeReceipt" not in code:
    anchor = 'if (portalPayDepositBtn) {'
    if anchor in code:
        code = code.replace(anchor, btn_app_fee_code + "\n  " + anchor, 1)
        print("Added btnViewAppFeeReceipt listener")

# 3. Expose switchModalInvoice on window
expose_anchor = 'window.openInvoiceReceiptModal = openInvoiceReceiptModal;'
new_expose = 'window.openInvoiceReceiptModal = openInvoiceReceiptModal;\n  window.switchModalInvoice = switchModalInvoice;'
if expose_anchor in code and "window.switchModalInvoice" not in code:
    code = code.replace(expose_anchor, new_expose, 1)
    print("Exposed window.switchModalInvoice")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(code)

print("Updated site_1to1/interactive_runtime.js successfully!")
