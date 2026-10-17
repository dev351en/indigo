import os
import zipfile

target_zip = '../uchicago_website_replica_complete.zip'
root_dir = '.'

# Exclude directories
EXCLUDE_DIRS = {'.git', 'node_modules', '__pycache__'}
EXCLUDE_FILES = {'.DS_Store', 'Thumbs.db'}

print(f"Creating master zip: {target_zip}")

count = 0
total_size = 0

with zipfile.ZipFile(target_zip, 'w', zipfile.ZIP_DEFLATED, compresslevel=6) as zipf:
    for root, dirs, files in os.walk(root_dir):
        # Filter out excluded directories in-place
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
        
        for f in files:
            if f in EXCLUDE_FILES or f.endswith(('.pyc', '.log')):
                continue
            
            filepath = os.path.join(root, f)
            arcname = os.path.relpath(filepath, root_dir)
            
            zipf.write(filepath, arcname)
            count += 1
            total_size += os.path.getsize(filepath)

print(f"Master ZIP successfully generated!")
print(f"Total files packaged: {count}")
print(f"Uncompressed size: {total_size / (1024 * 1024):.2f} MB")
print(f"Compressed archive size: {os.path.getsize(target_zip) / (1024 * 1024):.2f} MB")
