import re

with open("scratch/live_homepage.html", "r", encoding="utf-8") as f:
    html = f.read()

scripts = re.findall(r'<script([^>]*)>(.*?)</script>', html, re.DOTALL)
for i, (attrs, s) in enumerate(scripts):
    print(f"Script #{i}: attrs={attrs.strip()[:80]}, length={len(s)}, preview={s.strip()[:100]}...")
