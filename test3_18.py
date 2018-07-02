# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 09:39:01 2018

@author: DELL
"""

import nltk
from nltk.corpus import brown
import re

word = brown.words()
words = []
count = 0
while (count<1000):
    words.append(word[count])
    count = count + 1
wh_word  = [w for w in words if re.search(r'^wh',w.lower())]
print (set(wh_word))