import os, re, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('site_1to1/pages/admissions.html', 'r', encoding='utf-8') as f:
    c = f.read()

m = re.findall(r'<div class="EduBrandBar_navList[^"]*".*?</ul>\s*</div>', c, re.DOTALL)
print(f'Total BrandBar nav lists in admissions.html: {len(m)}')
print("Item 0:")
print(m[0])
