import urllib.request
import re

url = "https://www.uchicago.edu/academics/academic-departments"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
try:
    with urllib.request.urlopen(req) as resp:
        html = resp.read().decode("utf-8")
    print(f"Successfully fetched live page! Length: {len(html)}")
    
    match = re.search(r'(<section class="HeadlineTextBold_container[^"]*".*?</main>)', html, re.DOTALL)
    if match:
        section = match.group(1)
        print("Live Department Section snippet (first 1000 chars):")
        print(section[:1000])
        
        # Save to scratch
        with open("scratch/live_academic_departments.html", "w", encoding="utf-8") as f:
            f.write(html)
        print("Saved to scratch/live_academic_departments.html")
except Exception as e:
    print(f"Error: {e}")
