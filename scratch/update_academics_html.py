import re

acad_path = "site_1to1/pages/academics.html"
with open(acad_path, "r", encoding="utf-8") as f:
    a_html = f.read()

acad_tiles = [
    ("Undergraduate Programs", "sisrm-research-meeting-1600.jpg", "Undergraduate Research Discussion"),
    ("Graduate Programs", "harris-students-networking.jpg", "Graduate Students Networking")
]

for title_kw, img_file, alt in acad_tiles:
    pattern = rf'(<div class="CalloutTiles_tile__3DQir"[^>]*><div>)<span class="CalloutTiles_image__9f4H5"[^>]*>\s*</span>(</div><div class="CalloutTiles_textContainer__iLI0R"><div class="CalloutTiles_titleContainer__1PDN4"><h2 class="CalloutTiles_title__11Ltk">\s*{re.escape(title_kw)}[^<]*</h2>)'
    replacement = rf'\1<span class="CalloutTiles_image__9f4H5" style="display:block;overflow:hidden;border-radius:4px 4px 0 0;height:240px;"><img src="../assets/subpage_media/{img_file}" alt="{alt}" style="width:100%;height:100%;object-fit:cover;display:block;" /></span>\2'
    a_html, n = re.subn(pattern, replacement, a_html, count=1, flags=re.DOTALL)
    if n:
        print(f"  academics: Updated tile '{title_kw}' with {img_file}")
    else:
        print(f"  academics: Could not match tile for '{title_kw}'")

with open(acad_path, "w", encoding="utf-8") as f:
    f.write(a_html)

print("Updated academics.html successfully!")
