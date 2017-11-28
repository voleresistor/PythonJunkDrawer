# Think Python chapter 10 examples and exercises
# 07/16/2017

import math

# Section 10.2
# *************************************************************************************
# !! LISTS ARE MUTABLE !!
>>> numbers = [17, 123]
>>> print(numbers)
[17, 123]
>>> numbers[1] = 5
>>> print(numbers)
[17, 5]

# Section 10.4
# *************************************************************************************
# List operations
# + concatenates
# * repeats

>>> a = [1, 2, 3]
>>> b = [4, 5, 6]
>>> c = a + b
>>> print(c)
[1, 2, 3, 4, 5, 6]
>>> [0] * 4
[0, 0, 0, 0]
>>> [1, 2, 3] * 3
[1, 2, 3, 1, 2, 3, 1, 2, 3]

# Section 10.5
# *************************************************************************************
# A slice on the left side of an assignment updates multiple elements

>>> t = ['a', 'b', 'c', 'd', 'e', 'f']
>>> t
['a', 'b', 'c', 'd', 'e', 'f']
>>> t[1:3]
['b', 'c']
>>> t[1:3] = ['x', 'y']
>>> t
['a', 'x', 'y', 'd', 'e', 'f']

# Section 10.5
# *************************************************************************************
# Exercise 1  
# Write a function called nested_sum that takes a nested list of integers and add up
# the elements from all of the nested lists.
# !!! In this example, total is called an accumulator because it accumulates a sum !!!
def nested_sum(nlist):
    """
    Return the sum of nested lists. Can handle multiple levels of nesting and integers
    alongside nested lists.
    """
    total = 0
    for list_item in nlist:
        if isinstance(list_item, list):
            total += nested_sum(list_item)
        elif isinstance(list_item, int):
            total += list_item
        else:
            print(list_item, ' is not an integer or list.')
    return total

# Section 10.7
# *************************************************************************************
# Exercise 2  
# Use capitalize_all to write a function named capitalize_nested that takes a nested
# list of strings and returns a new nested list with all strings capitalized.
# !!! In this example capitalize_all is called a map because it maps a function to
# each element in a sequence !!!
def capitalize_all(t):
    res = []
    for s in t:
        res.append(s.capitalize())
    return res

def capitalize_nested(x):
    res = []
    for y in x:
        res.append(capitalize_all(y))
    return res

# Exercise 3  
# Write a function that takes a list of numbers and returns the cumulative sum;
# that is, a new list where the ith element is the sum of the first i+1 elements
# from the original list. For example, the cumulative sum of [1, 2, 3] is [1, 3, 6].
def cumulative_sum(t):
    """
    Return a new list where the ith element is the sum of all elements up to that
    position in the list. Ex: [1, 2, 3] returns [1, 3, 6]
    """
    res = [t[0]]
    for i in range(1, len(t)):
        res.append(res[-1] + t[i])
    return res

# Section 10.8
# *************************************************************************************
# Exercise 4  
# Write a function called middle that takes a list and returns a new list that
# contains all but the first and last elements. So middle([1,2,3,4]) should return [2,3].
def middle(t):
    """
    Return a new list that doesn't include the first or last elements from the original.
    """
    res = t
    del(res[0])
    del(res[-1])
    return res

# Exercise 5  
# Write a function called chop that takes a list, modifies it by removing the first
# and last elements, and returns None.
def chop(t):
    """
    Directly edit the given list to remove the first and last elements.
    """
    del(t[0])
    del(t[-1])
    return None

# Section 10.9
# *************************************************************************************
# Lists and strings
# Convert to list from string
>>> s = 'spam'
>>> t = list(s)
>>> print(t)
['s', 'p', 'a', 'm']

# Break string into list of words with default delimiter
>>> s = 'pining for the fjords'
>>> t = s.split()
>>> print(t)
['pining', 'for', 'the', 'fjords']

# Break string into list of words using hyphen delimiter
>>> s = 'spam-spam-spam'
>>> delim = '-'
>>> t = s.split(delim)
>>> print(t)
['spam', 'spam', 'spam']

# Join words into string from list
# !!! This one acts on the DELIMITER character
>>> t = ['pining', 'for', 'the', 'fjords']
>>> delim = ' '
>>> delim.join(t)
'pining for the fjords'

# Section 10.10
# *************************************************************************************
# In Python, two strings with identical values reference the same single object in memory.
# These are said to be equivalent and identical.
# Lists are always unique objects in memory, so even equivalent lists are NOT identical.

# Section 10.15
# *************************************************************************************
# Exercises

# Exercise 6
# Write a function called is_sorted that takes a list as a parameter and returns True
# if the list is sorted in ascending order and False otherwise. You can assume (as a
# precondition) that the elements of the list can be compared with the relational operators
# <, >, etc.
# For example, is_sorted([1,2,2]) should return True and is_sorted(['b','a']) should return
# False.
def is_sorted(t):
    if len(t) < 2:
        return True
    for i in range(len(t) - 1):
        if not t[i] <= t[i+1]:
            return False
    return True

