import re
import json

with open("scratch/live_homepage.html", "r", encoding="utf-8") as f:
    html = f.read()

scripts = re.findall(r'<script[^>]*>(.*?)</script>', html, re.DOTALL)
for i in [3, 4]:
    s = scripts[i]
    print(f"--- Script #{i} (len {len(s)}) ---")
    # find any media links
    urls = re.findall(r'https?://[^\s"\'\\]+|-/media/[^\s"\'\\]+', s)
    media = [u for u in urls if any(ext in u.lower() for ext in ['.jpg', '.png', '.jpeg', '.svg', '.webp', '.mp4', 'media'])]
    print(f"Found {len(media)} media references:")
    for m in set(media):
        print(" ", m)
