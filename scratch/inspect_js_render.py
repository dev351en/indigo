import re
import glob

js_files = glob.glob("site_1to1/dist/**/*.js", recursive=True) + glob.glob("site_1to1/js/*.js", recursive=True) + glob.glob("site/js/*.js", recursive=True)
print("Found JS files:", len(js_files))

for jf in js_files:
    with open(jf, "r", encoding="utf-8", errors="ignore") as f:
        c = f.read()
    if "CalloutTiles_image" in c or "ImageTileGrid" in c or "PhotoTabs" in c:
        print(f"Found in {jf}")
        # let's find snippets around CalloutTiles_image
        for m in re.finditer(r'CalloutTiles_image[^;]{0,200}', c):
            print("  CalloutTiles snippet:", m.group(0))
        for m in re.finditer(r'PhotoTabs_container[^;]{0,200}', c):
            print("  PhotoTabs snippet:", m.group(0))
