# -*- coding: utf-8 -*-

"""
Python 3
@author: Shagun Chauhan
Project: Image to Text and Text to Speech Conversion
"""

# for GUI use and image input
import tkinter
from tkinter.filedialog import askopenfilename

# check the ype of file
import filetype

# safe way to exit the program
from sys import exit

# detects language of the text
from langdetect import detect

# convert the image to text string 
import pytesseract	 

# adds image processing capabilities 
from PIL import Image	 

# converts the text to speech 
from gtts import gTTS 
import os 	 

# translates text into the desired language 
import google_trans_new
from google_trans_new import google_translator	 

# creating a root window
root = tkinter.Tk()

#use to hide tkinter window
#root.withdraw() 

# shows an "Open" dialog box and return the path to the selected file
path = askopenfilename(initialdir = root, title = "Select image to translate", filetypes = [("png files","*.png"), ("jpeg files","*.jpg")]) 

# destroy the GUI components
root.destroy()
    
# check if a file is selected or not
if len(path) != 0:
    # check if selected file is image or not
    if not(filetype.is_image(path)):
        print("Selected file is not an image")
        exit()
    
    # open an image from the source path
    img = Image.open(path)	 
else:
    print("No file Selected")
    exit()

# describes image format in the output 
print("\nImage Format: ")
print(img)	
					 
# path where the tesseract module is installed 
pytesseract.pytesseract.tesseract_cmd ='./tesseract.exe'

# converts the image to result and saves it into result variable 
result = pytesseract.image_to_string(img) 

# check if a file has text or not
if len(result) == 0:
    print("Selected File contains no text")
    exit()

# write text in a text file and save it to source path 
print("\nInput text:")
with open('test.txt',mode ='w') as file:	 
	file.write(result) 
	print(result) 

# list out keys and values separately from dictionary
key_list = list(google_trans_new.LANGUAGES.keys())
val_list = list(google_trans_new.LANGUAGES.values())

# print the languages to which text can be translated
print("\nLanguages:")
print(', '.join(val_list))

# convert text into desired language
output_lang_value = input("Enter the output language: ")
output_lang_value = output_lang_value.lower()

# check if text can be translated into desired language
if output_lang_value not in val_list:
    print("\nCan't translate to this language")
    exit()
else:
    output_lang_key = key_list[val_list.index(output_lang_value)]

# helps to do the translation
Translator = google_translator()		
			 
# translates the text into desired language 
try:
    input_lang = detect(result)
    output_text = Translator.translate(result, lang_src=input_lang, lang_tgt=output_lang_key)
except:
    print("Selected File contains no text")
    exit()

# print the translated text
print("\nOutput text:") 
print(output_text) 

# Text-to-speech conversion
# Passing the text and language to the engine
try:
    engine = gTTS(text=output_text, lang=output_lang_key, slow=False)  
except:
    print("\nAudio not supported for this language")
    exit()
  
# Saving the converted audio in a mp3 file named test 
engine.save("test.mp3") 
  
# Playing the converted file 
os.system("test.mp3") 