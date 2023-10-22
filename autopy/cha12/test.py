# import webbrowser
# webbrowser.open('https:/google.com/')

import bs4
import requests
import logging
import lxml
logging.basicConfig(filename='logging.txt',filemode='w',format='- %(message)s',level=logging.DEBUG)
logging.critical('START')
# res = requests.get('https://nostarch.com')
# logging.debug('form a response named "res"')
# res.raise_for_status()
# logging.debug('resopnse checked over')

# noStarchSoup = bs4.BeautifulSoup(res.text,'html.parser') 
# logging.debug('form a BeautifulSoup ')

# exampleFile = open('example.html')
# logging.debug('open exapmle.html')
# exampleSoup = bs4.BeautifulSoup(exampleFile,'lxml')
# logging.debug('form BeautifulSoup named exampleSoup')
# elems = exampleSoup.select('#author')
# logging.debug(f'find {len(elems)} id=author elements ')
# logging.debug(f'elems: {type(elems)}')
# logging.debug('show elems')
# for elem in elems:
#     logging.info(f'elem{elems.index(elem)}: {elem}')
#     print(elem)
#     print(str(elem))
#     print(elem.getText())
#     print(elem.attrs)
#     print('--------------')
# print()
# logging.info('STOP id=author HERE')
# logging.info('')
# print()

# pelems = exampleSoup.select('p')
# logging.debug(f'find {len(pelems)} paragraph elements')
# for pelem in pelems:
#     logging.info(f"pelem{pelems.index(pelem)}: {pelem}")
#     print(pelem)
#     print(pelem.getText())
#     print(pelem.attrs)
#     print('-----------------')
# print()
# exampleFile.close()

# logging.critical('END')

# from selenium import webdriver

# browser = webdriver.Firefox()
# browser.get('https://inventwithpython.com')

# linkElem = browser.find_element('link text','Read Online for Free')
# linkElem.click()

# from selenium import webdriver
# browser = webdriver.Firefox()
# browser.get('https://login.metafilter.com/')

# loginName = browser.find_element('id','user_name')
# loginName.send_keys('diaiboaobv')

# passWord = browser.find_element('id','user_pass')
# passWord.send_keys('acuiejbicauh')

# passWord.submit()

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get('https://inventwithpython.com')
classElem = browser.find_element('css selector','#mce-EMAIL')
classElem.send_keys('jsasajbskj')
time.sleep(3)
classElem.clear()
# print(classElem.tag_name)
# print(classElem.text)
# classElem.clear()
# print(classElem.text)
# htmlElem = browser.find_element('tag name','html')
# htmlElem.send_keys(Keys.DOWN)
# time.sleep(3)
# htmlElem.send_keys(Keys.UP)