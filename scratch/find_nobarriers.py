with open('site_1to1/pages/admissions.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('no-barriers')
if idx != -1:
    print(repr(text[idx-50:idx+100]))
else:
    print("no-barriers not found")
