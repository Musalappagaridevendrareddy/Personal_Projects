# Send mail with out SMTP Error

import time
import webbrowser
import keyboard
import pyautogui

ReceiverMail = 'whatiamgoingtobecome@gmail.com'  # Receiver mail
subject = 'Automating the mail'  # Subject to the mail
content = 'Testing the software'  # Content you want any thing to mention
webbrowser.open('www.gmail.com')  # opening the browser
keyboard.wait('esc')  # If you are having any process complete and press enter

time.sleep(3)  # waiting for some time
pyautogui.moveTo(97, 252)  # moving mouse to particular position
pyautogui.click()  # Tapping the position (Compose button)
time.sleep(2)  # waiting for some time
keyboard.write(ReceiverMail)  # Mentioning or entering the receiver mail
time.sleep(2)  # waiting for some time
keyboard.press_and_release('enter')  # clicking enter
time.sleep(2)  # waiting for some time
pyautogui.moveTo(1163, 519)  # Moving to particular position
pyautogui.click()  # Clicking or tapping
keyboard.write(subject)  # Writing the subject
time.sleep(2)  # waiting for some time
pyautogui.moveTo(1173, 586)  # Moving to particular position
pyautogui.click()  # waiting for some time
keyboard.write(content)  # Writing the content
keyboard.press_and_release('ctrl+enter')  # sending the mail