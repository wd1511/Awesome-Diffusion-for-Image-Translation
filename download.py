import os
import re
from pathlib import Path

import requests

# 读取完整论文清单
markdown_file = Path(__file__).with_name("PAPERS.md")

# 创建一个目录来保存下载的PDF文件
output_directory = "pdf_downloads"
os.makedirs(output_directory, exist_ok=True)

# 读取Markdown文件内容
with open(markdown_file, "r", encoding="utf-8") as f:
    markdown_content = f.read()

# 匹配 PDF、PDF1、PDF(old) 等链接，跳过模板中的占位地址
pdf_links = re.findall(r"\[PDF(?:\d+|\([^)]*\))?\]\((https?://[^\s)]+)\)", markdown_content)
print(len(pdf_links))

for pdf_url in pdf_links:
    # 生成保存的文件名，通常使用链接中的文件名部分
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
        print(f"下载成功: {file_name}")
    else:
        print(f"下载失败: {pdf_url_useful}")
