filepath = r'd:\Microvirt\OBSIDIAN\uchicago_replica\site_1to1\pages\academics_academic-departments.html'

with open(filepath, 'r', encoding='utf-8') as f:
    lines = f.readlines()

print('Initial line count:', len(lines))

# 1. Line 9 (0-indexed 8): fix background-image url trailing }
lines[8] = lines[8].replace('all-departments-hero-image.jpg}', 'all-departments-hero-image.jpg')

# 2. Line 10 (0-indexed 9) is the alphabet-jump-bar -> we delete it.
# 3. Line 11 (0-indexed 10) is the AlphabetFilter -> we keep it.
# 4. Lines 12 to 1526 (0-indexed 11 to 1525) are the departments-alphabet-directory -> delete.
# 5. Line 1527 (0-indexed 1526) starts with '</div><section class="single-col-inner">' -> strip the leading '</div>'.

filter_line = lines[10]
assert 'AlphabetFilter_alphabetFilter__p6Y6Q' in filter_line, "Expected filter line"

authentic_list_line = lines[1526]
assert authentic_list_line.startswith('</div><section class="single-col-inner">'), "Expected authentic list line"
authentic_list_line = authentic_list_line[6:] # strip leading </div>

new_lines = lines[:9] # lines 0..8 (1 to 9)
new_lines.append(filter_line) # AlphabetFilter
new_lines.append(authentic_list_line) # authentic list and rest of line
new_lines.extend(lines[1527:]) # rest of file

print('New line count:', len(new_lines))

with open(filepath, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print('Successfully cleaned academics_academic-departments.html')
