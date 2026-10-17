"""
Script to generate all 17 authentic departmental subpages for UChicago Replica.
Outputs high-fidelity, production-grade HTML files to site_1to1/pages/
"""

import os
import json
import re
import sys

sys.path.insert(0, os.path.dirname(__file__))

from uchicago_departments_data import DEPARTMENTS
from uchicago_complete_faculty import ALL_FACULTY

# Ensure output directory exists
PAGES_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "site_1to1", "pages"))
os.makedirs(PAGES_DIR, exist_ok=True)

# Helper function to get initials for avatar
def get_initials(name):
    clean = re.sub(r'^(Prof\.|Dr\.|Dean)\s*', '', name).strip()
    parts = clean.split()
    if len(parts) >= 2:
        return (parts[0][0] + parts[-1][0]).upper()
    elif len(parts) == 1:
        return parts[0][:2].upper()
    return "UC"

# Helper to normalize department matching
def get_dept_faculty(dept_id, dept_name):
    matching = []
    dept_id_clean = dept_id.lower().replace("department-of-", "").replace("-school", "").replace("-of-", "")
    for f in ALL_FACULTY:
        f_dept_key = (f.get("deptKey") or "").lower()
        f_dept_name = (f.get("department") or "").lower()
        if f_dept_key == dept_id or dept_id in f_dept_key:
            matching.append(f)
        elif dept_id_clean in f_dept_key or dept_id_clean in f_dept_name:
            matching.append(f)
        elif dept_name.lower() in f_dept_name:
            matching.append(f)
        elif "chemistry" in dept_id and "chem" in f_dept_key:
            matching.append(f)
        elif "economics" in dept_id and ("econ" in f_dept_key or "economics" in f_dept_name):
            matching.append(f)
        elif "computer-science" in dept_id and ("cs" == f_dept_key or "computer science" in f_dept_name):
            matching.append(f)
        elif "physics" in dept_id and ("phys" in f_dept_key or "physics" in f_dept_name):
            matching.append(f)
        elif "mathematics" in dept_id and ("math" in f_dept_key or "mathematics" in f_dept_name):
            matching.append(f)
        elif "statistics" in dept_id and ("stat" in f_dept_key or "statistics" in f_dept_name):
            matching.append(f)
        elif "molecular-engineering" in dept_id and ("pme" in f_dept_key or "molecular" in f_dept_name):
            matching.append(f)
        elif "biochemistry" in dept_id and ("biochem" in f_dept_key or "biochemistry" in f_dept_name):
            matching.append(f)
        elif "history" in dept_id and ("history" in f_dept_key or "history" in f_dept_name):
            matching.append(f)
        elif "philosophy" in dept_id and ("philosophy" in f_dept_key or "philosophy" in f_dept_name):
            matching.append(f)
        elif "political-science" in dept_id and ("polit" in f_dept_key or "political science" in f_dept_name):
            matching.append(f)
        elif "sociology" in dept_id and ("sociology" in f_dept_key or "sociology" in f_dept_name):
            matching.append(f)
        elif "english" in dept_id and ("english" in f_dept_key or "english" in f_dept_name):
            matching.append(f)
        elif "booth" in dept_id and ("booth" in f_dept_key or "booth" in f_dept_name):
            matching.append(f)
        elif "law" in dept_id and ("law" in f_dept_key or "law school" in f_dept_name):
            matching.append(f)
        elif "harris" in dept_id and ("harris" in f_dept_key or "harris" in f_dept_name or "public policy" in f_dept_name):
            matching.append(f)
        elif "medicine" in dept_id and ("medicine" in f_dept_key or "medicine" in f_dept_name or "pritzker" in f_dept_name):
            matching.append(f)
            
    # Deduplicate by ID
    seen = set()
    deduped = []
    for f in matching:
        if f["id"] not in seen:
            seen.add(f["id"])
            deduped.append(f)
    return deduped

