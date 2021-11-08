# Jarvis Virtual Assistant

# Importing the required libraries
import difflib
import subprocess
import time
import playsound
import psutil
import pyfiglet
import pyjokes
import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pywhatkit
import speedtest
import wikipedia
import keyboard
import os
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import json
import ctypes
from datetime import date
import winshell
import pyautogui
from colorama import Back, Fore, Style
from prettytable import PrettyTable

# Specify the Column Names while initializing the Table
myTable = PrettyTable(["Query", "Explanation"])  # Creating a table to display the tasks which are performed

# Add rows
myTable.add_row(["Open Facebook", "Just opens www.facebook.com"])
myTable.add_row(["Open Google and search for devendar", "opens www.google.com and search for devendar"])
myTable.add_row(["Send Mail", "You can give mail id and subject and content it will send mail"])
myTable.add_row(
    ["Open google and search for reverse integer python", "it opens your browser and search for your query"])
myTable.add_row(['Open groove music', "Open any app form your pc"])  # Not only music but any app
myTable.add_row(["Turn on bluetooth", "Turns on bluetooth"])
myTable.add_row(["Turn on wifi", "Turns on wifi"])
myTable.add_row(["Open youtube", 'Opens www.youtube.com'])
myTable.add_row(["weather today", "opens google and search for weather"])
myTable.add_row(["make a call", "opens your phone app"])  # If you mention any name or phone number it will make a call
myTable.add_row(["what day it is", "tells today's name of day"])
myTable.add_row(["what is the time now", "tells the time now"])
myTable.add_row(["today's date", "tells today's date"])
myTable.add_row(["tell me a joke or Feeling bored", "Tells you jokes"])
myTable.add_row(["Find DeadlyDevilDev", "It will search for DeadlyDevilDev in any file if you have opened it"])
# Search of any word mentioned
myTable.add_row(["search for DeadlyDevilDev in wikipedia", "It speaks ok the main content"])
myTable.add_row(["What is my age", "Asks you to enter the date of birth and speaks out your age"])
myTable.add_row(["what is the news today", "Speaks out news"])  # Main headlines
myTable.add_row(["Lock pc", "Locks pc"])
myTable.add_row(["Shutdown pc", "Shutdowns your pc"])
myTable.add_row(["Minimise all windows", "Minimises all windows"])
myTable.add_row(["Empty recycle bin", "Deletes all files in recycle bin"])
myTable.add_row(["Check Internet speed", "Speaks out your upload and download speed"])
myTable.add_row(["Say hello to ----", "Says hello to ----"])
myTable.add_row(["Convert text file to handwritten", "Asks file path and convert it to handwritten"])
myTable.add_row(["Cpu condition", "Speaks out the condition of CPU"])
myTable.add_row(["Can i change your name", "You can change even more not only name"])
myTable.add_row(["-------", "And So on"])


def age(dtob):  # To calculate date of birth
    today = date.today()
    return today.year - dtob.year - ((today.month, today.day) < (dtob.month, dtob.day))


def Mail():  # To send mail
    sender_mail = pyautogui.password(text='Enter Sender MailID', title='Mail', default='', mask='❤')
    speak('What is the subject?')
    subject = takeCommand()
    speak('What is the content?')
    content = takeCommand()
    webbrowser.open('www.gmail.com')
    keyboard.wait('esc')
    time.sleep(3)
    pyautogui.moveTo(97, 252)
    pyautogui.click()
    time.sleep(2)
    keyboard.write(sender_mail)
    time.sleep(2)
    keyboard.press_and_release('enter')
    time.sleep(2)
    pyautogui.moveTo(1163, 519)
    pyautogui.click()
    keyboard.write(subject)
    time.sleep(2)
    pyautogui.moveTo(1173, 586)
    pyautogui.click()
    keyboard.write(content)
    speak('Please Cross check your details!')
    keyboard.wait('esc')
    keyboard.press_and_release('ctrl+enter')


