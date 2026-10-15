import os
import urllib.request
import urllib.parse
import json

with open("scratch/jss_state.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Extract all images from JSS state
unique_urls = set()

def find_urls(obj):
    if isinstance(obj, dict):
        if "src" in obj and isinstance(obj["src"], str) and "media" in obj["src"]:
            unique_urls.add(obj["src"])
        for v in obj.values():
            find_urls(v)
    elif isinstance(obj, list):
        for item in obj:
            find_urls(item)

find_urls(data)

dest_dir = "site_1to1/assets/homepage_media"
os.makedirs(dest_dir, exist_ok=True)

print(f"Downloading {len(unique_urls)} images to {dest_dir}...")

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

downloaded = {}
for url in sorted(unique_urls):
    # Parse filename from URL
    parsed = urllib.parse.urlparse(url)
    filename = os.path.basename(parsed.path)
    if not filename:
        continue
    
    filepath = os.path.join(dest_dir, filename)
    print(f"Fetching {filename} from {url}...")
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=20) as resp:
            content = resp.read()
            with open(filepath, "wb") as out:
                out.write(content)
            downloaded[url] = f"assets/homepage_media/{filename}"
            print(f"  -> Saved {filename} ({len(content)} bytes)")
    except Exception as e:
        print(f"  -> Error downloading {url}: {e}")

with open("scratch/downloaded_mapping.json", "w", encoding="utf-8") as f:
    json.dump(downloaded, f, indent=2)

print(f"\nSuccessfully downloaded {len(downloaded)} / {len(unique_urls)} images!")
