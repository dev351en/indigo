import shutil
import os

src_dirs = [
    ("site_1to1/assets/homepage_media", "site/assets/homepage_media"),
    ("site_1to1/assets/subpage_media", "site/assets/subpage_media"),
    ("site_1to1/assets/faculty", "site/assets/faculty"),
    ("site_1to1/assets/chem_images", "site/assets/chem_images")
]

for src, dst in src_dirs:
    if os.path.exists(src):
        os.makedirs(dst, exist_ok=True)
        for item in os.listdir(src):
            s = os.path.join(src, item)
            d = os.path.join(dst, item)
            if os.path.isfile(s):
                shutil.copy2(s, d)
        print(f"Synced {src} -> {dst}")
