import re

with open('site_1to1/pages/admissions.html', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.findall(r'https?://[^"\'>\s]+media[^"\'>\s]+', text)
print("Found matches in admissions.html:", len(m))
for x in m:
    print(" ", x)