def build_department_page(dept):
    dept_id = dept["id"]
    dept_name = dept["name"]
    division = dept["division"]
    tagline = dept["tagline"]
    hero_img = dept.get("hero_image", "../assets/subpage_media/mainquadfall.png")
    description = dept["description"]
    highlights = dept.get("highlights", [])
    undergrad = dept.get("undergrad_program", "")
    masters = dept.get("masters_program", "")
    phd = dept.get("phd_program", "")
    research_areas = dept.get("research_areas", [])
    facilities = dept.get("facilities", [])
    events = dept.get("events", [])
    contact = dept.get("contact", {})
    building = dept.get("building", "")
    address = dept.get("address", "")
    chair = dept.get("chair", "")

    faculty_list = get_dept_faculty(dept_id, dept_name)
    faculty_count = len(faculty_list)

    # Build Faculty Cards HTML
    faculty_cards_html = []
    for f in faculty_list:
        initials = get_initials(f["name"])
        photo_url = f.get("photo", "")
        # Adjust photo url relative to pages/
        if photo_url:
            if not photo_url.startswith("../") and not photo_url.startswith("http"):
                photo_src = "../" + photo_url
            else:
                photo_src = photo_url
        else:
            photo_src = ""

        accolades_html = ""
        if f.get("accolades"):
            acc_tags = "".join([
                f'<span style="display:inline-block; font-size:11px; font-weight:700; color:#800000; background:#f5e8e8; border:1px solid #e2b9b9; padding:2px 7px; border-radius:3px; margin-right:4px; margin-bottom:4px;">{a}</span>'
                for a in f["accolades"][:3]
            ])
            accolades_html = f'<div style="margin-bottom:10px;">{acc_tags}</div>'

        tags_html = ""
        if f.get("tags"):
            tag_spans = "".join([
                f'<span style="display:inline-block; font-size:11.5px; color:#444; background:#f0f0f0; border:1px solid #ddd; padding:2px 8px; border-radius:3px; margin-right:4px; margin-bottom:4px;">{t}</span>'
                for t in f["tags"][:4]
            ])
            tags_html = f'<div style="margin-bottom:12px;">{tag_spans}</div>'

        avatar_markup = f'''<img src="{photo_src}" alt="{f['name']}" style="width:100%; height:100%; object-fit:cover; display:block;" onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';">
              <div style="display:none; width:100%; height:100%; background:#800000; color:#fff; font-family:'UChicagoSerif', Georgia, serif; font-size:32px; font-weight:700; align-items:center; justify-content:center; text-shadow:0 1px 2px rgba(0,0,0,0.3);">{initials}</div>''' if photo_src else f'''<div style="display:flex; width:100%; height:100%; background:#800000; color:#fff; font-family:'UChicagoSerif', Georgia, serif; font-size:32px; font-weight:700; align-items:center; justify-content:center; text-shadow:0 1px 2px rgba(0,0,0,0.3);">{initials}</div>'''

        office_span = f'<span><i class="fa fa-building" style="color:#800000; margin-right:4px;"></i>{f["office"]}</span>' if f.get('office') else ''
        email_span = f'<span><i class="fa fa-envelope" style="color:#800000; margin-right:4px;"></i><a href="mailto:{f["email"]}" style="color:#800000; text-decoration:underline;">{f["email"]}</a></span>' if f.get('email') else ''
        lab_span = f'<span><i class="fa fa-globe" style="color:#800000; margin-right:4px;"></i><a href="{f["lab"]}" target="_blank" rel="noopener noreferrer" style="color:#800000; text-decoration:underline;">Lab / Research Site</a></span>' if f.get('lab') else ''

        card_html = f'''
          <div class="faculty-card-item" id="faculty-{f['id']}" style="background:#fff; border:1px solid #e0e0e0; border-top:3px solid #800000; padding:22px; display:flex; gap:20px; align-items:flex-start; box-shadow:0 2px 5px rgba(0,0,0,0.04); transition:all 0.2s ease; margin-bottom:20px;">
            <div style="flex-shrink:0; width:105px; height:130px; background:#800000; overflow:hidden; border-radius:4px; position:relative; box-shadow:0 2px 4px rgba(0,0,0,0.15);">
              {avatar_markup}
            </div>
            <div style="flex:1; min-width:0;">
              <div style="display:flex; justify-content:space-between; align-items:baseline; flex-wrap:wrap;">
                <h3 style="font-family:'UChicagoSerif', Georgia, serif; font-size:20px; color:#1a1a1a; margin:0 0 4px 0; font-weight:700;">
                  <a href="javascript:void(0)" onclick="openFacultyModal('{f['id']}')" style="color:#1a1a1a; text-decoration:none;">{f['name']}</a>
                </h3>
              </div>
              <div style="font-size:13.5px; font-weight:700; color:#800000; margin-bottom:3px;">
                {f.get('title', '')}
              </div>
              <div style="font-size:12.5px; color:#666; margin-bottom:8px;">
                {f.get('degrees', '')}
              </div>
              {accolades_html}
              <div style="font-size:13.5px; line-height:1.55; color:#333; margin-bottom:10px;">
                {f.get('bio', '')[:220]}...
              </div>
              {tags_html}
              <div style="display:flex; gap:16px; align-items:center; flex-wrap:wrap; font-size:12.5px; color:#555; padding-top:8px; border-top:1px dashed #eee;">
                {office_span}
                {email_span}
                {lab_span}
                <button onclick="openFacultyModal('{f['id']}')" style="margin-left:auto; background:#800000; color:#fff; border:none; padding:4px 12px; font-size:12px; font-weight:600; border-radius:3px; cursor:pointer;">
                  View Profile &rarr;
                </button>
              </div>
            </div>
          </div>
        '''
        faculty_cards_html.append(card_html)

    faculty_cards_str = "\n".join(faculty_cards_html)

    # Highlights HTML
    highlights_html = ""
    if highlights:
        items = "".join([f'<li style="margin-bottom:8px;"><strong>{h}</strong></li>' for h in highlights])
        highlights_html = f'''
        <div style="background:#faf8f6; border-left:4px solid #800000; padding:16px 20px; margin:24px 0; border-radius:0 4px 4px 0;">
          <h4 style="font-family:'UChicagoSerif', Georgia, serif; font-size:17px; margin:0 0 10px 0; color:#800000; font-weight:700;">Department Highlights</h4>
          <ul style="margin:0; padding-left:18px; line-height:1.6; color:#222; font-size:14.5px;">
            {items}
          </ul>
        </div>
        '''

    # Degree Programs HTML
    dept_short_name = dept_name.replace("Department of ", "").replace("Kenneth C. Griffin Department of ", "")
    undergrad_html = ""
    if undergrad:
        undergrad_html = f'''
        <div style="background:#fff; border:1px solid #e2e2e2; border-left:4px solid #800000; padding:18px 20px; margin-bottom:18px; border-radius:0 4px 4px 0;">
          <h4 style="font-family:'UChicagoSerif', Georgia, serif; font-size:18px; color:#1a1a1a; margin:0 0 8px 0; font-weight:700;">
            Undergraduate Program in {dept_short_name}
          </h4>
          <p style="font-size:14.5px; line-height:1.6; color:#444; margin:0 0 10px 0;">
            {undergrad}
          </p>
          <div style="font-size:13px; color:#666;">
            <strong>Degrees Conferred:</strong> Bachelor of Arts (B.A.), Bachelor of Science (B.S.) &bull; Administered through <strong>The College</strong>
          </div>
        </div>
        '''

    masters_html = ""
    if masters:
        masters_html = f'''
        <div style="background:#fff; border:1px solid #e2e2e2; border-left:4px solid #4a4a4a; padding:18px 20px; margin-bottom:18px; border-radius:0 4px 4px 0;">
          <h4 style="font-family:'UChicagoSerif', Georgia, serif; font-size:18px; color:#1a1a1a; margin:0 0 8px 0; font-weight:700;">
            Master&rsquo;s &amp; Professional Degree Curricula
          </h4>
          <p style="font-size:14.5px; line-height:1.6; color:#444; margin:0 0 10px 0;">
            {masters}
          </p>
        </div>
        '''

    # Research Areas HTML
    research_areas_html = ""
    if research_areas:
        cards = []
        for ra in research_areas:
            cards.append(f'''
              <div style="background:#fff; border:1px solid #e4e4e4; border-top:2px solid #800000; padding:16px; border-radius:4px; box-shadow:0 1px 3px rgba(0,0,0,0.03);">
                <h4 style="font-family:'UChicagoSerif', Georgia, serif; font-size:16px; color:#1a1a1a; margin:0 0 6px 0; font-weight:700;">{ra['title']}</h4>
                <p style="font-size:13.5px; line-height:1.55; color:#444; margin:0;">{ra['desc']}</p>
              </div>
            ''')
        research_areas_html = f'''
        <div id="research" style="scroll-margin-top:100px; margin-top:36px; padding-top:20px; border-top:1px solid #e0e0e0;">
          <h3 style="font-family:'UChicagoSerif', Georgia, serif; font-size:24px; color:#1a1a1a; margin-bottom:14px; font-weight:700;">
            Research Areas &amp; Specializations
          </h3>
          <p style="font-size:15px; line-height:1.6; color:#333; margin-bottom:20px;">
            Faculty, postdoctoral fellows, and graduate researchers collaborate across interdisciplinary fields, driving theoretical innovations and empirical breakthroughs.
          </p>
          <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(280px, 1fr)); gap:16px; margin-bottom:24px;">
            {''.join(cards)}
          </div>
        </div>
        '''

    # Facilities HTML
    facilities_html = ""
    if facilities:
        items = "".join([f'<li style="margin-bottom:8px;">{fac}</li>' for fac in facilities])
        facilities_html = f'''
        <div id="facilities" style="scroll-margin-top:100px; margin-top:30px; background:#f9f9f9; border:1px solid #e5e5e5; padding:20px 24px; border-radius:4px;">
          <h3 style="font-family:'UChicagoSerif', Georgia, serif; font-size:20px; color:#1a1a1a; margin:0 0 12px 0; font-weight:700;">
            World-Class Facilities &amp; Affiliated Institutes
          </h3>
          <ul style="margin:0; padding-left:20px; line-height:1.65; color:#333; font-size:14px;">
            {items}
          </ul>
        </div>
        '''

    # Events HTML
    events_html = ""
    if events:
        items = []
        for ev in events:
            items.append(f'''
              <div style="display:flex; justify-content:space-between; align-items:baseline; padding:12px 0; border-bottom:1px solid #eee; flex-wrap:wrap;">
                <div>
                  <div style="font-weight:700; color:#1a1a1a; font-size:14.5px;">{ev['title']}</div>
                  <div style="font-size:13px; color:#666;">Speaker / Host: {ev.get('speaker', 'Departmental')} &bull; Location: {ev.get('loc', 'Main Hall')}</div>
                </div>
                <div style="font-size:13px; font-weight:600; color:#800000; background:#f6e8e8; padding:3px 10px; border-radius:3px;">
                  {ev.get('date', 'Weekly')}
                </div>
              </div>
            ''')
        events_html = f'''
        <div id="events" style="scroll-margin-top:100px; margin-top:36px; padding-top:20px; border-top:1px solid #e0e0e0;">
          <h3 style="font-family:'UChicagoSerif', Georgia, serif; font-size:24px; color:#1a1a1a; margin-bottom:14px; font-weight:700;">
            Seminars, Colloquia &amp; Events
          </h3>
          <div style="background:#fff; border:1px solid #e0e0e0; padding:16px 20px; border-radius:4px; margin-bottom:20px;">
            {''.join(items)}
          </div>
        </div>
        '''

    # Contact Box
    contact_phone = contact.get("phone", "(773) 702-1234")
    contact_email = contact.get("email", f"{dept_id.replace('department-of-', '')}@uchicago.asia")
    contact_office = contact.get("office", f"{building}, The University of Chicago")
    chair_html = f'<div style="margin-top:4px;"><strong>Department Leadership:</strong> {chair}</div>' if chair else ''

    contact_box_html = f'''
    <div id="contact" style="scroll-margin-top:100px; background:#f4f4f4; border:1px solid #e0e0e0; border-top:3px solid #800000; padding:20px 24px; margin-top:36px; font-size:14px; line-height:1.65;">
      <h3 style="font-family:'UChicagoSerif', Georgia, serif; font-size:18px; margin:0 0 10px 0; color:#1a1a1a; font-weight:700;">
        Department Headquarters &amp; Admissions Contact
      </h3>
      <div><strong>{building}</strong> &bull; {address}</div>
      <div style="margin-top:4px;">
        <strong>Phone:</strong> {contact_phone} &bull; 
        <strong>Email:</strong> <a href="mailto:{contact_email}" style="color:#800000; font-weight:600;">{contact_email}</a>
      </div>
      <div style="margin-top:4px;">
        <strong>Campus Office:</strong> {contact_office}
      </div>
      {chair_html}
    </div>
    '''

    # Full HTML Page Template
    html_content = f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>{dept_name} | The University of Chicago</title>
  <meta name="viewport" content="width=device-width,initial-scale=1,shrink-to-fit=no">
  <meta name="description" content="{dept_name} at The University of Chicago ({division}). Excellence in foundational research, doctoral fellowship programs, undergraduate curricula, and faculty scholarship.">
  <link rel="icon" href="/dist/intranet/favicon.ico">
  <link href="../css/main.316e8eaf.chunk.css" rel="stylesheet">
  <link href="../css/EduHeader.0831b491.chunk.css" rel="stylesheet">
  <link href="../css/Alert.2a28d6b7.chunk.css" rel="stylesheet">
  <link href="../css/PageHeroBanner.a18316f0.chunk.css" rel="stylesheet">
  <link href="../css/LeftNav.9868dff4.chunk.css" rel="stylesheet">
  <link href="../css/SubNavRelatedLinks.06128deb.chunk.css" rel="stylesheet">
  <link href="../css/HeadlineTextBold.e2cc6b10.chunk.css" rel="stylesheet">
  <link href="../css/Footer.6e030fa0.chunk.css" rel="stylesheet">
  <link rel="preload" href="../webfonts/fa-solid-900.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="stylesheet" href="../css/fontawesome.min.css">
  <link rel="stylesheet" href="../fonts/UChicagoSansSerif.css">
  <link rel="stylesheet" href="../fonts/UChicagoSerif.css">
  <link rel="stylesheet" href="../css/replica_1to1_enhancements.css">
  <link rel="stylesheet" href="../css/all_components.bundle.css">
  <style>
    .dept-quicktabs {{
      display: flex;
      gap: 12px;
      overflow-x: auto;
      padding: 12px 0;
      border-bottom: 2px solid #e0e0e0;
      margin-bottom: 24px;
      position: sticky;
      top: 0;
      background: #fff;
      z-index: 100;
    }}
    .dept-tab-btn {{
      padding: 6px 14px;
      font-size: 13.5px;
      font-weight: 600;
      color: #555;
      background: #f7f7f7;
      border: 1px solid #ddd;
      border-radius: 20px;
      text-decoration: none;
      white-space: nowrap;
      transition: all 0.2s;
    }}
    .dept-tab-btn:hover, .dept-tab-btn.active {{
      background: #800000;
      color: #fff;
      border-color: #800000;
    }}
    .faculty-card-item:hover {{
      transform: translateY(-2px);
      box-shadow: 0 6px 16px rgba(0,0,0,0.08) !important;
    }}
    /* Modal Styles */
    .faculty-modal-overlay {{
      display: none;
      position: fixed;
      inset: 0;
      background: rgba(0,0,0,0.65);
      z-index: 999999;
      align-items: center;
      justify-content: center;
      padding: 20px;
      backdrop-filter: blur(3px);
    }}
    .faculty-modal-overlay.is-active {{
      display: flex;
    }}
    .faculty-modal-card {{
      background: #fff;
      border-radius: 6px;
      max-width: 780px;
      width: 100%;
      max-height: 90vh;
      overflow-y: auto;
      position: relative;
      box-shadow: 0 10px 40px rgba(0,0,0,0.25);
      border-top: 5px solid #800000;
      padding: 30px;
      animation: modalFadeIn 0.2s ease-out;
    }}
    @keyframes modalFadeIn {{
      from {{ opacity: 0; transform: scale(0.96); }}
      to {{ opacity: 1; transform: scale(1); }}
    }}
    .faculty-modal-close {{
      position: absolute;
      top: 15px;
      right: 18px;
      background: transparent;
      border: none;
      font-size: 24px;
      color: #666;
      cursor: pointer;
      line-height: 1;
    }}
    .faculty-modal-close:hover {{
      color: #800000;
    }}
  </style>
