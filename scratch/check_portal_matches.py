import os
import re

pattern = re.compile(r'(?<=[a-zA-Z0-9\-_])\.edu(?=[/?#\'"<>:\s,\)]|$)')

files_to_check = [
    'site_1to1/portal.html',
    'site_1to1/app.js',
    'site/portal.html',
    'site/app.js'
]

for p in files_to_check:
    if os.path.exists(p):
        with open(p, 'r', encoding='utf-8') as f:
            content = f.read()
        matches = list(pattern.finditer(content))
        print(f"{p}: {len(matches)} matches")
        for m in matches[:5]:
            start = max(0, m.start() - 20)
            end = min(len(content), m.end() + 20)
            print("   context:", repr(content[start:end]))
