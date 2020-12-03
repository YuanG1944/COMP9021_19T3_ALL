# COMP9021 19T3 - Rachid Hamadi
# Quiz 4 *** Due Thursday Week 5
#
# Prompts the user for an arity (a natural number) n and a word.
# Call symbol a word consisting of nothing but alphabetic characters
# and underscores.
# Checks that the word is valid, in that it satisfies the following
# inductive definition:
# - a symbol, with spaces allowed at both ends, is a valid word;
# - a word of the form s(w_1,...,w_n) with s denoting a symbol and
#   w_1, ..., w_n denoting valid words, with spaces allowed at both ends
#   and around parentheses and commas, is a valid word.


import sys


def is_valid(word, arity):
    # REPLACE THE RETURN STATEMENT ABOVE WITH YOUR CODE
    # wordn = word.split()
    # for value in range(1, len(wordn)):
    #     if wordn[value] == ",":
    #         continue
    #     if wordn[value] == ")":
    #         continue
    #     if wordn[value - 1].isalpha():
    #         return False
    #     else:
    #         continue
    # 去空格
    word = ''.join(word.split())
    # 拆分
    word_list = []
    puntuation_list = [',', '(', ')', '_']
    puntuation_list2 = ['_']
    # 不能连续出现两个以上的逗号
    count_comma = 0
    for value in word:
        if value == ',':
            count_comma += 1
        else:
            count_comma = 0
        if count_comma > 1:
            return False
    for value in word:
        word_list.append(value)
    for value in word_list:
        if value.isalpha() or value in puntuation_list:
            pass
        else:
            return False
    left = 0
    right = 0
    for value in word_list:
        if value == '(':
            left += 1
        if value == ')':
            right += 1
    if arity > 0 and (left == 0 or right == 0):
        return False
    if left != right:
        return False
    for value in range(len(word_list)):
        while word_list[value] == '(':
            if not word_list[value - 1].isalpha() and word_list[value - 1] not in puntuation_list2:
                return False
            else:
                break
    pop_list = []
    test_list = []
    for value in range(len(word_list)):
        pop_list.append(word_list[value])
        i = 0
        arity2 = arity
        if word_list[value] == ')':
            while arity2:
                t = pop_list.pop()
                test_list.append(t)
                if t == ',':
                    i += 1
                if t == '(':
                    break
            if i == arity2 - 1:
                continue
            else:
                return False
    # print(pop_list)
    #判段pop_list中剩下的元素
    if len(pop_list) == 0:
        return False
    if len(pop_list) == 1:
        if not pop_list[0].isalpha() and pop_list[0] not in puntuation_list2:
            return False
    else:
        for value in pop_list:
            if value.isalpha() or value in puntuation_list2:
                pass
            else:
                return False
    return True


try:
    arity = int(input('Input an arity : '))
    if arity < 0:
        raise ValueError
except ValueError:
    print('Incorrect arity, giving up...')
    sys.exit()
word = input('Input a word: ')
if is_valid(word, arity):
    print('The word is valid.')
else:
    print('The word is invalid.')

