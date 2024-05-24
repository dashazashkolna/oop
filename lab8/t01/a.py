a1, a2 = 0, 1
b1, b2 = 1, 1
s1 = 2
s2 = 4
n = int(input('член послідовності: '))
for x in range(3, n+1):
    bk = b2 + a2
    ak = a2 / x + a1 * bk
    s2 += (2 ** x / (ak + bk))
    b1, b2 = b2, bk
    a1, a2 = a2, ak

print(s2)
