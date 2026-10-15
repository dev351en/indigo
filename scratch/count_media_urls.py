import os
import re

pattern = re.compile(r'https?://(?:www\.)?uchicago\.asia(/-(?:jss)?media/[^"\'\s>)]+)', re.IGNORECASE)

matches = []
for root, dirs, files in os.walk('site_1to1'):
    for f in files:
        if f.endswith(('.html', '.js')):
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8', errors='ignore') as fp:
                c = fp.read()
            found = pattern.findall(c)
            if found:
                matches.append((path, len(found)))

print(f"Total files with uchicago.edu/-/media or /-/jssmedia: {len(matches)}")
print(f"Total occurrences: {sum(m[1] for m in matches)}")
