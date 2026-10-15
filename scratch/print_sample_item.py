import json

with open('scratch/chem_faculty_api.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

faculty_list = d['data']
print("Keys in first item:", list(faculty_list[0].keys()))
print("First item content:\n", json.dumps(faculty_list[0], indent=2))
print("Second item content:\n", json.dumps(faculty_list[1], indent=2))
