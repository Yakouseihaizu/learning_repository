# This is a guess the number game
import random

secret_number = random.randint(1,20)

print("I am thinking a number between 1 and 20")

# Ask the player to guess 6 times

for i in range(1,7):
    guess = int(input('Take a guess.\n'))

    if guess < secret_number:
        print('Your guess is too low.')
    elif guess > secret_number:
        print('You guess is too high')
    else:
        break

if guess == secret_number:
    print("Good job! You guessed my number in " + str(i) +" times.")
else:
    print("Nope. The number I was thinking of was " + str(secret_number)+'.')