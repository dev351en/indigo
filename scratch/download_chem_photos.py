import os
import urllib.request
import ssl
import json
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
}

with open('scratch/chem_faculty_api.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

faculty_list = d['data']

os.makedirs('site_1to1/assets/faculty', exist_ok=True)
os.makedirs('site/assets/faculty', exist_ok=True)

downloaded = {}

for f in faculty_list:
    name = f.get('fullName')
    photo_url = f.get('photoUrl')
    if not photo_url:
        continue
    
    # slugify name
    slug = re.sub(r'[^a-zA-Z0-9]+', '_', name).strip('_').lower()
    ext = os.path.splitext(photo_url.split('?')[0])[1] or '.jpg'
    filename = f"{slug}{ext}"
    local_path_1 = os.path.join('site_1to1/assets/faculty', filename)
    local_path_2 = os.path.join('site/assets/faculty', filename)

    try:
        req = urllib.request.Request(photo_url, headers=headers)
        with urllib.request.urlopen(req, context=ctx, timeout=10) as resp:
            data = resp.read()
        with open(local_path_1, 'wb') as out:
            out.write(data)
        with open(local_path_2, 'wb') as out:
            out.write(data)
        downloaded[name] = filename
        print(f"Downloaded photo for {name}: {filename} ({len(data)} bytes)")
    except Exception as e:
        print(f"Failed {name} ({photo_url}): {e}")

print(f"\nSuccessfully downloaded {len(downloaded)} faculty photos!")
with open('scratch/downloaded_faculty_photos.json', 'w', encoding='utf-8') as out:
    json.dump(downloaded, out, indent=2)
