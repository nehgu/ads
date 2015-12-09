"""
    Crawler_Tool:A module that extracts links of HTML pages in a website url
    ~~~~~~~~~~~~
    Added by: Neha Gupta Nov-Dec 2015
"""

import sys
from bs4 import BeautifulSoup
import urllib
import urlparse
import os

def getimg(url):    
    " Store the html page in soup object "
    r = urllib.urlopen(url).read()
    soup = BeautifulSoup(r, "html.parser")

    " Generate all embedded text in a text file all_text.txt    "
    current_dir=os.path.dirname(os.path.realpath(__file__))
    f = open(os.path.join(current_dir,'all_img.txt'), 'w')
    for tag in soup.findAll('img', src=True):
        image_url = urlparse.urljoin(url, tag['src'])
        f.write(image_url+'\n')
    f.close()



