import glob
import os
import re
import json

raw_dir = r"d:\Microvirt\OBSIDIAN\uchicago_replica\raw_scraped_pages"
site_dir = r"d:\Microvirt\OBSIDIAN\uchicago_replica\site_1to1"

raw_files = glob.glob(os.path.join(raw_dir, "*.html"))
print(f"Total raw HTML files: {len(raw_files)}")

def get_images(html_content):
    imgs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', html_content)
    bgs = [b.strip('\'"') for b in re.findall(r'url\(([^)]+)\)', html_content)]
    return set(imgs), set(bgs)

comparison = {}

for rpath in raw_files:
    fname = os.path.basename(rpath)
    if fname == "home.html":
        spath = os.path.join(site_dir, "index.html")
    else:
        spath = os.path.join(site_dir, "pages", fname)

    if not os.path.exists(spath):
        comparison[fname] = {"status": "missing_in_site"}
        continue

    with open(rpath, 'r', encoding='utf-8', errors='ignore') as f:
        r_content = f.read()
    with open(spath, 'r', encoding='utf-8', errors='ignore') as f:
        s_content = f.read()

    r_imgs, r_bgs = get_images(r_content)
    s_imgs, s_bgs = get_images(s_content)

    def clean_set(s):
        out = set()
        for x in s:
            x_clean = x.split('?')[0].rstrip('}')
            # normalize domain
            x_clean = re.sub(r'^https?://www\.uchicago\.(edu|asia)', '', x_clean)
            x_clean = re.sub(r'^\.\./', '/', x_clean)
            x_clean = re.sub(r'^\./', '/', x_clean)
            if not x_clean.startswith('/'):
                x_clean = '/' + x_clean
            out.add(x_clean)
        return out

    r_all = clean_set(r_imgs | r_bgs)
    s_all = clean_set(s_imgs | s_bgs)

    # Ignore standard logos / css assets
    common_ignore = {
        '/assets/logo-background.svg',
        '/assets/logo-background-mobile.svg',
        '/assets/footerlogo.jpg',
        '/-/media/images/logo-background.svg',
        '/-/media/images/logo-background-mobile.svg',
        '/-/media/project/uchicago-tenant/intranet/test-images/footerlogo.jpg',
        '/dist/intranet/favicon.ico'
    }

    r_unique = r_all - common_ignore
    s_unique = s_all - common_ignore

    missing = r_unique - s_unique
    extra = s_unique - r_unique

    comparison[fname] = {
        "status": "ok",
        "raw_count": len(r_unique),
        "site_count": len(s_unique),
        "missing_in_site": list(missing),
        "extra_in_site": list(extra)
    }

with open(r"d:\Microvirt\OBSIDIAN\uchicago_replica\scratch\raw_vs_site_images.json", "w", encoding="utf-8") as f:
    json.dump(comparison, f, indent=2)

print("\nSummary of differences with raw scraped pages:")
mismatch_count = 0
for fname, data in comparison.items():
    if data["status"] == "ok":
        if data["missing_in_site"] or data["extra_in_site"]:
            mismatch_count += 1
            print(f"[{fname}] Missing: {len(data['missing_in_site'])}, Extra: {len(data['extra_in_site'])}")
            if data["missing_in_site"]:
                print(f"   Missing: {data['missing_in_site']}")
            if data["extra_in_site"]:
                print(f"   Extra: {data['extra_in_site']}")

print(f"\nTotal pages with image differences: {mismatch_count} / {len(raw_files)}")
