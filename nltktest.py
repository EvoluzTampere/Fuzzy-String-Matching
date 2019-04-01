from nltk.stem.snowball import SnowballStemmer

letter = [u'kissassa']

for word in letter:
    print word, SnowballStemmer("finnish").stem(word)

# read file (get a string)
# detect charset (UTF-8)
# decode (get a Unicode code point presentation)
# tokenize
# try out the Snowball stemmer

