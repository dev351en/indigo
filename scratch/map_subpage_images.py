import json
import os

files = {
    "who-we-are": "scratch/jss_who-we-are.json",
    "research": "scratch/jss_research.json",
    "academics": "scratch/jss_academics.json",
    "life": "scratch/jss_life-at-uchicago.json"
}

for name, fpath in files.items():
    if not os.path.exists(fpath):
        continue
    with open(fpath, "r", encoding="utf-8") as f:
        data = json.load(f)
    print(f"\n==================== {name} ====================")
    route = data.get("sitecore", {}).get("route", {})
    pl = route.get("placeholders", {})
    for pl_k, comp_list in pl.items():
        for comp in comp_list:
            cname = comp.get("componentName")
            # look for images in fields
            def inspect_comp(c, prefix=""):
                f = c.get("fields", {})
                for k, v in f.items():
                    if isinstance(v, dict) and "value" in v and isinstance(v["value"], dict) and "src" in v["value"]:
                        print(f"  {prefix}[{c.get('componentName')}] {k}: {v['value'].get('src')}")
                    elif isinstance(v, list):
                        for item in v:
                            if isinstance(item, dict):
                                it_fields = item.get("fields", {})
                                for ik, iv in it_fields.items():
                                    if isinstance(iv, dict) and "value" in iv and isinstance(iv["value"], dict) and "src" in iv["value"]:
                                        t_title = it_fields.get("title", {}).get("value") or item.get("name")
                                        print(f"    Item '{t_title}' {ik}: {iv['value'].get('src')}")
                for sub_k, sub_list in c.get("placeholders", {}).items():
                    for sub_c in sub_list:
                        inspect_comp(sub_c, prefix=f"  {sub_k} -> ")
            inspect_comp(comp)
