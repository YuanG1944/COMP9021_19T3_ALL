import re

def get_matrix(filename):
    maze = open(filename)
    draft_list = []
    maze_dic = {}
    maze_list = []
    i = 0
    lines = maze.readlines()
    for value in lines:
        if re.match(r'^[\n]+$', value):
            pass
        else:
            draft_list.append(value)
    for value in draft_list:
        if re.findall(r'[0-9]+', value):
            num = re.findall(r'[0-9]+', value)
            num = ''.join(num)
            maze_dic[i] = num
            i += 1
    for value in maze_dic.values():
        maze_list.append(value)
    #判断是错误输出
    for i in range(len(maze_list)):
        for j in range(len(maze_list[i])):
            if maze_list[i][j] not in ['0', '1', '2', '3']:
                return None
    if len(maze_list) < 2 or len(maze_list) > 41:
        return None
    for i in range(len(maze_list) - 1):
        if len(maze_list[i]) < 2 or len(maze_list[i]) > 31:
            return None
        if len(maze_list[i]) != len(maze_list[i+1]):
            return None
    #判断不是个地图
    for key in maze_dic.keys():
        if maze_dic[key][len(maze_dic[key]) - 1] == '1' or maze_dic[key][len(maze_dic[key]) - 1] == '3':
            return False
    for key2 in range(len(maze_dic[0])):
        if maze_dic[len(maze_dic) - 1][key2] == '2' or maze_dic[len(maze_dic) - 1][key2] == '3':
            return False

    return maze_list


def display_grid(gridx):
    for row in gridx:
        print('   ', *row)

a = get_matrix('incorrect_input_6.txt')
print(a)
if a:
    display_grid(a)