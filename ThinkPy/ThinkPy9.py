# Think Python chapter 9 examples and exercises
# 07/13/2017

import math

# Section 9.1
# *************************************************************************************
# Reading Word Lists - download this list: http://thinkpython.com/code/words.txt
# 
# Open a file for reading and read the first line (to a line break)
# >>> fin = open('words.txt')
# >>> fin.readline()
# aa\n
# 
# Strip the line break from the output
# >>> line = fin.readline()
# >>> word - line.strip()
# >>> print (word)
# aah
# 
# A loop to print the words
# >>> for line in fin:
# >>> ....word = line.strip()
# >>> ....print word

# Exercise 1  
# Write a program that reads words.txt and prints only the words with more than 20
# characters (not counting whitespace).
def long_words(file, n):
    """ Print all words from given text file that are over n in length.
    file = file name
    n = length
    """
    fin = open(file)
    for line in fin:
        word = line.strip()
        if len(word) >= n:
            print (word)
    fin.close()

# Section 9.2
# *************************************************************************************
# Exercises

# Exercise 2  
# In 1939 Ernest Vincent Wright published a 50,000 word novel called Gadsby that does
# not contain the letter “e.” Since “e” is the most common letter in English, that’s not
# easy to do.
# In fact, it is difficult to construct a solitary thought without using that most
# common symbol. It is slow going at first, but with caution and hours of training you
# can gradually gain facility.
# 
# All right, I’ll stop now.
# 
# Write a function called has_no_e that returns True if the given word doesn’t have
# the letter “e” in it.
# 
# Modify your program from the previous section to print only the words that have no “e”
# and compute the percentage of the words in the list have no “e.”
def has_no_e(word, x):
    """
    Check for the presence of the given letter in given word. Return True if none, else
    return False.
    word = word to check
    x = letter to check for
    """
    for char in word[:]:
        if char == x:
            return False
    return True

def long_words_no_e(file, x):
    """
    Print all words from given text file that don't have the given character.
    Return the percentage of words without an e.
    file = file name
    x = character
    """
    fin = open(file)
    tot = 0
    no_e = 0
    for line in fin:
        tot += 1
        word = line.strip()
        if has_no_e(word, x):
            print (word)
            no_e += 1
    fin.close()
    print ('Percent of words without "e": %s' % ((no_e/tot)*100))

# Exercise 3  
# Write a function named avoids that takes a word and a string of forbidden letters,
# and that returns True if the word doesn’t use any of the forbidden letters.
# Modify your program to prompt the user to enter a string of forbidden letters and
# then print the number of words that don’t contain any of them. Can you find a combination
# of 5 forbidden letters that excludes the smallest number of words?
def avoids(word, forbidden):
    """
    Checks a word for a string of forbidden characters.
    Return False if any are present, else return True
    word = word to check
    forbidden = characters to avoid
    """
    for char in forbidden:
        if char in word:
            return False
    return True

def forbid_chars(file, bad_chars=''):
    """
    Checks all words in a given text file for forbidden characters and returns
    a count of words that don't contain those letters.
    file = name of words files
    bad_chars = 5 characters to check
    """
    if len(bad_chars) != 5:
        bad_chars = input('Please enter 5 letters without spaces: ')
    fin = open(file)
    no_letter = 0
    for line in fin:
        word = line.strip() # We want to get rid of newline characters
        if avoids(word, bad_chars):
            no_letter += 1
    fin.close()
    return no_letter

# Exercise 4  
# Write a function named uses_only that takes a word and a string of letters,
# and that returns True if the word contains only letters in the list. Can you
# make a sentence using only the letters acefhlo? Other than “Hoe alfalfa?”
def uses_only(word, letters):
    for char in word:
        if char not in letters:
            return False
    return True

# hallo, loco loofah!
for line in fin:
    word = line.strip()
    if uses_only(word, 'acefhlo'):
        print(word)

# Exercise 5  
# Write a function named uses_all that takes a word and a string of required
# letters, and that returns True if the word uses all the required letters at
# least once. How many words are there that use all the vowels aeiou? How about
# aeiouy?
def uses_all(word, letters):
    for char in letters:
        if not char in word:
            return False
    return True

# There appears to be 0 words that use all vowels
count = 0
for line in fin:
    word = line.strip()
    if uses_all(word, 'aeiouy'):
        count += 1

# Exercise 6  
# Write a function called is_abecedarian that returns True if the letters in a
# word appear in alphabetical order (double letters are ok). How many abecedarian
# words are there?
def is_abecadarian(word):
    old = ord(word[0])
    for char in word[1:]:
        if not ord(char) >= old:
            return False
        old = ord(char)
    return True

# There appear to be 0 words that are abecadarian
count = 0
for line in fin:
    word = line.strip()
    if is_abecadarian(word):
        count += 1

# Section 9.3
# *************************************************************************************
# 