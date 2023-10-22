#! Python3
# backupToZip.py - Copies an entire folder and its contents into
# a ZIP file whose filename increments.

import zipfile,os

def backupToZip(folder):
    # Back up to the entire content of "folder" into a ZIP file.
    folder = os.path.abspath(folder)
    # Fihure out the filename this code shuold based on
    # what files already exits.
    number = 1
    while True:
        zipFileName = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFileName):
            break
        number+=1

    # TODO: create the Zip file
    backupZip = zipfile.ZipFile(zipFileName,'w')
    for foldername,subfolders,filenames in os.walk('.'):
        print(f'Adding files in {foldername}')
        backupZip.write(foldername)
        # Add all the files in this folder to zip file.
        for filename in filenames:
            newBase = os.path.basename(folder)+'_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue
            backupZip.write(os.path.join(foldername,filename))
    backupZip.close()
    print('Done')
from pathlib import Path 
backupToZip(Path.cwd())


