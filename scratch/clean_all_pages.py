import os
import re

site_dir = r"d:\Microvirt\OBSIDIAN\uchicago_replica\site_1to1"

# 1. Update CSS replica_1to1_enhancements.css
css_path = os.path.join(site_dir, "css", "replica_1to1_enhancements.css")
with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

# Replace green styles in CSS
css = css.replace("#f0f7f2 !important", "#fbf8f8 !important")
css = css.replace("#a3d2b2 !important", "#e0d0d0 !important")
css = css.replace("#176531 !important", "#800000 !important")
css = css.replace("#176531", "#800000")
css = css.replace("#1b873f !important", "#800000 !important")
css = css.replace("#1b873f", "#800000")
css = css.replace("#eaf5ed !important", "#f4f4f5 !important")
css = css.replace("#f4f8f5 !important", "#fdfbfb !important")
css = css.replace("#cce5d4 !important", "#e5dada !important")
css = css.replace("#274730 !important", "#444444 !important")
css = css.replace("#e6f4ea", "#fdf2f2")
css = css.replace("#ceead6", "#d9c5c5")
css = css.replace("#137333", "#800000")
css = css.replace("#2e7d32", "#800000")
css = css.replace("#0d652d", "#800000")
css = css.replace("#276738", "#444444")
css = css.replace("#e8f5e9", "#fdf2f2")

with open(css_path, "w", encoding="utf-8") as f:
    f.write(css)
print("Updated replica_1to1_enhancements.css")

# 2. Update interactive_runtime.js
js_path = os.path.join(site_dir, "interactive_runtime.js")
with open(js_path, "r", encoding="utf-8") as f:
    js = f.read()

js = js.replace("#137333", "#800000")
js = js.replace("#176531", "#800000")
js = js.replace("#ceead6", "#d9c5c5")
js = js.replace("#e6f4ea", "#fdf2f2")
js = js.replace("#2e7d32", "#800000")
js = js.replace("Nov 15, 2026", "Nov 11, 2026")
js = js.replace("November 15, 2026", "November 11, 2026")
js = js.replace("uchicago.edu", "uchicago.edu")

with open(js_path, "w", encoding="utf-8") as f:
    f.write(js)
print("Updated interactive_runtime.js")

# 3. Process all HTML and JS files in site_1to1
green_hex_replacements = [
    ("#176531", "#800000"),
    ("#137333", "#800000"),
    ("#276738", "#444444"),
    ("#0d652d", "#800000"),
    ("#2e7d32", "#800000"),
    ("#1b873f", "#800000"),
    ("#e6f4ea", "#f4f4f5"),
    ("#ceead6", "#e5e7eb"),
    ("#f0f7f2", "#fbf8f8"),
    ("#c2e2cc", "#e5e7eb"),
    ("#e8f5e9", "#fdf2f2"),
    ("stroke=\"#176531\"", "stroke=\"#800000\""),
    ("stroke=\"#137333\"", "stroke=\"#800000\""),
    ("fill=\"#176531\"", "fill=\"#800000\""),
    ("fill=\"#137333\"", "fill=\"#800000\""),
]

date_replacements = [
    ("Nov 15, 2026", "Nov 11, 2026"),
    ("November 15, 2026", "November 11, 2026"),
    ("15th November 2026", "11th November 2026"),
    ("Priority Deadline: Nov 15", "Priority Deadline: Nov 11"),
]

updated_count = 0
asia_count = 0

for root, dirs, files in os.walk(site_dir):
    for fname in files:
        if fname.endswith((".html", ".htm", ".js", ".json")):
            fpath = os.path.join(root, fname)
            try:
                with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()
                
                orig = content

                # Replace uchicago.edu -> uchicago.edu
                if "uchicago.edu" in content:
                    content = content.replace("uchicago.edu", "uchicago.edu")
                    asia_count += 1

                # Replace green hexes
                for old_val, new_val in green_hex_replacements:
                    if old_val in content:
                        content = content.replace(old_val, new_val)

                # Replace deadline dates
                for old_date, new_date in date_replacements:
                    if old_date in content:
                        content = content.replace(old_date, new_date)

                if content != orig:
                    with open(fpath, "w", encoding="utf-8") as f:
                        f.write(content)
                    updated_count += 1
            except Exception as e:
                print(f"Error processing {fpath}: {e}")

print(f"Completed! Total files updated: {updated_count}. Files with uchicago.edu replaced: {asia_count}")
