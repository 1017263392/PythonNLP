# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 15:35:26 2018

@author: DELL
"""

def load(file):
    f = open(file)
    return f.read()
file = 'corpus.txt'
print(load(file))



