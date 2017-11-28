# Think Python chapter 11 examples and exercises
# 07/20/2017

import math

# Dictionaries
# *************************************************************************************

# Exercise 1  
# Write a function that reads the words in words.txt and stores them as keys in a
# dictionary. It doesn’t matter what the values are. Then you can use the in operator as
# a fast way to check whether a string is in the dictionary.
# If you did Exercise 11, you can compare the speed of this implementation with the list
# in operator and the bisection search.
def store_words(file):
    fin = open(file)
    res = dict()
    i = 0
    for line in fin:
        word = line.strip()
        res[word] = i
        i += 1
    fin.close()
    return res


# Section 11.1
# *************************************************************************************
# 

# Exercise 8  
# Exponentiation of large integers is the basis of common algorithms for public-key
# encryption. Read the Wikipedia page on the RSA algorithm
# (http://en.wikipedia.org/wiki/RSA_(algorithm)) and write functions to encode and decode
# messages.

primes = [3, 5, 7, 11, 13, 17, 19, 23, 27, 29, 31, 37, 41]

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def rsa_generate(b):
    if not b >= 256:
        print('Must be at least 256 bits')
        return -1
    e = 65537
    n = 0
    p = 0
    q = 0
    while math.gcd(e, n) != 1 or abs(p - q)>>(int((b / 2) - 100)) == 0:
        p = random.getrandbits(int(b / 2))
        q = random.getrandbits(int(b / 2))
        n = int(lcm(p - 1, q - 1))
    keys = {'n': p * q, 'e': e, 'd': modinv(e, n)}
    return keys

def lcm(i, j):
    return (i * j) / math.gcd(i, j)

# /**
#  * Encrypt
#  *
#  * @param   {m} int / bigInt: the 'message' to be encoded
#  * @param   {n} int / bigInt: n value returned from RSA.generate() aka public key (part I)
#  * @param   {e} int / bigInt: e value returned from RSA.generate() aka public key (part II)
#  * @returns {bigInt} encrypted message
#  */
# RSA.encrypt = function(m, n, e){
# 	return bigInt(m).modPow(e, n);   
# };
def rsa_encrypt(m, n, e):
    return m # At this point, it looks like doing a modpow as in the c example is not simple in python

# /**
#  * Decrypt
#  *
#  * @param   {c} int / bigInt: the 'message' to be decoded (encoded with RSA.encrypt())
#  * @param   {d} int / bigInt: d value returned from RSA.generate() aka private key
#  * @param   {n} int / bigInt: n value returned from RSA.generate() aka public key (part I)
#  * @returns {bigInt} decrypted message
#  */
# RSA.decrypt = function(c, d, n){
# 	return bigInt(c).modPow(d, n);   
# };
def rsa_decrypt(c, d, n):
    return c # Same modpow issue


# Exercise 9  
# If you did Exercise 8, you already have a function named has_duplicates that takes a list
# as a parameter and returns True if there is any object that appears more than once in the list.
# Use a dictionary to write a faster, simpler version of has_duplicates.
# Solution: http://thinkpython.com/code/has_duplicates.py.
# 
# Exercise 10  
# Two words are “rotate pairs” if you can rotate one of them and get the other (see rotate_word
# in Exercise 12).
# Write a program that reads a wordlist and finds all the rotate pairs.
# Solution: http://thinkpython.com/code/rotate_pairs.py.
# 
# Exercise 11  
# Here’s another Puzzler from Car Talk (http://www.cartalk.com/content/puzzlers):
# This was sent in by a fellow named Dan O’Leary. He came upon a common one-syllable, five-letter
# word recently that has the following unique property. When you remove the first letter, the
# remaining letters form a homophone of the original word, that is a word that sounds exactly the
# same. Replace the first letter, that is, put it back and remove the second letter and the result
# is yet another homophone of the original word. And the question is, what’s the word?
# Now I’m going to give you an example that doesn’t work. Let’s look at the five-letter word,
# ‘wrack.’ W-R-A-C-K, you know like to ‘wrack with pain.’ If I remove the first letter, I am left
# with a four-letter word, ’R-A-C-K.’ As in, ‘Holy cow, did you see the rack on that buck! It must
# have been a nine-pointer!’ It’s a perfect homophone. If you put the ‘w’ back, and remove the ‘r,’
# instead, you’re left with the word, ‘wack,’ which is a real word, it’s just not a homophone of
# the other two words.
# But there is, however, at least one word that Dan and we know of, which will yield two homophones
# if you remove either of the first two letters to make two, new four-letter words. The question
# is, what’s the word?
# 
# You can use the dictionary from Exercise 1 to check whether a string is in the word list.
# 
# To check whether two words are homophones, you can use the CMU Pronouncing Dictionary.
# You can download it from http://www.speech.cs.cmu.edu/cgi-bin/cmudict or
# from http://thinkpython.com/code/c06d and you can also download http://thinkpython.com/code/pronounce.py,
# which provides a function named read_dictionary that reads the pronouncing dictionary and returns a
# Python dictionary that maps from each word to a string that describes its primary pronunciation.
# 
# Write a program that lists all the words that solve the Puzzler.
# Solution: http://thinkpython.com/code/homophone.py.