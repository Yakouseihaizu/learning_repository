formData = [
    {'name':'Alice','fear':'eavesdroppers','source':'wand',
     'robocop':4,'comments':'Tell Bob I said hi'},
    {'name':'Carol','fear':'puppets','source':'crystal ball',
     'robocop':1,'comments':'Please take the puppets out of the break room'},
    {'name':'Bob','fear':'bees','source':'amulet',
     'robocop':4,'comments':'n/a'},
    {'name':'Alex Murphy','fear':'ED-209','source':'money',
     'robocop':5,'comments':'Protect the innocent. Serve the public trust.Uphold the law'},
]

import pyautogui
pyautogui.sleep(5)
fwl = pyautogui.getWindowsWithTitle('Excel')
fw = fwl[0]
# fw.maximize()
# fw.activate()

pyautogui.click(106,396)
pyautogui.write(['right','right'])
for person in formData:
    print(f">>>Writing imformation of {person['name']}<<<")
    pyautogui.sleep(5)
    pyautogui.write(person['name']+'\t',0.5)
    pyautogui.hotkey('altleft','down')
    if person['fear'] == 'eavesdroppers':
        pyautogui.write(['enter','\t'],0.5)
    elif person['fear'] == 'bees':
        pyautogui.write(['down','enter','\t'],0.5)
    elif person['fear'] == 'puppets':
        pyautogui.write(['down','down','enter','\t'],0.5)
    elif person['fear'] == 'ED-209':
        pyautogui.write(['down','down','down','enter','\t'],0.5)
    pyautogui.write(person['source']+'\t',0.5)
    pyautogui.write(str(person['robocop']),0.5)
    pyautogui.write('\t',0.5)
    pyautogui.write(person['comments']+'\t',0.5)
    pyautogui.write('\n')
    
    


    




