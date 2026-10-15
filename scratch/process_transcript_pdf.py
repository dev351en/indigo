import pymupdf # PyMuPDF
import os
import shutil

src_pdf = r"C:\Users\brode\.gemini\antigravity-ide\brain\94957be3-4e99-4205-a4b5-6bf393e5ed92\.user_uploaded\media_1792093976572.pdf"
dest_dir = r"d:\Microvirt\OBSIDIAN\uchicago_replica\site_1to1\assets\documents"
os.makedirs(dest_dir, exist_ok=True)

dest_pdf = os.path.join(dest_dir, "Official_Transcript_IITGN_24510041.pdf")
shutil.copy2(src_pdf, dest_pdf)
print(f"Copied PDF to: {dest_pdf} ({os.path.getsize(dest_pdf)} bytes)")

doc = pymupdf.open(src_pdf)
print(f"Total pages: {len(doc)}")

for i, page in enumerate(doc):
    # Render page at 2x resolution (144 dpi) for crystal-clear text
    zoom = 2.0
    mat = pymupdf.Matrix(zoom, zoom)
    pix = page.get_pixmap(matrix=mat, alpha=False)
    img_path = os.path.join(dest_dir, f"transcript_page_{i+1}.png")
    pix.save(img_path)
    print(f"Saved page {i+1} to: {img_path} ({os.path.getsize(img_path)} bytes)")

print("Transcript conversion complete!")
