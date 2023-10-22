import re
from pathlib import Path
import os
import sys
import pprint

if len(sys.argv) == 2 :
    regex = re.compile(sys.argv[1])
path = Path.cwd()
txts = list(path.glob('*.txt'))
result = []
for text in txts:
    with open(text) as fp :
        content = fp.readlines()
        for line in content:
            if regex.findall(line):
                result.append(line)

pprint.pprint(result)
