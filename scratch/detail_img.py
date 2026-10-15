import urllib.request
import re

def inspect_page(name, url, local_rel_path):
    with open(f"d:/Microvirt/OBSIDIAN/uchicago_replica/{local_rel_path}", "r", encoding="utf-8") as f:
        loc = f.read()

    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=10) as r:
        live = r.read().decode('utf-8', errors='ignore')

    loc_imgs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', loc)
    live_imgs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', live)

    loc_bg = re.findall(r'url\(([^)]+)\)', loc)
    live_bg = re.findall(r'url\(([^)]+)\)', live)

    print(f"=== {name} ===")
    print("LIVE <img>:")
    for img in live_imgs:
        print("  ", img)
    print("LOCAL <img>:")
    for img in loc_imgs:
        print("  ", img)
    print("LIVE bg:")
    for bg in live_bg:
        print("  ", bg)
    print("LOCAL bg:")
    for bg in loc_bg:
        print("  ", bg)

inspect_page("academics", "https://www.uchicago.edu/academics", "site_1to1/pages/academics.html")
