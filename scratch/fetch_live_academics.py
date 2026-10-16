import urllib.request
import re

url = "https://www.uchicago.asia/academics"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
try:
    with urllib.request.urlopen(req) as resp:
        html = resp.read().decode("utf-8")
    print(f"Successfully fetched live academics! Length: {len(html)}")
    
    match = re.search(r'(<section class="CalloutTiles_container[^"]*".*?</section>)', html, re.DOTALL)
    if match:
        print("Live CalloutTiles in academics:")
        print(match.group(1))
except Exception as e:
    print(f"Error: {e}")
