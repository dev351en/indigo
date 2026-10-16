import os
import re

site_dir = r"d:\Microvirt\OBSIDIAN\uchicago_replica\site_1to1"

html_count = 0
modified_count = 0

for root, dirs, files in os.walk(site_dir):
    for f in files:
        if f.endswith(".html"):
            html_count += 1
            fpath = os.path.join(root, f)
            with open(fpath, "r", encoding="utf-8", errors="ignore") as fp:
                content = fp.read()

            rel_to_site = os.path.relpath(fpath, site_dir)
            is_subpage = os.path.dirname(rel_to_site) != ""

            new_content = content

            # 1. Remove kit.fontawesome.com blocking script
            kit_pattern = r'<script[^>]*src="https://kit\.fontawesome\.com/[^"]*"[^>]*></script>'
            new_content = re.sub(kit_pattern, '', new_content)

            # 2. Determine relative css path
            if is_subpage:
                fa_css = "../css/fontawesome.min.css"
                fa_font = "../webfonts/fa-solid-900.woff2"
            else:
                fa_css = "css/fontawesome.min.css"
                fa_font = "webfonts/fa-solid-900.woff2"

            # 3. Replace external cdnjs font-awesome with local fontawesome
            cdnjs_pattern = r'<link[^>]*href="https://cdnjs\.cloudflare\.com/ajax/libs/font-awesome/[^"]*"[^>]*>'
            replacement_fa = f'<link rel="preload" href="{fa_font}" as="font" type="font/woff2" crossorigin>\n  <link rel="stylesheet" href="{fa_css}">'
            new_content = re.sub(cdnjs_pattern, replacement_fa, new_content)

            # 4. If page has no fontawesome css at all but has fa icons, ensure local FA is included
            if ('<i class="fa' in new_content or 'class="EduBrandBar_searchButton' in new_content) and 'fontawesome.min.css' not in new_content:
                # Insert before </head>
                if '</head>' in new_content:
                    new_content = new_content.replace('</head>', f'  <link rel="preload" href="{fa_font}" as="font" type="font/woff2" crossorigin>\n  <link rel="stylesheet" href="{fa_css}">\n</head>')

            if new_content != content:
                with open(fpath, "w", encoding="utf-8") as fp:
                    fp.write(new_content)
                modified_count += 1

print(f"Scanned {html_count} html files, updated {modified_count} files for ultra-fast local icon rendering.")
