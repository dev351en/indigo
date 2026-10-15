with open('site_1to1/pages/department-of-chemistry.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('PROF. ALEX CUSUMANO')
print(text[idx-200:idx+800])
