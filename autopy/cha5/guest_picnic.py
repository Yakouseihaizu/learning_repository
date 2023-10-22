import pprint

allGuests = {'Alice':{'apples':5,'prezels':12},
             'Bob':{'ham sandwiches':3,'apples':2},
             'Carol':{'cups':3,'apple pies':1}}
def total_brought(guest,item):
    num_brought = 0
    for k,v in guest.items():
        num_brought += v.get(item,0)
    return num_brought

print('Number of things being brought:')
print(' - Apples %s' %(total_brought(allGuests,'apples')))
print(' - Cups %s' %(total_brought(allGuests,'cups')))
print(' - Cakes %s' %(total_brought(allGuests,'cakes')))
print(' - Ham Sandwiches %s' %(total_brought(allGuests,'ham sandwiches')))
print(' - Apple pies %s' %(total_brought(allGuests,'apple pies')))
