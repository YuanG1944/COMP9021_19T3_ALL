def split_1(list):
    a = list
    b = []
    for value in a:
        print(value)
        if a.count(value) > 1:
            if value not in b:
                b.append(value + '_')
            a = a.split(value)
            print(a)
            a = ''.join(a)
            c = value
            print(c)
    if b:
        for value in a:
            if list.index(value) < list.rindex(c):
                b.append(value)
                a = a.split(value)
                a = ''.join(a)
                print(a)
        if len(b) == 1:
            b = [b[0][0]]
            print(a)
            print(b)
    return a, b

def split_2(a, b):
    final_list = []
    for value in condition:
        a, b = split_1(value)
        if condition[condition.index(value)] != condition[-1]:
            if len(b) == 1:
                #偶数
                if len(a) % 2 == 0:
                    a = fm_even_condition(a)
                else:
                    a = fm_odd_condition(a)
                    # a = '_' + a
            else:
                # 偶数
                if len(a) % 2 == 0:
                    a = fm_even_condition(a)
                    # a = '_' + a
                else:
                    a = fm_odd_condition(a)
        else:
            #偶数
            if len(b) == 1:
                if len(a) % 2 == 0:
                    a = b_even_condition(a)
                else:
                    a = b_odd_condition(a)
                    a = "_" + a
            else:
                # 偶数
                if len(a) % 2 == 0:
                    a = b_even_condition(a)
                else:
                    a = b_odd_condition(a)
                    a = "_" + a
        final_list.append(''.join(b))
        final_list.append(a)
        # final_string = ''.join(b) + a
    print(final_string)
    final_list = final_list[::-1]
    final_list2 = []
    final_list2.append(final_list[0])
    for value in range(1, len(final_list)):
        if value % 2 == 0:
            if len(final_list[value]) % 2 == 0:
                final_list[value] = "_" + final_list[value]
                final_list2.append(final_list[value])
            else:
                final_list2.append(final_list[value])
        else:
            final_list2.append(final_list[value])
    final_list2 = final_list2[::-1]
    final_list2 = "".join(final_list2)
    return final_list2

a = ['I', 'OO', 'PPPLlkjJh', 'HHg', 'GGGFGDFs', 'SSSa', 'AAzZxCc', 'VVV', 'BBN']
print(a)
print(split_1(a))