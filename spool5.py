# This file: "spool5.py"
# Usage: python spool5.py
# Author: Selja Vanamo (Vanamo.Selja.K@student.uta.fi)
# Date: 5.11.2018
# The purpose of this program is to automatically annotate some war-time letter files. 
# Purpose of this code is to read all filenames in Unicode form from a given directory and then select the wanted filenames 
# (letter files of certain type of name). Then the program reads the content of the selected files (contents must be in UTF-8), 
# makes a copy of the file names and writes the content of the original files to the copies. The file names are also decoded from
# UTF-8 to Unicode. Before writing the contents to the copy files, the angle brackets ("<" and ">") are removed from the letter text 
# to avoid confusions with the tagged information added in the annotation part of the program. Also an individual id number (globalid) 
# for each file is created and also a locally individual id number for each file in same subcollection (localid). 
# For each file it's also important to pick up the date information in standardized way in tags from the filename. 
# Because for each letter file we create some tagged beginning infromation, we also need some ending tags as well to "close the file". 

import os, sys # os for operating system dependent interface, sys for system spesific parameters
import os.path # for checking existing paths
import re # for regular expressions

# The actual path of the directory. Please notice to modify to match your directory path. 
letterpath = "/home/stud/sis/a626811" # text in input files must be in UTF-8

# Returns all the filenames from the given directory as a list. 
def read_all_filenames(letterpath):
    all_files = [] # empty list
    dirs = os.listdir(letterpath) # enter the path of the file, return the dictionary name of path name

    for file in dirs: # make a for loop to extract file names one by one
        ufile = file.decode('utf-8') # decode to Unicode
        all_files.append(ufile) # add a single element to the end of the list

    return all_files

# Returns a selected subset of filenames as a list. 
def select_filenames(all_files):
    selected_files = [] # empty list  
    
    for filename in all_files: # make a for loop to extract file names one by one
        number = filename.split("_")[0] # split the first number(s) before an underscore "_" to get the collection number
        if number.isdigit(): # check that the beginning of the filename contains only numbers
            for number in range(350): # make a for loop to check that the collection number is under 350
                start = str(number) + "_" # convert the integer to string with the collection number and an underscore
                middle = filename.split("_")[1] # split the rest of the filename after an underscore
                # Check that filename starts with certain kind of string, file type is ".txt" 
                # and that the last part of the filename contains at least six numbers after an underscore.
                if filename.startswith(start) and filename.endswith(".txt") and str(middle[:6].isdigit()):
                    selected_files.append(filename) # add a single element to the end of the list
        
    return sorted(selected_files) # return alphabetically sorted list

# Opens and reads the file contents and returns it as Python's Unicode string. 
def get_file_contents(filename):
    orig_file = open(filename, "r") # open the original file for reading
    filetext = orig_file.read() # read the contents of the file
    ufiletext = filetext.decode('utf-8') # decode to Unicode

    orig_file.close() # close the file

    return ufiletext

# Creates and returns a copy of filename adding string "copy_" at the beginning of the original filename. 
def modify_filename(filename):
    new_name = "copy_" + filename # create a new filename of the original name
    modified_filename = new_name.decode('utf-8') # decode to Unicode

    return modified_filename

# First checks that the given filename doesn't exist (if so, gives an error message and exits from the program) and then 
# adds the copy of the file contents to the newly named file. 
# We assume US style INPUT filenames using conventional chars in the ASCII RANGE only. 
def write_to_file(modified_filename, annotated_text):
    if os.path.exists(modified_filename): # check if the filename already exists to avoid overwriting
        print "File already exists. Please use another name."
        sys.exit("Exiting.")
    else: 
        new_filetext = annotated_text.encode('utf-8') # encode to UTF-8
        new_file = open(modified_filename, "w") # open the new file for writing
        new_file.write(new_filetext) # write to file

        new_file.close() # close the file

# Replaces the possible "<" and ">" marks (angle brackets) from the text to avoid later complications with the added tags.
# The "l<" marks are replaced with the capital letter "K", the "<" marks are replaced with the small letter "k" 
# and the ">" marks are replaced with "" (removed).  
def remove_brackets(utext):
    cleaned1 = utext.replace("l<", "K") # replace "l<" with "K"
    cleaned2 = cleaned1.replace("<", "k") # replace "<" with "k"
    cleaned3 = cleaned2.replace(">", "") # replace ">" with "" (remove the mark)

    return cleaned3

# get the date of the letter from filename
def get_date(filename):
    find_date = filename.split("_")[1] # get the date's numbers from filename after an underscore
    date = "19" + str(find_date[:6]) # create a date in form of yyyymmdd, for example 19390101

    return date

# Adds annotated structure and information at the beginning of the letter text. 
# The order of added information and the structure at the beginning of the file is this: 
# <letter> --- is the starting point of each individual letter
# <globalid>n</globalid> --- is individual number for each letter in directory
# <collection>n</collection> --- is the first one to three numbers before underscore referring to subcollection number
# <localid>n</localid> --- is individual number for each letter in one subcollection
# <date>19xxxxxx</date> --- the date of the letter
# <comment>NULL</comment>
# <text> --- is the starting point of letter's contents
# cleaned_text here as a whole
def add_beginning_tags(globalid, localid, collection_number, date, cleaned_text):
    # the tags and their information at the beginning of the file's content
    annotated_text = "<letter>" + "\n" + "<globalid>" + str(globalid) + "</globalid>" + "\n" + \
    "<collection>" + str(collection_number) + "</collection>" + "\n" + "<localid>" + str(localid) + "</localid>" + "\n" + \
    "<date>" + date + "</date>" + "\n" + "<comment>NULL</comment>" + "\n" + "<text>" + "\n" + cleaned_text
    
    return annotated_text

# Adds annotated structure at the end of the letter text. 
# The order of added information and structure after the beginning tags and the whole letter text is this: 
# annotated_text here as a whole
# </text>
# </letter>
def add_ending_tags(annotated_text):
    # the tags at the end of the file's content
    # after the letter's annotated contents change the line so if something comes after this, it starts at a new line
    finished_text = annotated_text + "</text>" + "\n" + "</letter>" + "\n"

    return finished_text

#

# Begin main

#
globalid = 0 # iterator for creating individual id numbers for each selected file in directory
localid = 0 # iterator for creating individual id numbers for each selected file in one subcollection
current_subcollection = "" # current subcollection number that can change

all_files = read_all_filenames(letterpath) # Unicode
selected_files = select_filenames(all_files) # Unicode
for filename in selected_files: # Unicode
    collection_number = filename.split("_")[0] # pick up the collection number at the beginning of the filename (numbers before "_")
    globalid += 1 # add numbers in every round of interation
    if collection_number != current_subcollection: # if subcollection has changed, reset localid and set new current subcollection
        localid = 1 # first file in new subcollection
        current_subcollection = collection_number
    else: # if subcollection is still same as last round, increase localid
        localid += 1 # add numbers in every round of interation
    utext = get_file_contents(filename) # Unicode
    cleaned_text = remove_brackets(utext) # Unicode
    copy_name = modify_filename(filename) # Unicode
    date = get_date(filename) # get date information from filename
    annotated_text = add_beginning_tags(globalid, localid, collection_number, date, cleaned_text) # Unicode
    finished_text = add_ending_tags(annotated_text) # Unicode
    write_to_file(copy_name, finished_text) # filenames written in UTF-8