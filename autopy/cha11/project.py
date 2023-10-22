import random
import logging
logging.basicConfig(filename='Log.txt',format='%(asctime)s %(levelname)s %(message)s',level=logging.DEBUG)
logging.critical('START')
guess = ' '
times = 0
while guess not in ('heads','tails'):
    guess = input('Guess the coin toss! Enter heads or tails:\n')
    logging.debug('guess is %s' %(guess))
toss = random.randint(0,1) # 0 is tails, 1 is heads
logging.debug('toss is %s' %(toss))
if toss == guess:
    print('You got it! ')
else:
    times+=1
    print('Nope! Guess again!')
    guess = input()
    logging.debug('guess is %s' %(guess))
    if toss == guess:
        print('You got it.')
    else:
        print('Nope. You are really bad at this game.')

logging.critical('END')