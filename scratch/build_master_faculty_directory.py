"""
Master Faculty Directory Generator
Compiles all 148 faculty members into:
- site_1to1/faculty.html (root directory)
- site_1to1/pages/faculty.html (pages directory)
- site_1to1/assets/faculty/faculty_directory.json
"""

import os
import json
import re
import sys

sys.path.insert(0, os.path.dirname(__file__))

from uchicago_complete_faculty import ALL_FACULTY

SITE_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "site_1to1"))

# Normalize faculty entries
for f in ALL_FACULTY:
    # Ensure accolades list
    if "accolades" not in f:
        f["accolades"] = []
    # Ensure tags list
    if "tags" not in f:
        f["tags"] = []
    # Ensure publications list
    if "publications" not in f:
        f["publications"] = []

print(f"Loaded {len(ALL_FACULTY)} master faculty profiles.")

DEPARTMENTS_OPTIONS = [
    ("all", "All Departments & Schools (17)"),
    ("department-of-chemistry", "Department of Chemistry"),
    ("department-of-computer-science", "Department of Computer Science"),
    ("department-of-economics", "Kenneth C. Griffin Department of Economics"),
    ("department-of-physics", "Department of Physics"),
    ("department-of-mathematics", "Department of Mathematics"),
    ("department-of-statistics", "Department of Statistics & Data Science"),
    ("pritzker-school-of-molecular-engineering", "Pritzker School of Molecular Engineering"),
    ("department-of-biochemistry-and-molecular-biology", "Department of Biochemistry & Molecular Biology"),
    ("department-of-history", "Department of History"),
    ("department-of-philosophy", "Department of Philosophy"),
    ("department-of-political-science", "Department of Political Science"),
    ("department-of-sociology", "Department of Sociology"),
    ("department-of-english", "Department of English Language & Literature"),
    ("chicago-booth-school-of-business", "Chicago Booth School of Business"),
    ("university-of-chicago-law-school", "The University of Chicago Law School"),
    ("harris-school-of-public-policy", "Harris School of Public Policy"),
    ("pritzker-school-of-medicine", "Pritzker School of Medicine"),
]

