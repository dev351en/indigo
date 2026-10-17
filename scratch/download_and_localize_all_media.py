import os
import re
import urllib.request
import ssl

ctx = ssl._create_unverified_context()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

site_dir = 'site_1to1'
pages_dir = os.path.join(site_dir, 'pages')
media_dir = os.path.join(site_dir, 'assets', 'subpage_media')
os.makedirs(media_dir, exist_ok=True)

img_pat = re.compile(r'<img\s+[^>]*?src=["\']([^"\']+)["\']', re.IGNORECASE)

# 1. Collect all remote URLs across all HTML files
remote_urls = {}
for root, dirs, files in os.walk(site_dir):
    for f in files:
        if f.endswith('.html'):
            filepath = os.path.join(root, f)
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as fp:
                c = fp.read()
            for src in img_pat.findall(c):
                if src.startswith(('http://', 'https://', '//')) and '${' not in src:
                    remote_urls.setdefault(src, []).append(filepath)

print(f"Total unique remote image URLs: {len(remote_urls)}")

# 2. Download each unique remote image if not present
url_to_local_file = {}
downloaded = 0
failed = 0

for src_url in remote_urls.keys():
    # Parse path and determine filename
    url_clean = src_url.split('?')[0].split('#')[0]
    base_name = os.path.basename(url_clean)
    if not base_name or '.' not in base_name:
        # Generate safe filename from path
        safe_name = re.sub(r'[^a-zA-Z0-9_.-]', '_', url_clean.split('//')[-1])[-50:]
        if not safe_name.endswith(('.jpg', '.png', '.svg', '.jpeg', '.gif')):
            safe_name += '.jpg'
        base_name = safe_name

    local_path = os.path.join(media_dir, base_name)
    
    # If already downloaded and valid
    if os.path.exists(local_path) and os.path.getsize(local_path) > 500:
        url_to_local_file[src_url] = base_name
        continue

    # Try downloading from uchicago.edu if it was uchicago.asia
    fetch_url = src_url
    if 'uchicago.asia' in src_url:
        fetch_url = src_url.replace('uchicago.asia', 'uchicago.edu')

    try:
        req = urllib.request.Request(fetch_url, headers=headers)
        with urllib.request.urlopen(req, context=ctx, timeout=8) as resp:
            data = resp.read()
            if data.startswith(b'<!doctype') or data.startswith(b'<html') or len(data) < 200:
                failed += 1
            else:
                with open(local_path, 'wb') as out_f:
                    out_f.write(data)
                downloaded += 1
                url_to_local_file[src_url] = base_name
                print(f"  [+ downloaded] {base_name} ({len(data)} bytes)")
    except Exception as e:
        failed += 1
        # If download fails, check if we have any fallback or existing asset
        if os.path.exists(local_path):
            url_to_local_file[src_url] = base_name

print(f"Download results: {downloaded} downloaded, {failed} failed, {len(url_to_local_file)} mapped.")

# 3. Replace in all HTML files
replaced_count = 0
for src_url, base_name in url_to_local_file.items():
    for filepath in remote_urls[src_url]:
        is_in_pages = 'pages' in os.path.normpath(filepath).split(os.sep)
        rel_prefix = '../assets/subpage_media/' if is_in_pages else 'assets/subpage_media/'
        local_src = rel_prefix + base_name
        
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as fp:
            content = fp.read()
        
        if src_url in content:
            new_content = content.replace(src_url, local_src)
            with open(filepath, 'w', encoding='utf-8') as fp:
                fp.write(new_content)
            replaced_count += 1

print(f"Total HTML replacements completed: {replaced_count}")
