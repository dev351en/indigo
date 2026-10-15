import re

date_block = '''          <!-- Key Program Dates -->
          <div class="portal-sidebar-card">
            <h3 class="portal-sidebar-heading">
              <i class="fa-solid fa-calendar-days" style="color: maroon;"></i> Key Program Dates
            </h3>
            <ul class="portal-date-list">
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

def update_dates(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Match existing date block
    m = re.search(r'<!-- Key Program Dates.*?</ul>\s*</div>', content, re.DOTALL)
    if m:
        content = content[:m.start()] + date_block + content[m.end():]
        print(f"[{filepath}] Updated date block.")
    else:
        print(f"[{filepath}] Date block not found!")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

update_dates(r'd:\Microvirt\OBSIDIAN\uchicago_replica\site_1to1\portal.html')
update_dates(r'd:\Microvirt\OBSIDIAN\uchicago_replica\site_1to1\pages\portal.html')
