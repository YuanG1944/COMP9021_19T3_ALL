import re
import sys
from math import pow
import itertools

in_num = input("How can I help you? ")

# in_num = "Please convert 1982"
# in_num = 'Please convert asdasdasdf minimally'
# in_num = 'Please convert VI minimally'
in_num1 = None
in_num2 = None
in_rule2 = None
in_num3 = None

# 正则判断输入格式
march_test11 = re.match(r'^Please convert [a-zA-Z]+$', in_num)
march_test12 = re.match(r'^Please convert [0-9]+$', in_num)
# print(march_test11)
# print(march_test12)
march_test21 = re.match(r'^Please convert [a-zA-Z_]+ using [a-zA-Z_]+$', in_num)
march_test22 = re.match(r'^Please convert [0-9]+ using [a-zA-Z]+$', in_num)
# print(march_test21)
# print(march_test22)
march_test3 = re.match(r'^Please convert [0-9a-zA-Z]+ minimally$', in_num)
# print(march_test3)
try:
    if march_test11 is None and march_test12 is None and march_test21 \
            is None and march_test22 is None and march_test3 is None:
        raise ValueError
except ValueError:
    print('I don\'t get what you want, sorry mate!')
    sys.exit()
#第一问判断
if march_test11 or march_test12:
    if in_num[(in_num.index('t') + 2)] == '0':
        print('Hey, ask me something that\'s not impossible to do!')
        sys.exit()
    else:
        in_num1 = in_num[(in_num.index('t') + 2):]
    # print(in_num)
    in_intnum = None
    in_romnum = None
    if not in_num1.isalpha():
        in_intnum = int(in_num1)
    else:
        in_romnum = in_num1
#第二问判断
if march_test21 or march_test22:
    if in_num[(in_num.index('t') + 2)] == '0':
        print('Hey, ask me something that\'s not impossible to do!')
        sys.exit()
    else:
        in_num2 = in_num[(in_num.index('t') + 2): (in_num.index('u') - 1)]
        in_rule2 = in_num[(in_num.index('g') + 2):]
    # print(in_num2)
    # print(in_rule2)
    for value in in_rule2:
        if in_rule2.count(value) > 1:
            print('Hey, ask me something that\'s not impossible to do!')
            sys.exit()
    in_intnum2 = None
    in_romnum2 = None
    if in_num2.find("_") != -1:
        print('Hey, ask me something that\'s not impossible to do!')
        sys.exit()
    if not in_num2.isalpha():
        in_intnum2 = int(in_num2)
    else:
        in_romnum2 = in_num2
#第三问判断
if march_test3:
    if not in_num[(in_num.index('t') + 2): (in_num.index('m') - 1)].isalpha():
        print('Hey, ask me something that\'s not impossible to do!')
        sys.exit()
    in_num3 = in_num[(in_num.index('t') + 2): (in_num.index('m') - 1)]
    # print(in_num3)


