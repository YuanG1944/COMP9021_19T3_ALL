import itertools
import re
from math import pow

p1 = 'ete'
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
a = 'ete'

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
        print(len(key))
        if re.match(r'^([a-zA-Z])\1{0,2}$', key):
            value_dic[key] = [key[0], '_' + key[0]]
        elif len(key) == 2 and key[0] != key[1]:
            value_dic[key] = [key[1] + key[0], key[0] + key[1], '_' + key[0] + key[1], '_' + key[1] + key[0]]
        elif len(key) >= 3 and key == list[-1]:
            print('run1')
            if len(key) % 2 == 1:
                k = b_odd_condition(key)
                value_dic[key] = [k, '_' + key]
            else:
                k = b_even_condition(key)
                value_dic[key] = [k, '_' + key]
        else:
            print('run2')
            if len(key) % 2 == 1:
                k = fm_odd_condition(key)
                value_dic[key] = [k, '_' + key]
            else:
                k = fm_even_condition(key)
                value_dic[key] = [k, '_' + key]

    print(value_dic)

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


condition = split_list('brbwwqaaaZZZXCCKBOPL')
    a, b = split_1(condition)
    rom_rule = split_2(a, b)
    if rom_rule[0] == "_":
        rom_rule = rom_rule[1:]
    if rom_rule[-1] == "_":
        rom_rule = rom_rule[:-1]
    general_roman_num = rom_rule
    final_value = GeneralRomnumConvertInt(in_num3)
    if rom_rule and final_value:
        print("Sure! It is " + str(final_value) + " using " + str(rom_rule))
    else:
        print('Hey, ask me something that\'s not impossible to do!')
        exit()