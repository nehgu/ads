"""
    Crawler_Tool
    ~~~~~~~~~~~~

    A module that extracts all div objects from a website url.

"""

import sys
from bs4 import BeautifulSoup
import urllib
import urlparse
from bs4 import UnicodeDammit

""" Store the html page in soup object """
url='http://www.columbia.edu'
r = urllib.urlopen(url).read()
soup = BeautifulSoup(r, "html.parser")
"Remove all script elements"
for script in soup(["script"]):
    script.extract() 

""" Generate all embedded text in a text file all_text.txt    """
texts = soup.findAll(text=True)
f = open('all_text.txt', 'w')
f.write(str(texts))
f.close()



