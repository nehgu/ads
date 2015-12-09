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

def getlinks(filename,url):    
    " Store the html page in soup object "
    r = urllib.urlopen(url).read()
    soup = BeautifulSoup(r, "html.parser")
    "Remove all script elements"
    for script in soup(["script"]):
        script.extract() 

    "Store a local copy of the webpage as html page"
    with open(os.path.join(os.path.dirname(__file__),filename), 'w') as fid:
        fid.write(r)
    fid.close()

    " Generate all embedded urls in a text file all_links.txt    "
    urlArray = []
    f = open((os.path.join(os.path.dirname(__file__),'all_links.txt')), 'w')
    for tag in soup.findAll('a', href=True):
        tag['href'] = urlparse.urljoin(url, tag['href'])
        urlArray = tag['href']
        f.write(urlArray+'\n')
    f.close()
