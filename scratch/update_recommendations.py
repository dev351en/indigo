import re

lor_block_full = '''          <!-- Letters of Recommendation (5 of 5 Received) -->
          <div class="portal-card-block">
            <h2 class="portal-card-block-title">
              <span><i class="fa-solid fa-envelope-open-text" style="color: maroon; margin-right: 8px;"></i>Letters of Recommendation</span>
              <span style="font-size: 12px; font-family: 'UChicagoSansSerif-Regular', sans-serif; color: #176531; font-weight: 700;">5 of 5 Received</span>
            </h2>
            <ul class="portal-checklist">
              <li class="portal-checklist-item">
                <div class="portal-checklist-label">
                  <svg style="display:inline-block; vertical-align:-2px; margin-right:4px;" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#176531" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>
                  <div>
                    <div style="font-weight: 600; color: #222;">1. Dr. Bhaskar Datta</div>
                    <div style="font-size: 12px; color: #666;">Professor, Department of Chemistry &amp; Biological Engineering • Indian Institute of Technology (IIT) Gandhinagar</div>
                  </div>
                </div>
                <span class="portal-badge-received">Received (Official)</span>
              </li>
              <li class="portal-checklist-item">
                <div class="portal-checklist-label">
                  <svg style="display:inline-block; vertical-align:-2px; margin-right:4px;" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#176531" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>
                  <div>
                    <div style="font-weight: 600; color: #222;">2. Dr. Sivapriya Kirubakaran</div>
                    <div style="font-size: 12px; color: #666;">Professor &amp; Head, Department of Chemistry • Indian Institute of Technology (IIT) Gandhinagar</div>
                  </div>
                </div>
                <span class="portal-badge-received">Received (Official)</span>
              </li>
              <li class="portal-checklist-item">
                <div class="portal-checklist-label">
                  <svg style="display:inline-block; vertical-align:-2px; margin-right:4px;" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#176531" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>
                  <div>
                    <div style="font-weight: 600; color: #222;">3. Dr. Shraedha Tiwari</div>
                    <div style="font-size: 12px; color: #666;">Assistant Professor, Department of Chemistry • Institute of Chemical Technology (ICT) Mumbai, India</div>
                  </div>
                </div>
                <span class="portal-badge-received">Received (Official)</span>
              </li>
              <li class="portal-checklist-item">
                <div class="portal-checklist-label">
                  <svg style="display:inline-block; vertical-align:-2px; margin-right:4px;" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#176531" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>
                  <div>
                    <div style="font-weight: 600; color: #222;">4. Dr. Kasturi Venkataraman</div>
                    <div style="font-size: 12px; color: #666;">Professor • Indian Institute of Science (IISc) Bangalore</div>
                  </div>
                </div>
                <span class="portal-badge-received">Received (Official)</span>
              </li>
              <li class="portal-checklist-item">
                <div class="portal-checklist-label">
                  <svg style="display:inline-block; vertical-align:-2px; margin-right:4px;" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#176531" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>
                  <div>
                    <div style="font-weight: 600; color: #222;">5. Dr. Sriram Kanvah Gundimeda</div>
                    <div style="font-size: 12px; color: #666;">Professor, Department of Chemistry • Indian Institute of Technology (IIT) Gandhinagar</div>
                  </div>
                </div>
                <span class="portal-badge-received">Received (Official)</span>
              </li>
            </ul>
          </div>'''

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Remove Demo Credentials Helper Callout
    # Search for anything matching the demo credentials box
    content = re.sub(
        r'<!-- Demo Credentials Helper Callout -->\s*<div style="margin-top: 24px; padding: 12px 14px; background: #fafafa; border: 1px dashed #c0c0c0;.*?</div>\s*',
        '',
        content,
        flags=re.DOTALL
    )

    # In case there's any other variant
    content = re.sub(
        r'<div style="margin-top: 24px;[^"]*border: 1px dashed #c0c0c0;.*?</div>\s*',
        '',
        content,
        flags=re.DOTALL
    )

    # 2. Make input placeholders clean without demo IDs
    content = content.replace('placeholder="e.g. UC-2027-89321 or your registered email"', 'placeholder="Application ID or registered email"')
    content = content.replace('placeholder="e.g. UC-2027-89321 or your email"', 'placeholder="Application ID or email"')

    # 3. Replace Letters of Recommendation section
    lor_match = re.search(r'<!-- Letters of Recommendation.*?</ul>\s*</div>', content, re.DOTALL)
    if lor_match:
        content = content[:lor_match.start()] + lor_block_full + content[lor_match.end():]
        print(f"[{filepath}] Replaced Letters of Recommendation block.")
    else:
        print(f"[{filepath}] Warning: Letters of Recommendation block not found.")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Saved {filepath}")

process_file(r'd:\Microvirt\OBSIDIAN\uchicago_replica\site_1to1\portal.html')
process_file(r'd:\Microvirt\OBSIDIAN\uchicago_replica\site_1to1\pages\portal.html')
