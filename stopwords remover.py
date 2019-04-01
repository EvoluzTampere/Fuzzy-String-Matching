# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 14:11:47 2018
#https://www.tutorialspoint.com/python/python_remove_stopwords.htm
@author: tibozh
"""

import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
#print stopwords.fileids()
u = en_stops = set(stopwords.words('finnish'))  # A set of Finnish stopwords, the stopwords can be updated for our own dataset
U = ', '.join(u) #turn set into str (might use file2list, explained below)
#ifile = raw_input("./TXT_41.txt")
#ulines = file2ulist(ifile) # return list of lines (in Unicode)
#ulines = file2ulist('./TXT_41.txt') # return list of lines (in Unicode)
#all_words = open("./TXT_40.txt").read().split()
all_words = open("./testrun.txt").read().split() # We test whether (in Unicode-form) words in testrun.txt file
are included in the stopwords set
for word in all_words:
    uword = word.decode('utf-8')
    if uword not in en_stops:
        print(uword.encode('utf-8')) #f not, word is printed (and in UTF-8 form), .encode() on specific utf-8, ASCII, latin-1.
