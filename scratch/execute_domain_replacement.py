import os
import re

pattern = re.compile(r'(?<=[a-zA-Z0-9\-_])\.edu(?![a-zA-Z0-9\-_])', re.IGNORECASE)

def replacer(match):
    val = match.group(0)
    if val == '.EDU':
        return '.ASIA'
    elif val == '.Edu':
        return '.Asia'
    return '.asia'

total_replacements = 0
modified_files = 0

for folder in ['site_1to1', 'site']:
    for root, dirs, files in os.walk(folder):
        for f in files:
            if f.endswith(('.html', '.js', '.json', '.css')):
                path = os.path.join(root, f)
                with open(path, 'r', encoding='utf-8', errors='ignore') as fp:
                    content = fp.read()
                
                new_content, count = pattern.subn(replacer, content)
                if count > 0:
                    with open(path, 'w', encoding='utf-8') as fp:
                        fp.write(new_content)
                    modified_files += 1
                    total_replacements += count
                    print(f"Updated {path}: {count} replacements")

print(f"\nCompleted! Modified {modified_files} files with {total_replacements} total replacements.")
