"""
Clean up faculty photo paths in uchicago_complete_faculty.py and generate_faculty_directory.py
Ensures 100% of faculty photo references exist on disk or cleanly fallback to styled avatar.
"""

import os
import re

SITE_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "site_1to1"))
FACULTY_DIR = os.path.join(SITE_ROOT, "assets", "faculty")
SUBPAGE_DIR = os.path.join(SITE_ROOT, "assets", "subpage_media")

KNOWN_FIXES = {
    "steven_levitt.jpg": "assets/subpage_media/stevenlevitt.jpg",
    "wu_hung.jpg": "assets/subpage_media/1994-wu-hung-cropped-for-web.jpg",
    "martha_nussbaum.jpg": "assets/subpage_media/2016-martha-c-nussbaum-cropped.jpg",
    "richard_thaler.jpg": "assets/subpage_media/2017-prof-richard-thaler.jpg",
    "douglas_diamond.jpg": "assets/subpage_media/doug-diamond-crop-1600.jpg",
    "eugene_fama.jpg": "assets/subpage_media/fama-1600.jpg",
    "james_heckman.jpg": "assets/subpage_media/jamesheckman.jpg",
    "nadya_mason.jpg": "assets/subpage_media/nadya-mason.jpg",
    "wendy_freedman.jpg": "assets/subpage_media/wendy-freedman.jpg",
    "james_robinson.jpg": "assets/subpage_media/james-robinson.jpg",
}

def verify_and_fix_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Apply known replacements
    for bad_name, good_path in KNOWN_FIXES.items():
        content = content.replace(f'"assets/faculty/{bad_name}"', f'"{good_path}"')
        content = content.replace(f"'assets/faculty/{bad_name}'", f"'{good_path}'")

    # 2. Find any remaining photo paths that do not exist
    def photo_replacer(match):
        prefix = match.group(1)
        path = match.group(2)
        suffix = match.group(3)
        if not path:
            return match.group(0)
        
        full_path = os.path.join(SITE_ROOT, path)
        if not os.path.exists(full_path):
            print(f"  Photo not found: {path} -> setting to empty string for fallback avatar")
            return f'{prefix}""{suffix}'
        return match.group(0)

    content = re.sub(r'("photo":\s*)"([^"]*)"(,?|\s*)', photo_replacer, content)
    content = re.sub(r"('photo':\s*)'([^']*)'(,?|\s*)", photo_replacer, content)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Verified and cleaned {filepath}")

if __name__ == "__main__":
    verify_and_fix_file("scratch/generate_faculty_directory.py")
    verify_and_fix_file("scratch/build_complete_faculty_directory.py")
    verify_and_fix_file("scratch/uchicago_complete_faculty.py")
