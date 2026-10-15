import os
import re

img_src_pattern = re.compile(r'src=["\'](https?://www\.uchicago\.asia(/-(?:jss)?media/[^"\']+))["\']', re.IGNORECASE)
bg_pattern = re.compile(r'url\(["\']?(https?://www\.uchicago\.asia(/-(?:jss)?media/[^"\'\)]+))["\']?\)', re.IGNORECASE)

unique_media = {}

for root, dirs, files in os.walk('site_1to1'):
    for f in files:
        if f.endswith(('.html', '.js', '.css')):
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8', errors='ignore') as fp:
                c = fp.read()
            for full, rel in img_src_pattern.findall(c):
                unique_media[full] = rel
            for full, rel in bg_pattern.findall(c):
                unique_media[full] = rel

print(f"Total unique media URLs: {len(unique_media)}")
for k, v in list(unique_media.items())[:15]:
    print(f"  {k} -> {v}")
