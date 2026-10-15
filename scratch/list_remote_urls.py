import os
import re

img_src_pattern = re.compile(r'src=["\'](https?://[^"\']*(?:uchicago\.asia|uchicago\.edu)[^"\']*)["\']', re.IGNORECASE)
bg_pattern = re.compile(r'url\(["\']?(https?://[^"\')\s]*(?:uchicago\.asia|uchicago\.edu)[^"\')\s]*)["\']?\)', re.IGNORECASE)

urls = set()

for root, dirs, files in os.walk('site_1to1'):
    for f in files:
        if f.endswith(('.html', '.js')):
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8', errors='ignore') as fp:
                c = fp.read()
            for u in img_src_pattern.findall(c):
                urls.add(u)
            for u in bg_pattern.findall(c):
                urls.add(u)

print(f"Total unique remote uchicago URLs in src and url(): {len(urls)}")
for u in sorted(list(urls))[:20]:
    print(" ", u)
