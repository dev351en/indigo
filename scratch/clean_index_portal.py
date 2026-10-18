with open('site_1to1/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx_start = text.find('<!-- Admissions Application Portal Modal -->')
idx_end = text.find('<script src="interactive_runtime.js"></script>')

if idx_start != -1 and idx_end != -1:
    new_text = text[:idx_start] + text[idx_end:]
    with open('site_1to1/index.html', 'w', encoding='utf-8') as f:
        f.write(new_text)
    print("Successfully removed applicant personal details modal from index.html!")
else:
    print("Could not find start or end index in index.html!")
