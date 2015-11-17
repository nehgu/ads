"""
    Crawler_Tool
    ~~~~~~~~~~~~

    A module that extracts all image objects from a website url.

"""

import sys
from bs4 import BeautifulSoup
import urllib
import urlparse

""" Store the html page in soup object """
url='http://www.columbia.edu'
r = urllib.urlopen(url).read()
soup = BeautifulSoup(r, "html.parser")

""" Generate all embedded text in a text file all_text.txt    """
f = open('all_img.txt', 'w')
for tag in soup.findAll('img', src=True):
    image_url = urlparse.urljoin(url, tag['src'])
    f.write(image_url+'\n')
f.close()



