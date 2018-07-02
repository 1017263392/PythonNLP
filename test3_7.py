# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 10:06:32 2018

@author: DELL
"""
import nltk,re

word = [w for w in nltk.corpus.words.words() if re.search('^(a|an|the)$',w)]
print(word)
def mycollocation(text):
    if(re.search('^([0-9]+[\*\+])+[0-9]$',text)):
        return text
    return "null"
