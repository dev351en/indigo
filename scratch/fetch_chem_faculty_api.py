import urllib.request
import ssl
import json

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
}

url = "https://live-ucchem.pantheonsite.io/api/faculty_index"
req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req, context=ctx, timeout=15) as resp:
    data = json.loads(resp.read().decode('utf-8'))

print(f"Total faculty records returned from API: {len(data)}")
for i, f in enumerate(data[:10]):
    print(f"\n[{i+1}] {f.get('title')} - {f.get('field_faculty_title')}")
    print(f"    Image: {f.get('field_faculty_photo') or f.get('field_image') or f.get('photo')}")
    print(f"    Email: {f.get('field_email') or f.get('mail')}")
    print(f"    Lab/URL: {f.get('view_node') or f.get('field_lab_website')}")

with open('scratch/chem_faculty_api.json', 'w', encoding='utf-8') as out:
    json.dump(data, out, indent=2)
