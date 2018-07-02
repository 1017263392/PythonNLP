# -*- coding: utf-8 -*-
"""
Created on Sat Jun 30 10:09:17 2018

@author: DELL
"""
import nltk

wsj = nltk.corpus.treebank.tagged_words()
word_tag_fd = nltk.FreqDist(wsj)
words_V = [word +"/" + tag for (word,tag) in word_tag_fd if tag.startswith('N')]
print(words_V)