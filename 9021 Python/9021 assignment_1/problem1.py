import re
import sys
from math import pow

in_num = input("How can I help you? ")

# march_test1 = re.match(r'Please convert [a-zA-Z0-9]+', in_num)
# march_test2 = re.match(r'Please convert [a-zA-Z0-9]+ by using [a-zA-Z]+', in_num)
# march_test3 = re.match(r'Please convert [a-zA-Z]+ minimally', in_num)
#
# try:
#     if not march_test1 and march_test2 and march_test3:
#         raise ValueError
# except ValueError:
#     print('I don\'t get what you want, sorry mate!')
#     sys.exit()
#
# try:
#     if not march_test1 or march_test2 or march_test3:
#         raise ValueError
# except ValueError:
#     print('I don\'t get what you want, sorry mate!')
#     sys.exit()

in_num = in_num[(in_num.index('t') + 2):]

if in_num[(in_num.index('t') + 2)] == '0':
    print('Hey, ask me something that\'s not impossible to do!')
    sys.exit()
in_intnum = None
in_romnum = None
if not in_num.isalpha():
    in_intnum = int(in_num)
else:
    in_romnum = in_num


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


if in_num:
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
