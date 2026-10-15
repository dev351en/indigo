import glob
import re
import os

html_files = glob.glob(r'd:\Microvirt\OBSIDIAN\uchicago_replica\site_1to1\**\*.html', recursive=True)
print(f"Found {len(html_files)} HTML files.")

for fpath in html_files:
    fname = os.path.basename(fpath)
    with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    modified = False

    # 1. Remove alphabet-jump-bar
    if 'alphabet-jump-bar' in content:
        content = re.sub(r'<div class="alphabet-jump-bar"[^>]*>.*?</div>\s*', '', content, flags=re.DOTALL)
        print(f"[{fname}] Removed alphabet-jump-bar")
        modified = True

    # 2. Fix malformed background-image urls with trailing } e.g. style="background-image:url(https://...jpg})"
    if re.search(r'url\([^)]+\}\)', content):
        content = re.sub(r'url\(([^)]+)\}\)', r'url(\1)', content)
        print(f"[{fname}] Fixed background-image url trailing brace")
        modified = True

    # 3. Check for any malformed url() with quotes or braces
    # e.g., url(https://...}) or url("https:...}")
    if re.search(r'url\(["\']?([^"\')]+)\}(["\']?)\)', content):
        content = re.sub(r'url\(["\']?([^"\')]+)\}(["\']?)\)', r'url(\1)', content)
        print(f"[{fname}] Fixed background-image url trailing brace (quoted)")
        modified = True

    if modified:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)

print("Finished initial cleanup pass.")
