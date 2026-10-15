import re

def update_portal_file(filepath, is_pages_dir=False):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    prefix = "../" if is_pages_dir else ""

    transcript_card = f'''
          <!-- Official Academic Transcript Card -->
          <div class="portal-card-block" id="portalTranscriptSection">
            <h2 class="portal-card-block-title">
              <span><i class="fa-solid fa-graduation-cap" style="color: maroon; margin-right: 8px;"></i>Official Academic Transcript</span>
              <span class="portal-badge-received" style="background:#e6f4ea; color:#137333; font-weight:700;"><i class="fa-solid fa-lock" style="margin-right:4px;"></i>Verified &amp; Locked</span>
            </h2>
            <div style="background: #ffffff; border: 1px solid #e0e0e0; border-left: 4px solid #137333; padding: 22px; border-radius: 4px; box-shadow: 0 1px 4px rgba(0,0,0,0.04);">
              <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 16px; margin-bottom: 16px;">
                <div style="display: flex; gap: 16px; align-items: flex-start;">
                  <div style="width: 48px; height: 48px; border-radius: 50%; background: #fdf2f2; border: 1.5px solid maroon; display: flex; align-items: center; justify-content: center; color: maroon; font-size: 22px; flex-shrink: 0;">
                    <i class="fa-solid fa-building-columns"></i>
                  </div>
                  <div>
                    <div style="font-weight: 700; font-size: 16.5px; color: #111;">
                      Indian Institute of Technology Gandhinagar (IITGN)
                    </div>
                    <div style="font-size: 13.5px; color: #333; margin-top: 3px; font-weight: 500;">
                      Consolidated Academic Transcript &amp; Grade Record • Ref: <strong>IITGN-MSC-2026-24510041</strong>
                    </div>
                    <div style="font-size: 12px; color: #666; margin-top: 4px; line-height: 1.45;">
                      Student Name: <strong>Devendra Dubey Biswambharnath Geeta</strong> • Roll / ID: <strong>24510041</strong><br />
                      Program: <strong>M.Sc. Chemistry</strong> • Batch / Year: <strong>2024 – 2026</strong> • Issued: <strong>24th August 2026</strong>
                    </div>
                  </div>
                </div>
                <div style="text-align: right; flex-shrink: 0;">
                  <div style="background: #f0f7f2; border: 1px solid #c2e2cc; border-radius: 4px; padding: 8px 14px; display: inline-block; text-align: right;">
                    <div style="font-size: 11px; text-transform: uppercase; letter-spacing: 0.5px; color: #137333; font-weight: 700;">Final Cumulative GPA</div>
                    <div style="font-size: 20px; font-weight: 800; color: #0d652d; line-height: 1.2;">8.46 <span style="font-size: 13px; font-weight: 500; color: #666;">/ 10.00</span></div>
                    <div style="font-size: 11px; color: #137333; font-weight: 700; margin-top: 2px;">First Class with Distinction</div>
                  </div>
                </div>
              </div>

              <!-- Academic Metrics & Highlights Grid -->
              <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(135px, 1fr)); gap: 10px; background: #fafafa; border: 1px solid #eee; padding: 12px 14px; border-radius: 4px; margin-bottom: 14px; font-size: 12.5px;">
                <div><span style="color:#666;">Total Credits:</span> <strong style="color:#111;">85 Credits</strong></div>
                <div><span style="color:#666;">GPA Credits:</span> <strong style="color:#111;">74 Credits</strong></div>
                <div><span style="color:#666;">Non-GPA / Pass:</span> <strong style="color:#111;">11 Credits</strong></div>
                <div><span style="color:#666;">Completed Courses:</span> <strong style="color:#111;">28 Courses</strong></div>
                <div><span style="color:#666;">Credit Points:</span> <strong style="color:#111;">626 Points</strong></div>
                <div><span style="color:#666;">Graduation Status:</span> <strong style="color:#137333;"><i class="fa-solid fa-circle-check"></i> Requirements Completed</strong></div>
              </div>

              <!-- Research Assistant Fellowship Remark -->
              <div style="font-size: 11.5px; line-height: 1.5; color: #555; background: #fffdf5; border: 1px solid #f0e6c8; padding: 8px 12px; border-radius: 3px; margin-bottom: 16px;">
                <strong style="color: #856404;"><i class="fa-solid fa-award"></i> Academic &amp; Research Remark:</strong> Pursuing the Prime Minister's Research Assistant Fellowship (PMRAF) in the Department of Atomic and Molecular Physics at Physical Research Laboratory (PRL), Ahmedabad, under the guidance of Prof. Bhaskar Datta.
              </div>

              <!-- Actions & Locked Upload Notice -->
              <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 12px; padding-top: 14px; border-top: 1px solid #f0f0f0;">
                <div style="display: flex; gap: 10px; flex-wrap: wrap;">
                  <button type="button" class="portal-transcript-view-btn" id="portalTranscriptPreviewBtn" style="background: maroon; color: #ffffff; border: none; padding: 9px 18px; font-family: 'UChicagoSansSerif-Bold', sans-serif; font-size: 13px; text-transform: uppercase; letter-spacing: 0.5px; cursor: pointer; border-radius: 2px; display: inline-flex; align-items: center; gap: 7px; transition: background 0.15s ease;">
                    <i class="fa-regular fa-file-pdf"></i> View Official Transcript (2 Pages)
                  </button>
                  <a href="{prefix}assets/documents/Official_Transcript_IITGN_24510041.pdf" target="_blank" download="Official_Transcript_IITGN_24510041.pdf" style="background: #ffffff; color: #333333; border: 1.5px solid #c0c0c0; padding: 8px 16px; font-family: 'UChicagoSansSerif-Bold', sans-serif; font-size: 12.5px; text-transform: uppercase; text-decoration: none; border-radius: 2px; display: inline-flex; align-items: center; gap: 6px;">
                    <i class="fa-solid fa-download"></i> Download Verified PDF
                  </a>
                </div>

                <!-- Strict Lock Notice — Option to upload new transcript removed -->
                <div style="display: flex; align-items: center; gap: 6px; font-size: 12px; color: #666; background: #f4f4f4; padding: 6px 12px; border-radius: 3px; border: 1px solid #e0e0e0;">
                  <i class="fa-solid fa-lock" style="color: #666;"></i>
                  <span><strong>Upload Locked:</strong> Official institutional transcript verified. Submission of new transcripts is disabled.</span>
                </div>
              </div>
            </div>
          </div>
'''

    transcript_modal = f'''
  <!-- Official Academic Transcript Modal Viewer -->
  <div class="portal-transcript-modal-overlay" id="transcriptModalOverlay" role="dialog" aria-modal="true" aria-labelledby="transcriptModalTitle" aria-hidden="true">
    <div class="portal-transcript-modal-card">
      <div class="portal-transcript-modal-header">
        <div style="display: flex; align-items: center; gap: 12px;">
          <div style="width: 38px; height: 38px; border-radius: 50%; background: #fdf2f2; border: 1px solid maroon; display: flex; align-items: center; justify-content: center; color: maroon; font-size: 18px;">
            <i class="fa-solid fa-file-lines"></i>
          </div>
          <div>
            <h2 id="transcriptModalTitle" style="font-family: 'UChicagoSerif', Georgia, serif; font-size: 18px; margin: 0; color: #111;">
              Indian Institute of Technology Gandhinagar — Official Transcript
            </h2>
            <div style="font-size: 12px; color: #555; margin-top: 2px;">
              Student: <strong>Devendra Dubey Biswambharnath Geeta</strong> • Roll: <strong>24510041</strong> • Ref: <strong>IITGN-MSC-2026-24510041</strong> • CGPA: <strong>8.46 / 10.00</strong>
            </div>
          </div>
        </div>
        <div style="display: flex; align-items: center; gap: 10px;">
          <button type="button" id="transcriptPrintBtn" style="background: #ffffff; border: 1px solid #ccc; color: #333; padding: 6px 12px; font-size: 12px; font-weight: 600; cursor: pointer; border-radius: 2px; display: inline-flex; align-items: center; gap: 5px;">
            <i class="fa-solid fa-print"></i> Print
          </button>
          <a href="{prefix}assets/documents/Official_Transcript_IITGN_24510041.pdf" target="_blank" download="Official_Transcript_IITGN_24510041.pdf" style="background: maroon; color: #fff; text-decoration: none; padding: 6px 12px; font-size: 12px; font-weight: 600; border-radius: 2px; display: inline-flex; align-items: center; gap: 5px;">
            <i class="fa-solid fa-download"></i> Download PDF
          </a>
          <button type="button" id="transcriptModalClose" aria-label="Close Transcript" style="background: transparent; border: none; font-size: 26px; line-height: 1; cursor: pointer; color: #666; padding: 0 4px;">&times;</button>
        </div>
      </div>
      <div class="portal-transcript-modal-body">
        <div class="portal-transcript-page-wrap">
          <div class="portal-transcript-page-label">
            <span>Page 1 of 2 — Consolidated Academic Transcript (Semesters I &amp; II)</span>
            <span>Ref: IITGN-MSC-2026-24510041</span>
          </div>
          <img src="{prefix}assets/documents/transcript_page_1.png" alt="IIT Gandhinagar Official Academic Transcript Page 1 - Devendra Dubey Biswambharnath Geeta" />
        </div>
        <div class="portal-transcript-page-wrap">
          <div class="portal-transcript-page-label">
            <span>Page 2 of 2 — Semesters III &amp; IV, PMRAF Research Fellowship &amp; Graduation Summary</span>
            <span>Final CGPA: 8.46 / 10.00 (First Class with Distinction)</span>
          </div>
          <img src="{prefix}assets/documents/transcript_page_2.png" alt="IIT Gandhinagar Official Academic Transcript Page 2 - Devendra Dubey Biswambharnath Geeta" />
        </div>
      </div>
      <div style="padding: 12px 24px; background: #fafafa; border-top: 1px solid #e0e0e0; display: flex; justify-content: space-between; align-items: center; font-size: 12px; color: #666; flex-shrink: 0;">
        <div>
          <i class="fa-solid fa-shield-halved" style="color: #176531; margin-right: 4px;"></i>
          System Verified Institutional Document • Registrar (Academic Affairs), Indian Institute of Technology Gandhinagar
        </div>
        <button type="button" id="transcriptModalCloseBtn2" style="background: #e0e0e0; color: #333; border: none; padding: 6px 14px; font-size: 12px; font-weight: 600; cursor: pointer; border-radius: 2px;">
          Close Viewer
        </button>
      </div>
    </div>
  </div>
'''

    # Insert transcript card right before the Curriculum Vitae card
    if 'id="portalTranscriptSection"' not in content:
        cv_marker = '<!-- Curriculum Vitae / Resume Section -->'
        if cv_marker in content:
            content = content.replace(cv_marker, transcript_card + "\n" + cv_marker)
        else:
            # Fallback insert before Letters of Recommendation
            lor_marker = '<!-- Letters of Recommendation'
            content = content.replace(lor_marker, transcript_card + "\n" + lor_marker)

    # Update the checklist item
    old_chk = re.search(r'<li class="portal-checklist-item">\s*<div class="portal-checklist-label">\s*<svg[^>]*>.*?</svg>\s*<span>Official Academic Transcripts[^<]*</span>\s*</div>\s*<span class="portal-badge-received">Received[^<]*</span>\s*</li>', content, re.DOTALL)
    if old_chk:
        new_chk = f'''<li class="portal-checklist-item" style="background: #fafafa; border-left: 3px solid #137333;">
                <div class="portal-checklist-label">
                  <svg style="display:inline-block; vertical-align:-2px; margin-right:6px; flex-shrink: 0;" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#176531" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>
                  <div>
                    <div style="font-weight: 700; color: #222;">Official Academic Transcript — Indian Institute of Technology Gandhinagar (IITGN)</div>
                    <div style="font-size: 12px; color: #555; margin-top: 2px;">
                      M.Sc. Chemistry • Ref: IITGN-MSC-2026-24510041 • Final CGPA: <strong>8.46 / 10.00 (Distinction)</strong> • Institutional Copy Received
                    </div>
                  </div>
                </div>
                <div style="display: flex; align-items: center; gap: 8px; flex-shrink: 0;">
                  <button type="button" class="portal-transcript-view-btn" style="background: #ffffff; border: 1px solid #b0b0b0; color: maroon; font-size: 12px; font-weight: 700; padding: 4px 10px; border-radius: 2px; cursor: pointer; display: inline-flex; align-items: center; gap: 4px;">
                    <i class="fa-regular fa-eye"></i> View
                  </button>
                  <span class="portal-badge-received" style="background: #e6f4ea; color: #137333; font-weight: 700;">
                    <i class="fa-solid fa-lock" style="font-size: 10px; margin-right: 3px;"></i> Received &amp; Locked
                  </span>
                </div>
              </li>'''
        content = content[:old_chk.start()] + new_chk + content[old_chk.end():]

    # Insert modal before </body>
    if 'id="transcriptModalOverlay"' not in content:
        content = content.replace('</body>', transcript_modal + '\n</body>')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filepath}")

update_portal_file(r'd:\Microvirt\OBSIDIAN\uchicago_replica\site_1to1\portal.html', is_pages_dir=False)
update_portal_file(r'd:\Microvirt\OBSIDIAN\uchicago_replica\site_1to1\pages\portal.html', is_pages_dir=True)
