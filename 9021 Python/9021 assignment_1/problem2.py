from math import pow
general_roman_num = 'ab'

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
    print(general_roman_num_list)
    roman_set = [general_roman_num_list[i:i + 2] for i in range(0, len(general_roman_num_list), 2)]
    last_list = roman_set[len(roman_set) - 1]
    return (len(roman_set) - 1), last_list

print(MakeGRList(general_roman_num))

print(maxLen(general_roman_num))

#做伪罗马数字表
def MakeANList(general_roman):
    a, last_list = maxLen(general_roman_num)
    general_roman_num_list = general_roman[::-1]
    print(general_roman_num_list)
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
        bound = 9 * int(pow(10, a))
    print('边界' + str(bound))
    if int_num >= bound:
        return False
    else:
        rom_rule = MakeANList(general_roman_num)
        print(rom_rule)
        num_list = []
        key = len(str(int_num))
        while key:
            print(rom_rule[key][(int_num // int(pow(10, key - 1))) % 10])
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

print(GeneralIntConvertRomnum(49269))
print(GeneralRomnumConvertInt('aba'))