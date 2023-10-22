import random, sys

print("Rock,   PAPER,  SCISSORS")

class Note:
    def __init__(self):
        self.next = None

rock = Note()
paper = Note()
scissors = Note()
rock.next = paper
paper.next = scissors
scissors.next = rock

# These variables keep track of the number of wins, losses, and ties
wins = 0
losses = 0
ties = 0

while True: # The main game loop
    print("%s  Wins,  %s  Losses,   %s  Ties" % (wins,losses,ties))
    while True: # The player input loop
        print("Enter your move : (r)rock, (p)paper, (s)scissors or (q)quit")
        player_move = input()
        if player_move =='q':
            sys.exit()  # Quit the program
        elif player_move in ['r','p','s']:
            break

    # Display what the player chose:
    if player_move == 'r':
        print("ROCK",end=' ')
        player_choice = rock
    elif player_move == 'p':
        print("PAPER",end=' ')
        player_choice = paper
    else:
        print("SCISSORS",end=' ')
        player_choice = scissors
    print("versus...")

    # Display what the program chose:
    computer_choice = random.choice((rock,paper,scissors))
    # Display and record the win/lose/tie
    if player_choice == computer_choice:
        print("It's a tie")
        ties+=1
    elif player_choice == computer_choice.next :
        print("You win")
        wins+=1
    else:
        print("You lose")
        losses+=1

