import re

pages_to_check = [
    "site_1to1/pages/academics.html",
    "site_1to1/pages/who-we-are.html",
    "site_1to1/pages/research-and-scholarship.html",
    "site_1to1/pages/life-at-uchicago.html"
]

for p in pages_to_check:
    with open(p, "r", encoding="utf-8") as f:
        html = f.read()
    print(f"\n==================== {p} ====================")
    # find all CalloutTiles or similar with titles
    tiles = re.findall(r'<div class="[^"]*tile[^"]*">.*?</div>\s*</div>\s*</div>', html, re.DOTALL)
    print(f"Total tile blocks: {len(tiles)}")
    for t in tiles[:5]:
        title = re.search(r'<h[23][^>]*>(.*?)</h[23]>', t)
        t_text = title.group(1) if title else "No title"
        has_empty_span = bool(re.search(r'<span class="[^"]*image[^"]*"[^>]*>\s*</span>', t))
        has_img = bool(re.search(r'<img\s', t))
        print(f"  Tile: '{t_text}', empty_span: {has_empty_span}, has_img: {has_img}")
