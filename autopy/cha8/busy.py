import pyinputplus as pyip

while True:
    answer = pyip.inputYesNo('Want to konew how to make a person busy for hours?\n',
                             yesVal='yes',noVal='no',allowRegexes=['yes'])
    if answer == 'no':
        break
    else:
        print(answer)
        continue
print('Thank you, have a nice day!')
