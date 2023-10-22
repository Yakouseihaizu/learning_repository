import re

# phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# mo = phoneNumRegex.search('My phone number is 415-555-4242.')
# print('Phone number found: ' + mo.group())

# xamx_regex = re.compile(r'\d+\s\w+')
# mo = xamx_regex.findall('12 drummer nlnan jcccjn, 11 pipers, 10 lords')

# vowelRegex = re.compile(r'[aeiouAEIOU]')
# mo = vowelRegex.findall('RoboCop eats bady foods.BABY FOOD.')
# consonantRegex = re.compile(r'[^aeiouAEIOU]')
# mo = consonantRegex.findall('RoboCop eats bady foods.BABY FOOD.')

# begins_with_hello = re.compile(r'^Hello')
# mo = begins_with_hello.search('Hello world!')
# mo1 = begins_with_hello.search('Say Hello')

# ends_with_number = re.compile(r'\d+$')
# mo2 = ends_with_number.search('Your number is 42')
# # print(mo2)

# whole_string_is_num = re.compile(r'^\d+$')
# mo3 = whole_string_is_num.search('1234567890')
# mo4 = whole_string_is_num.search('12345xyz67890')
# mo5 = whole_string_is_num.search('12 4567890')
# print(mo3)
# print(mo4)
# print(mo5)

# print(mo)
# if mo1:
#     print(mo1.group())
# else:
#     print(mo1)
# 15388581288

# my_regex = re.compile(r'[^a-c6]+')
# mo = my_regex.search('adc6egfa4576')
# mo = my_regex.search('avbcjb')
# print(mo)
# name_regex = re.compile(r'First Name: (.*) Last Name: (.*)')
# name_regex = re.compile(r'First Name: (.*?) Last Name: (.*?)')
# mo = name_regex.search('First Name: Al Last Name: Sweigart')
# print(mo.group(1))
# print(mo.group(2))

# nongreedy_regex = re.compile(r'<.*?>')
# text = '<To serve man> for dinner.>'
# mo1 = nongreedy_regex.search(text)
# print(mo1)

# greedy_regex = re.compile(r'<.*>')
# mo2 = greedy_regex.search(text)
# print(mo2)

# robocop = re.compile(r'robocop',re.I)
# mo = robocop.search('Robocop is part man, part machine, all cop')
# print(mo.group())
# mo = robocop.search('ROBOCOP projects the innocent.')
# print(mo.group())
# mo = robocop.search('Al, why does your programing book talk about robocop so mach?')
# print(mo.group())

# nameRegex = re.compile(r'Agent \w+')
# mo = nameRegex.sub('CENSORED','Agent Alice gave the secret documents to Agent Bob')
# print(mo)

# nameRegex = re.compile(r'Agent (\w)\w*')
# mo = nameRegex.sub(r'\1******','Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent')
# print(mo)

# phone_regex = re.compile(r'''(
# (\d{3}|\(\d{3}\))?           # area code
# (\s|\.|-)*                  # sperator
# (\d{3})
# (\s|-|\.)*
# (\d{4})
# (\s*(ext|x|ext.)\s*\d{2,4})?        # Extent
# )
# ''',re.VERBOSE)
# mo = phone_regex.search('(415)-555-1234  ext. 1234')
# print(mo.group())

# import re

# s = 'hello 123 world 456'

# # 非捕获组匹配但不捕获数字
# pattern = re.compile(r'hello (?:\d+) world (?:\d+)') 
# match = pattern.search(s)

# print(match.groups()) # ()

# regex = re.compile(r'(\d{,3})?(,\d\d\d)*')
# mo = regex.search('1234')
# print(mo)

# regex = re.compile(r'[A-Z]\w*\sNakamoto')
# texts = ['Satoshi Nakamoto','Alice Nakamoto','Robocop Nakamoto','satoshi Nakamoto','Mr. Nakamoto','Nakamoto','Satoshi nakamoto']
# for text in texts:
#     mo = regex.search(text)
#     print(mo)

regex = re.compile(r'(Alice|Bob|Carol) (eats|pets|throws) (apples|cats|baseballs).',re.I)
texts = ['Alice eats apples.','Bob pets cats.',
         'Carol throws baseballs.','BOB EAT CATS.',
         'Robocop eats apples.','ALICE THROWS FOOTBALLS.','Carol eats 7 cats.']
for text in texts:
    mo = regex.search(text)
    print(mo)