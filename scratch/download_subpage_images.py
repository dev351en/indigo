import os
import urllib.request
import urllib.parse
import json
import re

dest_dir = "site_1to1/assets/subpage_media"
os.makedirs(dest_dir, exist_ok=True)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

# Collect all images from the downloaded subpage jss states
subpage_jss = ["scratch/jss_who-we-are.json", "scratch/jss_research.json", "scratch/jss_academics.json", "scratch/jss_life-at-uchicago.json"]

urls = set()
for sp in subpage_jss:
    if os.path.exists(sp):
        with open(sp, "r", encoding="utf-8") as f:
            data = json.load(f)
        def find_u(o):
            if isinstance(o, dict):
                if "src" in o and isinstance(o["src"], str) and "media" in o["src"]:
                    urls.add(o["src"])
                for v in o.values():
                    find_u(v)
            elif isinstance(o, list):
                for i in o:
                    find_u(i)
        find_u(data)

print(f"Total unique images to download for subpages: {len(urls)}")

downloaded = {}
for u in sorted(urls):
    parsed = urllib.parse.urlparse(u)
    fname = os.path.basename(parsed.path)
    if not fname or not any(fname.lower().endswith(ext) for ext in ['.jpg', '.jpeg', '.png', '.svg', '.webp']):
        continue
    filepath = os.path.join(dest_dir, fname)
    if not os.path.exists(filepath):
        try:
            req = urllib.request.Request(u, headers=headers)
            with urllib.request.urlopen(req, timeout=15) as resp:
                content = resp.read()
                with open(filepath, "wb") as out:
                    out.write(content)
                downloaded[u] = f"assets/subpage_media/{fname}"
                print(f"  Downloaded {fname} ({len(content)} bytes)")
        except Exception as e:
            print(f"  Failed {u}: {e}")
    else:
        downloaded[u] = f"assets/subpage_media/{fname}"

print(f"Ready with {len(downloaded)} subpage images!")
with open("scratch/subpage_img_map.json", "w", encoding="utf-8") as f:
    json.dump(downloaded, f, indent=2)
