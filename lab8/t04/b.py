x = float(input('значення х: '))
a1 = x
an = (16 + x) / (1 + abs(a1**3))
eps = 10 ** -5
i = int(1 / eps)
for el in range(1, i + 1):
    a1 = an
    an = (16 + x) / (1 + abs(a1**3))

print(an)
