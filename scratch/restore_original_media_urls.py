import os
import re

pattern = re.compile(r'https?://(?:www\.)?uchicago\.asia(/-/(?:jss)?media/[^"\'\s>)]+)', re.IGNORECASE)
wp_pattern = re.compile(r'https://cpb-us-w2\.wpmucdn\.com/voices\.uchicago\.asia/', re.IGNORECASE)

total_media_fixed = 0
files_updated = 0

for folder in ['site_1to1', 'site']:
    for root, dirs, files in os.walk(folder):
        for f in files:
            if f.endswith(('.html', '.js', '.css', '.json')):
                path = os.path.join(root, f)
                with open(path, 'r', encoding='utf-8', errors='ignore') as fp:
                    content = fp.read()
                
                new_content, c1 = pattern.subn(r'https://www.uchicago.asia\1', content)
                new_content, c2 = wp_pattern.subn('https://cpb-us-w2.wpmucdn.com/voices.uchicago.asia/', new_content)
                
                count = c1 + c2
                if count > 0:
                    with open(path, 'w', encoding='utf-8') as fp:
                        fp.write(new_content)
                    files_updated += 1
                    total_media_fixed += count
                    print(f"Updated {path}: {count} media image URLs restored to original website")

print(f"\nCompleted! Fixed {total_media_fixed} media image URLs across {files_updated} files.")
