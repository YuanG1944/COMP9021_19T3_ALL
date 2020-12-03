import re
# bin(the_input)[2:]
the_input = [11, 24]
def encode(list_of_integers):
    l = [bin(e)[2: ] for e in list_of_integers]
    encode_list = []
    encode = []
    for value in l:
        value = str(value)
        while value:
            if re.match(r'^1', value):
                re_a = re.match(r'^1', value)
                encode_list.append('11')
                value = value[1:]
            if re.match(r'^0', value):
                re_a = re.match(r'^0', value)
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

print(encode(the_input))

