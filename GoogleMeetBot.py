# Google Meet bot

# Import the required library's
import webbrowser
import time
from pynput.keyboard import Key, Controller
from datetime import datetime
from datetime import date
import calendar
import pandas as pd
from plyer import notification

keyboard = Controller()  # To control the keys in browser
schedule = pd.read_excel('schedule.xlsx')  # List of links to attend the class and also includes Timings


def notify(mes):  # Notifier when you join and entered out the meet
    title = "GoogleMeet"
    message = 'You ' + mes + ' the Meet'
    notification.notify(title=title, message=message, app_icon=None, timeout=10, toast=False)


def findDate():  # Checks if today date matches the list of dates in document
    born = date.today().weekday()
    return calendar.day_name[born]


def findTime():  # Returns the time
    now = datetime.now().time()
    return findDate(), now.hour, now.minute


def press_and_release(key):  # To press and release the keys
    keyboard.press(key)
    keyboard.release(key)


def open_link(link):  # This function opens the link provided in document which matches the requirements
    webbrowser.open(link)  # Opening via web browser
    time.sleep(4)
    for i in range(0, 1):  # Skipping the unwanted tabs
        press_and_release(Key.tab)
        time.sleep(1)
    # DISABLE CAMERA AND MIC AND ENTER ROOM
    for i in range(0, 6):
        press_and_release(Key.tab)
        if i in [2, 3]:
            press_and_release(Key.enter)  # Turn off mic and vedio
        time.sleep(1)

    press_and_release(Key.tab)
    time.sleep(1)
    press_and_release(Key.tab)
    press_and_release(Key.enter)  # Clicking on join button
    time.sleep(3)
    time.sleep(3100)  # This is the duration of the class if this completes it automatically enters out from the meet
    keyboard.press(Key.ctrl)
    keyboard.press('w')
    keyboard.release(Key.ctrl)  # By clicking ctrl + w
    keyboard.release('w')
    notify('Entered Out from')  # And it notifies you as you entered out from the meet
    lookup_schedule()  # After that it checks if any other meeting are short listed if exists it does the same process


def lookup_schedule():
    current_time = findTime()  # gets the current time
    row_count = len(schedule.index)  # counting the len of all data or rows
    print("CURRENT TIME:", current_time)  # Prints the current time
    for i in range(row_count):
        current_row = schedule.iloc[i]
        link = current_row['LINK']
        subject_time = current_row['TIME']
        day = current_row['DAY OF WEEK']
        hour = subject_time.hour
        minute = subject_time.minute
        look_up = (day, hour, minute)
        print("LOOKUP RESULT:", look_up)  # It will look into the schedule and if any of them matches
        if current_time == look_up:
            print("EXECUTING")
            notify('Entered in to')
            open_link(link)  # opens the link
    print('\n')


def background_process():
    lookup_schedule()
    time.sleep(1)


while True:
    background_process()
