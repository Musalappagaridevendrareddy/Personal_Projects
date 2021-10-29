from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from pynput.keyboard import Key, Controller
from datetime import datetime
from datetime import date
import calendar
import pandas as pd
from plyer import notification

keyboard = Controller()
schedule = pd.read_excel('schedule.xlsx')


def notify(mes):
    title = "GoogleMeet"
    message = 'You ' + mes + ' the Meet'
    notification.notify(title=title, message=message, app_icon=None, timeout=10, toast=False)


def findDate():
    born = date.today().weekday()
    return calendar.day_name[born]


def findTime():
    now = datetime.now().time()
    return findDate(), now.hour, now.minute


def press_and_release(key):
    keyboard.press(key)
    keyboard.release(key)


def open_link(link):
    options = Options()
    # edit this to your corresponding user data location for google chrome
    options.add_argument("user-data-dir=C:\\Users\\Dell\\AppData\\Local\\Google\\Chrome\\User Data\\")
    driver = webdriver.Chrome(options=options)
    driver.get(link)
    time.sleep(4)
    for i in range(0, 2):
        press_and_release(Key.tab)
        time.sleep(1)
    # DISABLE CAMERA AND MIC AND ENTER ROOM
    for i in range(0, 6):
        press_and_release(Key.tab)
        if i in [2, 3]: press_and_release(Key.enter) # changed 3 to 4
        time.sleep(1)

    press_and_release(Key.tab)
    time.sleep(1)
    press_and_release(Key.tab)
    press_and_release(Key.enter)
    time.sleep(3300)
    driver.close()
    notify('Entered Out from')
    lookup_schedule()


def lookup_schedule():
    current_time = findTime()
    row_count = len(schedule.index)
    print("CURRENT TIME:", current_time)
    for i in range(row_count):
        current_row = schedule.iloc[i]
        link = current_row['LINK']
        subject_time = current_row['TIME']
        day = current_row['DAY OF WEEK']
        hour = subject_time.hour
        minute = subject_time.minute
        look_up = (day, hour, minute)
        print("LOOKUP RESULT:", look_up)
        if current_time == look_up:
            print("EXECUTING")
            notify('Entered in to')
            open_link(link)
    print('\n')


def background_process():
    lookup_schedule()
    time.sleep(1)


while True: background_process()
