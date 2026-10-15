with open('site_1to1/pages/department-of-chemistry.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('awuttig@uchicago.asia')
print(text[idx:idx+800])
