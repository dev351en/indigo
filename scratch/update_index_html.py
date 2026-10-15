import re
import json

with open("site_1to1/index.html", "r", encoding="utf-8") as f:
    html = f.read()

print("Original HTML length:", len(html))

# 1. Update News images in ul.NewsFeatured_newsList__19dBn
news_images = [
    ("125716.png", "Michael Dean Woodford"),
    ("125703.jpg", "The launch vehicle carries PUEO"),
    ("125710.png", "A scientist ladles vapor from a steaming container"),
    ("125702.png", "Five books with page side visible chained together with a padlock")
]

# Find the 4 NewsItem_image spans in NewsFeatured
news_span_pattern = r'<span class="NewsItem_image__3ztUc"[^>]*></span>'
matches = list(re.finditer(news_span_pattern, html))
print(f"Found {len(matches)} empty NewsItem_image spans.")

if len(matches) == 4:
    # Replace from back to front
    for i in reversed(range(4)):
        m = matches[i]
        img_file, alt = news_images[i]
        replacement = f'<span class="NewsItem_image__3ztUc" style="display:block;overflow:hidden;border-radius:4px 4px 0 0;height:180px;"><img src="assets/homepage_media/{img_file}" alt="{alt}" style="width:100%;height:100%;object-fit:cover;display:block;" /></span>'
        html = html[:m.start()] + replacement + html[m.end():]
    print("Updated 4 NewsItem images!")

# 2. First PhotoTabs (Harper Memorial Library)
# Target: <section class="PhotoTabs_container__pDqWQ single-col-inner"><span class="" style="display:inline-block"></span></section>
photo_tabs_pattern = r'<section class="PhotoTabs_container__pDqWQ single-col-inner"><span class="" style="display:inline-block"></span></section>'
pt_matches = list(re.finditer(photo_tabs_pattern, html))
print(f"Found {len(pt_matches)} empty PhotoTabs sections.")

harper_html = '''<section class="PhotoTabs_container__pDqWQ single-col-inner" style="display:flex;flex-wrap:wrap;margin:40px auto;background:#fff;box-shadow:0 2px 12px rgba(0,0,0,0.06);border-radius:4px;overflow:hidden;">
  <div class="PhotoTabs_imageContainer__3afCy" style="flex:1 1 50%;min-height:420px;background-image:url(assets/homepage_media/harper-crop-3.jpg);background-size:cover;background-position:center;position:relative;">
    <div class="PhotoTabs_tabDescription__muXEe" style="position:absolute;bottom:0;left:0;right:0;background:rgba(0,0,0,0.65);color:#fff;padding:12px 18px;">
      <p class="PhotoTabs_description__2TV3C" style="margin:0;font-size:14px;color:#fff;">Harper Memorial Library</p>
    </div>
  </div>
  <div class="PhotoTabs_tabContainer__1PBt-" style="flex:1 1 50%;padding:48px 40px;display:flex;flex-direction:column;justify-content:center;">
    <h2 class="PhotoTabs_title__2KMpI" style="font-family:'UChicagoSerif',Georgia,serif;font-size:32px;line-height:1.25;color:#1a1a1a;margin-bottom:16px;">An atmosphere of free and boundless inquiry</h2>
    <p class="PhotoTabs_description__2TV3C" style="font-size:16px;line-height:1.6;color:#555;margin-bottom:24px;">We empower individuals to challenge conventional thinking in pursuit of original ideas. Students learn in the College, graduate programs, and professional schools to become the next generation of leaders in academia, business, government, and society.</p>
    <div class="PhotoTabs_ctaLinkContainer__3RJ9i">
      <a href="pages/academics.html" class="PhotoTabs_ctaLink__20nZX" style="display:inline-block;padding:10px 22px;background:#800000;color:#fff;text-decoration:none;font-weight:600;font-size:14px;border-radius:2px;letter-spacing:0.5px;text-transform:uppercase;">
        <span class="linkText">Explore Academics &rarr;</span>
      </a>
    </div>
  </div>
</section>'''

