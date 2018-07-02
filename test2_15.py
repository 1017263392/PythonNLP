import nltk
from nltk.corpus import brown
fb = nltk.FreqDist(brown.words())
word = [w for w in set(brown.words()) if fb[w] >= 3]
print(word[:100])
