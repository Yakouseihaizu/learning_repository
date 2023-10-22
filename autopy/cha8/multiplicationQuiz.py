import pyinputplus as pyip
import random
import time

number_questions = 10
correct_answer = 0
for question_number in range(number_questions):

# pick 2 random number
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)
    prompt = f'#{question_number} {num1} x {num2} = '

    try :
        response = pyip.inputStr(prompt=prompt,limit = 3,timeout=8,allowRegexes=[f'^{num1*num2}$'],blockRegexes=[(r'\.*','Invalid!')])
    except pyip.RetryLimitException:
        print('Out of time!')
    except pyip.TimeoutException:
        print('out of tries!')
    else:
        print('Correct!')
        correct_answer+=1
    time.sleep(1)

print(f'Score: {correct_answer}/{number_questions}')


