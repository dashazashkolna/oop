x = float(input('значення х: '))
x0 = x
sn = x
eps = 10 ** -13
n = 1
while abs(x0) > eps:
    x0 *= - x**2 * (2 * n - 1) / (n * (2 * n + 1))
    n += 1
    sn += x0

print(sn, "n =", n)
