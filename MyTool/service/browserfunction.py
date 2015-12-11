"""
    Crawler_Tool:A module that extracts links of HTML pages in a website url
    ~~~~~~~~~~~~
    Added by: Neha Gupta Nov-Dec 2015
"""

import sys
from bs4 import BeautifulSoup, NavigableString
import urllib
import urlparse
import os
import webbrowser

def show_in_browser(output_dir,new_filename):
    url='file://' + str(os.path.join(output_dir,new_filename))
    webbrowser.open(url)
