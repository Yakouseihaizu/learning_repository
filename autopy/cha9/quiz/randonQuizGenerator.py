# randomQuizGenerator.py - Creates quizzes with questions and answers in random order,
# along with the answer key

import random
import csv
import re
import pprint

# The quiz data. Keys are states and values are their capitals
capitals = {}
regex = re.compile(r'([a-zA-Z ]+)\t([a-zA-Z ]+)\t.*')
with open('states_capital.txt') as fp:
    content = fp.readlines()
    # pprint.pprint(content)
    for line in content:
        result = regex.search(line)
        capitals[result.group(1)] = result.group(2)

for quizNum in range(35):
    # TODO: Creat the quiz and answer key files
    quizFile = open(f'capitalsquiz{quizNum + 1}.txt','w')
    answerFile = open(f'capitalsquiz_answer{quizNum + 1}.txt','w')

    # TODO: Write out the header for the quiz
    quizFile.write(f'Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write(' '*20 + f'Capitals Quiz (Form:{quizNum+1})')
    quizFile.write('\n\n')
    
    # TODO: Shuffle the order of the states
    states = list(capitals.keys())
    random.shuffle(states)
    
    # TODO: Loop through all 50 states , making a question for each
    for questionNum in range(50):
        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[questionNum]
        wrongAnswers = random.sample(wrongAnswers,3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)

        quizFile.write(f'{questionNum+1}. What is the capital of {states[questionNum]}?\n')
        for i in range(4):
            quizFile.write(f"\t{'ABCD'[i]}. {answerOptions[i]}\n")
        quizFile.write('\n')
        answerFile.write(f"{questionNum+1}. {'ABCD'[answerOptions.index(correctAnswer)]}\n")


