import PyPDF2

fp = open('meetingminutes.pdf','rb')
pdfReader = PyPDF2.PdfReader(fp)
en = open('encrypted.pdf','wb')
pdfWriter = PyPDF2.PdfWriter()
for page in pdfReader.pages:
    pdfWriter.add_page(page)
pdfWriter.encrypt('MOTHERHOOD')
pdfWriter.write(en)

fp.close()
en.close()