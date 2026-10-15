import urllib.request
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
}

url = "https://live-ucchem.pantheonsite.io/faculty"
req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req, context=ctx, timeout=10) as resp:
    html = resp.read().decode('utf-8', errors='ignore')

print("Page content around main:")
main_m = re.search(r'<main[^>]*>(.*?)</main>', html, re.DOTALL)
if main_m:
    print(main_m.group(0)[:2000])
else:
    print(html[:2000])
