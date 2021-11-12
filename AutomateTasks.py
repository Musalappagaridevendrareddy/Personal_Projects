import time
from itertools import chain
import keyboard
import pyautogui

Count = int(input('Number of clicks:'))
Choice = input("Do you want to type any where:(yes or no)")
position, Type = [], []

if Choice == 'yes':
    Times = int(input('How many times do you want to type:'))
    for i in range(Times):
        print('---Enter On which click and text you want to type---')
        Type.append([int(input('On which click:')), input('Text:')])

for i in range(Count):
    keyboard.wait('esc')
    time.sleep(1)
    position.append([pyautogui.position().x, pyautogui.position().y])

print(position)
print(Type)
TimeToSleep = int(input('Time to sleep:'))
time.sleep(TimeToSleep)
c = 0
for i in range(Count):
    pyautogui.moveTo(position[i][0], position[i][1])
    time.sleep(1)
    pyautogui.click()
    time.sleep(2)
    if i+1 in chain(*Type):
        keyboard.write(Type[c][1])
        pyautogui.click()
        c += 1
    time.sleep(2)









