import urllib.request
import re
import json
import os

pages_to_check = [
    ("who-we-are", "https://www.uchicago.edu/who-we-are", "site_1to1/pages/who-we-are.html"),
    ("academics", "https://www.uchicago.edu/academics", "site_1to1/pages/academics.html"),
    ("research-and-scholarship", "https://www.uchicago.edu/research-and-scholarship", "site_1to1/pages/research-and-scholarship.html"),
    ("admissions", "https://www.uchicago.edu/admissions", "site_1to1/pages/admissions.html"),
    ("life-at-uchicago", "https://www.uchicago.edu/life-at-uchicago", "site_1to1/pages/life-at-uchicago.html"),
    ("medicine", "https://www.uchicago.edu/medicine", "site_1to1/pages/medicine.html"),
    ("academic-departments", "https://www.uchicago.edu/academics/academic-departments", "site_1to1/pages/academics_academic-departments.html"),
    ("schools-and-divisions", "https://www.uchicago.edu/academics/schools-and-divisions", "site_1to1/pages/academics_schools-and-divisions.html"),
    ("undergraduate-programs", "https://www.uchicago.edu/academics/undergraduate-programs", "site_1to1/pages/academics_undergraduate-programs.html"),
    ("graduate-programs", "https://www.uchicago.edu/academics/graduate-programs", "site_1to1/pages/academics_graduate-programs.html"),
    ("center", "https://www.uchicago.edu/research-and-scholarship/center", "site_1to1/pages/research-and-scholarship_center.html"),
    ("affiliated-laboratories", "https://www.uchicago.edu/research-and-scholarship/affiliated-laboratories", "site_1to1/pages/research-and-scholarship_affiliated-laboratories.html"),
    ("global-campuses", "https://www.uchicago.edu/research-and-scholarship/global-campuses-and-centers", "site_1to1/pages/research-and-scholarship_global-campuses-and-centers.html"),
    ("community-impact", "https://www.uchicago.edu/who-we-are/community-impact", "site_1to1/pages/who-we-are_community-impact.html"),
    ("global-impact", "https://www.uchicago.edu/who-we-are/global-impact", "site_1to1/pages/who-we-are_global-impact.html"),
    ("history-and-traditions", "https://www.uchicago.edu/who-we-are/history-and-traditions", "site_1to1/pages/who-we-are_history-and-traditions.html"),
    ("facts-and-figures", "https://www.uchicago.edu/who-we-are/facts-and-figures", "site_1to1/pages/who-we-are_facts-and-figures.html"),
    ("hyde-park", "https://www.uchicago.edu/life-at-uchicago/hyde-park", "site_1to1/pages/life-at-uchicago_hyde-park.html"),
    ("student-life", "https://www.uchicago.edu/life-at-uchicago/student-life", "site_1to1/pages/life-at-uchicago_student-life.html"),
    ("campus-resources", "https://www.uchicago.edu/life-at-uchicago/campus-resources", "site_1to1/pages/life-at-uchicago_campus-resources.html"),
    ("arts", "https://www.uchicago.edu/life-at-uchicago/arts", "site_1to1/pages/life-at-uchicago_arts.html"),
]

def extract_images(html_text):
    # Extracts all image sources: <img> src, and style background-image:url(...)
    imgs = set()
    # <img> src
    for src in re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', html_text):
        if not src.startswith('data:'):
            # Normalize url
            imgs.add(src)
    # background-image
    for bg in re.findall(r'url\(([^)]+)\)', html_text):
        bg = bg.strip('\'"')
        if not bg.startswith('data:'):
            imgs.add(bg)
    return imgs

results = {}

for name, url, local_rel_path in pages_to_check:
    full_local_path = os.path.join(r"d:\Microvirt\OBSIDIAN\uchicago_replica", local_rel_path)
    if not os.path.exists(full_local_path):
        results[name] = {"status": "missing_local"}
        continue

    with open(full_local_path, "r", encoding="utf-8", errors="ignore") as f:
        local_content = f.read()

    local_imgs = extract_images(local_content)

    # Fetch live
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            live_content = resp.read().decode('utf-8', errors='ignore')
        live_imgs = extract_images(live_content)
        
        # Filter out common header/footer icons if we want, but let's see differences
        # Normalize: ignore domain prefix for comparing paths
        def normalize_img(img_str):
            clean = img_str.split('?')[0].rstrip('}')
            clean = re.sub(r'^https?://www\.uchicago\.(edu|asia)', '', clean)
            clean = re.sub(r'^\.\./', '/', clean)
            return clean

        norm_local = {normalize_img(x): x for x in local_imgs}
        norm_live = {normalize_img(x): x for x in live_imgs}

        missing_in_local = set(norm_live.keys()) - set(norm_local.keys())
        extra_in_local = set(norm_local.keys()) - set(norm_live.keys())

        results[name] = {
            "status": "ok",
            "live_count": len(live_imgs),
            "local_count": len(local_imgs),
            "missing_in_local": list(missing_in_local),
            "extra_in_local": list(extra_in_local)
        }
    except Exception as e:
        results[name] = {"status": "error", "error": str(e)}

with open(r"d:\Microvirt\OBSIDIAN\uchicago_replica\scratch\image_comparison_report.json", "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2)

print("Report generated. Summary:")
for name, data in results.items():
    if data["status"] == "ok":
        print(f"[{name}] Live imgs: {data['live_count']}, Local imgs: {data['local_count']}, Missing in local: {len(data['missing_in_local'])}, Extra in local: {len(data['extra_in_local'])}")
    else:
        print(f"[{name}] {data['status']}: {data.get('error', '')}")
