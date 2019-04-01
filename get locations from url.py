# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 14:53:30 2018

@author: Yang
"""

import requests
from bs4 import BeautifulSoup
r = requests.get('http://ldf.fi/warsa/data?graph=http://ldf.fi/warsa/places/karelian_places')
soup = BeautifulSoup(r.text, 'lxml')
pattern = soup.find_all('prefLabel>', '@')
for item in pattern:
    print(item.string)
