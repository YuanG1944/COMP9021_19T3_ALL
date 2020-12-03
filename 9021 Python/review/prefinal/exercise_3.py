from itertools import compress,accumulate
from math import sqrt
import operator

def prime(n):
    isp = [True] * (n + 1)
    for i in range(2, int(n ** 0.5 + 1)):
        if isp[i]:
            for j in range(i * i, n + 1, i):
                isp[j] = False
    return [x for x in range(2, n + 1) if isp[x]]

def single_factors(number):
    '''
    Returns the product of the prime divisors of "number"
    (using each prime divisor only once).

    You can assume that "number" is an integer at least equal to 2.

    >>> single_factors(2)
    2
    >>> single_factors(4096)                 # 4096 == 2**12
    2
    >>> single_factors(85)                   # 85 == 5 * 17
    85
    >>> single_factors(10440125)             # 10440125 == 5**3 * 17**4
    85
    >>> single_factors(154)                  # 154 == 2 * 7 * 11
    154
    >>> single_factors(52399401037149926144) # 52399401037149926144 == 2**8 * 7**2 * 11**15
    154
    '''
    
    p = []
    a = prime(1000)
    for value in a:
        while number % value == 0:
            p.append(value)
            number = int(number // value)
    p = set(p)
    r = 1
    for value in p:
        r *= value
    print(r)
        
    

if __name__ == '__main__':
    import doctest
    doctest.testmod()
