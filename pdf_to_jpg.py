# Convert all pages of pdf documents in a directory to jpg

import os
from pdf2image import convert_from_path

pdf_data_path = './pdf_data'
jpg_data_path = './jpg_data'

for filename in os.listdir(pdf_data_path):
    if filename.endswith(".pdf"):
        pages = convert_from_path(os.path.join(pdf_data_path, filename), 500)
        for page in pages:
            page.save(os.path.splitext(os.path.join(
                jpg_data_path, filename))[0]+'.jpg', 'JPEG')
        continue
    else:
        continue
