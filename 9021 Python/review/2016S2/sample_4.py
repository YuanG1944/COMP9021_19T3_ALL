
def is_heterosquare(square):
    '''
    A heterosquare of order n is an arrangement of the integers 1 to n**2 in a square,
    such that the rows, columns, and diagonals all sum to DIFFERENT values.
    In contrast, magic squares have all these sums equal.
    
    
    >>> is_heterosquare([[1, 2, 3],\
                         [8, 9, 4],\
                         [7, 6, 5]])
    True
    >>> is_heterosquare([[1, 2, 3],\
                         [9, 8, 4],\
                         [7, 6, 5]])
    False
    >>> is_heterosquare([[2, 1, 3, 4],\
                         [5, 6, 7, 8],\
                         [9, 10, 11, 12],\
                         [13, 14, 15, 16]])
    True
    >>> is_heterosquare([[1, 2, 3, 4],\
                         [5, 6, 7, 8],\
                         [9, 10, 11, 12],\
                         [13, 14, 15, 16]])
    False
    '''
    n = len(square)
    if any(len(line) != n for line in square):
        return False
    # Insert your code here
    square2 = list(map(list, zip(*square)))
    a = []
    b = []
    c = []
    for value in square:
        temp = sum(value)
        a.append(temp)
    for value in square2:
        temp = sum(value)
        a.append(temp)
    for num in range(len(square)):
        b.append(square[num][num])
    for num in range(len(square)):
        k = square[num][::-1]
        c.append(k[num])
    a.append(sum(b))
    a.append(sum(c))
    if len(set(a)) == len(a):
        print('True')
    else:
        print('False')
    # i_list = []
    # j_list = []
    # temp = []
    # temp2 = []
    # temp3 = []
    # value_list = []
    # for i in square:
    #     i_list.append(sum(i))
    # for i in range(len(square[0])):
    #     for j in range(len(square)):
    #         temp.append(square[j][i])
    #     j_list.append(sum(temp))
    #     temp = []
    # for i in range(len(square)):
    #     temp2.append(square[i][i])
    # for i in range(len(square)):
    #     temp3.append(square[i][-(i+1)])
    # l = sum(temp3)
    # r = sum(temp2)
    # for value in i_list:
    #     value_list.append(value)
    # for value in j_list:
    #     value_list.append(value)
    # value_list.append(l)
    # value_list.append(r)
    # value_list2 = set(value_list)
    # if len(value_list) == len(value_list2):
    #     print('True') #return True
    # else:
    #     print('False') #retune False
 
# Possibly define other functions

    
if __name__ == '__main__':
    import doctest
    doctest.testmod()
    # is_heterosquare([[1, 2, 3, 4], \
    #                  [5, 6, 7, 8], \
    #                  [9, 10, 11, 12], \
    #                  [13, 14, 15, 16]])
