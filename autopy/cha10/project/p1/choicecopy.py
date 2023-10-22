import re,os,shutil
from pathlib import Path

p = Path.cwd()
regex = re.compile(r'(.*.pdf)|(.*.jpg)')
os.makedirs(p/Path('destination'))
for foldername,subnames,filenames in os.walk(p/'./files'):
    for filename in filenames:
        if regex.search(filename) != None:
            shutil.copy(p/Path(foldername)/Path(filename),p/Path('destination'))

