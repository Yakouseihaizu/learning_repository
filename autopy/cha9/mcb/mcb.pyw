#! Python3
# mcb.pyw - Saves and loads pieces of text to the clipboard
# Usage: py.exe mcb.pyw save <keyword> - Save clipboard to keyword
#        py.exe mcb.pyw <keyword> - Loads keyboard to clipboard
#        py.exe mcb.pyw list - Loads all keywords to clipboard

import sys,shelve,pyperclip

mcbShelf = shelve.open('mcb')

# TODO: Save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf.keys():
        pyperclip.copy(mcbShelf[sys.argv[1]])
mcbShelf.close()

# TODO: List keywords and load content.
# C:\Users\HUAWEI\AppData\Local\Programs\Python\  

mcbShelf.close()