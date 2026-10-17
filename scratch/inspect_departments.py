import re

content = open('site_1to1/pages/academics_academic-departments.html', 'r', encoding='utf-8').read()
pattern = r'<li class="AlphabetList_listItem__[^"]*">\s*<a href="([^"]*)"[^>]*>(.*?)</a>'
matches = re.findall(pattern, content, re.DOTALL)
print(f"Total departments found: {len(matches)}")
depts = []
for href, name in matches:
    name_clean = re.sub(r'<[^>]+>', '', name).strip()
    depts.append({"name": name_clean, "href": href})
    print(f"- {name_clean} | {href}")

import json
with open('scratch/all_academic_departments.json', 'w', encoding='utf-8') as f:
    json.dump(depts, f, indent=2)
