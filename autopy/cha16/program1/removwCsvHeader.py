import csv
import os
from pathlib import Path
import re
import pprint

regex = re.compile('^.*.csv$')

Dict = []
csvs = []

for folder,subfolders,filenames in os.walk(Path.cwd()):
    for filename in filenames:
        if regex.search(filename):
            filepath = Path(folder)/filename
            csvs.append(filepath)
            fp = open(filepath)
            dictReader = csv.reader(fp)
            elems = list(dictReader)[0]
            for elem in elems:
                if elem not in Dict:
                    Dict.append(elem)
            fp.close()
fp = open('merged.csv','w',newline='')
csvDictWriter = csv.DictWriter(fp,Dict)
csvDictWriter.writeheader()
# pprint.pprint(csvs)
for file in csvs:
    csvFile = open(file)
    csvDICTReader = csv.DictReader(csvFile)
    for row in csvDICTReader:
        # print(row)
        csvDictWriter.writerow(row)
    csvFile.close()
fp.close()