welcome_html = '''<section class="PhotoTabs_container__pDqWQ single-col-inner" style="display:flex;flex-wrap:wrap;margin:40px auto;background:#fff;box-shadow:0 2px 12px rgba(0,0,0,0.06);border-radius:4px;overflow:hidden;">
  <div class="PhotoTabs_tabContainer__1PBt-" style="flex:1 1 50%;padding:48px 40px;display:flex;flex-direction:column;justify-content:center;">
    <h2 class="PhotoTabs_title__2KMpI" style="font-family:'UChicagoSerif',Georgia,serif;font-size:32px;line-height:1.25;color:#1a1a1a;margin-bottom:16px;">We welcome all</h2>
    <p class="PhotoTabs_description__2TV3C" style="font-size:16px;line-height:1.6;color:#555;margin-bottom:24px;">Only when different values, experiences, and perspectives are met with free and open discourse can education be truly transformative. This is why we continue to work together as an institution, and within our community, to promote a more inclusive environment on our campus and beyond.</p>
    <div class="PhotoTabs_ctaLinkContainer__3RJ9i">
      <a href="pages/life-at-uchicago_diversity.html" class="PhotoTabs_ctaLink__20nZX" style="display:inline-block;padding:10px 22px;background:#800000;color:#fff;text-decoration:none;font-weight:600;font-size:14px;border-radius:2px;letter-spacing:0.5px;text-transform:uppercase;">
        <span class="linkText">Learn more &rarr;</span>
      </a>
    </div>
  </div>
  <div class="PhotoTabs_imageContainer__3afCy" style="flex:1 1 50%;min-height:420px;background-image:url(assets/homepage_media/we-welcome-all.jpg);background-size:cover;background-position:center;position:relative;">
    <div class="PhotoTabs_tabDescription__muXEe" style="position:absolute;bottom:0;left:0;right:0;background:rgba(0,0,0,0.65);color:#fff;padding:12px 18px;">
      <p class="PhotoTabs_description__2TV3C" style="margin:0;font-size:14px;color:#fff;">We Welcome All</p>
    </div>
  </div>
</section>'''

if len(pt_matches) >= 2:
    # replace second first
    html = html[:pt_matches[1].start()] + welcome_html + html[pt_matches[1].end():]
    # replace first
    html = html[:pt_matches[0].start()] + harper_html + html[pt_matches[0].end():]
    print("Replaced both PhotoTabs sections!")
elif len(pt_matches) == 1:
    html = html[:pt_matches[0].start()] + harper_html + html[pt_matches[0].end():]
    print("Replaced 1 PhotoTabs section!")

# 3. First ImageTileGrid (Scholars & Breakthroughs)
# Target: <section class="ImageTileGrid_container__3qHJn single-col-inner"><span class="" style="display:inline-block"></span></section>
grid_pattern = r'<section class="ImageTileGrid_container__3qHJn single-col-inner"><span class="" style="display:inline-block"></span></section>'
grid_matches = list(re.finditer(grid_pattern, html))
print(f"Found {len(grid_matches)} empty ImageTileGrid sections.")

