import os
import re

def sync_admissions_hub():
    path = "site_1to1/pages/admissions.html"
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    # In admissions.html, update the Graduate Admissions tile description & link to highlight the 100% full funding / fellowship guarantee, and ensure Financial Aid & Tuition is prominently linked.
    # Look for Graduate admissions tile
    old_grad_pattern = r'(<h2 class="CalloutTiles_title__11Ltk">Graduate admissions</h2></div><div class="CalloutTiles_calendarLinkContainer__3Ictp"><p class="CalloutTiles_description__3qbDt">)(.*?)(</p></div><div class="CalloutTiles_ctaContainer__3hOWO"><a href=")(.*?)(" class="CalloutTiles_cta__1Iiwv"[^>]*>)'
    
    new_grad_desc = "Doctoral scholars across physical sciences and graduate divisions receive 100% full tuition remission, guaranteed annual living stipends ($36,000+), comprehensive U-SHIP health coverage, and multi-year faculty research sponsorships."
    
    def repl_grad(m):
        return f'{m.group(1)}{new_grad_desc}{m.group(3)}admissions_financial-aid-and-tuition.html#doctoral-fellowships{m.group(5)}'

    new_text, count = re.subn(old_grad_pattern, repl_grad, text, count=1)
    print(f"Updated Graduate Admissions in admissions.html: {count} replacement(s)")

    # Check if we can also add a dedicated Financial Aid & Fellowship Spotlight Banner right after the callout tiles
    spotlight_marker = '</section><section class="CalloutTiles_container__2AH3J single-col-inner" data-tilesperrow="three"'
    if spotlight_marker in new_text:
        fellowship_spotlight = """</section>
<!-- Graduate Fellowship & Financial Aid Spotlight Banner (Offer Letter Design Format) -->
<section class="single-col-wide" style="margin: 30px 0;">
  <div class="single-col-inner">
    <div style="background: #faf8f5; border: 1.5px solid #800000; border-radius: 6px; padding: 26px 30px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 20px; box-shadow: 0 4px 16px rgba(128,0,0,0.06);">
      <div style="max-width: 680px;">
        <div style="font-size: 11px; font-weight: 800; text-transform: uppercase; letter-spacing: 0.6px; color: #800000; margin-bottom: 6px;">
          <i class="fa-solid fa-award"></i> GRADUATE FELLOWSHIPS &amp; FINANCIAL GUARANTEES
        </div>
        <h3 style="font-family: 'UChicagoSerif', Georgia, serif; font-size: 22px; color: #800000; margin: 0 0 8px;">
          100% Fully Funded Doctoral Education &amp; Stipend Guarantees
        </h3>
        <p style="font-size: 14px; color: #444; line-height: 1.55; margin: 0;">
          All admitted Ph.D. candidates in the Division of the Physical Sciences, Chemistry, and graduate disciplines receive 100% full tuition remission ($60,000/yr), a guaranteed living stipend of $3,000/month ($36,000/yr), full U-SHIP health coverage, and a 100% reimbursable seat confirmation deposit.
        </p>
      </div>
      <div style="display: flex; gap: 10px; flex-wrap: wrap;">
        <a href="admissions_financial-aid-and-tuition.html#offer-letter-matrix" class="portal-btn-primary" style="background: #800000; color: #ffffff; text-decoration: none; padding: 11px 20px; font-size: 13px; font-weight: 700; border-radius: 4px;">
          <i class="fa-solid fa-file-contract"></i> View Fellowship Matrix
        </a>
        <a href="admissions_financial-aid-and-tuition.html" class="portal-btn-outline" style="border-color: #800000; color: #800000; text-decoration: none; padding: 11px 18px; font-size: 13px; font-weight: 700; border-radius: 4px;">
          Tuition &amp; Fees Schedule <i class="fa-solid fa-arrow-right" style="font-size: 11px;"></i>
        </a>
      </div>
    </div>
  </div>
</section>
<section class="CalloutTiles_container__2AH3J single-col-inner" data-tilesperrow="three" """
        new_text = new_text.replace(spotlight_marker, fellowship_spotlight, 1)
        print("Inserted Fellowship Spotlight Banner into admissions.html")

    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)

