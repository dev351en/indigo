import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from uchicago_complete_faculty import ALL_FACULTY
from uchicago_departments_data import DEPARTMENTS

print("Total ALL_FACULTY:", len(ALL_FACULTY))
for d in DEPARTMENTS:
    did = d['id']
    matching = [
        f for f in ALL_FACULTY 
        if f.get('deptKey') == did or did in f.get('deptKey', '') or d['name'].lower() in f.get('department', '').lower()
    ]
    print(f"- {d['name']} ({did}): {len(matching)} faculty")
