import itertools as tools
a = 'asd'
b = list(a)
print(b)
c = ''.join(b)
print(c)

a = [[1,2,3], [4,5,6]]

b = list(tools.chain.from_iterable(a))
print(b)

def prime(n):
    isp = [True] * (n + 1)
    for i in range(2, int(n ** 0.5 + 1)):
        if isp:
            for j in range(i * i, n + 1, i):
                isp[j] = False
    return [x for x in range(2, n + 1) if isp[x]]

a = [1,2,3,4,5,6,7,8,9]
b = [a[i:i+3] for i in range(0, len(a), 3)]
print(b)

a = 'sadjaskldajsdkla'
b = a[::-1]
print(a)
print(b)