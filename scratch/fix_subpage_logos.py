import os
import re

site_dir = 'site_1to1'
pages_dir = os.path.join(site_dir, 'pages')

logo_replacements = [
    (re.compile(r'https?://(?:www\.)?uchicago\.asia/-/media/images/logo-background\.svg[^"\'\s>]*', re.I), '../assets/logo-background.svg'),
    (re.compile(r'https?://(?:www\.)?uchicago\.asia/-/media/images/logo-background-mobile\.svg[^"\'\s>]*', re.I), '../assets/logo-background-mobile.svg'),
    (re.compile(r'https?://(?:www\.)?uchicago\.asia/-/media/project/uchicago-tenant/intranet/test-images/footerlogo\.jpg[^"\'\s>]*', re.I), '../assets/footerlogo.jpg'),
    (re.compile(r'https?://(?:www\.)?uchicago\.asia/-/media/images/logo-background/campus_aerial_2-min\.png[^"\'\s>]*', re.I), '../assets/homepage_media/campus_aerial_2-min.png'),
    (re.compile(r'https?://(?:www\.)?uchicago\.asia/-/media/project/uchicago-tenant/shared/phoenix\.png[^"\'\s>]*', re.I), '../assets/phoenix.png'),
]

root_logo_replacements = [
    (re.compile(r'https?://(?:www\.)?uchicago\.asia/-/media/images/logo-background\.svg[^"\'\s>]*', re.I), 'assets/logo-background.svg'),
    (re.compile(r'https?://(?:www\.)?uchicago\.asia/-/media/images/logo-background-mobile\.svg[^"\'\s>]*', re.I), 'assets/logo-background-mobile.svg'),
    (re.compile(r'https?://(?:www\.)?uchicago\.asia/-/media/project/uchicago-tenant/intranet/test-images/footerlogo\.jpg[^"\'\s>]*', re.I), 'assets/footerlogo.jpg'),
    (re.compile(r'https?://(?:www\.)?uchicago\.asia/-/media/images/logo-background/campus_aerial_2-min\.png[^"\'\s>]*', re.I), 'assets/homepage_media/campus_aerial_2-min.png'),
    (re.compile(r'https?://(?:www\.)?uchicago\.asia/-/media/project/uchicago-tenant/shared/phoenix\.png[^"\'\s>]*', re.I), 'assets/phoenix.png'),
]

total_fixed = 0
for f in os.listdir(pages_dir):
    if f.endswith('.html'):
        p = os.path.join(pages_dir, f)
        with open(p, 'r', encoding='utf-8', errors='ignore') as fp:
            content = fp.read()
        
        orig = content
        for pat, repl in logo_replacements:
            content, count = pat.subn(repl, content)
            total_fixed += count
        
        if content != orig:
            with open(p, 'w', encoding='utf-8') as fp:
                fp.write(content)

for f in os.listdir(site_dir):
    p = os.path.join(site_dir, f)
    if os.path.isfile(p) and f.endswith('.html'):
        with open(p, 'r', encoding='utf-8', errors='ignore') as fp:
            content = fp.read()
        orig = content
        for pat, repl in root_logo_replacements:
            content, count = pat.subn(repl, content)
            total_fixed += count
        if content != orig:
            with open(p, 'w', encoding='utf-8') as fp:
                fp.write(content)

print(f"Total logo URLs replaced with local assets: {total_fixed}")
