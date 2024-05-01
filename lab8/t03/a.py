x = float(input('значення х: '))
x0 = 1
sn = 1
eps = 10 ** -13
n = 1
while abs(x0) > eps:
    x0 *= x ** 2 / (2 * n)
    n += 1
    sn += x0

print(sn, 'n =', n)
