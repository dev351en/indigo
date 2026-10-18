import re

with open('site_1to1/pages/who-we-are_a2z.html', 'r', encoding='utf-8') as f:
    text = f.read()

matches = re.findall(r'<h3[^>]*id="([^"]+)"[^>]*>([^<]+)</h3>', text)
print('Existing H3 ids in who-we-are_a2z.html:', matches)

filter_links = re.findall(r'href="(#[A-Z])"', text)
print('Filter links in who-we-are_a2z.html:', filter_links)
