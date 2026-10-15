with open(r'd:\Microvirt\OBSIDIAN\uchicago_replica\site_1to1\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

prefix = ""

transcript_card = f'''      <!-- Official Academic Transcript Card -->
      <div class="portal-card-block" id="portalTranscriptSection" style="margin-bottom: 16px;">
        <div style="background: #ffffff; border: 1px solid #e0e0e0; border-left: 4px solid #137333; padding: 18px 20px; border-radius: 4px; box-shadow: 0 1px 4px rgba(0,0,0,0.04);">
          <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 14px; margin-bottom: 14px;">
            <div style="display: flex; gap: 14px; align-items: flex-start;">
              <div style="width: 44px; height: 44px; border-radius: 50%; background: #fdf2f2; border: 1.5px solid maroon; display: flex; align-items: center; justify-content: center; color: maroon; font-size: 20px; flex-shrink: 0;">
                <i class="fa-solid fa-graduation-cap"></i>
              </div>
              <div>
                <div style="font-weight: 700; font-size: 15.5px; color: #111;">
                  Indian Institute of Technology Gandhinagar (IITGN)
                </div>
                <div style="font-size: 12.5px; color: #333; margin-top: 2px; font-weight: 500;">
                  Official Academic Transcript &amp; Grade Record • Ref: <strong>IITGN-MSC-2026-24510041</strong>
                </div>
                <div style="font-size: 11.5px; color: #666; margin-top: 3px; line-height: 1.4;">
                  Student: <strong>Devendra Dubey Biswambharnath Geeta</strong> • Roll: <strong>24510041</strong><br />
                  Program: <strong>M.Sc. Chemistry (2024–2026)</strong> • Verified: <strong>24th August 2026</strong>
                </div>
              </div>
            </div>
            <div style="text-align: right; flex-shrink: 0;">
              <div style="background: #f0f7f2; border: 1px solid #c2e2cc; border-radius: 4px; padding: 6px 12px; display: inline-block; text-align: right;">
                <div style="font-size: 10px; text-transform: uppercase; letter-spacing: 0.5px; color: #137333; font-weight: 700;">Final Cumulative GPA</div>
                <div style="font-size: 18px; font-weight: 800; color: #0d652d; line-height: 1.2;">8.46 <span style="font-size: 11px; font-weight: 500; color: #666;">/ 10.00</span></div>
                <div style="font-size: 10.5px; color: #137333; font-weight: 700; margin-top: 1px;">First Class with Distinction</div>
              </div>
            </div>
          </div>

          <!-- Academic Metrics & Highlights Grid -->
          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(110px, 1fr)); gap: 8px; background: #fafafa; border: 1px solid #eee; padding: 10px 12px; border-radius: 3px; margin-bottom: 12px; font-size: 11.5px;">
            <div><span style="color:#666;">Total Credits:</span> <strong style="color:#111;">85</strong></div>
            <div><span style="color:#666;">GPA Credits:</span> <strong style="color:#111;">74</strong></div>
            <div><span style="color:#666;">Courses:</span> <strong style="color:#111;">28</strong></div>
            <div><span style="color:#666;">Credit Points:</span> <strong style="color:#111;">626</strong></div>
            <div><span style="color:#666;">Status:</span> <strong style="color:#137333;"><i class="fa-solid fa-circle-check"></i> Completed</strong></div>
          </div>

          <!-- Research Fellowship Remark -->
          <div style="font-size: 11px; line-height: 1.45; color: #555; background: #fffdf5; border: 1px solid #f0e6c8; padding: 7px 10px; border-radius: 3px; margin-bottom: 14px;">
            <strong style="color: #856404;"><i class="fa-solid fa-award"></i> PMRAF Fellowship:</strong> Pursuing Prime Minister's Research Assistant Fellowship (PMRAF) at Physical Research Laboratory (PRL), Ahmedabad under Prof. Bhaskar Datta.
          </div>

          <!-- Actions & Locked Upload Notice -->
          <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px; padding-top: 12px; border-top: 1px solid #f0f0f0;">
            <div style="display: flex; gap: 8px; flex-wrap: wrap;">
              <button type="button" class="portal-transcript-view-btn" id="portalTranscriptPreviewBtn" style="background: maroon; color: #ffffff; border: none; padding: 8px 14px; font-family: 'UChicagoSansSerif-Bold', sans-serif; font-size: 11.5px; text-transform: uppercase; letter-spacing: 0.5px; cursor: pointer; border-radius: 2px; display: inline-flex; align-items: center; gap: 6px;">
                <i class="fa-regular fa-file-pdf"></i> View Official Transcript (2 Pages)
              </button>
              <a href="assets/documents/Official_Transcript_IITGN_24510041.pdf" target="_blank" download="Official_Transcript_IITGN_24510041.pdf" style="background: #ffffff; color: #333333; border: 1px solid #c0c0c0; padding: 7px 12px; font-family: 'UChicagoSansSerif-Bold', sans-serif; font-size: 11.5px; text-transform: uppercase; text-decoration: none; border-radius: 2px; display: inline-flex; align-items: center; gap: 5px;">
                <i class="fa-solid fa-download"></i> Download PDF
              </a>
            </div>

            <!-- Upload Locked Notice -->
            <div style="display: flex; align-items: center; gap: 5px; font-size: 11px; color: #666; background: #f4f4f4; padding: 5px 10px; border-radius: 3px; border: 1px solid #e0e0e0;">
              <i class="fa-solid fa-lock" style="color: #666;"></i>
              <span><strong>Upload Locked:</strong> Official transcript verified. Upload option disabled.</span>
            </div>
          </div>
        </div>
      </div>
'''

transcript_modal = f'''  <!-- Official Academic Transcript Modal Viewer -->
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
          <a href="assets/documents/Official_Transcript_IITGN_24510041.pdf" target="_blank" download="Official_Transcript_IITGN_24510041.pdf" style="background: maroon; color: #fff; text-decoration: none; padding: 6px 12px; font-size: 12px; font-weight: 600; border-radius: 2px; display: inline-flex; align-items: center; gap: 5px;">
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
          <img src="assets/documents/transcript_page_1.png" alt="IIT Gandhinagar Official Academic Transcript Page 1 - Devendra Dubey Biswambharnath Geeta" />
        </div>
        <div class="portal-transcript-page-wrap">
          <div class="portal-transcript-page-label">
            <span>Page 2 of 2 — Semesters III &amp; IV, PMRAF Research Fellowship &amp; Graduation Summary</span>
            <span>Final CGPA: 8.46 / 10.00 (First Class with Distinction)</span>
          </div>
          <img src="assets/documents/transcript_page_2.png" alt="IIT Gandhinagar Official Academic Transcript Page 2 - Devendra Dubey Biswambharnath Geeta" />
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
  </div>'''

# Insert card before Resume section in index.html
if 'id="portalTranscriptSection"' not in content:
    cv_marker = '<!-- Curriculum Vitae / Resume Section -->'
    if cv_marker in content:
        content = content.replace(cv_marker, transcript_card + "\n      " + cv_marker)

# Update checklist item
old_item = '''        <li class="portal-checklist-item">
          <div class="portal-checklist-label"><i class="fa-solid fa-check"></i> <span>Official Academic Transcripts (Undergraduate &amp; Postgraduate)</span></div>
          <span class="portal-badge-received">Received (Official)</span>
        </li>'''

new_item = '''        <li class="portal-checklist-item" style="background: #fafafa; border-left: 3px solid #137333;">
          <div class="portal-checklist-label">
            <i class="fa-solid fa-circle-check" style="color: #176531;"></i>
            <div>
              <div style="font-weight: 700; color: #222;">Official Academic Transcript — IIT Gandhinagar</div>
              <div style="font-size: 11px; color: #555; margin-top: 1px;">Ref #IITGN-MSC-2026-24510041 • CGPA: 8.46 / 10.00 • Institutional Record Locked</div>
            </div>
          </div>
          <div style="display: flex; align-items: center; gap: 6px; flex-shrink: 0;">
            <button type="button" class="portal-transcript-view-btn" style="background: #ffffff; border: 1px solid #b0b0b0; color: maroon; font-size: 11px; font-weight: 700; padding: 3px 8px; border-radius: 2px; cursor: pointer; display: inline-flex; align-items: center; gap: 3px;">
              <i class="fa-regular fa-eye"></i> View
            </button>
            <span class="portal-badge-received" style="background: #e6f4ea; color: #137333; font-weight: 700; font-size: 11px; padding: 3px 8px;">
              <i class="fa-solid fa-lock" style="font-size: 9px; margin-right: 2px;"></i> Locked
            </span>
          </div>
        </li>'''

if old_item in content:
    content = content.replace(old_item, new_item)

if 'id="transcriptModalOverlay"' not in content:
    content = content.replace('</body>', transcript_modal + '\n</body>')

with open(r'd:\Microvirt\OBSIDIAN\uchicago_replica\site_1to1\index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated index.html with transcript card, locked status, and viewer modal!")
