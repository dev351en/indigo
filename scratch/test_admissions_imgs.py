import re

with open('site_1to1/pages/admissions.html', 'r', encoding='utf-8') as f:
    text = f.read()

imgs = re.findall(r'<img[^>]+>', text)
for im in imgs:
    print(im)
