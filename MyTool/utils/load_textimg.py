"""
    load_textimg:A module that loads all the extracted text/image from html page into variables and returns them
    ~~~~~~~~~~~~
    Added by: Neha Gupta Nov-Dec 2015
"""

import sys
from bs4 import BeautifulSoup
import urllib
import urlparse
import os

current_dir=os.path.dirname(os.path.realpath(__file__))
def load_text():    
    "Loading all text to be added first"
    with open((os.path.join(current_dir,'all_text.txt')),'r') as f:
        texts=f.readlines()
    f.close()
    with open((os.path.join(current_dir,'NewText.txt')),'r') as f:
        for text in f:
            texts.append(text)
    f.close()
    return texts

def load_img():      
    "Loading all images to be added"
    with open((os.path.join(current_dir,'all_img.txt')),'r') as f:
        images=f.readlines()
    f.close()
    with open((os.path.join(os.path.dirname(__file__),'NewImage.txt')),'r') as f:
        for image in f:
            images.append(image)
    f.close()
    return images



