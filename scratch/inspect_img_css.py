import re

with open("site_1to1/css/NewsFeatured.030ee8bf.chunk.css", "r", encoding="utf-8") as f:
    news_css = f.read()

for m in re.finditer(r'([^{]+NewsItem[^{]+{[^}]+})', news_css):
    print(m.group(0)[:120])

print("\n--- CalloutTiles image rules ---")
with open("site_1to1/css/CalloutTiles.27d841b2.chunk.css", "r", encoding="utf-8") as f:
    co_css = f.read()

for m in re.finditer(r'([^{]+CalloutTiles_image[^{]+{[^}]+})', co_css):
    print(m.group(0))

print("\n--- ImageTileGrid image rules ---")
with open("site_1to1/css/ImageTileGrid.0f9ff19e.chunk.css", "r", encoding="utf-8") as f:
    grid_css = f.read()

for m in re.finditer(r'([^{]+ImageTileGrid_[^{]+{[^}]+})', grid_css):
    print(m.group(0)[:120])
