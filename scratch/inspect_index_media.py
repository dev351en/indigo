with open('site_1to1/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
imgs = re.findall(r'<img[^>]+>', text)
print("Img tags in index.html:")
for im in imgs:
    print(" ", im)

videos = re.findall(r'<video[^>]*>.*?</video>', text, re.DOTALL)
print("Video tags in index.html:")
for v in videos:
    print(" ", v)

bgs = re.findall(r'url\([^)]+\)', text)
print(f"Background URLs in index.html: {len(bgs)}")
for b in bgs[:10]:
    print(" ", b)
