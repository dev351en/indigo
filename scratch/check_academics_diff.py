import re

with open(r'd:\Microvirt\OBSIDIAN\uchicago_replica\raw_scraped_pages\academics.html', 'r', encoding='utf-8') as f:
    raw = f.read()

with open(r'd:\Microvirt\OBSIDIAN\uchicago_replica\site_1to1\pages\academics.html', 'r', encoding='utf-8') as f:
    site = f.read()

raw_headings = re.findall(r'<h[1-6][^>]*>(.*?)</h[1-6]>', raw)
site_headings = re.findall(r'<h[1-6][^>]*>(.*?)</h[1-6]>', site)

print("RAW HEADINGS in academics.html:")
for h in raw_headings:
    print("  ", h)

print("\nSITE HEADINGS in academics.html:")
for h in site_headings:
    print("  ", h)

# Check CalloutTiles in raw
raw_callout = re.findall(r'<div class="[^"]*CalloutTile[^"]*"[^>]*>(.*?)</div>', raw)
print(f"\nRaw CalloutTiles count: {len(raw_callout)}")
for c in raw_callout:
    print("--- RAW CALLOUT ---")
    print(c[:300])

site_callout = re.findall(r'<div class="[^"]*CalloutTile[^"]*"[^>]*>(.*?)</div>', site)
print(f"\nSite CalloutTiles count: {len(site_callout)}")
for c in site_callout:
    print("--- SITE CALLOUT ---")
    print(c[:300])
