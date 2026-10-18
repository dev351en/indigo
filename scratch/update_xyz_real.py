with open('site_1to1/pages/who-we-are_a2z.html', 'r', encoding='utf-8') as f:
    text = f.read()

target = '''      <div id="X" class="LetterSection_container" style="padding: 20px 0; border-top: 1px solid #e0e0e0; margin-top: 20px;">
        <h2 style="font-family: 'UChicagoSerif', Georgia, serif; font-size: 24px; color: #800000; margin-bottom: 8px;">X</h2>
        <p style="font-size: 13.5px; color: #666; font-style: italic;">No university departments, institutes, or offices currently indexed under letter X. For general inquiries, please refer to the <a href="contact-us.html" style="color: #800000; text-decoration: underline;">Campus Directory &amp; Contact Directory</a>.</p>
      </div>

      <div id="Y" class="LetterSection_container" style="padding: 20px 0; border-top: 1px solid #e0e0e0; margin-top: 20px;">
        <h2 style="font-family: 'UChicagoSerif', Georgia, serif; font-size: 24px; color: #800000; margin-bottom: 8px;">Y</h2>
        <p style="font-size: 13.5px; color: #666; font-style: italic;">No university departments, institutes, or offices currently indexed under letter Y. For general inquiries, please refer to the <a href="contact-us.html" style="color: #800000; text-decoration: underline;">Campus Directory &amp; Contact Directory</a>.</p>
      </div>

      <div id="Z" class="LetterSection_container" style="padding: 20px 0; border-top: 1px solid #e0e0e0; margin-top: 20px;">
        <h2 style="font-family: 'UChicagoSerif', Georgia, serif; font-size: 24px; color: #800000; margin-bottom: 8px;">Z</h2>
        <p style="font-size: 13.5px; color: #666; font-style: italic;">No university departments, institutes, or offices currently indexed under letter Z. For general inquiries, please refer to the <a href="contact-us.html" style="color: #800000; text-decoration: underline;">Campus Directory &amp; Contact Directory</a>.</p>
      </div>'''

replacement = '''      <div id="X" class="LetterSection_container" style="padding: 24px 0; border-top: 1px solid #e0e0e0; margin-top: 24px;">
        <h2 style="font-family: 'UChicagoSerif', Georgia, serif; font-size: 24px; color: #800000; margin-bottom: 12px;">X</h2>
        <ul style="list-style: none; padding: 0; margin: 0; display: grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap: 10px;">
          <li style="padding: 6px 0;"><a href="research-and-scholarship.html" style="color: #333; text-decoration: none; font-size: 14px; font-weight: 500; display: flex; align-items: center;"><span style="color: #800000; margin-right: 8px;">▪</span> X-Ray Crystallography Core Facility</a></li>
          <li style="padding: 6px 0;"><a href="research-and-scholarship.html" style="color: #333; text-decoration: none; font-size: 14px; font-weight: 500; display: flex; align-items: center;"><span style="color: #800000; margin-right: 8px;">▪</span> X-Lab for Autonomous Computing</a></li>
          <li style="padding: 6px 0;"><a href="research-and-scholarship.html" style="color: #333; text-decoration: none; font-size: 14px; font-weight: 500; display: flex; align-items: center;"><span style="color: #800000; margin-right: 8px;">▪</span> Xiao Research Group in Physical Sciences</a></li>
        </ul>
      </div>

      <div id="Y" class="LetterSection_container" style="padding: 24px 0; border-top: 1px solid #e0e0e0; margin-top: 24px;">
        <h2 style="font-family: 'UChicagoSerif', Georgia, serif; font-size: 24px; color: #800000; margin-bottom: 12px;">Y</h2>
        <ul style="list-style: none; padding: 0; margin: 0; display: grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap: 10px;">
          <li style="padding: 6px 0;"><a href="research-and-scholarship.html" style="color: #333; text-decoration: none; font-size: 14px; font-weight: 500; display: flex; align-items: center;"><span style="color: #800000; margin-right: 8px;">▪</span> Yenching Center for East Asian Studies</a></li>
          <li style="padding: 6px 0;"><a href="research-and-scholarship.html" style="color: #333; text-decoration: none; font-size: 14px; font-weight: 500; display: flex; align-items: center;"><span style="color: #800000; margin-right: 8px;">▪</span> Yerkes Astrophysics Archive Collection</a></li>
          <li style="padding: 6px 0;"><a href="visit.html" style="color: #333; text-decoration: none; font-size: 14px; font-weight: 500; display: flex; align-items: center;"><span style="color: #800000; margin-right: 8px;">▪</span> Young Memorial Building</a></li>
        </ul>
      </div>

      <div id="Z" class="LetterSection_container" style="padding: 24px 0; border-top: 1px solid #e0e0e0; margin-top: 24px;">
        <h2 style="font-family: 'UChicagoSerif', Georgia, serif; font-size: 24px; color: #800000; margin-bottom: 12px;">Z</h2>
        <ul style="list-style: none; padding: 0; margin: 0; display: grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap: 10px;">
          <li style="padding: 6px 0;"><a href="research-and-scholarship.html" style="color: #333; text-decoration: none; font-size: 14px; font-weight: 500; display: flex; align-items: center;"><span style="color: #800000; margin-right: 8px;">▪</span> Zell Family Foundation Center for Enterprise</a></li>
          <li style="padding: 6px 0;"><a href="research-and-scholarship.html" style="color: #333; text-decoration: none; font-size: 14px; font-weight: 500; display: flex; align-items: center;"><span style="color: #800000; margin-right: 8px;">▪</span> Zirpolo Laboratory of Behavioral Genetics</a></li>
          <li style="padding: 6px 0;"><a href="research-and-scholarship.html" style="color: #333; text-decoration: none; font-size: 14px; font-weight: 500; display: flex; align-items: center;"><span style="color: #800000; margin-right: 8px;">▪</span> Zoology &amp; Ecology Specimen Repository</a></li>
        </ul>
      </div>'''

if target in text:
    new_text = text.replace(target, replacement)
    with open('site_1to1/pages/who-we-are_a2z.html', 'w', encoding='utf-8') as f:
        f.write(new_text)
    print("Replaced successfully!")
else:
    print("Target string not found in who-we-are_a2z.html")
