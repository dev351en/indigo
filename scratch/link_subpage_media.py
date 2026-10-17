import os
import glob
import re

site_dir = r"d:/Microvirt/OBSIDIAN/uchicago_replica/site_1to1"
subpage_media_dir = os.path.join(site_dir, "assets", "subpage_media")
local_files = {f.lower(): f for f in os.listdir(subpage_media_dir)}

html_files = glob.glob(os.path.join(site_dir, "pages", "*.html")) + glob.glob(os.path.join(site_dir, "*.html"))
print(f"Total HTML files: {len(html_files)}")
print(f"Total local subpage media files: {len(local_files)}")

# Pattern matching https://www.uchicago.asia/-/media/... or /-/media/...
media_regex = re.compile(r'(https?://(?:www\.)?uchicago\.asia)?/-/media/[^"\'\)\s]+/([^"\'\)\s\?\#]+\.(?:jpg|jpeg|png|svg|webp|gif))', re.IGNORECASE)

files_updated = 0
total_replacements = 0

for hf in html_files:
    is_subpage = "pages" in os.path.split(hf)[0]
    asset_prefix = "../assets/subpage_media/" if is_subpage else "assets/subpage_media/"
    
    with open(hf, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    def repl(m):
        global total_replacements
        full_match = m.group(0)
        filename = m.group(2)
        lower_fn = filename.lower()
        if lower_fn in local_files:
            total_replacements += 1
            actual_fn = local_files[lower_fn]
            return asset_prefix + actual_fn
        return full_match

    new_content, count = media_regex.subn(repl, content)
    if count > 0:
        with open(hf, "w", encoding="utf-8") as f:
            f.write(new_content)
        files_updated += 1

print(f"Files updated: {files_updated}, Total replacements: {total_replacements}")
