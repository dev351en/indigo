import os
import re
from urllib.parse import urlparse

site_dir = 'site_1to1'
html_files = []
for root, dirs, files in os.walk(site_dir):
    for f in files:
        if f.endswith('.html'):
            html_files.append(os.path.join(root, f))

print(f"Total HTML files in {site_dir}: {len(html_files)}")

# 1. Check uchicago.edu occurrences (case-insensitive)
edu_matches = []
edu_pat = re.compile(r'uchicago\.edu', re.IGNORECASE)
for hf in html_files:
    content = open(hf, 'r', encoding='utf-8', errors='ignore').read()
    found = edu_pat.findall(content)
    if found:
        edu_matches.append((hf, len(found)))

print(f"\n1. UCHICAGO.EDU occurrences: {len(edu_matches)} files")
for hf, cnt in edu_matches:
    print(f"   {hf}: {cnt}")

# 2. Check remote images
img_pat = re.compile(r'<img\s+[^>]*?src=["\']([^"\']+)["\']', re.IGNORECASE)
remote_imgs = {}
broken_local_imgs = []

for hf in html_files:
    content = open(hf, 'r', encoding='utf-8', errors='ignore').read()
    for src in img_pat.findall(content):
        # Ignore template strings like ${photoSrc}
        if '${' in src:
            continue
        clean_src = src.split('?')[0].split('#')[0]
        if clean_src.startswith(('http://', 'https://', '//')):
            remote_imgs.setdefault(clean_src, []).append(hf)
        elif not clean_src.startswith('data:'):
            # check local existence
            rel_path = os.path.normpath(os.path.join(os.path.dirname(hf), clean_src))
            root_rel = os.path.normpath(os.path.join(site_dir, clean_src.lstrip('/')))
            if not (os.path.exists(rel_path) or os.path.exists(root_rel)):
                broken_local_imgs.append((hf, src))

print(f"\n2. Unique Remote Images: {len(remote_imgs)}")
for rimg, files in list(remote_imgs.items())[:20]:
    print(f"   {rimg} (used in {len(files)} files)")

print(f"\n3. Broken Local Images: {len(broken_local_imgs)}")
for hf, src in broken_local_imgs[:20]:
    print(f"   {hf} -> {src}")
