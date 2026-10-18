import os
import re

def update_financial_aid_page():
    path = "site_1to1/pages/admissions_financial-aid-and-tuition.html"
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    main_start = content.find("<main")
    main_end = content.find("</main>") + len("</main>")
    if main_start == -1 or main_end == -1:
        raise ValueError("Could not find <main> in financial-aid-and-tuition.html")

    head_part = content[:main_start]
    foot_part = content[main_end:]

    # Construct rich, authoritative UChicago-styled Main section
    new_main = """<main data-sitename="www" apm="false" tcl="false">
<div class="jss-main">
  <!-- Top Spacing Section -->
  <section class="single-col-wide"></section>

  <!-- 1. Hero Banner with Official UChicago Visuals -->
  <section class="single-col-wide">
    <section class="PageHeroBanner_container__RKHAN" style="background-image:url(../assets/subpage_media/fallleaves_students.png); background-position: center 30%;">
      <div class="PageHeroBanner_containerInner__CEU0x">
        <h1 class="PageHeroBanner_title__2XMBn" data-backgroundcolor="white">Financial Aid, Scholarships &amp; Tuition</h1>
      </div>
    </section>
  </section>

  <!-- 2. HeadlineBar: Mission & Institutional Commitment -->
  <section class="single-col-wide">
    <section class="HeadlineBar_container__3V-KO">
      <div class="HeadlineBar_heading__3xJfb">
        <h2 class="HeadlineBar_title__2LJw5" style="font-family: 'UChicagoSerif', Georgia, serif; color: #800000;">
          Investing in Extraordinary Minds
        </h2>
      </div>
      <div class="HeadlineBar_content__1lt38">
        <p class="HeadlineBar_description__wqxBb" style="font-size: 16px; line-height: 1.6; color: #444;">
          The University of Chicago is steadfastly committed to ensuring that financial considerations never stand between extraordinary scholars and a transformative education. Through comprehensive fellowship packages, 100% full tuition remission, guaranteed annual living stipends, institutional health coverage, and pioneering undergraduate aid, we empower students to pursue boundary-pushing research with clarity and complete security.
        </p>
      </div>
    </section>

    <!-- Quick Navigation Pills -->
    <div class="single-col-inner">
      <ul class="fin-pill-nav">
        <li><a href="#doctoral-fellowships" class="fin-pill-btn"><i class="fa-solid fa-graduation-cap"></i> Doctoral Fellowships (Ph.D.)</a></li>
        <li><a href="#offer-letter-matrix" class="fin-pill-btn"><i class="fa-solid fa-file-contract"></i> Master Fellowship Matrix</a></li>
        <li><a href="#tuition-fees" class="fin-pill-btn"><i class="fa-solid fa-receipt"></i> Tuition &amp; Fee Schedule</a></li>
        <li><a href="#deposit-policy" class="fin-pill-btn"><i class="fa-solid fa-shield-halved"></i> Seat Deposit &amp; Refund Policy</a></li>
        <li><a href="#undergraduate-aid" class="fin-pill-btn"><i class="fa-solid fa-building-columns"></i> Undergraduate Scholarships</a></li>
        <li><a href="#international-aid" class="fin-pill-btn"><i class="fa-solid fa-globe"></i> International Student Aid</a></li>
        <li><a href="#bursar-operations" class="fin-pill-btn"><i class="fa-solid fa-wallet"></i> Bursar &amp; Disbursements</a></li>
      </ul>
    </div>

    <!-- 3. High-Impact Factoids Grid -->
    <div class="single-col-inner">
      <div class="fin-grid-4">
        <div class="fin-stat-card">
          <div class="fin-stat-number">100%</div>
          <div class="fin-stat-label">Tuition Remission for Ph.D. Scholars</div>
        </div>
        <div class="fin-stat-card">
          <div class="fin-stat-number">$36,000</div>
          <div class="fin-stat-label">Annual Living Stipend ($3,000/Month)</div>
        </div>
        <div class="fin-stat-card">
          <div class="fin-stat-number">$0</div>
          <div class="fin-stat-label">Net Student Tuition Liability</div>
        </div>
        <div class="fin-stat-card">
          <div class="fin-stat-number">90 Days</div>
          <div class="fin-stat-label">100% Deposit Reimbursement Window</div>
        </div>
      </div>
    </div>

    <!-- 4. MASTER FINANCIAL BREAKDOWN MATRIX (Styled Identically to Offer Letter Page 3) -->
    <div class="single-col-inner" id="offer-letter-matrix">
      <div class="fin-matrix-container">
        <div class="fin-matrix-header">
          <div>
            <h3 class="fin-matrix-title">
              <i class="fa-solid fa-award"></i>
              DOCTORAL FELLOWSHIP AWARD MATRIX &amp; ENROLLMENT TERMS
            </h3>
            <div class="fin-matrix-subtitle">
              Division of the Physical Sciences • Department of Chemistry • Autumn Quarter 2027 Matriculation
            </div>
          </div>
          <div class="fin-matrix-badge">
            <i class="fa-solid fa-check-circle" style="color: #1b6329; margin-right: 4px;"></i>
            OFFICIAL INSTITUTIONAL RATIFICATION
          </div>
        </div>

        <div class="fin-table-wrap">
          <table class="fin-table">
            <thead>
              <tr>
                <th style="width: 22%;">AWARD COMPONENT</th>
                <th style="width: 20%;">GUARANTEED VALUE</th>
                <th style="width: 36%;">DISBURSEMENT &amp; COVERAGE TERMS</th>
                <th style="width: 22%;">INSTITUTIONAL STATUS</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>
                  <div class="fin-component-title">Full Tuition Remission</div>
                  <div class="fin-val-sub">Division of the Physical Sciences</div>
                </td>
                <td>
                  <div class="fin-val-highlight">$20,000.00 USD <span style="font-size: 12px; font-weight: normal; color: #555;">/ Semester</span></div>
                  <div class="fin-val-sub">($60,000.00 / academic year)</div>
                </td>
                <td>
                  <strong style="color: #800000;">100% Fully Funded</strong> via Physical Sciences Division Tuition Remission Fellowship. <strong>Zero student tuition liability</strong> throughout doctoral tenure in good academic standing.
                </td>
                <td>
                  <span class="fin-tag-funded"><i class="fa-solid fa-circle-check"></i> 100% FULLY FUNDED</span>
                </td>
              </tr>
              <tr>
                <td>
                  <div class="fin-component-title">Doctoral Living Stipend</div>
                  <div class="fin-val-sub">Graduate Research Assistantship (GRA)</div>
                </td>
                <td>
                  <div class="fin-val-highlight">$3,000.00 USD <span style="font-size: 12px; font-weight: normal; color: #555;">/ Month</span></div>
                  <div class="fin-val-sub">($36,000.00 annual living stipend)</div>
                </td>
                <td>
                  Funded via Graduate Research Assistantship under the Cusumano Research Group / Department of Chemistry; disbursed bi-weekly directly to candidate's personal banking / Bursar account.
                </td>
                <td>
                  <span class="fin-tag-funded"><i class="fa-solid fa-circle-check"></i> GUARANTEED STIPEND</span>
                </td>
              </tr>
              <tr>
                <td>
                  <div class="fin-component-title">U-SHIP Platinum Health Coverage</div>
                  <div class="fin-val-sub">University Student Health Insurance Plan</div>
                </td>
                <td>
                  <div class="fin-val-highlight">100% Comprehensive</div>
                  <div class="fin-val-sub">Individual Platinum Coverage ($4,850+ value)</div>
                </td>
                <td>
                  Full annual premium paid directly by the Division of the Physical Sciences; includes comprehensive medical, prescription, dental, and vision insurance with zero premium deduction.
                </td>
                <td>
                  <span class="fin-tag-funded"><i class="fa-solid fa-shield-virus"></i> FULL PREMIUM COVERED</span>
                </td>
              </tr>
              <tr>
                <td>
                  <div class="fin-component-title">Seat Confirmation Deposit</div>
                  <div class="fin-val-sub">Matriculation &amp; Research Lock</div>
                </td>
                <td>
                  <div class="fin-val-highlight">$6,200.00 USD</div>
                  <div class="fin-val-sub" style="color: #800000; font-weight: 700;">Priority Deadline: Nov 14, 2026</div>
                </td>
                <td>
                  <strong>100% Reimbursable within 90 days</strong> of semester start credited directly back to Bursar account; <strong>100% Refundable within 90 business days</strong> in case of unforeseen visa or travel complications.
                </td>
                <td>
                  <span class="fin-tag-maroon"><i class="fa-solid fa-lock"></i> 100% PROTECTED &amp; REIMBURSABLE</span>
                </td>
              </tr>
              <tr>
                <td>
                  <div class="fin-component-title">Application Processing Fee</div>
                  <div class="fin-val-sub">Graduate Admissions Administration</div>
                </td>
                <td>
                  <div class="fin-val-highlight">$90.00 USD</div>
                  <div class="fin-val-sub">One-time application filing</div>
                </td>
                <td>
                  Institutional credentialing and admissions file review fee. Verified and credited upon official dossier submission; official receipt archived in applicant portal.
                </td>
                <td>
                  <span class="fin-tag-funded"><i class="fa-solid fa-check"></i> VERIFIED &amp; CREDITED</span>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <!-- 5. TERMS OF SEAT CONFIRMATION DEPOSIT & GUARANTEED REFUND POLICY CALLOUT -->
    <div class="single-col-inner" id="deposit-policy">
      <div class="fin-policy-callout">
        <h4 class="fin-policy-title">
          <i class="fa-solid fa-shield-halved"></i>
          TERMS OF SEAT CONFIRMATION DEPOSIT &amp; GUARANTEED REFUND POLICY
        </h4>
        <div style="font-size: 14px; color: #333; line-height: 1.6; margin-bottom: 14px;">
          To reserve and officially lock graduate research placement in the designated doctoral laboratory, admitted candidates submit a Ph.D. Matriculation Seat Confirmation Deposit of <strong>$6,200.00 USD</strong> by the priority deadline of <strong>November 14, 2026</strong>. The University of Chicago maintains the following strict institutional guarantees governing this deposit:
        </div>
        <ul style="font-size: 13.5px; color: #333; line-height: 1.65; margin: 0 0 16px 20px; padding: 0;">
          <li style="margin-bottom: 10px;">
            <strong style="color: #800000;">Full Reimbursability within 90 Days of Semester Start:</strong> The entire $6,200.00 USD seat locking fee is <strong>100% reimbursable within 90 days</strong> from the formal commencement of the Autumn Quarter (August 2027). The full amount is credited directly back to the student's Bursar account and disbursed alongside the doctoral fellowship living stipend.
          </li>
          <li style="margin-bottom: 6px;">
            <strong style="color: #800000;">Full Refundability within 90 Business Days for Unforeseen Travel / Visa Complications:</strong> In the unforeseen event of visa denial, administrative visa processing cancellation, international travel restrictions, or non-enrollment due to extenuating circumstances beyond the candidate's control, <strong>the $6,200.00 USD seat deposit is 100% refundable within 90 business days</strong> upon written notification and supporting documentation submitted to the Division of the Physical Sciences Admissions Office.
          </li>
        </ul>
        <div style="font-size: 12.5px; color: #666; border-top: 1px solid #e0d8d8; padding-top: 12px; display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 8px;">
          <div>
            <i class="fa-solid fa-stamp" style="color: #800000; margin-right: 5px;"></i>
            Institutional Policy ratified under the authority of <strong>Dean James G. Nondorf</strong>, Dean of Admissions and Financial Aid.
          </div>
          <div>
            <a href="../portal.html?applicantId=UC-2027-89321" class="portal-btn-primary" style="padding: 6px 14px; font-size: 12px; text-decoration: none; border-radius: 3px;">
              <i class="fa-solid fa-arrow-right"></i> View Deposit Terms in Portal
            </a>
          </div>
        </div>
      </div>
    </div>

    <!-- 6. ADMISSIONS DOMAINS DETAILED BREAKDOWN -->
    <div class="single-col-inner" id="doctoral-fellowships">
      <!-- Domain 1: Doctoral & Graduate Fellowships -->
      <div class="fin-domain-card">
        <h3 class="fin-domain-title">
          <i class="fa-solid fa-flask-vial"></i>
          1. Doctoral Programs &amp; Division Fellowships (Ph.D.)
        </h3>
        <p style="font-size: 14.5px; color: #444; line-height: 1.6; margin-bottom: 16px;">
          Doctoral students across all five graduate divisions and specialized schools at the University of Chicago receive competitive, multi-year fellowship packages guaranteed for the normal duration of their program (typically 5 years). Fellowships provide complete tuition remission, a competitive living stipend, full health insurance premiums, and dedicated research support funds.
        </p>

        <div class="fin-grid-2">
          <div style="background: #faf8f5; border: 1px solid #ebe4dc; border-radius: 4px; padding: 18px 20px;">
            <h4 style="font-family: 'UChicagoSerif', Georgia, serif; color: #800000; font-size: 16px; margin: 0 0 10px;">
              <i class="fa-solid fa-atom"></i> Division of the Physical Sciences (PSD)
            </h4>
            <ul style="font-size: 13px; color: #444; line-height: 1.6; margin: 0 0 0 18px; padding: 0;">
              <li><strong>Departments:</strong> Chemistry, Physics, Computer Science, Mathematics, Statistics, Geophysical Sciences, Astronomy &amp; Astrophysics.</li>
              <li><strong>Guaranteed Tuition Remission:</strong> 100% ($20,000/sem, $60,000/yr).</li>
              <li><strong>Doctoral Living Stipend:</strong> $3,000/month ($36,000/year) minimum.</li>
              <li><strong>Health Insurance:</strong> 100% individual U-SHIP Platinum coverage paid.</li>
              <li><strong>Research Sponsoring:</strong> Graduate Research Assistantship (GRA) under faculty research groups (e.g., Cusumano Research Group) and Searle Chemistry Laboratories.</li>
            </ul>
          </div>

          <div style="background: #faf8f5; border: 1px solid #ebe4dc; border-radius: 4px; padding: 18px 20px;">
            <h4 style="font-family: 'UChicagoSerif', Georgia, serif; color: #800000; font-size: 16px; margin: 0 0 10px;">
              <i class="fa-solid fa-dna"></i> Biological Sciences &amp; Pritzker Molecular Engineering
            </h4>
            <ul style="font-size: 13px; color: #444; line-height: 1.6; margin: 0 0 0 18px; padding: 0;">
              <li><strong>Units:</strong> Biological Sciences Division (BSD), Pritzker School of Molecular Engineering (PME), Institute for Biophysical Dynamics.</li>
              <li><strong>Full Funding Guarantee:</strong> 100% tuition remission + annual competitive stipend ($37,000 – $44,000/yr depending on lab fellowship).</li>
              <li><strong>U-SHIP Health &amp; Dental:</strong> 100% coverage funded by division.</li>
              <li><strong>Travel &amp; Conference Grants:</strong> Up to $1,500/year in professional dissemination awards.</li>
            </ul>
          </div>
        </div>

        <div style="margin-top: 14px; font-size: 13px; color: #555; background: #ffffff; border: 1px dashed #d5cbc2; padding: 12px 16px; border-radius: 4px;">
          <strong style="color: #800000;">Zero Tuition Liability Guarantee:</strong> As a doctoral scholar in good academic standing, you will never receive a tuition bill from the University. Your tuition waiver is automatically applied to your student account by the Office of the Bursar at the start of each quarter.
        </div>
      </div>

      <!-- Domain 2: Tuition & Mandatory Fee Schedule -->
      <div class="fin-domain-card" id="tuition-fees">
        <h3 class="fin-domain-title">
          <i class="fa-solid fa-receipt"></i>
          2. Official Tuition, Fees &amp; Seat Deposit Schedule (Academic Year 2026–2027 / 2027–2028)
        </h3>
        <p style="font-size: 14.5px; color: #444; line-height: 1.6; margin-bottom: 16px;">
          The University of Chicago publishes its comprehensive tuition and fee schedule annually. Below is the published schedule for graduate physical sciences programs, itemizing published institutional rates alongside the corresponding fellowship award offsets:
        </p>

        <div class="fin-table-wrap">
          <table class="fin-table">
            <thead>
              <tr>
                <th>FEE CATEGORY</th>
                <th>PUBLISHED RATE (QUARTER / SEMESTER)</th>
                <th>ANNUAL ESTIMATE</th>
                <th>FELLOWSHIP REMISSION</th>
                <th>NET STUDENT COST</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Doctoral Graduate Tuition</strong></td>
                <td>$20,000.00 / Term</td>
                <td>$60,000.00 / Academic Year</td>
                <td><strong style="color: #1b6329;">-$60,000.00 (100% Paid)</strong></td>
                <td><strong style="color: #1b6329;">$0.00</strong></td>
              </tr>
              <tr>
                <td><strong>Student Life &amp; Activities Fee</strong></td>
                <td>$440.00 / Quarter</td>
                <td>$1,320.00 / Year</td>
                <td><strong style="color: #1b6329;">Departmental Subsidized</strong></td>
                <td><strong style="color: #1b6329;">$0.00</strong></td>
              </tr>
              <tr>
                <td><strong>Student Health &amp; Wellness Fee</strong></td>
                <td>$275.00 / Quarter</td>
                <td>$825.00 / Year</td>
                <td><strong style="color: #1b6329;">Fully Covered</strong></td>
                <td><strong style="color: #1b6329;">$0.00</strong></td>
              </tr>
              <tr>
                <td><strong>U-SHIP Health Insurance Premium</strong></td>
                <td>$1,616.00 / Quarter</td>
                <td>$4,848.00 / Year</td>
                <td><strong style="color: #1b6329;">-$4,848.00 (100% Paid)</strong></td>
                <td><strong style="color: #1b6329;">$0.00</strong></td>
              </tr>
              <tr>
                <td><strong>CTA Transit U-Pass Access</strong></td>
                <td>$110.00 / Quarter</td>
                <td>$330.00 / Year</td>
                <td><strong style="color: #1b6329;">Included in Fellow Pass</strong></td>
                <td><strong style="color: #1b6329;">$0.00</strong></td>
              </tr>
              <tr style="background: #faf4f4; font-weight: 700;">
                <td><strong>NET ANNUAL COST OF DOCTORAL STUDY</strong></td>
                <td>—</td>
                <td>$67,323.00 Published Total</td>
                <td>-$67,323.00 Total Remission</td>
                <td><span style="font-size: 16px; color: #1b6329;">$0.00 / YEAR</span></td>
              </tr>
              <tr style="background: #fdfaf7;">
                <td><strong>Doctoral Research Stipend Disbursed to Student</strong></td>
                <td>$3,000.00 / Month</td>
                <td>+$36,000.00 Annual Income</td>
                <td>GRA / Departmental Payroll</td>
                <td><strong style="color: #800000; font-size: 15px;">+$36,000.00 (Paid to Student)</strong></td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- Domain 3: Undergraduate Financial Aid & Empower Initiative -->
      <div class="fin-domain-card" id="undergraduate-aid">
        <h3 class="fin-domain-title">
          <i class="fa-solid fa-building-columns"></i>
          3. Undergraduate Financial Aid &amp; The Empower Initiative
        </h3>
        <p style="font-size: 14.5px; color: #444; line-height: 1.6; margin-bottom: 16px;">
          For students in the College, the University of Chicago provides need-based aid packages that meet 100% of demonstrated financial need with no loans. Under the landmark UChicago Empower Initiative and expanded affordability policies:
        </p>

        <div class="fin-grid-2">
          <div style="background: #ffffff; border: 1px solid #e0d8d8; border-top: 3px solid #800000; padding: 18px 20px; border-radius: 4px;">
            <div style="font-size: 11px; text-transform: uppercase; font-weight: 800; color: #800000; margin-bottom: 4px;">HOUSEHOLD INCOME UP TO $250,000</div>
            <h4 style="font-family: 'UChicagoSerif', Georgia, serif; font-size: 24px; color: #222; margin: 0 0 8px;">Free Tuition Guarantee</h4>
            <p style="font-size: 13px; color: #555; line-height: 1.5; margin: 0;">
              Beginning Autumn Quarter 2027, undergraduate students from families earning up to $250,000 (with typical assets) receive free tuition, covering the full cost of instructional fees.
            </p>
          </div>

          <div style="background: #ffffff; border: 1px solid #e0d8d8; border-top: 3px solid #800000; padding: 18px 20px; border-radius: 4px;">
            <div style="font-size: 11px; text-transform: uppercase; font-weight: 800; color: #800000; margin-bottom: 4px;">HOUSEHOLD INCOME UNDER $125,000</div>
            <h4 style="font-family: 'UChicagoSerif', Georgia, serif; font-size: 24px; color: #222; margin: 0 0 8px;">Free College Comprehensive</h4>
            <p style="font-size: 13px; color: #555; line-height: 1.5; margin: 0;">
              Families earning under $125,000 have tuition, on-campus housing, meal plans, and all mandatory student fees covered in full through institutional grant aid.
            </p>
          </div>
        </div>

        <div style="margin-top: 14px; font-size: 13.5px; color: #444; line-height: 1.6;">
          <strong>Additional Undergraduate Scholarships:</strong>
          <ul style="margin: 6px 0 0 18px; padding: 0;">
            <li><strong>First Phoenix Scholarship:</strong> Guaranteed minimum $20,000 award, funded summer research internship, and mentorship for all first-generation college students.</li>
            <li><strong>Odyssey Scholarship Program:</strong> Comprehensive support for students from under-resourced communities, including funded study abroad and textbook stipends.</li>
          </ul>
        </div>
      </div>

      <!-- Domain 4: International Student Financial Guidelines & Visa Verification -->
      <div class="fin-domain-card" id="international-aid">
        <h3 class="fin-domain-title">
          <i class="fa-solid fa-globe"></i>
          4. International Student Financial Guidelines &amp; Visa Verification (F-1 / J-1)
        </h3>
        <p style="font-size: 14.5px; color: #444; line-height: 1.6; margin-bottom: 16px;">
          The University of Chicago warmly welcomes international scholars from over 100 nations. Because doctoral fellows receive 100% full funding, international admission and visa processing are streamlined:
        </p>

        <div class="fin-grid-2">
          <div style="background: #faf8f5; border: 1px solid #ebe4dc; border-radius: 4px; padding: 18px 20px;">
            <h4 style="font-family: 'UChicagoSerif', Georgia, serif; color: #800000; font-size: 16px; margin: 0 0 10px;">
              <i class="fa-solid fa-passport"></i> Form I-20 &amp; DS-2019 Financial Clearance
            </h4>
            <ul style="font-size: 13px; color: #444; line-height: 1.6; margin: 0 0 0 18px; padding: 0;">
              <li><strong>Institutional Financial Certificate:</strong> Your official offer letter and fellowship ratification serve as full proof of financial capability for Form I-20 / DS-2019 issuance.</li>
              <li><strong>Zero Bank Balance Burden:</strong> Doctoral candidates with full tuition remission and living stipends are <em>not required</em> to submit personal or family bank statements for the tuition and living cost components.</li>
              <li><strong>Office of International Affairs (OIA):</strong> Dedicated international advisors assist with SEVIS record creation, visa interview documentation, and arrival orientation.</li>
            </ul>
          </div>

          <div style="background: #faf8f5; border: 1px solid #ebe4dc; border-radius: 4px; padding: 18px 20px;">
            <h4 style="font-family: 'UChicagoSerif', Georgia, serif; color: #800000; font-size: 16px; margin: 0 0 10px;">
              <i class="fa-solid fa-handshake-angle"></i> Visa Protection &amp; Emergency Refund Clauses
            </h4>
            <ul style="font-size: 13px; color: #444; line-height: 1.6; margin: 0 0 0 18px; padding: 0;">
              <li><strong>100% Guaranteed Refund within 90 Business Days:</strong> If unforeseen visa denial, administrative 221(g) processing delays, or international travel restrictions prevent travel to Chicago, your $6,200 seat deposit is 100% refunded.</li>
              <li><strong>Deferral Flexibility:</strong> Candidates facing embassy scheduling delays may request a one-quarter or one-year admission deferral with full fellowship preservation.</li>
              <li><strong>SEVIS &amp; Consular Verification:</strong> Admitted students can generate verified institutional letters directly from the Applicant Portal.</li>
            </ul>
          </div>
        </div>
      </div>

      <!-- Domain 5: Office of the Bursar & Financial Operations -->
      <div class="fin-domain-card" id="bursar-operations">
        <h3 class="fin-domain-title">
          <i class="fa-solid fa-wallet"></i>
          5. Office of the Bursar &amp; Student Financial Operations
        </h3>
        <p style="font-size: 14.5px; color: #444; line-height: 1.6; margin-bottom: 16px;">
          The Office of the Bursar manages student financial accounts, billing statements, fellowship tuition waivers, direct deposit payroll, and fee reimbursements.
        </p>

        <div class="fin-grid-2">
          <div style="background: #ffffff; border: 1px solid #e0d8d8; padding: 18px 20px; border-radius: 4px;">
            <h4 style="font-family: 'UChicagoSerif', Georgia, serif; color: #800000; font-size: 16px; margin: 0 0 8px;">
              <i class="fa-solid fa-money-bill-transfer"></i> Bi-Weekly Stipend Direct Deposit
            </h4>
            <p style="font-size: 13px; color: #555; line-height: 1.5; margin: 0;">
              Living stipends ($3,000/month) are disbursed on a bi-weekly cycle through the University payroll system (Workday@UChicago). Scholars establish direct deposit to their preferred U.S. banking institution during onboarding.
            </p>
          </div>

          <div style="background: #ffffff; border: 1px solid #e0d8d8; padding: 18px 20px; border-radius: 4px;">
            <h4 style="font-family: 'UChicagoSerif', Georgia, serif; color: #800000; font-size: 16px; margin: 0 0 8px;">
              <i class="fa-solid fa-file-invoice-dollar"></i> Deposit Reimbursement Processing
            </h4>
            <p style="font-size: 13px; color: #555; line-height: 1.5; margin: 0;">
              Upon formal matriculation in the Autumn Quarter, the Bursar automatically credits the $6,200.00 seat deposit to the student account within the guaranteed 90-day window, releasing funds via electronic transfer.
            </p>
          </div>
        </div>

        <div style="margin-top: 18px; padding-top: 14px; border-top: 1px solid #ebe5df; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 12px;">
          <div style="font-size: 13px; color: #666;">
            <strong>Office of the Bursar:</strong> 5801 S. Ellis Avenue, Suite 101, Chicago, IL 60637 • Phone: 773.702.8000 • Email: bursar@uchicago.asia
          </div>
          <div>
            <a href="../receipt.html" target="_blank" class="portal-btn-outline" style="font-size: 12px; padding: 6px 14px; text-decoration: none;">
              <i class="fa-solid fa-file-invoice"></i> View Official Receipt Sample
            </a>
          </div>
        </div>
      </div>
    </div>

    <!-- 7. Portal Call to Action & Quick Links -->
    <div class="single-col-inner" style="margin-bottom: 50px;">
      <div style="background: #800000; color: #ffffff; border-radius: 6px; padding: 32px 36px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 20px;">
        <div style="max-width: 650px;">
          <h3 style="font-family: 'UChicagoSerif', Georgia, serif; font-size: 24px; color: #ffffff; margin: 0 0 8px;">
            Access Your Official Admissions Dossier
          </h3>
          <p style="font-size: 14.5px; color: rgba(255,255,255,0.9); margin: 0; line-height: 1.5;">
            Log in to the secure UChicago Applicant Status Portal to review your official admission offer, view the 3-page ratified fellowship grant, and confirm your research placement.
          </p>
        </div>
        <div style="display: flex; gap: 12px; flex-wrap: wrap;">
          <a href="../portal.html?applicantId=UC-2027-89321" class="portal-btn-primary" style="background: #ffffff; color: #800000; font-weight: 800; text-decoration: none; padding: 12px 22px; font-size: 13.5px; border-radius: 4px; box-shadow: 0 4px 12px rgba(0,0,0,0.2);">
            <i class="fa-solid fa-arrow-right-to-bracket"></i> Applicant Portal
          </a>
          <a href="../offer-letter.html" target="_blank" style="background: transparent; border: 1.5px solid #ffffff; color: #ffffff; font-weight: 700; text-decoration: none; padding: 12px 20px; font-size: 13.5px; border-radius: 4px;">
            <i class="fa-solid fa-file-contract"></i> View Offer Letter
          </a>
        </div>
      </div>
    </div>

  </section>
</div>
</main>"""

    full_html = head_part + new_main + foot_part
    with open(path, "w", encoding="utf-8") as f:
        f.write(full_html)
    print("Successfully updated site_1to1/pages/admissions_financial-aid-and-tuition.html")

update_financial_aid_page()
