import re

with open("scratch/live_academic_departments.html", "r", encoding="utf-8") as f:
    live = f.read()

with open("site_1to1/pages/academics_academic-departments.html", "r", encoding="utf-8") as f:
    local = f.read()

# Compare the main section in both
live_match = re.search(r'(<section class="HeadlineTextBold_container[^"]*".*?)(?=<footer)', live, re.DOTALL)
local_match = re.search(r'(<section class="HeadlineTextBold_container[^"]*".*?)(?=<footer)', local, re.DOTALL)

if live_match and local_match:
    print("Live main section length:", len(live_match.group(1)))
    print("Local main section length:", len(local_match.group(1)))
    
    # Check letter A in live
    print("\n--- LIVE LETTER A ---")
    live_a = re.search(r'(<div><h3 id="A".*?</div>)', live, re.DOTALL)
    if live_a:
        print(live_a.group(1)[:600])
        
    print("\n--- LOCAL LETTER A ---")
    local_a = re.search(r'(<div class="AlphabetList_container" id="A".*?</ul>\s*</div>)', local, re.DOTALL)
    if local_a:
        print(local_a.group(1)[:600])
