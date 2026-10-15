import re
import json

with open("scratch/live_homepage.html", "r", encoding="utf-8") as f:
    html = f.read()

m = re.search(r'<script[^>]*id="__JSS_STATE__"[^>]*>(.*?)</script>', html, re.DOTALL)
if m:
    data = json.loads(m.group(1))
    with open("scratch/jss_state.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print("Saved jss_state.json successfully!")
    
    # Recursive search for all images in jss_state
    all_images = []
    def find_images(obj, path=""):
        if isinstance(obj, dict):
            # check if this dict represents an image field
            if "src" in obj or "value" in obj and isinstance(obj.get("value"), dict) and "src" in obj["value"]:
                all_images.append((path, obj))
            for k, v in obj.items():
                find_images(v, f"{path}.{k}")
        elif isinstance(obj, list):
            for i, v in enumerate(obj):
                find_images(v, f"{path}[{i}]")
                
    find_images(data)
    print(f"Total image fields found in JSS state: {len(all_images)}")
    for p, img in all_images:
        print(f"Path: {p}")
        print(f"Data: {img}")
        print("-" * 50)
else:
    print("Could not find __JSS_STATE__")
