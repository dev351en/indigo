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
    raw_data = resp.read().decode('utf-8')
    data = json.loads(raw_data)

with open('scratch/chem_faculty_api.json', 'w', encoding='utf-8') as out:
    out.write(raw_data)

print("Type of data:", type(data))
if isinstance(data, dict):
    print("Keys:", list(data.keys()))
    for k in data.keys():
        v = data[k]
        print(f"Key {k}: type {type(v)}, len {len(v) if hasattr(v, '__len__') else 'N/A'}")
