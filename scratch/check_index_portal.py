with open('site_1to1/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
print("portal.html occurrences in index.html:")
for m in re.finditer(r'href="[^"]*portal[^"]*"', text):
    print(m.group(0))

print("\nScripts referencing portal:")
scripts = re.findall(r'<script[^>]*>([\s\S]*?)</script>', text)
for i, s in enumerate(scripts):
    if 'portal' in s.lower():
        print(f"=== Script {i} ===")
        for line in s.split('\n'):
            if 'portal' in line.lower():
                print("  ", line.strip())
