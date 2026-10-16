import re

def sync():
    with open('site_1to1/portal.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Relative path transforms for files in pages/
    # 1. Assets, css, fonts, dist, runtime
    content = content.replace('href="dist/', 'href="../dist/')
    content = content.replace('href="css/', 'href="../css/')
    content = content.replace('href="fonts/', 'href="../fonts/')
    content = content.replace('src="assets/', 'src="../assets/')
    content = content.replace('href="assets/', 'href="../assets/')
    content = content.replace('src="interactive_runtime.js"', 'src="../interactive_runtime.js"')
    
    # 2. Page links
    content = content.replace('href="index.html"', 'href="../index.html"')
    content = content.replace('href="portal.html"', 'href="../portal.html"')
    # Offer letter and email are in the same pages/ directory
    content = content.replace('href="pages/offer-letter.html"', 'href="offer-letter.html"')
    content = content.replace('href="pages/admissions-offer-email.html"', 'href="admissions-offer-email.html"')
    content = content.replace('href="pages/', 'href="')

    # Breadcrumb bar in pages/
    # <a href="index.html">Home</a> -> <a href="../index.html">Home</a>
    # <a href="pages/admissions.html">Admissions</a> -> <a href="admissions.html">Admissions</a>

    with open('site_1to1/pages/portal.html', 'w', encoding='utf-8') as f:
        f.write(content)

    print('Successfully synchronized site_1to1/pages/portal.html with site_1to1/portal.html!')

if __name__ == '__main__':
    sync()