research_grid_html = '''<section class="ImageTileGrid_container__3qHJn single-col-inner" style="margin:36px auto;">
  <div class="ImageTileGrid_imageTileGrid__GcImq">
    <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(260px, 1fr));gap:20px;">
      <div style="position:relative;height:360px;border-radius:4px;overflow:hidden;box-shadow:0 4px 14px rgba(0,0,0,0.12);group;">
        <img src="assets/homepage_media/bookofdead.jpg" alt="Alison Whyte works on a mummy for an exhibit" style="width:100%;height:100%;object-fit:cover;display:block;" />
        <div style="position:absolute;inset:0;background:linear-gradient(to top, rgba(128,0,0,0.92) 0%, rgba(128,0,0,0.6) 50%, rgba(0,0,0,0.1) 100%);color:#fff;padding:20px;display:flex;flex-direction:column;justify-content:flex-end;">
          <h4 style="font-size:17px;font-weight:700;margin:0 0 8px 0;color:#fff;">Archaeological Excavations</h4>
          <p style="font-size:13px;line-height:1.45;color:#f0f0f0;margin:0;">UChicago scholars have led excavations around the world, enriching our understanding of human civilization.</p>
        </div>
      </div>
      <div style="position:relative;height:360px;border-radius:4px;overflow:hidden;box-shadow:0 4px 14px rgba(0,0,0,0.12);">
        <img src="assets/homepage_media/ashlynsparrow.jpg" alt="Ashlyn Sparrow" style="width:100%;height:100%;object-fit:cover;display:block;" />
        <div style="position:absolute;inset:0;background:linear-gradient(to top, rgba(128,0,0,0.92) 0%, rgba(128,0,0,0.6) 50%, rgba(0,0,0,0.1) 100%);color:#fff;padding:20px;display:flex;flex-direction:column;justify-content:flex-end;">
          <h4 style="font-size:17px;font-weight:700;margin:0 0 8px 0;color:#fff;">Weston Game Lab</h4>
          <p style="font-size:13px;line-height:1.45;color:#f0f0f0;margin:0;">Bringing scholars together to explore the artistic, cultural, and technological aspects of gaming.</p>
        </div>
      </div>
      <div style="position:relative;height:360px;border-radius:4px;overflow:hidden;box-shadow:0 4px 14px rgba(0,0,0,0.12);">
        <img src="assets/homepage_media/rogers-2-crop.jpg" alt="Selwyn Rogers" style="width:100%;height:100%;object-fit:cover;display:block;" />
        <div style="position:absolute;inset:0;background:linear-gradient(to top, rgba(128,0,0,0.92) 0%, rgba(128,0,0,0.6) 50%, rgba(0,0,0,0.1) 100%);color:#fff;padding:20px;display:flex;flex-direction:column;justify-content:flex-end;">
          <h4 style="font-size:17px;font-weight:700;margin:0 0 8px 0;color:#fff;">UChicago Trauma Center</h4>
          <p style="font-size:13px;line-height:1.45;color:#f0f0f0;margin:0;">A state-of-the-art facility serving the health needs of the South Side of Chicago and beyond.</p>
        </div>
      </div>
      <div style="position:relative;height:360px;border-radius:4px;overflow:hidden;box-shadow:0 4px 14px rgba(0,0,0,0.12);">
        <img src="assets/homepage_media/chemist-at-uchicago.jpg" alt="UChicago Chemist" style="width:100%;height:100%;object-fit:cover;display:block;" />
        <div style="position:absolute;inset:0;background:linear-gradient(to top, rgba(128,0,0,0.92) 0%, rgba(128,0,0,0.6) 50%, rgba(0,0,0,0.1) 100%);color:#fff;padding:20px;display:flex;flex-direction:column;justify-content:flex-end;">
          <h4 style="font-size:17px;font-weight:700;margin:0 0 8px 0;color:#fff;">Field-Defining Discoveries</h4>
          <p style="font-size:13px;line-height:1.45;color:#f0f0f0;margin:0;">Scholars at the forefront of breakthroughs and innovative research across chemical sciences.</p>
        </div>
      </div>
      <div style="position:relative;height:360px;border-radius:4px;overflow:hidden;box-shadow:0 4px 14px rgba(0,0,0,0.12);">
        <img src="assets/homepage_media/www-handmorph.jpg" alt="Handmorph" style="width:100%;height:100%;object-fit:cover;display:block;" />
        <div style="position:absolute;inset:0;background:linear-gradient(to top, rgba(128,0,0,0.92) 0%, rgba(128,0,0,0.6) 50%, rgba(0,0,0,0.1) 100%);color:#fff;padding:20px;display:flex;flex-direction:column;justify-content:flex-end;">
          <h4 style="font-size:17px;font-weight:700;margin:0 0 8px 0;color:#fff;">Human Computer Integration</h4>
          <p style="font-size:13px;line-height:1.45;color:#f0f0f0;margin:0;">Solving frontier questions through wearable technology, augmented robotics, and haptics.</p>
        </div>
      </div>
    </div>
  </div>
</section>'''

