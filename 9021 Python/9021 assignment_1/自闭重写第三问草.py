import re
import sys
from math import pow
import itertools

num = 'IOOPPPLlkjJhHHgGGGFGDFsSSSaAAzZxCcVVVBBN'
rule_list = ['_'] * len(num)
print(rule_list)
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
        # k = len(ln)
        # while k:
        #     if loc + 1 < len(ln):
        #         if ln[loc] == ln[loc + 1]:
        #             loc += 1
        #     k -= 1
        # print(loc)
        slide = ln[:loc]
        l2.append(slide)
        ln = ln.replace(slide, '')
    if ln != '':
        l2.append(ln)
    return l2
l = split_list(num)
print(l)

def check_l(l):
    l2 = []
    for value in l:
        if re.findall(r'([A-Za-z])\1{1,2}', value):
            check_repeat = re.findall(r'([A-Za-z])\1{1,2}', value)
            l2.append(check_repeat[0])
        else:
            l2.append('')
    return l2

check_list = check_l(l)
print(check_list)
#
# # 第二步切在XXX,XX处切片
# def split_list_2(l):
#     ln = []
#     for i in l:
#         if re.findall(r'([A-Za-z])\1{1,2}', i):
#             slide1 = i[:i.index(i[-1])]
#             print(slide1)
#             slide2 = i[i.index(i[-1]):i.rindex(i[-1]) + 1]
#             print(slide2)
#             for k in slide2:
#                 if k in slide1:
#                     break
#                 else:
#                     if slide1 not in ln:
#                         ln.append(slide1)
#                     if slide2 not in ln:
#                         ln.append(slide2)
#         else:
#             if i not in ln:
#                 ln.append(i)
#     return ln

# for value in range(len(l)):



