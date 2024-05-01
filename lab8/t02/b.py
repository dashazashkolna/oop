from math import log, e

x = float(input('значення х: '))
x1 = x
sn = x
eps = 10 ** -13
n = 2
while abs(x1) > eps:
    x1 *= -x * (n-1) / n
    n += 1
    sn += x1

print(sn)
print(log((1+x), e))
