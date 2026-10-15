with open('site_1to1/interactive_runtime.js', 'r', encoding='utf-8') as f:
    text = f.read()

# Fix broken multiline alert
text = text.replace(
    'alert("New Bursar Security Code dispatched to devendra.dubey@iitgn.ac.in\n\nCode: 893201");',
    'alert("New Bursar Security Code dispatched to devendra.dubey@iitgn.ac.in\\n\\nCode: 893201");'
)
text = text.replace(
    'alert("New Bursar Security Code dispatched to devendra.dubey@iitgn.ac.in\r\n\r\nCode: 893201");',
    'alert("New Bursar Security Code dispatched to devendra.dubey@iitgn.ac.in\\n\\nCode: 893201");'
)

with open('site_1to1/interactive_runtime.js', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated multiline alert.")
