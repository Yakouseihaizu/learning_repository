import re
import sys
# TODO: using regex to find the dateliked part
date_regex = re.compile(r'(\d{1,2})/(\d{1,2})/(\d{4})')
mo = date_regex.findall('29/22/2000')
dates = []

if mo:
    for date in mo:
        day = date[0]
        month = date[1]
        year = date[2]
        dates.append([day,month,year])
else:
    print('No date')
    sys.exit()
    
# print(dates)
# TODO: judge if the part is right for date
for date in dates:
    if int(date[2]) < 1000 or int(date[2]) > 2999:
        print('Year wrong')
        break
    if int(date[2])%4==0 and int(date[2])%100 :
        days_in_Feb = 29
    elif int(date[2])%400==0:
        days_in_Feb = 29
    else:
        days_in_Feb = 28
    _31_month = [1,3,5,7,8,10,12]
    _30_month = [4,6,9,11]
    # print(date)
    date_str = '-'.join(date)
    if int(date[1])==2:
        if int(date[0]) <= days_in_Feb:
            print(f"{date_str} is right")
        else:
            print(f"{date_str} is wrong")
    elif int(date[1]) in _31_month:
        if date[0] <= 31:
            print(f"{date_str} is right")
        else:
            print(f"{date_str} is wrong")
    elif int(date[1]) in _30_month:
        if date[0] <= 30:
            print(f"{date_str} is right")
        else:
            print(f"{date_str} is wrong")
    else:
        print('Wrong month')