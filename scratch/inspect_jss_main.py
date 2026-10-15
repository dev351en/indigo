import json

with open("scratch/jss_state.json", "r", encoding="utf-8") as f:
    data = json.load(f)

route = data.get("sitecore", {}).get("route", {})
placeholders = route.get("placeholders", {})
print("Placeholders:", list(placeholders.keys()))

jss_main = placeholders.get("jss-main", [])
print(f"jss-main length: {len(jss_main)}")

for i, comp in enumerate(jss_main):
    cname = comp.get("componentName")
    print(f"\n--- Item #{i}: {cname} ---")
    sub_pl = comp.get("placeholders", {})
    if sub_pl:
        print("  Sub-placeholders:", list(sub_pl.keys()))
        for spk, sp_list in sub_pl.items():
            print(f"    {spk}: {[c.get('componentName') for c in sp_list]}")
    fields = comp.get("fields", {})
    if fields:
        print("  Fields keys:", list(fields.keys()))
