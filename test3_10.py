# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 09:18:55 2018

@author: DELL
"""

sent = ['The','dog','gave','John','the','newspaper']
result = []
for word in sent:
    result.append((word,len(word)))
result.append(0)
print (result)
type(result)

