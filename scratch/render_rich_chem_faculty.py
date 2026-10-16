import re

page_path = 'site_1to1/pages/department-of-chemistry.html'
with open(page_path, 'r', encoding='utf-8') as f:
    content = f.read()

start_marker = '<div id="faculty"'
end_marker = '<!-- Department Facilities & Resources -->'

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx == -1 or end_idx == -1:
    print("Could not find markers:", start_idx, end_idx)
    exit(1)

new_faculty_html = """<div id="faculty" style="scroll-margin-top: 100px; margin-top: 40px; border-top: 3px solid #800000; padding-top: 30px;">
                <div style="display: flex; justify-content: space-between; align-items: baseline; flex-wrap: wrap; margin-bottom: 24px;">
                  <div>
                    <div style="font-family: 'UChicagoSansSerif-Bold', sans-serif; font-size: 13px; color: #800000; text-transform: uppercase; letter-spacing: 1px; font-weight: 700;">
                      The University of Chicago &bull; Division of the Physical Sciences
                    </div>
                    <h2 style="font-family: 'UChicagoSerif', Georgia, serif; font-size: 32px; color: #111; margin: 6px 0 10px 0; font-weight: 700;">
                      Department of Chemistry Faculty Directory
                    </h2>
                  </div>
                  <div style="font-size: 13.5px; color: #555; background: #f7f7f7; padding: 6px 14px; border-radius: 4px; border: 1px solid #e0e0e0;">
                    <i class="fa-solid fa-users" style="color: #800000; margin-right: 6px;"></i> <strong>43 Active Primary &amp; Joint Faculty</strong>
                  </div>
                </div>

                <p style="font-size: 15px; line-height: 1.6; color: #333; margin-bottom: 28px;">
                  Our faculty members are internationally renowned innovators across physical, theoretical, synthetic organic, inorganic, materials, and biological chemistry. Through deep interdisciplinary appointments across the Physical Sciences Division, Biological Sciences Division, and Pritzker School of Molecular Engineering, our labs pioneer chemical discovery and actively train doctoral scholars for Autumn 2027 matriculation.
                </p>

                <!-- Faculty Spotlight: Prof. Alex Cusumano (Graduate Advisor) -->
                <div style="background: linear-gradient(135deg, #fff9f9 0%, #ffffff 100%); border: 2px solid #800000; border-radius: 6px; padding: 24px; margin-bottom: 30px; box-shadow: 0 4px 14px rgba(128,0,0,0.08);">
                  <div style="display: flex; gap: 24px; align-items: flex-start; flex-wrap: wrap;">
                    <div style="flex-shrink: 0; text-align: center;">
                      <img src="../assets/faculty/alex_cusumano.jpg" alt="Prof. Alex Cusumano" style="width: 140px; height: 165px; object-fit: cover; border-radius: 4px; border: 2px solid #800000; box-shadow: 0 4px 10px rgba(0,0,0,0.15);" />
                      <div style="margin-top: 8px;">
                        <span style="background: #800000; color: #fff; font-size: 11px; font-weight: 700; padding: 3px 8px; border-radius: 3px; display: inline-block;">Primary Advisor</span>
                      </div>
                    </div>
                    <div style="flex: 1; min-width: 280px;">
                      <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 8px; margin-bottom: 4px;">
                        <h3 style="font-family: 'UChicagoSerif', Georgia, serif; font-size: 24px; margin: 0; color: #111;">
                          Prof. Alex (Alexander Q.) Cusumano
                        </h3>
                        <span style="background: #e8f5e9; color: #1b5e20; font-size: 12px; font-weight: 700; padding: 4px 10px; border-radius: 4px; border: 1px solid #c8e6c9;">
                          <i class="fa-solid fa-circle-check"></i> Accepting Ph.D. Students Autumn 2027
                        </span>
                      </div>
                      <div style="font-size: 14px; font-weight: 600; color: #800000; margin-bottom: 10px;">
                        Assistant Professor of Chemistry &bull; Graduate Faculty Advisor &bull; Division of the Physical Sciences
                      </div>
                      <p style="font-size: 14px; line-height: 1.6; color: #333; margin: 0 0 14px 0;">
                        Prof. Cusumano directs <strong>The Cusumano Research Group</strong>, focusing on the interface of computational chemistry, quantum mechanics, and catalysis. His laboratory leverages density functional theory (DFT), ab initio molecular dynamics, and machine-learning accelerated potential energy surface exploration to uncover reaction mechanisms and rationally design next-generation catalytic systems.
                      </p>
                      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 10px; background: #fafafa; border-radius: 4px; padding: 12px 16px; margin-bottom: 14px; font-size: 13.5px; border: 1px solid #eee;">
                        <div><i class="fa-solid fa-location-dot" style="color: #800000; width: 18px;"></i> <strong>Lab / Office:</strong> Searle Chemistry Laboratory 320</div>
                        <div><i class="fa-solid fa-envelope" style="color: #800000; width: 18px;"></i> <strong>Email:</strong> <a href="mailto:aqcusumano@uchicago.asia" style="color: #800000; font-weight: 600;">aqcusumano@uchicago.asia</a></div>
                        <div><i class="fa-solid fa-flask" style="color: #800000; width: 18px;"></i> <strong>Research Group:</strong> Cusumano Catalysis Lab</div>
                        <div><i class="fa-solid fa-calendar-check" style="color: #800000; width: 18px;"></i> <strong>Office Hours:</strong> Wed 2:00 &ndash; 4:00 PM CST</div>
                      </div>
                      <div style="display: flex; gap: 6px; flex-wrap: wrap;">
                        <span style="background: #f0f0f0; color: #333; font-size: 12px; font-weight: 600; padding: 3px 8px; border-radius: 3px;">Computational Chemistry</span>
                        <span style="background: #f0f0f0; color: #333; font-size: 12px; font-weight: 600; padding: 3px 8px; border-radius: 3px;">Density Functional Theory</span>
                        <span style="background: #f0f0f0; color: #333; font-size: 12px; font-weight: 600; padding: 3px 8px; border-radius: 3px;">Catalytic Mechanisms</span>
                        <span style="background: #f0f0f0; color: #333; font-size: 12px; font-weight: 600; padding: 3px 8px; border-radius: 3px;">Quantum Chemistry</span>
                      </div>
                    </div>
                  </div>
                </div>

                <!-- Primary Faculty Directory Grid -->
                <div style="display: grid; grid-template-columns: 1fr; gap: 20px; margin-bottom: 36px;">

                  <!-- Prof. Chuan He -->
                  <div style="background: #ffffff; border: 1px solid #ddd; border-radius: 6px; padding: 20px; box-shadow: 0 2px 6px rgba(0,0,0,0.04); display: flex; gap: 20px; flex-wrap: wrap;">
                    <img src="../assets/faculty/chuan_he.jpg" alt="Prof. Chuan He" style="width: 120px; height: 145px; object-fit: cover; border-radius: 4px; border: 1px solid #ccc; flex-shrink: 0;" />
                    <div style="flex: 1; min-width: 260px;">
                      <div style="display: flex; justify-content: space-between; align-items: baseline; flex-wrap: wrap; margin-bottom: 4px;">
                        <h4 style="font-family: 'UChicagoSerif', Georgia, serif; font-size: 20px; margin: 0; color: #111;">Prof. Chuan He</h4>
                        <span style="font-size: 12px; color: #666;"><i class="fa-solid fa-location-dot" style="color: #800000;"></i> Searle Labs 306</span>
                      </div>
                      <div style="font-size: 13.5px; font-weight: 600; color: #800000; margin-bottom: 6px;">
                        John T. Wilson Distinguished Service Professor &bull; Investigator, Howard Hughes Medical Institute (HHMI)
                      </div>
                      <p style="font-size: 13.5px; line-height: 1.5; color: #444; margin: 0 0 10px 0;">
                        Pioneered the discovery and mechanistic understanding of reversible RNA methylation in biological gene expression regulation, with fundamental impacts on cancer biology and agricultural biotechnology. MacArthur Fellow and Wolf Prize in Chemistry Laureate.
                      </p>
                      <div style="font-size: 13px; color: #555; margin-bottom: 10px;">
                        <strong>Email:</strong> <a href="mailto:chuanhe@uchicago.asia" style="color: #800000;">chuanhe@uchicago.asia</a> &bull; 
                        <strong>Lab:</strong> <a href="http://he-group.uchicago.asia" target="_blank" style="color: #800000;">The He Group</a>
                      </div>
                      <div style="display: flex; gap: 6px; flex-wrap: wrap;">
                        <span style="background: #f5f5f5; color: #444; font-size: 11.5px; padding: 2px 8px; border-radius: 3px;">Chemical Biology</span>
                        <span style="background: #f5f5f5; color: #444; font-size: 11.5px; padding: 2px 8px; border-radius: 3px;">Epitranscriptomics</span>
                        <span style="background: #f5f5f5; color: #444; font-size: 11.5px; padding: 2px 8px; border-radius: 3px;">Inorganic Chemistry</span>
                      </div>
                    </div>
                  </div>

                  <!-- Prof. Bryan Dickinson -->
                  <div style="background: #ffffff; border: 1px solid #ddd; border-radius: 6px; padding: 20px; box-shadow: 0 2px 6px rgba(0,0,0,0.04); display: flex; gap: 20px; flex-wrap: wrap;">
                    <img src="../assets/faculty/bryan_dickinson.jpg" alt="Prof. Bryan Dickinson" style="width: 120px; height: 145px; object-fit: cover; border-radius: 4px; border: 1px solid #ccc; flex-shrink: 0;" />
                    <div style="flex: 1; min-width: 260px;">
                      <div style="display: flex; justify-content: space-between; align-items: baseline; flex-wrap: wrap; margin-bottom: 4px;">
                        <h4 style="font-family: 'UChicagoSerif', Georgia, serif; font-size: 20px; margin: 0; color: #111;">Prof. Bryan C. Dickinson</h4>
                        <span style="font-size: 12px; color: #666;"><i class="fa-solid fa-location-dot" style="color: #800000;"></i> Gordon Center W308</span>
                      </div>
                      <div style="font-size: 13.5px; font-weight: 600; color: #800000; margin-bottom: 6px;">
                        Professor of Chemistry &bull; Member, Committee on Cancer Biology &bull; Pritzker Molecular Engineering
                      </div>
                      <p style="font-size: 13.5px; line-height: 1.5; color: #444; margin: 0 0 10px 0;">
                        Designs and deploys functional synthetic molecules and molecular devices to study and control dynamic biological signaling, lipid regulation, protein-protein interactions, and targeted RNA therapeutics.
                      </p>
                      <div style="font-size: 13px; color: #555; margin-bottom: 10px;">
                        <strong>Email:</strong> <a href="mailto:dickinson@uchicago.asia" style="color: #800000;">dickinson@uchicago.asia</a> &bull; 
                        <strong>Lab:</strong> <a href="http://dickinsonlab.uchicago.asia" target="_blank" style="color: #800000;">The Dickinson Laboratory</a>
                      </div>
                      <div style="display: flex; gap: 6px; flex-wrap: wrap;">
                        <span style="background: #f5f5f5; color: #444; font-size: 11.5px; padding: 2px 8px; border-radius: 3px;">Chemical Biology</span>
                        <span style="background: #f5f5f5; color: #444; font-size: 11.5px; padding: 2px 8px; border-radius: 3px;">Synthetic Virology</span>
                        <span style="background: #f5f5f5; color: #444; font-size: 11.5px; padding: 2px 8px; border-radius: 3px;">RNA Targeting</span>
                      </div>
                    </div>
                  </div>

                  <!-- Prof. Laura Gagliardi -->
                  <div style="background: #ffffff; border: 1px solid #ddd; border-radius: 6px; padding: 20px; box-shadow: 0 2px 6px rgba(0,0,0,0.04); display: flex; gap: 20px; flex-wrap: wrap;">
                    <img src="../assets/faculty/laura_gagliardi.png" alt="Prof. Laura Gagliardi" style="width: 120px; height: 145px; object-fit: cover; border-radius: 4px; border: 1px solid #ccc; flex-shrink: 0;" />
                    <div style="flex: 1; min-width: 260px;">
                      <div style="display: flex; justify-content: space-between; align-items: baseline; flex-wrap: wrap; margin-bottom: 4px;">
                        <h4 style="font-family: 'UChicagoSerif', Georgia, serif; font-size: 20px; margin: 0; color: #111;">Prof. Laura Gagliardi</h4>
                        <span style="font-size: 12px; color: #666;"><i class="fa-solid fa-location-dot" style="color: #800000;"></i> Eckhardt Center 315</span>
                      </div>
                      <div style="font-size: 13.5px; font-weight: 600; color: #800000; margin-bottom: 6px;">
                        Richard and Kathy Leventhal Professor of Chemistry &bull; Pritzker School of Molecular Engineering
                      </div>
                      <p style="font-size: 13.5px; line-height: 1.5; color: #444; margin: 0 0 10px 0;">
                        Develops advanced electronic structure theories and multi-reference quantum chemical models for complex catalytic systems, clean energy conversion, metal-organic frameworks (MOFs), and quantum information science.
                      </p>
                      <div style="font-size: 13px; color: #555; margin-bottom: 10px;">
                        <strong>Email:</strong> <a href="mailto:lgagliardi@uchicago.asia" style="color: #800000;">lgagliardi@uchicago.asia</a> &bull; 
                        <strong>Lab:</strong> Gagliardi Research Group
                      </div>
                      <div style="display: flex; gap: 6px; flex-wrap: wrap;">
                        <span style="background: #f5f5f5; color: #444; font-size: 11.5px; padding: 2px 8px; border-radius: 3px;">Theoretical Chemistry</span>
                        <span style="background: #f5f5f5; color: #444; font-size: 11.5px; padding: 2px 8px; border-radius: 3px;">Quantum Catalysis</span>
                        <span style="background: #f5f5f5; color: #444; font-size: 11.5px; padding: 2px 8px; border-radius: 3px;">Energy Materials</span>
                      </div>
                    </div>
                  </div>

                  <!-- Prof. Jack W. Szostak (Nobel Laureate) -->
                  <div style="background: #ffffff; border: 1px solid #ddd; border-left: 4px solid #b8860b; border-radius: 6px; padding: 20px; box-shadow: 0 2px 6px rgba(0,0,0,0.04); display: flex; gap: 20px; flex-wrap: wrap;">
                    <img src="../assets/faculty/jack_w_szostak.jpg" alt="Prof. Jack W. Szostak" style="width: 120px; height: 145px; object-fit: cover; border-radius: 4px; border: 1px solid #ccc; flex-shrink: 0;" />
                    <div style="flex: 1; min-width: 260px;">
                      <div style="display: flex; justify-content: space-between; align-items: baseline; flex-wrap: wrap; margin-bottom: 4px;">
                        <h4 style="font-family: 'UChicagoSerif', Georgia, serif; font-size: 20px; margin: 0; color: #111;">Prof. Jack W. Szostak &bull; Nobel Laureate</h4>
                        <span style="font-size: 12px; color: #666;"><i class="fa-solid fa-location-dot" style="color: #800000;"></i> GCIS Building</span>
                      </div>
                      <div style="font-size: 13.5px; font-weight: 600; color: #800000; margin-bottom: 6px;">
                        University Professor of Chemistry &bull; Nobel Prize in Physiology or Medicine (2009)
                      </div>
                      <p style="font-size: 13.5px; line-height: 1.5; color: #444; margin: 0 0 10px 0;">
                        Leader of the Chicago Center for the Origins of Life. Research focuses on the chemical origins of life, prebiotic chemistry, autonomous replication of RNA and model proto-cellular vesicles.
                      </p>
                      <div style="font-size: 13px; color: #555; margin-bottom: 10px;">
                        <strong>Email:</strong> <a href="mailto:szostak@uchicago.asia" style="color: #800000;">szostak@uchicago.asia</a> &bull; 
                        <strong>Lab:</strong> Szostak Origins of Life Laboratory
                      </div>
                      <div style="display: flex; gap: 6px; flex-wrap: wrap;">
                        <span style="background: #fff8e1; color: #b8860b; font-size: 11.5px; font-weight: 700; padding: 2px 8px; border-radius: 3px;">Nobel Laureate</span>
                        <span style="background: #f5f5f5; color: #444; font-size: 11.5px; padding: 2px 8px; border-radius: 3px;">Prebiotic Chemistry</span>
                        <span style="background: #f5f5f5; color: #444; font-size: 11.5px; padding: 2px 8px; border-radius: 3px;">Biophysics</span>
                      </div>
                    </div>
                  </div>

                  <!-- Prof. Bozhi Tian -->
                  <div style="background: #ffffff; border: 1px solid #ddd; border-radius: 6px; padding: 20px; box-shadow: 0 2px 6px rgba(0,0,0,0.04); display: flex; gap: 20px; flex-wrap: wrap;">
                    <img src="../assets/faculty/bozhi_tian.jpg" alt="Prof. Bozhi Tian" style="width: 120px; height: 145px; object-fit: cover; border-radius: 4px; border: 1px solid #ccc; flex-shrink: 0;" />
                    <div style="flex: 1; min-width: 260px;">
                      <div style="display: flex; justify-content: space-between; align-items: baseline; flex-wrap: wrap; margin-bottom: 4px;">
                        <h4 style="font-family: 'UChicagoSerif', Georgia, serif; font-size: 20px; margin: 0; color: #111;">Prof. Bozhi Tian</h4>
                        <span style="font-size: 12px; color: #666;"><i class="fa-solid fa-location-dot" style="color: #800000;"></i> Gordon Center W312</span>
                      </div>
                      <div style="font-size: 13.5px; font-weight: 600; color: #800000; margin-bottom: 6px;">
                        Professor of Chemistry &bull; Institute for Biophysical Dynamics
                      </div>
                      <p style="font-size: 13.5px; line-height: 1.5; color: #444; margin: 0 0 10px 0;">
                        Focuses on semiconductor biointerfaces, bioelectronic medicine, and photostimulated modulation of cellular and subcellular electrophysiology.
                      </p>
                      <div style="font-size: 13px; color: #555; margin-bottom: 10px;">
                        <strong>Email:</strong> <a href="mailto:btian@uchicago.asia" style="color: #800000;">btian@uchicago.asia</a> &bull; 
                        <strong>Lab:</strong> Tian Group
                      </div>
                      <div style="display: flex; gap: 6px; flex-wrap: wrap;">
                        <span style="background: #f5f5f5; color: #444; font-size: 11.5px; padding: 2px 8px; border-radius: 3px;">Biointerfaces</span>
                        <span style="background: #f5f5f5; color: #444; font-size: 11.5px; padding: 2px 8px; border-radius: 3px;">Materials Chemistry</span>
                        <span style="background: #f5f5f5; color: #444; font-size: 11.5px; padding: 2px 8px; border-radius: 3px;">Biophysics</span>
                      </div>
                    </div>
                  </div>

                  <!-- Prof. Gregory A. Voth -->
                  <div style="background: #ffffff; border: 1px solid #ddd; border-radius: 6px; padding: 20px; box-shadow: 0 2px 6px rgba(0,0,0,0.04); display: flex; gap: 20px; flex-wrap: wrap;">
                    <img src="../assets/faculty/gregory_a_voth.jpg" alt="Prof. Gregory A. Voth" style="width: 120px; height: 145px; object-fit: cover; border-radius: 4px; border: 1px solid #ccc; flex-shrink: 0;" />
                    <div style="flex: 1; min-width: 260px;">
                      <div style="display: flex; justify-content: space-between; align-items: baseline; flex-wrap: wrap; margin-bottom: 4px;">
                        <h4 style="font-family: 'UChicagoSerif', Georgia, serif; font-size: 20px; margin: 0; color: #111;">Prof. Gregory A. Voth</h4>
                        <span style="font-size: 12px; color: #666;"><i class="fa-solid fa-location-dot" style="color: #800000;"></i> Gordon Center W302</span>
                      </div>
                      <div style="font-size: 13.5px; font-weight: 600; color: #800000; margin-bottom: 6px;">
                        Haig P. Papazian Distinguished Service Professor of Chemistry
                      </div>
                      <p style="font-size: 13.5px; line-height: 1.5; color: #444; margin: 0 0 10px 0;">
                        Leader in multiscale computer simulation, multiscale coarse-graining, condensed matter theory, proton transport, and complex biomolecular assemblies (HIV capsids, actin filaments).
                      </p>
                      <div style="font-size: 13px; color: #555; margin-bottom: 10px;">
                        <strong>Email:</strong> <a href="mailto:gavoth@uchicago.asia" style="color: #800000;">gavoth@uchicago.asia</a> &bull; 
                        <strong>Lab:</strong> Voth Research Group
                      </div>
                      <div style="display: flex; gap: 6px; flex-wrap: wrap;">
                        <span style="background: #f5f5f5; color: #444; font-size: 11.5px; padding: 2px 8px; border-radius: 3px;">Theoretical Chemistry</span>
                        <span style="background: #f5f5f5; color: #444; font-size: 11.5px; padding: 2px 8px; border-radius: 3px;">Multiscale Simulation</span>
                        <span style="background: #f5f5f5; color: #444; font-size: 11.5px; padding: 2px 8px; border-radius: 3px;">Biophysics</span>
                      </div>
                    </div>
                  </div>

                  <!-- Prof. Jiwoong Park -->
                  <div style="background: #ffffff; border: 1px solid #ddd; border-radius: 6px; padding: 20px; box-shadow: 0 2px 6px rgba(0,0,0,0.04); display: flex; gap: 20px; flex-wrap: wrap;">
                    <img src="../assets/faculty/jiwoong_park.png" alt="Prof. Jiwoong Park" style="width: 120px; height: 145px; object-fit: cover; border-radius: 4px; border: 1px solid #ccc; flex-shrink: 0;" />
                    <div style="flex: 1; min-width: 260px;">
                      <div style="display: flex; justify-content: space-between; align-items: baseline; flex-wrap: wrap; margin-bottom: 4px;">
                        <h4 style="font-family: 'UChicagoSerif', Georgia, serif; font-size: 20px; margin: 0; color: #111;">Prof. Jiwoong Park</h4>
                        <span style="font-size: 12px; color: #666;"><i class="fa-solid fa-location-dot" style="color: #800000;"></i> Eckhardt Center 311</span>
                      </div>
                      <div style="font-size: 13.5px; font-weight: 600; color: #800000; margin-bottom: 6px;">
                        Professor and Department Chair &bull; Pritzker Molecular Engineering
                      </div>
                      <p style="font-size: 13.5px; line-height: 1.5; color: #444; margin: 0 0 10px 0;">
                        Focuses on the science and technology of atomically thin two-dimensional (2D) materials, nanoscale electronics, photonics, and wafer-scale synthesis of inorganic membranes.
                      </p>
                      <div style="font-size: 13px; color: #555; margin-bottom: 10px;">
                        <strong>Email:</strong> <a href="mailto:jwpark@uchicago.asia" style="color: #800000;">jwpark@uchicago.asia</a> &bull; 
                        <strong>Lab:</strong> The Park Group
                      </div>
                      <div style="display: flex; gap: 6px; flex-wrap: wrap;">
                        <span style="background: #f5f5f5; color: #444; font-size: 11.5px; padding: 2px 8px; border-radius: 3px;">2D Materials</span>
                        <span style="background: #f5f5f5; color: #444; font-size: 11.5px; padding: 2px 8px; border-radius: 3px;">Materials Chemistry</span>
                        <span style="background: #f5f5f5; color: #444; font-size: 11.5px; padding: 2px 8px; border-radius: 3px;">Physical Chemistry</span>
                      </div>
                    </div>
                  </div>

                  <!-- Prof. Anna Wuttig -->
                  <div style="background: #ffffff; border: 1px solid #ddd; border-radius: 6px; padding: 20px; box-shadow: 0 2px 6px rgba(0,0,0,0.04); display: flex; gap: 20px; flex-wrap: wrap;">
                    <img src="../assets/faculty/anna_wuttig.png" alt="Prof. Anna Wuttig" style="width: 120px; height: 145px; object-fit: cover; border-radius: 4px; border: 1px solid #ccc; flex-shrink: 0;" />
                    <div style="flex: 1; min-width: 260px;">
                      <div style="display: flex; justify-content: space-between; align-items: baseline; flex-wrap: wrap; margin-bottom: 4px;">
                        <h4 style="font-family: 'UChicagoSerif', Georgia, serif; font-size: 20px; margin: 0; color: #111;">Prof. Anna Wuttig</h4>
                        <span style="font-size: 12px; color: #666;"><i class="fa-solid fa-location-dot" style="color: #800000;"></i> Searle Labs 204</span>
                      </div>
                      <div style="font-size: 13.5px; font-weight: 600; color: #800000; margin-bottom: 6px;">
                        Assistant Professor of Chemistry
                      </div>
                      <p style="font-size: 13.5px; line-height: 1.5; color: #444; margin: 0 0 10px 0;">
                        Synthesizes and interrogates electrocatalytic interfaces to understand the fundamental charge-transfer reactions that govern renewable fuel synthesis and decarbonized organic transformations.
                      </p>
                      <div style="font-size: 13px; color: #555; margin-bottom: 10px;">
                        <strong>Email:</strong> <a href="mailto:awuttig@uchicago.asia" style="color: #800000;">awuttig@uchicago.asia</a> &bull; 
                        <strong>Lab:</strong> Wuttig Electrocatalysis Lab
                      </div>
                      <div style="display: flex; gap: 6px; flex-wrap: wrap;">
                        <span style="background: #f5f5f5; color: #444; font-size: 11.5px; padding: 2px 8px; border-radius: 3px;">Electrocatalysis</span>
                        <span style="background: #f5f5f5; color: #444; font-size: 11.5px; padding: 2px 8px; border-radius: 3px;">Inorganic Chemistry</span>
                        <span style="background: #f5f5f5; color: #444; font-size: 11.5px; padding: 2px 8px; border-radius: 3px;">Materials Chemistry</span>
                      </div>
                    </div>
                  </div>

                </div>

                <!-- Live Chemistry Facility & Lab Gallery -->
                <div style="background: #fafafa; border: 1px solid #e0e0e0; border-radius: 6px; padding: 24px; margin-bottom: 30px;">
                  <h3 style="font-family: 'UChicagoSerif', Georgia, serif; font-size: 22px; color: #111; margin: 0 0 8px 0;">
                    Department Facilities &amp; Research Centers
                  </h3>
                  <p style="font-size: 14px; color: #555; margin: 0 0 18px 0;">
                    Photographs from our core facilities across the Searle Chemistry Laboratory, Gordon Center for Integrative Science, and William Eckhardt Research Center:
                  </p>
                  <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 16px;">
                    <div style="background: #fff; border: 1px solid #ddd; border-radius: 4px; overflow: hidden; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
                      <img src="../assets/chem_images/softmatter.jpeg" alt="Soft Matter Facility" style="width: 100%; height: 160px; object-fit: cover;" />
                      <div style="padding: 12px;">
                        <div style="font-weight: 700; font-size: 14px; color: #111; margin-bottom: 4px;">Soft Matter Synthesis Facility</div>
                        <div style="font-size: 12.5px; color: #666; line-height: 1.4;">Advanced macromolecular characterization, rheology, and precision polymer synthesis in GCIS.</div>
                      </div>
                    </div>
                    <div style="background: #fff; border: 1px solid #ddd; border-radius: 4px; overflow: hidden; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
                      <img src="../assets/chem_images/jacklab2_1_0.jpg" alt="Advanced Synthetic Lab" style="width: 100%; height: 160px; object-fit: cover;" />
                      <div style="padding: 12px;">
                        <div style="font-weight: 700; font-size: 14px; color: #111; margin-bottom: 4px;">Searle Synthetic Laboratories</div>
                        <div style="font-size: 12.5px; color: #666; line-height: 1.4;">State-of-the-art chemical fume hoods, inert-atmosphere gloveboxes, and high-pressure reactors.</div>
                      </div>
                    </div>
                    <div style="background: #fff; border: 1px solid #ddd; border-radius: 4px; overflow: hidden; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
                      <img src="../assets/chem_images/ombuds_1.jpg" alt="Graduate Research Center" style="width: 100%; height: 160px; object-fit: cover;" />
                      <div style="padding: 12px;">
                        <div style="font-weight: 700; font-size: 14px; color: #111; margin-bottom: 4px;">Graduate Research Commons</div>
                        <div style="font-size: 12.5px; color: #666; line-height: 1.4;">Dedicated collaborative work and mentoring space for doctoral candidates and postdoctoral fellows.</div>
                      </div>
                    </div>
                  </div>
                </div>

              </div>
"""

updated_content = content[:start_idx] + new_faculty_html + "\n                " + content[end_idx:]

with open(page_path, 'w', encoding='utf-8') as f:
    f.write(updated_content)

print("Successfully updated chemistry faculty section with official portraits and facility photographs!")
