import re
import json

with open("scratch/live_homepage.html", "r", encoding="utf-8") as f:
    html = f.read()

# Look for image extensions
media_urls = re.findall(r'(https?://[^"\'\s]+\.(?:png|jpe?g|webp|svg|gif|mp4))', html, re.I)
print(f"Total direct media extension matches: {len(media_urls)}")
for u in sorted(set(media_urls))[:20]:
    print(u)

# Look for /media/ or /jssmedia/
jss_media = re.findall(r'(/[^\'"]*(?:media|jssmedia)[^\'"]*)', html, re.I)
print(f"\nTotal media/jssmedia path matches: {len(jss_media)}")
for u in sorted(set(jss_media))[:20]:
    print(u)

# Look for __NEXT_DATA__ or script tags containing JSON
scripts = re.findall(r'<script[^>]*>(.*?)</script>', html, re.DOTALL)
print(f"\nTotal scripts found: {len(scripts)}")
for i, s in enumerate(scripts):
    if "media" in s.lower() or "jss" in s.lower() or "image" in s.lower():
        print(f"Script #{i} length {len(s)} contains media/image keywords")