</head>
<body>
  <div id="root">
    <!-- Header -->
    <header class="EduHeader_container__2uGdE" id="header" data-mobilenavisopen="false">
      <a href="#maincontent" class="EduHeader_skipLink__188b9">Skip to main content</a>
      <a class="EduHeader_logoContainer__1rYiP" href="../index.html">
        <span class="linkText">
          <img alt="The University of Chicago Logo" class="EduHeader_desktopLogo__2qFkS" src="../assets/logo-background.svg" />
          <img alt="The University of Chicago Logo" class="EduHeader_mobileLogo__2-wip" src="../assets/logo-background-mobile.svg" />
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
                  <li class="EduBrandBar_linkListItem__YDMHQ"><a class="EduBrandBar_brandBarLink__2sbcq" href="careers.html"><span class="linkText">Careers</span></a></li>
                </ul>
              </div>
              <div class="EduBrandBar_navList__8fxdi">
                <ul class="EduBrandBar_linkContainer__GvNmq">
                  <li class="EduBrandBar_linkListItem__YDMHQ"><a class="EduBrandBar_brandBarLink__2sbcq" href="visit.html"><span class="linkText">Visit</span></a></li>
                  <li class="EduBrandBar_linkListItem__YDMHQ"><a class="EduBrandBar_brandBarLink__2sbcq" href="contact-us.html"><span class="linkText">Contact Us</span></a></li>
                  <li class="EduBrandBar_linkListItem__YDMHQ"><a href="faculty.html" class="EduBrandBar_brandBarLink__2sbcq"><span class="linkText"><i class="fa fa-users" style="margin-right:4px; color:#800000;"></i>Directory</span></a></li>
                </ul>
                <a href="../portal.html" class="EduBrandBar_brandBarLink__2sbcq" style="background:#800000; color:#fff !important; padding:4px 12px; border-radius:3px; font-weight:700; margin-left:12px;">Portal</a>
              </div>
            </div>
          </div>
        </div>

        <nav class="EduNavigation_container__2jUpk" aria-label="Main">
          <div class="single-col-inner">
            <div class="EduNavigation_navContainer__3rU6H">
              <ul class="EduNavigation_navList__-DNEa EduNavigation_leftNav__1H8RA">
                <li class="EduNavigation_navListItem__2Qihw"><a class="EduNavigation_l1Link__1J9ID" href="who-we-are.html"><span class="linkText">Who We Are</span></a></li>
                <li class="EduNavigation_navListItem__2Qihw"><a class="EduNavigation_l1Link__1J9ID" href="academics.html"><span class="linkText">Academics</span></a></li>
                <li class="EduNavigation_navListItem__2Qihw"><a class="EduNavigation_l1Link__1J9ID" href="research-and-scholarship.html"><span class="linkText">Research</span></a></li>
                <li class="EduNavigation_navListItem__2Qihw"><a class="EduNavigation_l1Link__1J9ID" href="admissions.html"><span class="linkText">Admissions</span></a></li>
              </ul>
              <ul class="EduNavigation_navList__-DNEa EduNavigation_rightNav__367Qa">
                <li class="EduNavigation_navListItem__2Qihw"><a class="EduNavigation_l1Link__1J9ID" href="life-at-uchicago.html"><span class="linkText">Life at UChicago</span></a></li>
                <li class="EduNavigation_navListItem__2Qihw"><a class="EduNavigation_l1Link__1J9ID" href="faculty.html"><span class="linkText">Faculty</span></a></li>
                <li class="EduNavigation_navListItem__2Qihw"><a class="EduNavigation_l1Link__1J9ID EduNavigation_linkHighlight__iQb01" href="../portal.html" style="color:#800000; font-weight:700;"><span class="linkText"><i class="fa-solid fa-lock" style="margin-right:4px;"></i>Applicant Portal</span></a></li>
              </ul>
            </div>
          </div>
        </nav>
      </div>
      <div id="maincontent" class="EduHeader_skipLinkAnchor__2XFq9">Main content</div>
    </header>

    <!-- Page Banner -->
    <main data-sitename="www">
      <div class="jss-main">
        <section class="single-col-wide">
          <section class="PageHeroBanner_container__RKHAN" style="background-image:url({hero_img}); background-position:center; background-size:cover;">
            <div class="PageHeroBanner_containerInner__CEU0x">
              <div style="font-size:13px; font-weight:700; text-transform:uppercase; letter-spacing:1px; color:#fff; background:rgba(128,0,0,0.85); display:inline-block; padding:4px 10px; border-radius:3px; margin-bottom:8px;">
                {division}
              </div>
              <h1 class="PageHeroBanner_title__2XMBn" data-backgroundcolor="white">{dept_name}</h1>
            </div>
          </section>
        </section>

        <!-- Two Column Main Body -->
        <section class="twocol">
          <!-- Left Navigation -->
          <div class="twocol-small">
            <nav class="LeftNav_container__1eaqi">
              <ul class="LeftNav_list__1Ii30" data-navlevel="L1">
                <li class="LeftNav_listItem__3uwaS"><a class="LeftNav_listItemAction__3GY3m" href="academics_schools-and-divisions.html"><span class="linkText">Schools and Divisions</span></a></li>
                <li class="LeftNav_listItem__3uwaS"><a class="LeftNav_listItemAction__3GY3m" href="academics_academic-departments.html"><span class="linkText">Academic Departments</span></a></li>
                <li class="LeftNav_listItem__3uwaS" style="background:#f7f7f7; border-left:3px solid #800000;"><a class="LeftNav_listItemAction__3GY3m" href="{dept_id}.html" style="color:#800000; font-weight:700;"><span class="linkText">{dept_name}</span></a></li>
                <li class="LeftNav_listItem__3uwaS"><a class="LeftNav_listItemAction__3GY3m" href="#faculty" style="color:#333;"><span class="linkText"><i class="fa-solid fa-user-group" style="margin-right:6px; color:#800000; font-size:11px;"></i>Faculty Directory ({faculty_count})</span></a></li>
                <li class="LeftNav_listItem__3uwaS"><a class="LeftNav_listItemAction__3GY3m" href="faculty.html"><span class="linkText">All University Faculty</span></a></li>
              </ul>
            </nav>

            <section class="SubNavRelatedLinks_subNavContainer__1PSrH">
              <p class="SubNavRelatedLinks_title__32HKs">Department Links</p>
              <div class="SubNavRelatedLinks_innerContainer__13yxZ">
                <ul class="SubNavRelatedLinks_list__2TZSs">
                  <li class="SubNavRelatedLinks_listItem__1oKUp"><a class="SubNavRelatedLinks_listItemLink__37RUX" data-chevron="true" href="#faculty" style="font-weight:700; color:#1a1a1a;"><span class="linkText"><i class="fa-solid fa-user-graduate" style="margin-right:4px; color:#800000;"></i>Faculty Directory ({faculty_count})</span></a></li>
                  <li class="SubNavRelatedLinks_listItem__1oKUp"><a class="SubNavRelatedLinks_listItemLink__37RUX" data-chevron="true" href="../portal.html" style="font-weight:700; color:#800000;"><span class="linkText"><i class="fa-solid fa-lock" style="margin-right:4px;"></i>Ph.D. Applicant Portal</span></a></li>
                  <li class="SubNavRelatedLinks_listItem__1oKUp"><a class="SubNavRelatedLinks_listItemLink__37RUX" data-chevron="true" href="#programs"><span class="linkText">Graduate &amp; Undergrad Degrees</span></a></li>
                  <li class="SubNavRelatedLinks_listItem__1oKUp"><a class="SubNavRelatedLinks_listItemLink__37RUX" data-chevron="true" href="#research"><span class="linkText">Research Labs &amp; Centers</span></a></li>
                  <li class="SubNavRelatedLinks_listItem__1oKUp"><a class="SubNavRelatedLinks_listItemLink__37RUX" data-chevron="true" href="academics_academic-calendar.html"><span class="linkText">Academic Calendar</span></a></li>
                  <li class="SubNavRelatedLinks_listItem__1oKUp"><a class="SubNavRelatedLinks_listItemLink__37RUX" data-chevron="true" href="visit.html"><span class="linkText">Visit Hyde Park Campus</span></a></li>
                </ul>
              </div>
            </section>
          </div>

          <!-- Right Content Area -->
          <div class="twocol-large">
            
            <!-- Quick Anchor Navigation Tabs -->
            <div class="dept-quicktabs">
              <a href="#overview" class="dept-tab-btn">Overview</a>
              <a href="#programs" class="dept-tab-btn">Degree Programs</a>
              <a href="#research" class="dept-tab-btn">Research Areas</a>
              <a href="#facilities" class="dept-tab-btn">Facilities</a>
              <a href="#faculty" class="dept-tab-btn">Faculty ({faculty_count})</a>
              <a href="#events" class="dept-tab-btn">Events</a>
              <a href="#contact" class="dept-tab-btn">Contact</a>
            </div>

            <!-- Overview Section -->
            <div id="overview">
              <section class="HeadlineTextBold_container__1OGJ8 single-col-inner" data-alignment="left" style="margin-bottom:16px;">
                <h2 class="HeadlineTextBold_title__J6Fj_" style="font-size:28px; line-height:1.25; color:#111;">{tagline}</h2>
              </section>

              <div class="richtext" style="font-size:15px; line-height:1.7; color:#333;">
                <p>
                  {description}
                </p>

                {highlights_html}
              </div>
            </div>

            <!-- Academic Degree Programs -->
            <div id="programs" style="scroll-margin-top:100px; margin-top:36px; padding-top:20px; border-top:1px solid #e0e0e0;">
              <h3 style="font-family:'UChicagoSerif', Georgia, serif; font-size:24px; color:#1a1a1a; margin-bottom:16px; font-weight:700;">
                Academic Degree Programs
              </h3>

              <!-- Undergraduate Program -->
              {undergrad_html}

              <!-- Master's Program -->
              {masters_html}

              <!-- Doctoral (Ph.D.) Program -->
              <div style="background:#fff9f9; border:1px solid #e8bcbc; border-left:4px solid #800000; padding:20px 22px; margin-bottom:20px; border-radius:0 4px 4px 0;">
                <div style="display:flex; justify-content:space-between; align-items:baseline; flex-wrap:wrap; margin-bottom:8px;">
                  <h4 style="font-family:'UChicagoSerif', Georgia, serif; font-size:19px; color:#800000; margin:0; font-weight:700;">
                    Doctor of Philosophy (Ph.D.) Program
                  </h4>
                  <span style="font-size:12px; font-weight:700; color:#800000; background:#f5dede; padding:3px 8px; border-radius:3px;">
                    Full Fellowship Funding
                  </span>
                </div>
                <p style="font-size:14.5px; line-height:1.6; color:#333; margin:0 0 14px 0;">
                  {phd if phd else f"The doctoral program in {dept_name} is designed to cultivate innovative research scholars. Graduate candidates engage in original research supported by rigorous departmental coursework, faculty mentorship, and comprehensive multi-year financial packages."}
                </p>
                <div style="background:#fff; border:1px solid #eed0d0; padding:12px 16px; border-radius:4px; font-size:13.5px; line-height:1.6; margin-bottom:16px;">
                  <div style="font-weight:700; color:#800000; margin-bottom:4px;"><i class="fa fa-shield-alt" style="margin-right:6px;"></i>Guaranteed 5-Year Doctoral Fellowship Package:</div>
                  <ul style="margin:0; padding-left:18px; color:#444;">
                    <li>100% Full Tuition Remission covered by the University</li>
                    <li>Competitive Annual Living Stipend ($44,000+ per year)</li>
                    <li>Comprehensive UChicago Student Health Insurance (U-SHIP)</li>
                    <li>Guaranteed research assistantship and travel conference grants</li>
                  </ul>
                </div>
                <div style="display:flex; gap:12px; align-items:center; flex-wrap:wrap;">
                  <a href="../portal.html" style="background:#800000; color:#fff; text-decoration:none; padding:8px 18px; border-radius:4px; font-weight:700; font-size:13.5px; display:inline-flex; align-items:center; gap:6px;">
                    <i class="fa fa-lock"></i> Apply via Applicant Portal &rarr;
                  </a>
                  <span style="font-size:13px; color:#666;">
                    Applications for Autumn 2027 matriculation now open.
                  </span>
                </div>
              </div>
            </div>

            <!-- Research Areas -->
            {research_areas_html}

            <!-- Facilities -->
            {facilities_html}

            <!-- Department Faculty Directory Section -->
            <div id="faculty" style="scroll-margin-top:100px; margin-top:40px; border-top:3px solid #800000; padding-top:28px;">
              <div style="display:flex; justify-content:space-between; align-items:baseline; flex-wrap:wrap; margin-bottom:20px;">
                <div>
                  <div style="font-family:'UChicagoSansSerif-Bold', sans-serif; font-size:12.5px; color:#800000; text-transform:uppercase; letter-spacing:1px; font-weight:700;">
                    {division} &bull; The University of Chicago
                  </div>
                  <h2 style="font-family:'UChicagoSerif', Georgia, serif; font-size:30px; color:#111; margin:6px 0 8px 0; font-weight:700;">
                    {dept_name} Faculty
                  </h2>
                </div>
                <div style="font-size:13.5px; color:#444; background:#f7f7f7; padding:6px 14px; border-radius:4px; border:1px solid #e0e0e0;">
                  <i class="fa-solid fa-users" style="color:#800000; margin-right:6px;"></i> <strong>{faculty_count} Active Faculty Profiles</strong>
                </div>
              </div>

              <p style="font-size:14.5px; line-height:1.6; color:#444; margin-bottom:24px;">
                Our faculty members are world-leading thinkers, mentors, and scholars in {dept_name}. Click any professor's profile to inspect biographical narratives, research specializations, laboratory affiliations, and selected publications.
              </p>

              <!-- Faculty Cards List -->
              <div class="faculty-cards-container">
                {faculty_cards_str}
              </div>

              <div style="text-align:center; padding:16px 0; margin-top:10px;">
                <a href="faculty.html" style="color:#800000; font-weight:700; text-decoration:underline; font-size:14px;">
                  Explore All 140+ University of Chicago Faculty Across All Divisions &rarr;
                </a>
              </div>
            </div>

            <!-- Events Section -->
            {events_html}

            <!-- Contact Box -->
            {contact_box_html}

            <!-- Bottom Admissions CTA -->
            <div style="background:#800000; color:#fff; padding:28px 32px; border-radius:6px; margin-top:40px; display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:16px;">
              <div>
                <h3 style="font-family:'UChicagoSerif', Georgia, serif; font-size:22px; color:#fff; margin:0 0 6px 0; font-weight:700;">
                  Ready to Shape the Future with {dept_name}?
                </h3>
                <p style="margin:0; font-size:14.5px; color:#f0d0d0; max-width:550px;">
                  Explore our undergraduate concentrations, master's curricula, and fully-funded Ph.D. fellowships. Access application instructions, deadlines, and portal status.
                </p>
              </div>
              <div>
                <a href="../portal.html" style="background:#fff; color:#800000; text-decoration:none; padding:10px 22px; border-radius:4px; font-weight:700; font-size:14px; display:inline-block;">
                  Access Applicant Portal &rarr;
                </a>
              </div>
            </div>

          </div>
        </section>
      </div>
    </main>

    <!-- Modal Dialog -->
    <div id="facultyModal" class="faculty-modal-overlay" role="dialog" aria-modal="true">
      <div class="faculty-modal-card">
        <button class="faculty-modal-close" onclick="closeFacultyModal()" aria-label="Close modal">&times;</button>
        <div id="facultyModalBody"></div>
      </div>
    </div>

    <!-- Footer -->
    <footer class="Footer_container__2FhK_">
      <div class="single-col-inner">
        <div class="Footer_topContainer__3dKx4">
          <div class="Footer_leftCol__3qE_5">
            <a class="Footer_logoLink__2rZ5m" href="../index.html">
              <img alt="The University of Chicago" class="Footer_logo__1S719" src="../assets/logo-background.svg" />
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
              <li><a href="who-we-are.html">Who We Are</a></li>
              <li><a href="academics.html">Academics</a></li>
              <li><a href="academics_academic-departments.html">Academic Departments</a></li>
              <li><a href="faculty.html">Faculty Directory</a></li>
              <li><a href="research-and-scholarship.html">Research &amp; Scholarship</a></li>
              <li><a href="admissions.html">Admissions &amp; Aid</a></li>
              <li><a href="../portal.html">Applicant Portal</a></li>
            </ul>
          </div>
        </div>
        <div class="Footer_bottomContainer__2_e1O">
          <p class="Footer_copyright__3rD-u">&copy; 2026 The University of Chicago. All rights reserved.</p>
        </div>
      </div>
    </footer>
  </div>

  <!-- Faculty Data JSON & Script for Modals & Mobile Nav -->
  <script>
    var DEPT_FACULTY = {json.dumps(faculty_list, indent=2)};

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

    function openFacultyModal(id) {{
      var f = DEPT_FACULTY.find(function(item) {{ return item.id === id; }});
      if (!f) return;

      var initials = getInitials(f.name);
      var photoSrc = f.photo ? (f.photo.indexOf("../") === 0 || f.photo.indexOf("http") === 0 ? f.photo : "../" + f.photo) : "";

      var pubList = (f.publications || []).map(function(p) {{
        return "<li style='margin-bottom:6px;'>" + p + "</li>";
      }}).join("");

      var accoladesList = (f.accolades || []).map(function(a) {{
        return "<span style='display:inline-block; font-size:11.5px; font-weight:700; color:#800000; background:#f6e8e8; border:1px solid #e0bebe; padding:3px 8px; border-radius:3px; margin-right:6px; margin-bottom:6px;'>" + a + "</span>";
      }}).join("");

      var tagsList = (f.tags || []).map(function(t) {{
        return "<span style='display:inline-block; font-size:12px; color:#333; background:#f0f0f0; border:1px solid #ddd; padding:3px 8px; border-radius:3px; margin-right:6px; margin-bottom:6px;'>" + t + "</span>";
      }}).join("");

      var html = `
        <div style="display:flex; gap:20px; align-items:flex-start; margin-bottom:20px; border-bottom:1px solid #eee; padding-bottom:18px;">
          <div style="width:110px; height:135px; flex-shrink:0; background:#800000; border-radius:4px; overflow:hidden;">
            ${{photoSrc ? `
              <img src="${{photoSrc}}" alt="${{f.name}}" style="width:100%; height:100%; object-fit:cover;" onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';">
              <div style="display:none; width:100%; height:100%; background:#800000; color:#fff; font-family:'UChicagoSerif', Georgia, serif; font-size:36px; font-weight:700; align-items:center; justify-content:center;">${{initials}}</div>
            ` : `
              <div style="display:flex; width:100%; height:100%; background:#800000; color:#fff; font-family:'UChicagoSerif', Georgia, serif; font-size:36px; font-weight:700; align-items:center; justify-content:center;">${{initials}}</div>
            `}}
          </div>
          <div>
            <div style="font-size:12px; font-weight:700; color:#800000; text-transform:uppercase; letter-spacing:0.5px; margin-bottom:4px;">
              ${{f.domainLabel}} &bull; ${{f.department}}
            </div>
            <h2 style="font-family:'UChicagoSerif', Georgia, serif; font-size:24px; color:#1a1a1a; margin:0 0 6px 0; font-weight:700;">
              ${{f.name}}
            </h2>
            <div style="font-size:14px; font-weight:600; color:#444; margin-bottom:4px;">${{f.title}}</div>
            <div style="font-size:13px; color:#666; margin-bottom:10px;">${{f.degrees || ''}}</div>
            <div>${{accoladesList}}</div>
          </div>
        </div>

        <div style="font-size:14.5px; line-height:1.65; color:#222; margin-bottom:20px;">
          <h4 style="font-family:'UChicagoSerif', Georgia, serif; font-size:16px; margin:0 0 8px 0; color:#1a1a1a; font-weight:700;">Biography &amp; Scholarship</h4>
          <p style="margin:0;">${{f.bio}}</p>
        </div>

        ${{tagsList ? `
          <div style="margin-bottom:20px;">
            <h4 style="font-family:'UChicagoSerif', Georgia, serif; font-size:16px; margin:0 0 8px 0; color:#1a1a1a; font-weight:700;">Research Specializations</h4>
            <div>${{tagsList}}</div>
          </div>
        ` : ''}}

        ${{pubList ? `
          <div style="margin-bottom:20px;">
            <h4 style="font-family:'UChicagoSerif', Georgia, serif; font-size:16px; margin:0 0 8px 0; color:#1a1a1a; font-weight:700;">Selected Publications</h4>
            <ul style="margin:0; padding-left:20px; font-size:13.5px; line-height:1.6; color:#333;">${{pubList}}</ul>
          </div>
        ` : ''}}

        <div style="background:#f8f8f8; border:1px solid #e5e5e5; padding:14px 18px; border-radius:4px; font-size:13.5px; line-height:1.6;">
          <h4 style="font-family:'UChicagoSerif', Georgia, serif; font-size:15px; margin:0 0 6px 0; color:#1a1a1a; font-weight:700;">Campus Contact</h4>
          ${{f.office ? `<div><strong>Office:</strong> ${{f.office}}</div>` : ''}}
          ${{f.email ? `<div><strong>Email:</strong> <a href="mailto:${{f.email}}" style="color:#800000; font-weight:600;">${{f.email}}</a></div>` : ''}}
          ${{f.lab ? `<div style="margin-top:6px;"><a href="${{f.lab}}" target="_blank" rel="noopener noreferrer" style="color:#800000; font-weight:600; text-decoration:underline;">Visit Lab / Personal Website &rarr;</a></div>` : ''}}
        </div>
      `;

      document.getElementById("facultyModalBody").innerHTML = html;
      document.getElementById("facultyModal").classList.add("is-active");
    }}

    function closeFacultyModal() {{
      document.getElementById("facultyModal").classList.remove("is-active");
    }}

    document.getElementById("facultyModal").addEventListener("click", function(e) {{
      if (e.target === this) {{
        closeFacultyModal();
      }}
    }});

    document.addEventListener("keydown", function(e) {{
      if (e.key === "Escape") {{
        closeFacultyModal();
      }}
    }});

    // Mobile Navigation Toggle
    var mobileToggle = document.getElementById("mobileTogBtn");
    var headerEl = document.getElementById("header");
    if (mobileToggle && headerEl) {{
      mobileToggle.addEventListener("click", function () {{
        var isOpen = headerEl.getAttribute("data-mobilenavisopen") === "true";
        headerEl.setAttribute("data-mobilenavisopen", !isOpen ? "true" : "false");
        mobileToggle.setAttribute("aria-expanded", !isOpen ? "true" : "false");
      }});
    }}
  </script>
</body>
</html>
'''
    return html_content

def generate_all():
    print(f"Generating departmental pages for {len(DEPARTMENTS)} departments...")
    for dept in DEPARTMENTS:
        slug = dept["id"]
        out_path = os.path.join(PAGES_DIR, f"{slug}.html")
        html = build_department_page(dept)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Generated: {slug}.html")
    print("All departmental subpages generated successfully!")

if __name__ == "__main__":
    generate_all()
