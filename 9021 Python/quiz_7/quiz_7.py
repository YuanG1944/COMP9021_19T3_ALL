# COMP9021 19T3 - Rachid Hamadi
# Quiz 7 *** Due Thursday Week 9
#
# Randomly generates a grid of 0s and 1s and determines
# the maximum number of "spikes" in a shape.
# A shape is made up of 1s connected horizontally or vertically (it can contain holes).
# A "spike" in a shape is a 1 that is part of this shape and "sticks out"
# (has exactly one neighbour in the shape).


from random import seed, randrange
import sys


dim = 10


def display_grid():
    for row in grid:
        print('   ', *row) 


# Returns the number of shapes we have discovered and "coloured".
# We "colour" the first shape we find by replacing all the 1s
# that make it with 2. We "colour" the second shape we find by
# replacing all the 1s that make it with 3.
def find_group(
        i, j, map, fill):
    if 0 <= i < 10 and 0 <= j < 10:
        if map[i][j] == 1:
            map[i][j] = fill
            for x, y in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                find_group(i+x, j+y, map, fill)
    else:
        return map

def colour_shapes():
    colour = 2
    for i in range(dim):
        for j in range(dim):
            if grid[i][j]:
                find_group(i, j, grid, colour)
            colour += 1

    colour_dic = {}
    for i in range(dim):
        for j in range(dim):
            if grid[i][j] > 0:
                colour_dic.setdefault(grid[i][j], []).append((i, j))
    # print(colour_dic)
    count = 0
    node = 0
    node_list = []
    for key in colour_dic:
        # print(key)
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


def max_number_of_spikes(nb_of_shapes):
    return nb_of_shapes

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
nb_of_shapes = colour_shapes()
print('The maximum number of spikes of some shape is:',
      max_number_of_spikes(nb_of_shapes)
     )
