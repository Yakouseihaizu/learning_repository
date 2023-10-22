# spam = 'Hello, world'
# print(spam[0])
# print(spam[4])
# print(spam[-1])
# print(spam[0:5])
# print(spam[:5])
# print(spam[7:])

# fizz = spam[:5]
# print(fizz)
# print(id(fizz))

# name = 'Al'
# age = 4000
# print('Hello,my name is %s. I am %s years old' %(name,age))
# print(f'My name is {name}. Next year,I\'ll be {age+1}')
# spam = 'Hello, world!'
# spam = spam.upper()
# print(spam)
# spam = spam.lower()
# print(spam)

# feeling = input('How are you?\n')
# if feeling.lower() == 'great':
#     print('I feel great too.')
# else:
#     print('I hope the rest of your day is good.')

# if 'Hello, world!'.startswith('Hello'):
#     print('Yes')

# if 'Hello, world!'.endswith('world!'):
#     print('Yes')

# if 'abc123'.startswith('abcdef'):
#     print('Yes')

# if 'abc123'.endswith('12'):
#     print('Yes')

# if 'Hello, world!'.startswith('Hello, world'):
#     print('Yes')

# if 'Hello, world!'.endswith('Hello, world!'):
#     print('Yes')

# spam = '''Dear Alice,
# How have you been? I am fine.
# There is a container in the fridge.
# that is labeled "Milk Experiment".

# Please do not drink it.
# Sincerely,
# Bob'''
# import pprint
# pprint.pprint(spam.split('\n'))


# print(', '.join(['cats','rats','bats']))
# print(' '.join(['My','name','is','Simon']))
# print('ABC'.join(['My','name','is','Simon']))

# print('Hello, world!'.partition('world'))
# print('Hello, world!'.partition('XYZ'))
# spam = 'Hello'
# print(spam.rjust(10,'-'))
# print(spam.ljust(10,'*'))
# # print(spam)
# print(spam.center(10,'-'))

# spam = '       Hello, world!       '
# print(spam.strip()+'#')
# print(spam.lstrip()+'#')
# print(spam.rstrip()+'#')
# spam = 'SpamSpamBaconSpamEggsSpamSpam'
# print(spam.rstrip('ampS'))

import pyperclip
# pyperclip.copy('Hello, world')
print(pyperclip.paste())

