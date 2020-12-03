# COMP9021 19T3 - Rachid Hamadi
# Quiz 6 *** Due Thursday Week 8
#
# Randomly fills an array of size 10x10 with 0s and 1s, and outputs the size of
# the largest parallelogram with horizontal sides.
# A parallelogram consists of a line with at least 2 consecutive 1s,
# with below at least one line with the same number of consecutive 1s,
# all those lines being aligned vertically in which case the parallelogram
# is actually a rectangle, e.g.
#      111
#      111
#      111
#      111
# or consecutive lines move to the left by one position, e.g.
#      111
#     111
#    111
#   111
# or consecutive lines move to the right by one position, e.g.
#      111
#       111
#        111
#         111

from random import seed, randrange
from copy import deepcopy
import sys

dim = 10

def display_grid():
    for row in grid:
        print('   ', *row)

def check_lr(a):
    one = []
    left = []
    for value in range(len(a)):
        if a[value] > -10:
            x = a[value]
            left.append(x)
            if value == len(a) - 1:
                one.append(left)
                left = []
        else:
            if len(left) > 1:
                one.append(left)
            left = []
    return one

def location(map):
    one_list = []
    for i in range(dim):
        one = check_lr(map[i])
        one_list.append(one)
    return one_list

def change_value(map):
    for i in range(dim):
        for j in range(dim):
            if map[i][j] == 0:
                map[i][j] = -99
            else:
                map[i][j] = j
    return map

def change_left(map):
    i = 0
    for row in map:
        for j in range(len(row)):
            row[j] = int(row[j]) + i
        i += 1
    return map

def change_right(map):
    i = 0
    for row in map:
        for j in range(len(row)):
            row[j] = int(row[j]) - i
        i += 1
    return map

def extra_same_elem(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    iset = set1.intersection(set2)
    return list(iset)

def function(highstart, highend, inter, listone, listmax):
    if highend < 10:
        for j in range(len(listone[highend])):
            l = extra_same_elem(inter, listone[highend][j])
            if l and len(l) > 1:
                mj = len(l) * (highend - highstart + 1)
                listmax = function(highstart, highend + 1, l, listone, listmax)
                listmax.append(mj)
            else:
                listmax.append(0)
        return listmax
    else:
        return listmax

def size_of_largest_parallelogram():
    grid_1 = deepcopy(grid)
    list_max = []
    list_max2 = []
    list_max3 = []
    list_max4 = []
    grid_1 = change_value(grid_1)
    grid_2 = deepcopy(grid_1)
    list_one = location(grid_1)
    list_left = change_left(grid_2)
    list_right = change_right(grid_1)
    list_right = location(list_right)
    list_left = location(list_left)
    for i in range(dim - 1):
        for j in range(len(list_one[i])):
            new_list_max_down = function(i, i + 1, list_one[i][j], list_one, list_max)
            mmm1 = max(new_list_max_down)
            list_max2.append(mmm1)
        for j in range(len(list_left[i])):
            new_list_max_left = function(i, i + 1, list_left[i][j], list_left, list_max)
            mmm2 = max(new_list_max_left)
            list_max3.append(mmm2)
        for j in range(len(list_right[i])):
            new_list_max_right = function(i, i + 1, list_right[i][j], list_right, list_max)
            mmm3 = max(new_list_max_right)
            list_max4.append(mmm3)
    if list_max2:
        mmm0 = max(list_max2)
        return mmm0
    else:
        return 0

try:
    
    for_seed, density = (int(x) for x in input('Enter two integers, the second '
                                               'one being strictly positive: '
                                              ).split()
                    )
    if density <= 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(for_seed)
grid = [[int(randrange(density) != 0) for _ in range(dim)]
            for _ in range(dim)
       ]
print('Here is the grid that has been generated:')
display_grid()
size = size_of_largest_parallelogram()
if size:
    print('The largest parallelogram with horizontal sides '
          f'has a size of {size}.'
         )
else:
    print('There is no parallelogram with horizontal sides.')
