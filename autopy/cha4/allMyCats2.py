cat_names=[]
while True:
    name = input(f"Enter the name pf cat {len(cat_names)+1} (Or enter nothing to quit):\n")
    if name:
        cat_names.append(name)
    else:
        break
print("The cat names are:")
for name in cat_names:
    print('\t'+ name)
