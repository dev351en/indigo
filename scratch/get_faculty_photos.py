import urllib.request
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
}

url = "https://chemistry.uchicago.asia/faculty"
req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req, context=ctx, timeout=15) as resp:
    html = resp.read().decode('utf-8', errors='ignore')

# find faculty items
items = re.findall(r'<div[^>]*class="[^"]*views-row[^"]*"[^>]*>(.*?)</div>\s*</div>', html, re.DOTALL)
if not items:
    # try broader pattern
    items = re.findall(r'<div[^>]*class="[^"]*faculty[^"]*"[^>]*>(.*?)</div>', html, re.DOTALL)

print(f"Total faculty rows/blocks: {len(items)}")

# extract all img tags with alt
imgs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\'][^>]*alt=["\']([^"\']*)["\']', html)
if not imgs:
    imgs = re.findall(r'<img[^>]+alt=["\']([^"\']*)["\'][^>]*src=["\']([^"\']+)["\']', html)
    # swap to (src, alt)
    imgs = [(src, alt) for alt, src in imgs]

print(f"Total img tags found with alt: {len(imgs)}")
for src, alt in imgs[:25]:
    print(f"  Alt: {alt} -> Src: {src}")
