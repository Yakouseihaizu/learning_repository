import requests
import os
import sys
import bs4
import time
import webbrowser
from pathlib import Path
# import logging
res = requests.get(strring := 'https://www.bing.com/images/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text,'html.parser')
time.sleep(1)

mimgs = soup.select('div.img_cont >img.mimg')
print(len(mimgs))
if len(mimgs) != 0:
    for mimg in mimgs[1:11]:
        image = mimg.get('src')
        print(image)
        res = requests.get(image)
        imageFile = open(f'images/No{mimgs.index(mimg)}.jpeg','wb')
        for chunk in res.iter_content(10_000):
            imageFile.write(chunk)
        # imageFile = open('images/'+os.path.basename(source),'wb')
        # res = requests.get(source)
        # for chunk in res.iter_content(10_000):
        #     imageFile.write(chunk)
        # imageFil

# from selenium import webdriver
# import sys
# import requests
# browser = webdriver.Firefox()
# browser.get('https://www.bing.com/images/search?q='+' '.join(sys.argv[1:]))

# images = browser.find_elements('css selector','div > div.imgpt > a')

# for image in images:
#     image.click()
#     image = browser.find_element('css selector','img.nofocus')
#     image.get_attribute('src')
    