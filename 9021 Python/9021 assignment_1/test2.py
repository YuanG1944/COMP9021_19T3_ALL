# bb = 'jhgdazx'
# aa = 'IiknMo'
#
#
# def even_condition(l):
#     a = list(l)
#     for value in range(len(a) - 1):
#         if value % 2 == 1:
#             temp = a[value]
#             a[value] = a[value + 1]
#             a[value + 1] = temp
#     a = ''.join(a)
#     return a
#
# num1 = even_condition(aa)
#
# def odd_condition(l):
#     b = list(l)
#     for value in range(len(b) - 1):
#         if value % 2 == 0:
#             temp = b[value]
#             b[value] = b[value + 1]
#             b[value + 1] = temp
#     b = ''.join(b)
#     return b
#
# num2 = odd_condition(bb)
# print(num1, num2)

minimally_rule = 'yioplkhjdgzaxcvbbm'
minimally_rule = list(minimally_rule)
minimally_rule = ''.join(minimally_rule)

print(minimally_rule)