def generate_directory_html(is_subpage=False):
    asset_prefix = "../" if is_subpage else ""
    pages_prefix = "" if is_subpage else "pages/"
    root_link = "../index.html" if is_subpage else "index.html"
    portal_link = "../portal.html" if is_subpage else "portal.html"

    # Count accolades
    nobel_count = len([f for f in ALL_FACULTY if any("nobel" in str(a).lower() for a in f.get("accolades", []))])
    nas_count = len([f for f in ALL_FACULTY if any("national academy" in str(a).lower() or "nas" in str(a).lower() or "nam" in str(a).lower() or "nae" in str(a).lower() for a in f.get("accolades", []))])
    macarthur_count = len([f for f in ALL_FACULTY if any("macarthur" in str(a).lower() for a in f.get("accolades", []))])

    dept_options_html = "\n".join([
        f'              <option value="{val}">{label}</option>'
        for val, label in DEPARTMENTS_OPTIONS
    ])

    html = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Faculty Directory | The University of Chicago</title>
  <meta name="viewport" content="width=device-width,initial-scale=1,shrink-to-fit=no">
  <meta name="description" content="Explore distinguished faculty across 17 academic departments and 6 divisions at The University of Chicago. Search profiles, research specializations, Nobel laureates, and laboratory websites.">
  <link rel="icon" href="/dist/intranet/favicon.ico">
  <link href="{asset_prefix}css/main.316e8eaf.chunk.css" rel="stylesheet">
  <link href="{asset_prefix}css/EduHeader.0831b491.chunk.css" rel="stylesheet">
  <link href="{asset_prefix}css/Alert.2a28d6b7.chunk.css" rel="stylesheet">
  <link href="{asset_prefix}css/PageHeroBanner.a18316f0.chunk.css" rel="stylesheet">
  <link href="{asset_prefix}css/LeftNav.9868dff4.chunk.css" rel="stylesheet">
  <link href="{asset_prefix}css/HeadlineTextBold.e2cc6b10.chunk.css" rel="stylesheet">
  <link href="{asset_prefix}css/Footer.6e030fa0.chunk.css" rel="stylesheet">
  <link rel="preload" href="{asset_prefix}webfonts/fa-solid-900.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="stylesheet" href="{asset_prefix}css/fontawesome.min.css">
  <link rel="stylesheet" href="{asset_prefix}fonts/UChicagoSansSerif.css">
  <link rel="stylesheet" href="{asset_prefix}fonts/UChicagoSerif.css">
  <link rel="stylesheet" href="{asset_prefix}css/replica_1to1_enhancements.css">
  <link rel="stylesheet" href="{asset_prefix}css/all_components.bundle.css">
  
  <style>
    .faculty-hero-section {{
      background: linear-gradient(135deg, #4b0000 0%, #800000 65%, #300000 100%);
      color: #fff;
      padding: 60px 24px 50px;
      text-align: center;
      position: relative;
      box-shadow: inset 0 -10px 20px rgba(0,0,0,0.2);
    }}
    .faculty-hero-inner {{
      max-width: 1050px;
      margin: 0 auto;
    }}
    .faculty-hero-badge {{
      display: inline-block;
      background: rgba(255,255,255,0.15);
      border: 1px solid rgba(255,255,255,0.3);
      padding: 5px 14px;
      border-radius: 20px;
      font-size: 13px;
      font-weight: 600;
      letter-spacing: 0.5px;
      margin-bottom: 14px;
      text-transform: uppercase;
    }}
    .faculty-hero-title {{
      font-family: 'UChicagoSerif', Georgia, serif;
      font-size: 46px;
      line-height: 1.15;
      margin: 0 0 16px 0;
      font-weight: 700;
      text-shadow: 0 2px 4px rgba(0,0,0,0.3);
    }}
    .faculty-hero-sub {{
      font-size: 17px;
      line-height: 1.6;
      max-width: 760px;
      margin: 0 auto 30px;
      color: #f7dede;
    }}
    .stat-ribbon {{
      display: flex;
      justify-content: center;
      gap: 36px;
      flex-wrap: wrap;
      padding-top: 20px;
      border-top: 1px solid rgba(255,255,255,0.2);
    }}
    .stat-item {{
      text-align: center;
    }}
    .stat-number {{
      font-family: 'UChicagoSerif', Georgia, serif;
      font-size: 32px;
      font-weight: 700;
      color: #fff;
      display: block;
      line-height: 1.1;
    }}
    .stat-label {{
      font-size: 12px;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      color: #f0caca;
      font-weight: 600;
    }}

    /* Directory Container */
    .faculty-directory-wrap {{
      max-width: 1280px;
      margin: 0 auto;
      padding: 30px 24px 60px;
    }}

    /* Sticky Search & Filter Toolbar */
    .directory-toolbar {{
      background: #fff;
      border: 1px solid #e0e0e0;
      border-radius: 6px;
      box-shadow: 0 4px 14px rgba(0,0,0,0.06);
      padding: 20px 24px;
      margin-bottom: 28px;
      position: sticky;
      top: 0;
      z-index: 1000;
      backdrop-filter: blur(8px);
    }}
    .toolbar-row-top {{
      display: flex;
      gap: 16px;
      align-items: center;
      flex-wrap: wrap;
      margin-bottom: 16px;
    }}
    .search-input-box {{
      flex: 1;
      min-width: 280px;
      position: relative;
    }}
    .search-input-box input {{
      width: 100%;
      height: 44px;
      border: 1px solid #ccc;
      border-radius: 4px;
      padding: 0 16px 0 42px;
      font-size: 15px;
      color: #222;
      transition: all 0.2s;
      box-sizing: border-box;
    }}
    .search-input-box input:focus {{
      border-color: #800000;
      outline: none;
      box-shadow: 0 0 0 3px rgba(128,0,0,0.15);
    }}
    .search-input-box i {{
      position: absolute;
      left: 14px;
      top: 14px;
      color: #800000;
      font-size: 16px;
    }}
    .filter-dropdowns {{
      display: flex;
      gap: 12px;
      flex-wrap: wrap;
    }}
    .filter-select {{
      height: 44px;
      border: 1px solid #ccc;
      border-radius: 4px;
      padding: 0 14px;
      font-size: 14px;
      color: #333;
      background: #fafafa;
      font-weight: 500;
      cursor: pointer;
      max-width: 280px;
    }}
    .filter-select:focus {{
      border-color: #800000;
      outline: none;
    }}

    /* Domain Tabs */
    .domain-tabs {{
      display: flex;
      gap: 8px;
      overflow-x: auto;
      padding-bottom: 4px;
      border-top: 1px solid #eee;
      padding-top: 14px;
    }}
    .domain-tab-btn {{
      background: #f4f4f4;
      border: 1px solid #ddd;
      border-radius: 20px;
      padding: 6px 16px;
      font-size: 13.5px;
      font-weight: 600;
      color: #444;
      cursor: pointer;
      white-space: nowrap;
      transition: all 0.2s;
    }}
    .domain-tab-btn:hover {{
      background: #eaeaea;
      color: #111;
    }}
    .domain-tab-btn.is-active {{
      background: #800000;
      color: #fff;
      border-color: #800000;
      box-shadow: 0 2px 4px rgba(128,0,0,0.25);
    }}

    /* Results Header */
    .results-meta-bar {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 20px;
      font-size: 14px;
      color: #555;
    }}
    .reset-filters-btn {{
      background: none;
      border: none;
      color: #800000;
      text-decoration: underline;
      font-weight: 600;
      cursor: pointer;
      font-size: 13.5px;
    }}

    /* Faculty Grid */
    .faculty-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(360px, 1fr));
      gap: 24px;
    }}
    .faculty-card {{
      background: #fff;
      border: 1px solid #e2e2e2;
      border-top: 4px solid #800000;
      border-radius: 4px;
      box-shadow: 0 2px 6px rgba(0,0,0,0.04);
      display: flex;
      flex-direction: column;
      transition: transform 0.2s, box-shadow 0.2s;
      overflow: hidden;
    }}
    .faculty-card:hover {{
      transform: translateY(-3px);
      box-shadow: 0 8px 20px rgba(0,0,0,0.09);
    }}
    .card-top {{
      display: flex;
      gap: 16px;
      padding: 20px 20px 14px;
    }}
    .avatar-wrapper {{
      width: 90px;
      height: 115px;
      flex-shrink: 0;
      background: #800000;
      border-radius: 3px;
      overflow: hidden;
      box-shadow: 0 2px 4px rgba(0,0,0,0.12);
      position: relative;
    }}
    .avatar-wrapper img {{
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
    }}
    .faculty-avatar-fallback {{
      display: flex;
      width: 100%;
      height: 100%;
      background: #800000;
      color: #fff;
      font-family: 'UChicagoSerif', Georgia, serif;
      font-weight: 700;
      font-size: 28px;
      align-items: center;
      justify-content: center;
      text-shadow: 0 1px 2px rgba(0,0,0,0.3);
    }}
    .card-header-info {{
      flex: 1;
      min-width: 0;
    }}
    .faculty-division-pill {{
      display: inline-block;
      font-size: 11px;
      font-weight: 700;
      color: #800000;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      margin-bottom: 4px;
    }}
    .faculty-card-name {{
      font-family: 'UChicagoSerif', Georgia, serif;
      font-size: 20px;
      line-height: 1.25;
      margin: 0 0 4px 0;
      font-weight: 700;
      color: #1a1a1a;
    }}
    .faculty-card-name a {{
      color: #1a1a1a;
      text-decoration: none;
    }}
    .faculty-card-name a:hover {{
      color: #800000;
    }}
    .faculty-card-title {{
      font-size: 13px;
      font-weight: 600;
      color: #444;
      line-height: 1.4;
      margin-bottom: 3px;
    }}
    .faculty-card-degrees {{
      font-size: 12px;
      color: #777;
      margin-bottom: 6px;
    }}
    .accolade-badges {{
      display: flex;
      flex-wrap: wrap;
      gap: 4px;
      margin-top: 6px;
    }}
    .accolade-tag {{
      font-size: 11px;
      font-weight: 700;
      color: #800000;
      background: #f7e8e8;
      border: 1px solid #e4bebe;
      padding: 2px 6px;
      border-radius: 3px;
    }}
    .card-body {{
      padding: 0 20px 16px;
      flex: 1;
    }}
    .faculty-bio-snippet {{
      font-size: 13px;
      line-height: 1.55;
      color: #333;
      margin-bottom: 12px;
      display: -webkit-box;
      -webkit-line-clamp: 3;
      -webkit-box-orient: vertical;
      overflow: hidden;
    }}
    .faculty-tags-box {{
      display: flex;
      flex-wrap: wrap;
      gap: 4px;
      margin-bottom: 12px;
    }}
    .research-pill {{
      font-size: 11.5px;
      color: #444;
      background: #f0f0f0;
      border: 1px solid #ddd;
      padding: 2px 7px;
      border-radius: 3px;
    }}
    .card-footer {{
      padding: 12px 20px;
      background: #fafafa;
      border-top: 1px solid #eee;
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 12.5px;
    }}
    .card-footer-links a {{
      color: #800000;
      font-weight: 600;
      text-decoration: underline;
      margin-right: 12px;
    }}
    .profile-modal-btn {{
      background: #800000;
      color: #fff;
      border: none;
      padding: 6px 14px;
      border-radius: 3px;
      font-size: 12.5px;
      font-weight: 600;
      cursor: pointer;
      transition: background 0.2s;
    }}
    .profile-modal-btn:hover {{
      background: #5e0000;
    }}

    /* Modal Styles */
    .modal-overlay {{
      display: none;
      position: fixed;
      inset: 0;
      background: rgba(0,0,0,0.65);
      z-index: 99999;
      align-items: center;
      justify-content: center;
      padding: 20px;
      backdrop-filter: blur(3px);
    }}
    .modal-overlay.is-active {{
      display: flex;
    }}
    .modal-card {{
      background: #fff;
      border-radius: 6px;
      max-width: 800px;
      width: 100%;
      max-height: 90vh;
      overflow-y: auto;
      position: relative;
      box-shadow: 0 10px 40px rgba(0,0,0,0.25);
      border-top: 5px solid #800000;
      padding: 32px;
      animation: modalFadeIn 0.2s ease-out;
    }}
    .modal-close-btn {{
      position: absolute;
      top: 16px;
      right: 18px;
      background: transparent;
      border: none;
      font-size: 26px;
      color: #666;
      cursor: pointer;
      line-height: 1;
    }}
    .modal-close-btn:hover {{
      color: #800000;
    }}
    .modal-header-section {{
      display: flex;
      gap: 22px;
      align-items: flex-start;
      margin-bottom: 24px;
      padding-bottom: 20px;
      border-bottom: 1px solid #eee;
    }}
    .modal-avatar-wrap {{
      width: 110px;
      height: 140px;
      flex-shrink: 0;
      background: #800000;
      border-radius: 4px;
      overflow: hidden;
      box-shadow: 0 2px 6px rgba(0,0,0,0.15);
    }}
    .modal-avatar-wrap img {{
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
    }}
    .modal-title-box h2 {{
      font-family: 'UChicagoSerif', Georgia, serif;
      font-size: 28px;
      color: #1a1a1a;
      margin: 0 0 6px 0;
      font-weight: 700;
    }}
    .modal-section-title {{
      font-family: 'UChicagoSerif', Georgia, serif;
      font-size: 18px;
      color: #800000;
      margin: 20px 0 8px 0;
      font-weight: 700;
      border-bottom: 1px solid #eee;
      padding-bottom: 4px;
    }}
    .modal-bio-text {{
      font-size: 15px;
      line-height: 1.7;
      color: #333;
    }}
    .modal-publications-list {{
      padding-left: 20px;
      font-size: 14px;
      line-height: 1.65;
      color: #444;
      margin: 0;
    }}
  </style>
