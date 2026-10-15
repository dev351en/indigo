import glob
import os
import re
import urllib.request

html_files = glob.glob(r'd:\Microvirt\OBSIDIAN\uchicago_replica\site_1to1\**\*.html', recursive=True)
print(f"Checking images across {len(html_files)} HTML files...")

broken_images = []
checked_urls = {}

for hf in html_files:
    fname = os.path.relpath(hf, r'd:\Microvirt\OBSIDIAN\uchicago_replica\site_1to1')
    dir_of_file = os.path.dirname(hf)
    with open(hf, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    imgs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', content)
    bgs = [b.strip('\'"') for b in re.findall(r'url\(([^)]+)\)', content)]

    all_media = imgs + bgs
    for m in all_media:
        if m.startswith('data:') or m.startswith('#') or not m:
            continue
        # clean query string for local check
        m_path = m.split('?')[0].rstrip('}')

        if m.startswith('http://') or m.startswith('https://'):
            # Remote url
            pass
        elif m.startswith('/'):
            # absolute to site_1to1 root
            local_full = os.path.normpath(os.path.join(r'd:\Microvirt\OBSIDIAN\uchicago_replica\site_1to1', m_path.lstrip('/\\')))
            if not os.path.exists(local_full):
                broken_images.append((fname, m, local_full))
        else:
            # relative to file directory
            local_full = os.path.normpath(os.path.join(dir_of_file, m_path))
            if not os.path.exists(local_full):
                broken_images.append((fname, m, local_full))

print(f"Total broken local image references found: {len(broken_images)}")
for item in broken_images[:20]:
    print(" ", item[0], "->", item[1], "(looked in:", item[2], ")")
