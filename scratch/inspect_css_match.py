import re

path = 'site/styles.css'
pattern = re.compile(r'(?<=[a-zA-Z0-9\-_])\.edu(?=[/?#\'"<>:\s,\)]|$)')
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

for m in pattern.finditer(text):
    start = max(0, m.start() - 30)
    end = min(len(text), m.end() + 30)
    print("Match:", repr(text[start:end]))
