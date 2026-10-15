import os
import re
import urllib.request
import json
from html.parser import HTMLParser

class ImgParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags = []

    def handle_starttag(self, tag, attrs):
        if tag in ['img', 'source', 'video']:
            attr_dict = dict(attrs)
            src = attr_dict.get('src') or attr_dict.get('data-src') or attr_dict.get('srcset') or attr_dict.get('poster')
            alt = attr_dict.get('alt', '')
            if src:
                self.tags.append({'tag': tag, 'src': src, 'alt': alt, 'attrs': attr_dict})

def analyze():
    url = "https://www.uchicago.edu/"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            live_html = resp.read().decode('utf-8', errors='ignore')
            print(f"Fetched live HTML length: {len(live_html)}")
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return

    parser = ImgParser()
    parser.feed(live_html)
    print(f"Found {len(parser.tags)} image/source references on live homepage.")
    
    os.makedirs("scratch", exist_ok=True)
    with open("scratch/live_homepage_images.json", "w", encoding="utf-8") as f:
        json.dump(parser.tags, f, indent=2)

    # Save live_html to scratch for inspection
    with open("scratch/live_homepage.html", "w", encoding="utf-8") as f:
        f.write(live_html)

    # Inspect site_1to1/index.html
    with open("site_1to1/index.html", "r", encoding="utf-8") as f:
        local_html = f.read()

    local_parser = ImgParser()
    local_parser.feed(local_html)
    print(f"Found {len(local_parser.tags)} image/source/video references in site_1to1/index.html.")
    with open("scratch/local_homepage_images.json", "w", encoding="utf-8") as f:
        json.dump(local_parser.tags, f, indent=2)

if __name__ == '__main__':
    analyze()
