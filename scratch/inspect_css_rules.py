with open("site_1to1/css/CalloutTiles.27d841b2.chunk.css", "r", encoding="utf-8") as f:
    css = f.read()

import re
rules = re.findall(r'(\.CalloutTiles_[^{]+{[^}]+})', css)
for r in rules[:10]:
    print(r)

print("\n--- ImageTileGrid CSS rules ---")
with open("site_1to1/css/ImageTileGrid.0f9ff19e.chunk.css", "r", encoding="utf-8") as f:
    css_grid = f.read()
grid_rules = re.findall(r'(\.ImageTileGrid_[^{]+{[^}]+})', css_grid)
for r in grid_rules[:10]:
    print(r)

print("\n--- PhotoTabs CSS rules ---")
with open("site_1to1/css/PhotoTabs.218bbdf9.chunk.css", "r", encoding="utf-8") as f:
    css_tabs = f.read()
tabs_rules = re.findall(r'(\.PhotoTabs_[^{]+{[^}]+})', css_tabs)
for r in tabs_rules[:10]:
    print(r)
