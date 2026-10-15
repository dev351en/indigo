import os
import re

pattern = re.compile(r'([a-zA-Z0-9\-_.]+\.edu)(?=[/?#\'"<>:\s,\)]|$)')

matches = set()
for folder in ['site_1to1', 'site']:
    for root, dirs, files in os.walk(folder):
        for f in files:
            if f.endswith('.html') or f.endswith('.js') or f.endswith('.json'):
                path = os.path.join(root, f)
                with open(path, 'r', encoding='utf-8', errors='ignore') as fp:
                    content = fp.read()
                found = pattern.findall(content)
                for m in found:
                    matches.add(m)

print(f"Total unique domains matched: {len(matches)}")
sample = sorted(list(matches))
print("Sample of matches (first 25):")
for s in sample[:25]:
    print("  ", s)
print("Sample of matches (last 25):")
for s in sample[-25:]:
    print("  ", s)
