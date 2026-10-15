import json
import glob
import os

jss_files = glob.glob(r'd:\Microvirt\OBSIDIAN\uchicago_replica\scratch\jss_*.json')

for jf in jss_files:
    fname = os.path.basename(jf)
    with open(jf, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    imgs = []
    def extract_imgs(o):
        if isinstance(o, dict):
            if "src" in o and isinstance(o["src"], str) and "media" in o["src"]:
                imgs.append((o.get("src"), o.get("alt", "")))
            for v in o.values():
                extract_imgs(v)
        elif isinstance(o, list):
            for item in o:
                extract_imgs(item)
    
    extract_imgs(data)
    print(f"\n=== {fname} ({len(imgs)} images) ===")
    for src, alt in imgs:
        print(f"  alt: '{alt}' | src: {src}")
