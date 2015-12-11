"""
    TextAdd:A module that performs random addition/deletion of text in HTML pages in a website url
    ~~~~~~~~~~~~
    Added by: Neha Gupta Nov-Dec 2015
"""

import sys
from bs4 import BeautifulSoup, NavigableString
import urllib
import urlparse
import os
import random
import lxml.etree
import lxml.etree as ET
from StringIO import StringIO
from htmldom import htmldom
import re

def text_add(newsoup,text):
    text=text.strip('\n')
    divcount=len(newsoup.find_all("div"))
    c=random.randint(1,divcount)
    cc=0
    temp_soup=BeautifulSoup('<div id="dummy123"><mark><strong>'+text+'</strong></mark></div>', "html.parser")
    div_tag=temp_soup.div
    for tag in newsoup.find_all(re.compile("^[a-z]+.*")):     
        if (tag.name == "div"):
            cc=cc+1
            if (cc==c):    
                #insert new div here and put into soup                
                tag.append(div_tag)
    return newsoup

def text_rem(newsoup,text2):
    text2=text2.strip('\n')
    giantstring=str(newsoup)
    if (text2 in giantstring):
        giantstring=giantstring.replace(text2,"Removed Text from Here")
        latestsoup=BeautifulSoup(giantstring, "html.parser")
    else:
        latestsoup=newsoup
    return latestsoup
