import re
from html.parser import HTMLParser

with open("site_1to1/index.html", "r", encoding="utf-8") as f:
    local_html = f.read()

# Find all img src, background-image, and video tags in site_1to1/index.html
imgs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', local_html, re.I)
sources = re.findall(r'<source[^>]+src(?:set)?=["\']([^"\']+)["\']', local_html, re.I)
bg_imgs = re.findall(r'url\(["\']?([^"\')]+)["\']?\)', local_html, re.I)

print(f"site_1to1/index.html - Images count: {len(imgs)}")
for im in imgs:
    print(" IMG:", im)

print(f"\nsite_1to1/index.html - Sources count: {len(sources)}")
for s in sources:
    print(" SRC:", s)

print(f"\nsite_1to1/index.html - Background-images count: {len(bg_imgs)}")
for b in bg_imgs[:10]:
    print(" BG:", b)
