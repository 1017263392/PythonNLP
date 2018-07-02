# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 11:45:22 2018

@author: DELL
"""

def segment(text, segs):
    words = []
    last = 0
    for i in range(len(segs)):
        if segs[i] == '1':
            words.append(text[last:i+1])
            last = i+1
    words.append(text[last:])
    return words

text = "royousethekittyseethedoggydoyoulikethekittylikethedoggy"
seg1 = "0000000000000010000000000100000000000000001000000000001"
word = segment(text, seg1)
print(word)