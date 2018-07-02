# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 11:50:51 2018

@author: DELL
"""

import nltk
import example3_2

def evaluate(text, segs):
    words = segment(text, segs)
    text_size = len(words)
    lexicon_size = len(' '.join(list(set(words))))
    return text_size + lexicon_size
text = "royousethekittyseethedoggydoyoulikethekittylikethedoggy"
seg1 = "000000000000001000000000010000000000000000100000000000"
print(evaluate(text,seg1))
