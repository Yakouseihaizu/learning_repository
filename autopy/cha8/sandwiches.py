import pyinputplus as pyip
order = {}
breads = {'wheat':1,'white':3,'sourdough':4}
protiens = {'chicken':2,'turkey':3,'ham':4,'tofu':1}
cheeses = {'cheddar':2,'Swiss':4,'mozzarella':3}
bread = pyip.inputMenu(list(breads.keys()),lettered=True,prompt='chose your bread:\n')
order[bread] = breads[bread]
protien = pyip.inputMenu(list(protiens.keys()),lettered=True,prompt='chose your protien:\n')
order[protien] = protiens[protien]
cheese = pyip.inputYesNo('Would you like some cheese\n')
if cheese == 'yes':
    cheese_type = pyip.inputMenu(list(cheeses.keys()),lettered=True,prompt='chose your cheese:\n')
    order[cheese] = cheeses[cheese]
more = pyip.inputYesNo('Would you like some mayo, mustard, lettuce, tomato?\n')
if more == 'yes':
    order['more'] = 2
number = pyip.inputNum('How many sandwiches would you like to have?\n',min=1)

total = 0
print('The orders are as follow:')
for pieces,price in order.items():
    total+=price
    print(pieces)

print(f'total: ${total*number}')

