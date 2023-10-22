import pyautogui
import pyperclip

fwl = pyautogui.getWindowsWithTitle('Notepad')
fw = fwl[0]
fw.activate()
fw.maximize()

pyautogui.click(2082,1250)
pyautogui.hotkey('ctrl','a')
pyautogui.sleep(1)
pyautogui.hotkey('ctrl','c')
message = pyperclip.paste()
# print(message)
pyautogui.sleep(1)
pyautogui.click(2082,1250)
pyautogui.write(message)

