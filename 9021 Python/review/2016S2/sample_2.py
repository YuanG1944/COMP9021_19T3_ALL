import sys
from math import factorial


def f(n):
    '''
    >>> f(0)
    0 factorial is 1
    It has 1 digit, the trailing 0's excepted
    >>> f(4)
    4 factorial is 24
    It has 2 digits, the trailing 0's excepted
    >>> f(6)
    6 factorial is 720
    It has 2 digits, the trailing 0's excepted
    >>> f(10)
    10 factorial is 3628800
    It has 5 digits, the trailing 0's excepted
    >>> f(20)
    20 factorial is 2432902008176640000
    It has 15 digits, the trailing 0's excepted
    >>> f(30)
    30 factorial is 265252859812191058636308480000000
    It has 26 digits, the trailing 0's excepted
    >>> f(40)
    40 factorial is 815915283247897734345611269596115894272000000000
    It has 39 digits, the trailing 0's excepted
    '''
    if n < 0:
        sys.exit()
    n_factorial = factorial(n)
    nb_of_digits_excluding_the_trailing_0s = 0
    # Insert your code here
    a = str(n_factorial)
    b = a[::-1]
    b = int(b)
    b = str(b)
    c = len(b)
    print(f"{n} factorial is {n_factorial}")
    if c == 1:
        print(f"It has {c} digit, the trailing 0's excepted")
    else:
        print(f"It has {c} digits, the trailing 0's excepted")
    '''str_f = str(n_factorial)
    str_f = str_f[::-1]
    a = 0
    for num in range(len(str_f)):
        if str_f[num] != '0':
            a = num
            break
    str_f2 = str_f[a:]
    str_f2 = str_f2[::-1]
    l_dig = len(str_f2)
    print(f"{n} factorial is {n_factorial}")
    if l_dig == 1:
        print(f"It has {l_dig} digit, the trailing 0's excepted")
    else:
        print(f"It has {l_dig} digits, the trailing 0's excepted")'''
        
if __name__ == '__main__':
    import doctest
    doctest.testmod()
