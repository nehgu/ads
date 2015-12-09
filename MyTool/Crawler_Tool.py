"""
    Crawler_Tool:A module that extracts links of HTML pages in a website url
    ~~~~~~~~~~~~
    Added by: Neha Gupta Nov-Dec 2015
"""
from bs4 import BeautifulSoup, NavigableString
from ConfigParser import ConfigParser
import utils
from utils import get_img,get_text,load_textimg,get_links
import urllib
import urlparse
import copy
import os
import sys
import random

"load the settings from settings.txt file"
current_dir=os.path.dirname(os.path.realpath(__file__))
config=ConfigParser()
config.read(os.path.join(current_dir,'settings.ini'))
url=config.get('General','urltoOpen')
NumOfModifications=int(config.get('General','NumModificationeachPage'))
TotalPages=int(config.get('General','TotalPages'))
filename=config.get('General','Filename')

utils.get_img.getimg(url)
utils.get_text.gettext(url)

""" Choose among following options of modification based on random choice between text/image modification"""
"Choose between text or image"
addremText=random.choice((True,False))
addremImage=random.choice((True,False))
"Choose randomly and store the number of text/image elements to be added/removed"
if (addremText and not(addremImage)):
    AddNewText=random.randint(0,NumOfModifications)
    RemoveText=random.randint(0,(NumOfModifications-AddNewText))
    AddNewImage=0
    RemoveImage=0
elif (addremText and addremImage):
    NumText=random.randint(0,NumOfModifications)
    NumImage=random.randint(0,(NumOfModifications-NumText))
    AddNewText=random.randint(0,NumText)
    RemoveText=random.randint(0,(NumText-AddNewText))
    AddNewImage=random.randint(0,NumImage)
    RemoveImage=random.randint(0,(NumImage-AddNewImage))
elif (not(addremText) and addremImage):
    AddNewText=0
    RemoveText=0
    AddNewImage=random.randint(0,NumOfModifications)
    RemoveImage=random.randint(0,(NumOfModifications-AddNewImage))
elif (not(addremText) and not(addremImage)):
    print "Default case: Just modifying random text elements equal to total num of differences by default"
    AddNewText=0
    RemoveText=0
    AddNewImage=0
    RemoveImage=0

" Store the html page in soup object "
r = urllib.urlopen(url).read()
soup = BeautifulSoup(r, "html.parser")

"Start modifying the html content we got in soup"
texts=utils.load_textimg.load_text()
images=utils.load_textimg.load_img()
utils.get_links.getlinks(filename,url)

##Modify and save html content
##Create a new div
##add_soup=BeautifulSoup('<div id="Soupified"></div>', "html.parser")
##div_tag = add_soup.html.body.div
##add_soup.body.insert(3, div_tag)
#newsoup.body.append(copy.deepcopy(add_soup))
#print i,texts[i]
#newsoup=copy.deepcopy(add_soup)

for n in xrange(TotalPages):
    newsoup=copy.deepcopy(soup)
    "For adding text"
    for x in xrange(AddNewText):
        i=random.randint(0,len(texts))
        add_soup=BeautifulSoup('<p><h2><mark>'+texts[i]+'</mark></h2></p>', "html.parser")
        add_soup.p.string.wrap(newsoup.new_tag("b"))
        add_soup.p.wrap(newsoup.new_tag("div"))
        newsoup.body.append(copy.deepcopy(add_soup))
    "For adding images"
    for x in xrange(AddNewImage):
        i=random.randint(0,len(images)-1)
        images[i]=images[i].rstrip('\n')
        new_tag=newsoup.new_tag('img', src=images[i])
        newsoup.div.append(new_tag)
##    #For modifying text
##    for a in newsoup.findAll('a'):
##        j=random.randint(0,len(texts)-1)
##        if soup.body.findAll(text=texts[j]):
##            a.string='SOUP'
            
    dot_pos = filename.rfind('.')
    new_filename = filename[:dot_pos]+"new-"+str(n)+filename[dot_pos:]
    with open((os.path.join(os.path.dirname(__file__),new_filename)), 'w') as fout:
        fout.write(newsoup.prettify("utf-8"))
