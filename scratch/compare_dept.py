with open(r'd:\Microvirt\OBSIDIAN\uchicago_replica\scratch\live_academic_departments.html', 'r', encoding='utf-8') as f:
    live = f.read()

live_start = live.find('<section class="single-col-inner"><div><h3 id="A"')
live_end = live.find('</section><div class="richtext"><section><br class="t-last-br" />', live_start)
live_chunk = live[live_start:live_end]

with open(r'd:\Microvirt\OBSIDIAN\uchicago_replica\site_1to1\pages\academics_academic-departments.html', 'r', encoding='utf-8') as f:
    local_lines = f.readlines()

local_list_start = local_lines[1526].find('<section class="single-col-inner"><div><h3 id="A"')
local_list_end = local_lines[1526].find('</section><div class="richtext"><section><br class="t-last-br" />', local_list_start)
local_chunk = local_lines[1526][local_list_start:local_list_end]

import difflib
diff = list(difflib.unified_diff(live_chunk.splitlines(True), local_chunk.splitlines(True), fromfile='live', tofile='local'))
print(''.join(diff[:30]))

# Also check chemistry
for line in local_chunk.split('<li '):
    if 'Chemistry' in line:
        print('Local Chemistry:', line[:150])
for line in live_chunk.split('<li '):
    if 'Chemistry' in line:
        print('Live Chemistry:', line[:150])
