import re

regex = re.compile(r'(ADJECTIVE|NOUN|ADVERB|VERB)')
with open('sentence.txt','r') as fp:
    content = fp.read()
    parts = regex.findall(content)
    replace = []
    for piece in parts:
        replace.append(input(f"Enter a {piece.lower()}:\n"))
    for piece in replace:
        content = regex.sub(piece,content,count=1)

with open('sentence.txt','w') as fp:
    fp.write(content)
    print(content)


