# Convert the text in pdf to audio using python

# importing the required modules
import pyttsx3  # To convert text to speech
import PyPDF2  # Read data from text
import os  # To Play the mp3 file

# opening the required file
with open('C:/Users/Dell/Downloads/Sujan_2021.pdf', 'rb') as book:  # Open the readable file or mention path
    reader = PyPDF2.PdfFileReader(book)  # reading the file

    audio_reader = pyttsx3.init()  # Converting text into audio
    audio_reader.setProperty('rate', 200)  # Speed of speech here i set it to 200. You can increase or decrease
    # reading the content of each page using for loop
    for page in range(reader.numPages):  # Reading them
        next_page = reader.getPage(page)
        content = next_page.extractText()
        # saving the file
        audio_reader.save_to_file(content, 'my_audiobook.mp3')  # This file will be saved where current file is saved
        audio_reader.runAndWait()

os.startfile('my_audiobook.mp3')  # Playing the file
