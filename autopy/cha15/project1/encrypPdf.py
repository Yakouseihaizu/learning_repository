import PyPDF2
import os
from pathlib import Path
import pprint
import re
import sys
import logging


logging.basicConfig(level=logging.DEBUG,format='%(message)s')
password = sys.argv[1]
def encrypt_pdf(folder,filename):
    try:
        
        pdfFile = open(str(Path(folder)/filename)+'.pdf','rb')
        pdfReader =PyPDF2.PdfReader(pdfFile)
        
        logging.debug('open successful')
        newFile = open(str(Path.cwd()/'..'/'source'/filename)+'_encrypted.pdf','wb')
        pdfWriter = PyPDF2.PdfWriter()
        for page in pdfReader.pages:
            pdfWriter.add_page(page)
        
        pdfWriter.encrypt(password)
        pdfWriter.write(newFile)
        pdfFile.close()
        newFile.close()
        print(f'{filename} is encrypted')
    except:
        print('Fail to encrypt')

path = Path('C:/Users/HUAWEI/Desktop/autopy/cha15')
# if path == Path.cwd():
#     print('Success')
# pprint.pprint(list(os.walk(path)))
regex = re.compile('^(.*).pdf$')

for folder,subfolders,filenames in list(os.walk(path)):
    for filename in filenames:
        if mo := regex.search(filename):
            name = mo.group(1)
            encrypt_pdf(folder,name)
            # print(str(Path(folder)/filename)+'.pdf')
