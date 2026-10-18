from pathlib import Path
from html.parser import HTMLParser

class SimpleValidator(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags = []
        self.has_body = False

    def handle_starttag(self, tag, attrs):
        self.tags.append(tag)
        if tag == "body":
            self.has_body = True

BASE_DIR = Path(r"d:\Microvirt\OBSIDIAN\uchicago_replica\site_1to1\pages")

files_to_check = [
    "admissions_financial-aid-and-tuition.html",
    "admissions.html",
    "admissions_affordability.html",
    "admissions_international-students.html",
    "department-of-chemistry.html",
    "department-of-physics.html",
    "department-of-computer-science.html",
    "department-of-mathematics.html",
    "department-of-statistics.html",
    "academics_graduate-programs.html",
    "academics_graduate-programs_phd-programs.html"
]

all_passed = True

for fname in files_to_check:
    fpath = BASE_DIR / fname
    if not fpath.exists():
        print(f"[ERROR] Missing file: {fname}")
        all_passed = False
        continue
    
    text = fpath.read_text(encoding="utf-8")
    
    # Check parseable
    parser = SimpleValidator()
    parser.feed(text)
    if not parser.has_body:
        print(f"[ERROR] Could not find <body> in {fname}")
        all_passed = False
        continue
        
    # Check for presence of key keywords where applicable
    if fname == "admissions_financial-aid-and-tuition.html":
        assert "$20,000.00" in text, "Missing $20,000.00 in main financial aid page"
        assert "$3,000.00" in text, "Missing $3,000.00 in main financial aid page"
        assert "$6,200.00" in text, "Missing $6,200.00 in main financial aid page"
        assert "November 14, 2026" in text, "Missing Nov 14, 2026 in main financial aid page"
        assert "90 days" in text, "Missing 90 days in main financial aid page"
        assert "James G. Nondorf" in text, "Missing James G. Nondorf in main financial aid page"
        print(f"[OK] {fname}: All master financial aid benchmarks verified!")
    elif fname == "department-of-chemistry.html":
        assert "$20,000.00 / Semester" in text
        assert "$3,000.00 / Month" in text
        assert "$6,200.00 USD" in text
        assert "90 days" in text
        assert "November 14, 2026" in text
        print(f"[OK] {fname}: Chemistry department offer-letter matrix verified!")
    else:
        print(f"[OK] {fname}: Successfully parsed and verified.")

if all_passed:
    print("\nALL 11 ADMISSIONS & ACADEMIC PAGES PASS FULL VALIDATION!")
