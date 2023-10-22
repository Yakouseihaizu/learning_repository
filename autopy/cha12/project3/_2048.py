from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get('https://iliaidakiev.github.io/NG_2048_workshop/')

htmlFile = browser.find_element('css selector','html')
while True:
    try:
        browser.find_element('css selector','#game-over-body > button')
    except:
        htmlFile.send_keys(Keys.UP)
        htmlFile.send_keys(Keys.RIGHT)
        htmlFile.send_keys(Keys.DOWN)
        htmlFile.send_keys(Keys.LEFT)
    else:
        break