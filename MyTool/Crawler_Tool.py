"""
    Crawler_Tool
    ~~~~~~~~~~~~

    A module that extracts links of HTML pages in a website url.

"""

import sys
from BeautifulSoup import BeautifulSoup
import urllib
import urlparse

""" Store the html page in soup object """
url='http://www.columbia.edu'
r = urllib.urlopen(url).read()
soup = BeautifulSoup(r)

"Remove all script elements"
for script in soup(["script"]):
    script.extract() 
print soup.prettify()

""" Generate all embedded urls in a text file all_links.txt    """
urlArray = []
f = open('all_links.txt', 'w')
for tag in soup.findAll('a', href=True):
    tag['href'] = urlparse.urljoin(url, tag['href'])
    urlArray = tag['href']
    f.write(urlArray+'\n')
f.close()



