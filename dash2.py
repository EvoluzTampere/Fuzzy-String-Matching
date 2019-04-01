# 18-19 Jun 2018 Heikki Keskustalo and Boyang Zhang
#
# usage: python filter_letters.py
# input: text file in UTF-8 (wartime letters)
#
# Read input file, process, write output into file
#
# The goal is to process lines ending with a dash in a meaningful way,
# nothing else.
#
# Steps:
#
# -Read input file (lines ending with newline)
# -add each line into list of strings
# Note: by "letter/character at the end of line" we mean character preceding the newline
# -decode into Unicode (UTF-8 into Python Code Points)
# Start processing file lines:
# -strip spaces at the beginning/end of lines
# -if dash at the end of line, remove newline (to create "dashed tokens")
# -replace remaining newlines with spaces (file without newlines)
# -replace sequences of blancos by one blanco (space)
# -Process "dashed tokens" of the form A-B (A and B are strings)
#    --if A ends with small vowel and B begins with it, keep dash ("talvi-ilta")
#    --else if B starts with capital letter and A ends with any letter, keep dash ("Keski-Suomi")
#    --else if A ends with letter and B starts with letter, remove dash ("terveh-dys" -> "tervehdys")
#    --else keep the dash
# -encod into iso-8859-1 or UTF-8
# -Write to file
 
#
# output: analysis (frequencies and their word tokens)
from __future__ import division
import nltk
from nltk import re
from nltk import FreqDist
import chardet
import sys
 
#####################################################################
# Function definitions:
#####################################################################
 
def file2ulist(ifile): # return file as list (line as Unicode string)
    f = open(ifile,'rU')
    ulines_list = [] # we will add decoded lines into this list
    for rawline in f:
        uline = rawline.decode('utf-8') # decode into Unicode
        ulines_list.append(uline) # append line
    f.close()
    return ulines_list # list of lines (in Unicode)
 
#####################################################################
 
def strip_beg_and_end(ilines): # strip spaces from the beginnings and endings of lines
    olines_list = []
    for iline in ilines: # input
        oline = iline.strip() # now the line does not end with space or even a newline
        oline = oline + u"\n" # now we have very clean lines, ending a with newline
        olines_list.append(oline)
    return olines_list # list of lines (beginning and ending spaces stripped)
 
#####################################################################
def combine_dash(ilines): # remove newline if line ends with dash
    olines_list = []
    for iline in ilines:
        if len(iline) >= 2 and iline[-2]==u'-': # possible to remove newline
            olines_list.append(iline[:-1]) # accept line after removing newline
        else:
            olines_list.append(iline)      # accept line as-is
    return olines_list # list of lines (stripped spaces from line beginnings and endings)
 
#####################################################################
 
def newline_to_space(ilines): # for the remaining lines replace ending newline with space
    olines_list = []
    for iline in ilines:
        if len(iline) >= 1 and iline[-1]==u'\n': # string has last element and it is newline
            new_oline = iline[:-1] + u' ' # remove newline and replace it with space
            olines_list.append(new_oline)
        else:
            olines_list.append(iline)      # accept line as-is
    return olines_list # N.B.!  It is impossible for these lines to end with newline
 
#####################################################################
 
def make_oneline(ilines): # catenate strings in input list into one long string
    longline = u""
    for iline in ilines:
        longline = longline + iline # catenate
    return longline
 
#####################################################################
 
def compress_spaces(longline): # replace several spaces by one
    new_longline = " ".join(longline.split()) # simply split and join using space
    return new_longline
 
#####################################################################
 
def space_tokenize(longline): # tokenize by splitting via whitespaces
    tokenlist = longline.split()
    return tokenlist
 
#####################################################################
 
def glue(token): # input always contains dash
    vowels = set([u'a', u'e', u'i', u'o', u'u', u'y', u'\xe4', u'\xf6'])
    d = token.index('-') # index position of the first dash
    if d >=1 and len(token) >= (d + 2):
        if token[d-1] == token[d+1] and token[d-1] in vowels:
            #print token, "<--- analysis: #1 (same vowels case)"
            return token
        elif token[d+1].isupper() and token[d-1].isalpha():
            #print token, "<--- analysis: #2 (Uppercase letter case)"
            return token
        elif token[d-1].isalpha() and token[d+1].isalpha():
            newtoken = token[0:d] + token[d+1:]
            #print token, "<--- analysis: #3 (case to GLUE): proposing: ", newtoken
            return newtoken
        else:
            #print token, "<--- analysis: #4 (all remaining cases)"
            return token
    else:
            return token
 
#####################################################################
 
def modify_if_dash_token(tokens): # modify tokens with dash but not others
    tokenlist = []
    for token in tokens:
        if '-' in token:
            newtoken = glue(token) # special processing with dashed tokens
            tokenlist.append(newtoken)
        else:
            tokenlist.append(token) # other tokens are kept as they are
    return tokenlist
 
#####################################################################
#####################################################################
 
# Begin Main Program:
 
#####################################################################
# 1 of 3: Read input
#ifile = raw_input("./TXT_41.txt")
#ulines = file2ulist(ifile) # return list of lines (in Unicode)
ulines = file2ulist('./TXT_41.txt') # return list of lines (in Unicode)
#####################################################################
 
#####################################################################
# 2 of 3: Process
ulines2 = strip_beg_and_end(ulines) # list of lines: remove spaces (from both the beginning and ending of each line), keep "\n"
ulines3 = combine_dash(ulines2) # list of lines: remove newline, if the line ends with dash (to later create "dashed tokens")
ulines4 = newline_to_space(ulines3) # list of lines: replace all remaining newlines (=at the end of lines) with a space
longline1 = make_oneline(ulines4) # one long line: lines catenated into one
longline2 = compress_spaces(longline1) # one long line: "compress" sequences of spaces into one space
tokens1 = space_tokenize(longline2) # list of tokens: split line into space-separated tokens
tokens2 = modify_if_dash_token(tokens1) # list of tokens but those tokens containing dash are modified, others not
#####################################################################
 
#Stream of finalized tokens (dash-words modified)
#for t in tokens2:
#    print t.encode('utf-8')
 
#####################################################################
# 3 of 3: Write output into file
# we always use UTF-8 unless there is a good reason to use some other char set
ofp = open('testrun.txt', 'w') # open file to write
# catenate token steam into a long string by using spaces as separators; encode Unicode into UTF-8; print to file
longline = " ".join(tokens2)
elongline = longline.encode('utf-8')
ofp.write("%s" % (elongline))
ofp.write(u"\n")
ofp.close() # remember to close the file
#####################################################################
 
#Old code clips
#for utoken in all_utokens:
#    if u'\ufeff' in utoken:
#        print "Skipping Unicode token with illegal char (Unicode: U+FEFF)"
#        detected = chardet.detect(rawline)['encoding'] # detect char set
