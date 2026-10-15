import os

files = ["component_main.html", "full_homepage.html", "original_source.html"]
for f in files:
    if os.path.exists(f):
        size = os.path.getsize(f)
        print(f"{f}: {size} bytes")
        with open(f, "r", encoding="utf-8", errors="ignore") as fp:
            text = fp.read()
            has_photo_tabs = "PhotoTabs" in text
            has_image_grid = "ImageTileGrid" in text
            has_news = "NewsFeatured" in text
            print(f"  PhotoTabs: {has_photo_tabs}, ImageTileGrid: {has_image_grid}, NewsFeatured: {has_news}")
