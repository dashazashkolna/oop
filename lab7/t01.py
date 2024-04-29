def sqr(n):
    x = 2 ** 0.5
    yield x
    for i in range(n):
        x += 2
        x **= 0.5
        yield x


n = int(input())
x = 2 ** 0.5
for i in range(n):
    x += 2
    x **= 0.5

print(x, '\n')

s = list(sqr(n))
print(s[n])