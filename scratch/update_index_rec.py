import re

with open(r'd:\Microvirt\OBSIDIAN\uchicago_replica\site_1to1\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

index_lor_block = '''      <!-- Letters of Recommendation (5 of 5 Received) -->
      <h3 class="portal-checklist-title">Letters of Recommendation (5 of 5 Received)</h3>
      <ul class="portal-checklist">
        <li class="portal-checklist-item">
          <div class="portal-checklist-label">
            <i class="fa-solid fa-check"></i>
            <div>
              <div style="font-weight: 600; color: #222;">1. Dr. Bhaskar Datta</div>
              <div style="font-size: 11.5px; color: #666;">Professor, Department of Chemistry &amp; Biological Engineering • Indian Institute of Technology (IIT) Gandhinagar</div>
            </div>
          </div>
          <span class="portal-badge-received">Received (Official)</span>
        </li>
        <li class="portal-checklist-item">
          <div class="portal-checklist-label">
            <i class="fa-solid fa-check"></i>
            <div>
              <div style="font-weight: 600; color: #222;">2. Dr. Sivapriya Kirubakaran</div>
              <div style="font-size: 11.5px; color: #666;">Professor &amp; Head, Department of Chemistry • Indian Institute of Technology (IIT) Gandhinagar</div>
            </div>
          </div>
          <span class="portal-badge-received">Received (Official)</span>
        </li>
        <li class="portal-checklist-item">
          <div class="portal-checklist-label">
            <i class="fa-solid fa-check"></i>
            <div>
              <div style="font-weight: 600; color: #222;">3. Dr. Shraedha Tiwari</div>
              <div style="font-size: 11.5px; color: #666;">Assistant Professor, Department of Chemistry • Institute of Chemical Technology (ICT) Mumbai, India</div>
            </div>
          </div>
          <span class="portal-badge-received">Received (Official)</span>
        </li>
        <li class="portal-checklist-item">
          <div class="portal-checklist-label">
            <i class="fa-solid fa-check"></i>
            <div>
              <div style="font-weight: 600; color: #222;">4. Dr. Kasturi Venkataraman</div>
              <div style="font-size: 11.5px; color: #666;">Professor • Indian Institute of Science (IISc) Bangalore</div>
            </div>
          </div>
          <span class="portal-badge-received">Received (Official)</span>
        </li>
        <li class="portal-checklist-item">
          <div class="portal-checklist-label">
            <i class="fa-solid fa-check"></i>
            <div>
              <div style="font-weight: 600; color: #222;">5. Dr. Sriram Kanvah Gundimeda</div>
              <div style="font-size: 11.5px; color: #666;">Professor, Department of Chemistry • Indian Institute of Technology (IIT) Gandhinagar</div>
            </div>
          </div>
          <span class="portal-badge-received">Received (Official)</span>
        </li>
      </ul>'''

m = re.search(r'<!-- Letters of Recommendation.*?</ul>', content, re.DOTALL)
if m:
    content = content[:m.start()] + index_lor_block + content[m.end():]
    print("Updated Letters of Recommendation in index.html")

with open(r'd:\Microvirt\OBSIDIAN\uchicago_replica\site_1to1\index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Saved index.html")
