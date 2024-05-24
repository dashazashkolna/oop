def gen(n):
    yield 0
    s2 = 1/2
    yield s2
    for x in range(3, n+1):
        s2 += 1 / ((x - 1) * x)
        yield s2


n = int(input('член послідовності: '))
s2 = 1/2
for x in range(3, n+1):
    s2 += 1 / ((x-1) * x)
print(s2)

s2 = 1/2
for x in gen(n):
    s2 = x
print(s2)