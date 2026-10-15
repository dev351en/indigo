page_path = 'site_1to1/pages/department-of-chemistry.html'
with open(page_path, 'r', encoding='utf-8') as f:
    content = f.read()

start_marker = '<div id="faculty"'
start_idx = content.find(start_marker)

# find where the faculty container closes after awuttig
aw_idx = content.find('awuttig@uchicago.asia')
# look for </div>\n              </div> after aw_idx
close_marker = '</div>\n              </div>'
end_idx = content.find(close_marker, aw_idx)
if end_idx != -1:
    end_idx += len(close_marker)

print("Found bounds:", start_idx, end_idx)
print("Text at end_idx - 50 to end_idx + 50:\n", repr(content[end_idx-50:end_idx+50]))