chicago_grid_html = '''<section class="ImageTileGrid_container__3qHJn single-col-inner" style="margin:36px auto;">
  <div class="ImageTileGrid_imageTileGrid__GcImq">
    <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(260px, 1fr));gap:20px;">
      <div style="position:relative;height:360px;border-radius:4px;overflow:hidden;box-shadow:0 4px 14px rgba(0,0,0,0.12);">
        <img src="assets/homepage_media/city-skyline-chicago.jpg" alt="Chicago skyline" style="width:100%;height:100%;object-fit:cover;display:block;" />
        <div style="position:absolute;inset:0;background:linear-gradient(to top, rgba(0,0,0,0.85) 0%, rgba(0,0,0,0.4) 50%, transparent 100%);color:#fff;padding:20px;display:flex;flex-direction:column;justify-content:flex-end;">
          <h4 style="font-size:17px;font-weight:700;margin:0 0 8px 0;color:#fff;">Downtown &amp; Hyde Park</h4>
          <p style="font-size:13px;line-height:1.45;color:#f0f0f0;margin:0;">A short trip from downtown Chicago, offering easy access to culture, commerce, and inquiry.</p>
        </div>
      </div>
      <div style="position:relative;height:360px;border-radius:4px;overflow:hidden;box-shadow:0 4px 14px rgba(0,0,0,0.12);">
        <img src="assets/homepage_media/a-woman-in-a-sun-hat-views-art-at-the-smart-museum.jpg" alt="Smart Museum of Art" style="width:100%;height:100%;object-fit:cover;display:block;" />
        <div style="position:absolute;inset:0;background:linear-gradient(to top, rgba(0,0,0,0.85) 0%, rgba(0,0,0,0.4) 50%, transparent 100%);color:#fff;padding:20px;display:flex;flex-direction:column;justify-content:flex-end;">
          <h4 style="font-size:17px;font-weight:700;margin:0 0 8px 0;color:#fff;">Smart Museum of Art</h4>
          <p style="font-size:13px;line-height:1.45;color:#f0f0f0;margin:0;">Explore a diverse range of artwork and exhibitions at the University's premier fine arts museum.</p>
        </div>
      </div>
      <div style="position:relative;height:360px;border-radius:4px;overflow:hidden;box-shadow:0 4px 14px rgba(0,0,0,0.12);">
        <img src="assets/homepage_media/cobbgate-sized.jpg" alt="Cobb Gate" style="width:100%;height:100%;object-fit:cover;display:block;" />
        <div style="position:absolute;inset:0;background:linear-gradient(to top, rgba(0,0,0,0.85) 0%, rgba(0,0,0,0.4) 50%, transparent 100%);color:#fff;padding:20px;display:flex;flex-direction:column;justify-content:flex-end;">
          <h4 style="font-size:17px;font-weight:700;margin:0 0 8px 0;color:#fff;">Historic Cobb Gate</h4>
          <p style="font-size:13px;line-height:1.45;color:#f0f0f0;margin:0;">Gothic grotesques adorn Cobb Gate and greet visitors entering the historic campus.</p>
        </div>
      </div>
      <div style="position:relative;height:360px;border-radius:4px;overflow:hidden;box-shadow:0 4px 14px rgba(0,0,0,0.12);">
        <img src="assets/homepage_media/hyde-park-jazz-fest-couple.png" alt="Hyde Park Jazz Festival" style="width:100%;height:100%;object-fit:cover;display:block;" />
        <div style="position:absolute;inset:0;background:linear-gradient(to top, rgba(0,0,0,0.85) 0%, rgba(0,0,0,0.4) 50%, transparent 100%);color:#fff;padding:20px;display:flex;flex-direction:column;justify-content:flex-end;">
          <h4 style="font-size:17px;font-weight:700;margin:0 0 8px 0;color:#fff;">Hyde Park Arts &amp; Music</h4>
          <p style="font-size:13px;line-height:1.45;color:#f0f0f0;margin:0;">Replete with cafes, bookstores, restaurants, jazz clubs, and theatrical venues.</p>
        </div>
      </div>
      <div style="position:relative;height:360px;border-radius:4px;overflow:hidden;box-shadow:0 4px 14px rgba(0,0,0,0.12);">
        <img src="assets/homepage_media/fall-campus-quad-walk.png" alt="Students walk through the Main Quadrangles" style="width:100%;height:100%;object-fit:cover;display:block;" />
        <div style="position:absolute;inset:0;background:linear-gradient(to top, rgba(0,0,0,0.85) 0%, rgba(0,0,0,0.4) 50%, transparent 100%);color:#fff;padding:20px;display:flex;flex-direction:column;justify-content:flex-end;">
          <h4 style="font-size:17px;font-weight:700;margin:0 0 8px 0;color:#fff;">Main Quadrangles</h4>
          <p style="font-size:13px;line-height:1.45;color:#f0f0f0;margin:0;">Students walking through botanic gardens and collegiate Gothic architecture on a crisp fall day.</p>
        </div>
      </div>
    </div>
  </div>
</section>'''

if len(grid_matches) >= 2:
    html = html[:grid_matches[1].start()] + chicago_grid_html + html[grid_matches[1].end():]
    html = html[:grid_matches[0].start()] + research_grid_html + html[grid_matches[0].end():]
    print("Replaced both ImageTileGrid sections!")
elif len(grid_matches) == 1:
    html = html[:grid_matches[0].start()] + research_grid_html + html[grid_matches[0].end():]
    print("Replaced 1 ImageTileGrid section!")

# 4. Update CalloutTiles images!
# There are 5 CalloutTiles_image spans:
# First 2 are: quantum-research.png, popolvuh.jpg
# Next 3 are: breakthroughs-1952.jpg, fall-student-teacher-480-resize.jpg, hongkong480.jpg
callout_images = [
    ("quantum-research.png", "Quantum research"),
    ("popolvuh.jpg", "Popol Vuh class"),
    ("breakthroughs-1952.jpg", "The Miller-Urey experiment"),
    ("fall-student-teacher-480-resize.jpg", "A teacher works with young students"),
    ("hongkong480.jpg", "Hong Kong campus")
]

co_span_pattern = r'<span class="CalloutTiles_image__9f4H5"[^>]*></span>'
co_matches = list(re.finditer(co_span_pattern, html))
print(f"Found {len(co_matches)} empty CalloutTiles_image spans.")

if len(co_matches) == 5:
    for i in reversed(range(5)):
        m = co_matches[i]
        img_file, alt = callout_images[i]
        replacement = f'<span class="CalloutTiles_image__9f4H5" style="display:block;overflow:hidden;border-radius:4px 4px 0 0;height:240px;"><img src="assets/homepage_media/{img_file}" alt="{alt}" style="width:100%;height:100%;object-fit:cover;display:block;" /></span>'
        html = html[:m.start()] + replacement + html[m.end():]
    print("Updated 5 CalloutTiles images!")

# Write updated HTML
with open("site_1to1/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Updated site_1to1/index.html successfully! New length:", len(html))
