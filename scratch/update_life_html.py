import re
import os

life_path = "site_1to1/pages/life-at-uchicago.html"
with open(life_path, "r", encoding="utf-8") as f:
    l_html = f.read()

life_tiles = [
    ("Arts institutions and programs", "artsgraycenter.png", "Arts and Gray Center"),
    ("Athletics and recreation", "football.png", "Athletics and recreation"),
    ("Campus resources", "regenstein.png", "Regenstein Library"),
    ("Health and wellness", "wellalpalooza.png", "Health and wellness")
]

for title_kw, img_file, alt in life_tiles:
    pattern = rf'(<div class="CalloutTiles_tile__3DQir"[^>]*><div>)<span class="CalloutTiles_image__9f4H5"[^>]*>\s*</span>(</div><div class="CalloutTiles_textContainer__iLI0R"><div class="CalloutTiles_titleContainer__1PDN4"><h2 class="CalloutTiles_title__11Ltk">\s*{re.escape(title_kw)}[^<]*</h2>)'
    replacement = rf'\1<span class="CalloutTiles_image__9f4H5" style="display:block;overflow:hidden;border-radius:4px 4px 0 0;height:240px;"><img src="../assets/subpage_media/{img_file}" alt="{alt}" style="width:100%;height:100%;object-fit:cover;display:block;" /></span>\2'
    l_html, n = re.subn(pattern, replacement, l_html, count=1, flags=re.DOTALL)
    if n:
        print(f"  life-at-uchicago: Updated tile '{title_kw}' with {img_file}")
    else:
        print(f"  life-at-uchicago: Could not match tile for '{title_kw}'")

with open(life_path, "w", encoding="utf-8") as f:
    f.write(l_html)

print("Updated life-at-uchicago.html!")
