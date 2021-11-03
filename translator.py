# Language translator using python

# Importing the required library
from translate import Translator

in_lang = input("Enter your in language:")  # Asking the user to enter the original language in which he is entering
to_lang = input("Enter your to language:")  # Asking the user to enter the language name to convert
text = input("Type your text:")  # Text to convert
try:
	translator = Translator(from_lang=in_lang, to_lang=to_lang)  # Translator to convert the text
	result = translator.translate(text)  # Translating
	print(result)  # Printing the result
except:
	print("Error! Sorry for this try again. Provide network connection or Provide correct words")
