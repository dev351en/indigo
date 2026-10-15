import json

with open("scratch/jss_state.json", "r", encoding="utf-8") as f:
    data = json.load(f)

comps = data["sitecore"]["route"]["placeholders"]["jss-main"][2]["placeholders"]["jss-single-col-wide"]

print("=== NEWS FEATURED ===")
print(json.dumps(comps[1]["placeholders"]["jss-section-wrap-content"][1]["fields"], indent=2))

print("\n=== IMAGE TILE GRID (PEOPLE / RESEARCH) ===")
print(json.dumps(comps[5]["fields"], indent=2))
