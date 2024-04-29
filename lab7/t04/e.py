def gen(n, a):
    d1 = a
    d2 = a ** 2 - 1
    yield d1
    yield d2
    for x in range(3, n+1):
        dn = a * d2 - d1
        d1, d2 = d2, dn
        yield d2


n = int(input('член послідовності: '))
a = int(input('параметр: '))
d1 = a
d2 = a ** 2 - 1
for x in range(3, n+1):
    dn = a * d2 - d1
    d1, d2 = d2, dn

print(d2)

d2 = a ** 2 - 1
for x in gen(n, a):
    d2 = x
print(d2)