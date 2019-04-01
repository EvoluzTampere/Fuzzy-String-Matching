import collections
import operator
# sample text for testing (could come from a text file)
#text_raw = str(esal) #turning the select 414 files into string
text_raw = str(bsal)
text_replace=text_raw.replace('<bsal>','') #remove tag
text=text_replace.replace('</bsal>','')
# create a word list of the words in text 
# remove given punctuation marks and change to lower case    
word_list = [word.strip('.,!?:;"').lower() for word in text.split()]
#print(word_list)  # test
cnt = collections.Counter()
for word in word_list:
    cnt[word] += 1
#print(cnt)  # test
print("The most frequent words are:")
# operator.itemgetter(1) implies v (frequency)
freq = operator.itemgetter(1)
for k, v in sorted(cnt.items(), reverse=False, key=freq): #reverse can be true, False it is easy to see from the very end of the results.
    print("%3d  %s" % (v, k))
