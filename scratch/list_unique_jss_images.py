import json

with open("scratch/jss_state.json", "r", encoding="utf-8") as f:
    data = json.load(f)

unique_images = {}

def extract_imgs(obj):
    if isinstance(obj, dict):
        if "value" in obj and isinstance(obj["value"], dict) and "src" in obj["value"]:
            val = obj["value"]
            src = val.get("src")
            if src and src not in unique_images:
                unique_images[src] = val
        elif "src" in obj and isinstance(obj["src"], str) and "media" in obj["src"]:
            src = obj["src"]
            if src not in unique_images:
                unique_images[src] = obj
        for v in obj.values():
            extract_imgs(v)
    elif isinstance(obj, list):
        for item in obj:
            extract_imgs(item)

extract_imgs(data)

print(f"Total unique images extracted from JSS state: {len(unique_images)}")
for src, meta in unique_images.items():
    print(f"SRC: {src}")
    print(f"ALT: {meta.get('alt')}")
    print(f"DIM: {meta.get('width')}x{meta.get('height')}")
    print("-" * 40)
