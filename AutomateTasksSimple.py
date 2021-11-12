import time

import keyboard
import pyautogui

Count = int(input('Number of clicks:'))
position = []
for i in range(Count):
    keyboard.wait('esc')
    time.sleep(1)
    position.append([pyautogui.position().x, pyautogui.position().y])

print(position)
TimeToSleep = int(input('Time to sleep:'))
time.sleep(TimeToSleep)
for i in range(Count):
    pyautogui.moveTo(position[i][0], position[i][1])
    pyautogui.click()
    time.sleep(5)
