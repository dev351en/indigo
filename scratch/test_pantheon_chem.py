import urllib.request
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
}

for path in ['/faculty', '/people/faculty', '/directory', '/people', '/faculty-members']:
    url = f"https://live-ucchem.pantheonsite.io{path}"
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, context=ctx, timeout=8) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            imgs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', html)
            print(f"Status for {url}: {resp.status}, HTML len: {len(html)}, Images: {len(imgs)}")
            if len(imgs) > 1:
                for img in imgs[:5]:
                    print("  ", img)
    except Exception as e:
        print(f"Failed {url}: {e}")
