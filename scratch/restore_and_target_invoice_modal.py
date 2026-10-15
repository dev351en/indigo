import os

base_dir = os.path.dirname(os.path.abspath(__file__))
site_dir = os.path.join(base_dir, "..", "site_1to1")

files = [
    os.path.join(site_dir, "portal.html"),
    os.path.join(site_dir, "pages", "portal.html"),
    os.path.join(site_dir, "index.html"),
]

for fp in files:
    if not os.path.exists(fp):
        continue
    with open(fp, "r", encoding="utf-8") as f:
        content = f.read()

    rel = "../" if "/pages/" in fp.replace("\\", "/") else ""

    # Restore Transcript Modal Header
    transcript_target_start = content.find('id="transcriptModalOverlay"')
    if transcript_target_start != -1:
        card_start = content.find('<div class="portal-transcript-modal-card">', transcript_target_start)
        body_start = content.find('<div class="portal-transcript-modal-body">', card_start)
        if card_start != -1 and body_start != -1:
            proper_transcript_header = f'''<div class="portal-transcript-modal-card">
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
          <a href="{rel}assets/documents/Official_Transcript_IITGN_24510041.pdf" target="_blank" download="Official_Transcript_IITGN_24510041.pdf" style="background: maroon; color: #fff; text-decoration: none; padding: 6px 12px; font-size: 12px; font-weight: 600; border-radius: 2px; display: inline-flex; align-items: center; gap: 5px;">
            <i class="fa-solid fa-download"></i> Download PDF
          </a>
          <button type="button" id="transcriptModalClose" aria-label="Close Transcript" style="background: transparent; border: none; font-size: 26px; line-height: 1; cursor: pointer; color: #666; padding: 0 4px;">&times;</button>
        </div>
      </div>
      '''
            content = content[:card_start] + proper_transcript_header + content[body_start:]
            print(f"Restored transcript header in {os.path.basename(fp)}")

    # Restore CV Modal Header
    cv_target_start = content.find('id="cvModalOverlay"')
    if cv_target_start != -1:
        card_start = content.find('<div class="portal-transcript-modal-card">', cv_target_start)
        body_start = content.find('<div class="portal-transcript-modal-body">', card_start)
        if card_start != -1 and body_start != -1:
            proper_cv_header = f'''<div class="portal-transcript-modal-card">
      <div class="portal-transcript-modal-header">
        <div style="display: flex; align-items: center; gap: 12px;">
          <div style="width: 38px; height: 38px; border-radius: 50%; background: #fdf2f2; border: 1px solid maroon; display: flex; align-items: center; justify-content: center; color: maroon; font-size: 18px;">
            <i class="fa-solid fa-file-invoice"></i>
          </div>
          <div>
            <h2 id="cvModalTitle" style="font-family: 'UChicagoSerif', Georgia, serif; font-size: 18px; margin: 0; color: #111;">
              Curriculum Vitae — Devendra B. Dubey
            </h2>
            <div style="font-size: 12px; color: #555; margin-top: 2px;">
              Candidate: <strong>Devendra B. Dubey</strong> • M.Sc. Chemistry, IITGN (CPI: <strong>8.46/10</strong>) • PMRAF Fellow • IIT JAM AIR <strong>403</strong>
            </div>
          </div>
        </div>
        <div style="display: flex; align-items: center; gap: 10px;">
          <button type="button" id="cvPrintBtn" style="background: #ffffff; border: 1px solid #ccc; color: #333; padding: 6px 12px; font-size: 12px; font-weight: 600; cursor: pointer; border-radius: 2px; display: inline-flex; align-items: center; gap: 5px;">
            <i class="fa-solid fa-print"></i> Print
          </button>
          <a href="{rel}assets/documents/CV_Devendra_B_Dubey.pdf" target="_blank" download="CV_Devendra_B_Dubey.pdf" style="background: maroon; color: #fff; text-decoration: none; padding: 6px 12px; font-size: 12px; font-weight: 600; border-radius: 2px; display: inline-flex; align-items: center; gap: 5px;">
            <i class="fa-solid fa-download"></i> Download PDF
          </a>
          <button type="button" id="cvModalClose" aria-label="Close CV" style="background: transparent; border: none; font-size: 26px; line-height: 1; cursor: pointer; color: #666; padding: 0 4px;">&times;</button>
        </div>
      </div>
      '''
            content = content[:card_start] + proper_cv_header + content[body_start:]
            print(f"Restored CV header in {os.path.basename(fp)}")

    with open(fp, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Saved {fp}")
