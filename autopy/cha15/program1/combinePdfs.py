import PyPDF2
import os
from pathlib import Path
import re

path = Path.cwd()
regex = re.compile(r'^.+(\.pdf)$')
fileList = os.listdir(path)
pdfWriter = PyPDF2.PdfWriter()
times = True
for filename in fileList:
    if regex.search(filename):
        pdfFile = open(filename,'rb')
        pdfReader = PyPDF2.PdfReader(pdfFile)
        if times:
            pdfWriter.add_page(pdfReader.pages[0])
            times = False
        for page in pdfReader.pages[1:]:
            pdfWriter.add_page(page)
        pdfFile.close()

result = open('result.pdf','wb')
pdfWriter.write(result)
result.close()