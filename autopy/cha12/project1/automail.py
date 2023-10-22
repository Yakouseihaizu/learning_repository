from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys

browser = webdriver.Firefox()
browser.get('https://mail.zju.edu.cn/coremail/')

username = browser.find_element('css selector','#uid')
# username.click()
username.send_keys('3220104387')

password = browser.find_element('css selector', '#fakePassword')
password.send_keys('Yk20041229')

submit = browser.find_element('css selector','.submit')
submit.click()

import time
time.sleep(1)

writebtn = browser.find_element('css selector','button.u-btn:nth-child(1)')
writebtn.click()

time.sleep(1)
content = browser.find_element('css selector','html body.windows.firefox117.zh_CN section.m-layout.j-layout article.lymain section div.lycontent.j-layout-content div.j-layout-panel section.m-mail article.mlmain.mltabview div.mltabview-content.j-mlcnt div.mltabview-panel div.m-mlcompose div.main.j-main form.u-form.mn-form.j-form div.form-edr.j-form-edr div.ke-container.ke-container-xt5 div.ke-edit iframe.ke-edit-iframe')
content.send_keys(' '.join(sys.argv[3:]))

address = browser.find_element('css selector','div.u-form-item:nth-child(2) > input:nth-child(3)')
address.send_keys(sys.argv[1])
address.send_keys(Keys.ENTER)

topic = browser.find_element('css selector','.input')
topic.send_keys(sys.argv[2])

send = browser.find_element('css selector','span.u-btn-primary')
send.click()

# htmlFile = browser.find_element('tag name','html')
# htmlFile.send_keys('3220104387@zju.edu.cn')

browser.quit()
