import re
from pathlib import Path

PAGES_DIR = Path(r"d:\Microvirt\OBSIDIAN\uchicago_replica\site_1to1\pages")

# 1. Update academics_graduate-programs_phd-programs.html
phd_page = PAGES_DIR / "academics_graduate-programs_phd-programs.html"
if phd_page.exists():
    text = phd_page.read_text(encoding="utf-8")
    target = '<h2 style="text-align: left;">Explore programs across UChicago&rsquo;s divisions and schools</h2>'
    callout = '''<div class="fin-policy-callout" style="background:#faf8f5; border:1px solid #e0d6cb; border-left:4px solid #800000; padding:18px 22px; border-radius:0 4px 4px 0; margin-bottom:24px;">
  <div style="display:flex; justify-content:space-between; align-items:baseline; flex-wrap:wrap; margin-bottom:8px;">
    <h3 style="font-family:'UChicagoSerif', Georgia, serif; font-size:18px; color:#800000; margin:0; font-weight:700;">
      <i class="fa-solid fa-graduation-cap" style="margin-right:6px;"></i>Guaranteed Doctoral Fellowship &amp; Financial Support
    </h3>
    <span style="font-size:11.5px; font-weight:700; color:#2e7d32; background:#e8f5e9; padding:2px 8px; border-radius:3px;">
      100% Fully Funded Ph.D. Education
    </span>
  </div>
  <p style="font-size:13.5px; color:#333; line-height:1.6; margin:0 0 10px;">
    The University of Chicago guarantees comprehensive multi-year financial packages for doctoral candidates in good academic standing. This includes <strong>100% Full Tuition Remission</strong> ($20,000.00/semester &bull; $60,000.00/year), competitive living stipends (<strong>$3,000.00/month &bull; $36,000.00/year</strong> minimum), and individual <strong>U-SHIP Platinum Health, Dental &amp; Vision</strong> coverage fully paid by the University.
  </p>
  <div style="font-size:12.5px; color:#555; margin-bottom:12px;">
    <strong>Matriculation Commitment:</strong> The $6,200.00 Ph.D. seat confirmation deposit is <strong>100% reimbursable within 90 days</strong> of semester commencement, and <strong>100% refundable within 90 business days</strong> for visa or administrative complications.
  </div>
  <div style="display:flex; gap:12px; align-items:center; flex-wrap:wrap;">
    <a href="admissions_financial-aid-and-tuition.html#doctoral-fellowships" style="background:#800000; color:#fff; text-decoration:none; padding:6px 14px; border-radius:3px; font-size:13px; font-weight:700; display:inline-flex; align-items:center; gap:6px;">
      <i class="fa-solid fa-table-list"></i> View Fellowship Breakdown Matrix &rarr;
    </a>
    <a href="../portal.html" style="background:#fff; color:#800000; border:1px solid #800000; text-decoration:none; padding:5px 12px; border-radius:3px; font-size:13px; font-weight:600; display:inline-flex; align-items:center; gap:6px;">
      <i class="fa-solid fa-lock"></i> Ph.D. Applicant Portal
    </a>
    <a href="../offer-letter.html" style="background:#faf7f2; color:#4a0000; border:1px solid #d5cbc2; text-decoration:none; padding:5px 12px; border-radius:3px; font-size:13px; font-weight:600; display:inline-flex; align-items:center; gap:6px;">
      <i class="fa-solid fa-file-signature"></i> Offer Letter Format
    </a>
  </div>
</div>
'''
    if target in text and "Guaranteed Doctoral Fellowship" not in text:
        text = text.replace(target, callout + target)
        phd_page.write_text(text, encoding="utf-8")
        print("Updated academics_graduate-programs_phd-programs.html with fellowship callout!")
    else:
        print("phd-programs.html: target not found or already updated.")

