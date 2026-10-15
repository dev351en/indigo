with open('site_1to1/pages/department-of-chemistry.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.findall(r'<h[34][^>]*>(.*?)</h[34]>', text)
print("H3/H4 tags in chemistry page:")
for m in matches:
    if 'PROF' in m.upper() or 'ALEX' in m.upper():
        print(" ", m)
