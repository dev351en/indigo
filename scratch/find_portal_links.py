import os, re, sys
sys.stdout.reconfigure(encoding='utf-8')

for root, dirs, files in os.walk('site_1to1'):
    for f in files:
        if f.endswith('.html'):
            p = os.path.join(root, f)
            with open(p, 'r', encoding='utf-8', errors='ignore') as fp:
                c = fp.read()
            for m in re.finditer(r'<a\s+[^>]*href=["\']([^"\']+)["\'][^>]*>(.*?)</a>', c, re.IGNORECASE | re.DOTALL):
                href = m.group(1)
                text = re.sub(r'<[^>]+>', '', m.group(2)).strip()
                if 'portal' in href.lower() or 'portal' in text.lower():
                    if 'office.com' not in href:
                        print(f'{p}: href="{href}" text="{text}"')