# 2. Update academics_graduate-programs.html
grad_page = PAGES_DIR / "academics_graduate-programs.html"
if grad_page.exists():
    text = grad_page.read_text(encoding="utf-8")
    # Search for PhD programs callout banner
    phd_banner_target = re.compile(
        r'(<section class="CalloutBannerFullwidth_container__1gavT[^>]*>.*?Explore Doctoral Degree Programs.*?<\/section>)',
        re.DOTALL
    )
    fellowship_banner = '''
<section class="CalloutBannerFullwidth_container__1gavT CalloutBannerFullwidth_hasImage__32bOX" data-theme="light" data-accentcolor="red"><div class="CalloutBannerFullwidth_accentContainer__Zq9yU"><div class="CalloutBannerFullwidth_textContainer__1VQrF  "><h1 class="CalloutBannerFullwidth_title__o2K_Z serif-head-1">Graduate Fellowships &amp; Tuition Remission</h1><p>Doctoral candidates at UChicago receive guaranteed multi-year funding packages, including 100% full tuition remission ($20,000/sem, $60,000/yr), competitive monthly living stipends ($3,000/mo minimum), comprehensive U-SHIP health coverage, and full seat deposit reimbursement within 90 days.</p></div><div class="CalloutBannerFullwidth_ctaContainer__Ibksr"><a target="_self" class="CalloutBannerFullwidth_link__3nIqX" data-chevron="true" href="admissions_financial-aid-and-tuition.html#doctoral-fellowships"><span class="linkText">Explore Fellowship Funding &amp; Tuition Schedules</span></a></div></div><div class="CalloutBannerFullwidth_imageContainer__2Zb1U" style="background-image:url(../assets/subpage_media/fallleaves_students.png)"></div></section>'''
    
    if phd_banner_target.search(text) and "Graduate Fellowships &amp; Tuition Remission" not in text:
        text = phd_banner_target.sub(r'\1' + fellowship_banner, text, count=1)
        grad_page.write_text(text, encoding="utf-8")
        print("Updated academics_graduate-programs.html with fellowship banner!")
    else:
        print("graduate-programs.html: target not found or already updated.")

# 3. Update PSD subpages (Physics, CS, Math, Stats)
psd_files = [
    "department-of-physics.html",
    "department-of-computer-science.html",
    "department-of-mathematics.html",
    "department-of-statistics.html",
]

old_stipend_snippet = re.compile(
    r'<div style="background:#fff; border:1px solid #eed0d0; padding:12px 16px; border-radius:4px; font-size:13.5px; line-height:1.6; margin-bottom:16px;">\s*<div style="font-weight:700; color:#800000; margin-bottom:4px;"><i class="fa fa-shield-alt" style="margin-right:6px;"></i>Guaranteed 5-Year Doctoral Fellowship Package:</div>\s*<ul style="margin:0; padding-left:18px; color:#444;">\s*<li>100% Full Tuition Remission covered by the University</li>\s*<li>Competitive Annual Living Stipend \(\$44,000\+ per year\)</li>\s*<li>Comprehensive UChicago Student Health Insurance \(U-SHIP\)</li>\s*<li>Guaranteed research assistantship and travel conference grants</li>\s*</ul>\s*</div>',
    re.DOTALL
)

new_psd_fellowship = '''<div style="background:#fff; border:1px solid #eed0d0; padding:12px 16px; border-radius:4px; font-size:13.5px; line-height:1.6; margin-bottom:16px;">
                  <div style="font-weight:700; color:#800000; margin-bottom:6px;"><i class="fa fa-shield-alt" style="margin-right:6px;"></i>Physical Sciences Division &bull; Guaranteed 5-Year Doctoral Fellowship:</div>
                  <ul style="margin:0 0 8px 0; padding-left:18px; color:#444;">
                    <li><strong>100% Full Tuition Remission:</strong> $20,000.00 / semester ($60,000.00 / year) &bull; Zero tuition liability</li>
                    <li><strong>Doctoral Living Stipend:</strong> $3,000.00 / month ($36,000.00 / year) disbursed bi-weekly via GRA / TA</li>
                    <li><strong>U-SHIP Platinum Health, Dental &amp; Vision:</strong> 100% individual premium paid ($4,850+ value)</li>
                    <li><strong>Seat Deposit Protection:</strong> $6,200 deposit 100% reimbursable within 90 days; 100% refundable within 90 business days for visa denial</li>
                  </ul>
                  <div style="font-size:12px; color:#800000; border-top:1px dashed #eed0d0; padding-top:6px;">
                    <a href="admissions_financial-aid-and-tuition.html#doctoral-fellowships" style="color:#800000; font-weight:700; text-decoration:none;">View Official Fellowship Award Matrix &rarr;</a>
                  </div>
                </div>'''

for fname in psd_files:
    fpath = PAGES_DIR / fname
    if fpath.exists():
        ftext = fpath.read_text(encoding="utf-8")
        if old_stipend_snippet.search(ftext):
            ftext = old_stipend_snippet.sub(new_psd_fellowship, ftext, count=1)
            fpath.write_text(ftext, encoding="utf-8")
            print(f"Updated {fname} with official PSD fellowship guarantee!")
        else:
            print(f"{fname}: Old snippet not matched.")
