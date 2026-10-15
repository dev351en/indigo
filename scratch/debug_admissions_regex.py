with open('site_1to1/pages/admissions.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
print("Matches in admissions.html with simple pattern:")
for m in re.finditer(r'https://www\.uchicago\.asia/-(jss)?media[^\s"\'\)]+', text):
    print(m.group(0))
