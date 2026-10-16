import urllib.request
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
}

url = "https://chemistry.uchicago.asia/phd-program"
req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req, context=ctx, timeout=15) as resp:
    html = resp.read().decode('utf-8', errors='ignore')

links = re.findall(r'href=["\']([^"\']+)["\']', html)
print(f"Total links on phd-program: {len(links)}")
for l in sorted(list(set(links))):
    if any(k in l.lower() for k in ['faculty', 'people', 'research', 'person']):
        print("  ", l)
