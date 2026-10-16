#!/usr/bin/env python3
import glob
import re

target_sub = '<li class="EduBrandBar_infoDropdownListItem__3KUhM"><a href="faculty.html" data-chevron="true" data-size="small" data-color="grey"><span class="linkText">Faculty</span></a></li>'

pattern = re.compile(r'<li class="EduBrandBar_infoDropdownListItem__3KUhM"><a href="https://intranet\.uchicago\.edu/info-for-faculty"[^>]*><span class="linkText">Faculty</span></a></li>')

updated = 0
for f in glob.glob('site_1to1/pages/*.html'):
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    if pattern.search(c):
        new_c = pattern.sub(target_sub, c)
        with open(f, 'w', encoding='utf-8') as fp:
            fp.write(new_c)
        updated += 1

print(f'Updated faculty links across {updated} subpages')
