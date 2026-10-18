with open('site_1to1/portal.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('loginForm.addEventListener')
print("=== loginForm listener ===")
print(text[idx-50:idx+800])

idx_submit = text.find('type="submit"')
print("\n=== submit button ===")
print(text[idx_submit-50:idx_submit+300])
