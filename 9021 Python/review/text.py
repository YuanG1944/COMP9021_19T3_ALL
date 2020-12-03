# def prime(n):
#     flag = [1] * (n+2)
#     p = 2
#     while p <= n:
#         print(p)
#         for i in range(2 * p, n + 1, p):
#             flag[i] = 0
#         while 1:
#             p += 1
#             if flag[p] == 1:
#                 break
#
#
# #求素数
# def eratosthenes(n):
#     IsPrime = [True] * (n + 1)
#     for i in range(2, int(n ** 0.5) + 1):
#         if IsPrime[i]:
#             for j in range(i * i, n + 1, i):
#                 IsPrime[j] = False
#     return [x for x in range(2, n + 1) if IsPrime[x]]


# matrix = [''] * 3
# matrix2 = [matrix] * 3
# print(matrix)
# print(matrix2)
#
# prime(10)

# n = 10
# for num in range(n):
#     if num < 25:
#         for i in range(num + 1):
#             print(i)
#     print('\n')

# aph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# for num in range(10):
#     if num < 25:
#         temp = aph[:num]
# print(temp)

# for value in range(1):
#     aph = aph + aph
# print(aph)

# word = 'abbbcaaabcccaaabbbbbccab'
#
# result = ['']
# if word:
#     # first method
#     for x in word:
#         letters = set(result)
#         for item in result:
#             if x not in item:
#                 value = item + x
#                 letters.add(value)
#             else:
#                 value = item.replace(x, '') + x
#                 letters.add(value)
#
#         result = list(letters)
#
# print(sorted(result))
# a = [1, 2, 3, 4]
# b = [2, 3, 4, 5]
# a = set(a)
# b = set(b)
# p = a.intersection(b)
# print(p)
from functools import reduce

a = [[1, 2, 3], [1, 3, 6], [7, 8, 9]]
map(list, zip(*a))
print(a)
b = map(list, zip(*a))
print(b)

aa = [1, 2, 3, 4, 5]
k = sorted(aa, reverse=True)
print(k)

kk = sorted(a, key=lambda x: (x[0], x[1]), reverse=True)
print(kk)


# def prime(n):
#     IsPrime = [True] * (n + 1)
#     for i in range(2, int(n ** 0.5) + 1):
#         if IsPrime[i]:
#             for j in range(i * i, n + 1, i):
#                 IsPrime[j] = False
#     return [x for x in range(2, n + 1) if IsPrime[x]]


# def prime(n):
#     isp = [True] * (n + 1)
#     for i in range(2, int(n ** 0.5 + 1)):
#         if isp[i]:
#             for j in range(i * i, n + 1, i):
#                 isp[j] = False
#     return [x for x in range(2, n + 1) if isp[x]]

# def prime(n):
#     isp = [True] * (n + 1)
#     for i in range(2, int(n ** 0.5 + 1)):
#         if isp[i]:
#             for j in range(i * i, n + 1, i):
#                 isp[j] = False
#     return [x for x in range(2, n + 1) if isp[x]]

def prime(n):
    isp = [True] * (n + 1)
    for i in range(2, int(n ** 0.5 + 1)):
        if isp[i]:
            for j in range(i * i, n + 1, i):
                isp[j] = False
    return [x for x in range(2, n + 1) if isp[x]]


print(prime(100))

matrix = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89]

# new = [temp[i:i + len(square[0])] for i in range(0, len(temp), n)]

# new = [matrix[i: i + 3] for i in range(0, len(matrix), 3)]

# new = [matrix[i: i + 3] for i in range(0, len(matrix), 3)]
# print(new)
#
# rnew = list(map(list, zip(*new)))
#
# print(rnew)

# sq2 = list(map(list,zip(*square)))

# r2 = sorted(r2, key=lambda x:(int(x[0]), int(x[1])))

# w1 = 'asdbjkasd'
# w2 = 'asd'
# w3 = set(w1) - set(w2)
# print(w3)
# print(w1[:3])
import itertools as tool

xxx = [[1, 2, 3, 4], [1, 3, 6], [7, 8, 9]]
a = tool.chain.from_iterable(xxx)
a = list(a)
print(a)
new = [a[i: i + 3] for i in range(0, len(a), 3)]
print(new)

a, b = divmod(10, 3)
print(a, b)

p = bin(10)
print(p[2:])

a = [1, 2, 3, 4]
b = [2, 3, 4, 5]
a = set(a)
b = set(b)
p = a.intersection(b)
k = a.union(b)
print(p)
print(k)

a = '00 00 30 42 05 53 045'
b = a.split('0')
b = ''.join(b)
print(b)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b = [a[i:i + 2] for i in range(0, len(a), 2)]
print(b)
c = tool.chain.from_iterable(b)
print(list(c))

def m(x, y):
    return x * y
d = reduce(m, a)
print(d)

xxx = [[1, 2, 3, 4], [1, 3, 6], [7, 8, 9]]
a = tool.chain.from_iterable(xxx)
print(list(a))

# def triangles():
#     L = [1]
#     while True:
#         yield L
#         L = [0] + L + [0]
#         L = [L[i] + L[i + 1] for i in range(len(L) - 1)]
#
# n = 0
# results = []
# for t in triangles():
#     results.append(t)
#     n = n + 1
#     if n == 11:
#         break
#
# for t in results:
#     print(t)

n = 30
word = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
kk = n // 7
for value in range(kk + 1):
    word = word + word
b = 0
e = 0
for value in range(n):
    k = value + 1
    b += value
    f = word[b:b + k]
    ff = f[::-1]
    if len(f) == 1:
        print(' ' * (n - len(f)) + f)
    else:
        print(' ' * (n - len(f)) + f + ff[1:])

# height = 13
# end = 0
# end2 = 0
# f = []
# for i in range(1, height + 1):
#     end += i * 2 - 1
#     end2 += (i - 1) * 2 - 1
#     for j in range(end):
#         if j > end2:
#             a = str(j)
#             f.append(a[-1])
#     f = ''.join(f)
#     print(' ' * (height - i) + f)
#     f = []

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
new = [a[i:i+3] for i in range(0, len(a), 3)]
print(new)
new2 = list(map(list, zip(*new)))
print(new2)
new3 = tool.chain.from_iterable(new2)
print(list(new3))

a = '00 00 30 42 05 53 045'
b = a.split('0')
b = ''.join(b)
print(b)

def ppp(n):
    isp = [True] *(n + 1)
    for i in range(2, int(n ** 0.5 + 1)):
        if isp[i]:
            for j in range(i*i, n+1, i):
                isp[j] = False
    return [x for x in range(2, n+1) if isp[x]]

print(ppp(10))

a = {1,2,3}
b = {4,5,6}
c = a.intersection(b)
d = a.union(b)
print(c)
print(d)


b = [1, 2, 3, 4, 5, 6, 7, 8, 9]

bb = [b[i:i+3] for i in range(0, len(b), 3)]
print(bb)
bbb = list(map(list, zip(*bb)))
print(bbb)

def prime(n):
    isp = [True] * (n + 1)
    for i in range(2, int(n**0.5 + 1)):
        if isp:
            for j in range(i * i, n + 1, i):
                isp[j] = False
    return [x for x in range(2, n + 1) if isp[x]]