import logging
# logging.disable(logging.ERROR)
logging.basicConfig(filename='myProgramLog',filemode='w',level=logging.INFO,format='%(asctime)s - %(levelname)s - %(message)s')

logging.critical('start program')

def factorial(n):
    logging.debug('Start for factorial(%s)' %(n))
    total = 1
    for i in range(1,n+1):
        total *= i
        logging.debug(f'i is {i}, total is {total}')
    logging.debug('End for factorial(%s)' %(n))
    return total

print(factorial(5))
logging.debug('End for program')
logging.basicConfig()
string = '%(value)s'.format(value=1)
print(string)