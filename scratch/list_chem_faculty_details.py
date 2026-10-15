import json

with open('scratch/chem_faculty_api.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

faculty_list = d['data']
print(f"Total faculty: {len(faculty_list)}")

for i, f in enumerate(faculty_list[:12]):
    print(f"\n[{i+1}] Name: {f.get('title')}")
    print(f"     Title: {f.get('field_faculty_title')}")
    print(f"     Photo: {f.get('field_faculty_photo')}")
    print(f"     Email: {f.get('field_faculty_email')}")
    print(f"     Subdisciplines: {f.get('field_faculty_subdisciplines')}")
    print(f"     URL: {f.get('view_node')}")
