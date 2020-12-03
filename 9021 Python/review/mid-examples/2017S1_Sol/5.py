import sys
from math import sqrt
from itertools import compress


# 利用byte求质数
def get_primes_3(n):
    """ Returns  a list of primes < n for n > 2 """
    sieve = bytearray([True]) * (n // 2)
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i // 2]:
            sieve[i * i // 2::i] = bytearray((n - i * i - 1) // (2 * i) + 1)

    return [2, *compress(range(3, n, 2), sieve[1:])]

def is_prime(n):
    # Only used to test odd numbers.
    return all(n % d for d in range(3, round(sqrt(n)) + 1, 2))

def f(a, b):
    '''
    Won't be tested for b greater than 10_000_000
    
    >>> f(3, 3)
    The number of prime numbers between 3 and 3 included is 1
    >>> f(4, 4)
    The number of prime numbers between 4 and 4 included is 0
    >>> f(2, 5)
    The number of prime numbers between 2 and 5 included is 3
    >>> f(2, 10)
    The number of prime numbers between 2 and 10 included is 4
    >>> f(2, 11)
    The number of prime numbers between 2 and 11 included is 5
    >>> f(1234, 567890)
    The number of prime numbers between 1234 and 567890 included is 46457
    >>> f(89, 5678901)
    The number of prime numbers between 89 and 5678901 included is 392201
    >>> f(89, 5678901)
    The number of prime numbers between 89 and 5678901 included is 392201
    '''
    count = 0
    for i in range(a,b+1):
        if is_prime(i):
            count+=1

    less_a_primes = get_primes_3(a + 1)
    less_b_primes = get_primes_3(b + 1)
    for item in less_a_primes:
        if item < a:
            less_b_primes.remove(item)

    count = len(less_b_primes)

    print(f'The number of prime numbers between {a} and {b} included is {count}')

if __name__ == '__main__':
    import doctest
    doctest.testmod()
