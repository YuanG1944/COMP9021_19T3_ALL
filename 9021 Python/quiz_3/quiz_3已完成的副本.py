# Written by *** and Eric Martin for COMP9021

# Reading the number written in base 8 from right to left,
# keeping the leading 0's, if any:
# 0: move N     1: move NE    2: move E     3: move SE
# 4: move S     5: move SW    6: move W     7: move NW
#
# We start from a position that is the unique position
# where the switch is on.
#
# Moving to a position switches on to off, off to on there.

import sys

on = '\u26aa'
off = '\u26ab'
code = input('Enter a non-strictly negative integer: ').strip()
try:
    if code[0] == '-':
        raise ValueError
    int(code)
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
nb_of_leading_zeroes = 0
for i in range(len(code) - 1):
    if code[i] == '0':
        nb_of_leading_zeroes += 1
    else:
        break
print("Keeping leading 0's, if any, in base 8,", code, 'reads as',
      '0' * nb_of_leading_zeroes + f'{int(code):o}.'
     )
print()

# INSERT YOUR CODE HERE
code1 = code
code_list1 = []
def print_codelist(code, code_list):
    # 把八进制数每一个元素存入列表,并反转
    code_str = str('0' * nb_of_leading_zeroes + f'{int(code):o}')
    # print(code_str)
    for value in code_str:
        code_list.append(value)
    code_list = list(reversed((code_list)))
    return code_list

print_codelist(code1, code_list1)

#方向坐标
ordinate = [[0, 1],
            [1, 1],
            [1, 0],
            [1, -1],
            [0, -1],
            [-1, -1],
            [-1, 0],
            [-1, 1]]

def track_trail(code_list, x_y):
    #x_y轴轨迹
    trail_list = []
    trail = 0
    trail_list.append(trail)
    for value in range(len(code_list)):
        trail += ordinate[int(code_list[value])][x_y]
        trail_list.append(trail)

    return trail_list

#创建空棋盘
def create_matrix(x, y):
    matrix = [None] * y
    for i in range(len(matrix)):
        matrix[i] = [off] * x
    return matrix

#确定行列
def find_row_column(list):
    value = max(list) - min((list))
    return value

x_list = track_trail(code_list1, 0)
y_list = track_trail(code_list1, 1)

dictionary = []
dictionary2 = []
for value in range(len(x_list)):
    dictionary.append([x_list[value], y_list[value]])

for value in dictionary:
    if value in dictionary2:
        dictionary2.remove(value)
    else:
        dictionary2.append(value)

if dictionary2:
    x_list = []
    y_list = []
    for value in dictionary2:
        x_list.append(value[0])
        y_list.append(value[1])
    #确定行列数
    row_x = find_row_column(x_list)
    column_y = find_row_column(y_list)
    #找最大值
    max_x = max(x_list)
    max_y = max(y_list)
    num_x = row_x + 1
    num_y = column_y + 1

    for value in range(len(x_list)):
        x_list[value] = max_x - x_list[value]

    for value in range(len(y_list)):
        y_list[value] = max_y - y_list[value]

    chessboard = create_matrix(num_x, num_y)
    #将坐标输入棋盘
    for value in range(len(y_list)):
        if chessboard[y_list[value]][x_list[value]] == off:
            chessboard[y_list[value]][x_list[value]] = on

    chessboard = list(reversed((chessboard)))
    # #打印棋盘
    for i in range(num_y):
        for j in range(num_x):
            print(chessboard[i][j], end='')
        if i != num_y - 1:
            print('')


