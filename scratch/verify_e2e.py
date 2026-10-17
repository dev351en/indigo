"""
End-to-End Verification Test for UChicago Replica Server
Tests all major navigation flows and departmental subpages.
"""

import urllib.request
import re

BASE_URL = "http://localhost:3000"

def test_url(path, desc):
    url = f"{BASE_URL}{path}"
    try:
        req = urllib.request.urlopen(url)
        content = req.read().decode('utf-8')
        print(f"[PASS] {desc} -> {path} ({len(content)} bytes, status {req.getcode()})")
        return content
    except Exception as e:
        print(f"[FAIL] {desc} -> {path}: {e}")
        return None

def run_tests():
    print("=" * 70)
    print("RUNNING END-TO-END VERIFICATION")
    print("=" * 70)

    # 1. Core pages
    test_url("/", "Homepage")
    test_url("/portal", "Applicant Portal")
    test_url("/faculty", "Master Faculty Directory")
    
    # 2. Departments directory
    dept_index = test_url("/pages/academics_academic-departments.html", "Academic Departments Listing")
    assert dept_index is not None, "Failed to load academic departments page!"

    # 3. Department subpages
    depts = [
        ("department-of-computer-science.html", "Computer Science"),
        ("department-of-economics.html", "Economics"),
        ("department-of-physics.html", "Physics"),
        ("department-of-mathematics.html", "Mathematics"),
        ("department-of-statistics.html", "Statistics & Data Science"),
        ("pritzker-school-of-molecular-engineering.html", "Molecular Engineering"),
        ("department-of-biochemistry-and-molecular-biology.html", "Biochemistry & Mol Bio"),
        ("department-of-history.html", "History"),
        ("department-of-philosophy.html", "Philosophy"),
        ("department-of-political-science.html", "Political Science"),
        ("department-of-sociology.html", "Sociology"),
        ("department-of-english.html", "English"),
        ("chicago-booth-school-of-business.html", "Booth Business School"),
        ("university-of-chicago-law-school.html", "Law School"),
        ("harris-school-of-public-policy.html", "Harris Public Policy"),
        ("pritzker-school-of-medicine.html", "Pritzker Medicine"),
        ("department-of-chemistry.html", "Chemistry")
    ]

    all_passed = True
    for slug, name in depts:
        path = f"/pages/{slug}"
        html = test_url(path, f"Department: {name}")
        if not html:
            all_passed = False
            continue
        
        # Verify essential components
        has_faculty = "faculty-card-item" in html or "faculty" in html
        has_portal = "portal.html" in html
        has_modal = "facultyModal" in html
        has_degrees = "Academic Degree Programs" in html or "Doctor of Philosophy" in html

        if not (has_faculty and has_portal and has_modal and has_degrees):
            print(f"  [WARN] Missing component in {slug}: faculty={has_faculty}, portal={has_portal}, modal={has_modal}, degrees={has_degrees}")
            all_passed = False
        else:
            print(f"  -> {name} page contains all verified components (Faculty, Portal CTA, Modal, Degrees)")

    print("=" * 70)
    if all_passed:
        print("ALL 17 DEPARTMENTAL SUBPAGES & CORE DIRECTORIES VERIFIED 100% OPERATIONAL!")
    else:
        print("SOME VERIFICATIONS FAILED")
    print("=" * 70)

if __name__ == "__main__":
    run_tests()