# Exercise 7  
# Two words are anagrams if you can rearrange the letters from one to spell the other.
# Write a function called is_anagram that takes two strings and returns True if they
# are anagrams.
def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    t1 = list(s1)
    t2 = list(s2)
    #print(t1, t2)
    for char in t2:
        if char in t1:
            t1.remove(char)
            #print('Removed: %s\nRemaning: %s' % (char, t1))
        else:
            return False
    return True

# Exercise 8  
# The (so-called) Birthday Paradox:
# Write a function called has_duplicates that takes a list and returns True if there
# is any element that appears more than once. It should not modify the original list.
# If there are 23 students in your class, what are the chances that two of you have
# the same birthday? You can estimate this probability by generating random samples
# of 23 birthdays and checking for matches. Hint: you can generate random birthdays
# with the randint function in the random module.
# You can read about this problem at http://en.wikipedia.org/wiki/Birthday_paradox,
# and you can download my solution from http://thinkpython.com/code/birthday.py.
import random
# This entire function would have been unnecessary had I thought to use ints from
# 1-365 to represent birthdays instead of getting stuck thinking about mm/dd/yy
# structures
def random_birthday():
    """
    Generate random birthdays using random.randint. Birthdays are returned as
    string objects in the format '(m)m-(d)d'.
    """
    days_31 = [1, 3, 5, 7, 8, 10, 12]
    days_30 = [4, 6, 9, 11]
    m = random.randint(1, 12)
    if m in days_31:
        d = random.randint(1, 31)
    elif m in days_30:
        d = random.randint(1, 30)
    else:
        d = random.randint(1, 29)
    return ('%s-%s' % (m, d))

def get_bdays(n=23):
    """
    Generate a list of random birthdays, stored as strings in the '(m)m-(d)d' format.
    n is the number of birthdays to generate. n defaults to 23.
    """
    res = []
    for i in range(n):
        res.append(random_birthday())
    return res

def has_duplicates(t):
    # Old Code
    # tmp = []
    # for i in t:
    #     tmp.append(i)
    # Worked solution this way because I didn't think to just use days 1-365 and instead
    # chose to work with strings like 'mm-dd'. I think the nested conditional is
    # particularly gross, especially given the knowledge that strings can be sorted
    # for i in t:
    #     if i in tmp:
    #         tmp.remove(i)
    #         if i in tmp:
    #             print(i)
    #             return True
    # Added or modified after looking at author's solution
    """
    Determine if any duplicates exist in a given list (t). Return True if so, otherwise
    return False. The given list is unaltered.
    """
    tmp = t[:]
    tmp.sort()
    for i in range(len(tmp) - 1):
        if tmp[i] == tmp[i+1]:
            return True
    return False

def count_duplicates(t):
    """
    Count the number of duplicate sets in a given list (t). Return an integer value.
    Sets greater than two are considered a single duplicate set.
    """
    tmp = t[:]
    tmp.sort()
    count = 0
    for i in range(len(t) - 1):
        if tmp[i] == tmp[i + 1] and tmp[i] != tmp[i - 1]:
            count += 1
    return count

# Exercise 9  
# Write a function called remove_duplicates that takes a list and returns a new list
# with only the unique elements from the original. Hint: they don’t have to be in the
# same order.
def find_duplicates(t):
    dups = []
    for i in range(len(t) - 1):
        if t[i] == t[i + 1]:
            dups.append(i)
            dups.append(i + 1)
            

def remove_duplicates(t):
    res = t[:]
    res.sort()
    for i in range(len(tmp) - 1):
        if tmp[i] == tmp[i + 1]:
            res.remove(tmp[i])
    return res

# Exercise 11  
# To check whether a word is in the word list, you could use the in operator, but it
# would be slow because it searches through the words in order.
# Because the words are in alphabetical order, we can speed things up with a
# bisection search (also known as binary search), which is similar to what you do when
# you look a word up in the dictionary. You start in the middle and check to see
# whether the word you are looking for comes before the word in the middle of the list.
# If so, then you search the first half of the list the same way. Otherwise you search
# the second half.
# 
# Either way, you cut the remaining search space in half. If the word list has 113,809
# words, it will take about 17 steps to find the word or conclude that it’s not there.
# 
# Write a function called bisect that takes a sorted list and a target value and
# returns the index of the value in the list, if it’s there, or None if it’s not.
# 
# Or you could read the documentation of the bisect module and use that!
# Solution: http://thinkpython.com/code/inlist.py.

def get_slist(file, count=0):
    fin = open(file)
    res = list()
    i = 1
    for line in fin:
        word = line.strip()
        res.append(word)
        if i == count:
            break
        i += 1
    fin.close()
    return res

def bisect(slist, value):
    """
    Use the bisection method to find the index of a word in a list.
    Precondition: list is sorted
    """
    if not all(slist[i] <= slist[i+1] for i in range(len(slist)-1)):
        print('Please supply a sorted list.')
        return None
    start = 0
    end = len(slist)
    middle = int(end / 2)
    while slist[middle] != value:
        if slist[middle] > value:
            end = middle
        elif slist[middle] < value:
            start = middle
        middle = start + int((end - start) / 2)
    return middle
