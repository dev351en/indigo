import json

with open('scratch/chem_faculty_api.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

print("Type of d:", type(d))
if isinstance(d, dict):
    print("Keys:", list(d.keys()))
    for k in d.keys():
        print(f"\n--- Key: {k} ---")
        val = d[k]
        if isinstance(val, list):
            print(f"List with {len(val)} items. First item:")
            if val:
                print(json.dumps(val[0], indent=2))
        elif isinstance(val, dict):
            print(f"Dict with keys: {list(val.keys())[:10]}")
