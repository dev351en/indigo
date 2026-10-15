with open('site_1to1/portal.html', 'r', encoding='utf-8') as f:
    portal_root = f.read()

with open('site_1to1/pages/portal.html', 'r', encoding='utf-8') as f:
    pages_portal = f.read()

card_start = '<!-- Official Admission Offer Letter & Fellowship Grant Card -->'
card_end = '<!-- Applicant Dossier Card -->'
card_chunk = portal_root[portal_root.find(card_start):portal_root.find(card_end)]

# Adapt paths for pages/ (add ../ to assets and documents)
card_chunk_pages = card_chunk.replace('href="assets/', 'href="../assets/').replace('src="assets/', 'src="../assets/').replace('href="offer-letter.html"', 'href="offer-letter.html"').replace('href="admissions-offer-email.html"', 'href="admissions-offer-email.html"')

modal_start = '<!-- Official Admission & Fellowship Offer Letter Modal Viewer -->'
modal_end = '<!-- ==========================================================================\n       Institutional Payment Gateway'
modal_chunk = portal_root[portal_root.find(modal_start):portal_root.find(modal_end)]
modal_chunk_pages = modal_chunk.replace('src="assets/', 'src="../assets/').replace('href="assets/', 'href="../assets/')

if card_start not in pages_portal:
    target = '<!-- Applicant Dossier Card -->'
    pages_portal = pages_portal.replace(target, card_chunk_pages + '\n          ' + target, 1)

if modal_start not in pages_portal:
    target_modal = '<!-- ==========================================================================\n       Institutional Payment Gateway'
    pages_portal = pages_portal.replace(target_modal, modal_chunk_pages + '\n  ' + target_modal, 1)

# Also update status banner
old_banner = '<div style="font-size: 15px; font-weight: 700; color: #800000;">Application Status: Complete &amp; Under Review • Faculty Advisor Confirmed</div>'
new_banner = '<div style="font-size: 15px; font-weight: 700; color: #800000;">Official Admissions Status: Admitted &amp; Fully Funded • Offer Letter Issued</div>'
pages_portal = pages_portal.replace(old_banner, new_banner)

with open('site_1to1/pages/portal.html', 'w', encoding='utf-8') as f:
    f.write(pages_portal)

print('Updated site_1to1/pages/portal.html successfully!')
