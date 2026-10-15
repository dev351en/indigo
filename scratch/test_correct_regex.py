with open('site_1to1/pages/admissions.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
pattern = re.compile(r'https?://www\.uchicago\.asia/-(?:jss)?media/[^"\'\s>)]+', re.IGNORECASE)
matches = pattern.findall(text)
print(f"Matched {len(matches)} media URLs in admissions.html:")
for m in matches:
    print(" ", m)
