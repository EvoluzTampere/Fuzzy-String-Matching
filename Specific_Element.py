# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 10:00:09 2019

@author: tibozh
#select the specific elements needed in the collection, below selects 4 fields: globalid, date, bsal, esal.



import re
from bs4 import BeautifulSoup
test = open("C:\\Users\\tibozh\\Downloads\\Fuzzy\\Selja\\all\\output.txt").read()
#test = open("C:\\Users\\tibozh\\Downloads\\Fuzzy\\Selja\\poimitut_batch2\\poimitut_toinen_batch\\output.txt").read()
soup = BeautifulSoup(test, 'lxml')
print(soup.prettify())#standard format

date = soup.find_all('date')#check element b
len(date) #check the number of elements date
bsal=soup.find_all('bsal')#check element i
esal= soup.find_all('esal')
gid = soup.find_all('globalid')
comment_test = soup.find_all('comment')
p = soup.find_all('date')
letter = soup.find_all('letter')

# Begin



raw_text = test

soup = BeautifulSoup(raw_text)


for item in soup.find_all('letter'): # loop letter by letter

    gid = item.find('globalid')              # get field

    date = item.find('date')              # get field

    bsal = item.find('text').find('bsal') # get field

    esal = item.find('text').find('esal') # get field

    print("<" + item.name + ">")

    if gid is not None:

        print (gid)

    if date is not None:

        print (date)

    if bsal is not None:

        print (bsal)

    if esal is not None:

        print (esal)

    print("</" + item.name + ">")


# end of program.
