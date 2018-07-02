# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 10:10:36 2018

@author: DELL
"""

import re

word = "who is don't you know"
print(re.findall(r"n't|\w+",word))
print(re.findall(r"^(\w*?)(n't)","don't"))