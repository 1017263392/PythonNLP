#coding=utf-8
import nltk
from nltk.corpus import brown
from nltk.corpus import stopwords

def findfreq50(text):
    stopword = stopwords.words('english')
    fdist1 = nltk.FreqDist(text)
    fdist2 = sorted(fdist1, key=lambda x:fdist1[x],reverse=True)
    fdist = [w for w in fdist2 if w.lower() not in stopword and w.isalpha()]
    return fdist[:50]
    
text = brown.words()
print(findfreq50(text))
