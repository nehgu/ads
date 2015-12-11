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
import random
import lxml.etree
import lxml.etree as ET
from StringIO import StringIO
from htmldom import htmldom
import re

def img_add(newsoup,image):    
    divcount1=len(newsoup.find_all("div"))
    if (divcount1>1):      
        c1=random.randint(1,divcount1)
        cc1=0
        temp_soup=BeautifulSoup('<div id="dummy123"><img src='+image+'></div>', "html.parser")
        div_tag=temp_soup.div
        for tag in newsoup.find_all(re.compile("^[a-z]+.*")):     
            if (tag.name == "div"):
                cc1=cc1+1
                if (cc1==c1):    
                    #insert new div here and put into soup                
                    tag.append(div_tag)
    else:
        temp_soup=BeautifulSoup('<div id="dummy123"><img src='+image+'></div>', "html.parser")
        div_tag=temp_soup.div
        for tag in newsoup.find_all(re.compile("^[a-z]+.*")):     
            if (tag.name == "div"):
                tag.append(div_tag)
    return newsoup

def img_rem(newsoup,image):
    divcount3=len(newsoup.find_all("img"))
    if (divcount3>1):
        c3=random.randint(1,divcount3)
        cc3=0
        for tag in newsoup.find_all("img"):     
            if (tag.name == "img"):            
                cc3=cc3+1
                if (cc3==c3):    
                    #remove image at the random tag and return soup
                    new_tag = newsoup.new_tag("b")
                    new_tag.string = "Removed Image"
                    tag.replace_with(new_tag)
    else:
        #if there are no images, add random image
        for tag in newsoup.find_all("img"):     
            if (tag.name == "img"):
                new_tag = newsoup.new_tag("b")
                new_tag.string = "Removed Image"
                tag.replace_with(new_tag)
    return newsoup
