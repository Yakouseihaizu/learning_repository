# mapIt.py - Launched a map in the browser using an address from the
# command line or clipboard.

import webbrowser,sys,pyperclip
if len(sys.argv) >1:
    # Get address from command lines.
    address = ' '.join(sys.argv[1:])

# TODO: Get aadress from clipboard.
else:
    address = pyperclip.paste()

webbrowser.open('https:/google.com/maps/place/%s' %(address))