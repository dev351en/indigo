import os
import re

base_dir = os.path.dirname(os.path.abspath(__file__))
site_dir = os.path.join(base_dir, "..", "site_1to1")

files_to_update = [
    os.path.join(site_dir, "portal.html"),
    os.path.join(site_dir, "pages", "portal.html"),
    os.path.join(site_dir, "index.html"),
]

for file_path in files_to_update:
    if not os.path.exists(file_path):
        continue
    with open(file_path, "r", encoding="utf-8") as f:
        html = f.read()

    rel_prefix = "../" if "/pages/" in file_path.replace("\\", "/") else ""

    # 1. Update Application Fee row in Applicant Dossier
    old_app_fee_pattern = re.compile(
        r'<div><strong>Application Fee:</strong>\s*<span[^>]*>.*?\$90\.00 Paid \(Received\)</span></div>',
        re.DOTALL
    )
    new_app_fee_html = f'''<div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 8px;">
                <div>
                  <strong>Application Fee:</strong>
                  <span style="color: #137333; font-weight: 700; display: inline-flex; align-items: center; gap: 4px; margin-left: 4px;">
                    <i class="fa-solid fa-circle-check"></i> $90.00 Paid (Received)
                  </span>
                  <span style="font-size: 11px; color: #666; margin-left: 6px;">• 01 Oct 2026, 6:30 AM IST</span>
                </div>
                <div style="display: flex; gap: 8px; align-items: center;">
                  <button type="button" id="btnViewAppFeeReceipt" class="portal-mini-receipt-badge" style="background: #800000; color: #ffffff; border: none; padding: 4px 11px; border-radius: 3px; font-size: 11px; font-weight: 700; cursor: pointer; display: inline-flex; align-items: center; gap: 5px; transition: background 0.15s ease;">
                    <i class="fa-solid fa-file-invoice-dollar"></i> View Application Fee Receipt
                  </button>
                  <a href="{rel_prefix}application-fee-receipt.html" target="_blank" style="font-size: 11px; color: #800000; font-weight: 600; text-decoration: underline; display: inline-flex; align-items: center; gap: 3px;">
                    Web View <i class="fa-solid fa-arrow-up-right-from-square"></i>
                  </a>
                </div>
              </div>'''

    html, count_app = old_app_fee_pattern.subn(lambda m: new_app_fee_html, html)
    print(f"Updated application fee row in {os.path.basename(file_path)}: count={count_app}")

    # 2. Update Bursar sidebar card to include Application Fee line
    old_bursar_sidebar_pattern = re.compile(
        r'(<div><strong>Tuition Waiver:</strong> 100% Remission Active</div>)',
        re.IGNORECASE
    )
    new_bursar_sidebar_addition = f'''\\1
              <div style="margin-top: 10px; padding: 8px 10px; background: #f0f7f2; border: 1px solid #c2e2cc; border-radius: 3px;">
                <div style="font-size: 11px; font-weight: 700; color: #137333;"><i class="fa-solid fa-circle-check"></i> Application Fee: $90.00 Paid</div>
                <div style="font-size: 10.5px; color: #555; margin-top: 1px;">Settled 01 Oct 2026, 6:30 AM IST • Discover Debit (•••• 0405)</div>
                <a href="#" onclick="event.preventDefault(); if (window.openInvoiceReceiptModal) window.openInvoiceReceiptModal('app_fee');" style="font-size: 11px; color: maroon; font-weight: 700; text-decoration: underline; margin-top: 3px; display: inline-block;">
                  <i class="fa-solid fa-receipt"></i> View Application Receipt
                </a>
              </div>'''

    if 'Application Fee: $90.00 Paid' not in html:
        html, count_bursar = old_bursar_sidebar_pattern.subn(new_bursar_sidebar_addition, html)
        print(f"Added app fee line to Bursar sidebar in {os.path.basename(file_path)}: count={count_bursar}")

    # 3. Upgrade Invoice Receipt Modal with Switcher Tabs
    old_modal_card_header = re.compile(
        r'<div class="portal-transcript-modal-card">.*?<div class="portal-transcript-modal-body">',
        re.DOTALL
    )

    new_modal_card_header = f'''<div class="portal-transcript-modal-card">
      <!-- Modal Header -->
      <div class="portal-transcript-modal-header" style="background: #fafafa; border-bottom: 1px solid #e0e0e0; padding: 14px 20px;">
        <div style="display: flex; align-items: center; gap: 12px;">
          <div style="width: 38px; height: 38px; border-radius: 50%; background: #fdf2f2; border: 1.5px solid maroon; display: flex; align-items: center; justify-content: center; color: maroon; font-size: 18px; flex-shrink: 0;">
            <i class="fa-solid fa-file-invoice-dollar"></i>
          </div>
          <div>
            <h2 id="invoiceReceiptModalTitle" style="font-family: 'UChicagoSerif', Georgia, serif; font-size: 17px; margin: 0; color: #111;">
              Official Bursar Tax Receipt &amp; Enrollment Mandate
            </h2>
            <div id="invoiceReceiptModalSubtitle" style="font-size: 11.5px; color: #555; margin-top: 2px;">
              Candidate: <strong>Devendra Dubey</strong> • Ref: <strong>REF-UCHI-DEP-2027-6200</strong> • Paid: <strong>$6,200.00 USD</strong> • Status: <strong>PAID IN FULL</strong>
            </div>
          </div>
        </div>
        <div style="display: flex; align-items: center; gap: 8px;">
          <button type="button" id="receiptPrintBtn" style="background: #ffffff; border: 1px solid #ccc; color: #333; padding: 6px 12px; font-size: 12px; font-weight: 600; cursor: pointer; border-radius: 2px; display: inline-flex; align-items: center; gap: 5px;">
            <i class="fa-solid fa-print"></i> Print
          </button>
          <a id="modalDownloadPdfBtn" href="{rel_prefix}assets/documents/Official_Receipt_UCHI_2027_6200.pdf" target="_blank" download="Official_Receipt_UCHI_2027_6200.pdf" style="background: maroon; color: #fff; text-decoration: none; padding: 6px 14px; font-size: 12px; font-weight: 700; border-radius: 2px; display: inline-flex; align-items: center; gap: 6px;">
            <i class="fa-solid fa-download"></i> Download PDF
          </a>
          <button type="button" id="receiptModalClose" aria-label="Close" style="background: transparent; border: none; font-size: 26px; line-height: 1; cursor: pointer; color: #666; padding: 0 4px; margin-left: 4px;">&times;</button>
        </div>
      </div>

      <!-- Invoice Switcher Tab Bar -->
      <div style="background: #f0f2f5; padding: 6px 20px; border-bottom: 1px solid #e0e0e0; display: flex; gap: 8px; align-items: center; justify-content: space-between; flex-wrap: wrap;">
        <div class="receipt-tab-group" style="display: inline-flex; background: #e2e6ea; padding: 3px; border-radius: 4px; border: 1px solid #ced4da; gap: 4px;">
          <button type="button" class="receipt-tab-btn is-active" id="modalTabSeatDeposit" onclick="switchModalInvoice('seat_deposit')" style="background: #ffffff; color: #800000; border: none; padding: 5px 12px; border-radius: 3px; font-size: 11.5px; font-weight: 700; cursor: pointer; display: inline-flex; align-items: center; gap: 5px; box-shadow: 0 1px 3px rgba(0,0,0,0.15);">
            <i class="fa-solid fa-certificate"></i> Seat Locking Deposit ($6,200)
          </button>
          <button type="button" class="receipt-tab-btn" id="modalTabAppFee" onclick="switchModalInvoice('app_fee')" style="background: transparent; color: #495057; border: none; padding: 5px 12px; border-radius: 3px; font-size: 11.5px; font-weight: 600; cursor: pointer; display: inline-flex; align-items: center; gap: 5px;">
            <i class="fa-solid fa-file-invoice-dollar"></i> Application Fee ($90 - 01 Oct 2026)
          </button>
        </div>
        <div id="modalInvoiceDateTag" style="font-size: 11px; color: #137333; font-weight: 600;">
          <i class="fa-solid fa-circle-check"></i> Form 1098-T Eligible • Settled via Discover (•••• 0405)
        </div>
      </div>

      <div class="portal-transcript-modal-body">'''

    html, count_modal_head = old_modal_card_header.subn(lambda m: new_modal_card_header, html)
    print(f"Updated modal card header in {os.path.basename(file_path)}: count={count_modal_head}")

    # 4. Update the image tag inside invoiceReceiptModalOverlay to give it an ID
    old_img_pattern = re.compile(
        r'<img src="[^"]*receipt_page_1\.png"[^>]*alt="Official Student Accounts Tax Receipt[^"]*"[^>]*/>'
    )
    new_img_tag = f'<img id="modalReceiptImg" src="{rel_prefix}assets/documents/receipt_page_1.png" alt="Official Student Accounts Tax Receipt &amp; Enrollment Mandate - Devendra Dubey" />'
    html, count_img = old_img_pattern.subn(new_img_tag, html)
    print(f"Updated modal receipt image tag in {os.path.basename(file_path)}: count={count_img}")

    # 5. Update footer link of receipt modal
    old_footer_link_pattern = re.compile(
        r'<a href="receipt\.html" target="_blank"[^>]*>.*?Open Web Receipt.*?</a>',
        re.DOTALL
    )
    new_footer_link = f'<a id="modalWebReceiptLink" href="{rel_prefix}receipt.html?type=seat_deposit" target="_blank" style="color: maroon; font-weight: 700; text-decoration: underline; font-size: 12px; display: inline-flex; align-items: center; gap: 4px;">Open Web Receipt <i class="fa-solid fa-arrow-up-right-from-square"></i></a>'
    html, count_foot = old_footer_link_pattern.subn(new_footer_link, html)
    print(f"Updated modal footer link in {os.path.basename(file_path)}: count={count_foot}")

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Successfully saved {file_path}")
