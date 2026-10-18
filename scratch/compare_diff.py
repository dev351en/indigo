import os, difflib

pairs = ['offer-letter.html', 'portal.html', 'receipt.html']
for p in pairs:
    with open(os.path.join('site_1to1', p), 'r', encoding='utf-8') as f1:
        lines1 = f1.readlines()
    with open(os.path.join('site_1to1', 'pages', p), 'r', encoding='utf-8') as f2:
        lines2 = f2.readlines()
    diff = list(difflib.unified_diff(lines1, lines2, fromfile=f'root/{p}', tofile=f'pages/{p}'))
    print(f"=== Diff for {p} ===")
    for d in diff[:25]:
        print(d, end='')
    print("\n")
