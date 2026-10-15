import os
import re

img_pattern = re.compile(r'<img\s+[^>]*?src=["\']([^"\']+)["\'][^>]*>', re.IGNORECASE)

pages_to_check = [
    'site_1to1/index.html',
    'site_1to1/portal.html',
    'site_1to1/pages/department-of-chemistry.html',
    'site_1to1/pages/faculty.html',
    'site_1to1/pages/academics_academic-departments.html',
    'site_1to1/pages/academics.html',
    'site_1to1/pages/admissions.html'
]

for p in pages_to_check:
    if not os.path.exists(p):
        continue
    with open(p, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    matches = img_pattern.findall(content)
    print(f"\n=== {p} (Total images: {len(matches)}) ===")
    for src in matches[:10]:
        exists = "REMOTE"
        if not src.startswith(('http://', 'https://', '//', 'data:')):
            rel_path = os.path.normpath(os.path.join(os.path.dirname(p), src.split('?')[0]))
            root_rel = os.path.normpath(os.path.join('site_1to1', src.lstrip('/').split('?')[0]))
            exists = "EXISTS" if os.path.exists(rel_path) or os.path.exists(root_rel) else "MISSING"
        print(f"  src: {src[:70]} | {exists}")
