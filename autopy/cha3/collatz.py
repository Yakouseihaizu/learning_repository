def collatz(num):
    print(num)
    if num==1:
        pass
    elif num%2:
        return collatz(num*3+1)
    else :
        return collatz(num//2)
    
while True:
    try :
        number = input('Enter number:\n')
        if number == 'q':
            break
        else:
            collatz(int(number))
    except ValueError:
        print("Input a number, please")
