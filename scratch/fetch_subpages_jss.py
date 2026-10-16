import urllib.request
import json
import re
import os

urls = [
    ("who-we-are", "https://www.uchicago.asia/who-we-are"),
    ("research", "https://www.uchicago.asia/research-and-scholarship"),
    ("academics", "https://www.uchicago.asia/academics"),
    ("life-at-uchicago", "https://www.uchicago.asia/life-at-uchicago")
]

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

for slug, url in urls:
    print(f"Fetching {url}...")
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=15) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            m = re.search(r'<script[^>]*id="__JSS_STATE__"[^>]*>(.*?)</script>', html, re.DOTALL)
            if m:
                data = json.loads(m.group(1))
                with open(f"scratch/jss_{slug}.json", "w", encoding="utf-8") as out:
                    json.dump(data, out, indent=2)
                
                # find all media urls
                imgs = []
                def get_imgs(o):
                    if isinstance(o, dict):
                        if "src" in o and isinstance(o["src"], str) and "media" in o["src"]:
                            imgs.append(o)
                        for v in o.values():
                            get_imgs(v)
                    elif isinstance(o, list):
                        for item in o:
                            get_imgs(item)
                get_imgs(data)
                print(f"  -> Success! Found {len(imgs)} image fields.")
                for im in imgs[:5]:
                    print("    ", im.get("src"))
    except Exception as e:
        print(f"  -> Error: {e}")