def TextToHandWritten():  # To convert text file to handwritten
    from tkinter import filedialog as f
    speak('Select document to convert.')
    filename = f.askopenfilename()
    print(filename)
    f = open(filename, 'r')
    a = ""
    for l in f:
        a += l
    pywhatkit.text_to_handwriting(a, rgb=[0, 0, 0])
    speak('Your handwritten document is saved go and take a look.')


def Call(query):  # To make a call
    keyboard.press_and_release('windows')
    time.sleep(3)
    keyboard.write('Your phone')
    time.sleep(5)
    keyboard.press_and_release('enter')
    keyboard.wait('Esc')
    time.sleep(3)
    pyautogui.moveTo(1641, 123)
    time.sleep(3)
    pyautogui.click()
    keyboard.write(query)
    time.sleep(2)
    keyboard.press_and_release('enter')
    pyautogui.moveTo(1669, 845)
    time.sleep(3)
    pyautogui.click()


def Open(p_name):  # To open any app
    keyboard.press_and_release('windows')
    time.sleep(2)
    keyboard.write(p_name)
    time.sleep(1)
    keyboard.press_and_release('enter')
    time.sleep(3)
    if 'groove' in p_name:
        keyboard.press_and_release('space')


def takeCommand():  # It takes microphone input from the user and returns string output
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print(f'{Fore.BLACK}{Style.BRIGHT}{Back.RED}L{Back.YELLOW}i{Back.GREEN}s{Back.BLUE}t{Back.MAGENTA}e{Back.CYAN}n{Back.LIGHTRED_EX}i{Back.GREEN}n{Back.WHITE}g{Back.WHITE}...')
        # Above line is for the loading animation
        r.pause_threshold = 0.7
        audio = r.listen(source)

        try:
            print(Fore.GREEN + Back.LIGHTBLACK_EX + "Recognizing")
            Query = r.recognize_google(audio, language='en-in')
            print(f'{Fore.RED}Y{Fore.YELLOW}o{Fore.GREEN}u {Fore.BLUE}S{Fore.MAGENTA}a{Fore.CYAN}i{Fore.GREEN}d', end=':-')
            print(Query)
            print()

        except Exception as e:
            print(e)
            print(f"{Fore.RED}{Back.BLACK}{Style.BRIGHT}Say that again sir, I didn't get you")
            return "None"

        return Query


def speak(audio):  # It takes string input from the user and speaks it out
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(audio)
    engine.runAndWait()


def tellDay():  # To tell the day
    day = datetime.datetime.today().weekday() + 1

    Day_dict = {1: 'Monday', 2: 'Tuesday',
                3: 'Wednesday', 4: 'Thursday',
                5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}

    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
        speak("Today is " + day_of_the_week)


def tellTime():  # To tell the time
    time = str(datetime.datetime.now())

    print(time)
    hour = time[11:13]
    min = time[14:16]
    speak("The time is " + hour + "Hours and" + min + "Minutes sir")


def InternetSpeed():  # To check the internet speed
    test = speedtest.Speedtest()

    test.get_servers()  # get list of servers

    download_result = test.download()  # performing test

    upload_result = test.upload()
    ping_result = test.results.ping

    speak(f'Download speed: {download_result / 1024 / 1024:.2f} Mbit/s')  # print the results
    speak(f'Upload speed: {upload_result / 1024 / 1024:.2f} Mbit/s')
    speak(f'Ping: {ping_result:.2f} ms')


def wishMe(name):  # To wish the user
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak(f"Good Morning {name}!")

    elif 12 <= hour < 18:
        speak(f"Good Afternoon {name}!")

    else:
        speak(f"Good Evening {name}!")


def Remember(ques, ans):  # To remember things or to store unknown things
    if os.path.isfile('./remember.json'):
        with open('remember.json', 'r+') as f:
            json_data = json.load(f)
            json_data[ques] = ans
            f.seek(0)
            f.write(json.dumps(json_data))
            f.truncate()
    else:
        Dict = {ques: ans}
        with open("remember.json", "w") as outfile:
            json.dump(Dict, outfile)


