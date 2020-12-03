import sys

def prime(n):
    isp = [True] * (n + 1)
    for i in range(2, int(n ** 0.5 + 1)):
        if isp[i]:
            for j in range(i * i, n + 1, i):
                isp[j] = False
    return [x for x in range(2, n+1) if isp[x]]

def f(a, b):
    '''
    The prime numbers between 2 and 12 (both included) are: 2, 3, 5, 7, 11
    The gaps between successive primes are: 0, 1, 1, 3.
    Hence the maximum gap is 3.
    
    Won't be tested for b greater than 10_000_000
    
    >>> f(3, 3)
    The maximum gap between successive prime numbers in that interval is 0
    >>> f(3, 4)
    The maximum gap between successive prime numbers in that interval is 0
    >>> f(3, 5)
    The maximum gap between successive prime numbers in that interval is 1
    >>> f(2, 12)
    The maximum gap between successive prime numbers in that interval is 3
    >>> f(5, 23)
    The maximum gap between successive prime numbers in that interval is 3
    >>> f(20, 106)
    The maximum gap between successive prime numbers in that interval is 7
    >>> f(31, 291)
    The maximum gap between successive prime numbers in that interval is 13
    '''
    c = set(prime(b)) - set(prime(a))
    aa = []
    if c:
        if len(c) == 1:
            print(f'The maximum gap between successive prime numbers in that interval is 1')
        else:
            c = sorted(c)
            for x, y in zip(c, c[1:]):
                num = y - x - 1
                aa.append(num)
            p = max(aa)
            print(f'The maximum gap between successive prime numbers in that interval is {p}')


    else:
        print(f'The maximum gap between successive prime numbers in that interval is 0')
    # if a <= 0 or b < a:
    #     sys.exit()
    # max_gap = 0
    # # Insert your code here
    # p_list = []
    # pp = []
    # for value in range(a, b + 1):
    #     if prime(value):
    #         p_list.append(value)
    # for x, y in zip(p_list, p_list[1:]):
    #     pp.append(y-x-1)
    # if pp == []:
    #     p_max = 0
    # else:
    #     p_max = max(pp)
    # print(f"The maximum gap between successive prime numbers in that interval is {p_max}")
                 

if __name__ == '__main__':
    import doctest
    doctest.testmod()