</head>
<body>
  <div id="root">
    <!-- Header -->
    <header class="EduHeader_container__2uGdE" id="header" data-mobilenavisopen="false">
      <a href="#maincontent" class="EduHeader_skipLink__188b9">Skip to main content</a>
      <a class="EduHeader_logoContainer__1rYiP" href="{root_link}">
        <span class="linkText">
          <img alt="The University of Chicago Logo" class="EduHeader_desktopLogo__2qFkS" src="{asset_prefix}assets/logo-background.svg" />
          <img alt="The University of Chicago Logo" class="EduHeader_mobileLogo__2-wip" src="{asset_prefix}assets/logo-background-mobile.svg" />
        </span>
      </a>
      <button id="mobileTogBtn" class="EduHeader_mobileNavToggle__1rFw5" aria-label="Show main menu" aria-expanded="false"></button>

      <div class="EduHeader_headerNavigation__3Hyzr EduHeader_desktopOnly__2L_Sd" data-nav-context="desktop">
        <div class="EduBrandBar_container__5LPzZ" data-brandbar="true">
          <div class="single-col-inner">
            <div class="EduBrandBar_innerContainer__3uAha">
              <div class="EduBrandBar_navList__8fxdi">
                <ul class="EduBrandBar_linkContainer__GvNmq">
                  <li class="EduBrandBar_linkListItem__YDMHQ"><a href="https://news.uchicago.asia" class="EduBrandBar_brandBarLink__2sbcq" target="_blank" rel="noopener noreferrer"><span class="linkText">News</span></a></li>
                  <li class="EduBrandBar_linkListItem__YDMHQ"><a href="https://events.uchicago.asia/" class="EduBrandBar_brandBarLink__2sbcq" target="_blank" rel="noopener noreferrer"><span class="linkText">Events</span></a></li>
                  <li class="EduBrandBar_linkListItem__YDMHQ"><a class="EduBrandBar_brandBarLink__2sbcq" href="{pages_prefix}careers.html"><span class="linkText">Careers</span></a></li>
                </ul>
              </div>
              <div class="EduBrandBar_navList__8fxdi">
                <ul class="EduBrandBar_linkContainer__GvNmq">
                  <li class="EduBrandBar_linkListItem__YDMHQ"><a class="EduBrandBar_brandBarLink__2sbcq" href="{pages_prefix}visit.html"><span class="linkText">Visit</span></a></li>
                  <li class="EduBrandBar_linkListItem__YDMHQ"><a class="EduBrandBar_brandBarLink__2sbcq" href="{pages_prefix}contact-us.html"><span class="linkText">Contact Us</span></a></li>
                  <li class="EduBrandBar_linkListItem__YDMHQ"><a href="{pages_prefix}faculty.html" class="EduBrandBar_brandBarLink__2sbcq"><span class="linkText"><i class="fa fa-users" style="margin-right:4px; color:#800000;"></i>Directory</span></a></li>
                </ul>
                <a href="{portal_link}" class="EduBrandBar_brandBarLink__2sbcq" style="background:#800000; color:#fff !important; padding:4px 12px; border-radius:3px; font-weight:700; margin-left:12px;">Portal</a>
              </div>
            </div>
          </div>
        </div>

        <nav class="EduNavigation_container__2jUpk" aria-label="Main">
          <div class="single-col-inner">
            <div class="EduNavigation_navContainer__3rU6H">
              <ul class="EduNavigation_navList__-DNEa EduNavigation_leftNav__1H8RA">
                <li class="EduNavigation_navListItem__2Qihw"><a class="EduNavigation_l1Link__1J9ID" href="{pages_prefix}who-we-are.html"><span class="linkText">Who We Are</span></a></li>
                <li class="EduNavigation_navListItem__2Qihw"><a class="EduNavigation_l1Link__1J9ID" href="{pages_prefix}academics.html"><span class="linkText">Academics</span></a></li>
                <li class="EduNavigation_navListItem__2Qihw"><a class="EduNavigation_l1Link__1J9ID" href="{pages_prefix}research-and-scholarship.html"><span class="linkText">Research</span></a></li>
                <li class="EduNavigation_navListItem__2Qihw"><a class="EduNavigation_l1Link__1J9ID" href="{pages_prefix}admissions.html"><span class="linkText">Admissions</span></a></li>
              </ul>
              <ul class="EduNavigation_navList__-DNEa EduNavigation_rightNav__367Qa">
                <li class="EduNavigation_navListItem__2Qihw"><a class="EduNavigation_l1Link__1J9ID" href="{pages_prefix}life-at-uchicago.html"><span class="linkText">Life at UChicago</span></a></li>
                <li class="EduNavigation_navListItem__2Qihw"><a class="EduNavigation_l1Link__1J9ID" href="{pages_prefix}faculty.html" style="color:#800000; font-weight:700;"><span class="linkText">Faculty</span></a></li>
                <li class="EduNavigation_navListItem__2Qihw"><a class="EduNavigation_l1Link__1J9ID EduNavigation_linkHighlight__iQb01" href="{portal_link}" style="color:#800000; font-weight:700;"><span class="linkText"><i class="fa-solid fa-lock" style="margin-right:4px;"></i>Applicant Portal</span></a></li>
              </ul>
            </div>
          </div>
        </nav>
      </div>
      <div id="maincontent" class="EduHeader_skipLinkAnchor__2XFq9">Main content</div>
    </header>

    <!-- Faculty Hero Banner -->
    <section class="faculty-hero-section">
      <div class="faculty-hero-inner">
        <div class="faculty-hero-badge">
          <i class="fa fa-university"></i> Academic Divisions &amp; Faculty
        </div>
        <h1 class="faculty-hero-title">Faculty Directory</h1>
        <p class="faculty-hero-sub">
          The University of Chicago is home to an extraordinary community of scholars, researchers, and educators pioneering breakthroughs and shaping disciplines across the physical, biological, and social sciences, the humanities, molecular engineering, and professional schools.
        </p>

        <!-- Stat Ribbon -->
        <div class="stat-ribbon">
          <div class="stat-item">
            <span class="stat-number">{nobel_count}+</span>
            <span class="stat-label">Nobel Laureates in Roster</span>
          </div>
          <div class="stat-item">
            <span class="stat-number">{nas_count}+</span>
            <span class="stat-label">National Academy Members</span>
          </div>
          <div class="stat-item">
            <span class="stat-number">{macarthur_count}+</span>
            <span class="stat-label">MacArthur Fellows</span>
          </div>
          <div class="stat-item">
            <span class="stat-number">17</span>
            <span class="stat-label">Academic Departments</span>
          </div>
          <div class="stat-item">
            <span class="stat-number">{len(ALL_FACULTY)}</span>
            <span class="stat-label">Distinguished Professors</span>
          </div>
        </div>
      </div>
    </section>

    <!-- Faculty Directory App -->
    <div class="faculty-directory-wrap">
      
      <!-- Interactive Sticky Toolbar -->
      <div class="directory-toolbar">
        <div class="toolbar-row-top">
          <!-- Real-time Search Input -->
          <div class="search-input-box">
            <i class="fa fa-search"></i>
            <input type="text" id="facultySearchInput" placeholder="Search by professor name, research area, tag, or office..." autocomplete="off">
          </div>

          <!-- Secondary Filters -->
          <div class="filter-dropdowns">
            <select id="departmentSelect" class="filter-select" aria-label="Filter by department">
{dept_options_html}
            </select>

            <select id="accoladeSelect" class="filter-select" aria-label="Filter by distinction">
              <option value="all">All Distinctions</option>
              <option value="nobel">Nobel Prize Laureates</option>
              <option value="national-academy">National Academy Members (NAS/NAE/NAM)</option>
              <option value="macarthur">MacArthur 'Genius' Fellows</option>
              <option value="chairs">Deans &amp; Department Chairs</option>
            </select>
          </div>
        </div>

        <!-- Academic Domain Tabs -->
        <div class="domain-tabs" id="domainTabsContainer">
          <button class="domain-tab-btn is-active" data-domain="all">All Domains ({len(ALL_FACULTY)})</button>
          <button class="domain-tab-btn" data-domain="psd">Physical Sciences (PSD)</button>
          <button class="domain-tab-btn" data-domain="bsd">Biological Sciences &amp; Medicine (BSD)</button>
          <button class="domain-tab-btn" data-domain="ssd">Social Sciences (SSD)</button>
          <button class="domain-tab-btn" data-domain="humanities">Humanities</button>
          <button class="domain-tab-btn" data-domain="pme">Molecular Engineering (PME)</button>
          <button class="domain-tab-btn" data-domain="professional">Professional Schools (Booth, Law, Harris)</button>
        </div>
      </div>

      <!-- Results Meta Information -->
      <div class="results-meta-bar">
        <div>
          Showing <strong><span id="resultsCount">{len(ALL_FACULTY)}</span></strong> of {len(ALL_FACULTY)} faculty members
          <span id="activeFilterDesc" style="color:#800000; font-weight:600; margin-left:6px;"></span>
        </div>
        <button id="resetFiltersBtn" class="reset-filters-btn" style="display:none;">Clear All Filters</button>
      </div>

      <!-- Main Faculty Grid -->
      <div class="faculty-grid" id="facultyGridContainer"></div>
    </div>

    <!-- Modal Dialog -->
    <div id="facultyModalOverlay" class="modal-overlay" role="dialog" aria-modal="true">
      <div class="modal-card">
        <button id="modalCloseBtn" class="modal-close-btn" aria-label="Close dialog">&times;</button>
        <div id="modalContentInner"></div>
      </div>
    </div>

    <!-- Footer -->
    <footer class="Footer_container__2FhK_">
      <div class="single-col-inner">
        <div class="Footer_topContainer__3dKx4">
          <div class="Footer_leftCol__3qE_5">
            <a class="Footer_logoLink__2rZ5m" href="{root_link}">
              <img alt="The University of Chicago" class="Footer_logo__1S719" src="{asset_prefix}assets/logo-background.svg" />
            </a>
            <p class="Footer_address__2v81N">
              The University of Chicago<br />
              Edward H. Levi Hall<br />
              5801 S. Ellis Avenue<br />
              Chicago, Illinois 60637
            </p>
          </div>
          <div class="Footer_middleCol__2f4jJ">
            <ul class="Footer_navList__3Z8K8">
              <li><a href="{pages_prefix}who-we-are.html">Who We Are</a></li>
              <li><a href="{pages_prefix}academics.html">Academics</a></li>
              <li><a href="{pages_prefix}academics_academic-departments.html">Academic Departments</a></li>
              <li><a href="{pages_prefix}faculty.html">Faculty Directory</a></li>
              <li><a href="{pages_prefix}research-and-scholarship.html">Research &amp; Scholarship</a></li>
              <li><a href="{pages_prefix}admissions.html">Admissions &amp; Aid</a></li>
              <li><a href="{portal_link}">Applicant Portal</a></li>
            </ul>
          </div>
        </div>
        <div class="Footer_bottomContainer__2_e1O">
          <p class="Footer_copyright__3rD-u">&copy; 2026 The University of Chicago. All rights reserved.</p>
        </div>
      </div>
    </footer>
  </div>

  <!-- Faculty Data JSON & Script -->
  <script>
    var FACULTY_DATA = {json.dumps(ALL_FACULTY, indent=2)};
    var assetPrefix = "{asset_prefix}";
    var pagesPrefix = "{pages_prefix}";

    (function () {{
      var currentDomain = "all";
      var currentDept = "all";
      var currentAccolade = "all";
      var searchQuery = "";

      var searchInput = document.getElementById("facultySearchInput");
      var deptSelect = document.getElementById("departmentSelect");
      var accoladeSelect = document.getElementById("accoladeSelect");
      var domainTabsContainer = document.getElementById("domainTabsContainer");
      var gridEl = document.getElementById("facultyGridContainer");
      var countEl = document.getElementById("resultsCount");
      var resetBtn = document.getElementById("resetFiltersBtn");
      var activeFilterDesc = document.getElementById("activeFilterDesc");

      var modalOverlay = document.getElementById("facultyModalOverlay");
      var modalCloseBtn = document.getElementById("modalCloseBtn");
      var modalContent = document.getElementById("modalContentInner");

      function getInitials(name) {{
        var clean = name.replace(/^(Prof\.|Dr\.|Dean)\s*/, "").trim();
        var parts = clean.split(" ");
        if (parts.length >= 2) {{
          return (parts[0][0] + parts[parts.length - 1][0]).toUpperCase();
        }} else if (parts.length === 1) {{
          return parts[0].substring(0, 2).toUpperCase();
        }}
        return "UC";
      }}

      function renderCard(f) {{
        var initials = getInitials(f.name);
        var photoSrc = f.photo ? (f.photo.indexOf("http") === 0 || f.photo.indexOf("../") === 0 ? f.photo : (assetPrefix + f.photo)) : "";

        var accoladesHtml = (f.accolades || []).slice(0, 3).map(function (a) {{
          return '<span class="accolade-tag">' + a + '</span>';
        }}).join("");

        var tagsHtml = (f.tags || []).slice(0, 4).map(function (t) {{
          return '<span class="research-pill">' + t + '</span>';
        }}).join("");

        var deptSlug = f.deptKey || "";
        var deptLinkHtml = "";
        if (deptSlug) {{
          deptLinkHtml = '<a href="' + pagesPrefix + deptSlug + '.html" style="color:#800000; text-decoration:underline;">' + f.department + '</a>';
        }} else {{
          deptLinkHtml = f.department;
        }}

        return `
          <div class="faculty-card" id="card-${{f.id}}">
            <div class="card-top">
              <div class="avatar-wrapper">
                ${{photoSrc ? `
                  <img src="${{photoSrc}}" alt="${{f.name}}" onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';">
                  <div class="faculty-avatar-fallback" style="display:none;">${{initials}}</div>
                ` : `
                  <div class="faculty-avatar-fallback">${{initials}}</div>
                `}}
              </div>
              <div class="card-header-info">
                <span class="faculty-division-pill">${{f.domainLabel || ''}}</span>
                <h3 class="faculty-card-name">
                  <a href="javascript:void(0)" onclick="openFacultyModal('${{f.id}}')">${{f.name}}</a>
                </h3>
                <div class="faculty-card-title">${{f.title}}</div>
                <div class="faculty-card-degrees">${{f.degrees || ''}}</div>
                ${{accoladesHtml ? '<div class="accolade-badges">' + accoladesHtml + '</div>' : ''}}
              </div>
            </div>

            <div class="card-body">
              <div style="font-size:12px; color:#666; margin-bottom:8px;">
                <i class="fa fa-university" style="color:#800000; margin-right:4px;"></i>${{deptLinkHtml}}
              </div>
              <div class="faculty-bio-snippet">${{f.bio}}</div>
              ${{tagsHtml ? '<div class="faculty-tags-box">' + tagsHtml + '</div>' : ''}}
            </div>

            <div class="card-footer">
              <div class="card-footer-links">
                ${{f.office ? '<span title="' + f.office + '"><i class="fa fa-building" style="color:#800000; margin-right:3px;"></i>' + f.office.split(" ")[0] + '</span>' : ''}}
                ${{f.email ? '<a href="mailto:' + f.email + '" style="margin-left:8px;"><i class="fa fa-envelope" style="margin-right:2px;"></i>Email</a>' : ''}}
              </div>
              <button class="profile-modal-btn" onclick="openFacultyModal('${{f.id}}')">Profile &rarr;</button>
            </div>
          </div>
        `;
      }}

      function filterAndRender() {{
        var q = searchQuery.toLowerCase().trim();

        var filtered = FACULTY_DATA.filter(function (f) {{
          // Domain Filter
          if (currentDomain !== "all" && f.domain !== currentDomain) return false;

          // Department Filter
          if (currentDept !== "all") {{
            var fKey = (f.deptKey || "").toLowerCase();
            var fDept = (f.department || "").toLowerCase();
            var target = currentDept.toLowerCase();
            var targetClean = target.replace("department-of-", "").replace("-school", "").replace("-of-", "");
            if (fKey !== target && !fKey.includes(target) && !fKey.includes(targetClean) && !fDept.includes(targetClean)) {{
              return false;
            }}
          }}

          // Distinction Filter
          if (currentAccolade === "nobel") {{
            if (!f.accolades || !f.accolades.some(function (a) {{ return a.toLowerCase().includes("nobel"); }})) return false;
          }} else if (currentAccolade === "national-academy") {{
            if (!f.accolades || !f.accolades.some(function (a) {{ return a.toLowerCase().includes("national academy") || a.includes("NAS") || a.includes("NAE") || a.includes("NAM"); }})) return false;
          }} else if (currentAccolade === "macarthur") {{
            if (!f.accolades || !f.accolades.some(function (a) {{ return a.toLowerCase().includes("macarthur"); }})) return false;
          }} else if (currentAccolade === "chairs") {{
            if (!f.accolades || !f.accolades.some(function (a) {{ return a.toLowerCase().includes("chair") || a.toLowerCase().includes("dean") || a.toLowerCase().includes("director") || a.toLowerCase().includes("provost"); }})) return false;
          }}

          // Search Query
          if (q) {{
            var searchHaystack = [
              f.name,
              f.title,
              f.department,
              f.domainLabel,
              f.degrees,
              f.office,
              f.bio,
              (f.tags || []).join(" "),
              (f.accolades || []).join(" "),
              (f.publications || []).join(" ")
            ].join(" ").toLowerCase();

            if (!searchHaystack.includes(q)) return false;
          }}

          return true;
        }});

        gridEl.innerHTML = filtered.map(renderCard).join("");
        countEl.textContent = filtered.length;

        var isFiltered = currentDomain !== "all" || currentDept !== "all" || currentAccolade !== "all" || q.length > 0;
        resetBtn.style.display = isFiltered ? "inline-block" : "none";

        var desc = [];
        if (currentDomain !== "all") desc.push("Domain: " + currentDomain.toUpperCase());
        if (currentDept !== "all") desc.push("Dept: " + currentDept.replace("department-of-", ""));
        if (currentAccolade !== "all") desc.push("Distinction: " + currentAccolade);
        if (q) desc.push('Search: "' + q + '"');
        activeFilterDesc.textContent = desc.length ? "(" + desc.join(", ") + ")" : "";
      }}

      // Event Listeners
      searchInput.addEventListener("input", function (e) {{
        searchQuery = e.target.value;
        filterAndRender();
      }});

      deptSelect.addEventListener("change", function (e) {{
        currentDept = e.target.value;
        filterAndRender();
      }});

      accoladeSelect.addEventListener("change", function (e) {{
        currentAccolade = e.target.value;
        filterAndRender();
      }});

      domainTabsContainer.addEventListener("click", function (e) {{
        var btn = e.target.closest(".domain-tab-btn");
        if (!btn) return;
        domainTabsContainer.querySelectorAll(".domain-tab-btn").forEach(function (b) {{ b.classList.remove("is-active"); }});
        btn.classList.add("is-active");
        currentDomain = btn.getAttribute("data-domain");
        filterAndRender();
      }});

      resetBtn.addEventListener("click", function () {{
        currentDomain = "all";
        currentDept = "all";
        currentAccolade = "all";
        searchQuery = "";
        searchInput.value = "";
        deptSelect.value = "all";
        accoladeSelect.value = "all";
        domainTabsContainer.querySelectorAll(".domain-tab-btn").forEach(function (b) {{
          if (b.getAttribute("data-domain") === "all") b.classList.add("is-active");
          else b.classList.remove("is-active");
        }});
        filterAndRender();
      }});

      // Modal Handler
      window.openFacultyModal = function (id) {{
        var f = FACULTY_DATA.find(function (item) {{ return item.id === id; }});
        if (!f) return;

        var initials = getInitials(f.name);
        var photoSrc = f.photo ? (f.photo.indexOf("http") === 0 || f.photo.indexOf("../") === 0 ? f.photo : (assetPrefix + f.photo)) : "";

        var pubList = (f.publications || []).map(function (p) {{ return "<li>" + p + "</li>"; }}).join("");
        var accoladesList = (f.accolades || []).map(function (a) {{ return '<span class="accolade-tag">' + a + '</span>'; }}).join(" ");

        modalContent.innerHTML = `
          <div class="modal-header-section">
            <div class="modal-avatar-wrap">
              ${{photoSrc ? `
                <img src="${{photoSrc}}" alt="${{f.name}}" onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';">
                <div class="faculty-avatar-fallback" style="display:none; width:100%; height:100%; font-size:36px;">${{initials}}</div>
              ` : `
                <div class="faculty-avatar-fallback" style="width:100%; height:100%; font-size:36px;">${{initials}}</div>
              `}}
            </div>
            <div class="modal-title-box">
              <span class="faculty-division-pill">${{f.domainLabel || ''}} &bull; ${{f.department}}</span>
              <h2>${{f.name}}</h2>
              <p><strong>${{f.title}}</strong></p>
              <p style="font-size:13px; color:#666;">${{f.degrees || ''}}</p>
              <div style="margin-top: 10px;">${{accoladesList}}</div>
            </div>
          </div>

          <div class="modal-section-title">Biography &amp; Scholarly Contributions</div>
          <div class="modal-bio-text">${{f.bio}}</div>

          ${{f.tags && f.tags.length ? `
            <div class="modal-section-title">Research Areas &amp; Specializations</div>
            <div class="faculty-tags-box" style="margin-bottom:20px;">
              ${{f.tags.map(function(t) {{ return '<span class="research-pill" style="font-size:13px; padding:4px 10px;">' + t + '</span>'; }}).join("")}}
            </div>
          ` : ''}}

          ${{pubList ? `
            <div class="modal-section-title">Selected Publications &amp; Works</div>
            <ul class="modal-publications-list">${{pubList}}</ul>
          ` : ''}}

          <div class="modal-section-title">Contact &amp; Campus Office</div>
          <div style="font-size:14px; line-height:1.7; color:#444;">
            ${{f.office ? '<div><strong>Campus Office:</strong> ' + f.office + ', The University of Chicago</div>' : ''}}
            ${{f.email ? '<div><strong>Email:</strong> <a href="mailto:' + f.email + '" style="color:#800000; font-weight:600;">' + f.email + '</a></div>' : ''}}
            ${{f.lab ? '<div style="margin-top:10px;"><a href="' + f.lab + '" target="_blank" rel="noopener noreferrer" style="color:#800000; text-decoration:underline; font-weight:600;">Visit Laboratory / Academic Directory Website &rarr;</a></div>' : ''}}
          </div>
        `;

        modalOverlay.classList.add("is-active");
      }};

      modalCloseBtn.addEventListener("click", function () {{
        modalOverlay.classList.remove("is-active");
      }});

      modalOverlay.addEventListener("click", function (e) {{
        if (e.target === modalOverlay) {{
          modalOverlay.classList.remove("is-active");
        }}
      }});

      document.addEventListener("keydown", function (e) {{
        if (e.key === "Escape" && modalOverlay.classList.contains("is-active")) {{
          modalOverlay.classList.remove("is-active");
        }}
      }});

      // Initial Render
      filterAndRender();

      // Mobile Menu Toggle Support
      var mobileToggle = document.getElementById("mobileTogBtn");
      var headerEl = document.getElementById("header");
      if (mobileToggle && headerEl) {{
        mobileToggle.addEventListener("click", function () {{
          var isOpen = headerEl.getAttribute("data-mobilenavisopen") === "true";
          headerEl.setAttribute("data-mobilenavisopen", !isOpen ? "true" : "false");
          mobileToggle.setAttribute("aria-expanded", !isOpen ? "true" : "false");
        }});
      }}
    }})();
  </script>
</body>
</html>
"""
    return html

def build_all():
    root_html = generate_directory_html(is_subpage=False)
    with open(os.path.join(SITE_ROOT, "faculty.html"), "w", encoding="utf-8") as f:
        f.write(root_html)
    print("Wrote site_1to1/faculty.html successfully!")

    subpage_html = generate_directory_html(is_subpage=True)
    with open(os.path.join(SITE_ROOT, "pages", "faculty.html"), "w", encoding="utf-8") as f:
        f.write(subpage_html)
    print("Wrote site_1to1/pages/faculty.html successfully!")

    json_path = os.path.join(SITE_ROOT, "assets", "faculty", "faculty_directory.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(ALL_FACULTY, f, indent=2)
    print(f"Wrote {json_path} successfully!")

if __name__ == "__main__":
    build_all()
