# Think Python chapter 13 examples and exercises
# 08/01/2017

import math

# Section 13.1
# *************************************************************************************
# Exercise 1  
# Write a program that reads a file, breaks each line into words, strips whitespace and
# punctuation from the words, and converts them to lowercase.
# Hint: The string module provides strings named whitespace, which contains space, tab,
# newline, etc., and punctuation which contains the punctuation characters. Let’s see
# if we can make Python swear:
# 
# >>> import string
# >>> print string.punctuation
# !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
# Also, you might consider using the string methods strip, replace and translate.
def split_line(line):
    res = []
    words = line.split(' ')
    return words

def clean_line(line):
    res = str()
    for char in line:
        if char == '-':
            res += char
        elif char not in string.punctuation:
            res += char
        elif char == '\n':
            print('GO CRAZY')
            continue
    return res

def read_words(file):
    word_list = list()
    fin = open(file)
    for line in fin:
        tmp = split_line(clean_line(line))
        for word in tmp:
            if word not in word_list:
                word_list.append(word)
    fin.close()
    return word_list


# Exercise 2  
# Go to Project Gutenberg (http://gutenberg.org) and download your favorite
# out-of-copyright book in plain text format.
# Modify your program from the previous exercise to read the book you downloaded, skip
# over the header information at the beginning of the file, and process the rest of the
# words as before.
# 
# Then modify the program to count the total number of words in the book, and the number
# of times each word is used.
# 
# Print the number of different words used in the book. Compare different books by
# different authors, written in different eras. Which author uses the most extensive
# vocabulary?
# 
# Exercise 3  
# Modify the program from the previous exercise to print the 20 most frequently-used words
# in the book.
# Exercise 4  
# Modify the previous program to read a word list (see Section 9.1) and then print all the
# words in the book that are not in the word list. How many of them are typos? How many of
# them are common words that should be in the word list, and how many of them are really
# obscure?