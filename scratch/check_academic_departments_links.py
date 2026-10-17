import re

with open('site_1to1/pages/academics_academic-departments.html', 'r', encoding='utf-8') as f:
    content = f.read()

dept_links = re.findall(r'<a[^>]+href=["\']([^"\']+)["\'][^>]*>(.*?)</a>', content, re.DOTALL)
print('Total <a> tags:', len(dept_links))
uchicago_links = [l for l in dept_links if 'uchicago.asia' in l[0] or 'department' in l[0] or 'school' in l[0] or 'chemistry' in l[0]]
print(f'UChicago-related links ({len(uchicago_links)}):')
for href, text in uchicago_links:
    clean_text = re.sub(r'<[^>]+>', '', text).strip()
    if clean_text:
        print(f' - {clean_text}: {href}')
