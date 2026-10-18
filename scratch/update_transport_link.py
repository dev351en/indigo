with open('site_1to1/pages/life-at-uchicago_safety-and-security_safe-transportation.html', 'r', encoding='utf-8') as f:
    text = f.read()

old_link = '<p><a href="visit.html">Transportation and Parking Guide</a></p>'
new_link = '<p><a href="../assets/documents/2024-transportation-and-parking-guide.pdf" target="_blank">Transportation and Parking Guide (Official 2024–2025 PDF)</a></p>'

if old_link in text:
    text = text.replace(old_link, new_link)
    with open('site_1to1/pages/life-at-uchicago_safety-and-security_safe-transportation.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print('Updated link in safe-transportation.html successfully!')
else:
    print('old_link not found!')
