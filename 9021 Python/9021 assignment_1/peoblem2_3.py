import itertools
import re
from math import pow

p1 = 'GGGFGDFs'
p = p1

#
# print(l1)
# 第一步,在重复元素处切片
def split_list(l):
    # 1.先在重复的地方切片
    l2 = []
    if re.findall(r'([A-Za-z])\1{1,2}', l):
        check_repeat = re.findall(r'([A-Za-z])\1{1,2}', l)
        # print(check_repeat)
    else:
        l2.append(l)
        return l2
    ln = l
    for value in check_repeat:
        loc = ln.index(value)
        k = len(ln)
        while k:
            if loc + 1 < len(ln):
                if ln[loc] == ln[loc + 1]:
                    loc += 1
            k -= 1
        # print(loc)
        slide = ln[:loc + 1]
        l2.append(slide)
        ln = ln.replace(slide, '')
    if ln != '':
        l2.append(ln)
    return l2


# 第二步切在XXX,XX处切片
def split_list_2(l):
    ln = []
    for i in l:
        if re.findall(r'([A-Za-z])\1{1,2}', i):
            slide1 = i[:i.index(i[-1])]
            slide2 = i[i.index(i[-1]):i.rindex(i[-1]) + 1]
            ln.append(slide1)
            ln.append(slide2)
        else:
            ln.append(i)
    return ln


# 第三步含有相同元素组切片
def split_list_3(l):
    ln = []
    lp = []
    for value in l:
        mem = ''
        for k in value:
            cnt = value.count(k)
            if cnt > 1:
                mem = k
        # print(mem)
        slide1 = value[:value.index(mem)]
        slide2 = value[value.index(mem):value.rindex(mem) + 1]
        slide3 = value[value.rindex(mem) + 1:]
        # print(slide1)
        # print('asd')
        # print(slide2)
        if mem:
            ln.append(slide1)
            ln.append(slide2)
            ln.append(slide3)
        else:
            ln.append(value)

    for value in ln:
        if value != '':
            lp.append(value)
    return lp



#第四步把余下的拆成两两一组
# def split_list_4(l):
#     list = []
#     for value in l:
#         if len(value) >= 3 and value[0] != value[-1]:
#             value = value[::-1]
#             k = [value[i:i + 2][::-1] for i in range(0, len(value), 2)]
#             k = k[::-1]
#             for val in k:
#                 list.append(val)
#         else:
#             list.append(value)
#     return list

#奇数情况

#中置前置奇数情况
def fm_even_condition(l):
    a = list(l)
    for value in range(len(a) - 1):
        if value % 2 == 1:
            temp = a[value]
            a[value] = a[value + 1]
            a[value + 1] = temp
    a = ''.join(a)
    return a
#中置前置偶数情况
def fm_odd_condition(l):
    b = list(l)
    for value in range(len(b) - 1):
        if value % 2 == 0:
            temp = b[value]
            b[value] = b[value + 1]
            b[value + 1] = temp
    b = ''.join(b)
    return b

#后置偶数情况
def b_even_condition(l):
    a = list(l)
    for value in range(len(a) - 1):
        if value % 2 == 0:
            temp = a[value]
            a[value] = a[value + 1]
            a[value + 1] = temp
    a = ''.join(a)
    return a
#后置奇数情况
def b_odd_condition(l):
    b = list(l)
    for value in range(len(b) - 1):
        if value % 2 == 1:
            temp = b[value]
            b[value] = b[value + 1]
            b[value + 1] = temp
    b = ''.join(b)
    return b

# key = 'DD'
def posibility_rule(list):
    value_dic = {}
    for value in list:
        value_dic[value] = ''

    for key, value in value_dic.items():
        # print(len(key))
        if re.match(r'^([a-zA-Z])\1{0,2}$', key):
            value_dic[key] = [key[0], '_' + key[0]]
        elif len(key) == 2 and key[0] != key[1]:
            value_dic[key] = [key[1] + key[0], key[0] + key[1], '_' + key[0] + key[1], '_' + key[1] + key[0]]
        elif len(key) == 3 and key[0] == key[-1] and key[1] != key[0]:
            value_dic[key] = [key[0] + '_' + key[1], '_' + key[0] + '_' + key[1]]
        elif len(key) == 4 and key[0] == key[-1]:
            value_dic[key] = [key[1] + key[0] + '_' + key[2]]
        elif len(key) >= 3 and key == list[-1]:
            # print('run1')
            if len(key) % 2 == 1:
                k = b_odd_condition(key)
                value_dic[key] = [k, '_' + k]
            else:
                k = b_even_condition(key)
                value_dic[key] = [k, '_' + k]
        else:
            # print('run2')
            if len(key) % 2 == 1:
                k = fm_odd_condition(key)
                value_dic[key] = [k, '_' + k]
            else:
                k = fm_even_condition(key)
                value_dic[key] = [k, '_' + k]

    # print(value_dic)

    possibility_list = []
    for i in itertools.product(*value_dic.values()):
        # print(i)
        possibility_list.append(i)
    # print(possibility_list)
    possibility_string = []
    for value in possibility_list:
        string = "".join(value)
        possibility_string.append(string)
    return possibility_string



