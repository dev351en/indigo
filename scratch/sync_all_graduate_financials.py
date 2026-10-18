import re
from pathlib import Path

BASE_DIR = Path(r"d:\Microvirt\OBSIDIAN\uchicago_replica\site_1to1\pages")

# 1. Update department-of-chemistry.html
chem_path = BASE_DIR / "department-of-chemistry.html"
chem_content = chem_path.read_text(encoding="utf-8")

chem_target_regex = re.compile(
    r'<!-- Doctoral \(Ph\.D\.\) Program -->\s*<div style="background:#fff9f9;.*?(?=<!-- Research Areas -->)',
    re.DOTALL
)

chem_replacement = '''<!-- Doctoral (Ph.D.) Program -->
              <div class="fin-matrix-container" style="margin-bottom: 28px; box-shadow: 0 4px 18px rgba(0,0,0,0.06); border-radius: 4px; overflow: hidden; border: 1px solid #d9c4c4;">
                <div class="fin-matrix-header" style="background: linear-gradient(135deg, #800000 0%, #4a0000 100%); padding: 18px 24px;">
                  <span class="fin-matrix-badge" style="background: #ffffff; color: #800000; font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; padding: 3px 8px; border-radius: 2px;">
                    Physical Sciences Division &bull; 5-Year Full Fellowship
                  </span>
                  <h4 style="font-family: 'UChicagoSerif', Georgia, serif; font-size: 21px; color: #ffffff; margin: 8px 0 4px; font-weight: 700;">
                    Doctor of Philosophy (Ph.D.) in Chemistry
                  </h4>
                  <p style="font-size: 13.5px; color: #f2dcdc; margin: 0; line-height: 1.5;">
                    Comprehensive multi-year doctoral fellowship guaranteed for all admitted candidates in good academic standing, ratified under the executive certification of Dean James G. Nondorf.
                  </p>
                </div>

                <div style="padding: 20px 24px; background: #ffffff;">
                  <p style="font-size: 14.5px; line-height: 1.6; color: #333; margin: 0 0 16px;">
                    Doctoral scholars in the Department of Chemistry conduct cutting-edge research across synthetic organic, chemical biology, inorganic nanomaterials, ultrafast spectroscopy, and theoretical chemistry with zero personal tuition liability and competitive institutional living support.
                  </p>

                  <div class="fin-table-wrap" style="border: 1px solid #ebe4dc; border-radius: 4px; overflow-x: auto; margin-bottom: 16px;">
                    <table class="fin-table" style="width: 100%; border-collapse: collapse; font-size: 13.5px;">
                      <thead>
                        <tr style="background: #faf7f2; border-bottom: 2px solid #800000; text-align: left;">
                          <th style="padding: 10px 14px; font-weight: 700; color: #800000; width: 28%;">Award Component</th>
                          <th style="padding: 10px 14px; font-weight: 700; color: #800000; width: 22%;">Guaranteed Value</th>
                          <th style="padding: 10px 14px; font-weight: 700; color: #800000; width: 34%;">Disbursement &amp; Coverage Terms</th>
                          <th style="padding: 10px 14px; font-weight: 700; color: #800000; width: 16%;">Institutional Status</th>
                        </tr>
                      </thead>
                      <tbody>
                        <tr style="border-bottom: 1px solid #eee;">
                          <td style="padding: 11px 14px; vertical-align: top;">
                            <div class="fin-component-title" style="font-weight: 700; color: #222;">Full Tuition Remission</div>
                            <div style="font-size: 12px; color: #666;">Searle Chemistry Laboratories</div>
                          </td>
                          <td style="padding: 11px 14px; vertical-align: top;">
                            <div class="fin-val-highlight" style="font-weight: 700; color: #800000; font-size: 14px;">$20,000.00 / Semester</div>
                            <div class="fin-val-sub" style="font-size: 11.5px; color: #666;">$60,000.00 / academic year</div>
                          </td>
                          <td style="padding: 11px 14px; font-size: 12.5px; color: #444; vertical-align: top;">
                            100% direct departmental tuition credit applied automatically to the Bursar account; zero student tuition liability.
                          </td>
                          <td style="padding: 11px 14px; vertical-align: top;">
                            <span class="fin-tag-funded" style="display: inline-block; background: #e8f5e9; color: #2e7d32; font-weight: 700; font-size: 11px; padding: 2px 8px; border-radius: 3px;">100% Fully Funded</span>
                          </td>
                        </tr>
                        <tr style="border-bottom: 1px solid #eee; background: #fdfcfb;">
                          <td style="padding: 11px 14px; vertical-align: top;">
                            <div class="fin-component-title" style="font-weight: 700; color: #222;">Doctoral Living Stipend</div>
                            <div style="font-size: 12px; color: #666;">GRA / Teaching Assistantship</div>
                          </td>
                          <td style="padding: 11px 14px; vertical-align: top;">
                            <div class="fin-val-highlight" style="font-weight: 700; color: #800000; font-size: 14px;">$3,000.00 / Month</div>
                            <div class="fin-val-sub" style="font-size: 11.5px; color: #666;">$36,000.00 / academic year</div>
                          </td>
                          <td style="padding: 11px 14px; font-size: 12.5px; color: #444; vertical-align: top;">
                            Disbursed on a semi-monthly (bi-weekly) payroll schedule via direct electronic bank deposit through UChicago Workday.
                          </td>
                          <td style="padding: 11px 14px; vertical-align: top;">
                            <span class="fin-tag-funded" style="display: inline-block; background: #e8f5e9; color: #2e7d32; font-weight: 700; font-size: 11px; padding: 2px 8px; border-radius: 3px;">Guaranteed (5 Years)</span>
                          </td>
                        </tr>
                        <tr style="border-bottom: 1px solid #eee;">
                          <td style="padding: 11px 14px; vertical-align: top;">
                            <div class="fin-component-title" style="font-weight: 700; color: #222;">Comprehensive Health &amp; Dental</div>
                            <div style="font-size: 12px; color: #666;">U-SHIP Platinum Individual Plan</div>
                          </td>
                          <td style="padding: 11px 14px; vertical-align: top;">
                            <div class="fin-val-highlight" style="font-weight: 700; color: #800000; font-size: 14px;">100% Individual Premium</div>
                            <div class="fin-val-sub" style="font-size: 11.5px; color: #666;">$4,850+ annual market value</div>
                          </td>
                          <td style="padding: 11px 14px; font-size: 12.5px; color: #444; vertical-align: top;">
                            Complete medical, dental, vision, preventive, and prescription drug coverage fully sponsored by the Division.
                          </td>
                          <td style="padding: 11px 14px; vertical-align: top;">
                            <span class="fin-tag-funded" style="display: inline-block; background: #e8f5e9; color: #2e7d32; font-weight: 700; font-size: 11px; padding: 2px 8px; border-radius: 3px;">100% University Paid</span>
                          </td>
                        </tr>
                        <tr style="background: #faf8f5;">
                          <td style="padding: 11px 14px; vertical-align: top;">
                            <div class="fin-component-title" style="font-weight: 700; color: #222;">Seat Confirmation Deposit</div>
                            <div style="font-size: 12px; color: #666;">Matriculation Commitment</div>
                          </td>
                          <td style="padding: 11px 14px; vertical-align: top;">
                            <div class="fin-val-highlight" style="font-weight: 700; color: #800000; font-size: 14px;">$6,200.00 USD</div>
                            <div class="fin-val-sub" style="font-size: 11.5px; color: #666;">Due November 14, 2026</div>
                          </td>
                          <td style="padding: 11px 14px; font-size: 12px; color: #444; vertical-align: top;">
                            <strong>100% Reimbursable within 90 days</strong> from the formal commencement of the semester, credited back to the student Bursar account and disbursed alongside the doctoral living stipend.
                          </td>
                          <td style="padding: 11px 14px; vertical-align: top;">
                            <span class="fin-tag-maroon" style="display: inline-block; background: #fdf2e9; color: #c0392b; font-weight: 700; font-size: 11px; padding: 2px 8px; border-radius: 3px;">100% Reimbursable</span>
                          </td>
                        </tr>
                      </tbody>
                    </table>
                  </div>

                  <!-- 90-Day Policy Callout -->
                  <div class="fin-policy-callout" style="background: #fdfbf7; border: 1px solid #ebd9c8; border-left: 4px solid #800000; border-radius: 4px; padding: 14px 18px; margin-bottom: 18px;">
                    <div style="font-weight: 700; color: #800000; font-size: 13.5px; margin-bottom: 4px;">
                      <i class="fa-solid fa-handshake-angle" style="margin-right: 6px;"></i>
                      Deposit Reimbursement &amp; Visa Safeguard Policy (Dean James G. Nondorf Certification)
                    </div>
                    <p style="font-size: 12.5px; color: #444; line-height: 1.55; margin: 0;">
                      The $6,200.00 matriculation seat confirmation deposit secures the candidate's laboratory placement in Searle Chemistry Laboratories. Pursuant to University policy, the deposit is <strong>100% reimbursable within 90 days</strong> following semester commencement. Furthermore, in the event of unforeseen visa denial, administrative processing cancellation, or international travel restrictions beyond candidate control, the deposit is <strong>100% fully refundable within 90 business days</strong>. Application fee: $90.00 USD.
                    </p>
                  </div>

                  <!-- CTAs -->
                  <div style="display: flex; gap: 12px; align-items: center; flex-wrap: wrap;">
                    <a href="../portal.html" style="background: #800000; color: #fff; text-decoration: none; padding: 8px 18px; border-radius: 4px; font-weight: 700; font-size: 13.5px; display: inline-flex; align-items: center; gap: 6px;">
                      <i class="fa-solid fa-lock"></i> Access Applicant Portal &rarr;
                    </a>
                    <a href="admissions_financial-aid-and-tuition.html#doctoral-fellowships" style="background: #ffffff; color: #800000; border: 1px solid #800000; text-decoration: none; padding: 7px 16px; border-radius: 4px; font-weight: 600; font-size: 13.5px; display: inline-flex; align-items: center; gap: 6px;">
                      <i class="fa-solid fa-table-list"></i> Full Financial Aid &amp; Tuition Matrix &rarr;
                    </a>
                    <a href="../offer-letter.html" style="background: #faf7f2; color: #4a0000; border: 1px solid #d5cbc2; text-decoration: none; padding: 7px 16px; border-radius: 4px; font-weight: 600; font-size: 13.5px; display: inline-flex; align-items: center; gap: 6px;">
                      <i class="fa-solid fa-file-signature"></i> View Offer Letter Format
                    </a>
                  </div>
                </div>
              </div>
            </div>

            <!-- Research Areas -->'''

if chem_target_regex.search(chem_content):
    chem_content = chem_target_regex.sub(chem_replacement, chem_content, count=1)
    chem_path.write_text(chem_content, encoding="utf-8")
    print("Successfully updated department-of-chemistry.html with offer-letter financial matrix!")
else:
    print("Could not find regex match in department-of-chemistry.html")
