import PyPDF2
from pathlib import Path
import os

path = Path.cwd()/'..'/'source'
for folder,subfolders,filenames in list(os.walk(path)):
    for file in filenames:
        filename = Path(folder)/file
        pdfFile = open(filename,'rb')
        pdfReader = PyPDF2.PdfReader(pdfFile)
        if pdfReader.decrypt('yk20041229'):
            print('yes')
        else:
            print('No')

