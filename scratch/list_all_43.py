import json

with open('scratch/chem_faculty_api.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

for i, f in enumerate(d['data']):
    name = f.get('fullName')
    photo = f.get('photoUrl')
    topics = ", ".join(f.get('topics') or [])
    print(f"[{i+1:2d}] {name} | Topics: {topics} | Photo: {bool(photo)}")
