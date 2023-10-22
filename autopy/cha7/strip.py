import re
def my_strip(string,delet=r'\s'):
    # string = ''
    regex = re.compile(f'^(?:{delet}*)([^{delet}]*)(?:{delet}*)$')
    # print(delet)
    mo = regex.search(string)
    return mo.group(1)
# print('(\s*)^([^ ]*)(\s*)$')
print('*'+my_strip('   safsf   ')+'*')
print(my_strip('----vjbdsjbvsdjb----',delet='-'))
