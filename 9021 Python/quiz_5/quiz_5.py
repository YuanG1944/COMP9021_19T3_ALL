# COMP9021 19T3 - Rachid Hamadi
# Quiz 5 *** Due Thursday Week 7
#
# Implements a function that, based on the encoding of
# a single strictly positive integer that in base 2,
# reads as b_1 ... b_n, as b_1b_1 ... b_nb_n, encodes
# a sequence of strictly positive integers N_1 ... N_k
# with k >= 1 as N_1* 0 ... 0 N_k* where for all 0 < i <= k,
# N_i* is the encoding of N_i.
#
# Implements a function to decode a positive integer N
# into a sequence of (one or more) strictly positive
# integers according to the previous encoding scheme,
# or return None in case N does not encode such a sequence.


import sys


def encode(list_of_integers):
    import re
    l = [bin(e)[2: ] for e in list_of_integers]
    encode_list = []
    encode = []
    for value in l:
        value = str(value)
        while value:
            if re.match(r'^1', value):
                encode_list.append('11')
                value = value[1:]
            if re.match(r'^0', value):
                encode_list.append('00')
                value = value[1:]
        v = ''.join(encode_list)
        encode_list = []
        encode.append(v)
    a = ''
    for value in encode:
        a += (value + '0')
    a = a[:-1]
    code = int(a, 2)
    return code
    # REPLACE pass ABOVE WITH YOUR CODE


def decode(integers):
    import re
    l = bin(integers)[2:]
    encode_list = []
    while l:
        if re.match(r'^11', l):
            encode_list.append('1')
            l = l[2:]
        if re.match(r'^00', l):
            encode_list.append('0')
            l = l[2:]
        if re.match(r'^01', l):
            encode_list.append(',')
            l = l[1:]
        if re.match(r'^10', l) or re.match(r'^1$', l) or re.match(r'^0$', l):
            return None
    encode = ''.join(encode_list)

    if "," in encode:
        code = []
        encode_list = encode.split(",")
        for value in encode_list:
            code.append(int(value, 2))
    else:
        code = []
        code.append(int(encode, 2))
    return code
    # REPLACE pass ABOVE WITH YOUR CODE


# We assume that user input is valid. No need to check
# for validity, nor to take action in case it is invalid.
print('Input either a strictly positive integer')
the_input = eval(input('or a nonempty list of strictly positive integers: '))
if type(the_input) is int:
    print('  In base 2,', the_input, 'reads as', bin(the_input)[2 :])
    decoding = decode(the_input)
    if decoding is None:
        print('Incorrect encoding!')
    else:
        print('  It encodes: ', decode(the_input))
else:
    print('  In base 2,', the_input, 'reads as',
          f'[{", ".join(bin(e)[2: ] for e in the_input)}]'
         )
    print('  It is encoded by', encode(the_input))
