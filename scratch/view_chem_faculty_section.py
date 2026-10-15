with open('site_1to1/pages/department-of-chemistry.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('id="faculty"')
print(text[idx:idx+1500])
