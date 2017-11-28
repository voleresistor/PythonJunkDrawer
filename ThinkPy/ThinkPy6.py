# Think Python chapter 6 examples and exercises
# 07/10/17

import math

# Section 6.1
# *************************************************************************************
# Fruitful functions
def area(radius):
    return (math.pi * radius**2)

def absolute_value(x):
    if x < 0:
        return -x
    else:
        return x

# Exercise 1
# Write a compare function that returns 1 if x > y, 0 if x == y, and -1 if x < y.
def compare_numbers(x, y):
    if x > y:
        return 1
    elif x < y:
        return -1
    else:
        return 0

# Section 6.2
# *************************************************************************************
# Incremental development and scaffolding
# Slowly built up function one piece at a time by adding and checking one step at a time
# The resulting print statements are called scaffolding
# Scaffolding can be removed once function is finalized
# eg. The following scaffolded function vs the final function:
# def distance(x1, y1, x2, y2):
#    dx = x2 - x1
#    dy = y2 - y1
#    print 'dx is', dx
#    print 'dy is', dy
#    return 0.0

def distance(x1, y1, x2, y2):
    # Pythagorean theorum: a**2 + b**2 = c**2
    return (math.sqrt((x2 - x1)**2 + (y2 - y1)**2))

# Exercise 2
# Use incremental development to write a function called hypotenuse that returns the
# length of the hypotenuse of a right triangle given the lengths of the two legs as
# arguments. Record each stage of the development process as you go.

# Step 1
def hypotenuse(a, b):
    return 0.0
# returns 0.0

# Step 2
def hypotenuse(a, b):
    asq = a**2
    bsq = b**2
    print ('a squared is %s' % (asq))
    print ('b squared is %s' % (bsq))
    return 0.0
# Prints asq and bsq and returns 0.0

# Step 3
def hypotenuse(a, b):
    asq = a**2
    bsq = b**2
    csq = asq + bsq
    print ('c squared is %s' % (csq))
    return 0.0
# Prints csq and returns 0.0

# Step 4
def hypotenuse(a, b):
    asq = a**2
    bsq = b**2
    csq = asq + bsq
    result = math.sqrt(csq)
    return result
# returns hypotenuse

# Final
def hypotenuse(a, b):
    # Pythagorean theorum: a**2 + b**2 = c**2
    return math.sqrt(a**2 + b**2)
# Scaffolding and temp files removed

# Section 6.3
# *************************************************************************************
# Composition: The ability of functions to call other functions
def circle_area(xc, yc, xp, yp):
    #radius = distance(xc,xp,yc,yp)
    #result = area(radius)
    #return result
    return (area(distance(xc,yc,xp,yp)))

# Section 6.4
# *************************************************************************************
# Functions can return booleans
# Exercise 3
# Write a function is_between(x, y, z) that returns True if x ≤ y ≤ z or False otherwise.
# Is y between x and z?
def is_between(x, y, z):
    if x <= y and y <= z:
        return True
    else:
        return False

# Section 6.5
# *************************************************************************************
# Recursion using factorials
def factorial(n):
    if n == 0:
        return 1
    else:
        recurse = factorial(n-1)
        result = n * recurse
        return result

# Section 6.6
# *************************************************************************************
# It's safe to assume that functions have been tested and are working correctly
# when reading program flow. To do otherwise could mean wasting significant time
# reading a program. Example: We assume Python's built in functions work without
# inspecting them each time we read a program

# Section 6.7
# *************************************************************************************
# Another example of recursion using Fibonacci
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Section 6.8
# *************************************************************************************
# Type checking
# Sometimes it's useful to verify that the data provided is the appropriate type
def factorial(n):
    if not isinstance(n, int):
        print ('Factorial is only defined for integers!')
        return None
    elif n < 0:
        print ('Factorial is not defined for negative integers!')
        return None
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Section 6.9
# *************************************************************************************
# Debugging - 3 places for bugs in a function
# 1. The data being given to the function (precondition)
# 2. The data being returned by the function (postcondition)
# 3. The way the returned data is used
# Check these by inserting print statements in functions to denote the program flow and
# the values being handled. Some values may need to be checked by hand
def factorial(n):
    space = ' ' * (4 * n)
    print ('%sfactorial %s' % (space, n))
    if n == 0:
        print ('%sreturning 1' % (space))
        return 1
    else:
        recurse = factorial(n-1)
        result = n * recurse
        print ('%sreturning %s' % (space, result))
        return result

# Section 6.11
# *************************************************************************************
# Exercise 5
# The Ackermann function, A(m, n), is defined:
# A(m, n) = 		
#               n+1	if  m = 0 
#         A(m−1, 1)	if  m > 0  and  n = 0 
# A(m−1, A(m, n−1))	if  m > 0  and  n > 0.
# See http://en.wikipedia.org/wiki/Ackermann_function. Write a function named ack that
# evaluates Ackermann’s function. Use your function to evaluate ack(3, 4), which should
# be 125. What happens for larger values of m and n?
# Solution: http://thinkpython.com/code/ackermann.py.
# Even at 3,4 this function recurses VERY deeply. At (4,6), the recursion limit is reached
# and Python raises an exception.
def ack(m, n):
    if not m >= 0 or not n >=0:
        print ('Values m and n must not be negative.')
        return None
    if m == 0:
        return n+1
    elif n == 0:
        return ack(m-1, 1)
    #else:
    # Removed as per the given solution. Is it better to return seprately or as
    # part of the conditional?
    return ack(m-1, ack(m, n-1))

# Exercise 6  
# A palindrome is a word that is spelled the same backward and forward, like “noon” and
# “redivider”. Recursively, a word is a palindrome if the first and last letters are the
# same and the middle is a palindrome.
# The following are functions that take a string argument and return the first, last, and
# middle letters:

def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

# We’ll see how they work in Chapter 8.
# Type these functions into a file named palindrome.py and test them out. What happens
# if you call middle with a string with two letters? One letter? What about the empty string,
# which is written '' and contains no letters?
# A1: Return is ''
# A2: Return is ''
# A3: Return is ''
#
# Write a function called is_palindrome that takes a string argument and returns True if it
# is a palindrome and False otherwise. Remember that you can use the built-in function len
# to check the length of a string.
# Solution: http://thinkpython.com/code/palindrome_soln.py.
def is_palindrome(word):
    if not first(word) == last(word):
        return False
    elif len(middle(word)) < 2:
        return True
    else:
        return is_palindrome(middle(word))

# Exercise 7  
# A number, a, is a power of b if it is divisible by b and a/b is a power of b. Write a
# function called is_power that takes parameters a and b and returns True if a is a power
# of b. Note: you will have to think about the base case.
def is_power(a, b):
    if a % b == 0 and (a / b) / b > 1:
        return is_power(int(a/b), b)
    elif a % b == 0 and (a / b) / b == 1:
        return True
    else:
        return False

# Exercise 8  
# The greatest common divisor (GCD) of a and b is the largest number that divides both
# of them with no remainder.
# One way to find the GCD of two numbers is based on the observation that if r is the
# remainder when a is divided by b, then gcd(a, b) = gcd(b, r). As a base case, we can
# use gcd(a, 0) = a.
# 
# Write a function called gcd that takes parameters a and b and returns their greatest
# common divisor.
# 
# Credit: This exercise is based on an example from Abelson and Sussman’s Structure and
# Interpretation of Computer Programs.
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)