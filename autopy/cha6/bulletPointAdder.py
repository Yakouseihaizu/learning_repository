#! python3
# bulletPointAdder.py - Add Wikipedia bullet points to the start
# of each line of text on the clipboard

import pyperclip
# filename = 'list.txt'
# with open(filename) as fp:
#     text = fp.read()

text = pyperclip.paste()

# print(text)

# TODO: Separate lines and add stars.
lines = text.split(sep='\n')


for i in range(len(lines)):
    lines[i] = '*' + lines[i]
# TODO: Combine the lines
# text = ''
text = '\n'.join(lines)

pyperclip.copy(text)
print(text)


