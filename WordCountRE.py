import re
test = open("C:\\Users\\tibozh\\Downloads\\41.txt").read()
result = (re.search('date.begin>(.*?)<date.end', test).group(1))
resultAll = re.findall('date.begin>(.*?)<date.end', test)
print(resultAll)

file = open(r"C:\\Users\\tibozh\\Downloads\\41.txt", "r", encoding="utf-8-sig")
from collections import Counter
wordcount = Counter(test.split())


resultString = ', '.join(resultAll) #cover list into a string for display
wordcount2 = Counter(resultString.split())
print(resultString)
