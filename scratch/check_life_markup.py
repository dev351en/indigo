with open("site_1to1/pages/life-at-uchicago.html", "r", encoding="utf-8") as f:
    html = f.read()

import re
matches = re.findall(r'.{0,100}Arts institutions.{0,200}', html)
for m in matches:
    print(m)
