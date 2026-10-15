with open("site_1to1/pages/academics.html", "r", encoding="utf-8") as f:
    html = f.read()

import re
matches = re.findall(r'<span class="[^"]*image[^"]*"[^>]*>\s*</span>', html, re.I)
print(f"Empty spans count: {len(matches)}")
for m in re.finditer(r'<span class="[^"]*image[^"]*"[^>]*>\s*</span>', html, re.I):
    start = max(0, m.start() - 150)
    end = min(len(html), m.end() + 250)
    print("--- SPAN SNIPPET ---")
    print(html[start:end])
