# Think Python chapter 7 examples and exercises
# 07/11/2017

import math

# Section 7.3
# *************************************************************************************
# Loops

# Not obvious if n can ever reach the loop's exit criteria
def sequence(n):
    while n != 1:
        print ('%s ' % (n), end='')
        if n%2 == 0:    # n is even
            n = n/2
        else:           # n is odd
            n = n*3+1

# Exercise 1  
# Rewrite the function print_n from Section 5.8 using iteration instead of recursion.
# 5.8 function (Python 2):
def print_n(s, n):
    if n <= 0:
        return
    print s
    print_n(s, n-1)

# Exercise function (Python 3):
def print_n(s, n):
    while n > 0:
        print (s)
        n = n-1
    return

# Section 7.4
# *************************************************************************************
# Break - break out of loop immediately from somewhere inside the loop body
# Affirmative stop.("stop now") Normal while loop is negative stop ("keep going until")

while True:
    line = raw_input('> ')
    if line == 'done':
        break               # break example
    print line
print 'Done!'

# Section 7.5
# *************************************************************************************
# Square roots
# Can be estimated by iterating this formula: y = (x + a/x) / 2
# Stop when x = y, but because y is likely a float, need a way to decide if it's close
# enough
while True:
    print x
    y = (x + a/x) / 2
    if y == x:
        break
    x = y

# Exercise 2  
# Encapsulate this loop in a function called square_root that takes a as a parameter,
# chooses a reasonable value of x, and returns an estimate of the square root of a.
def square_root(a):
    epsilon = 0.000005
    x = a/4
    while True:
        y = (x + a/x) / 2
        if abs(y-x) < epsilon:
            break
        x = y
    return x

# Section 7.9
# *************************************************************************************
# Exercises
# Exercise 3  
# To test the square root algorithm in this chapter, you could compare it with
# math.sqrt. Write a function named test_square_root that prints a table like this:
# 1.0 1.0           1.0           0.0
# 2.0 1.41421356237 1.41421356237 2.22044604925e-16
# 3.0 1.73205080757 1.73205080757 0.0
# 4.0 2.0           2.0           0.0
# 5.0 2.2360679775  2.2360679775  0.0
# 6.0 2.44948974278 2.44948974278 0.0
# 7.0 2.64575131106 2.64575131106 0.0
# 8.0 2.82842712475 2.82842712475 4.4408920985e-16
# 9.0 3.0           3.0           0.0
# 
# The first column is a number, a; the second column is the square root of a computed
# with the function from Section 7.5; the third column is the square root computed by
# math.sqrt; the fourth column is the absolute value of the difference between the two
# estimates.
def test_square_root():
    a = 1.0
    print ('%s\t%s\t%s\t%s' % ('Digit'.ljust(3), 'Built In'.ljust(19), 'External'.ljust(19), 'Difference'.ljust(19)))
    print ('%s\t%s\t%s\t%s' % ('-----'.ljust(3), '--------'.ljust(19), '--------'.ljust(19), '----------'.ljust(19)))
    while a < 10:
        space = ' ' * 20
        built_in = math.sqrt(a)
        extern = square_root(a)
        diff = abs(built_in - extern)
        print ('%s\t%s\t%s\t%s' % (str(a).ljust(3), str(built_in).ljust(19), str(extern).ljust(19), str(diff).ljust(19)))
        a = a + 1

# Exercise 4  
# The built-in function eval takes a string and evaluates it using the Python
# interpreter. For example:
#
# >>> eval('1 + 2 * 3')
# 7
# >>> import math
# >>> eval('math.sqrt(5)')
# 2.2360679774997898
# >>> eval('type(math.pi)')
# <type 'float'>
#
# Write a function called eval_loop that iteratively prompts the user, takes the
# resulting input and evaluates it using eval, and prints the result.
# It should continue until the user enters 'done', and then return the value of the last
# expression it evaluated.
def eval_loop():
    while True:
        data = input('>')
        if data == 'done':
            print (eval(old))
            break
        print (eval(data))
        old = data

# Exercise 5  
# The mathematician Srinivasa Ramanujan found an infinite series that can be used to
# generate a numerical approximation of 1 / π:
# 1 / π = (2	√2 / 9801) ∞∑k=0 (4k)!(1103+26390k)/(k!)4 3964k
#  
# Write a function called estimate_pi that uses this formula to compute and return an
# estimate of π. It should use a while loop to compute terms of the summation until the
# last term is smaller than 1e-15 (which is Python notation for 10^−15). You can check
# the result by comparing it to math.pi.
# Solution: http://thinkpython.com/code/pi.py.
def estimate_pi():
    epsilon = 1e-15
    while True:
