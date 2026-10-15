import urllib.request
import ssl
import os
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
}

# Download research and lab images from live chemistry site
urls = [
    "https://chemistry.uchicago.edu/sites/default/files/styles/medium_large/public/2024-11/softmatter.jpeg",
    "https://chemistry.uchicago.edu/sites/default/files/styles/medium_large/public/2024-12/jacklab2_1_0.jpg",
    "https://chemistry.uchicago.edu/sites/default/files/styles/medium_large/public/2024-12/ombuds_1.jpg"
]

os.makedirs('site_1to1/assets/chem_images', exist_ok=True)
os.makedirs('site/assets/chem_images', exist_ok=True)

for u in urls:
    filename = os.path.basename(u.split('?')[0])
    try:
        req = urllib.request.Request(u, headers=headers)
        with urllib.request.urlopen(req, context=ctx, timeout=10) as resp:
            data = resp.read()
        p1 = os.path.join('site_1to1/assets/chem_images', filename)
        p2 = os.path.join('site/assets/chem_images', filename)
        with open(p1, 'wb') as f:
            f.write(data)
        with open(p2, 'wb') as f:
            f.write(data)
        print(f"Downloaded {filename} ({len(data)} bytes)")
    except Exception as e:
        print(f"Failed {u}: {e}")
