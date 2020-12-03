from random import seed, randint
import sys

def f(arg_for_seed, nb_of_elements, max_element):
    '''
    >>> f(0, 0, 10)
    Here is L: []
    The second smallest element in L is: None
    The minimum gap in absolute value between successive elements in L is: 0
    >>> f(0, 1, 10)
    Here is L: [6]
    The second smallest element in L is: None
    The minimum gap in absolute value between successive elements in L is: 0
    >>> f(0, 2, 10)
    Here is L: [6, 6]
    The second smallest element in L is: None
    The minimum gap in absolute value between successive elements in L is: 0
    >>> f(1, 2, 10)
    Here is L: [2, 9]
    The second smallest element in L is: 9
    The minimum gap in absolute value between successive elements in L is: 7
    >>> f(0, 3, 10)
    Here is L: [6, 6, 0]
    The second smallest element in L is: 6
    The minimum gap in absolute value between successive elements in L is: 0
    >>> f(1, 4, 10)
    Here is L: [2, 9, 1, 4]
    The second smallest element in L is: 2
    The minimum gap in absolute value between successive elements in L is: 3
    >>> f(20, 5, 10)
    Here is L: [10, 2, 4, 10, 10]
    The second smallest element in L is: 4
    The minimum gap in absolute value between successive elements in L is: 0
    >>> f(1, 10, 20)
    Here is L: [4, 18, 2, 8, 3, 15, 14, 15, 20, 12]
    The second smallest element in L is: 3
    The minimum gap in absolute value between successive elements in L is: 1
    '''
    seed(arg_for_seed)
    L = [randint(0,max_element) for _ in range(nb_of_elements)]
    print ('Here is L:',L)
    if len(set(L)) > 1:
        a = sorted(L)
        a2 = a[1]
        p = []
        for x, y in zip(L, L[1:]):
            k = abs(y - x)
            p.append(k)
        a3 = min(p)
        print(f'The second smallest element in L is: {a2}')
        print(f'The minimum gap in absolute value between successive elements in L is: {a3}')
    else:
        print(f'The second smallest element in L is: None')
        print(f'The minimum gap in absolute value between successive elements in L is: 0')



    # if L == [] or len(L) == 1:
    #     b = None
    #     c = 0
    #     temp = 0
    # else:
    #     l1 = set(L)
    #     if len(l1) == 1:
    #         a = 0
    #         b = None
    #         c = 0
    #     else:
    #         a = min(l1)
    #         l1.remove(a)
    #         b = min(l1)
    #     temp = 999
    #     for x, y in zip(L, L[1:]):
    #         if abs(x - y) < temp:
    #             temp = abs(x - y)
        
    # print(f"The second smallest element in L is: {b}")
    # print(f"The minimum gap in absolute value between successive elements in L is: {temp}")

if __name__ == '__main__':
    import doctest
    doctest.testmod()
