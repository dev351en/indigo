import os
import re

edu_pattern = re.compile(r'([a-zA-Z0-9\-_.]*\.edu[a-zA-Z0-9\-_.]*)', re.IGNORECASE)

remaining = []
for folder in ['site_1to1', 'site']:
    for root, dirs, files in os.walk(folder):
        for f in files:
            if f.endswith(('.html', '.js', '.json', '.css')):
                path = os.path.join(root, f)
                with open(path, 'r', encoding='utf-8', errors='ignore') as fp:
                    content = fp.read()
                matches = edu_pattern.findall(content)
                for m in matches:
                    remaining.append((path, m))

print(f"Total remaining matches for .edu*: {len(remaining)}")
for path, m in remaining[:20]:
    print(f"  {path}: {m}")
