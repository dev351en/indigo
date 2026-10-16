import urllib.request
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
}

url = "https://chemistry.uchicago.asia/people/faculty"
req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req, context=ctx, timeout=15) as resp:
    html = resp.read().decode('utf-8', errors='ignore')

# find faculty card blocks
cards = re.findall(r'<article[^>]*>.*?</article>', html, re.DOTALL)
print(f"Total faculty article cards found: {len(cards)}")

faculty_data = []
for c in cards:
    name_m = re.search(r'<h[234][^>]*>\s*<a[^>]*>(.*?)</a>', c, re.DOTALL)
    img_m = re.search(r'<img[^>]+src=["\']([^"\']+)["\']', c)
    if name_m and img_m:
        name = name_m.group(1).strip()
        img = img_m.group(1).strip()
        faculty_data.append((name, img))

print(f"Extracted {len(faculty_data)} faculty with photos:")
for name, img in faculty_data[:15]:
    print(f"  {name}: {img}")
