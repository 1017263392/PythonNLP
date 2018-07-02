# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 14:17:36 2018

@author: DELL
"""
import urllib.request
import nltk
from nltk.corpus import nps_chat
url = "http://www.baidu.com"
get = urllib.request.urlopen(url).read()
print(get)

#一些测试
chat = nltk.Text(nps_chat.words())
chat.findall(r'<l.*>{3,}')