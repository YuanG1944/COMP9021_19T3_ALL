import itertools as tool
import functools as ftool
import collections as coll
def prime(n):
    isp = [True] * (n + 1)
    for i in range(2, int(n ** 0.5 + 1)):
        if isp[i]:
            for j in range(i * i, n+1, i):
                isp[j] = False
    return [x for x in range(2, n + 1) if isp[x]]

a = prime(100)
print(a)

b = [1, 2, 3, 4, 5, 6, 7, 8, 9]
bb = [b[i:i+3] for i in range(0, len(b), 3)]
print(bb)
bbb = list(map(list, zip(*bb)))
print("bbb", bbb)
bbbb = list(tool.chain.from_iterable(bbb))
print("bbbb", bbbb)
c = list(tool.combinations(bbbb, 2))
print(c)
cc = list(tool.permutations(bbbb, 2))
print(cc)
d = list(map(lambda x: (x * 2), b))
print(d)
dd = list(filter(lambda x: (x % 2 == 0), b))
print(dd)
ddd = ftool.reduce(lambda x, y: (x * y), b)
print(ddd)
e = sorted(bbb, key=lambda x: (-x[2]))
print('e = ', e)
ee = sorted(bbb, key=lambda x: (-x[2]), reverse=True)
print(ee)
b.extend([10, 11, 12])
print(b)

f = 'ABCDEFG'
print(f.lower())
print(f.upper())
print(f.capitalize())

g = 'abbbcaaabcccaaabbbbbccab'
gggg = {}
gg = [x for x, y in tool.groupby(g)]
print(gg)
ggg = [list(y) for x, y in tool.groupby(g)]
print(ggg)
h = g.split('a')
print(h)
hh = g.strip('a')
print(hh)
hh = hh.rstrip('b')
print(hh)

i = coll.defaultdict(list)
for j in range(9):
    for k in range(j):
        i[j].append(k)
print(i)
