import os
import re

pattern = re.compile(r'https?://(?:www\.)?uchicago\.asia/-(?:jss)?media/[^"\'\s>)]+', re.IGNORECASE)

files_with_media = {}
for root, dirs, files in os.walk('site_1to1'):
    for f in files:
        if f.endswith(('.html', '.js', '.css')):
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8', errors='ignore') as fp:
                c = fp.read()
            matches = pattern.findall(c)
            if matches:
                files_with_media[path] = len(matches)

print(f"Total files with uchicago.edu media: {len(files_with_media)}")
for p, count in sorted(files_with_media.items(), key=lambda x: x[1], reverse=True)[:25]:
    print(f"  {p}: {count} media URLs")
