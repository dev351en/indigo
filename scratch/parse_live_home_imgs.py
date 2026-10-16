with open('C:/Users/brode/.gemini/antigravity-ide/brain/b43cfd16-c0bf-46e0-a798-c000f4c7af2f/.system_generated/steps/1349/content.md', 'r', encoding='utf-8') as f:
    text = f.read()

import re
imgs = re.findall(r'<img[^>]+>', text)
print(f"Total img tags on live uchicago.asia: {len(imgs)}")
for im in imgs:
    print(" ", im)

# Also check for NewsItem images or background images or data-react-helmet
bgs = re.findall(r'url\([^)]+\)', text)
print(f"Background URLs: {len(bgs)}")
for b in bgs:
    print(" ", b)
