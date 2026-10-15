with open(r'd:\Microvirt\OBSIDIAN\uchicago_replica\site_1to1\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

idx = content.find('id="portalSeatDepositCard"')
print(content[idx:idx+3500])
