with open('site_1to1/pages/department-of-chemistry.html', 'r', encoding='utf-8') as f:
    text = f.read()

start_idx = text.find('id="faculty"')
end_idx = text.find('<!-- Department Facilities & Resources -->', start_idx)
if end_idx == -1:
    end_idx = text.find('</section>', start_idx)

print("Faculty section bounds:", start_idx, end_idx)
print("Content snippet:\n", text[start_idx:start_idx+600])
