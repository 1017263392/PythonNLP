# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 14:36:30 2018

@author: DELL
"""

import urllib
import nltk
from bs4 import BeautifulSoup

def html_read(url):
    html = urllib.request.urlopen(url).read()
    
    
    
url = 'http://www.nltk.org/'
print(html_read(url))