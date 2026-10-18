import os
import re
import urllib.parse
from bs4 import BeautifulSoup
import json

SITE_DIR = r"d:\Microvirt\OBSIDIAN\uchicago_replica\site_1to1"
PAGES_DIR = os.path.join(SITE_DIR, "pages")

def audit_all_pages():
    results = {
        "pages_scanned": 0,
        "links_checked": 0,
        "dead_links": [],
        "broken_anchors": [],
        "unhandled_empty_clicks": [],
        "missing_assets": [],
        "design_anomalies": [],
        "seat_locking_mentions": []
    }
    
    # Collect all html files
    html_files = []
    for root, dirs, files in os.walk(SITE_DIR):
        for f in files:
            if f.endswith(".html"):
                html_files.append(os.path.join(root, f))
                
    results["pages_scanned"] = len(html_files)
    print(f"Total HTML files found: {len(html_files)}")
    
    for file_path in html_files:
        rel_path = os.path.relpath(file_path, SITE_DIR).replace("\\", "/")
        try:
            with open(file_path, "r", encoding="utf-8", errors="ignore") as fp:
                content = fp.read()
        except Exception as e:
            print(f"Error reading {rel_path}: {e}")
            continue
            
        soup = BeautifulSoup(content, "html.parser")
        
        # 1. Check for seat locking fee mentions
        if "seat locking" in content.lower() or "seat confirmation" in content.lower() or "matriculation" in content.lower():
            # Find specific paragraphs or list items
            matches = re.findall(r'([^.<\n]*?(?:seat locking|matriculation fee|enrollment deposit|reimbursable|refundable)[^.<\n]*?\.)', content, re.IGNORECASE)
            if matches:
                results["seat_locking_mentions"].append({
                    "file": rel_path,
                    "snippets": [m.strip() for m in matches[:5]]
                })
                
        # 2. Check design elements
        has_header = bool(soup.find("header") or soup.find(class_=re.compile(r"header|brandbar|navbar", re.I)))
        has_footer = bool(soup.find("footer") or soup.find(class_=re.compile(r"footer", re.I)))
        has_viewport = bool(soup.find("meta", attrs={"name": "viewport"}))
        title = soup.find("title")
        title_text = title.text.strip() if title else ""
        
        if not has_viewport:
            results["design_anomalies"].append({
                "file": rel_path,
                "type": "missing_viewport",
                "details": "Missing <meta name='viewport'> tag, breaks mobile responsiveness"
            })
            
        if not title_text:
            results["design_anomalies"].append({
                "file": rel_path,
                "type": "missing_title",
                "details": "Empty or missing <title> tag"
            })
            
        # Collect IDs for anchor verification
        page_ids = set()
        for tag in soup.find_all(True):
            if tag.get("id"):
                page_ids.add(tag.get("id"))
                
        # 3. Check all links (<a>)
        for a in soup.find_all("a"):
            results["links_checked"] += 1
            href = a.get("href")
            link_text = a.get_text(strip=True)
            
            if href is None:
                continue
            href = href.strip()
            
            if href == "" or href == "#":
                onclick = a.get("onclick") or ""
                data_toggle = a.get("data-toggle") or a.get("data-bs-toggle") or a.get("data-target") or ""
                role = a.get("role") or ""
                if not (onclick or data_toggle or role == "tab" or role == "button" or a.get("id")):
                    results["unhandled_empty_clicks"].append({
                        "file": rel_path,
                        "text": link_text,
                        "href": href,
                        "html": str(a)[:120]
                    })
                continue
                
            if href.startswith("javascript:"):
                if href in ["javascript:void(0)", "javascript:void(0);", "javascript:;"]:
                    onclick = a.get("onclick") or ""
                    if not onclick:
                        results["unhandled_empty_clicks"].append({
                            "file": rel_path,
                            "text": link_text,
                            "href": href,
                            "html": str(a)[:120]
                        })
                continue
                
            if href.startswith("mailto:") or href.startswith("tel:"):
                continue
                
            if href.startswith("#"):
                target_id = href[1:]
                if target_id and target_id not in page_ids:
                    results["broken_anchors"].append({
                        "file": rel_path,
                        "anchor": href,
                        "text": link_text
                    })
                continue
                
            # Local or relative link
            # Remove query string and hash
            clean_href = href.split("?")[0].split("#")[0]
            if clean_href.startswith("http://") or clean_href.startswith("https://"):
                # Check if it's pointing to localhost or uchicago.asia
                parsed = urllib.parse.urlparse(clean_href)
                if parsed.netloc in ["localhost:3000", "uchicago.asia", "www.uchicago.asia", "portal.uchicago.asia"]:
                    clean_path = parsed.path.lstrip("/")
                else:
                    # External link
                    continue
            else:
                clean_path = clean_href.lstrip("/")
                
            if not clean_path:
                continue
                
            # Check if file exists in site_1to1 or site_1to1/pages or relative to current file
            target_direct = os.path.join(SITE_DIR, clean_path)
            target_html = os.path.join(SITE_DIR, clean_path + ".html")
            target_in_pages = os.path.join(PAGES_DIR, clean_path)
            target_in_pages_html = os.path.join(PAGES_DIR, clean_path + ".html")
            
            # Relative to file directory
            curr_dir = os.path.dirname(file_path)
            target_relative = os.path.join(curr_dir, clean_path)
            target_relative_html = os.path.join(curr_dir, clean_path + ".html")
            
            exists = (
                os.path.exists(target_direct) or
                os.path.exists(target_html) or
                os.path.exists(target_in_pages) or
                os.path.exists(target_in_pages_html) or
                os.path.exists(target_relative) or
                os.path.exists(target_relative_html)
            )
            
            if not exists:
                # Filter out intentional external routes or assets
                results["dead_links"].append({
                    "file": rel_path,
                    "href": href,
                    "text": link_text[:50]
                })

        # 4. Check images (<img>)
        for img in soup.find_all("img"):
            src = img.get("src")
            if not src:
                results["missing_assets"].append({
                    "file": rel_path,
                    "type": "empty_img_src",
                    "html": str(img)[:100]
                })
                continue
            src = src.strip()
            if src.startswith("data:"):
                continue
            clean_src = src.split("?")[0].split("#")[0]
            if clean_src.startswith("http://") or clean_src.startswith("https://"):
                parsed = urllib.parse.urlparse(clean_src)
                if parsed.netloc in ["localhost:3000", "uchicago.asia", "www.uchicago.asia"]:
                    clean_src_path = parsed.path.lstrip("/")
                else:
                    continue
            else:
                clean_src_path = clean_src.lstrip("/")
                
            target_img1 = os.path.join(SITE_DIR, clean_src_path)
            curr_dir = os.path.dirname(file_path)
            target_img2 = os.path.join(curr_dir, clean_src_path)
            target_img3 = os.path.join(SITE_DIR, "assets", "subpage_media", os.path.basename(clean_src_path))
            
            if not (os.path.exists(target_img1) or os.path.exists(target_img2) or os.path.exists(target_img3)):
                results["missing_assets"].append({
                    "file": rel_path,
                    "src": src,
                    "alt": img.get("alt", "")
                })

    with open(os.path.join(SITE_DIR, "..", "scratch", "audit_results.json"), "w", encoding="utf-8") as out:
        json.dump(results, out, indent=2)
        
    print(f"\n--- AUDIT SUMMARY ---")
    print(f"Pages Scanned: {results['pages_scanned']}")
    print(f"Links Checked: {results['links_checked']}")
    print(f"Dead Links Found: {len(results['dead_links'])}")
    print(f"Broken Anchors Found: {len(results['broken_anchors'])}")
    print(f"Unhandled Empty Clicks / Dead Ends: {len(results['unhandled_empty_clicks'])}")
    print(f"Missing Assets: {len(results['missing_assets'])}")
    print(f"Design Anomalies: {len(results['design_anomalies'])}")
    print(f"Files Mentioning Seat Locking / Matriculation: {len(results['seat_locking_mentions'])}")

if __name__ == "__main__":
    audit_all_pages()
