with open('site_1to1/pages/who-we-are_a2z.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx_w = text.find('id="W"')
print("Surrounding W section:")
print(text[idx_w-100:idx_w+1500])

# Also check what is after W to the end of the list container
idx_end = text.find('</section>', idx_w)
print("From W to </section>:")
print(text[idx_w:idx_end+20])
