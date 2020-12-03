import re
the_input = 3
l = 1100111101111000000
l = str(l)
print(l)
# word_in = word_in.replace(re_a.group(2), '')
def decode(integers):
    l = bin(integers)[2:]
    print(l)
    encode_list = []
    while l:
        if re.match(r'^11', l):
            re_a = re.match(r'^11', l)
            encode_list.append('1')
            l = l[2:]
        if re.match(r'^00', l):
            re_a = re.match(r'^00', l)
            encode_list.append('0')
            l = l[2:]
        if re.match(r'^01', l):
            re_a = re.match(r'^01', l)
            encode_list.append(',')
            l = l[1:]
        if re.match(r'^10', l) or re.match(r'^1$', l):
            return None
    encode = ''.join(encode_list)

    if "," in encode:
        code = []
        encode_list = encode.split(",")
        for value in encode_list:
            code.append(int(value, 2))
    else:
        code = int(encode, 2)
    return [code]

print(decode(the_input))