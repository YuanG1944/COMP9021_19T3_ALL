import sys
from math import sqrt
from itertools import compress

def prime(n):
    isp = [True] * (n + 1)
    for i in range(2, int(n ** 0.5 + 1)):
        if isp[i]:
            for j in range(i * i, n + 1, i):
                isp[j] = False
    return [x for x in range(2, n + 1) if isp[x]]


def f(n):
    '''
    Won't be tested for n greater than 10_000_000
    
    >>> f(3)
    The largest prime strictly smaller than 3 is 2.
    >>> f(10)
    The largest prime strictly smaller than 10 is 7.
    >>> f(20)
    The largest prime strictly smaller than 20 is 19.
    >>> f(210)
    The largest prime strictly smaller than 210 is 199.
    >>> f(1318)
    The largest prime strictly smaller than 1318 is 1307.
    '''
    if n <= 2:
        sys.exit()
    largest_prime_strictly_smaller_than_n = 0
    # Insert your code here
    a = prime(n)
    if n in a:
        pr = a[-2]
    else:
        pr = a[-1]
    print(f'The largest prime strictly smaller than {n} is {pr}.')

if __name__ == '__main__':
    import doctest
    doctest.testmod()
