with open('site_1to1/portal.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('class="portal-faculty-card"')
print(text[idx:idx+800])
