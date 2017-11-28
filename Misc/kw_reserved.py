# Title: kw_reserved
# Author: Andrew Ogden
# Email: voleresistor@gmail.com
# Date: 07/06/17
# Return True/False if a word is reserved in Python

import sys

# Lists of Py2 and Py3 reserved keywords
KW = ['and', 'del', 'from', 'not', 'while', 'as', 'elif', 'global', 'or', 'with', 'assert',
      'else', 'if', 'pass', 'yield', 'break', 'except', 'import', 'print', 'class', 'in', 'raise',
      'continue', 'finally', 'is', 'return', 'def', 'for', 'lambda', 'try', 'exec', 'nonlocal']

# A kewl function to check for the presence of a word
#def get_reserved(word):
#    return word in KW

# We need some words to check
if not len(sys.argv) >= 2:
    print('Please provide at least one word on the command line.')
    quit()

# Loop through all items in sys.argv
for i in range(1, len(sys.argv)):
    #if get_reserved(sys.argv[i]):
    if sys.argv[i] in KW:
        print('\t%s - Reserved' % (sys.argv[i]))
    else:
        print('\t%s - Free' % (sys.argv[i]))
