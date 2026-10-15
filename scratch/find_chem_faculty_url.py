import urllib.request
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
}

url = "https://chemistry.uchicago.edu/"
req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req, context=ctx, timeout=15) as resp:
    html = resp.read().decode('utf-8', errors='ignore')

links = re.findall(r'href=["\']([^"\']+)["\']', html)
people_links = [l for l in links if 'people' in l.lower() or 'faculty' in l.lower()]
print("People/faculty links found on homepage:")
for l in sorted(list(set(people_links))):
    print("  ", l)
