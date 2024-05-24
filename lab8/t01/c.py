a1, a2 = 1, 1
s1 = 1
s2 = 2
k0 = 2
n = int(input('член послідовності: '))
for x in range(3, n+1):
    ak = a2 + a1 / (2 ** x)
    k0 *= x
    s2 += k0 / ak
    a1, a2 = a2, ak

print(s2)
