while True:
    age = input('Enter your age:\n')
    if age.isdecimal():
        break
    print('please Enter a number of your age')

while 1:
    print('Selet a new password(letters and numbers only):')
    password = input()
    if password.isalnum():
        break
    print('Password can only have letters and numbers')

print(f'Success!\nAge:{age}\nPassword:{password}')
