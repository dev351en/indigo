"""
Audit https://uchicago.asia for any UI, layout, asset, or styling issues.
"""

import urllib.request
import re
import ssl
from urllib.parse import urljoin

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

BASE_URL = "https://uchicago.asia"

PAGES_TO_AUDIT = [
    "/",
    "/portal",
    "/faculty",
    "/chemistry",
    "/academics",
    "/who-we-are"
]

def audit_page(path):
    url = urljoin(BASE_URL, path)
    print(f"\n--- Auditing: {url} ---")
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        res = urllib.request.urlopen(req, context=ctx, timeout=10)
        html = res.read().decode('utf-8')
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return

    # Check stylesheets
    css_links = re.findall(r'<link[^>]+href=["\']([^"\']+\.css[^"\']*)["\']', html)
    # Check scripts
    js_links = re.findall(r'<script[^>]+src=["\']([^"\']+\.js[^"\']*)["\']', html)
    # Check images
    img_links = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', html)

    print(f"  Stylesheets: {len(css_links)}, Scripts: {len(js_links)}, Images: {len(img_links)}")

    failed_assets = []
    # Test top assets
    for asset in css_links + js_links + img_links[:20]:
        asset_url = urljoin(url, asset)
        try:
            a_req = urllib.request.Request(asset_url, headers={'User-Agent': 'Mozilla/5.0'})
            a_res = urllib.request.urlopen(a_req, context=ctx, timeout=5)
            if a_res.getcode() != 200:
                failed_assets.append((asset_url, a_res.getcode()))
        except Exception as err:
            failed_assets.append((asset_url, str(err)))

    if failed_assets:
        print(f"  [ISSUES FOUND] Failed assets ({len(failed_assets)}):")
        for fa, err in failed_assets:
            print(f"    - {fa}: {err}")
    else:
        print("  [SUCCESS] All sampled assets loaded with HTTP 200!")

if __name__ == "__main__":
    for p in PAGES_TO_AUDIT:
        audit_page(p)
