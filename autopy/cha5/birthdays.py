birthdays = {'Alice':'Apr 1','Bob':'Dec 12','Carol':'Mar 4'}

while True:
    name = input('Enter a name:(blank to quit) ')
    if name=='':
        break

    if name in birthdays:
        print(f'{birthdays[name]} is the birthday of {name}')
    else:
        print(f"I don't have a birthday information of {name}")
        bday = input("What's their birthday?\n")
        birthdays[name] = bday
        print('Birthday database updated')

