import os
import glob
import re

pages = glob.glob("site_1to1/pages/*.html")
print(f"Scanning {len(pages)} subpages...")

empty_containers = []
for p in pages:
    with open(p, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
    
    empty_spans = re.findall(r'<span class="[^"]*image[^"]*"[^>]*>\s*</span>', content, re.I)
    if empty_spans:
        empty_containers.append((os.path.basename(p), len(empty_spans)))

print(f"Found {len(empty_containers)} pages with empty image spans:")
for name, count in empty_containers[:20]:
    print(f"  {name}: {count} empty image spans")
