# Taking screenshot using python

# importing the required modules
import pyautogui
import tkinter as tk
import time
import keyboard

# creating the root
root = tk.Tk()

# creating frame
c1 = tk.Canvas(root, width=300, height=300)
c1.pack()


# creating a function
def takeScreenshot():
	# time.sleep(2)
	keyboard.wait('esc')
	# take screenshot
	myScreenshot = pyautogui.screenshot()
	# save the screenshot
	myScreenshot.save('screenshot.png')
	# print("Screenshot has been saved to your current directory")
	print('Screenshot has been saved to your current directory')


# creating button
b = tk.Button(text='Take Screenshot', command=takeScreenshot, bg='green', fg='white', font=10)
# adding it to frame
c1.create_window(150, 150, window=b)

root.mainloop()
