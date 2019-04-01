# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 10:00:09 2019

@author: tibozh
#the code offers the selection of the 10% of the training dataset, after tagging of the entire dataset as 100%, 
#if would like to select certain every nth of the dataset, for example, every 10th of the dataset, below method is a solution.
"""

import re
from bs4 import BeautifulSoup
test = open("C:\\Users\\tibozh\\Downloads\\Fuzzy\\Selja\\all\\output.txt").read()
#test = open("C:\\Users\\tibozh\\Downloads\\Fuzzy\\Selja\\poimitut_batch2\\poimitut_toinen_batch\\output.txt").read()
soup = BeautifulSoup(test, 'lxml')
print(soup.prettify())#standard format

letter = soup.find_all('letter')


f = open("letter.txt","w")
f.write(str(letter[0::10])) #select 10% with all field, [0::10] is every nth selection of string.
f.close()

Letter = list(letter)
len(list(letter))

Ten_letter=list(letter[0::10])

nity_letter = Letter #remove the 10% in the selection, it is the 90% left.
new_list = []
for e in Letter:
    if e not in Ten_letter:
        new_list.append(e)
nity_letter = new_list

f = open("letter90.txt","w")
f.write(str(nity_letter))
f.close()






