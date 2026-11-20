import os
import re
from pathlib import Path

import requests

# Use the source catalog to avoid duplicate entries from the reading views.
markdown_file = Path(__file__).parent / "catalog" / "full.md"

output_directory = "pdf_downloads"
os.makedirs(output_directory, exist_ok=True)

with open(markdown_file, "r", encoding="utf-8") as f:
    markdown_content = f.read()

# Include alternate PDF links such as PDF1 and PDF(old).
pdf_links = re.findall(r"\[PDF(?:\d+|\([^)]*\))?\]\((https?://[^\s)]+)\)", markdown_content)
print(len(pdf_links))

for pdf_url in pdf_links:
    pdf_url_sup = pdf_url.split('/') 
    if pdf_url_sup[2] == 'arxiv.org' and pdf_url_sup[3] == 'abs':
        pdf_url_useful = 'https://arxiv.org/pdf/'+pdf_url_sup[4]+'.pdf'
    else:
        pdf_url_useful = pdf_url
    file_name = os.path.join(output_directory, os.path.basename(pdf_url_useful))

    print(file_name, pdf_url_useful)

    response = requests.get(pdf_url_useful)
    if response.status_code == 200:
        with open(file_name, "wb") as pdf_file:
            pdf_file.write(response.content)
        print(f"Downloaded: {file_name}")
    else:
        print(f"Download failed: {pdf_url_useful}")
