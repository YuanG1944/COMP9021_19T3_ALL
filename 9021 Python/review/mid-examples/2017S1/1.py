from random import seed, randint
import sys
from collections import defaultdict
import csv

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

    if len(set(L)) < 2:
        print("The second smallest element in L is: None")
        print("The minimum gap in absolute value between successive elements in L is: 0")
    else:
        new_L = sorted(L)
        print(f"The second smallest element in L is: {new_L[1]}")
        first = new_L[0]
        result = []
        for second in L[1:]:
            result.append(second - first)
            first = second
        print(f"The minimum gap in absolute value between successive elements in L is: {min(result)}")


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    words = defaultdict(int)
    with open("dictionary.txt") as read_file:
        lines = read_file.readlines()
        print(lines)
        for line in lines:
            items = line.split(",")
            items[2]
            words[line.strip()] += 1
