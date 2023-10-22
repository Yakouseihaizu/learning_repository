# import pyinputplus as pyip
import random
import time
timelimit = 8
number_questions = 10
correct_answer = 0
for question_number in range(number_questions):

# pick 2 random number
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)
    prompt = f'#{question_number+1} {num1} x {num2} = '
    try_times = 0
    while try_times < 3:
        while True:
            try:
                kikan1 = time.time()
                response = input(prompt)
                kikan2 = time.time()
                if kikan2 - kikan1 >=timelimit:
                    response = 'timeout'
                else:
                    response = response.strip()
                    response = int(response)
            except ValueError:
                print('Please Enter a number')
                # try_times += 1
                if try_times ==2:
                    response = None
                    break
                else:   
                    try_times += 1
                    continue
            else:
                break
        if response != num1*num2:

            if response == 'timeout':
                print('timeout')
                try_times = 3
            elif response != None:
                print('Incorrect!')
                try_times+=1
            continue
        else:
            print('Corerect!!')
            correct_answer += 1
            try_times = 0
            break
    time.sleep(1)


print(f'Score: {correct_answer}/{number_questions}')