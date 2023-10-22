import os
from pathlib import Path

p = Path.cwd()
for foldername,subfolders,filenames in os.walk(p/'files'):

    for filename in filenames:
        path = p/foldername/filename
        size = os.path.getsize(path)
        if size >= 100:
            print(path)
            os.unlink(path)
        else:
            print(f'nothing {size}')

