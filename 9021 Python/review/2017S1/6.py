''' Hint in the form of syntactic notes:
    str(n) converts a number n to a string.
    set(s) converts a string s to a set of characters.
    len() returns the number of elements in its argument, e.g, a string, or a set.
    
    S1 | S2 returns the union of two sets S1 and S2.

'''

import sys

def once(n):
    m = str(n)
    m = list(m)
    k = set(m)
    if len(k) == len(m):
        return n
    else:
        return 0

def once2(n):
    m = ''.join(n)
    m = list(m)
    k = set(m)
    if len(k) == len(m):
        return n
    else:
        return 0

def f(a, b):
    '''
    Finds all numbers i and j with a <= i <= j <= b such that
    every digit occurs at most once in i, j and i * j.
    Outputs the solutions from smallest i to largest i,
    and for a given i from smallest j to largest j.
    
    >>> f(32, 49)
    32 * 49 = 1568 is a solution
    38 * 42 = 1596 is a solution
    >>> f(30, 50)
    32 * 49 = 1568 is a solution
    38 * 42 = 1596 is a solution
    >>> f(40, 80)
    48 * 65 = 3120 is a solution
    52 * 79 = 4108 is a solution
    53 * 76 = 4028 is a solution
    58 * 64 = 3712 is a solution
    59 * 68 = 4012 is a solution
    59 * 78 = 4602 is a solution
    68 * 74 = 5032 is a solution
    >>> f(50, 110)
    52 * 79 = 4108 is a solution
    53 * 76 = 4028 is a solution
    53 * 92 = 4876 is a solution
    57 * 86 = 4902 is a solution
    58 * 64 = 3712 is a solution
    59 * 68 = 4012 is a solution
    59 * 78 = 4602 is a solution
    59 * 108 = 6372 is a solution
    62 * 87 = 5394 is a solution
    68 * 74 = 5032 is a solution
    69 * 108 = 7452 is a solution
    72 * 95 = 6840 is a solution
    74 * 85 = 6290 is a solution
    '''
    once_list1 = []
    once_list2 = []
    r = []
    r2 = []
    for value in range(a, b + 1):
        if once(value):
            once_list1.append(value)
    for i in once_list1:
        for j in once_list1[::-1]:
            m = i * j
            once_list2.append([str(i), str(j), str(m)])
    for value in once_list2:
        if once2(value):
            r.append(value)
    for value in r:
        if int(value[0]) < int(value[1]):
            r2.append(value)
    r2 = sorted(r2, key=lambda x:(int(x[0]), int(x[1])))
    for value in r2:
        print(f"{value[0]} * {value[1]} = {value[2]} is a solution")


if __name__ == '__main__':
    import doctest

    doctest.testmod()
