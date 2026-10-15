import os
import re

raw_dir = "raw_scraped_pages"
site_dir = "site_1to1/pages"

raw_files = set(os.listdir(raw_dir))
site_files = set(os.listdir(site_dir))

common_files = sorted(list(raw_files.intersection(site_files)))
print(f"Common files count: {len(common_files)}")

# Check key pages
key_pages = [
    "who-we-are.html",
    "academics.html",
    "academics_academic-departments.html",
    "academics_schools-and-divisions.html",
    "academics_undergraduate-programs.html",
    "academics_graduate-programs.html",
    "research-and-scholarship.html",
    "research-and-scholarship_breakthroughs.html",
    "research-and-scholarship_center.html",
    "admissions.html",
    "life-at-uchicago.html",
    "visit.html",
    "contact-us.html"
]

for kp in key_pages:
    raw_p = os.path.join(raw_dir, kp)
    site_p = os.path.join(site_dir, kp)
    
    with open(raw_p, "r", encoding="utf-8", errors="ignore") as f:
        raw_html = f.read()
    with open(site_p, "r", encoding="utf-8", errors="ignore") as f:
        site_html = f.read()
        
    print(f"\nPage: {kp}")
    print(f"  Raw size: {len(raw_html)} bytes, Site size: {len(site_html)} bytes")
    
    # Check images in raw vs site
    raw_imgs = re.findall(r'<img[^>]+src=[\'"]([^\'"]+)[\'"]|url\([\'"]?([^\'"\)]+\.(?:jpg|png|svg|webp|jpeg)[^\'"\)]*)[\'"]?\)', raw_html, re.I)
    site_imgs = re.findall(r'<img[^>]+src=[\'"]([^\'"]+)[\'"]|url\([\'"]?([^\'"\)]+\.(?:jpg|png|svg|webp|jpeg)[^\'"\)]*)[\'"]?\)', site_html, re.I)
    
    raw_img_set = set([a or b for a, b in raw_imgs if (a or b) and not (a or b).startswith("data:")])
    site_img_set = set([a or b for a, b in site_imgs if (a or b) and not (a or b).startswith("data:")])
    
    print(f"  Raw unique images: {len(raw_img_set)}")
    print(f"  Site unique images: {len(site_img_set)}")
    
    # Images in site not in raw:
    added = site_img_set - raw_img_set
    if added:
        print(f"  Images in site NOT in raw ({len(added)}):")
        for img in list(added)[:5]:
            print(f"    + {img}")
            
    # Images in raw not in site:
    removed = raw_img_set - site_img_set
    if removed:
        print(f"  Images in raw NOT in site ({len(removed)}):")
        for img in list(removed)[:5]:
            print(f"    - {img}")
