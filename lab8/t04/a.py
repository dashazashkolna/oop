x = float(input('значення х: '))
a1 = x
an = (abs(4 * a1 ** 2 - 2 * x)) ** 0.5
i = 2
eps = 10 ** -13
while abs(an - a1) > eps:
    a1 = an
    an = (abs(4 * a1 ** 2 - 2 * x)) ** 0.5

print(an)