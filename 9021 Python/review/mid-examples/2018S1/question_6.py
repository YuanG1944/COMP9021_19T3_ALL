import itertools as tool
def display(square):
    print('\n'.join(' '.join(f'{x:2d}' for x in row) for row in square))

def check_out_square_and_fix_if_corrupted(square):
    '''
    Call "good square" an n x n matrix with n >= 2 consisting of all numbers
    between 1 and n ** 2.
    Call "corrupted square" a good square exactly one of whose entries has been
    replaced by 0.

    Note: marks can be scored by just checking whether the square is good or corrupted,
    without fixing it in case it is corrupted -- but hard coding won't help.
    
    >>> check_out_square_and_fix_if_corrupted([[1, 5, 7],\
                                               [2, 9, 3],\
                                               [6, 4, 8]])
    Here is the square: 
     1  5  7
     2  9  3
     6  4  8
    It is a good square.
    >>> check_out_square_and_fix_if_corrupted([[1, 5, 7],\
                                               [2, 9, 3],\
                                               [6, 10, 8]])
    Here is the square: 
     1  5  7
     2  9  3
     6 10  8
    It is neither a good nor a corrupted square.
    >>> check_out_square_and_fix_if_corrupted([[1, 5, 7],\
                                               [2, 9, 0],\
                                               [6, 4, 8]])
    Here is the square: 
     1  5  7
     2  9  0
     6  4  8
    It is a corrupted square, the good square being:
     1  5  7
     2  9  3
     6  4  8
    >>> check_out_square_and_fix_if_corrupted([[1, 5, 7, 11],\
                                               [2, 9, 0, 16],\
                                               [6, 4, 8, 12],\
                                               [13, 14, 15, 2]])
    Here is the square: 
     1  5  7 11
     2  9  0 16
     6  4  8 12
    13 14 15  2
    It is neither a good nor a corrupted square.
    >>> check_out_square_and_fix_if_corrupted([[1, 5, 7, 11],\
                                               [3, 9, 0, 16],\
                                               [6, 4, 8, 12],\
                                               [13, 14, 15, 2]])
    Here is the square: 
     1  5  7 11
     3  9  0 16
     6  4  8 12
    13 14 15  2
    It is a corrupted square, the good square being:
     1  5  7 11
     3  9 10 16
     6  4  8 12
    13 14 15  2
    '''
    n = len(square)
    if n < 2 or any(len(line) != n for line in square):
        return False
    print('Here is the square: ')
    display(square)
    good_square = False
    corrupted_square = False
    # Insert your code here
    a = list(tool.chain.from_iterable(square))
    aa = sorted(a)
    count = 0
    if aa[0] == 1:
        for x, y in zip(aa, aa[1:]):
            if x+1 == y:
                count += 1
        if count == len(a) - 1:
            print(f'It is a good square.')
        else:
            print(f'It is neither a good nor a corrupted square.')
    else:
        temp = []
        good = []
        aa.append(-1)
        for x, y in zip(aa, aa[1:]):
            if x+1 == y:
                temp.append(x)
            else:
                temp.append(x)
                good.append(temp)
                temp = []
        if len(good) != 2:
            print(f'It is neither a good nor a corrupted square.')
        else:
            k = good[1][0] - good[0][-1]
            for i in range(len(square)):
                for j in range(len(square[0])):
                    if square[i][j] == 0:
                        square[i][j] = good[0][-1] + 1 
            print(f'It is a corrupted square, the good square being:')
            display(square)

                
            
        
    

    
if __name__ == '__main__':
    import doctest
    doctest.testmod()
