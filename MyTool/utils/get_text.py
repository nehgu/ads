"""
    get_text:A module that extracts text from a HTML page and stores in a text file
    ~~~~~~~~~~~~
    Added by: Neha Gupta Nov-Dec 2015
"""

import sys
import os
from bs4 import BeautifulSoup
import urllib
import urlparse
from bs4 import UnicodeDammit

def gettext(url):   
    " Store the html page in soup object "
    r = urllib.urlopen(url).read()
    soup = BeautifulSoup(r, "html.parser")
    "Remove all script elements"
    for script in soup(["script"]):
        script.extract() 

    """ Generate all embedded text in a text file all_text.txt    """
    current_dir=os.path.dirname(os.path.realpath(__file__))
    f = open(os.path.join(current_dir,'all_text.txt'), 'w')
    for line in soup.stripped_strings:
        f.write(line.strip().encode('latin1','ignore')+'\n')
    f.close()
