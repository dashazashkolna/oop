from math import sinh

x = float(input('значення х: '))
x1 = x
sn = x
eps = 10 ** -13
n = 2
while abs(x1) > eps:
    x1 *= x ** 2 / ((2 * n - 2) * (2 * n - 1))
    n += 1
    sn += x1

print(sn)
print(sinh(x))
