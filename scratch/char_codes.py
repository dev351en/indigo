with open('site_1to1/pages/admissions.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('no-barriers')
substr = text[idx-40:idx]
print("Substr:", repr(substr))
print("Chars and codes:")
for c in substr:
    print(f" {repr(c)} -> {ord(c)}")
