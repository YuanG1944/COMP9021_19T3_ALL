path_line_dic = {4: [(0, 1), (1, 0), (1, 1)], 6: [(7, 0), (7, 1), (8, 1), (9, 1)],
                 7: [(7, 4), (7, 5), (7, 6), (8, 4), (9, 4)]}
print(path_line_dic)
path_line_dic2 = {}
count = 0

for key in path_line_dic:
    # print(key)
    for value in path_line_dic[key]:
        print(path_line_dic[key])
        x, y = value
        if (x + 1, y) in path_line_dic[key]:
            count += 1
        if (x - 1, y) in path_line_dic[key]:
            count += 1
        if (x, y + 1) in path_line_dic[key]:
            count += 1
        if (x, y - 1) in path_line_dic[key]:
            count += 1
        if count > 2:
            path_line_dic2.setdefault(key, []).append(value)
        count = 0
for key in path_line_dic2:
    if path_line_dic2[key] != []:
        path_line_dic.pop(key)

print(path_line_dic)
print(path_line_dic2)
