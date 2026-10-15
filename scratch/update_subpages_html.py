import re
import os

# 1. Update research-and-scholarship.html
res_path = "site_1to1/pages/research-and-scholarship.html"
if os.path.exists(res_path):
    with open(res_path, "r", encoding="utf-8") as f:
        r_html = f.read()

    research_tiles = [
        ("The doctor ushering in a new era of cancer research", "odunsi-2.jpg", "Adekunle Odunsi"),
        ("A film archivist who keeps families", "callout-saroopsingh.jpg", "Film archivist Saroop Singh"),
        ("A scientist making plastics more recyclable", "callout-sammarsden.jpg", "Sam Marsden"),
        ("An anthropologist studying Caribbean history", "ryan-cecil-jobson-tile.jpg", "Ryan Cecil Jobson"),
        ("Big Brains podcast", "wendy-freedman-as-a-guest-on-big-brains.jpg", "Wendy Freedman on Big Brains"),
        ("A history of breakthrough research", "cp1-rs-830-500.jpg", "Chicago Pile-1"),
        ("UChicago Explainer Series", "doomsday-clock-hands.jpg", "Doomsday Clock")
    ]

    for title_kw, img_file, alt in research_tiles:
        # Match the tile containing title_kw and replace its empty image span
        pattern = rf'(<div class="CalloutTiles_tile__3DQir"><div>)<span class="CalloutTiles_image__9f4H5"[^>]*>\s*</span>(</div><div class="CalloutTiles_textContainer__iLI0R"><div class="CalloutTiles_titleContainer__1PDN4"><h2 class="CalloutTiles_title__11Ltk">[^<]*{re.escape(title_kw)}[^<]*</h2>)'
        replacement = rf'\1<span class="CalloutTiles_image__9f4H5" style="display:block;overflow:hidden;border-radius:4px 4px 0 0;height:240px;"><img src="../assets/subpage_media/{img_file}" alt="{alt}" style="width:100%;height:100%;object-fit:cover;display:block;" /></span>\2'
        r_html, n = re.subn(pattern, replacement, r_html, count=1, flags=re.DOTALL)
        if n:
            print(f"  research-and-scholarship: Updated tile '{title_kw}' with {img_file}")
        else:
            print(f"  research-and-scholarship: Could not match tile for '{title_kw}'")

    with open(res_path, "w", encoding="utf-8") as f:
        f.write(r_html)
    print("Updated research-and-scholarship.html!")

# 2. Update who-we-are.html
wwa_path = "site_1to1/pages/who-we-are.html"
if os.path.exists(wwa_path):
    with open(wwa_path, "r", encoding="utf-8") as f:
        w_html = f.read()

    wwa_tiles = [
        ("Fueling discovery", "solar-wind.jpg", "Solar wind research"),
        ("Our history", "screen-shot-2021-05-21-at-103352-am.png", "UChicago history")
    ]
    for title_kw, img_file, alt in wwa_tiles:
        pattern = rf'(<div class="CalloutTiles_tile__3DQir"><div>)<span class="CalloutTiles_image__9f4H5"[^>]*>\s*</span>(</div><div class="CalloutTiles_textContainer__iLI0R"><div class="CalloutTiles_titleContainer__1PDN4"><h2 class="CalloutTiles_title__11Ltk">[^<]*{re.escape(title_kw)}[^<]*</h2>)'
        replacement = rf'\1<span class="CalloutTiles_image__9f4H5" style="display:block;overflow:hidden;border-radius:4px 4px 0 0;height:240px;"><img src="../assets/subpage_media/{img_file}" alt="{alt}" style="width:100%;height:100%;object-fit:cover;display:block;" /></span>\2'
        w_html, n = re.subn(pattern, replacement, w_html, count=1, flags=re.DOTALL)
        if n:
            print(f"  who-we-are: Updated tile '{title_kw}' with {img_file}")
        else:
            print(f"  who-we-are: Could not match tile for '{title_kw}'")

    with open(wwa_path, "w", encoding="utf-8") as f:
        f.write(w_html)
    print("Updated who-we-are.html!")

# 3. Update life-at-uchicago.html
life_path = "site_1to1/pages/life-at-uchicago.html"
if os.path.exists(life_path):
    with open(life_path, "r", encoding="utf-8") as f:
        l_html = f.read()

    life_tiles = [
        ("Arts institutions and programs", "artsgraycenter.png", "Arts and Gray Center"),
        ("Athletics and recreation", "football.png", "Athletics and recreation"),
        ("Campus resources", "regenstein.png", "Regenstein Library"),
        ("Health and wellness", "wellalpalooza.png", "Health and wellness")
    ]
    for title_kw, img_file, alt in life_tiles:
        pattern = rf'(<div class="CalloutTiles_tile__3DQir"><div>)<span class="CalloutTiles_image__9f4H5"[^>]*>\s*</span>(</div><div class="CalloutTiles_textContainer__iLI0R"><div class="CalloutTiles_titleContainer__1PDN4"><h2 class="CalloutTiles_title__11Ltk">[^<]*{re.escape(title_kw)}[^<]*</h2>)'
        replacement = rf'\1<span class="CalloutTiles_image__9f4H5" style="display:block;overflow:hidden;border-radius:4px 4px 0 0;height:240px;"><img src="../assets/subpage_media/{img_file}" alt="{alt}" style="width:100%;height:100%;object-fit:cover;display:block;" /></span>\2'
        l_html, n = re.subn(pattern, replacement, l_html, count=1, flags=re.DOTALL)
        if n:
            print(f"  life-at-uchicago: Updated tile '{title_kw}' with {img_file}")
        else:
            print(f"  life-at-uchicago: Could not match tile for '{title_kw}'")

    with open(life_path, "w", encoding="utf-8") as f:
        f.write(l_html)
    print("Updated life-at-uchicago.html!")
