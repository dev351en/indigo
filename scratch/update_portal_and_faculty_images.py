import re

# 1. Update portal.html in site_1to1 and site
for portal_path in ['site_1to1/portal.html', 'site/portal.html']:
    with open(portal_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    old_target = """<div class="portal-faculty-card">
            <div class="portal-faculty-badge"><i class="fa-solid fa-circle-check"></i> Faculty Acceptance Confirmed</div>
            <div class="portal-faculty-title">Research Advisor &amp; Laboratory Placement</div>
            <div class="portal-faculty-desc">
              You have been selected and officially accepted as a doctoral research student under <strong>Prof. Alex (Alexander Q.) Cusumano</strong>, Assistant Professor of Chemistry (Computational &amp; Theoretical Chemistry, Catalysis) in the Department of Chemistry.
            </div>"""

    new_replacement = """<div class="portal-faculty-card">
            <div class="portal-faculty-badge"><i class="fa-solid fa-circle-check"></i> Faculty Acceptance Confirmed</div>
            <div class="portal-faculty-title">Research Advisor &amp; Laboratory Placement</div>
            <div style="display: flex; gap: 20px; align-items: flex-start; flex-wrap: wrap; margin-bottom: 14px;">
              <div style="text-align: center; flex-shrink: 0;">
                <img src="assets/faculty/alex_cusumano.jpg" alt="Prof. Alex Cusumano" style="width: 110px; height: 130px; object-fit: cover; border-radius: 4px; border: 2px solid maroon; box-shadow: 0 4px 10px rgba(0,0,0,0.15);" />
                <div style="font-size: 11px; font-weight: 700; color: maroon; margin-top: 4px;">Advisor Photo</div>
              </div>
              <div style="flex: 1; min-width: 250px;">
                <div class="portal-faculty-desc" style="margin-top: 0;">
                  You have been selected and officially accepted as a doctoral research student under <strong>Prof. Alex (Alexander Q.) Cusumano</strong>, Assistant Professor of Chemistry (Computational &amp; Theoretical Chemistry, Catalysis) in the Department of Chemistry.
                </div>
              </div>
            </div>"""

    if old_target in content:
        content = content.replace(old_target, new_replacement, 1)
        with open(portal_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {portal_path} with advisor portrait!")
    else:
        print(f"Target not found in {portal_path}")

# 2. Update faculty.html in site_1to1
faculty_path = 'site_1to1/pages/faculty.html'
with open(faculty_path, 'r', encoding='utf-8') as f:
    fac_content = f.read()

old_chem_card_target = """<div style="background: #fafafa; border-left: 3px solid #800000; padding: 10px 14px; margin-bottom: 18px; font-size: 13px; color: #333;">
            <strong>Featured Faculty:</strong> Prof. Alex Cusumano (Graduate Advisor), Prof. Bryan Dickinson, Prof. Chuan He, Prof. Laura Gagliardi, Prof. Bozhi Tian
          </div>"""

new_chem_card_replacement = """<div style="display: flex; gap: 8px; margin-bottom: 14px; align-items: center; flex-wrap: wrap;">
            <img src="../assets/faculty/alex_cusumano.jpg" alt="Prof. Alex Cusumano" title="Prof. Alex Cusumano (Graduate Advisor)" style="width: 44px; height: 44px; border-radius: 50%; object-fit: cover; border: 2px solid #800000;" />
            <img src="../assets/faculty/chuan_he.jpg" alt="Prof. Chuan He" title="Prof. Chuan He (MacArthur Fellow, Wolf Prize)" style="width: 44px; height: 44px; border-radius: 50%; object-fit: cover; border: 2px solid #ddd;" />
            <img src="../assets/faculty/laura_gagliardi.png" alt="Prof. Laura Gagliardi" title="Prof. Laura Gagliardi" style="width: 44px; height: 44px; border-radius: 50%; object-fit: cover; border: 2px solid #ddd;" />
            <img src="../assets/faculty/jack_w_szostak.jpg" alt="Prof. Jack Szostak" title="Prof. Jack Szostak (Nobel Laureate)" style="width: 44px; height: 44px; border-radius: 50%; object-fit: cover; border: 2px solid #b8860b;" />
            <img src="../assets/faculty/bryan_dickinson.jpg" alt="Prof. Bryan Dickinson" title="Prof. Bryan Dickinson" style="width: 44px; height: 44px; border-radius: 50%; object-fit: cover; border: 2px solid #ddd;" />
            <span style="font-size: 12px; color: #666; font-weight: 700; margin-left: 4px;">+38 Faculty</span>
          </div>
          <div style="background: #fafafa; border-left: 3px solid #800000; padding: 10px 14px; margin-bottom: 18px; font-size: 13px; color: #333;">
            <strong>Featured Faculty:</strong> Prof. Alex Cusumano (Graduate Advisor), Prof. Bryan Dickinson, Prof. Chuan He, Prof. Laura Gagliardi, Prof. Bozhi Tian
          </div>"""

if old_chem_card_target in fac_content:
    fac_content = fac_content.replace(old_chem_card_target, new_chem_card_replacement, 1)
    with open(faculty_path, 'w', encoding='utf-8') as f:
        f.write(fac_content)
    print("Updated faculty.html with faculty avatars on Chemistry card!")
else:
    print("Chem card target not found in faculty.html")
