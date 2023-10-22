
# renameDates.py - Rename filenames with American MM-DD-YYYY date format
# to European DD-MM-YYYY

import re,os,shutil

regex = re.compile(r'''^(.*?) # before the date 
((0|1)?\d)       # month
-
((0|1|2|3)?\d)   # day
-
((19|20)\d\d)    # year
(.*?)$            # after the date
''',re.VERBOSE)

# TODO: loop over the files in the working directory.
for filename in os.listdir('.'):
    mo = regex.search(filename)
# TODO: Skip files without a date.
    if mo == None:
        continue
# TODO: Get the different parts of the filename.
    else:
        before = mo.group(1)
        month = mo.group(2)
        day = mo.group(4)
        year = mo.group(6)
        after = mo.group(8)
# TODO: Form the European-style filename
        newname = before+day+'-'+month+'-'+year+after
# TODO: Get the full, absolute file paths.
        dirpath = os.path.abspath('.')
        filepath = os.path.join(dirpath,filename)
        newpath = os.path.join(dirpath,newname)
# TODO: Rename the files
        print(f'Renaming "{filename}" to {newname}')
        shutil.move(filepath,newpath)
