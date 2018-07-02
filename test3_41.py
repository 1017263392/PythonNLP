# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 10:47:56 2018

@author: DELL
"""

words = ['attribution','confabulation','elocution','seguoia','tenacious','unidirectional']
vsequences = set()
temp = []
vsequences = [''.join(temp) for w in words
              for char in w
              if char not in 'aeiou']
