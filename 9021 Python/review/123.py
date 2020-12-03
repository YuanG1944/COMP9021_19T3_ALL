from functools import reduce

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def m(x, y):
    return x * y
def k(x):
    return x * 2
b = reduce(m, a)
c = map(k, a)
d = reduce(lambda x, y: (x * y), a)
e = map(lambda x: (x * 2), a)
print(b)
print(list(c))
print(d)
print(list(e))