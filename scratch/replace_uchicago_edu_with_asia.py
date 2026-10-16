#!/usr/bin/env python3
"""
Replace 'uchicago.asia' with 'uchicago.asia' across website text, links, and UI files.
"""

import os
import glob

TARGET_DIRS = ['site_1to1', 'site', 'scratch']
EXTENSIONS = ('.html', '.json', '.js', '.py')

total_replacements = 0
files_modified = 0

for target_dir in TARGET_DIRS:
    for root, dirs, files in os.walk(target_dir):
        if '__pycache__' in root or '.git' in root:
            continue
        for f in files:
            if f.endswith(EXTENSIONS):
                filepath = os.path.join(root, f)
                try:
                    with open(filepath, 'r', encoding='utf-8', errors='ignore') as fp:
                        content = fp.read()
                    
                    if 'uchicago.asia' in content:
                        count = content.count('uchicago.asia')
                        new_content = content.replace('uchicago.asia', 'uchicago.asia')
                        with open(filepath, 'w', encoding='utf-8') as fp:
                            fp.write(new_content)
                        
                        total_replacements += count
                        files_modified += 1
                        print(f"Updated {filepath}: replaced {count} occurrences")
                except Exception as e:
                    print(f"Error processing {filepath}: {e}")

print(f"\nDone! Modified {files_modified} files with {total_replacements} total replacements of 'uchicago.asia' -> 'uchicago.asia'.")
