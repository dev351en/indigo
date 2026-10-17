"""
Update links in academics_academic-departments.html and academics_schools-and-divisions.html
to point directly to our newly generated authentic departmental subpages.
"""

import os
import re

MAPPINGS = [
    # Computer Science
    (r'https?://(?:www\.)?computerscience\.uchicago\.asia/?', 'department-of-computer-science.html'),
    (r'https?://(?:www\.)?cs\.uchicago\.asia/?', 'department-of-computer-science.html'),
    # Economics
    (r'https?://(?:www\.)?economics\.uchicago\.asia/?', 'department-of-economics.html'),
    # Physics
    (r'https?://(?:www\.)?physics\.uchicago\.asia/?', 'department-of-physics.html'),
    # Mathematics
    (r'https?://(?:www\.)?math\.uchicago\.asia/?', 'department-of-mathematics.html'),
    # Statistics
    (r'https?://(?:www\.)?stat\.uchicago\.asia/?', 'department-of-statistics.html'),
    # PME
    (r'https?://(?:www\.)?pme\.uchicago\.asia/?', 'pritzker-school-of-molecular-engineering.html'),
    # Biochemistry
    (r'https?://(?:www\.)?biochem\.uchicago\.asia/?', 'department-of-biochemistry-and-molecular-biology.html'),
    # History
    (r'https?://(?:www\.)?history\.uchicago\.asia/?', 'department-of-history.html'),
    # Philosophy
    (r'https?://(?:www\.)?philosophy\.uchicago\.asia/?', 'department-of-philosophy.html'),
    # Political Science
    (r'https?://(?:www\.)?political-science\.uchicago\.asia/?', 'department-of-political-science.html'),
    # Sociology
    (r'https?://(?:www\.)?sociology\.uchicago\.asia/?', 'department-of-sociology.html'),
    # English
    (r'https?://(?:www\.)?english\.uchicago\.asia/?', 'department-of-english.html'),
    # Law School
    (r'https?://(?:www\.)?law\.uchicago\.asia(?:/index\.shtml)?/?', 'university-of-chicago-law-school.html'),
    # Harris School
    (r'https?://(?:www\.)?harris\.uchicago\.asia/?', 'harris-school-of-public-policy.html'),
    # Pritzker Medicine
    (r'https?://(?:www\.)?pritzker\.uchicago\.asia/?', 'pritzker-school-of-medicine.html'),
    # Booth
    (r'https?://(?:www\.)?chicagobooth\.uchicago\.asia/?', 'chicago-booth-school-of-business.html'),
    (r'https?://(?:www\.)?booth\.uchicago\.asia/?', 'chicago-booth-school-of-business.html'),
    # Chemistry
    (r'https?://(?:www\.)?chemistry\.uchicago\.asia/?', 'department-of-chemistry.html'),
]

TARGET_FILES = [
    "site_1to1/pages/academics_academic-departments.html",
    "site_1to1/pages/academics_schools-and-divisions.html",
    "site_1to1/pages/academics.html",
    "site_1to1/pages/research-and-scholarship.html"
]

def update_file(filepath):
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        return

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    original_content = content
    replacements_made = 0

    for pattern, target in MAPPINGS:
        matches = len(re.findall(pattern, content, flags=re.IGNORECASE))
        if matches > 0:
            content = re.sub(pattern, target, content, flags=re.IGNORECASE)
            replacements_made += matches
            print(f"  Replaced {matches} instances of {pattern} -> {target}")

    if content != original_content:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated {filepath} with {replacements_made} replacements.")
    else:
        print(f"No changes needed for {filepath}.")

if __name__ == "__main__":
    for tf in TARGET_FILES:
        print(f"Processing: {tf}")
        update_file(tf)
