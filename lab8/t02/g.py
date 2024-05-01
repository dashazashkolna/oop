x = float(input('значення х: '))
x0 = x / 2
sn = x / 2
eps = 10 ** -13
n = 2
while abs(x0) > eps:
    x0 *= -1 ** (n + 1) * (2 * n - 1) / (2 * n) * x
    n += 1
    sn += x0

print(1 + sn)
print((1+x)**0.5)
