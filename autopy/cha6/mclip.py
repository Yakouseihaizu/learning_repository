#! python3
# mclip.py - A  multi-clipboard program
import json

with open('TEXT.json','r') as fp:
    TEXT = json.load(fp)

import sys
import pyperclip

if len(sys.argv) < 2:
    print('Usage: py(thon) mclip.py [keyphrase] - copy phrase text')
    sys.exit()

keyphrase = sys.argv[1]  # first command line arg is the keyphase



if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print(f'Text for {keyphrase} copied to clipboard.')
else :
    print(f'There is no text for {keyphrase}')
    new = input(f'Add the new answer for {keyphrase}:(blank to quit)\n')
    if new:
        TEXT[keyphrase] = new
        with open('TEXT.json','w') as fp:
            json.dump(TEXT,fp)
    else :
        sys.exit()

    