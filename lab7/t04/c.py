def gen(n):
    d1 = 3
    d2 = 7
    yield d1
    yield d2
    for x in range(3, n+1):
        dn = 3 * d2 - 2 * d1
        d1, d2 = d2, dn
        yield d2


d1 = 3
d2 = 7
n = int(input('член послідовності: '))
for x in range(3, n+1):
    dn = 3 * d2 - 2 * d1
    d1, d2 = d2, dn

print(d2)

d2 = 7
for x in gen(n):
    d2 = x
print(d2)
