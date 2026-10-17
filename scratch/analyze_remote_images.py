import os
import re

site_dir = 'site_1to1'
img_pat = re.compile(r'<img\s+[^>]*?src=["\']([^"\']+)["\']', re.IGNORECASE)

counts = {}
for root, dirs, files in os.walk(site_dir):
    for f in files:
        if f.endswith('.html'):
            filepath = os.path.join(root, f)
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as fp:
                c = fp.read()
            imgs = [src for src in img_pat.findall(c) if src.startswith(('http://', 'https://', '//')) and '${' not in src]
            if imgs:
                counts[filepath] = imgs

print(f"Files with remote images: {len(counts)}")
for k, v in sorted(counts.items(), key=lambda x: -len(x[1]))[:25]:
    print(f"{k}: {len(v)} remote images")
    for src in v[:3]:
        print(f"    {src[:90]}")
