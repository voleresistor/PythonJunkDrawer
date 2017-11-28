def check_fermat(a, b, c, n):
    if a**n + b**n == c**n:
        print ('Holy smokes, Fermat was wrong!')
    else:
        print ('No, that doesn\'t work.')

def get_input():
    a = input('A: ')
    a = int(a)
    b = input('B: ')
    b = int(b)
    c = input('C: ')
    c = int(c)
    n = input('N: ')
    n = int(n)
    if n > 2:
        check_fermat(a, b, c, n)
    else:
        print ('n must be greater than 2')

def is_triangle(a, b, c):
    if a + b >= c:
        print ('Yes')
    else:
        print ('No')

def check_triangle():
    a = int(input('First stick: '))
    b = int(input('Second stick: '))
    c = int(input('Long stick: '))

    is_triangle(a, b, c)

#get_input()
check_triangle()


def bitleft(x, b):
    while b != 0:
        x = x * 2
        b -= 1
    return x

def bitright(x, b):
    while b != 0:
        x = x // 2
        b -= 1
    return x