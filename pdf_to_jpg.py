# Convert all pages of pdf documents in a directory to jpg

import os
from pdf2image import convert_from_path

for filename in os.listdir('./pdf_data'):
    if filename.endswith(".pdf"):
        pages = convert_from_path(os.path.join('./pdf_data', filename), 500)
        for page in pages:
            page.save(os.path.splitext(os.path.join(
                './jpg_data', filename))[0]+'.jpg', 'JPEG')
        continue
    else:
        continue
