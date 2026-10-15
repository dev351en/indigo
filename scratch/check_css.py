import os
import re

pattern = re.compile(r'(?<=[a-zA-Z0-9\-_])\.edu(?=[/?#\'"<>:\s,\)]|$)')

for folder in ['site_1to1', 'site']:
    for root, dirs, files in os.walk(folder):
        for f in files:
            if f.endswith('.css'):
                path = os.path.join(root, f)
                with open(path, 'r', encoding='utf-8', errors='ignore') as fp:
                    content = fp.read()
                matches = pattern.findall(content)
                if matches:
                    print(f"{path}: {len(matches)} matches")
