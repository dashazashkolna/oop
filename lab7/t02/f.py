def gen(x, k):
    x0 = x
    yield x0
    for i in range(1, k+1):
        x0 *= x ** 2 / (2 * i * (2 * i + 1))
        yield x0


x = int(input('введіть значення х: '))
x0 = x
k = int(input('член послідовності: '))
for i in range(1, k+1):
    x0 *= x ** 2 / (2 * i * (2 * i + 1))

print(x0)

x0 = x
for i in gen(x, k):
    x0 = i

print(x0)
