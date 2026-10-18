with open('site_1to1/pages/who-we-are_a2z.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Check if X is already in there
if 'id="X"' in text:
    print("X already present!")
else:
    # Find the end of W section
    idx_w = text.find('id="W"')
    if idx_w == -1:
        print("Could not find W section!")
    else:
        # The W section ends at </ul></div>
        idx_ul = text.find('</ul></div>', idx_w)
        if idx_ul == -1:
            print("Could not find </ul></div> after W")
        else:
            split_point = idx_ul + len('</ul></div>')
            
            xyz_html = '''<div><h3 id="X" class="AlphabetList_letter__2Mcp2">X</h3><ul class="AlphabetList_links__1epy_"><li class="AlphabetList_linkContainer__P1Plh"><a href="research-and-scholarship.html" class="AlphabetList_link__2wIjG" target="_blank" rel="noopener noreferrer" data-color="grey"><span class="linkText">X-Ray Crystallography Core Facility</span></a></li><li class="AlphabetList_linkContainer__P1Plh"><a href="research-and-scholarship.html" class="AlphabetList_link__2wIjG" target="_blank" rel="noopener noreferrer" data-color="grey"><span class="linkText">X-Lab for Autonomous Computing</span></a></li><li class="AlphabetList_linkContainer__P1Plh"><a href="research-and-scholarship.html" class="AlphabetList_link__2wIjG" target="_blank" rel="noopener noreferrer" data-color="grey"><span class="linkText">Xiao Research Group in Physical Sciences</span></a></li></ul></div><div><h3 id="Y" class="AlphabetList_letter__2Mcp2">Y</h3><ul class="AlphabetList_links__1epy_"><li class="AlphabetList_linkContainer__P1Plh"><a href="research-and-scholarship.html" class="AlphabetList_link__2wIjG" target="_blank" rel="noopener noreferrer" data-color="grey"><span class="linkText">Yenching Center for East Asian Studies</span></a></li><li class="AlphabetList_linkContainer__P1Plh"><a href="research-and-scholarship.html" class="AlphabetList_link__2wIjG" target="_blank" rel="noopener noreferrer" data-color="grey"><span class="linkText">Yerkes Astrophysics Archive Collection</span></a></li><li class="AlphabetList_linkContainer__P1Plh"><a href="visit.html" class="AlphabetList_link__2wIjG" target="_blank" rel="noopener noreferrer" data-color="grey"><span class="linkText">Young Memorial Building</span></a></li></ul></div><div><h3 id="Z" class="AlphabetList_letter__2Mcp2">Z</h3><ul class="AlphabetList_links__1epy_"><li class="AlphabetList_linkContainer__P1Plh"><a href="research-and-scholarship.html" class="AlphabetList_link__2wIjG" target="_blank" rel="noopener noreferrer" data-color="grey"><span class="linkText">Zell Family Foundation Center for Enterprise</span></a></li><li class="AlphabetList_linkContainer__P1Plh"><a href="research-and-scholarship.html" class="AlphabetList_link__2wIjG" target="_blank" rel="noopener noreferrer" data-color="grey"><span class="linkText">Zirpolo Laboratory of Behavioral Genetics</span></a></li><li class="AlphabetList_linkContainer__P1Plh"><a href="research-and-scholarship.html" class="AlphabetList_link__2wIjG" target="_blank" rel="noopener noreferrer" data-color="grey"><span class="linkText">Zoology & Ecology Specimen Repository</span></a></li></ul></div>'''
            
            new_text = text[:split_point] + xyz_html + text[split_point:]
            with open('site_1to1/pages/who-we-are_a2z.html', 'w', encoding='utf-8') as f_out:
                f_out.write(new_text)
            print("Successfully populated X, Y, and Z sections into who-we-are_a2z.html!")
