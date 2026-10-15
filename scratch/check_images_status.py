import os
import re

site_dir = "site_1to1/pages"
files = [f for f in os.listdir(site_dir) if f.endswith(".html")]
print(f"Total HTML files in {site_dir}: {len(files)}")

img_pattern = re.compile(r'<img[^>]+src=[\'"]([^\'"]+)[\'"]', re.IGNORECASE)
bg_pattern = re.compile(r'url\([\'"]?([^\'"\)]+)[\'"]?\)', re.IGNORECASE)

remote_urls = set()
local_paths = set()
missing_local = set()

for f in files:
    path = os.path.join(site_dir, f)
    with open(path, "r", encoding="utf-8", errors="ignore") as fp:
        html = fp.read()
    
    matches = img_pattern.findall(html) + bg_pattern.findall(html)
    for m in matches:
        if m.startswith("data:"):
            continue
        if m.startswith("http://") or m.startswith("https://"):
            remote_urls.add(m)
        else:
            clean = m.split("?")[0].split("#")[0]
            resolved = os.path.normpath(os.path.join(site_dir, clean))
            local_paths.add(clean)
            if not os.path.exists(resolved):
                missing_local.add((f, m, resolved))

print(f"Total unique remote media URLs: {len(remote_urls)}")
print(f"Total unique local media paths: {len(local_paths)}")
print(f"Total missing local paths: {len(missing_local)}")

if missing_local:
    print("\nSample missing local paths:")
    for f, m, res in list(missing_local)[:15]:
        print(f"  Page: {f} -> src: {m}")

print("\nSample remote URLs:")
for u in list(remote_urls)[:15]:
    print(f"  {u}")
