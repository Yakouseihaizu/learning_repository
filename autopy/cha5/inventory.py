# inventory.py
stuff = {'rope':1,'torch':6,'gold coin':42,'dagger':1,'arrow':12}

def display_inventory(inventory):
    print('Inventory:')
    total = 0

    for k,v in inventory.items():
        try :
            total += v    
            print(f'{v} {k}')
        except TypeError:
            print(f'Please input int for {k}')
    print(f'Total number of items: {total}')

def add_to_inventory(inventory,added_items):
    for item in added_items:
        inventory.setdefault(item,0)
        inventory[item] += 1
    
dragon_loot = ['gold coin','dagger','gold coin','gold coin','ruby']

display_inventory(stuff)
add_to_inventory(stuff,dragon_loot)
display_inventory(stuff)