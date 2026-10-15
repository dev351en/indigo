import os
import glob

css_files = [
    "css/NewsFeatured.030ee8bf.chunk.css",
    "css/PhotoTabs.218bbdf9.chunk.css",
    "css/ImageTileGrid.0f9ff19e.chunk.css",
    "css/CalloutTiles.27d841b2.chunk.css"
]

for cf in css_files:
    full_path = os.path.join("site_1to1", cf)
    if os.path.exists(full_path):
        with open(full_path, "r", encoding="utf-8") as f:
            content = f.read()
        print(f"=== {cf} (len {len(content)}) ===")
        # Print class names found
        import re
        classes = sorted(set(re.findall(r'\.([A-Za-z0-9_-]+)', content)))
        print("Classes:", [c for c in classes if not c.startswith("fa")][:25])
