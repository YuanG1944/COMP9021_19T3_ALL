from random import seed, randrange
from copy import copy, deepcopy

dim = 10
for_seed = 1
density = 4
seed(for_seed)
grid = [[int(randrange(density) != 0) for _ in range(dim)]
            for _ in range(dim)
       ]
def display_grid(gridx):
    for row in gridx:
        print('   ', *row)

grid_1 = deepcopy(grid)
grid_2 = deepcopy(grid)
grid_3 = deepcopy(grid)


def search_ele(i, j, map):
    if i < 9:
        if map[i][j] != 0 and map[i+1][j] != 0:
            map[i+1][j] = map[i][j] + map[i+1][j]
        search_ele(i + 1, j, map)
    return map

def search_ele_r(i, j, map):
    if i < 9 and j < 9:
        if map[i][j] != 0 and map[i+1][j+1] != 0:
            map[i+1][j+1] = map[i][j] + map[i+1][j+1]
        search_ele_r(i + 1, j + 1, map)
    return map

def search_ele_l(i, j, map):
    if i < 9 and j < 9:
        if map[i][j] != 0 and map[i+1][j-1] != 0:
            map[i+1][j-1] = map[i][j] + map[i+1][j-1]
        search_ele_r(i + 1, j-1, map)
    return map
print('\n')

# def change_value(function, map):
#     for value in range(10):
#         function(0, value, map)
#     display_grid(map)
#     print('\n')
#     for i in range(10):
#         for j in range(10):
#             if map[i][j] == 1:
#                 map[i][j] = 0
#     return map

def check_lr(a):
    one = []
    for value in range(len(a)):
        if a[value] != 0:
            x = str(a[value])
            one.append(x)
        else:
            one.append(',')
    one = ''.join(one)
    one = one.split(',')
    for value in one:
        if len(value) < 2:
            one.remove(value)
    for value in one:
        if len(value) < 2:
            one.remove(value)
    return one

#找出size的可能情况
def possible_size(map):
    size_list = []
    p = 0
    for value in map:
        possible_value = check_lr(value)

        for k in possible_value:
            min_num = 10
            if k == '':
                pass
            else:
                for j in k:
                    if int(j) <= min_num:
                        min_num = int(j)
                    size = len(k) * int(min_num)
                    if k.count(j) > 1:
                        p = int(j) * k.count(j)
                    if p > size:
                        size = p
                if size != None:
                    size_list.append(size)
    return size_list

for value in range(10):
    search_ele_l(0, value, grid_2)
display_grid(grid_2)
print('\n')
for i in range(10):
    for j in range(10):
        if grid_2[i][j] == 1:
            grid_2[i][j] = 0
display_grid(grid_2)





