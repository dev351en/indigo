with open('site_1to1/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('id="portalModalOverlay"')
print("=== portalModalOverlay and onwards ===")
print(text[idx-100:idx+3500])

# Also check where it ends
idx_end = text.find('</body>', idx)
print("\n=== End before </body> ===")
print(text[idx_end-1000:idx_end])
