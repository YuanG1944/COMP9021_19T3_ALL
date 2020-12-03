import sys
from math import sqrt

def get_all_divisor(n):
    if n == 1:
        return [1]
    result = set([])
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            result.add(i)
            result.add(n // i)
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
    if n == 1 or n == 2 or n ==3:
        print(f"{n} is deficient")
    else:
        divisors = get_all_divisor(n)
        if sum(divisors) + 1 < n:
            print(f"{n} is deficient")
        else:
            print(f"{n} is not deficient")

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
    a_divisors = get_all_divisor(a)
    b_divisors = get_all_divisor(b)
    if (1 + sum(a_divisors)) == b and (1 + sum(b_divisors)) == a:
        print(f"{a} and {b} are amicable.")
    else:
        print(f"{a} and {b} are not amicable.")


if __name__ == '__main__':
    import doctest
    doctest.testmod()
