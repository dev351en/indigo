import os
import re

pattern = re.compile(r'(?<=[a-zA-Z0-9\-_])\.edu(?![a-zA-Z0-9\-_])', re.IGNORECASE)

total_matches = 0
file_count = 0
unique_domains = set()

for folder in ['site_1to1', 'site']:
    for root, dirs, files in os.walk(folder):
        for f in files:
            if f.endswith(('.html', '.js', '.json')):
                path = os.path.join(root, f)
                with open(path, 'r', encoding='utf-8', errors='ignore') as fp:
                    content = fp.read()
                matches = pattern.findall(content)
                if matches:
                    file_count += 1
                    total_matches += len(matches)
                # Find the domain names
                domains = re.findall(r'([a-zA-Z0-9\-_.]+\.edu)(?![a-zA-Z0-9\-_])', content, re.IGNORECASE)
                for d in domains:
                    unique_domains.add(d.lower())

print(f"Total files with matches: {file_count}")
print(f"Total matches to be replaced: {total_matches}")
print(f"Unique domains: {len(unique_domains)}")
for d in sorted(list(unique_domains))[:15]:
    print("  ", d)
print("  ...")
for d in sorted(list(unique_domains))[-15:]:
    print("  ", d)
