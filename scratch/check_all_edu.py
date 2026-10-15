import os
import re

edu_pattern = re.compile(r'\.edu', re.IGNORECASE)

following_chars = {}
sample_contexts = {}

for folder in ['site_1to1', 'site']:
    for root, dirs, files in os.walk(folder):
        for f in files:
            if f.endswith('.html') or f.endswith('.js') or f.endswith('.json') or f.endswith('.css'):
                path = os.path.join(root, f)
                with open(path, 'r', encoding='utf-8', errors='ignore') as fp:
                    content = fp.read()
                for m in edu_pattern.finditer(content):
                    idx = m.end()
                    char = content[idx:idx+1] if idx < len(content) else 'EOF'
                    following_chars[char] = following_chars.get(char, 0) + 1
                    if char not in sample_contexts and len(sample_contexts) < 50:
                        start = max(0, m.start() - 25)
                        end = min(len(content), m.end() + 25)
                        sample_contexts[char] = content[start:end]

print("Following characters after .edu:")
for c, count in sorted(following_chars.items(), key=lambda x: x[1], reverse=True):
    print(f"  {repr(c)}: {count} times (sample: {repr(sample_contexts.get(c, ''))})")
