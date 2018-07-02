# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 14:55:03 2018

@author: DELL
"""

class MyCalssText:
    '只是用来测试python面对对象的类'
    varible1 = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        MyCalssText.varible1+=1
    
    def displayCount(self):
        print ("Total Employee %d" % MyCalssText.varible1)
    
class Test:
    def prt(self):
        print(self)
        print(self.__class__)
t = MyCalssText("ly",20134)
t.displayCount()
    