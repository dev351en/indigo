import os
import re

img_src_pattern = re.compile(r'<img\s+[^>]*?src=["\']([^"\']+)["\']', re.IGNORECASE)
bg_img_pattern = re.compile(r'url\(["\']?([^"\')]+)["\']?\)', re.IGNORECASE)

remote_images = set()
local_images = set()

for root, dirs, files in os.walk('site_1to1'):
    for f in files:
        if f.endswith(('.html', '.js', '.css')):
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8', errors='ignore') as fp:
                content = fp.read()
            for src in img_src_pattern.findall(content):
                if 'uchicago.asia' in src or 'uchicago.edu' in src:
                    remote_images.add(src)
                elif not src.startswith(('http://', 'https://', 'data:')):
                    local_images.add(src)
            for src in bg_img_pattern.findall(content):
                if 'uchicago.asia' in src or 'uchicago.edu' in src:
                    remote_images.add(src)

print(f"Total remote uchicago image URLs found: {len(remote_images)}")
for r in sorted(list(remote_images))[:20]:
    print(" ", r)
