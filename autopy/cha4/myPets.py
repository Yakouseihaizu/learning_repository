my_pets = ['Zophie','Pooka','Fat-tail']
name = input("Enter a pet name\n")
if name not in my_pets:
    print(f"I don't have a pet named {name}")
else:
    print(f"{name} is my pet")
    
