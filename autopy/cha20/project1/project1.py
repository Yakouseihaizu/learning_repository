import pyautogui
import time,datetime
start = datetime.datetime.now()
dt = datetime.timedelta(seconds=60*10)

while datetime.datetime.now() < start+dt:
    pyautogui.move(2,2,duration=0.01)
    pyautogui.move(-2,-2,duration=0.01)