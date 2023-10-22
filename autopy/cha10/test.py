import shutil,os
from pathlib import Path

p = Path.cwd()
# os.makedirs(p/'new')
# copied_spam_path = shutil.copy(p/'spam.txt',p/'new')
# print(copied_spam_path)
# copied_eggs_path = shutil.copy(p/'eggs.txt',p/'new')
# print(copied_eggs_path)
# os.makedirs(p/'test')
# with open(p/'test'/'spam.txt','w') as fp:
#     fp.write('Hello, spam!')
# with open(p/'test'/'eggs.txt','w') as fp:
#     fp.write('Eggs Here!')

# copied_spam_path = shutil.copytree(p/'test',p/'new')

# move_path = shutil.move(p/'move.txt',p/'new')
# print(move_path)
# p/Path('move').mkdir()
# os.makedirs(p/'move')
# for i in range(2):
#     with open(p/'move'/f'move{i+1}.txt','w') as fp:
#         fp.write('Moved'+f'{i+1}'*3+'to new.')
# move_folder_path = shutil.move(p/'move',p/'new')

import os
from pathlib import Path
import pprint

# for filename in list()
# for folderName, subfolders,filenames in os.walk('test.py'):
#     print(f'The current folder is {folderName}')
#     for subfolder in subfolders:
#         print(F'SUBFOLDER OF {folderName}: {subfolder}')
#     for filename in filenames:
#         print(f'FILE INSIDE OF {folderName}: {filename}')
#     print()
# pprint.pprint(list(os.walk('test.py')))
# if os.walk('test.py') == None:
    # print('yes')
# C:\Users\HUAWEI\Desktop\autopy\cha10\1152563.zip/340_1524816018/rungame.inie

import zipfile,os
from pathlib import Path
# p = Path.cwd()/'example.zip'
# example_zip = zipfile.ZipFile(p)
# print(example_zip.namelist())
# print(spaminfo := example_zip.getinfo('spam.txt'))
# print(spaminfo.file_size)
# print(spaminfo.compress_size)
# example_zip.extractall(Path.cwd()/'ZipPart')
# example_zip.extract('spam.txt')
# example_zip.close()

with zipfile.ZipFile('new.zip','w') as newZip:
    newZip.write('spam.txt',compress_type=zipfile.ZIP_DEFLATED)
with zipfile.ZipFile('new.zip') as newZip:
    print(newZip.namelist())
# newZip.close()
