from pathlib import Path
# path = Path('spam','bacon','eggs')

# print(str(path))

# my_files = ['accounts.txt','details.csv','invite.docx']
# for filename in my_files:
#     print(Path(r'C:/Users/Al',filename))

# print(Path('spam') / 'bacon' / 'eggs')
# print(Path('spam') / Path('bacon/eggs'))
# print(Path('spam') / Path('bacon','eggs'))
# try : 
#     print('spam' / 'bacon' / 'eggs')
# except:
#     pass

# print(Path('spam') / 'bacon' / 'eggs')
# print('spam' / Path('bacon') / 'eggs')

import os
# Path.cwd()
# p = Path('C:/Users/Al/spam.txt')
# print(p.anchor)
# print(p.parent)
# print(p.stem)
# print(p.suffix)
# print(p.drive)
# print('Parents:')
# for parent in p.parents:
#     print(parent)

# total_size = 0
# path = 'C:/Windows/System32'
# for file in os.listdir(path):
#     total_size += os.path.getsize(os.path.join(path,file))
# print(total_size)

# p = Path('C:/Users/HUAWEI/Desktop')
# p = Path('C:/Users/HUAWEI/Desktop/autopy/cha4')
# # for file in list(p.glob('*')):
#     # print(file)

# for file in list(p.glob('*MyCats?.py')):
#     print(file)

# notExistFile = Path('C:/No/Exits')
# calcFile = Path('C:/Windows/System32/calc.exe')
# winDir = Path('C:/Windows')

# print(f'notExistFile : {notExistFile.exists()}')
# print(f'clacFile:      {calcFile.exists()}    file: {calcFile.is_file()}')
# print(f'winDir:        {winDir.exists()  }     dir: {winDir.is_dir()}')


# with open('helloFile.txt') as fp:
#     content = fp.read()
#     print(content)

# import pprint
# with open('sonnet29.txt') as fp:
#     content = fp.readlines()
#     pprint.pprint(content)

import shelve

# shelfFile = shelve.open('mydata')
# print(shelfFile['cats'])
# shelfFile.close()
# with shelve.open('mydata') as sfp:
#     # sfp['dogs'] = ['mont','harry','enum']
#     print(sfp['cats'])
#     print(list(sfp.keys()))
#     print(list(sfp.values()))

import pprint
cats = [{'name':'Zophie','desc':'chubby'},{'name':'Pooka','desc':'fluffy'}]
str_to_py = pprint.pformat(cats)
with open('myCats.py','w') as fp:
    fp.write('cats = '+ str_to_py +'\n')