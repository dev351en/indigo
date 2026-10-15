with open(r'd:\Microvirt\OBSIDIAN\uchicago_replica\site_1to1\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_desc = 'To reserve and officially lock your graduate research seat in the <strong>Computational Chemistry Doctoral Program</strong> for the Autumn Quarter 2027 (commencing August 2027), please complete the required enrollment deposit below.'
new_desc = 'To reserve and officially lock your graduate research seat in the <strong>Computational Chemistry Doctoral Program</strong> for the Autumn Quarter 2027 (commencing August 2027), please complete the required enrollment deposit below by the <strong>Seat locking fee Deposit Priority Deadline: Nov 15, 2026</strong>.'

content = content.replace(old_desc, new_desc)

# Also add key dates card if not present in index.html
if 'Key Program Dates' not in content:
    dates_card = '''      <!-- Key Program Dates Card -->
      <div style="background: #faf8f5; border: 1px solid #e5ded5; padding: 14px 18px; border-radius: 4px; margin-bottom: 16px;">
        <h4 style="margin: 0 0 10px 0; font-family: 'UChicagoSansSerif-Bold', sans-serif; font-size: 13px; text-transform: uppercase; color: maroon; letter-spacing: 0.5px;">
          <i class="fa-solid fa-calendar-days" style="margin-right: 6px;"></i> Key Program Dates
        </h4>
        <ul class="portal-date-list" style="margin: 0; padding: 0; list-style: none;">
          <li class="portal-date-item">
            <span class="portal-date-label">Seat locking fee Deposit Priority Deadline</span>
            <span class="portal-date-val" style="color: #b91c1c; font-weight: 700;">Nov 15, 2026</span>
          </li>
          <li class="portal-date-item">
            <span class="portal-date-label">Fellowship Stipend Setup</span>
            <span class="portal-date-val">AUG 15, 2027</span>
          </li>
          <li class="portal-date-item">
            <span class="portal-date-label">Doctoral Matriculation &amp; Move-In</span>
            <span class="portal-date-val">August 2027</span>
          </li>
          <li class="portal-date-item">
            <span class="portal-date-label">PSD Graduate Orientation</span>
            <span class="portal-date-val">September 2027</span>
          </li>
          <li class="portal-date-item">
            <span class="portal-date-label">Autumn Quarter Classes Begin</span>
            <span class="portal-date-val">September 2027</span>
          </li>
        </ul>
      </div>'''
    marker = '<!-- Dedicated Full Page Portal Link -->'
    content = content.replace(marker, dates_card + '\n\n      ' + marker)

with open(r'd:\Microvirt\OBSIDIAN\uchicago_replica\site_1to1\index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated dates in index.html")
