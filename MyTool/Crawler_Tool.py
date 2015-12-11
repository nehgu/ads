"""
    Crawler_Tool:A module that extracts links of HTML pages in a website url
    ~~~~~~~~~~~~
    Added by: Neha Gupta Nov-Dec 2015
"""
from bs4 import BeautifulSoup, NavigableString
from ConfigParser import ConfigParser
import utils
from utils import get_img,get_text,load_textimg,get_links
import service
from service import TextAdd,ImageAdd,browserfunction
import urllib
import urlparse
import copy
import os
import sys
import random

"load the settings from settings.txt file"
current_dir=os.path.dirname(os.path.realpath(__file__))
output_dir=os.path.join(os.path.dirname(os.path.realpath(__file__)),"output")
config=ConfigParser()
config.read(os.path.join(current_dir,'settings.ini'))
url=config.get('General','urltoOpen')
NumOfModifications=int(config.get('General','NumModificationeachPage'))
TotalPages=int(config.get('General','TotalPages'))
filename=config.get('General','Filename')

utils.get_img.getimg(url)
utils.get_text.gettext(url)

" Store the html page in soup object "
r = urllib.urlopen(url).read()
soup = BeautifulSoup(r, "html.parser")

"Start modifying the html content we got in soup"
texts=utils.load_textimg.load_text()
images=utils.load_textimg.load_img()
utils.get_links.getlinks(filename,url)

for n in xrange(TotalPages):
    "Get random number of text/image addition/removals for each webpage generated"
    AddNewText=random.randint(1,NumOfModifications)
    RemoveText=random.randint(1,NumOfModifications)
    AddNewImage=random.randint(1,NumOfModifications)
    RemoveImage=random.randint(1,NumOfModifications)
    "Create output soup object"
    newsoup=soup
    
    "For adding text"
    for x in xrange(AddNewText):
        i=random.randint(0,len(texts))
        newsoup=service.TextAdd.text_add(newsoup,texts[i])
        
    "For removing text"
    for x in xrange(RemoveText):
        i=random.randint(0,len(texts))
        newsoup=service.TextAdd.text_rem(newsoup,texts[i])
        
    "For adding images"
    for x in xrange(AddNewImage):
        i=random.randint(0,len(images)-1)
        images[i]=images[i].rstrip('\n')
        newsoup=service.ImageAdd.img_add(newsoup,images[i])

    "For removing images"
    for x in xrange(RemoveImage):
        i=random.randint(0,len(images)-1)
        images[i]=images[i].rstrip('\n')
        newsoup=service.ImageAdd.img_rem(newsoup,images[i])
            
    dot_pos = filename.rfind('.')
    new_filename = filename[:dot_pos]+"new-"+str(n)+filename[dot_pos:]
    with open((os.path.join(output_dir,new_filename)), 'w') as fout:
        fout.write(newsoup.prettify("utf-8"))
    service.browserfunction.show_in_browser(output_dir,new_filename)

    print "For generated page: "+str(n)
    print "\tAdded Text: number="+str(AddNewText)
    print "\tremoved Text: number="+str(RemoveText)
    print "\tAdded image: number="+str(AddNewImage)
    print "\tremoved image: number="+str(RemoveImage)
