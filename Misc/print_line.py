'''
Do things
'''
import sys

def print_line(max_range, divisor):
    '''
    I have no idea
    '''
    for i in range(max_range):
        if i % divisor == 0:
            print("X", end="")
        else:
            print(".", end="")
    print("\n")

print_line(int(sys.argv[1]), int(sys.argv[2]))
