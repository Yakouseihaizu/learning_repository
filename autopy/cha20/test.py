import pyautogui
import time
# wh = pyautogui.size()
# print(wh)
# print(wh.height)
# print(wh[0])

# for i in range(10):
#     # pyautogui.moveTo(1000,750,duration=1)
#     # pyautogui.moveTo(1000,1200,duration=1)
#     # pyautogui.moveTo(2000,1200,duration=1)
#     # pyautogui.moveTo(2000,750,duration=1)
#     pyautogui.move(300,0,duration=1)
#     pyautogui.move(0,300,duration=1)
#     pyautogui.move(-300,0,duration=1)
#     pyautogui.move(0,-300,duration=1)

# pyautogui.click(369,41,button='right')
# pyautogui.rightClick(369,42)
# pyautogui.doubleClick(330,760)
# pyautogui.mouseDown(330,760)
# pyautogui.mouseUp(330,760)
# time.sleep(1)
# pyautogui.scroll(200)

# pyautogui.mouseInfo()
# im = pyautogui.screenshot()
# im.save('sreenshot1.png')
# print(pyautogui.pixel(0,0))
# print(pyautogui.pixel(1000,1000))
# print(pyautogui.pixelMatchesColor(0,0,(60,60,60)))
# print(pyautogui.pixelMatchesColor(0,0,(30,30,30)))
# b = pyautogui.locateOnScreen('onenote.png')
# pyautogui.pixel()
# import pyautogui

# fw = pyautogui.getActiveWindow()
# print(fw.left,fw.top,fw.right,fw.bottom)
# print(fw.box)
# print(fw.size)
# print(fw.midleft,fw.midbottom,fw.midright,fw.midtop)
# print(fw.center)
# print(fw.topleft,fw.topright,fw.bottomleft,fw.bottomright)
# print(fw.area)

# import pyautogui,time

# fw = pyautogui.getActiveWindow()
# # time.sleep(5); fw.activate()
# # print(fw.isActive)
# # fw.close()
# fw.maximize()

# pyautogui.click(982,30)
# # pyautogui.write('Hello,world!',0.25)
# pyautogui.write(['a','b','left','left','XYZYZY','Y'])
# import pprint
# pprint.pprint(pyautogui.KEYBOARD_KEYS)
# pyautogui.keyDown('shift')
# pyautogui.press('4')
# pyautogui.keyUp('shift')

# import threading
# def keybreak():
#     time.sleep(3)
#     pyautogui.click(1418,1227)
#     pyautogui.hotkey('ctrl','c')

# th1 = threading.Thread(target=keybreak)
# th1.start()
# pyautogui.countdown(5)

time.sleep(10)
# print(pyautogui.position())
im = pyautogui.screenshot()
im.save('execl.png')