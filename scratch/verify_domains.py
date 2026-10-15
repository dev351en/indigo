with open("site_1to1/index.html", "r", encoding="utf-8") as f:
    text = f.read()

import re

# Find any .edu domains that aren't media endpoints
matches = re.findall(r'https?://[a-zA-Z0-9.-]+\.edu(?!/-/media|/-/jssmedia)[^"\'\s>]*', text)
print(f"Non-media .edu matches in site_1to1/index.html: {len(matches)}")
for m in matches:
    print(" ", m)

# Check email addresses
email_matches = re.findall(r'[\w.-]+@[\w.-]+\.edu', text)
print(f"Email .edu matches in site_1to1/index.html: {len(email_matches)}")
for em in email_matches:
    print(" ", em)
