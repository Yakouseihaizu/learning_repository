from selenium import webdriver

browser = webdriver.Firefox()
browser.get('https://inventwithpython.com/')
try:
    elem = browser.find_element('class name','card-img-top')
    print('Found <%s> element with that class name!' %(elem.tag_name))
except:
    print('Was not able to find an element with that name.')
# import time
# from selenium import webdriver
# browser = webdriver.Firefox()
# browser.get("https://www.baidu.com")
# browser.find_element_by_id("kw").clear()
# browser.find_element_by_id("kw").send_keys("刘亦菲")
# browser.find_element_by_id("su").click()
# time.sleep(5)
# browser.quit()
