#! Pythonw.exe
# mcb.py - Save and loads pieces of text to the clipboard
# Usage: pythonw mcb.pyw save <keyword> - Save clipboard to keyword
#        pythonw mcb.pyw <keyword> - Loads keyword to clipboard
#        pythonw mcb.pyw list - Loads all keyword to clipboard
#        pythonw mcb.pyw delet <keyword> - delet the keyword
#        pythonw mcb.pyw deletall - delet all the keywords

import shelve,sys,pyperclip

shelf_file = shelve.open('mcb')
if len(sys.argv) == 3 :
    if sys.argv[1].lower() == 'save':
        shelf_file[sys.argv[2]] = pyperclip.paste()
    elif sys.argv[1].lower() == 'delet':
        del shelf_file[sys.argv[2]]
elif len(sys.argv) == 2:
    if sys.argv[1] == 'list':
        pyperclip.copy(str(list(shelf_file.keys())))
    elif sys.argv[1] == 'deletall':
        for key in list(shelf_file.keys()):
            del shelf_file[key]
    elif sys.argv[1] in shelf_file.keys():
        pyperclip.copy(str(shelf_file[sys.argv[1]]))
shelf_file.close()