import glob
import re
import urllib.request
import json

html_files = glob.glob(r'd:\Microvirt\OBSIDIAN\uchicago_replica\site_1to1\**\*.html', recursive=True)

remote_urls = set()
for hf in html_files:
    with open(hf, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    imgs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', content)
    bgs = [b.strip('\'"') for b in re.findall(r'url\(([^)]+)\)', content)]
    for m in imgs + bgs:
        if m.startswith('http://') or m.startswith('https://'):
            clean_m = m.rstrip('}')
            remote_urls.add(clean_m)

print(f"Total distinct remote image URLs: {len(remote_urls)}")

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

results = {}
for u in sorted(remote_urls):
    req = urllib.request.Request(u, headers=headers, method='HEAD')
    try:
        with urllib.request.urlopen(req, timeout=5) as resp:
            results[u] = resp.status
    except Exception as e:
        # try GET if HEAD is not allowed
        try:
            req_get = urllib.request.Request(u, headers=headers)
            with urllib.request.urlopen(req_get, timeout=5) as resp:
                results[u] = resp.status
        except Exception as e2:
            results[u] = str(e2)

bad = {k: v for k, v in results.items() if v != 200}
print(f"Tested {len(results)} remote URLs. Issues: {len(bad)}")
for k, v in bad.items():
    print(f"  {k} -> {v}")
