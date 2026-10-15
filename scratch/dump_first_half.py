import json

with open("scratch/jss_state.json", "r", encoding="utf-8") as f:
    data = json.load(f)

comps = data["sitecore"]["route"]["placeholders"]["jss-main"][2]["placeholders"]["jss-single-col-wide"]

def print_clean(title, obj):
    print("=" * 60)
    print(title)
    print("=" * 60)
    print(json.dumps(obj, indent=2))

# 1: NewsFeatured
print_clean("1: NewsFeatured", comps[1]["placeholders"]["jss-section-wrap-content"][1]["fields"])

# 3: PhotoTabs (Harper)
print_clean("3: PhotoTabs Harper", comps[3]["fields"])

# 5: ImageTileGrid (Alison Whyte, Ashlyn Sparrow, etc.)
print_clean("5: ImageTileGrid Research/People", comps[5]["fields"])

# 6: CalloutTiles (Quantum, Popol Vuh)
print_clean("6: CalloutTiles Independent Thinking", comps[6]["placeholders"]["jss-section-wrap-content"][1]["fields"])

# 7: CalloutTiles (Miller-Urey, Teacher, Hong Kong)
print_clean("7: CalloutTiles Global Impact", comps[7]["placeholders"]["jss-section-wrap-content"][1]["fields"])
