import os
import re

pattern = re.compile(r'https://www\.uchicago\.asia(/-/(?:jss)?media/[^"\'\s>)]+)', re.IGNORECASE)

urls_to_download = set()

for root, dirs, files in os.walk('site_1to1'):
    for f in files:
        if f.endswith(('.html', '.js', '.css')):
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8', errors='ignore') as fp:
                c = fp.read()
            for rel in pattern.findall(c):
                urls_to_download.add(rel)

print(f"Total unique uchicago media paths to download: {len(urls_to_download)}")
for u in sorted(list(urls_to_download))[:25]:
    print(" ", u)
