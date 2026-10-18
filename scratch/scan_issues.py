import os, re
from pathlib import Path

root = Path('site_1to1')
html_files = list(root.rglob('*.html'))

print(f"Scanning {len(html_files)} HTML files...")

malformed_protocols = []
old_fee_wording = []

for p in html_files:
    try:
        content = p.read_text(encoding='utf-8')
    except Exception as e:
        continue
    
    # 1. Malformed protocols
    bad_urls = re.findall(r'href=[\'"][^\'"]*http:?[/\\]+https?:?[/\\]+[^\'"]*[\'"]', content, re.I)
    if bad_urls:
        malformed_protocols.append((str(p), bad_urls))
        
    # 2. Old fee wording check
    if '90 days' in content and 'reimbursable' in content:
        # Check if it doesn't mention non-admission
        if 'non-admission' not in content and 'non admission' not in content:
            old_fee_wording.append(str(p))

print(f"Malformed protocol instances: {len(malformed_protocols)}")
for f, urls in malformed_protocols:
    print(f"  {f}: {urls}")

print(f"Old fee wording instances (without non-admission condition): {len(old_fee_wording)}")
for f in old_fee_wording:
    print(f"  {f}")