def Hello():  # To greet the user
    ascii_banner = pyfiglet.figlet_format('         J A R V I S')
    print(ascii_banner)
    print('    -----------------------------------------------------------')
    print('    -----------------------------------------------------------')
    playsound.playsound('Jarvis.mp3', False)
    time.sleep(25)
    TF = Memory("what's my name")
    if TF:
        wishMe(TF)
    else:
        speak("Welcome sir, before further proceedings.")
        speak("Let me know your name!")
        name = takeCommand()
        Remember("what's my name", name)
        speak(f"Nice meeting you {name}. I'm your personal assistant.")
    speak("How can i help you?")


def Memory(query):  # To retrieve the remembered things
    try:
        with open('remember.json', 'r+') as file:
            json_data = json.load(file)
            for ques, ans in json_data.items():
                if ques == query:
                    return ans
    except:
        return False


def Take_query():  # To take the query from the user
    Hello()
    while True:
        query = takeCommand().lower()
        if query.startswith('jarvis'):  # Allowing the user to take action only when he /she says Jarvis at the beginning
            query = query.replace('jarvis', '').strip()  # Removing the Jarvis from the query
            if "open facebook" in query:
                speak("Opening Facebook ")
                webbrowser.open("www.facebook.com")
                continue
            elif 'what can you do' in query:
                speak('I can the following tasks')
                print(myTable)
                continue
            elif 'mail' in query:
                speak('Opening main in web browser')
                Mail()
                continue
            elif "open google" in query:
                speak("Opening Google")
                webbrowser.open("www.google.com")
                if 'search' in query:
                    query = query.replace('open google', '')
                    query = query.replace('and search for', '')
                    speak(f"Searching for {query}")
                    keyboard.write(query)
                    keyboard.press_and_release('enter')
                continue

            elif 'weather today' in query:
                speak('Searching in google')
                webbrowser.open('weather today')
                continue

            elif 'call' in query or 'dail' in query:
                query = query.replace('call', '')
                query = query.replace('dail', '')
                speak(f'Calling {query}')
                Call(query)
                continue

            elif "open youtube" in query:
                speak("Opening Youtube")
                webbrowser.open("www.youtube.com")
                continue

            elif "day it is" in query:
                tellDay()
                continue

            elif "today's date" in query:
                today = date.today()
                speak(today.strftime("%B %d %Y"))
                continue

            elif "time now" in query:
                tellTime()
                continue

            elif 'how are you' in query or 'how day' in query:
                speak("I'm fine. Thanks")
                speak("how do you do")
                continue

            elif 'fine' in query or "good" in query:
                speak("It's good to know that you are fine")
                continue

            elif "see you later" in query or 'bye' in query or 'offline' in query:
                speak("Thanks for spending some time with me.")
                hour = datetime.datetime.now().hour
                TF = Memory("what's my name")
                if TF:
                    if (hour >= 21) and (hour < 6):
                        speak(f"Good Night {TF}! Have a nice Sleep")
                    else:
                        speak(f"Bye {TF}")
                exit()

            elif "who made you" in query or "who created you" in query or "who is your boss" in query:
                speak("I have been created by DeadlyDevilDev.")
                continue

            elif 'joke' in query or 'feeling bored' in query or 'boring' in query:
                speak('Let me tell you nice joke')
                speak(pyjokes.get_joke())
                speak("How's that!")
                continue

            elif "from wikipedia" in query:
                speak("Checking the wikipedia ")
                query = query.replace("wikipedia", "")

                result = wikipedia.summary(query, sentences=4)
                speak("According to wikipedia")
                speak(result)
                continue

            elif "my age" in query:
                Age = Memory(query)
                if Age:
                    speak(f"You are {Age} years old")
                else:
                    speak('Enter your date of birth')
                    db = list(map(int, input('Example:(2000 05 19):').split(' ')))
                    cal_age = age(date(db[0], db[1], db[2]))
                    Remember(query, cal_age)
                    speak(f"You are {cal_age} years old")
                continue
            elif "who are you" in query:
                speak("I'm your Jarvis your virtual assistant created by Devendar")
                continue
            elif 'who is devendar' in query or 'who is devendra' in query:
                speak('He is my boss')
                continue
            elif 'cpu' in query:
                speak(f'Cpu is at {str(psutil.cpu_percent())}')
                continue
            elif 'volume' in query:  # to change the volume by increasing or decreasing
                vol = int(''.join(filter(str.isdigit, query)))
                vol = vol * -1 if 'decrease' in query else vol
                devices = AudioUtilities.GetSpeakers()
                interface = devices.Activate(
                    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
                volume = cast(interface, POINTER(IAudioEndpointVolume))
                currentVolumeDb = volume.GetMasterVolumeLevel()
                volume.SetMasterVolumeLevel(currentVolumeDb + vol, None)

                speak("volume level's changed!")
                continue

            elif 'internet speed' in query:
                speak('Checking wait a minute')
                InternetSpeed()
                continue

            elif 'convert text file to handwritten' in query:
                TextToHandWritten()
                continue

            elif 'news today' in query:

                import requests
                from bs4 import BeautifulSoup

                url = 'https://www.bbc.com/news'
                response = requests.get(url)

                soup = BeautifulSoup(response.text, 'html.parser')
                headlines = soup.find('body').find_all('h3')
                for x in headlines:
                    speak(x.text.strip())
                continue

            elif 'lock pc' in query or 'lock my computer' in query:
                speak("locking the device")
                ctypes.windll.user32.LockWorkStation()
                continue

            elif 'say hello to' in query:
                query = query.replace('say hello to', '')
                speak(f'Hello {query}')
                continue

            elif "screenshot" in query:  # to take screenshot
                speak('Taking screenshot')
                pyautogui.screenshot(str(time.time()) + ".png").show()
                continue

            elif "i love you" in query:
                speak("Sorry! I'm in love with Devendar")
                continue

            elif 'shutdown system' in query:
                speak("Hold On a Sec ! Your system is on its way to shut down")
                subprocess.call('shutdown / p /f')
                continue
            elif 'bluetooth' in query:
                speak('Changing bluetooth state')
                keyboard.press('windows+a')
                pyautogui.moveTo(1667, 512)
                pyautogui.click()
                continue
            elif 'wifi' in query:
                speak('Changing wifi state')
                keyboard.press('windows+a')
                pyautogui.moveTo(1506, 509)
                pyautogui.click()
                continue
            elif 'empty recycle bin' in query:
                try:
                    winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
                    speak("Recycle Bin Recycled")
                except:
                    speak('Nothing exists in recycle bin')
                continue

            elif "minimize all" in query or 'minimise all' in query:
                keyboard.send('windows+d')
                continue
            elif 'find' in query:
                query = query.replace('find', '')
                keyboard.press_and_release('ctrl+f')
                keyboard.write(query)
                continue
            elif 'open' in query:
                query = query.replace('open ', '')
                speak(f"Opening {query}")
                Open(query)
                continue
            elif 'change' in query or 'update' in query:  # To update your query
                try:
                    query = query.replace('change', '').strip()
                    query = query.replace('update', '').strip()
                    with open('remember.json', 'r+') as file:
                        json_data = json.load(file)
                        file.close()

                        Bmatch = difflib.get_close_matches(query, json_data)
                        speak('Enter Updated text answer')
                        print(Bmatch)
                        UpAns = input("Enter your answer:")
                        for key in Bmatch:
                            json_data[key] = UpAns
                        print(json_data[Bmatch[0]])

                        File = open('remember.json', 'w+')
                        File.write(json.dumps(json_data))
                        File.close()
                except:
                    speak("Nothing to change or update. I'm really sorry for that!")
                continue

            elif Memory(query):
                speak(Memory(query))
                continue
            else:
                speak("I don't know. If you let me, i will remember")
                answer = takeCommand()
                Remember(query, answer)
                speak('Really! Nice')


if __name__ == '__main__':
    Take_query()
