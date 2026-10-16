import urllib.request
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
}

urls = [
    "https://chemistry.uchicago.asia/people/faculty",
    "https://chemistry.uchicago.asia/phd-program"
]

for url in urls:
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            imgs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', html)
            print(f"\nFetched {url}: found {len(imgs)} images")
            for img in imgs[:15]:
                print("  ", img)
    except Exception as e:
        print(f"Failed {url}: {e}")
