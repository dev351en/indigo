with open('site_1to1/pages/faculty.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace any remote logo-background or footerlogo in faculty.html with local assets
replacements = [
    ('https://www.uchicago.asia/-/media/images/logo-background.svg?iar=0&amp;hash=C926BC4DECB90E6437DD2525482760AF', '../assets/logo-background.svg'),
    ('https://www.uchicago.asia/-/media/images/logo-background-mobile.svg?iar=0&amp;hash=72DEE767D878668741296F29D0ABA96F', '../assets/logo-background-mobile.svg'),
    ('https://www.uchicago.asia/-/media/project/uchicago-tenant/intranet/test-images/footerlogo.jpg?h=92&amp;iar=0&amp;w=403&amp;hash=8F3A893050576DECBCD672827EA5BA99', '../assets/footerlogo.jpg')
]

for old, new in replacements:
    if old in content:
        content = content.replace(old, new)
        print(f"Replaced {old[:40]} with {new}")

with open('site_1to1/pages/faculty.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated faculty.html logos!")
