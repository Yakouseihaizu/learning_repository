import random 
import sys

def getAnswer(answerNumber):
    if answerNumber == 1:
        return "It's certain"
    elif answerNumber == 2:
        return "It's decidely so"
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Rely hazy try again'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Concentrate and ask again'
    elif answerNumber == 8:
        return 'Outlook not so good'
    elif answerNumber == 9:
        return 'Very doubtful'
    
# r = random.randint(1,9)
# fortune = getAnswer(r)
# print(fortune)

# print(getAnswer(random.randint(1,9)))

print(sys.getsizeof('Y'))
