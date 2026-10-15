with open("site_1to1/pages/life-at-uchicago.html", "r", encoding="utf-8") as f:
    html = f.read()

import re
idx = html.find("Arts institutions and programs")
print(html[idx-300:idx+300])
