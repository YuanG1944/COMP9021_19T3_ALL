import sys
from math import sqrt

def get_all_divisor(n):
    if n == 1:
        return [1]
    result = []
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            result.append(i)
            result.append(n // i)
    return result

def f(n):
    '''
    A number n is deficient if the sum of its proper divisors,
    1 included and itself excluded,
    is strictly smaller than n.
    
    >>> f(1)
    1 is deficient
    >>> f(2)
    2 is deficient
    >>> f(3)
    3 is deficient
    >>> f(6)
    6 is not deficient
    >>> f(29)
    29 is deficient
    >>> f(30)
    30 is not deficient
    >>> f(47)
    47 is deficient
    >>> f(48)
    48 is not deficient
    '''
    #input your code
    if n == 1:
        print(f'{n} is deficient')
    else:
        temp = 0
        for i in range(1, n):
            if n % i == 0:
                temp += i
        if n % temp == 0 and temp < n:
            print(f'{n} is deficient')
            temp = 0
        else:
            print(f'{n} is not deficient')
            temp = 0

def g(a, b):
    '''
    a and b are amicable if
    - the sum of the proper divisors of a, 1 included and a excluded, is equal to b, and
    - the sum of the proper divisors of b, 1 included and b excluded, is equal to a.
    
    >>> g(220, 284)
    220 and 284 are amicable.
    >>> g(2924, 2620)
    2924 and 2620 are amicable.
    >>> g(1084, 1208)
    1084 and 1208 are not amicable.
    >>> g(5010, 5574)
    5010 and 5574 are not amicable.
    
    '''
    temp1 = 0
    for i in range(1, a):
        if a % i == 0:
            temp1 += i
    temp2 = 0
    for j in range(1, b):
        if b % j == 0:
            temp2 += j
    if temp1 == b and temp2 == a:
        print(f'{a} and {b} are amicable.')
    else:
        print(f'{a} and {b} are not amicable.')

if __name__ == '__main__':
    import doctest
    doctest.testmod()
