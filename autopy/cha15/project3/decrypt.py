import PyPDF2

fp = open('encrypted.pdf','rb')
PdfReader = PyPDF2.PdfReader(fp)
dictionary = open('dictionary.txt')
passwords = dictionary.readlines()
pws = []
for pw in passwords:
    if pw.endswith('\n'):
        pws.append(pw[:-1])
# print(pws[:10])
for pwd in pws:
    if PdfReader.decrypt(pwd):
        break
print(pwd)
dictionary.close()

fp.close()
