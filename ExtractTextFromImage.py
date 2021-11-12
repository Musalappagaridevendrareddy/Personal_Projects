#  Extract text from image using python

import pytesseract  # Import the required library
from PIL import Image

image = Image.open('C:/Users/Dell/Desktop/download.jpg')  # Provide the path of the image to extract text
text = pytesseract.image_to_string(image)  # converting image containing text to string
print(text)  # printing the text
