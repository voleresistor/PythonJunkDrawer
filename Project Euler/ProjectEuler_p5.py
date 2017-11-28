'''
Project Euler p5 - https://projecteuler.net/problem=5
	2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any
	remainder. What is the smallest positive number that is evenly divisible by all of the numbers
	from 1 to 20?

Author: Andrew Ogden
Date: 10/31/2015
Revision: 2
'''
import sys

def main(consecutive_divisors):
    '''
	Increments by the number of required consecutive divisors until all digits from 1 to
	consecutive_divisors an be verified as divisors of small_num.
    '''
    count_num = 0
    small_num = 0

    while small_num == 0:
        count_num += consecutive_divisors
        if all(count_num % i == 0 for i in range(1, consecutive_divisors)):
            small_num = count_num

    print(small_num)

if __name__ == "__main__":
    main(int(sys.argv[1]))
