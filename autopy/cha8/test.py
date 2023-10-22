# while  True:
#     age = input('Enter your age.\n')
#     try:
#         age = int(age)
#     except:
#         print('Please use numeric digits.')
#         continue
#     if age<1:
#         print('Please Enter a positive age')
#         continue
#     break

import pyinputplus as pyip
# # response = pyip.inputNum('Enter a number:  ',max=4)
# # response = pyip.inputNum('Enter a number:  ',min=4)
# # response = pyip.inputNum('Enter a number:  ',greaterThan=4)
# # response = pyip.inputNum('Enter a number:  ',lessThan=4)
# # print(response)
# # help(pyip.inputNum)

# # response = pyip.inputNum('Enter a number:   ')
# # response = pyip.inputNum('Enter a number:   ',blank=True)
# # print(response)
# # lst = ['sbjc','cbcsakjc','acbaj']
# # response = pyip.inputChoice(lst)
# # response = pyip.inputMenu(lst,)
# response = pyip.inputNum('Enter a number:',limit=2,default='N/A')
# # response = pyip.inputNum('Enter a number:',timeout=2,default='N/A')
# print(response)

# response = pyip.inputNum('Enter a number:  ',allowRegexes=[r'[IVCDM]+',r'zero'])
# response = pyip.inputNum('Enter a number:   ',blockRegexes=[r'[02468]$'])
# response = pyip.inputNum('Enter a number:  ',allowRegexes=['caterpillar','categpry'],blockRegexes=['cat'])
# print(response)


# def adds_up_to_ten(numbers):
#     numbersList = list(numbers)
#     for i,digit in enumerate(numbersList):
#         numbersList[i] = int(digit)
#     if (nsum :=sum(numbersList)) != 10:
#         raise Exception(f'The digits must add up to 10. not {nsum}')
#     return int(numbers)

# response = pyip.inputCustom(adds_up_to_ten,'Enter a number whose digits adding to 10:  ')

# print(response)

