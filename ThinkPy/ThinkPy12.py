# Think Python chapter 12 examples and exercises
# 07/27/2017

import math

# Section 12.1
# *************************************************************************************
# Tuples are basically lists, but immutable
# Create empty tuple with tuple()
# Since tuples are immutable, you can only change one by creating a new one:
# >>> t = (1, 2, 3, 4, 5)
# >>> t[0]
# 1
# >>> t[0] = 0
# ERROR
# >>> t = (1,) + t[1:]
# >>> t
# (0, 2, 3, 4, 5)

# Section 12.2
# *************************************************************************************
# Use tuple assignment to assign values to variables or swap values
# >>> addr = 'monty@python.org'
# >>> uname, domain = addr.split('@')
# >>> uname
# 'monty'
# >>> domain
# 'python.org'

# Section 12.4
# *************************************************************************************
# 
# Exercise 1  
# Many of the built-in functions use variable-length argument tuples. For example,
# max and min can take any number of arguments:
# >>> max(1,2,3)
# 3
# But sum does not.
# >>> sum(1,2,3)
# TypeError: sum expected at most 2 arguments, got 3
# Write a function called sumall that takes any number of arguments and returns their sum.

def sumall(*args):
    """
    Returns the sum of an arbitrary number of integer arguments.
    Discards non-integer arguments.
    """
    s = 0
    for i in args:
        if isinstance(i, int):
            s += i
    return s

# Section 12.6 - Dicts and tuples
# *************************************************************************************
# dict method items returns tuples
# Py 2
# >>> d = {'a':1, 'b':2, 'c':3}
# >>> t = d.items()
# >>> t
# [('a', 1), ('b', 2), ('c', 3)]

# traverse dict
# >>> for key, value in d.items():
# ...     print(val, key)

# Section 12.7
# *************************************************************************************
# 
# DSU:
# Abbreviation of “decorate-sort-undecorate,” a pattern that involves building a list
# of tuples, sorting, and extracting part of the result.

# Exercise 2
def sort_by_length(words):
    t = []
    for word in words:
       t.append((len(word), word))
    t.sort(reverse=True)
    res = []
    for length, word in t:
        res.append(word)
    return res
# In this example, ties are broken by comparing words, so words with the same length
# appear in reverse alphabetical order. For other applications you might want to break
# ties at random. Modify this example so that words with the same length appear in
# random order. Hint: see the random function in the random module.
# Solution: http://thinkpython.com/code/unstable_sort.py.
def sblr(words):
    """
    Sort a list of words by descending length. In case of ties, spice each
    word with a random integer to act as a tiebreaker.
    """
    t = []
    for word in words:
           t.append((len(word), random.randint(1, 1000), word))
    t.sort(reverse=True)
    res = []
    for length, spice, word in t:
        res.append(word)
    return res

# Section 12.11
# *************************************************************************************
# 
# Exercise 3  
# Write a function called most_frequent that takes a string and prints the letters in
# decreasing order of frequency. Find text samples from several different languages and
# see how letter frequency varies between languages. Compare your results with the tables
# at http://en.wikipedia.org/wiki/Letter_frequencies.
# Solution: http://thinkpython.com/code/most_frequent.py.

def most_frequent(s):
    """
    Count the ocurrence of letters in the given string (s) and return a list of tuples
    in descending order of frequency.
    """
    freq = dict()
    for c in s:
        c = c.lower()
        if c >= 'a' and c <= 'z':
            freq[c] = freq.setdefault(c, 0) + 1
    res = []
    for ltr, cnt in freq.items():
        res.append((cnt, ltr))
    res.sort(reverse=True)
    return res

most_frequent(s)

# Exercise 4  
# More anagrams!
# Write a program that reads a word list from a file (see Section 9.1) and prints all
# the sets of words that are anagrams.
# Here is an example of what the output might look like:
# ['deltas', 'desalt', 'lasted', 'salted', 'slated', 'staled']
# ['retainers', 'ternaries']
# ['generating', 'greatening']
# ['resmelts', 'smelters', 'termless']
# Hint: you might want to build a dictionary that maps from a set of letters to a list of
# words that can be spelled with those letters. The question is, how can you represent
# the set of letters in a way that can be used as a key?
# Modify the previous program so that it prints the largest set of anagrams first,
# followed by the second largest set, and so on.
# In Scrabble a “bingo” is when you play all seven tiles in your rack, along with a letter
# on the board, to form an eight-letter word. What set of 8 letters forms the most possible
# bingos? Hint: there are seven.
# Solution: http://thinkpython.com/code/anagram_sets.py.

# Exercise 5  
# Two words form a “metathesis pair” if you can transform one into the other by swapping
# two letters; for example, “converse” and “conserve.” Write a program that finds all of
# the metathesis pairs in the dictionary. Hint: don’t test all pairs of words, and don’t
# test all possible swaps. Solution: http://thinkpython.com/code/metathesis.py.
# Credit: This exercise is inspired by an example at http://puzzlers.org.

# Exercise 6  
# Here’s another Car Talk Puzzler (http://www.cartalk.com/content/puzzlers):
# What is the longest English word, that remains a valid English word, as you remove its
# letters one at a time?
# Now, letters can be removed from either end, or the middle, but you can’t rearrange any
# of the letters. Every time you drop a letter, you wind up with another English word. If
# you do that, you’re eventually going to wind up with one letter and that too is going
# to be an English word—one that’s found in the dictionary. I want to know what’s the
# longest word and how many letters does it have?
# I’m going to give you a little modest example: Sprite. Ok? You start off with sprite,
# you take a letter off, one from the interior of the word, take the r away, and we’re
# left with the word spite, then we take the e off the end, we’re left with spit, we
# take the s off, we’re left with pit, it, and I.
# 
# Write a program to find all words that can be reduced in this way, and then find the
# longest one.
# 
# This exercise is a little more challenging than most, so here are some suggestions:
# 
# You might want to write a function that takes a word and computes a list of all the
# words that can be formed by removing one letter. These are the “children” of the word.
# Recursively, a word is reducible if any of its children are reducible. As a base case,
# you can consider the empty string reducible.
# The wordlist I provided, words.txt, doesn’t contain single letter words. So you might
# want to add “I”, “a”, and the empty string.
# To improve the performance of your program, you might want to memoize the words that
# are known to be reducible.
# Solution: http://thinkpython.com/code/reducible.py.