# 做罗马数字对应的数字表
def MakeGRList(general_roman):
    general_roman_num_dic = {}
    general_roman_num_list = general_roman[::-1]
    i = 1
    j = 5
    for value in range(len(general_roman_num_list)):
        if value % 2 == 0:
            general_roman_num_dic[general_roman_num_list[value]] = i
            i = i * 10
        else:
            general_roman_num_dic[general_roman_num_list[value]] = j
            j = j * 10
    return general_roman_num_dic


# 求出最大长度,和最后一组元素用来确定最大值
def maxLen(general_roman):
    general_roman_num_list = general_roman[::-1]
    # print(general_roman_num_list)
    roman_set = [general_roman_num_list[i:i + 2] for i in range(0, len(general_roman_num_list), 2)]
    last_list = roman_set[len(roman_set) - 1]
    return (len(roman_set) - 1), last_list


# 做伪罗马数字表
def MakeANList(general_roman):
    a, last_list = maxLen(general_roman_num)
    general_roman_num_list = general_roman[::-1]
    # print(general_roman_num_list)
    roman_set = [general_roman_num_list[i:i + 2] for i in range(0, len(general_roman_num_list), 2)]
    general_roman_ch_dic = {}
    for value in range(len(roman_set) - 1):
        i = roman_set[value][0]
        j = roman_set[value][1]
        one = i
        two = i + i
        three = i + i + i
        four = i + j
        five = j
        six = j + i
        seven = j + i + i
        eight = j + i + i + i
        nine = i + roman_set[value + 1][0]
        list_num = ["", one, two, three, four, five, six, seven, eight, nine]
        general_roman_ch_dic[value + 1] = list_num

    for value in range(len(roman_set) - 1, len(roman_set)):
        if len(last_list) == 2:
            i = roman_set[value][0]
            j = roman_set[value][1]
            one = i
            two = i + i
            three = i + i + i
            four = i + j
            five = j
            six = j + i
            seven = j + i + i
            eight = j + i + i + i
            list_num2 = ["", one, two, three, four, five, six, seven, eight]
        else:
            i = roman_set[value][0]
            one = i
            two = i + i
            three = i + i + i
            list_num2 = ["", one, two, three]
        general_roman_ch_dic[value + 1] = list_num2
    return general_roman_ch_dic


# 数字转罗马数字
def GeneralIntConvertRomnum(int_num):
    a, last_list = maxLen(general_roman_num)
    if len(last_list) == 1:
        bound = 4 * int(pow(10, a))
    else:
        bound = 10 * int(pow(10, a))
    # print(bound)
    if int_num >= bound:
        return False
    else:
        rom_rule = MakeANList(general_roman_num)
        # print(rom_rule)
        num_list = []
        key = len(str(int_num))
        while key:
            # print(rom_rule[key][(int_num // int(pow(10, key - 1))) % 10])
            num_list.append(rom_rule[key][(int_num // int(pow(10, key - 1))) % 10])
            key -= 1
        rom_num = ""
        for num in num_list:
            rom_num = rom_num + num
        return rom_num


# 罗马数字转换阿拉伯数字
def GeneralRomnumConvertInt(rom_num):
    if rom_num[0] == '_':
        return False
    a, last_list = maxLen(general_roman_num)
    if len(last_list) == 1:
        bound = 4 * int(pow(10, a))
    else:
        bound = 10 * int(pow(10, a))
    int_rule = MakeGRList(general_roman_num)
    rom_num_list = []
    for value in rom_num:
        rom_num_list.append(value)
    int_num = 0
    for value in range(len(rom_num_list) - 1):
        if int_rule[rom_num_list[value]] < int_rule[rom_num_list[value + 1]]:
            int_num = int_num - int_rule[rom_num_list[value]]
        else:
            int_num = int_num + int_rule[rom_num_list[value]]
    int_num = int_num + int_rule[rom_num_list[-1]]
    if int_num < bound:
        reve_num = GeneralIntConvertRomnum(int_num)
    else:
        return False
    if reve_num == rom_num:
        return int_num
    else:
        return False

p = split_list(p)
print(p)
p = split_list_2(p)
print(p)
p = split_list_3(p)
print(p)
# p = split_list_4(p)
# print(p)
rule_list = posibility_rule(p)
value_dic = {}
for rule in rule_list:
    general_roman_num = rule
    # print(general_roman_num)
    value = GeneralRomnumConvertInt(p1)
    # print(value)
    if value:
        value_dic[rule] = value

minimally_rule = min(value_dic, key=value_dic.get)
minimally_value = value_dic[minimally_rule]
minimally_rule = ''.join(minimally_rule)

print(value_dic)
print(minimally_rule, minimally_value)


