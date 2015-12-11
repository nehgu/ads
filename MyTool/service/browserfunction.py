"""
    Browserfunction:A module that renders HTML pages to browser
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
    webbrowser.open_new_tab(url)
