import re

with open('site_1to1/pages/life-at-uchicago_safety-and-security_safe-transportation.html', 'r', encoding='utf-8') as f:
    text = f.read()

print('Visit links:', re.findall(r'href="[^"]*visit[^"]*"', text))
print('PDF links:', re.findall(r'href="[^"]*\.pdf"', text))
for m in re.finditer(r'visit\.html', text):
    start = max(0, m.start() - 100)
    end = min(len(text), m.end() + 100)
    print("Match context:", text[start:end])
