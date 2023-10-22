
# import traceback

# try:
#     raise Exception('This is the error message.')
# except:
#     error_file = open('errorInfo.txt','w')
#     error_file.write(traceback.format_exc())
#     error_file.close()
#     print('The traceback info was written to errorInfo.txt .')

# ages = [26,57,92,54,22,15,17,80,47,73]
# ages.sort()

# assert ages[0] >= ages[-1]
# import unittest

# class Ages:
#     def __init__(self) -> None:
#         self.list = []

#     def add_to_list(self,new):
#         self.list.append(new)
    
#     def show_list(self):
#         print(self.list)

# class TestAges(unittest.TestCase):
#     def setUp(self):
#         self.years = Ages()
#         self.set=[]
#         for new in [23,46,75,4,7,3,54]:
#             self.years.add_to_list(int(new))
#             self.set.append(int(new))
#     def test_single_age(self):
#         test = self.set[0]
#         self.assertIn(test,self.years.list)
#     def test_multi_ages(self):
#         for test in self.set[:-1]:
#             test = self.set[:-1]
#         for test in self.set[:-1]:
#             self.assertIn(test,self.years.list)
    
# if __name__ == '__main__':
#     unittest.main()

# market_2nd = {'ns':'green','ew':'red'}
# mission_16th = {'ns':'red','ew':'green'}

# def switchLights(stoplight):
#     for key in stoplight.keys():
#         if stoplight[key] == 'green':
#             stoplight[key] = 'yellow'
#         elif stoplight[key] == 'yellow':
#             stoplight[key] = 'red'
#         elif stoplight[key] == 'red':
#             stoplight[key] = 'green'
#     assert 'red' in stoplight.values() #, f'Neither light is red! {stoplight}'

# switchLights(market_2nd)
# switchLights(mission_16th)

# print('Enter the first number to add:')
# first = input()
# second = input('Enter the second number to add:\n')
# third = input('Enter the third number to add:\n')
# print('The sum is %s' %(int(first)+int(second)+int(third)))

# number = int(input('int: '))
# assert number>=10 

# eggs = input('eggs: ').lower()
# bacon = input('bacon: ').lower()
# assert eggs==bacon 

# assert False
import logging
logging.basicConfig(filename='logs',format='%(acsdate)s %(levelname)s %(message)s',level=logging.DEBUG)
