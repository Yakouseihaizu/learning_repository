import re,pyperclip
# TODO: create regex for phone numbers
phone_regex = re.compile(r'''
((\d{3}|\(\d{3}\))?
(\s|-|\.)*
(\d{3})
(\s|-|\.)*
(\d{4})
(\s*(?:ext.|x|ext)\s*(\d{2,4}))?                         
)''',re.VERBOSE)
# TODO: create regex for email address
email_regex = re.compile(r'''
(([a-zA-Z0-9._%+-])+
@
([a-zA-Z0-9_.])+
(\.[a-zA-Z]{2,4})
        
)''',re.VERBOSE)
# TODO: find match in clipboard text
text = str(pyperclip.paste())
text = '415-863-9900 x 34'
matches = []
print(phone_regex.findall(text))
for groups in phone_regex.findall(text):
    phone_number = '-'.join([groups[1],groups[3],groups[5]])
    if phone_number != '':
        phone_number += 'x' + groups[7]+'*'
    matches.append(phone_number)
for groups in email_regex.findall(text):
    matches.append(groups[0])

result = '\n'.join(matches)

pyperclip.copy(result)
print(result)

# TODO: copy result to the clipboard