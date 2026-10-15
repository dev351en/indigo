with open('site_1to1/pages/faculty.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('Chemistry Department Card (Featured)')
print(text[idx:idx+1500])
