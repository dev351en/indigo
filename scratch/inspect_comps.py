import json

with open("scratch/jss_state.json", "r", encoding="utf-8") as f:
    data = json.load(f)

comps = data["sitecore"]["route"]["placeholders"]["jss-main"][2]["placeholders"]["jss-single-col-wide"]

for i, comp in enumerate(comps):
    cname = comp.get("componentName")
    print(f"\n==================== Component {i}: {cname} ====================")
    fields = comp.get("fields", {})
    sub_pl = comp.get("placeholders", {})
    
    if sub_pl:
        print("  Sub-placeholders:")
        for k, v in sub_pl.items():
            print(f"    {k}: {[c.get('componentName') for c in v]}")
            for sc in v:
                sc_name = sc.get("componentName")
                sc_fields = sc.get("fields", {})
                print(f"      [{sc_name}] fields keys: {list(sc_fields.keys())}")
                if "items" in sc_fields:
                    print(f"        items count: {len(sc_fields['items'])}")
                if "children" in sc_fields:
                    print(f"        children count: {len(sc_fields['children'])}")
    else:
        print(f"  Fields keys: {list(fields.keys())}")
        if "items" in fields:
            print(f"    items count: {len(fields['items'])}")
        if "children" in fields:
            print(f"    children count: {len(fields['children'])}")