def sync_affordability():
    path = "site_1to1/pages/admissions_affordability.html"
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    # In admissions_affordability.html, update the Ph.D. Programs description & CTA link
    old_phd_tile = r'(<h2 class="CalloutTiles_title__11Ltk">Ph\.D\. Programs</h2></div><div class="CalloutTiles_calendarLinkContainer__3Ictp"><p class="CalloutTiles_description__3qbDt">)(.*?)(</p></div><div class="CalloutTiles_ctaContainer__3hOWO"><a href=")(.*?)(" class="CalloutTiles_cta__1Iiwv"[^>]*>)'
    
    new_phd_desc = "Doctoral scholars in the physical sciences and graduate divisions receive 100% full funding packages covering full tuition remission ($60,000/year value), full U-SHIP platinum health insurance, and a guaranteed living stipend of at least $36,000 ($3,000/month) for the duration of the program, with zero net tuition liability."

    def repl_phd(m):
        return f'{m.group(1)}{new_phd_desc}{m.group(3)}admissions_financial-aid-and-tuition.html#doctoral-fellowships{m.group(5)}'

    new_text, count = re.subn(old_phd_tile, repl_phd, text, count=1)
    print(f"Updated Ph.D. tile in admissions_affordability.html: {count} replacement(s)")

    # Insert a link to the Master Financial Aid & Fellowship Matrix right under Graduate outcomes
    grad_outcomes_marker = '<h3 class="Factoids_title__1Jz1V">Master&#x27;s and Ph.D. outcomes</h3>'
    if grad_outcomes_marker in new_text:
        offer_letter_box = """<h3 class="Factoids_title__1Jz1V">Master&#x27;s and Ph.D. outcomes</h3></div><div style="margin: 12px 0 20px; background: #faf4f4; border-left: 4px solid #800000; padding: 14px 18px; border-radius: 0 4px 4px 0;"><div style="font-size: 13.5px; color: #333; line-height: 1.5;"><strong>Physical Sciences &amp; Chemistry Doctoral Fellowship Standard:</strong> 100% Full Tuition Remission ($20,000/sem) • $3,000/Month Living Stipend • Comprehensive U-SHIP Platinum Health • $6,200 Seat Confirmation Deposit with 100% 90-Day Reimbursement and 90-Business-Day Visa Refund Guarantee. <a href="admissions_financial-aid-and-tuition.html#offer-letter-matrix" style="color: #800000; font-weight: 700; margin-left: 6px;">View Complete Master Fellowship Matrix &rarr;</a></div></div><div class="Factoids_contentDescription__VrS3r" style="display:none;"""
        new_text = new_text.replace(grad_outcomes_marker, grad_outcomes_marker + '</div><div style="margin: 14px 0 20px; background: #faf4f4; border-left: 4px solid #800000; padding: 14px 18px; border-radius: 0 4px 4px 0;"><div style="font-size: 13.5px; color: #333; line-height: 1.5;"><strong>Physical Sciences &amp; Chemistry Doctoral Fellowship Guarantee:</strong> 100% Full Tuition Remission ($20,000/sem, $60,000/yr) • $3,000/Month Living Stipend • 100% U-SHIP Platinum Health Coverage • $6,200 Seat Deposit with 90-Day Bursar Reimbursement &amp; 90-Business-Day Visa Protection. <a href="admissions_financial-aid-and-tuition.html#offer-letter-matrix" style="color: #800000; font-weight: 700; margin-left: 6px;">View Complete Master Fellowship Matrix &rarr;</a></div>', 1)
        print("Added Fellowship callout to admissions_affordability.html")

    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)

def sync_international():
    path = "site_1to1/pages/admissions_international-students.html"
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    # Update Graduate Funding link to point to admissions_financial-aid-and-tuition.html#international-aid
    old_link = 'href="https://grad.uchicago.asia/admissions/funding/international-students/"'
    new_link = 'href="admissions_financial-aid-and-tuition.html#international-aid"'
    new_text = text.replace(old_link, new_link)

    # Also add a dedicated International Fellowships & Visa Verification callout before quick links
    marker = '<section class="QuickLinks_container__MjOHH QuickLinks_buttonLayout___aGUk single-col-inner"><div class=""><h3 class="QuickLinks_header__f9c33 sans-head-3">Information for graduate students</h3>'
    if marker in new_text:
        callout = """<section class="single-col-wide" style="margin: 24px 0;">
  <div class="single-col-inner">
    <div style="background: #faf8f5; border: 1px solid #e5ded5; border-left: 4px solid #800000; border-radius: 4px; padding: 22px 26px; box-shadow: 0 3px 12px rgba(0,0,0,0.04);">
      <h3 style="font-family: 'UChicagoSerif', Georgia, serif; font-size: 20px; color: #800000; margin: 0 0 8px;">
        <i class="fa-solid fa-passport"></i> International Doctoral Fellowships &amp; Visa Clearance
      </h3>
      <p style="font-size: 14px; color: #444; line-height: 1.55; margin: 0 0 12px;">
        Because all Ph.D. scholars receive 100% full tuition remission ($60,000/yr) and guaranteed living stipends ($3,000/mo, $36,000/yr), institutional fellowship award letters serve as official proof of funds for Form I-20 / DS-2019 issuance. Additionally, the $6,200 seat confirmation deposit carries a <strong>100% refund guarantee within 90 business days</strong> if visa delays or travel restrictions occur.
      </p>
      <div style="display: flex; gap: 10px; align-items: center; flex-wrap: wrap;">
        <a href="admissions_financial-aid-and-tuition.html#offer-letter-matrix" style="color: #800000; font-weight: 700; font-size: 13.5px; text-decoration: none;">
          <i class="fa-solid fa-file-contract"></i> View Fellowship Matrix &amp; Terms &rarr;
        </a>
      </div>
    </div>
  </div>
</section>
""" + marker
        new_text = new_text.replace(marker, callout, 1)
        print("Added International Fellowship Callout to admissions_international-students.html")

    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)

sync_admissions_hub()
sync_affordability()
sync_international()
print("All admissions domain pages synchronized successfully!")
