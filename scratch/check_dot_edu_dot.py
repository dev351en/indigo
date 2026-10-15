import os
import re

dot_pattern = re.compile(r'\.edu\.', re.IGNORECASE)

for folder in ['site_1to1', 'site']:
    for root, dirs, files in os.walk(folder):
        for f in files:
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8', errors='ignore') as fp:
                content = fp.read()
            matches = list(dot_pattern.finditer(content))
            if matches:
                print(f"{path}: {len(matches)} matches for .edu.")
                for m in matches[:3]:
                    start = max(0, m.start() - 25)
                    end = min(len(content), m.end() + 25)
                    print("  ", repr(content[start:end]))
