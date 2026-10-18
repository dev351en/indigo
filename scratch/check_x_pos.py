with open('site_1to1/pages/who-we-are_a2z.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx_x = text.find('id="X"')
print(text[idx_x-50:idx_x+1800])
