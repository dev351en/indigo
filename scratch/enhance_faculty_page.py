import os

faculty_path = "d:/Microvirt/OBSIDIAN/uchicago_replica/site_1to1/pages/faculty.html"

with open(faculty_path, "r", encoding="utf-8") as f:
    content = f.read()

target = '<section class="Accordion_container__2Q1zs">'

dept_faculty_section = """
<!-- Department Faculty Directories & Research Section -->
<section id="department-faculty-directories" style="background: #f4f4f4; padding: 60px 24px; border-top: 1px solid #e0e0e0; border-bottom: 1px solid #e0e0e0; font-family: 'Proxima Nova', Arial, sans-serif;">
  <div style="max-width: 1200px; margin: 0 auto;">
    <div style="margin-bottom: 36px; text-align: left;">
      <span style="font-size: 13px; font-weight: 700; text-transform: uppercase; letter-spacing: 1.5px; color: #800000; display: block; margin-bottom: 8px;">Academic Divisions & Institutes</span>
      <h2 style="font-family: 'Georgia', serif; font-size: 38px; color: #111; margin: 0 0 16px 0; font-weight: 700; line-height: 1.2;">Faculty Directories by Department</h2>
      <p style="font-size: 17px; color: #444; max-width: 860px; line-height: 1.6; margin: 0;">
        Explore faculty scholarship, laboratories, and research groups across the University of Chicago's academic departments. Filter by division or visit individual departmental faculty listings.
      </p>
    </div>

    <!-- Quick Department Cards Grid -->
    <div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(360px, 1fr)); gap: 24px; margin-bottom: 40px;">
      
      <!-- Chemistry Department Card (Featured) -->
      <div style="background: #ffffff; border: 1px solid #ddd; border-top: 4px solid #800000; border-radius: 4px; padding: 28px; box-shadow: 0 4px 12px rgba(0,0,0,0.06); display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 12px;">
            <span style="font-size: 12px; font-weight: 700; color: #800000; text-transform: uppercase; letter-spacing: 1px;">Physical Sciences Division</span>
            <span style="background: #e8f5e9; color: #2e7d32; font-size: 11px; font-weight: 700; padding: 3px 8px; border-radius: 3px;">Ph.D. Recruiting</span>
          </div>
          <h3 style="font-family: 'Georgia', serif; font-size: 24px; margin: 0 0 10px 0; color: #111;">Department of Chemistry</h3>
          <p style="font-size: 14px; color: #555; line-height: 1.5; margin-bottom: 16px;">
            Pioneering research across inorganic, organic, physical, biological, and theoretical chemistry. Home to world-class laboratories, Nobel laureates, and active doctoral mentorship.
          </p>
          <div style="background: #fafafa; border-left: 3px solid #800000; padding: 10px 14px; margin-bottom: 18px; font-size: 13px; color: #333;">
            <strong>Featured Faculty:</strong> Prof. Alex Cusumano (Graduate Advisor), Prof. Bryan Dickinson, Prof. Chuan He, Prof. Laura Gagliardi, Prof. Bozhi Tian
          </div>
        </div>
        <div style="display: flex; gap: 10px; margin-top: auto;">
          <a href="department-of-chemistry.html#faculty" style="flex: 1; text-align: center; background: #800000; color: #fff; padding: 10px 16px; font-size: 14px; font-weight: 700; text-decoration: none; border-radius: 3px; transition: background 0.2s;">View Chemistry Faculty &rarr;</a>
          <a href="department-of-chemistry.html" style="background: #eee; color: #222; padding: 10px 14px; font-size: 14px; font-weight: 600; text-decoration: none; border-radius: 3px;">Overview</a>
        </div>
      </div>

      <!-- Computer Science Card -->
      <div style="background: #ffffff; border: 1px solid #ddd; border-top: 4px solid #111; border-radius: 4px; padding: 28px; box-shadow: 0 4px 12px rgba(0,0,0,0.06); display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="margin-bottom: 12px;">
            <span style="font-size: 12px; font-weight: 700; color: #555; text-transform: uppercase; letter-spacing: 1px;">Physical Sciences Division</span>
          </div>
          <h3 style="font-family: 'Georgia', serif; font-size: 24px; margin: 0 0 10px 0; color: #111;">Department of Computer Science</h3>
          <p style="font-size: 14px; color: #555; line-height: 1.5; margin-bottom: 16px;">
            World leaders in Artificial Intelligence, Machine Learning, Systems & Networks, Quantum Computing, Security, and Human-Computer Interaction in the John Crerar Science Building.
          </p>
          <div style="background: #fafafa; border-left: 3px solid #333; padding: 10px 14px; margin-bottom: 18px; font-size: 13px; color: #333;">
            <strong>Research Areas:</strong> AI/ML, Quantum Information, Systems, Theory, Data Science & Security.
          </div>
        </div>
        <div style="display: flex; gap: 10px; margin-top: auto;">
          <a href="academics_academic-departments.html#C" style="flex: 1; text-align: center; background: #222; color: #fff; padding: 10px 16px; font-size: 14px; font-weight: 700; text-decoration: none; border-radius: 3px;">View CS Faculty &rarr;</a>
        </div>
      </div>

      <!-- Physics Department Card -->
      <div style="background: #ffffff; border: 1px solid #ddd; border-top: 4px solid #800000; border-radius: 4px; padding: 28px; box-shadow: 0 4px 12px rgba(0,0,0,0.06); display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="margin-bottom: 12px;">
            <span style="font-size: 12px; font-weight: 700; color: #800000; text-transform: uppercase; letter-spacing: 1px;">Physical Sciences Division</span>
          </div>
          <h3 style="font-family: 'Georgia', serif; font-size: 24px; margin: 0 0 10px 0; color: #111;">Department of Physics</h3>
          <p style="font-size: 14px; color: #555; line-height: 1.5; margin-bottom: 16px;">
            Continuing the legacy of Enrico Fermi, Subrahmanyan Chandrasekhar, and Albert Michelson in condensed matter, high energy physics, cosmology, and quantum matter.
          </p>
          <div style="background: #fafafa; border-left: 3px solid #800000; padding: 10px 14px; margin-bottom: 18px; font-size: 13px; color: #333;">
            <strong>Affiliated Institutes:</strong> Enrico Fermi Institute (EFI), James Franck Institute (JFI).
          </div>
        </div>
        <div style="display: flex; gap: 10px; margin-top: auto;">
          <a href="academics_academic-departments.html#P" style="flex: 1; text-align: center; background: #800000; color: #fff; padding: 10px 16px; font-size: 14px; font-weight: 700; text-decoration: none; border-radius: 3px;">View Physics Faculty &rarr;</a>
        </div>
      </div>

      <!-- Economics Department Card -->
      <div style="background: #ffffff; border: 1px solid #ddd; border-top: 4px solid #111; border-radius: 4px; padding: 28px; box-shadow: 0 4px 12px rgba(0,0,0,0.06); display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="margin-bottom: 12px;">
            <span style="font-size: 12px; font-weight: 700; color: #555; text-transform: uppercase; letter-spacing: 1px;">Social Sciences Division</span>
          </div>
          <h3 style="font-family: 'Georgia', serif; font-size: 24px; margin: 0 0 10px 0; color: #111;">Kenneth C. Griffin Economics</h3>
          <p style="font-size: 14px; color: #555; line-height: 1.5; margin-bottom: 16px;">
            Renowned worldwide for the Chicago School of Economics, producing 30+ Nobel Prize winners in Economic Sciences, foundational price theory, and empirical methodology.
          </p>
          <div style="background: #fafafa; border-left: 3px solid #333; padding: 10px 14px; margin-bottom: 18px; font-size: 13px; color: #333;">
            <strong>Affiliated Centers:</strong> Becker Friedman Institute (BFI), Center for the Economics of Human Development.
          </div>
        </div>
        <div style="display: flex; gap: 10px; margin-top: auto;">
          <a href="academics_academic-departments.html#E" style="flex: 1; text-align: center; background: #222; color: #fff; padding: 10px 16px; font-size: 14px; font-weight: 700; text-decoration: none; border-radius: 3px;">View Economics Faculty &rarr;</a>
        </div>
      </div>

      <!-- Biological Sciences & Medicine Card -->
      <div style="background: #ffffff; border: 1px solid #ddd; border-top: 4px solid #800000; border-radius: 4px; padding: 28px; box-shadow: 0 4px 12px rgba(0,0,0,0.06); display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="margin-bottom: 12px;">
            <span style="font-size: 12px; font-weight: 700; color: #800000; text-transform: uppercase; letter-spacing: 1px;">Biological Sciences & Pritzker Medicine</span>
          </div>
          <h3 style="font-family: 'Georgia', serif; font-size: 24px; margin: 0 0 10px 0; color: #111;">Biological Sciences & Medicine</h3>
          <p style="font-size: 14px; color: #555; line-height: 1.5; margin-bottom: 16px;">
            Integrating basic biological inquiry with clinical research across the Pritzker School of Medicine, Duchossois Family Institute, and UChicago Medicine Health System.
          </p>
          <div style="background: #fafafa; border-left: 3px solid #800000; padding: 10px 14px; margin-bottom: 18px; font-size: 13px; color: #333;">
            <strong>Key Units:</strong> Human Genetics, Biochemistry & Molecular Biology, Neurobiology, Immunology.
          </div>
        </div>
        <div style="display: flex; gap: 10px; margin-top: auto;">
          <a href="academics_academic-departments.html#B" style="flex: 1; text-align: center; background: #800000; color: #fff; padding: 10px 16px; font-size: 14px; font-weight: 700; text-decoration: none; border-radius: 3px;">View Bio/Med Faculty &rarr;</a>
        </div>
      </div>

      <!-- Mathematics Department Card -->
      <div style="background: #ffffff; border: 1px solid #ddd; border-top: 4px solid #111; border-radius: 4px; padding: 28px; box-shadow: 0 4px 12px rgba(0,0,0,0.06); display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="margin-bottom: 12px;">
            <span style="font-size: 12px; font-weight: 700; color: #555; text-transform: uppercase; letter-spacing: 1px;">Physical Sciences Division</span>
          </div>
          <h3 style="font-family: 'Georgia', serif; font-size: 24px; margin: 0 0 10px 0; color: #111;">Department of Mathematics</h3>
          <p style="font-size: 14px; color: #555; line-height: 1.5; margin-bottom: 16px;">
            Historic excellence in pure and applied mathematics, algebraic topology, algebraic geometry, partial differential equations, and dynamic systems in Eckhart Hall.
          </p>
          <div style="background: #fafafa; border-left: 3px solid #333; padding: 10px 14px; margin-bottom: 18px; font-size: 13px; color: #333;">
            <strong>Distinction:</strong> Home to Fields Medalists and Wolf Prize recipients.
          </div>
        </div>
        <div style="display: flex; gap: 10px; margin-top: auto;">
          <a href="academics_academic-departments.html#M" style="flex: 1; text-align: center; background: #222; color: #fff; padding: 10px 16px; font-size: 14px; font-weight: 700; text-decoration: none; border-radius: 3px;">View Math Faculty &rarr;</a>
        </div>
      </div>

    </div>

    <!-- Banner linking to all 87 Academic Departments Directory -->
    <div style="background: linear-gradient(135deg, #800000 0%, #4a0000 100%); color: #fff; border-radius: 6px; padding: 32px 36px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 20px; box-shadow: 0 6px 18px rgba(128,0,0,0.25);">
      <div style="max-width: 720px;">
        <h3 style="font-family: 'Georgia', serif; font-size: 26px; margin: 0 0 8px 0; color: #fff;">Looking for Faculty in Another Field?</h3>
        <p style="font-size: 15px; margin: 0; color: #f0e6e6; line-height: 1.5;">
          Access the complete alphabetical index of all 87 academic departments, cross-divisional committees, and professional schools with direct links to faculty, lab directories, and research programs.
        </p>
      </div>
      <div>
        <a href="academics_academic-departments.html" style="display: inline-block; background: #ffffff; color: #800000; padding: 14px 28px; font-size: 15px; font-weight: 700; text-decoration: none; border-radius: 4px; box-shadow: 0 2px 6px rgba(0,0,0,0.15); text-transform: uppercase; letter-spacing: 0.5px;">Browse All 87 Departments &rarr;</a>
      </div>
    </div>
  </div>
</section>
"""

if target in content and "id=\"department-faculty-directories\"" not in content:
    new_content = content.replace(target, dept_faculty_section + "\n" + target, 1)
    with open(faculty_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Successfully enhanced faculty.html with Department Faculty Directories section!")
else:
    print("Target not found or section already present.")
