import os
import re

for kp in ['who-we-are.html', 'academics.html', 'academics_academic-departments.html']:
    raw_p = os.path.join('raw_scraped_pages', kp)
    site_p = os.path.join('site_1to1/pages', kp)
    with open(raw_p, 'r', encoding='utf-8', errors='ignore') as f:
        raw_html = f.read()
    with open(site_p, 'r', encoding='utf-8', errors='ignore') as f:
        site_html = f.read()
    print(f"=== {kp} ===")
    print("Raw len:", len(raw_html), "Site len:", len(site_html))
    site_added = re.findall(r'(\.\./assets/subpage_media/[^\s"\'\>]+)', site_html)
    print("Injected subpage_media:", site_added)
