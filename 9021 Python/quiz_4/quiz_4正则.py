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
    import re
    word_in = word
    if re.match(r'^(.*?)(\,\s\,)(.*)$', word_in):
        return False
    if arity == 0:
        re_a = None
    else:
        re_a = re.match(r'^([a-zA-Z_\s]*?)((\()[a-zA-Z_\s\,\)]+)', word_in)
        if re_a is None:
            return False
    while re_a is not None:
        if arity == 1:
            re_a = re.match(r'^(.*?)((\()([a-zA-Z_\s]+)(\)))(.*)$', word_in)
        else:
            re_a = re.match(r'^(.*?)((\()(([a-zA-z_\s]+\,)+)([a-zA-Z_\s]+\)))(.*)$', word_in)
        if re_a:
            b = re_a.group(4)
            if b.count(',') == (arity - 1):
                word_in = word_in.replace(re_a.group(2), '')
            else:
                break
    re_x = re.match(r'^([a-zA-z_]+)$', word_in)
    if re_x:
        return True
    else:
        return False


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
