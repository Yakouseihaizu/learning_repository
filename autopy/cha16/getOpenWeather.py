# getOpenWeather.py - Prints the weather for a location from the command line.

APPID = '0853e252548d0567b0e5c604a3541011'

import json,requests,sys,pprint

# Compute location from command line aarguments.
if len(sys.argv)<2:
    print('Usage: getOpenWeather.py city_name, 2-letter_country_code')
    sys.exit()
location = ' '.join(sys.argv[1:])

# TODO: Download the JSON data from OpenWeatherMap.org's API
url = 'https://api.openweathermap.org/data/2.5/forecast?q=%s&cnt=3&APPID=%s' %(location,APPID)

res = requests.get(url)
res.raise_for_status()

weather = json.loads(res.text)

w = weather['list']
print('Current weather in %s: '%(location))
print(w[1]['weather'][0]['main']+' - '+ w[1]['weather'][0]['description'])
print('Tomorrow:')
print(w[1]['weather'][0]['main']+' - '+ w[1]['weather'][0]['description'])
print()
print('Day after tomorrow:')
print(w[2]['weather'][0]['main']+' - '+ w[2]['weather'][0]['description'])

# jsonData = res.text
# TODO: Load JSON data into a Python variable
# pythonData = json.dump(res.text)
# print(pythonData)
# python = json.loads(res.text)
# jsont = json.dumps(python)
# # dict(python)
# # with open('new.json','w') as fp:
# #     json.dump(dict(),fp)

# with open('new.json','w') as fp:
#     # json.dump(jsont,fp)
#     fp.write(res.text)
