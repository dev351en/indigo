with open('site_1to1/pages/admissions.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
pattern = re.compile(r'https?://www\.uchicago\.asia/-/jssmedia/[^"\'\s>)]+', re.IGNORECASE)
matches = pattern.findall(text)
print(f"Matched {len(matches)} jssmedia URLs:")
for m in matches:
    print(" ", m)

pattern2 = re.compile(r'https?://www\.uchicago\.asia/-/media/[^"\'\s>)]+', re.IGNORECASE)
matches2 = pattern2.findall(text)
print(f"Matched {len(matches2)} media URLs:")
for m in matches2:
    print(" ", m)