# _____________第一问主函数_____________________________________________________________________________________________________
#阿拉伯数字转罗马数字
def IntConvertRomnum(int_num):
    if int_num >= 4000:
        return False
    else:
        rom_rule = {1: ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"],
                    2: ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"],
                    3: ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"],
                    4: ["", "M", "MM", "MMM"],
                    }

        num_list = []
        num_list.append(rom_rule[4][int_num // 1000])
        num_list.append(rom_rule[3][int_num % 1000 // 100])
        num_list.append(rom_rule[2][int_num % 100 // 10])
        num_list.append(rom_rule[1][int_num % 10])

        rom_num = ""
        for num in num_list:
            rom_num = rom_num + num
        return rom_num

#罗马数字转阿拉伯数字
def RomnumConvertInt(rom_num):
    int_rule = {"I": 1,
                "V": 5,
                "X": 10,
                "L": 50,
                "C": 100,
                "D": 500,
                "M": 1000,
                }
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
    if int_num < 4000:
        reve_num = IntConvertRomnum(int_num)
    else:
        return False
    if reve_num == rom_num:
        return int_num
    else:
        return False

# _____________第二问主函数_____________________________________________________________________________________________________
#做罗马数字对应的数字表
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

#求出最大长度,和最后一组元素用来确定最大值
def maxLen(general_roman):
    general_roman_num_list = general_roman[::-1]
    # print(general_roman_num_list)
    roman_set = [general_roman_num_list[i:i + 2] for i in range(0, len(general_roman_num_list), 2)]
    last_list = roman_set[len(roman_set) - 1]
    return (len(roman_set) - 1), last_list

#做伪罗马数字表
def MakeANList(general_roman):
    a, last_list = maxLen(general_roman_num)
    general_roman_num_list = general_roman[::-1]
    # print(general_roman_num_list)
    roman_set = [general_roman_num_list[i:i+2] for i in range(0, len(general_roman_num_list), 2)]
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

#数字转罗马数字
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

#罗马数字转换阿拉伯数字
def GeneralRomnumConvertInt(rom_num):
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

# _____________第三问主函数_____________________________________________________________________________________________________
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
def split_list_4(l):
    list = []
    for value in l:
        if len(value) >= 3 and value[0] != value[-1]:
            value = value[::-1]
            k = [value[i:i + 2][::-1] for i in range(0, len(value), 2)]
            k = k[::-1]
            for val in k:
                list.append(val)
        else:
            list.append(value)
    return list

#第五步找出所有可能规则
def posibility_rule(list):
    value_dic = {}
    for value in list:
        value_dic[value] = ''

    for key, value in value_dic.items():
        # print(len(key))
        if re.match(r'^([a-zA-Z])\1{0,2}$', key):
            value_dic[key] = [key[0], '_' + key[0]]
        if len(key) == 3 and key[0] == key[-1] and key[1] != key[0]:
            value_dic[key] = [key[0] + '_' + key[1], '_' + key[0] + '_' + key[1]]
        if len(key) == 4 and key[0] == key[-1]:
            value_dic[key] = [key[1] + key[0] + '_' + key[2], key[1] + '_' + key[0] + '_' + key[2]]
        if len(key) == 2 and key[0] != key[1]:
            value_dic[key] = [key[1] + key[0], key[0] + key[1], key[1] + '_' + key[0]]
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

# _____________主程序_____________________________________________________________________________________________________
if in_num1:
    if in_intnum:
        if IntConvertRomnum(in_intnum):
            print('Sure! It is ' + str(IntConvertRomnum(in_intnum)))
        else:
            print('Hey, ask me something that\'s not impossible to do!')
    elif in_romnum:
        try:
            RomnumConvertInt(in_romnum)
        except KeyError:
            print('Hey, ask me something that\'s not impossible to do!')
            exit()
        else:
            if RomnumConvertInt(in_romnum):
                print('Sure! It is ' + str(RomnumConvertInt(in_romnum)))
            else:
                print('Hey, ask me something that\'s not impossible to do!')

if in_num2 and in_rule2:
    general_roman_num = in_rule2
    if in_intnum2:
        if GeneralIntConvertRomnum(in_intnum2):
            print('Sure! It is ' + str(GeneralIntConvertRomnum(in_intnum2)))
        else:
            print('Hey, ask me something that\'s not impossible to do!')
            exit()
    elif in_romnum2:
        try:
            GeneralRomnumConvertInt(in_romnum2)
        except KeyError:
            print('Hey, ask me something that\'s not impossible to do!')
            exit()
        else:
            if GeneralRomnumConvertInt(in_romnum2):
                print('Sure! It is ' + str(GeneralRomnumConvertInt(in_romnum2)))
            else:
                print('Hey, ask me something that\'s not impossible to do!')
                exit()
if in_num3:
    # print("开始程序3")
    in_num3ex = in_num3
    # print(in_num3ex)
    in_num3ex = split_list(in_num3ex)
    # print(in_num3ex)
    in_num3ex = split_list_2(in_num3ex)
    # print(in_num3ex)
    in_num3ex = split_list_3(in_num3ex)
    # print(in_num3ex)
    in_num3ex = split_list_4(in_num3ex)
    # print(in_num3ex)
    rule_list = posibility_rule(in_num3ex)
    # print(in_num3ex)
    #创建值字典
    value_dic = {}
    for rule in rule_list:
        general_roman_num = rule
        # print(general_roman_num)
        value = GeneralRomnumConvertInt(in_num3)
        # print(value)
        if value:
            value_dic[rule] = value
    if not value_dic:
        print('Hey, ask me something that\'s not impossible to do!')
        sys.exit()
    minimally_rule = min(value_dic, key=value_dic.get)
    minimally_value = value_dic[minimally_rule]
    if minimally_rule and minimally_value:
        print("Sure! It is " + str(minimally_value) + " using " + str(minimally_rule))
    else:
        print('Hey, ask me something that\'s not impossible to do!')
        exit()