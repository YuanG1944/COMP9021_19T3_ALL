from random import seed, randrange
from copy import copy, deepcopy

dim = 10
for_seed = 2
density = 2
seed(for_seed)
grid = [[int(randrange(density) != 0) for _ in range(dim)]
            for _ in range(dim)
       ]
def display_grid(gridx):
    for row in gridx:
        print('   ', *row)
display_grid(grid)

def find_group(i, j, map, fill):
    if 0 <= i < 10 and 0 <= j < 10:
        if map[i][j] == 1:
            map[i][j] = fill
            for x, y in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                find_group(i+x, j+y, map, fill)
    else:
        return map

def max_number_of_spikes():
    colour = 2
    for i in range(dim):
        for j in range(dim):
            if grid[i][j]:
                find_group(i, j, grid, colour)
            colour += 1

    print("\n")
    display_grid(grid)

    colour_dic = {}
    for i in range(dim):
        for j in range(dim):
            if grid[i][j] > 0:
                colour_dic.setdefault(grid[i][j], []).append((i,j))
    print(colour_dic)
    count = 0
    node = 0
    node_list = []
    for key in colour_dic:
        print(key)
        for value in colour_dic[key]:
            x, y = value
            for i, j in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                new = (x + i, y + j)
                if new in colour_dic[key]:
                    count += 1
            if count == 1:
                node += 1
                count = 0
            else:
                count = 0
        node_list.append(node)
        node = 0
    max_spikes = max(node_list)
    return max_spikes

print(max_number_of_spikes())