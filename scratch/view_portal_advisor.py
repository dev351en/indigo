with open('site_1to1/portal.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('Cusumano')
if idx != -1:
    print(text[idx-200:idx+600])
else:
    print("Cusumano not found in portal.html")
