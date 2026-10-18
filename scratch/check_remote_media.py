import os
import re

def check_remote_media():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    site_dir = os.path.join(base_dir, "..", "site_1to1")

    img_src_pattern = re.compile(
        r'src=["\'](https?://[^"\']*(?:uchicago\.asia|uchicago\.edu)[^"\']*)["\']',
        re.IGNORECASE
    )
    bg_pattern = re.compile(
        r'url\(["\']?(https?://[^"\')\s]*(?:uchicago\.asia|uchicago\.edu)[^"\')\s]*)["\']?\)',
        re.IGNORECASE
    )

    remote_media = []

    for root, _, files in os.walk(site_dir):
        for f in files:
            if f.endswith(('.html', '.js', '.css')):
                fpath = os.path.join(root, f)
                rel_path = os.path.relpath(fpath, site_dir)
                try:
                    with open(fpath, 'r', encoding='utf-8', errors='ignore') as fp:
                        content = fp.read()
                    for m in img_src_pattern.findall(content):
                        remote_media.append((rel_path, "src", m))
                    for m in bg_pattern.findall(content):
                        remote_media.append((rel_path, "bg", m))
                except Exception as err:
                    print(f"Error reading {rel_path}: {err}")

    print(f"Checked site_1to1 directory: Found {len(remote_media)} remote media references.")
    if remote_media:
        print("Sample findings:")
        for rpath, mtype, url in remote_media[:10]:
            print(f"  [{rpath}] ({mtype}): {url}")
    else:
        print("All media references are fully localized or clean.")

if __name__ == "__main__":
    check_remote_media()
