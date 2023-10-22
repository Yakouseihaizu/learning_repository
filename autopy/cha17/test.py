# import time
# import sys

# # sys.set_int_max_str_digits(460000)

# def calProd():
#     # Calculate the product of the first 100,,000 numbers
#     product = 1
#     for i in range(1,100_000):
#         product = product*i
#     return product

# startTime = time.time()
# prod = calProd()
# endTime = time.time()
# print('The result is %s digits long.' %(len(str(prod))))
# print('Took %s seconds to calculate.' %(endTime-startTime))

# import time
# print(time.ctime())
# time.sleep(1)
# thisMoment = time.time()
# print(time.ctime(thisMoment))

# import time
# for i in range(3):
#     print('Tick')
#     time.sleep(1)
#     print('Tock')
#     time.sleep(1)
# time.sleep(5)

# import time
# now = time.time()
# print(round(now,2))
# print(round(now,4))
# print(round(now))


# import datetime,time
# # print(datetime.datetime.now())
# halloween2019 = datetime.datetime(2019,10,31,0,0,0)
# oct_31_2019 = datetime.datetime(2019,10,31,0,0,0)
# newyear2024 = datetime.datetime(2024,1,1)
# print(halloween2019 == oct_31_2019)
# print(newyear2024>oct_31_2019)
# print(oct_31_2019>newyear2024)
# print(newyear2024!=oct_31_2019)

# import datetime,time
# print(datetime.datetime.fromtimestamp(1_000_000))
# print(datetime.datetime.fromtimestamp(time.time()))

# import datetime
# delta = datetime.timedelta(days=11,hours=10,minutes=9,seconds=8)
# print((delta.days,delta.seconds,delta.microseconds))
# print(delta.total_seconds())
# print(delta)

# import datetime,time
# dt = datetime.datetime.now()
# thousandDays = datetime.timedelta(days=1000)
# fivesecond = datetime.timedelta(seconds=5)
# time.sleep(fivesecond.total_seconds())
# print(dt)
# print(dt+thousandDays)
# print(dt+2*thousandDays)

# import datetime

# # oct21st = datetime.datetime(2019,10,21,16,29,0)
# # print(oct21st.strftime('%Y/%m/%d %H:%M:%S'))
# # print(oct21st.strftime('%I:%M  %p'))
# # print(oct21st.strftime('%B of %Y'))

# Nov_63 = datetime.datetime.strptime('November of 63','%B of %y')
# print(Nov_63)
# Nov_1963 = datetime.datetime.strptime('November of 1963','%B of %Y')
# print(Nov_1963)
# Oct21st_2019 = datetime.datetime.strptime('Oct 21, 2019','%b %d, %Y')
# print(Oct21st_2019)
# now = datetime.datetime.strptime('2019/10/21  16:29:00','%Y/%m/%d  %H:%M:%S')
# print(now)

# import time,datetime,threading

# startTime = datetime.datetime(2029,10,31,0,0,0)
# while datetime.datetime.now() < startTime:
#     time.sleep(1)
# print('Program noe starting on Helloween 2029')

# import threading,time
# print('Start of program')
# def takeANap():
#     print('start!')
#     time.sleep(5)
#     print('Wake up')
# threadObj = threading.Thread(target=takeANap)
# threadObj.start()

# print('End of program')

# import threading
# threadObj = threading.Thread(target=print,args=['Cats','Dogs','Frog'],kwargs={'sep':' & '})
# threadObj.start()

# import subprocess
# # subprocess.Popen('C:\\Windows\\System32\\calc.exe')
# # subprocess.Popen(['C:\\Windows\\notepad.exe','C:\\Users\\HUAWEI\\Desktop\\autop\\cha17\\new.txt'])
# # "C:\Users\HUAWEI\AppData\Local\Microsoft\WindowsApps\Microsoft.Paint_8wekyb3d8bbwe\mspaint.exe"
# subprocess.Popen(["C:\\Users\\HUAWEI\\AppData\\Local\\Programs\\Python\\Python311\\python.exe","C:\\Users\\HUAWEI\\Desktop\\autopy\\cha1-2\\hello.py"])


# import time,subprocess
# timeLeft = 60
# while timeLeft > 0:
#     print(timeLeft)
#     time.sleep(1)
#     timeLeft-=1

# subprocess.Popen(['start','alarm.wav'],shell=True)
print('#'+'ABC'.rjust(4)+'#')
